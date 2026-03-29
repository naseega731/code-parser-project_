import ast
import re

class ErrorDetector(ast.NodeVisitor):

    def __init__(self):
        self.errors = []

    def visit_FunctionDef(self, node):

        # Check function name (snake_case)
        if not re.match(r'^[a-z_]+$', node.name):
            self.errors.append(f"Function name '{node.name}' should be snake_case")

        # Check number of arguments
        if len(node.args.args) > 5:
            self.errors.append(f"Function '{node.name}' has too many arguments")

        # Check function length
        length = node.end_lineno - node.lineno
        if length > 40:
            self.errors.append(f"Function '{node.name}' is too long")

        self.generic_visit(node)


def detect_errors(code):

    try:
        tree = ast.parse(code)

        detector = ErrorDetector()
        detector.visit(tree)

        return detector.errors

    except Exception as e:
        return [f"Error while detecting issues: {e}"]