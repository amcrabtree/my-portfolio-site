import reflex as rx

@rx.page(route="/contact")
def contact_page() -> rx.Component:
    return rx.box(
        rx.text("Hello")
    )