import reflex as rx
from my_portfolio_site.styles import Colors, FontSizes, Spacing
from my_portfolio_site.utils import (
    navbar_dropdown,
    download_cv_button,
    circle_image,
    linkedin_link, github_link, youtube_link
)

def youtube_thumbnail(src: str, width="300px"):
    return rx.image(
        src=src, 
        alt="Image with curved border",
        width=width,
        height="auto",
        border_radius="10px",  # Adjust this value for desired curvature
        border="2px solid #333",  # Optional: Add a solid border line
        box_shadow="0px 4px 8px rgba(0, 0, 0, 0.1)", # Optional: Add a subtle shadow
    )

# ---------- Section components ----------
def about_biodataworks():
    return rx.box(
        rx.heading(
            "About BioDataWorks", 
            size=FontSizes.SECTION_HEADER, 
            text_align="center", 
            margin_bottom="1rem", 
            color=Colors.TEXT),
        rx.text(
            """
            We create software applications that make labs faster, smarter, and more competitive.
            From summarizing lab notebooks and tracking project progress, to automating data pipelines and generating
            actionable insights, we help labs operate at the speed and precision today's high-stakes funding
            environment demands. The goal is simple: spend less time on repetitive tasks and more time producing
            high-impact science.
            """,
            font_size=FontSizes.MAIN_TEXT,
            color=Colors.TEXT,
            line_height="1.6",
            margin_bottom="2rem",
        ),
        width="75%",
    )


def about_individual(name: str, title: str, email: str, photo_file: str, content: str, 
                     linkedin_href: str, github_href: str, youtube_href: str=""):
    bg_color = "gray.50"
    border_color = "teal.300" 
    
    return rx.box(
        rx.hstack(
            circle_image(photo_file),
            rx.vstack(
                rx.heading(
                    name,
                    color=Colors.TEXT,
                    size=FontSizes.SECTION_HEADER,
                    margin_top="1rem",
                    align="center",
                ),
                rx.text(
                    rx.text.em(title),
                    color=Colors.JADE,
                    font_size=FontSizes.MAIN_TEXT,
                    align="center",
                ),
                rx.hstack(
                    rx.icon("mail", color=Colors.JADE, size=FontSizes.ICON),
                    rx.text(email, color=Colors.TEXT, font_size=FontSizes.MAIN_TEXT,),
                    padding_top=Spacing.PAGE_SIDE,
                ),
            ),
            padding_bottom=Spacing.PAGE_SIDE,
        ),

        rx.vstack(
            rx.vstack(
                rx.text(content, font_size=FontSizes.SMALL_TEXT, text_align="justify", color=Colors.TEXT, line_height="1.6"),
                spacing="5",
                padding_bottom=Spacing.PAGE_SIDE,
            ),
            padding_bottom=Spacing.PAGE_SIDE,
        ),
        
        rx.vstack(
            rx.mobile_only(
                rx.vstack(
                    linkedin_link(linkedin_href),
                    github_link(github_href),
                    youtube_link(youtube_href),
                ),
                padding_bottom=Spacing.PAGE_SIDE,
            ),
            rx.tablet_and_desktop(
                rx.hstack(
                    linkedin_link(linkedin_href),
                    github_link(github_href),
                    youtube_link(youtube_href),
                    spacing="9",
                ),
                spacing="2",
                padding_bottom=Spacing.PAGE_SIDE,
            ),
            download_cv_button(),
            align="center",
        ),
        background_color=bg_color,
        border_width="1px",
        border_color=border_color,
        border_radius="15px",
        padding=Spacing.PAGE_SIDE,
        shadow="sm",
        width="700px",
    )

def about_angela():
    return about_individual(
        name="Angela Crabtree, MS",
        title="Bioinformatician & Founder",
        email="angela.crabtree@biodataworks.com",
        photo_file="/me.jpg",
        content="""
            I help academic research labs efficiently harness their data to accelerate discovery.
            With 10+ years in microbiology and cancer bioinformatics, I know firsthand how much time
            and energy goes into managing experiments, analyzing results, and keeping
            track of lab workflows. I build custom tools that cut through the busywork so your team can focus
            on the science that matters— and the funding that sustains it.
            """,
        linkedin_href="https://linkedin.com/in/amcrabtree",
        github_href="https://github.com/amcrabtree",
        youtube_href="https://www.youtube.com/@angelac.1653",
    )


# ---------- Page Layout ----------
@rx.page(route="/about")
def about_section():
    return rx.box(
        navbar_dropdown(),
        rx.vstack(
            about_biodataworks(),
            about_angela(),
            padding=Spacing.PAGE_TOP,
            align="center",
        ),
        background_color=Colors.BACKGROUND,
        font_family="Arial, sans-serif",
    )

# ---------- App Setup ----------
app = rx.App()
app.add_page(about_section, title="BioDataWorks | About")
