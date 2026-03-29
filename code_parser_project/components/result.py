import reflex as rx
from code_parser_project.state import State

def result_section():
    return rx.box(
        rx.vstack(
            rx.heading("AI Suggestions", color="#ff00cc"),

            # 🔥 Error message
            rx.text(State.result, color="white"),

            # 🔥 Optimized code section (SAFE)
            rx.cond(
                State.optimized_code,
                rx.box(
                    rx.heading("Optimized Code", color="#00ffff"),
                    rx.code_block(State.optimized_code),
                ),
                rx.text("")  # fallback (important)
            ),

            spacing="4"
        ),
        padding="2em",
        border_radius="15px",
        background="linear-gradient(135deg, #1a0033, #000033)",
        width="100%"
    )