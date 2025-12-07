import reflex as rx
from my_portfolio_site.styles import Colors, FontSizes, Spacing
from my_portfolio_site.utils import (
    navbar_dropdown,
    contact_form,
)


@rx.page(route="/contact")
def contact_page() -> rx.Component:
    return rx.box(
        navbar_dropdown(),
        rx.vstack(
            rx.heading(
                "Contact",
                size=FontSizes.SECTION_HEADER,
                text_align="center",
                margin_bottom="1rem",
                color=Colors.TEXT,
            ),
            rx.text(
                "We'd love to hear about your lab's needs!",
                font_size=FontSizes.MAIN_TEXT,
                font_style="italic",
                text_align="center",
                max_width="800px",
                color=Colors.TEXT,
            ),
            rx.hstack(
                rx.icon("mail", color=Colors.JADE, size=FontSizes.ICON),
                rx.text("contact@biodataworks.com", color=Colors.TEXT, font_size=FontSizes.MAIN_TEXT,),
                padding_bottom=Spacing.SECTION_BOTTOM,
            ),
            contact_form(),
            padding=Spacing.PAGE_TOP,
            align="center",
        ),
        background_color=Colors.BACKGROUND,
    )