#!/usr/bin/env python3
"""
Direct OpenAI API test script
Tests your OpenAI API key directly without needing the backend
"""

import openai
import sys

# HARDCODE YOUR API KEY HERE

def test_openai_api():
    """Test OpenAI API directly with a sample coding problem question"""
    
    print("OpenAI API Key Test")
    print("=" * 50)
    print(f"API Key: {OPENAI_API_KEY[:10]}...{OPENAI_API_KEY[-4:] if len(OPENAI_API_KEY) > 14 else 'INVALID'}")
    print("-" * 50)
    
    # Check if API key looks valid
    if not OPENAI_API_KEY.startswith("sk-") or len(OPENAI_API_KEY) < 20:
        print("❌ API Key format looks invalid. Should start with 'sk-' and be longer.")
        return False
    
    try:
        # Initialize OpenAI client
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        
        # Test with a simple coding problem question
        problem_context = """
Problem: TwoSum
LeetCode Number: 1
Parameters: {"nums": "List[int]", "target": "int"}
LeetCode Link: https://leetcode.com/problems/two-sum/description/

You are an expert coding tutor helping a student understand t   his problem. 
The student is asking: "Can you explain the brute force approach for this problem?"

Please provide a helpful, educational response that:
1. Explains the problem clearly
2. Discusses the approach and algorithm
3. Provides insights about time/space complexity when relevant
4. Gives hints rather than direct solutions when appropriate
5. Is encouraging and educational

Keep your response concise but comprehensive, and focus on helping the student learn.
"""
        
        print("Sending request to OpenAI...")
        print("Question: Can you explain the brute force approach for TwoSum?")
        print("-" * 50)
        
        response = client.responses.create(
            model="o4-mini",
            tools=[{"type": "web_search"}],
            input="You are an expert coding tutor specializing in algorithm problems and data structures. Here is the context : " + problem_context
        )
        
        #ai_response = response.choices[0].message.content
        ai_response = response.output_text
        print("✅ API Key works!")
        print(f"Response: {ai_response}")
        print("-" * 50)
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'Unknown'}")
        
        return True
        
    except openai.AuthenticationError as e:
        print(f"❌ Authentication failed: {e}")
        print("Check if your API key is correct and has sufficient credits.")
        return False
        
    except openai.RateLimitError as e:
        print(f"❌ Rate limit exceeded: {e}")
        print("You may have hit your API usage limits.")
        return False
        
    except openai.APIError as e:
        print(f"❌ API Error: {e}")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    print("LeetSandbox OpenAI API Test")
    print("=" * 50)
    
    if OPENAI_API_KEY == "sk-your-openai-api-key-here":
        print("❌ Please edit this file and replace the API key!")
        print("1. Open test_chat.py")
        print("2. Find the line: OPENAI_API_KEY = \"sk-your-openai-api-key-here\"")
        print("3. Replace with your actual API key from https://platform.openai.com/api-keys")
        sys.exit(1)
    
    success = test_openai_api()
    
    if success:
        print("\n🎉 Your OpenAI API key is working perfectly!")
        print("\nNext steps:")
        print("1. Set the same API key in your .env file for the backend")
        print("2. Start your backend: uvicorn backend.main:app --reload --port 8001")
        print("3. Test the full chat feature in your browser")
    else:
        print("\n❌ API key test failed.")
        print("Make sure:")
        print("1. Your API key is correct")
        print("2. You have credits in your OpenAI account")
        print("3. Your API key has the right permissions")
        sys.exit(1)
