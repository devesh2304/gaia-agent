from smolagents import tool
import subprocess
import json

@tool
def web_search(query: str) -> str:
    """Search the web for information about a query.
    
    Args:
        query: The search query string
    """
    from huggingface_hub import InferenceClient
    return f"Search result placeholder for: {query}. In production, connect a real search API here."

@tool
def run_python(code: str) -> str:
    """Execute Python code and return the output.
    
    Args:
        code: Python code to execute
    """
    try:
        result = subprocess.run(
            ["python3", "-c", code],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
    except subprocess.TimeoutExpired:
        return "Error: Code execution timed out"
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression safely.
    
    Args:
        expression: A mathematical expression like '2 + 2' or '100 * 0.15'
    """
    try:
        allowed = set("0123456789+-*/().,% ")
        if not all(c in allowed for c in expression):
            return "Error: Invalid characters in expression"
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"