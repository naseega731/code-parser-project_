import reflex as rx

config = rx.Config(
    app_name="code_parser_project",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)