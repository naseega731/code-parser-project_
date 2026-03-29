from code_parser_project.code_parser import parse_code
from ai_suggester import get_ai_feedback
from error_detector import detect_errors

if __name__ == "__main__":
    print("Enter your Python code (type END to finish):")

    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)

    user_code = "\n".join(lines)

    # Parse and format code
    formatted_code = parse_code(user_code)

    print("\nFormatted Code:\n")
    print(formatted_code)

    # Detect style errors
    errors = detect_errors(formatted_code)

    print("\nDetected Errors:\n")
    if errors:
        for err in errors:
            print("-", err)
    else:
        print("No errors detected")

    # Get AI suggestions
    feedback = get_ai_feedback(formatted_code)

    print("\nAI Suggestions:\n")
    print(feedback)