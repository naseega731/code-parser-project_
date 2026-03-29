import reflex as rx

def footer():
    return rx.vstack(
        rx.text("© 2026 AI Code Reviewer"),
        rx.text("Built with Reflex"),
        padding="1em",
        bg="lightgray"
    )