import reflex as rx
from my_portfolio_site.utils import navbar_dropdown


# ------ some default settings -------
section_header_sizing = rx.breakpoints(initial="5", sm="6", md="7", lg="8",)
services_header_sizing = rx.breakpoints(initial="3", sm="4", md="5", lg="6",)
main_text_font_sizing = ["1.3em", "1.4em", "1.4em"]
smaller_text_font_sizing = ["1.0em", "1.1em", "1.3em"]
icon_link_sizing = 30

palette_color_1 = "#bee3b6"
palette_color_2 = "#8fd4cb"
palette_color_3 = "#7998cc"
palette_color_4 = "#765fb0"
palette_color_5 = "#883689"

service_card_color = "#ccf7f0"
background_color = palette_color_2
dark_font_color = "#183E43"

# ---------- Theme settings ----------
def circle_image(src: str, size=["150px", "150px", "200px"]):
    return rx.image(
        src=src,
        border_radius="50%",
        box_shadow="0 0 10px rgba(0,0,0,0.3)",
        width=size,
        height=size,
        object_fit="cover",
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

def about_section():
    return rx.box(
        rx.heading("About BioDataWorks", size=section_header_sizing, margin_bottom="0.5em", color=dark_font_color),
        rx.text(
            """
            We create software applications that make labs faster, smarter, and more competitive. 
            From summarizing lab notebooks and tracking project progress, to automating data pipelines and generating 
            actionable insights, we help labs operate at the speed and precision today’s high-stakes funding 
            environment demands. The goal is simple: spend less time on repetitive tasks and more time producing 
            high-impact science.
            """,
            font_size=main_text_font_sizing,
            color="white",
            line_height="1.6em",
        ), 
        rx.hstack(
            rx.text(
                color=dark_font_color,
                font_size=main_text_font_sizing, 
                align="center",
            ),
            circle_image("/me.jpg"),
            rx.vstack(
                rx.heading(
                    "Angela Crabtree, MS", 
                    color="white",
                    size=section_header_sizing, 
                    margin_top="1em",
                    align="center",
                ),
                rx.text(
                    rx.text.em("Bioinformatician & AI Consultant"), 
                    color=dark_font_color,
                    font_size=main_text_font_sizing, 
                    align="center",
                ),
            ),
            padding_y=["1em", "1em", "2em"],
            padding_x=["1em", "1em", "2em"],
            width="100%",
        ),
        rx.vstack(
            rx.text(
                """
                I help academic research labs efficiently harness their data to accelerate discovery. 
                With 10+ years in microbiology and cancer bioinformatics, I know firsthand how much time 
                and energy goes into managing experiments, analyzing results, and keeping 
                track of lab workflows. I build custom tools that cut through the busywork so your team can focus 
                on the science that matters— and the funding that sustains it. 
                """,
                font_size=main_text_font_sizing,
                color=dark_font_color,
                line_height="1.6em",
            ),
            spacing="5", 
            padding_x=["1em", "1em", "2em"],
        ),
        padding_top=["5em", "5em", "7em"],
        padding_bottom=["1em", "1em", "2em"],
        max_width="800px",
        margin="auto",
    )


def timeline_section():
    timeline_items = [
        ("2025–Present", "work", "Freelance Consultant (AI & ML Applications for Life Sciences), BioDataWorks"),
        ("2023–Present", "work", "Bioinformatics Scientist, Earle A. Chiles Research Institute"),
        ("2022–2023", "work", "Bioinformatics Intern, Earle A. Chiles Research Institute"),
        ("2021–2022", "school", "M.S. Biology (Bioinformatics & Genomics), University of Oregon"),
        ("2017–2021", "work", "Research Technician, University of Idaho - Rowley Lab"),
        ("2015–2017", "work", "Microbiologist, Washington State University"),
        ("2014–2015", "work", "Chemist, Anatek Labs, Inc."),
        ("2012–2014", "school", "B.S. Microbiology, University of Idaho"),
        ("2006–2011", "school", "B.S. Chemistry, University of Idaho"),
    ]
    return rx.box(
        rx.heading("Experience & Education", size=section_header_sizing, margin_bottom="1em", color=dark_font_color),
        rx.vstack(
            *[
                rx.box(
                    rx.text(f"{year}", font_weight="bold", color=dark_font_color, font_size=main_text_font_sizing,),
                    rx.text(desc, color=dark_font_color, font_size=smaller_text_font_sizing,),
                    border_left=f"4px solid {palette_color_5}" if exp_type=="school" else f"4px solid {palette_color_3}",
                    padding_left="1em",
                    margin_bottom="1.5em",
                )
                for year, exp_type, desc in timeline_items
            ],
            rx.link(
                rx.button(
                    "Download CV", bg=palette_color_3, border_radius="20px", font_size=smaller_text_font_sizing,
                    _hover={
                        "background_color": palette_color_4,
                        "color": "white",
                        "cursor": "pointer"
                        },
                    transition="background-color 0.3s, color 0.3s",
                    on_click=rx.download(url="/resume.pdf"),
                    box_shadow="0px 4px 8px rgba(0, 0, 0, 0.3)",
                    ),
                is_external=False,
            ),
            padding_left=["1em", "1em", "3em", "3em"],
            align="start",
            spacing="3",
        ),
        padding_y="4em",
        padding_x="2em",
        max_width="800px",
        margin="auto",
    )


def contact_section():
    return rx.box(
        rx.heading("Contact", size=section_header_sizing, margin_bottom="1em", color=dark_font_color),
        rx.vstack(
            rx.text(
                "Reach out for collaboration or project inquiries!", 
                color=dark_font_color,
                font_size=main_text_font_sizing,
            ),
            rx.hstack(
                rx.icon("mail", color=dark_font_color, size=icon_link_sizing),
                rx.text("angela.crabtree@biodataworks.com", color=dark_font_color, font_size=main_text_font_sizing,)
            ),
            rx.mobile_only(
                rx.vstack(
                    linkedin_link(),
                    github_link(),
                    youtube_link(),
                ),
            ),
            rx.tablet_and_desktop(
                rx.hstack(
                    linkedin_link(),
                    github_link(),
                    youtube_link(),
                    spacing="9",
                ),
                spacing="2",
            ), 
            rx.image("/biodataworks_qr.png", width="200px", height="auto",),
            padding_left=["1em", "1em", "3em", "3em"],  
        ),
        padding_y="1em",
        padding_x="2em",
        max_width="800px",
        margin="auto",
    )


# -------- Contact Links ----------

def linkedin_link():
    return rx.link(
        rx.hstack(
            rx.icon("linkedin", color=palette_color_3, size=icon_link_sizing),
            rx.text("LinkedIn", color=palette_color_3, font_size=main_text_font_sizing,)
        ),
        href="https://linkedin.com/in/amcrabtree",
        is_external=False,
    )

def github_link():
    return rx.link(
        rx.hstack(
            rx.icon("github", color=palette_color_3, size=icon_link_sizing),
            rx.text("GitHub", color=palette_color_3, font_size=main_text_font_sizing,)
        ),
        href="https://github.com/amcrabtree",
        is_external=False,
    )

def youtube_link():
    return rx.link(
        rx.hstack(
            rx.icon("youtube", color=palette_color_3, size=icon_link_sizing),
            rx.text("YouTube", color=palette_color_3, font_size=main_text_font_sizing,)
        ),
        href="https://www.youtube.com/@angelac.1653",
        is_external=False,
    )

# ---------- Page Layout ----------
@rx.page(route="/about")
def index():
    return rx.box(
        navbar_dropdown(),
        about_section(),
        timeline_section(),
        contact_section(),
        background_color=background_color,
        font_family="Arial, sans-serif",
        padding_bottom="7em",
    )


# ---------- App Setup ----------
app = rx.App()
app.add_page(index, title="Angela Crabtree | BioDataWorks Consulting")
