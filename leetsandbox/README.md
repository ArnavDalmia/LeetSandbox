# LeetSandbox

A learning tool that lets users pick a LeetCode-style problem, enter their own test-case inputs in a type-safe form, click Run, and instantly see the output produced by a hidden reference **Python 3.12** solution.

## Quick Start

1.  Create a virtual environment:
    ```sh
    python -m venv venv
    ```
2.  Activate it:
    *   On Windows: `.\\venv\\Scripts\\activate`
    *   On macOS/Linux: `source venv/bin/activate`
3.  Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4.  Run the database seed script (currently a placeholder):
    ```sh
     .\scripts\seed.bat
    ```
5.  Start the development server:
    ```sh
    make dev OR .\scripts\dev.bat
    ```
6.  Open the frontend in your browser. Install Live Server and open index.html with Live Server