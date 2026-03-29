import reflex as rx

def navbar():
    return rx.box(
        rx.hstack(
            rx.text(
                "AI Code Reviewer",
                font_size="20px",
                font_weight="bold",
            ),

            rx.spacer(),

            rx.hstack(
                rx.link("Home", href="/"),
                rx.link("Review Code", href="#"),
                rx.link("About", href="#"),
                spacing="5",
            ),

            width="100%",
        ),
        bg="linear-gradient(90deg, #0d001a, #1a0033)",
        padding="1em",
        width="100%",
    )