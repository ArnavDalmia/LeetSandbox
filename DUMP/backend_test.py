import requests
import json

# The URL for your local running FastAPI server
API_URL = "https://leetsandbox-api.onrender.com/problems"
EXPECTED_PROBLEMS = ["two-sum", "reverse-string"]

def run_test():
    """
    Connects to the API, fetches the list of problems, and checks if it's valid.
    """
    print(f"▶️  Attempting to connect to API at {API_URL}...")

    try:
        response = requests.get(API_URL, timeout=5)
    except requests.ConnectionError:
        print("❌ TEST FAILED: Connection could not be established.")
        print("   Please ensure the backend server is running via `make dev` or your dev script.")
        return
    except requests.Timeout:
        print("❌ TEST FAILED: Connection timed out.")
        return

    if response.status_code != 200:
        print(f"❌ TEST FAILED: Received a bad status code: {response.status_code}")
        print(f"   Response body: {response.text}")
        return
    
    print("✅ Connection successful (Status 200 OK).")

    try:
        problems = response.json()
    except json.JSONDecodeError:
        print("❌ TEST FAILED: Response was not valid JSON.")
        return
    
    if not isinstance(problems, list):
        print("❌ TEST FAILED: API response was not a list.")
        return
    
    print(f"✅ API returned a list with {len(problems)} problem(s).")

    # Check if the expected problems are present
    loaded_slugs = [p['slug'] for p in problems]
    all_found = True
    for expected in EXPECTED_PROBLEMS:
        if expected not in loaded_slugs:
            print(f"❌ TEST FAILED: Expected problem '{expected}' was not found in the API response.")
            all_found = False
    
    if all_found:
        print("✅ All expected problems were found.")
        print("\n🎉 All tests passed! The API is loading problems correctly.")
    else:
        print(f"\n💥 One or more tests failed. Found problems: {loaded_slugs}")


if __name__ == "__main__":
    run_test() 