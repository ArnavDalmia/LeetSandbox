@echo off
echo Starting development server...
uvicorn backend.main:app --reload --port 8001
```

3. Run it from the leetsandbox directory:
```sh
.\scripts\dev.bat
```

This will:
- Start a development server on port 8001 (matching the README)
- Enable auto-reload when code changes
- Serve your FastAPI application from the `backend.main:app` entry point

The `--reload` flag is useful during development as it automatically restarts the server when you make code changes.// filepath: c:\Users\arnav\Documents\GitHub\LeetSandbox\leetsandbox\scripts\dev.bat
@echo off
echo Starting development server...
uvicorn backend.main:app --reload --port 8001
```

3. Run it from the leetsandbox directory:
```sh
.\scripts\dev.bat
```

This will:
- Start a development server on port 8001 (matching the README)
- Enable auto-reload when code changes
- Serve your FastAPI application from the `backend.main:app` entry point

The `--reload` flag is useful during development as it automatically restarts the server when you make code changes.