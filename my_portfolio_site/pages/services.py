import reflex as rx
from my_portfolio_site.styles import Colors, FontSizes, Spacing
from my_portfolio_site.utils import navbar_dropdown


@rx.page(route="/services")
def pricing_pilots_page() -> rx.Component:
    return rx.box(
        navbar_dropdown(),
        rx.vstack(
            rx.box(
                rx.vstack(
                    # Header
                    rx.heading(
                        "Pricing & Pilots",
                        size=FontSizes.SECTION_HEADER,
                        text_align="center",
                        margin_bottom="1rem",
                        color=Colors.TEXT,
                    ),
                    rx.text(
                        "Future-proof your lab's knowledge with flexible, modular solutions.",
                        font_size=FontSizes.MAIN_TEXT,
                        font_style="italic",
                        text_align="center",
                        max_width="800px",
                        margin_x="auto",
                        margin_bottom="2rem",
                        color=Colors.TEXT,
                    ),

                    # Tier 1 — Starter Pack (highlighted)
                    tier_card(
                        title="Starter Pack — Lab Diary & Basic Management",
                        duration="2–4 weeks",
                        price="$950–$1,500",
                        bullets=[
                            "Lightweight digital experiment diary for 1–3 users",
                            "Basic stock/asset tracking (strains, plasmids, reagents)",
                            "Drag-and-drop image organization + auto-tagging",
                            "Quick onboarding for students & PI",
                            "Exportable data for compliance",
                        ],
                        note="Purpose: Test the waters. Minimal disruption. Low-risk first step.",
                        highlight=True
                    ),

                    # Tier 2 — Standard Pilot
                    tier_card(
                        title="Standard Pilot — AI-Powered Lab Knowledge Hub",
                        duration="4–8 weeks",
                        price="$3,500–$5,500",
                        bullets=[
                            "MCP-based knowledge base for selected lab data",
                            "Secure LLM querying of documents, images, and diary entries",
                            "Simple dashboards for PI visibility & trainee tracking",
                            "Onboarding support for all lab members",
                            "1–2 light integrations (e.g., Google Drive, Sheets)",
                        ],
                        note="Purpose: Demonstrate real ROI. Organize scattered lab knowledge. Prepare for future add-ons.",
                        highlight=False
                    ),
                    align="center",
                ), 

                # Optional Add-Ons
                rx.box(
                    rx.vstack(
                        rx.heading("Optional Add-Ons", size=FontSizes.SECTION_HEADER, margin_top="2rem", margin_bottom="1rem", color=Colors.TEXT),
                        rx.text(
                            "Labs can purchase any combination of these add-ons after completing a Starter or Standard Pilot.",
                            margin_bottom="2rem",
                            font_size=FontSizes.MAIN_TEXT,
                            color=Colors.TEXT,
                        ),
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("Add-On"),
                                    rx.table.column_header_cell("Description"),
                                    rx.table.column_header_cell("Typical Cost"),
                                ),
                                
                            ),
                            rx.table.body(
                                *[
                                    table_row("Additional Data Sources", 
                                            "Integrate more Google Drives, ELNs, Benchling, or local servers", 
                                            "$1,500–$3,500"),
                                    table_row("Custom Data Processing", 
                                            "Automate calculations, metadata extraction, image processing", 
                                            "$1,000–$3,000"),
                                    table_row("Advanced Dashboards", 
                                            "PI & student dashboards, reporting tools", 
                                            "$1,500–$3,000"),
                                    table_row("LLM Query Enhancements", 
                                            "Advanced NLP for experiment summaries, cross-year searches", 
                                            "$2,000–$4,000"),
                                    table_row("Training & Onboarding", 
                                            "Workshops, guides, and documentation for new members", 
                                            "$500–$1,500"),
                                ]
                            ),
                            variant="surface",
                        ),
                        padding_bottom="2rem",
                    ),
                ),

                # Benefits Section
                rx.vstack(
                    rx.heading("Key Benefits", size=FontSizes.SECTION_HEADER, margin_top="2rem", margin_bottom="1rem", color=Colors.TEXT),
                    rx.list(
                        rx.list_item(
                            rx.icon("circle_check_big", color="green"), " Faster access to historical experiments", color=Colors.TEXT),
                        rx.list_item(
                            rx.icon("circle_check_big", color="green"), " Reduced redundancy (20–30% fewer repeated experiments)", color=Colors.TEXT),
                        rx.list_item(
                            rx.icon("circle_check_big", color="green"), " Accelerated onboarding for new trainees", color=Colors.TEXT),
                        rx.list_item(
                            rx.icon("circle_check_big", color="green"), " Secure, central lab memory", color=Colors.TEXT),
                        rx.list_item(
                            rx.icon("circle_check_big", color="green"), " Scalable — choose add-ons when you're ready", color=Colors.TEXT),
                        spacing="6",
                        font_size=FontSizes.SMALL_TEXT,
                    ),
                    padding_bottom="2rem",
                ),
                max_width="900px",
                margin_x="auto",
                padding=Spacing.PAGE_SIDE,
            ),
            padding_top=Spacing.PAGE_TOP,
            padding_bottom=Spacing.PAGE_BOTTOM,
        ),
        background_color=Colors.BACKGROUND,
        font_family="Arial, sans-serif",
        min_height="100vh",
    )

# --- Reusable Helper Components ---

def tier_card(title: str, duration: str, price: str, bullets: list[str], note: str, highlight: bool) -> rx.Component:
    bg_color = "gray.50" if highlight else "teal"
    border_color = "teal.300" if highlight else "gray.200"
    return rx.box(
        rx.heading(title, size=FontSizes.SUBSECTION_HEADER, margin_bottom="1rem", color=Colors.TEXT),
        rx.text(f"Duration: {duration}  |  Price: {price}", font_size=FontSizes.MAIN_TEXT, margin_bottom="1rem", color=Colors.TEXT),
        rx.list(*[rx.list_item(b, font_size=FontSizes.SMALL_TEXT, color=Colors.TEXT) for b in bullets], style={"margin-left": "1.5rem", "margin-top": "0.5rem"}),
        rx.text(note, font_size=FontSizes.SMALL_TEXT, font_style="italic", margin_top="1rem", color=Colors.TEXT),
        background_color=bg_color,
        border_width="1px",
        border_color=border_color,
        border_radius="15px",
        padding="2rem",
        shadow="sm",
        width="600px",
    )

def table_row(addon: str, desc: str, cost: str) -> rx.Component:
    return rx.table.row(
            rx.table.row_header_cell(addon),
            rx.table.cell(desc),
            rx.table.cell(cost),
    )
