import reflex as rx

def hero():
    return rx.box(
        rx.vstack(
            rx.heading(
                "Review Your Code with AI",
                size="8",
                color="white"
            ),
            rx.text(
                "Detect bugs, improve code, and get suggestions instantly",
                color="white",
                opacity="0.8"
            ),
            rx.button(
                "Start Reviewing",
                background="linear-gradient(90deg, #ff00cc, #3333ff)",
                color="white",
                _hover={"opacity": 0.8}
            ),
            spacing="4",
            align="center"
        ),
        padding="3em",
        border_radius="15px",
        background="linear-gradient(135deg, #1a0033, #330066, #000033)",
        width="100%"
    )