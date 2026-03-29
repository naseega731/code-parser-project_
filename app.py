import reflex as rx

from code_parser_project.pages.index import index
from code_parser_project.state import State

app = rx.App(state=State)

app.add_page(index)