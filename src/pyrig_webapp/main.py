"""Project entry point."""

import reflex as rx


def index() -> rx.Component:
    """A simple page."""
    return rx.el.p("Hello, World!")


app = rx.App()
app.add_page(index)
