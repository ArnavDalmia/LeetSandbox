import time
import importlib
import asyncio
from typing import Dict, Any

def _slug_to_camel_case(slug: str) -> str: #copied function for format
    #Converts a kebab-case slug like 'two-sum' to 'twoSum'
    parts = slug.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def _execute_solution(slug: str, inputs: Dict[str, Any]) -> Any:
    # Synchronously imports and runs the solution's main function. This function is designed to be run in a separate thread.
    
    module_name = _slug_to_camel_case(slug)
    try:
        module_path = f"problemFunctions.{module_name}"
        module = importlib.import_module(module_path) # represents the solution code
    except ImportError as e:
        raise Exception(f"Could not import solution for '{slug}'. Make sure '{module_path.replace('.', '/')}.py' exists.") from e

    if not hasattr(module, 'main'):
        raise Exception(f"Solution module for '{slug}' does not have a 'main' function.")

    return module.main(**inputs)


async def safe_exec(slug: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
    #runs the main function for a given problem/slug with a 2-second timeout using asyncio
    
    start_time = time.time()
    try:
        # Run the synchronous (blocking) solution in a separate thread to avoid
        # freezing the server, and apply a timeout to the operation.
        result = await asyncio.wait_for(
            asyncio.to_thread(_execute_solution, slug, inputs),
            timeout=2.0
        )
        exec_ms = int((time.time() - start_time) * 1000)
        return {
            "status": "OK",
            "stdout": str(result),
            "stderr": "",
            "exec_ms": exec_ms,
        }
    except asyncio.TimeoutError:
        return {
            "status": "ERROR",
            "stderr": "Execution timed out after 2 seconds.",
            "stdout": "",
            "exec_ms": 2000,
        }
    except Exception as e:
        exec_ms = int((time.time() - start_time) * 1000)
        return {
            "status": "ERROR",
            "stderr": repr(e),
            "stdout": "",
            "exec_ms": exec_ms,
        } 