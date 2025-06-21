import time
import importlib
import timeout_decorator
from typing import Dict, Any

def _slug_to_camel_case(slug: str) -> str:
    """Converts a kebab-case slug like 'two-sum' to 'twoSum'."""
    parts = slug.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def _execute_solution(slug: str, inputs: Dict[str, Any]) -> Any:
    """
    Dynamically imports the solution module and executes its main function.
    """
    module_name = _slug_to_camel_case(slug)
    try:
        module_path = f"problemFunctions.{module_name}"
        module = importlib.import_module(module_path)
    except ImportError as e:
        raise Exception(f"Could not import solution for '{slug}'. Make sure '{module_path.replace('.', '/')}.py' exists.") from e

    if not hasattr(module, 'main'):
        raise Exception(f"Solution module for '{slug}' does not have a 'main' function.")

    return module.main(**inputs)

# We can keep the timeout decorator for safety
@timeout_decorator.timeout(2, use_signals=False)
def _timed_execute(slug: str, inputs: Dict[str, Any]) -> Any:
    return _execute_solution(slug, inputs)

def safe_exec(slug: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes the main function for a given slug with a 2-second timeout.
    """
    start_time = time.time()
    try:
        result = _timed_execute(slug, inputs)
        exec_ms = int((time.time() - start_time) * 1000)
        return {
            "status": "OK",
            "stdout": str(result), # The result from main() is the stdout
            "stderr": "",
            "exec_ms": exec_ms,
        }
    except timeout_decorator.TimeoutError:
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