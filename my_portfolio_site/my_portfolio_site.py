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
                "AI & Machine Learning for Life Sciences",
                font_size="2em",
            ),
            rx.text.em(
                "building AI tools that accelerate biological discovery",
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
                I'm developing AI-driven tools and workflows for biological research and offering consulting 
                for labs looking to modernize their computational capabilities. As a bench 
                scientist turned bioinformatician, I understand the challenges of bridging experimental work 
                and computational analysis. 
                """,
                font_size="1.4em",
                color="black",
                line_height="1.6em",
            ),
                rx.text(
                """
                At BioDataWorks, I help biological researchers streamline their work by building custom AI-powered 
                tools—whether it’s finding relevant literature, searching past experimental data, or automating 
                repetitive analysis steps. I design accessible solutions that make research faster, smarter, 
                and more enjoyable.
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
                    rx.heading("Consulting for Research Labs", size="6"),
                    rx.text(
                        "End-to-end consulting for labs seeking to leverage AI, RAG systems, and bioinformatics pipelines.",
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
                    rx.heading("AI Agent Development", size="6"),
                    rx.text(
                        "Custom AI agents for literature review, workflow guidance, and data summarization.",
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
                        href="https://github.com/amcrabtree/cell-sidebot",
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
                    rx.heading("RAG-Powered Knowledge Systems", size="6"),
                    rx.text(
                        "Turn scattered lab notes into searchable knowledgebases using Retrieval-Augmented Generation (RAG).",
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
                        href="https://github.com/amcrabtree/lab-note-rag",
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
                    rx.heading("Workflow Automation for Biological Data", size="6"),
                    rx.text(
                        "Python-based automation for repetitive image analysis and data reporting tasks.",
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
            spacing="4",
        ),
        padding_y="4em",
        padding_x="2em",
        max_width="800px",
        margin="auto",
    )


def timeline_section():
    timeline_items = [
        ("2025–Present", "Freelance Consultant (AI & ML for Life Sciences), BioDataWorks"),
        ("2023–Present", "Bioinformatics Scientist, Earle A. Chiles Research Institute"),
        ("2022–2023", "Bioinformatics Intern, Earle A. Chiles Research Institute"),
        ("2021–2022", "M.S. Biology (Bioinformatics & Genomics), University of Oregon"),
        ("2017–2021", "Research Technician, University of Idaho"),
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
                transition="background-color 0.3s, color 0.3s"
                ),
            href="/assets/resume.pdf",
            font_size="18px",
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
