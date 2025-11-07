import reflex as rx

# ------ some default settings -------
section_header_sizing = "8"

palette_color_1 = "#bee3b6"
palette_color_2 = "#8fd4cb"
palette_color_3 = "#7998cc"
palette_color_4 = "#765fb0"
palette_color_5 = "#883689"

service_card_color = palette_color_1
background_color = palette_color_2
dark_font_color = "#183E43"

# ---------- Theme settings ----------
def circle_image(src: str, size="200px"):
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
def header_section():
    return rx.center(
        rx.vstack(
            circle_image("/me.jpg"),
            rx.heading("Angela Crabtree, MS", size="9", margin_top="1em"),
            rx.text(
                "AI Applications Consultant for Life Sciences",
                font_size="2em",
            ),
            rx.text.em(
                "building tools that accelerate biological discovery",
                color=dark_font_color,
                font_size="1.7em",
            ),
            rx.image(
                src="/biodataworks_logo_alpha.png",
                width="300px",
                height="300px",
            ),
            spacing="4",
            align="center",
        ),
        padding_top="4em", 
        padding_bottom="0em", 
    )


def about_section():
    return rx.box(
        rx.heading("About Me", size=section_header_sizing, margin_bottom="0.5em", color=dark_font_color),
        rx.vstack(
            rx.text(
                """
                I help research labs efficiently harness their data to supercharge discovery. 
                As a bench scientist turned bioinformatician, 
                I know firsthand how much time and energy goes into managing experiments, analyzing results, and keeping 
                track of lab workflows. I build custom tools that cut through the busywork so labs can focus on the 
                science that matters—and the grants that fund it.
                """,
                font_size="1.4em",
                color=dark_font_color,
                line_height="1.6em",
            ),
            rx.text(
                """
                At BioDataWorks, I create AI applications that make labs faster, smarter, and more competitive. 
                From summarizing lab notebooks and tracking project progress, to automating data pipelines and generating 
                actionable insights, my tools help labs operate at the speed and precision today’s high-stakes funding 
                environment demands. The goal is simple: spend less time on repetitive tasks and more time producing 
                high-impact science.
                """,
                font_size="1.4em",
                color=dark_font_color,
                line_height="1.6em",
            ),
            spacing="5", 
        ),
        padding_y="4em",
        padding_x="2em",
        max_width="800px",
        margin="auto",
    )


