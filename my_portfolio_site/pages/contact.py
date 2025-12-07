import reflex as rx
from my_portfolio_site.utils import navbar_dropdown, contact_form

# Font sizing
section_header_sizing = rx.breakpoints(initial="5", sm="6", md="7", lg="8",)
services_header_sizing = rx.breakpoints(initial="3", sm="4", md="5", lg="6",)
main_text_font_sizing = ["1.3em", "1.4em", "1.4em"]
smaller_text_font_sizing = ["1.0em", "1.1em", "1.3em"]


@rx.page(route="/contact")
def contact_page() -> rx.Component:
    return rx.box(
        navbar_dropdown(),
        rx.vstack(
            rx.heading(
                "Contact",
                font_size="2.5rem",
                font_weight="700",
                text_align="center",
                margin_bottom="1rem",
            ),
            rx.text(
                "We'd love to hear about your lab’s needs!",
                font_size=main_text_font_sizing,
                font_style="italic",
                text_align="center",
                max_width="800px",
                margin_x="auto",
                margin_bottom="3rem",
            ),
            contact_form(),
            padding_top="7em",
            align="center",
        ),
    )