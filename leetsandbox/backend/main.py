from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, List, Optional

# Use absolute imports for clarity and robustness
from backend.runner import safe_exec
from backend.problems import PROBLEMS

app = FastAPI()

# Configure CORS to allow the frontend to communicate with the backend.
# This is crucial for local development from file:// or a different port.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In a real production app, restrict this to the frontend domain
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


# Pydantic models for type-safe request and response bodies
class ProblemInfo(BaseModel):
    slug: str
    params: Dict[str, str]
    number: Optional[int] = None


class RunRequest(BaseModel):
    slug: str
    inputs: Dict[str, Any]


class RunResponse(BaseModel):
    status: str
    stdout: str
    stderr: str
    exec_ms: int


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

    # The runner is now async, so we must await its result
    result_dict = await safe_exec(request.slug, request.inputs)
    return RunResponse(**result_dict) 