def services_section():
    return rx.box(
        rx.heading("Services", size=section_header_sizing, margin_bottom="1em", color=dark_font_color),
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.heading("Consulting for Research Labs", size="6", color=dark_font_color),
                    rx.text(
                        """
                        I partner with PIs and research teams to identify where AI can have the biggest impact—streamlining workflows, improving data quality, and helping your lab extract insights faster and more reliably.
                        """,
                        size="5",
                        color=dark_font_color,
                    ),
                ),
                padding_y="2em",
                padding_x="2em",
                background_color=service_card_color,
                border_radius="5px",
                width="100%",
                margin="8px",
                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.5)",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("Lab Management Apps", size="6", color=dark_font_color),
                    rx.text(
                        """
                        AI-powered tools to track experiments, manage lab notebooks, monitor project progress, 
                        and highlight critical trends—so PIs and team members get actionable insights 
                        without hours of manual review.
                        """,
                        size="5",
                        color=dark_font_color,
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "AI Lab Notebook Search Assistant",
                                bg=palette_color_3, 
                                border_radius="15px",
                                font_size="20px",
                                _hover={
                                    "background_color": dark_font_color,
                                    "color": "lightblue",
                                    "cursor": "pointer",
                                },
                                transition="background-color 0.3s, color 0.3s",
                                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.3)",
                            ),
                            href="https://github.com/amcrabtree/lab-note-rag",  
                            is_external=True,
                        ),
                        justify="center",
                        spacing="5",
                    ),
                    spacing="4",
                ),
                padding_y="2em",
                padding_x="2em",
                background_color=service_card_color,
                border_radius="5px",
                width="100%",
                margin="8px",
                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.5)",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("Bioinformatics & Analysis Apps", size="6", color=dark_font_color),
                    rx.text(
                        """
                        Make complex computational analyses reproducible and accessible for non-coders. Automate workflows for sequence alignment, variant calling, or other bioinformatics tasks, so your team can focus on interpreting results rather than managing pipelines.
                        """,
                        size="5",
                        color=dark_font_color,
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Alignment & Variant Calling", bg=palette_color_3, 
                                border_radius="15px", font_size="20px",
                                _hover={
                                    "background_color": dark_font_color,
                                    "color": "lightblue",
                                    "cursor": "pointer"
                                },
                                transition="background-color 0.3s, color 0.3s",
                                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.3)",
                            ),
                            href="https://github.com/amcrabtree/killer-align",  
                            font_size="18px",
                            is_external=True,
                        ),
                        rx.link(
                            rx.button(
                                "De Novo Assembly", bg=palette_color_3, 
                                border_radius="15px", font_size="20px",
                                _hover={
                                    "background_color": dark_font_color,
                                    "color": "lightblue",
                                    "cursor": "pointer"
                                },
                                transition="background-color 0.3s, color 0.3s",
                                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.3)",
                            ),
                            href="https://github.com/amcrabtree/killer-denovo",  
                            font_size="18px",
                            is_external=True,
                        ),
                        justify="center",
                        spacing="5",
                    ),
                ),
                padding_y="2em",
                padding_x="2em",
                background_color=service_card_color,
                border_radius="5px",
                width="100%",
                margin="8px",
                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.5)",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("Interactive Dashboards & Reporting", size="6", color=dark_font_color),
                    rx.text(
                        """
                        Transform experimental results into intuitive, interactive dashboards. Quickly explore data, identify key patterns, and generate concise reports for lab meetings, publications, or grant submissions.
                        """,
                        size="5",
                        color=dark_font_color,
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Survival Analysis Reporting", bg=palette_color_3, 
                                border_radius="15px", font_size="20px",
                                _hover={
                                    "background_color": dark_font_color,
                                    "color": "lightblue",
                                    "cursor": "pointer"
                                },
                                transition="background-color 0.3s, color 0.3s",
                                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.3)",
                            ),
                            href="https://github.com/amcrabtree/worm_survival",  
                            font_size="18px",
                            is_external=True,
                        ),
                        rx.link(
                            rx.button(
                                "Viral Entry Assay Explorer", bg=palette_color_3, 
                                border_radius="15px", font_size="20px",
                                _hover={
                                    "background_color": dark_font_color,
                                    "color": "lightblue",
                                    "cursor": "pointer"
                                },
                                transition="background-color 0.3s, color 0.3s",
                                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.3)",
                            ),
                            href="https://amcrabtree.shinyapps.io/ebov_proj/",  
                            font_size="18px",
                            is_external=True,
                        ),
                        justify="center",
                        spacing="5",
                    ),
                ),
                padding_y="2em",
                padding_x="2em",
                background_color=service_card_color,
                border_radius="5px",
                width="100%",
                margin="8px",
                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.5)",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("Workshops & Training", size="6", color=dark_font_color),
                    rx.text(
                        """
                        Build your lab's computational and AI capacity through live workshops on Python development, AI implementation, bioinformatics analyses, and machine learning model training.
                        """,
                        size="5",
                        color=dark_font_color,
                    ),
                    rx.hstack(
                        rx.link(
                            youtube_thumbnail("/youtube_conch_app.jpg"),
                            href="https://www.youtube.com/watch?v=1g1Nr0XGKu8",  
                            font_size="18px",
                            is_external=True,
                        ),
                        rx.text("How to build an ML app", size="5", color=dark_font_color,
                        ),
                        padding="1em"
                    ),
                    rx.hstack(
                        rx.link(
                            youtube_thumbnail("/youtube_train_model.jpg"),
                            href="https://youtu.be/VyMzvriztdg",  
                            font_size="18px",
                            is_external=True,
                        ),
                        rx.text("How to train an ML model", size="5", color=dark_font_color,
                        ),
                        padding="1em"
                    ),
                    rx.hstack(
                        rx.link(
                            youtube_thumbnail("/youtube_count_cells.jpg"),
                            href="https://youtu.be/3Hj6NZIjxbk",  
                            font_size="18px",
                            is_external=True,
                        ),
                        rx.text("How to detect cells in images", size="5", color=dark_font_color,
                        ),
                        padding="1em"
                    ),
                ),
                padding_y="2em",
                padding_x="2em",
                background_color=service_card_color,
                border_radius="5px",
                width="100%",
                margin="8px",
                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.5)",
            ),
            spacing="4",
            padding_left="2em",
        ),
        padding_y="1em",
        padding_x="2em",
        max_width="800px",
        margin="auto",
    )




