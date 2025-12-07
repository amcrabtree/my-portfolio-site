import reflex as rx
from my_portfolio_site.utils import contact_button, navbar_dropdown

# Font sizing
section_header_sizing = rx.breakpoints(initial="5", sm="6", md="7", lg="8",)
services_header_sizing = rx.breakpoints(initial="3", sm="4", md="5", lg="6",)
main_text_font_sizing = ["1.3em", "1.4em", "1.4em"]
smaller_text_font_sizing = ["1.0em", "1.1em", "1.3em"]

@rx.page(route="/case_study")
def case_study_page() -> rx.Component:
    return rx.box(
        navbar_dropdown(),
        rx.box(
        rx.vstack(
            # Header
            rx.heading(
                "Case Study — Unlocking a Yeast Lab’s Hidden Knowledge",
                font_size="2.5rem",
                font_weight="700",
                text_align="center",
                margin_bottom="1rem",
            ),
            rx.text.em(
                "How BioDataWorks helped a virus–host research lab unlock years of experimental data.",
                font_size=main_text_font_sizing,
                text_align="center",
                max_width="800px",
                margin_x="auto",
                margin_bottom="3rem",
            ),

            # Background Section
            section(
                "🔬 Background",
                "A leading yeast genetics lab was generating valuable results, but key discoveries were difficult to track due to handwritten notebooks, scattered files, and constant student turnover. The PI’s biggest concern: institutional knowledge was disappearing as fast as it was created."
            ),

            # Pain Point Section
            section(
                "🤯 The Pain Point",
                "Experiments were being repeated because no one knew they'd been done before. Students struggled to find previous results. Redundant effort wasted 20–30% of time, and onboarding new lab members took months."
            ),

            # Solution Section
            rx.heading("🚀 The BioDataWorks Solution", size=section_header_sizing, margin_top="2rem"),
            phase(
                "Phase 1 — Inventory Intelligence",
                [
                    "Indexed >200 yeast stocks with metadata.",
                    "Added QR codes to physical stocks.",
                    "Mapped strains to past experiments.",
                ],
                "Result: Assets became trackable and usable."
            ),
            phase(
                "Phase 2 — Experiment Context Layer",
                [
                    "Introduced lightweight daily digital diaries.",
                    "Auto-tagged image data and linked to strains.",
                    "Improved documentation without changing lab notebooks.",
                ],
                "Result: Clear context around experiments."
            ),
            phase(
                "Phase 3 — Searchable Lab Memory",
                [
                    "Built LLM-powered querying using MCP.",
                    "Enabled fast search for previous experiments and results.",
                    "Restored institutional memory.",
                ],
                "Result: Seconds to find what took weeks before."
            ),

            # Metrics Section
            rx.heading("🔥 Outcomes", size=section_header_sizing, margin_top="2rem"),
            outcomes_table(),

            # Quote
            quote(
                "A second brain for the lab. We finally see everything we’ve been doing."
            ),

            # Future Vision Section
            section(
                "💡 Future Vision",
                "The lab is expanding to automatic phenotype scoring, ELN integration, and publication-ready data exports — built on a strong digital foundation."
            ),

            # CTA Section
            rx.box(
                rx.text(
                    "Let’s modernize your lab’s knowledge — without disrupting what works.",
                    font_size="1.25rem",
                    font_weight="600",
                    text_align="center",
                    margin_bottom="1rem",
                ),
                rx.hstack(
                    contact_button("/contact", main_text_font_sizing),
                    justify="center",
                ),
                margin_top="3rem",
                margin_bottom="5rem",
            ),

            max_width="900px",
            margin_x="auto",
            padding="2rem",
            ),
        padding_top="7em",
        ),
    )

# --- Reusable Helper Components ---

def section(title: str, text: str) -> rx.Component:
    return rx.box(
        rx.heading(title, size=section_header_sizing, margin_top="2rem"),
        rx.text(text, margin_top=main_text_font_sizing, font_size=main_text_font_sizing, line_height="1.6"),
        padding_bottom="1em",
    )

def phase(title: str, bullets: list[str], result: str) -> rx.Component:
    return rx.box(
        rx.heading(title, size=services_header_sizing, margin_top="1.5rem"),
        rx.box(
            rx.vstack(
                rx.list.unordered(
                    *[rx.list_item(b, font_size=main_text_font_sizing) for b in bullets],
                    style={"margin-left": "1.5rem", "margin-top": "0.5rem"}
                ),
                rx.text(f"📌 {result}", font_size=main_text_font_sizing, margin_top="0.5rem", font_style="italic"),
                padding_bottom="1em",
            ),
            padding_left=["1em", "1em", "4em"], 
        ),
    )

def outcomes_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Metric"), 
                rx.table.column_header_cell("Before"), 
                rx.table.column_header_cell("After")
            )
        ),
        rx.table.body(
            *[
                table_row("Time to track past results", "Days–Weeks", "Seconds"),
                table_row("Experiment redundancy", "20–30%", "Near zero"),
                table_row("New student independence", "Low", "High"),
                table_row("PI visibility", "Minimal", "Real-time dashboard"),
                table_row("Data loss from turnover", "High", "Greatly reduced"),
            ]
        ),
        variant="surface",
        margin_top="1rem"
    )

def table_row(metric: str, before: str, after: str) -> rx.Component:
    return rx.table.row(
            rx.table.row_header_cell(metric),
            rx.table.cell(before),
            rx.table.cell(after),
    )

def quote(text: str) -> rx.Component:
    return rx.box(
        rx.text.em(
            f"“{text}”",
            font_size="1.15rem",
            text_align="center",
            padding="1rem",
            max_width="700px",
            margin_x="auto",
            margin_top="2rem",
        )
    )
