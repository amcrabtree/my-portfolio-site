import reflex as rx

# ------ some default settings -------
section_header_sizing = rx.breakpoints(initial="4", sm="5", md="6", lg="7",)
services_header_sizing = rx.breakpoints(initial="3", sm="4", md="5", lg="6",)
main_text_font_sizing = ["1.3", "1.4", "1.4em"]
smaller_text_font_sizing = ["1.0", "1.1", "1.3em"]
icon_link_sizing = 30

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

# ----------- Services links -------------

def alignment_button(text_sizing: list):
    return rx.link(
        rx.button(
            "Alignment & Variant Calling", 
            bg=palette_color_3, 
            border_radius="15px", 
            font_size=text_sizing,
            _hover={
                "background_color": dark_font_color,
                "color": "lightblue",
                "cursor": "pointer"
            },
            transition="background-color 0.3s, color 0.3s",
            box_shadow="0px 4px 8px rgba(0, 0, 0, 0.3)",
        ),
        href="https://github.com/amcrabtree/killer-align",  
        is_external=True,
    )

def assembly_button(text_sizing: list):
    return rx.link(
        rx.button(
            "De Novo Assembly", 
            bg=palette_color_3, 
            border_radius="15px", 
            font_size=text_sizing,
            _hover={
                "background_color": dark_font_color,
                "color": "lightblue",
                "cursor": "pointer"
            },
            transition="background-color 0.3s, color 0.3s",
            box_shadow="0px 4px 8px rgba(0, 0, 0, 0.3)",
        ),
        href="https://github.com/amcrabtree/killer-denovo",  
        is_external=True,
    )

def survival_analysis_button(text_sizing: list):
    return rx.link(
        rx.button(
            "Survival Analysis Reporting", 
            bg=palette_color_3, 
            border_radius="15px", 
            font_size=text_sizing,
            _hover={
                "background_color": dark_font_color,
                "color": "lightblue",
                "cursor": "pointer"
            },
            transition="background-color 0.3s, color 0.3s",
            box_shadow="0px 4px 8px rgba(0, 0, 0, 0.3)",
        ),
        href="https://github.com/amcrabtree/worm_survival", 
        is_external=True,
    )

def viral_entry_button(text_sizing: list):
    return rx.link(
        rx.button(
            "Viral Entry Assay Explorer", 
            bg=palette_color_3, 
            border_radius="15px", 
            font_size=text_sizing,
            _hover={
                "background_color": dark_font_color,
                "color": "lightblue",
                "cursor": "pointer"
            },
            transition="background-color 0.3s, color 0.3s",
            box_shadow="0px 4px 8px rgba(0, 0, 0, 0.3)",
        ),
        href="https://amcrabtree.shinyapps.io/ebov_proj/",  
        is_external=True,
    )

def lab_notebook_assistant(text_sizing: list):
    return rx.link(
        rx.button(
            "AI Lab Notebook Assistant",
            bg=palette_color_3, 
            border_radius="15px",
            font_size=text_sizing,
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
    )



# ---------- Section components ----------
def header_section():
    return rx.center(
        rx.vstack(
            circle_image("/me.jpg"),
            rx.heading(
                "Angela Crabtree, MS", 
                color="white",
                size=rx.breakpoints(initial="8", sm="8", md="9", lg="9",), 
                margin_top="1em",
                align="center",
            ),
            rx.text(
                "AI Applications Consultant for Life Sciences",
                font_size=["1.3em", "1.6em", "2em"],
                align="center",
                color="white",
                weight="medium",
            ),
            rx.text.em(
                "building tools that accelerate biological discovery",
                font_size=["1.3em", "1.5em", "1.7em"],
                align="center",
                color=dark_font_color,
            ),
            rx.image(
                src="/biodataworks_logo_alpha.png",
                width="300px",
                height="300px",
            ),
            spacing="4",
            align="center",
        ),
        padding_top=["1em", "1em", "4em"], 
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
                font_size=main_text_font_sizing,
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
                font_size=main_text_font_sizing,
                color=dark_font_color,
                line_height="1.6em",
            ),
            spacing="5", 
        ),
        padding_y=["1em", "1em", "2em"],
        padding_x=["1em", "1em", "2em"],
        max_width="800px",
        margin="auto",
    )


