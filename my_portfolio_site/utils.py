import reflex as rx
import requests
import os
from dotenv import load_dotenv

load_dotenv()

MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_FROM = os.getenv("MAILGUN_FROM")
MAILGUN_TO = os.getenv("MAILGUN_TO")

dark_font_color = "#183E43"
smaller_text_font_sizing = ["1.0em", "1.1em", "1.3em"]


def circle_image(src: str, size=["150px", "150px", "200px"]):
    return rx.image(
        src=src,
        border_radius="50%",
        box_shadow="0 0 10px rgba(0,0,0,0.3)",
        width=size,
        height=size,
        object_fit="cover",
    )


def contact_button(href: str, text_sizing: list=smaller_text_font_sizing):
    return rx.link(
        rx.button(
            "Contact Us", 
            as_="a",
            font_size=text_sizing,
            size="4",
            color_scheme="teal",
            variant="outline",
            _hover={
                "background_color": dark_font_color,
                "color": "lightblue",
                "cursor": "pointer"
            },
        ),
        href=href,  
    )


def get_started_button(href: str, text_sizing: list=smaller_text_font_sizing):
    return rx.link(
        rx.button(
            "Get Started", 
            font_size=text_sizing,
            size="4",
            color_scheme="teal", 
            _hover={
                "background_color": dark_font_color,
                "color": "lightblue",
                "cursor": "pointer"
            },
        ),
        href=href,  
    )


def about_me_button(href: str, text_sizing: list=smaller_text_font_sizing):
    return rx.link(
        rx.button(
            "About Me", 
            font_size=text_sizing,
            size="4",
            color_scheme="teal", 
            #variant="outline",
            _hover={
                "background_color": dark_font_color,
                "color": "lightblue",
                "cursor": "pointer"
            },
        ),
        href=href,  
    )


def case_study_button(href: str, text_sizing: list=smaller_text_font_sizing):
    return rx.link(
        rx.button(
            "See a Case Study", 
            font_size=text_sizing,
            size="4",
            color_scheme="blue", 
            variant="outline",
            _hover={
                "background_color": dark_font_color,
                "color": "lightblue",
                "cursor": "pointer"
            },
        ),
        href=href,  
    )


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="5", weight="bold", color=dark_font_color), href=url)


def navbar_dropdown(home_href: str="/", services_href: str="/services", contact_href: str="/contact", about_href: str="/about") -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/biodataworks_logo_smallest.png",
                        width="3em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("BioDataWorks", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", home_href),
                    navbar_link("Pricing", services_href),
                    navbar_link("Contact", contact_href),
                    navbar_link("About", about_href),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/biodataworks_logo_smallest.png", width="25px", height="25px", border_radius="25%"
                    ),
                    rx.heading("BioDataWorks", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.link(rx.menu.item("Home"), href=home_href),
                        rx.link(rx.menu.item("Pricing"), href=services_href),
                        rx.link(rx.menu.item("Contact"), href=contact_href),
                        rx.link(rx.menu.item("About"), href=about_href),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("teal"),
        font_color="white",
        padding="1em",
        width="100%",
        position="fixed",
    )


class ContactState(rx.State):
    message_sent: bool = False
    submitting: bool = False
    error_message: str = ""

    def submit_form(self, form_data):
        self.submitting = True
        self.error_message = ""

        first_name = form_data.get("first_name", "")
        last_name = form_data.get("last_name", "")
        email = form_data.get("email", "")
        message = form_data.get("message", "")

        full_name = f"{first_name} {last_name}".strip()

        try:
            response = requests.post(
                f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
                auth=("api", MAILGUN_API_KEY),
                data={
                    "from": f"{full_name} <{MAILGUN_FROM}>",
                    "to": MAILGUN_TO,
                    "subject": "New Contact Form Submission",
                    "text": f"Name: {full_name}\nEmail: {email}\n\nMessage:\n{message}",
                },
                timeout=10,
            )

            if response.status_code == 200:
                self.message_sent = True
            else:
                self.error_message = "Hmm… something went wrong. Please try again later."

        except Exception:
            self.error_message = "Unable to send message right now."
        finally:
            self.submitting = False


def form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(placeholder=placeholder, type=type),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
    )


def contact_form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="mail-plus", size=32),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading("Send us a message", size="4", weight="bold"),
                    rx.text("Fill the form to contact us", size="2"),
                    spacing="1",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field("First Name", "First Name", "text", "first_name"),
                        form_field("Last Name", "Last Name", "text", "last_name"),
                        spacing="3",
                        flex_direction=["column", "row", "row"],
                    ),
                    rx.flex(
                        form_field("Email", "researcher@university.edu", "email", "email"),
                        flex_direction=["column", "row", "row"],
                    ),
                    rx.flex(
                        rx.text(
                            "Message",
                            style={
                                "font-size": "15px",
                                "font-weight": "500",
                                "line-height": "35px",
                            },
                        ),
                        rx.text_area(
                            placeholder="Message",
                            name="message",
                            resize="vertical",
                            width="500px",
                            height="150px",
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.submit(
                        rx.button("Submit",
                            loading=ContactState.submitting,
                            disabled=ContactState.submitting,
                        ),
                        as_child=True,
                    ),

                    rx.cond(
                        ContactState.message_sent,
                        rx.text("Thanks! We’ll be in touch soon.", color="#50C878", font_size=smaller_text_font_sizing),
                        rx.cond(
                            ContactState.error_message != "",
                            rx.text(ContactState.error_message, color="red"),
                        ),
                    ),

                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=ContactState.submit_form,
                reset_on_submit=True,
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )

