import reflex as rx

# ------ some default settings -------
section_header_sizing = "8"
service_card_color = "#7F6B94"

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
            rx.heading("Angela Crabtree", size="9", margin_top="1em"),
            rx.text(
                "AI App Consultant",
                font_size="2em",
                ),
            rx.text.em(
                "building AI tools for accelerating biological discovery",
                color="black",
                font_size="1.8em",
                ),
            spacing="4",  
            align="center",
        ),
        padding_y="5em",
    )


def about_section():
    return rx.box(
        rx.heading("About Me", size=section_header_sizing, margin_bottom="0.5em"),
        rx.text(
            """
            I help biological researchers streamline their work by building custom AI-powered tools. 
            Whether it’s finding relevant literature, searching past experimental data, or automating repetitive 
            analysis steps, I design accessible solutions that make research faster, smarter, and more enjoyable.
            """,
            font_size="1.4em",
            color="black",
            line_height="1.6em",
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
                rx.heading("Consulting for Research Labs", size="6"),
                rx.text("End-to-end consulting for labs seeking to leverage AI and bioinformatics pipelines.", size="5", color="black"),
                padding_y="1em",
                padding_x="2em",
                background_color=service_card_color,
                border_radius="5px",
                width="60%",
                margin="8px",
            ),
            rx.box(
                rx.heading("AI Tool Development", size="6"),
                rx.text("Custom Python/Streamlit/Reflex apps for biological data workflows.", size="5", color="black"),
                rx.link(
                    rx.button("GitHub Example", bg="#068771", border_radius="15px"),
                    href="https://github.com/amcrabtree/pub-rag",
                    font_size="18px",
                    is_external=True,  # Optional: opens the link in a new tab if True
                    ),
                padding_y="1em",
                padding_x="2em",
                background_color=service_card_color,
                border_radius="5px",
                width="60%",
                margin="8px",
            ),
            rx.box(
                rx.heading("ML Model Training & Analysis", size="6"),
                rx.text("Cell typing, image segmentation, and predictive modeling for biological datasets.", size="5", color="black"),
                rx.link(
                    rx.button("YouTube Demo", bg="#068771", border_radius="15px"),
                    href="https://github.com/amcrabtree/pub-rag",
                    font_size="18px",
                    is_external=True,  
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
        ("2023–Present", "Bioinformatics Scientist, Major Cancer Institute"),
        ("2019–2023", "Research Associate, Immuno-oncology Lab"),
        ("2018", "M.S. in Computational Biology, University of Example"),
        ("2015", "B.S. in Molecular Biology, State University"),
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
        rx.link("LinkedIn", href="https://linkedin.com/in/amcrabtree", color="teal"),
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
