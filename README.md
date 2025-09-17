# 🏖️ LeetSandbox

**The playground where you test, learn, and master LeetCode problems on your own terms.**

## Why LeetSandbox?

Ever been stuck on a LeetCode problem because the 1-2 example test cases just weren't enough? Wondered what happens with edge cases but had no way to test them without spoiling the solution? 

That's exactly why LeetSandbox exists.

Sometimes LeetCode problems only show you a couple of basic examples, leaving you guessing about edge cases and constraints. When you're trying to understand the problem deeply (not just memorize someone else's solution), you need the freedom to test your own scenarios. You want to identify patterns yourself, formulate algorithms in your head, and *actually learn* - not just copy-paste solutions.

LeetSandbox gives you that playground. Pick any problem, create dozens of custom test cases, and instantly see the expected output from hidden reference solutions. No login required, no data saved, just pure learning through experimentation.

**Features:**
- 🧪 **Custom Test Cases** - Create unlimited test cases beyond the basic examples
- ⚡ **Instant Results** - Get immediate feedback from optimized reference solutions  
- 🤖 **Built-in AI Tutor** - Get hints and explanations when you're stuck
- 🎯 **Pattern Recognition** - Test edge cases to understand problem constraints
- 📚 **30+ Problems** - Curated collection of essential LeetCode problems
- 🚀 **Zero Setup** - No accounts, no saving, just start testing

## 🚀 Quick Start (Use the Live Tool)

Just visit the deployed version and start testing! *(Add your deployment URL here)*

## 🛠️ Local Development Setup

Want to run LeetSandbox locally or contribute? Here's how:

1.  **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

2.  **Activate it:**
    *   On Windows: `.\\venv\\Scripts\\activate`
    *   On macOS/Linux: `source venv/bin/activate`

3.  **Install dependencies:**
    ```sh
    pip install -r leetsandbox/requirements.txt
    ```

4.  **Set up environment variables:**
    ```sh
    # Copy and configure your OpenAI API key for the AI tutor feature
    cp .env.example .env
    # Edit .env and add your OPENAI_API_KEY
    ```

5.  **Run the database seed script:**
    ```sh
    .\scripts\seed.bat
    ```

6.  **Start the development server:**
    ```sh
    make dev
    # OR
    .\scripts\dev.bat
    ```

7.  **Open the frontend:**
    - Install the Live Server extension in VS Code
    - Open `leetsandbox/frontend/index.html` with Live Server
    - Navigate to the provided local URL (usually `http://127.0.0.1:5500`)

## 🤝 Contributing

Found this helpful? Want to add more problems or improve the experience?

**Fork this repo and:**
- Add new problem functions to `problemFunctions/`
- Update the `PROBLEMS` dictionary in `backend/problems.py`  
- Improve the frontend UI/UX
- Add better error handling or performance optimizations

Pull requests are welcome! This tool was built to help people learn, so any improvements that make learning easier are appreciated.

## 📜 License

MIT License - feel free to use this for your own learning or teaching!

---

*Built with ❤️ for developers who learn by doing. If this tool helps you land that dream job, send me a message - I'd love to hear about it!*