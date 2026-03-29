import ast

def analyze_and_fix(code):
    try:
        tree = ast.parse(code)
        formatted = ast.unparse(tree)
        return f"No errors ✅\n\n{formatted}"
    except Exception as e:
        return f"Error ❌: {e}"