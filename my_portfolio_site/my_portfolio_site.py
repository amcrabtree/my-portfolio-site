import reflex as rx

# ------ some default settings -------
section_header_sizing = "8"
service_card_color = "#62D582"

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
                color="black",
                font_size="1.8em",
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
        rx.heading("About Me", size=section_header_sizing, margin_bottom="0.5em"),
        rx.vstack(
            rx.text(
                """
                I help research labs harness AI to turn data into discovery. As a bench scientist turned bioinformatician, 
                I know firsthand how much time and energy goes into managing experiments, analyzing results, and keeping 
                track of lab workflows. I build AI-powered tools that cut through the busywork so labs can focus on the 
                science that matters—and the grants that fund it.
                """,
                font_size="1.4em",
                color="black",
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
                color="black",
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
        rx.heading("Services", size=section_header_sizing, margin_bottom="1em"),
        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.heading("Consulting for Research Labs", size="6", color="black"),
                    rx.text(
                        "I partner with PIs to identify where AI can make the biggest impact in your lab—streamlining workflows, improving data quality, and helping your team produce more high-impact results.",
                        size="5",
                        color="black",
                    ),
                ),
                padding_y="1em",
                padding_x="2em",
                background_color=service_card_color,
                border_radius="5px",
                width="60%",
                margin="8px",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("Lab Management & Progress Tracking", size="6", color="black"),
                    rx.text(
                        "Custom AI-powered dashboards to summarize lab notebooks, track project milestones, and highlight both high-performing and struggling team members. PIs get actionable insights without hours of manual review.",
                        size="5",
                        color="black",
                    ),
                    rx.link(
                        rx.button(
                            "View Example", bg="#068771", border_radius="15px",
                            _hover={
                                "background_color": "black",
                                "color": "lightblue",
                                "cursor": "pointer"
                            },
                            transition="background-color 0.3s, color 0.3s"
                        ),
                        href="https://github.com/amcrabtree",  # Update to specific repo when ready
                        font_size="18px",
                        is_external=True,
                    ),
                ),
                padding_y="1em",
                padding_x="2em",
                background_color=service_card_color,
                border_radius="5px",
                width="60%",
                margin="8px",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("Data Automation & Analysis Pipelines", size="6", color="black"),
                    rx.text(
                        "Python-based automation of repetitive data analysis, image processing, and reporting. Free up your team to focus on experiments and high-impact results that strengthen publications and grant applications.",
                        size="5",
                        color="black",
                    ),
                    rx.link(
                        rx.button(
                            "View Example", bg="#068771", border_radius="15px",
                            _hover={
                                "background_color": "black",
                                "color": "lightblue",
                                "cursor": "pointer"
                            },
                            transition="background-color 0.3s, color 0.3s"
                        ),
                        href="https://github.com/amcrabtree/bioinfo-workflows",
                        font_size="18px",
                        is_external=True,
                    ),
                ),
                padding_y="1em",
                padding_x="2em",
                background_color=service_card_color,
                border_radius="5px",
                width="60%",
                margin="8px",
            ),
            rx.box(
                rx.vstack(
                    rx.heading("Knowledge & Literature Tools", size="6", color="black"),
                    rx.text(
                        """
                        Turn scattered lab notes and literature into actionable insights. 
                        AI-powered tools help labs quickly identify key findings, summarize results, 
                        and produce concise reports for decision-making or writing.
                        """,
                        size="5",
                        color="black",
                    ),
                    rx.link(
                        rx.button(
                            "View Example", bg="#068771", border_radius="15px",
                            _hover={
                                "background_color": "black",
                                "color": "lightblue",
                                "cursor": "pointer"
                            },
                            transition="background-color 0.3s, color 0.3s"
                        ),
                        href="https://github.com/amcrabtree/pub-rag",  # Update to specific repo
                        font_size="18px",
                        is_external=True,
                    ),
                ),
                padding_y="1em",
                padding_x="2em",
                background_color=service_card_color,
                border_radius="5px",
                width="60%",
                margin="8px",
            ),
            spacing="4",
        ),
        padding_y="4em",
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
        rx.heading("Experience & Education", size=section_header_sizing, margin_bottom="1em"),
        rx.vstack(
            *[
                rx.box(
                    rx.text(f"{year}", font_weight="bold", color="black", size="5"),
                    rx.text(desc, color="black", size="4"),
                    border_left="3px solid teal",
                    padding_left="2em",
                    margin_bottom="1.5em",
                )
                for year, desc in timeline_items
            ],
            align="start",
            spacing="3",
        ),
        rx.link(
            rx.button(
                "Download CV", bg="#068771", border_radius="15px",
                _hover={
                    "background_color": "#62D582",
                    "color": "lightblue",
                    "cursor": "pointer"
                    },
                transition="background-color 0.3s, color 0.3s",
                on_click=rx.download(url="/resume.pdf"),
                ),
            font_size="18px",
            is_external=False,
        ),
        padding_y="4em",
        padding_x="2em",
        max_width="800px",
        margin="auto",
    )


def contact_section():
    return rx.box(
        rx.heading("Contact", size=section_header_sizing, margin_bottom="1em"),
        rx.text("Feel free to reach out for collaboration or project inquiries:", color="black"),
        rx.text("📧 angela.crabtree@biodataworks.com", font_weight="bold", color="black"),
        rx.text("📞 +1 (208) 596-1751", color="black"),
        rx.hstack(
            rx.link("🌐 Website", href="https://amcrabtree.github.io/my-portfolio", color="teal"),
            rx.link("LinkedIn", href="https://linkedin.com/in/amcrabtree", color="teal"),
            rx.link("GitHub", href="https://github.com/amcrabtree", color="teal"),
            rx.link("YouTube", href="https://www.youtube.com/@angelac.1653", color="teal"),
            spacing="5",
            justify="center",
        ),
        padding_y="4em",
        padding_x="2em",
        text_align="center",
    )


# ---------- Page Layout ----------
def index():
    return rx.box(
        header_section(),
        about_section(),
        services_section(),
        timeline_section(),
        contact_section(),
        background_color="#7fbeb3",
        font_family="Arial, sans-serif",
    )


# ---------- App Setup ----------
app = rx.App()
app.add_page(index, title="Angela Crabtree | BioDataWorks Consulting")

if __name__ == "__main__":
    app.run()
