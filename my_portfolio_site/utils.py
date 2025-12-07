import reflex as rx

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
            as_="a",
            font_size=text_sizing,
            size="4",
            color_scheme="blue",
            _hover={
                "background_color": dark_font_color,
                "color": "lightblue",
                "cursor": "pointer"
            },
        ),
        href=href,  
    )


def learn_more_button(href: str, text_sizing: list=smaller_text_font_sizing):
    return rx.link(
        rx.button(
            "Learn More", 
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