def timeline_section():
    timeline_items = [
        ("2025–Present", "Freelance Consultant (AI & ML Applications for Life Sciences), BioDataWorks"),
        ("2023–Present", "Bioinformatics Scientist, Earle A. Chiles Research Institute"),
        ("2022–2023", "Bioinformatics Intern, Earle A. Chiles Research Institute"),
        ("2021–2022", "M.S. Biology (Bioinformatics & Genomics), University of Oregon"),
        ("2017–2021", "Research Technician, University of Idaho - Rowley Lab"),
        ("2015–2017", "Microbiologist, Washington State University"),
        ("2014–2015", "Chemist, Anatek Labs, Inc."),
        ("2012–2014", "B.S. Microbiology, University of Idaho"),
        ("2006–2011", "B.S. Chemistry, University of Idaho"),
    ]
    return rx.box(
        rx.heading("Experience & Education", size=section_header_sizing, margin_bottom="1em", color=dark_font_color),
        rx.vstack(
            *[
                rx.box(
                    rx.text(f"{year}", font_weight="bold", color=dark_font_color, size="5"),
                    rx.text(desc, color=dark_font_color, size="4"),
                    border_left=f"4px solid {palette_color_1}",
                    padding_left="1em",
                    margin_bottom="1.5em",
                )
                for year, desc in timeline_items
            ],
            rx.link(
                rx.button(
                    "Download CV", bg=palette_color_3, border_radius="20px", font_size="20px",
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
            padding_left="3em",
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
        rx.heading("Contact", size=section_header_sizing, margin_bottom="1em", text_align="center", color=dark_font_color),
        rx.vstack(
            rx.text("Feel free to reach out for collaboration or project inquiries!", color=dark_font_color),
            rx.hstack(
                        rx.icon("mail", color=dark_font_color, size=36),
                        rx.text("angela.crabtree@biodataworks.com", color=dark_font_color)
                    ),
            rx.hstack(
                rx.link(
                    rx.hstack(
                        rx.icon("linkedin", color=palette_color_3, size=36),
                        rx.text("LinkedIn", color=palette_color_3)
                    ),
                    href="https://linkedin.com/in/amcrabtree",
                    is_external=False,
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("github", color=palette_color_3, size=36),
                        rx.text("GitHub", color=palette_color_3)
                    ),
                    href="https://github.com/amcrabtree",
                    is_external=False,
                ),
                rx.link(
                    rx.hstack(
                        rx.icon("youtube", color=palette_color_3, size=36),
                        rx.text("YouTube", color=palette_color_3)
                    ),
                    href="https://www.youtube.com/@angelac.1653",
                    is_external=False,
                ),
                spacing="9",
                justify="center",
            ),
            spacing="2",
            align="center",  # <--- centers all items in the vstack horizontally
        ),
        padding_y="1em",
        padding_x="2em",
        max_width="800px",
        margin="auto",
        font_size="24px",
    )


# ---------- Page Layout ----------
def index():
    return rx.box(
        header_section(),
        about_section(),
        services_section(),
        timeline_section(),
        contact_section(),
        background_color=background_color,
        font_family="Arial, sans-serif",
        padding_bottom="7em"
    )


# ---------- App Setup ----------
app = rx.App()
app.add_page(index, title="Angela Crabtree | BioDataWorks Consulting")

if __name__ == "__main__":
    app.run()
