import reflex as rx
from code_parser_project.state import State


def code_input():
    return rx.vstack(

        # -------- AI SELECT DROPDOWN --------
        rx.select(
            ["openai", "grok"],
            value=State.selected_ai,
            on_change=State.set_selected_ai,
            placeholder="Select AI",
            width="200px"
        ),

        # -------- CODE INPUT BOX --------
        rx.text_area(
            placeholder="Paste your code here...",
            value=State.code,
            on_change=State.set_code,
            width="100%",
            height="200px"
        ),

        # -------- ANALYZE BUTTON --------
        rx.button(
            "Analyze Code",
            on_click=State.analyze_code,
            width="100%",
            color_scheme="blue"
        ),

        spacing="4",
        width="100%"
    )