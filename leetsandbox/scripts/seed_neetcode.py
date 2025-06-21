# This script is a placeholder for a future feature where we would
# scrape or fetch problems from an external source like NeetCode
# and use them to populate the `backend/problems.py` file.

import os

def seed():
    print("Attempting to seed problems...")
    # In a real implementation, this would involve:
    # 1. Fetching data from an API or scraping a website.
    # 2. Transforming the data into the desired format.
    # 3. Generating the Python code for the PROBLEMS dictionary.
    # 4. Writing that code to `backend/problems.py`.
    
    # For now, we just confirm that the problems file exists.
    problems_path = os.path.join(os.path.dirname(__file__), '..', 'backend', 'problems.py')
    if os.path.exists(problems_path):
        print(f"'{os.path.relpath(problems_path)}' already exists. Nothing to do.")
    else:
        print(f"Error: '{os.path.relpath(problems_path)}' not found.")

if __name__ == "__main__":
    seed() 