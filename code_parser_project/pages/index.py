import reflex as rx

from code_parser_project.components.navbar import navbar
from code_parser_project.components.hero import hero
from code_parser_project.components.footer import footer
from code_parser_project.components.code_input import code_input
from code_parser_project.components.result import result_section


def index():
    return rx.vstack(
        navbar(),
        hero(),
        code_input(),      
        result_section(),  
        footer(),
        spacing="5"
    )