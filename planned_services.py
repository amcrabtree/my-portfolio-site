import reflex as rx

# ------ some default settings -------
section_header_sizing = "8"
service_card_color = "#62D582"

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
                        href="https://github.com/amcrabtree",  
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