def services_section():
    return rx.box(
        rx.heading("Services", size=section_header_sizing, margin_bottom="1em", color=dark_font_color),
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.heading("Consulting for Research Labs", size=services_header_sizing, color=dark_font_color),
                    rx.text(
                        """
                        I partner with PIs and research teams to identify where AI can have the biggest 
                        impact—streamlining workflows, improving data quality, and helping your lab extract 
                        insights faster and more reliably.
                        """,
                        font_size=smaller_text_font_sizing,
                        color=dark_font_color,
                    ),
                ),
                padding_y=["1em", "1em", "2em"],
                padding_x=["1em", "1em", "2em"],
                background_color=service_card_color,
                width="100%",
                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.5)",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("Lab Management Apps", size=services_header_sizing, color=dark_font_color),
                    rx.text(
                        """
                        AI-powered tools to track experiments, manage lab notebooks, monitor project progress, 
                        and highlight critical trends—so PIs and team members get actionable insights 
                        without hours of manual review.
                        """,
                        font_size=smaller_text_font_sizing,
                        color=dark_font_color,
                    ),
                    rx.hstack(
                        lab_notebook_assistant(smaller_text_font_sizing),
                        justify="center",
                        spacing="5",
                    ),
                    spacing="4",
                ),
                padding_y=["1em", "1em", "2em"],
                padding_x=["1em", "1em", "2em"],
                background_color=service_card_color,
                width="100%",
                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.5)",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("Bioinformatics & Analysis Apps", size=services_header_sizing, color=dark_font_color),
                    rx.text(
                        """
                        Make complex computational analyses reproducible and accessible for non-coders. Automate workflows for sequence alignment, variant calling, or other bioinformatics tasks, so your team can focus on interpreting results rather than managing pipelines.
                        """,
                        font_size=smaller_text_font_sizing,
                        color=dark_font_color,
                    ),
                    rx.mobile_only(
                        rx.vstack(
                            alignment_button(smaller_text_font_sizing),
                            assembly_button(smaller_text_font_sizing),
                            justify="center",
                        ),
                    ),
                    rx.tablet_and_desktop(
                        rx.hstack(
                            alignment_button(smaller_text_font_sizing),
                            assembly_button(smaller_text_font_sizing),
                            justify="center",
                            spacing="5",
                        ),
                    ),
                    
                ),
                padding_y=["1em", "1em", "2em"],
                padding_x=["1em", "1em", "2em"],
                background_color=service_card_color,
                width="100%",
                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.5)",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("Interactive Dashboards & Reporting", size=services_header_sizing, color=dark_font_color),
                    rx.text(
                        """
                        Transform experimental results into intuitive, interactive dashboards. Quickly explore data, identify key patterns, and generate concise reports for lab meetings, publications, or grant submissions.
                        """,
                        font_size=smaller_text_font_sizing,
                        color=dark_font_color,
                    ),
                    rx.mobile_only(
                        rx.vstack(
                            survival_analysis_button(smaller_text_font_sizing),
                            viral_entry_button(smaller_text_font_sizing),
                            justify="center",
                        ),
                    ),
                    rx.tablet_and_desktop(
                        rx.hstack(
                            survival_analysis_button(smaller_text_font_sizing),
                            viral_entry_button(smaller_text_font_sizing),
                            justify="center",
                            spacing="5",
                        ),
                    ),
                        
                ),
                padding_y=["1em", "1em", "2em"],
                padding_x=["1em", "1em", "2em"],
                background_color=service_card_color,
                width="100%",
                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.5)",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("Workshops & Training", size=services_header_sizing, color=dark_font_color),
                    rx.text(
                        """
                        Build your lab's computational and AI capacity through live workshops on Python development, AI implementation, bioinformatics analyses, and machine learning model training.
                        """,
                        font_size=smaller_text_font_sizing,
                        color=dark_font_color,
                    ),
                    rx.vstack(
                        rx.vstack(
                            rx.link(
                                youtube_thumbnail("/youtube_conch_app.jpg"),
                                href="https://www.youtube.com/watch?v=1g1Nr0XGKu8",  
                                font_size=smaller_text_font_sizing,
                                is_external=True,
                            ),
                            rx.text.em(
                                "How to build an ML app", font_size=main_text_font_sizing, color=dark_font_color,
                            ),
                            padding="1em",
                            align="center",
                        ),
                        rx.vstack(
                            rx.link(
                                youtube_thumbnail("/youtube_train_model.jpg"),
                                href="https://youtu.be/VyMzvriztdg",  
                                font_size=smaller_text_font_sizing,
                                is_external=True,
                            ),
                            rx.text.em(
                                "How to train an ML model", font_size=main_text_font_sizing, color=dark_font_color,
                            ),
                            padding="1em",
                            align="center",
                            
                        ),
                        rx.vstack(
                            rx.link(
                                youtube_thumbnail("/youtube_count_cells.jpg"),
                                href="https://youtu.be/3Hj6NZIjxbk",  
                                font_size="18px",
                                is_external=True,
                            ),
                            rx.text.em(
                                "How to detect cells in images", font_size=main_text_font_sizing, color=dark_font_color,
                            ),
                            padding="1em",
                            align="center",
                        ),
                        align="center",
                        width="100%",
                    ),
                ),
                padding_y=["1em", "1em", "2em"],
                padding_x=["1em", "1em", "2em"],
                background_color=service_card_color,
                width="100%",
                box_shadow="0px 4px 8px rgba(0, 0, 0, 0.5)",
            ),
            spacing="6",
            padding_left="2em",
        ),
        padding_y=["1em", "1em", "2em"],
        padding_x=["1em", "1em", "2em"],
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
                "Feel free to reach out for collaboration or project inquiries!", 
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
            rx.image("/biodataworks_qr.png", width="200px", height="auto", border_radius="10px", border="1px solid #333",),
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
