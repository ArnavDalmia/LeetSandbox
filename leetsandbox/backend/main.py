from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
import os
from dotenv import load_dotenv
import openai

from backend.runner import safe_exec
from backend.problems import PROBLEMS

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()
#models setup
# Configure CORS to allow the frontend to communicate with the backend for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins for debugging, can switch later once everyting works
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


# Pydantic models for type-safe request and response bodies
class ProblemInfo(BaseModel):
    slug: str
    params: Dict[str, str]
    number: Optional[int] = None
    originLeetCode: bool
    link: Optional[str] = None


class RunRequest(BaseModel):
    slug: str
    inputs: Dict[str, Any]


class RunResponse(BaseModel):
    status: str
    stdout: str
    stderr: str
    exec_ms: int


class ChatRequest(BaseModel):
    problem_slug: str
    message: str


class ChatResponse(BaseModel):
    response: str
    status: str


@app.get("/problems", response_model=List[ProblemInfo])
async def get_problems():
    """
    Returns a list of available problems, including their slugs and
    parameter definitions, so the frontend can build submission forms.
    """
    return [
        {
            "slug": slug,
            "params": data["params"],
            "number": data.get("number"),
            "originLeetCode": data.get("originLeetCode", False),
            "link": data.get("link"),
        }
        for slug, data in PROBLEMS.items()
    ]


@app.post("/run", response_model=RunResponse)
async def run_code(request: RunRequest):
    """
    Receives a problem slug and user inputs, retrieves the corresponding
    solution code, executes it safely, and returns the result.
    """
    problem_data = PROBLEMS.get(request.slug)
    if not problem_data:
        return RunResponse(
            status="ERROR",
            stdout="",
            stderr=f"Problem '{request.slug}' not found.",
            exec_ms=0,
        )

    result_dict = await safe_exec(request.slug, request.inputs)
    return RunResponse(**result_dict)


@app.post("/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    """
    Chat endpoint that provides AI-powered explanations for coding problems.
    The AI has full context about the current problem being worked on.
    """
    try:
        # Get problem details
        problem_data = PROBLEMS.get(request.problem_slug)
        if not problem_data:
            return ChatResponse(
                response="Sorry, I couldn't find information about this problem.",
                status="error"
            )
        
        # Build problem context for the AI
        problem_context = f"""
Problem: {request.problem_slug}
LeetCode Number: {problem_data.get('number', 'N/A')}
Parameters: {problem_data.get('params', {})}
LeetCode Link: {problem_data.get('link', 'N/A')}

You are an expert coding tutor helping a student understand this specific LeetCode problem. 
The student is asking: "{request.message}"

IMPORTANT RULES:
1. ONLY answer questions related to this LeetCode problem. If the user asks about anything else (general programming, other topics, etc.), respond with: "I'm sorry, unfortunately I'm here to help with LeetCode problems only. For any general inquiries, please ask someone else."

2. Answer the user's specific question directly and concisely. Don't give a full problem explanation unless they specifically ask for "Help" or want a complete overview.

3. If the user says "Help" or asks for a general explanation, explain the solution approach and algorithm (not the code) - how it's supposed to work conceptually.

4. Be direct and focused - don't over-explain unless specifically asked.

5. Keep responses concise and to the point.

6. If the user asks for a specific approach or algorithm, explain it in a way that's easy to understand and follow.

7. Encourage the student to think through the problem and try to solve it themselves. Don't give them the solution directly. Feel free to give them hints.

8. Based on the user's questions and difficulty, give them custom testcases to try.
"""
        
        # Call OpenAI API
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.responses.create(
            model="o4-mini",
            tools=[{"type": "web_search"}],
            input="You are an expert coding tutor specializing in algorithm problems and data structures. Here is the context : " + problem_context
        )
        
        ai_response = response.output_text
        
        return ChatResponse(
            response=ai_response,
            status="success"
        )
        
    except Exception as e:
        return ChatResponse(
            response=f"Sorry, I encountered an error: {str(e)}",
            status="error"
        ) 