import reflex as rx
from my_portfolio_site.styles import Colors, FontSizes, Spacing
from my_portfolio_site.utils import (
    contact_button,
    navbar_dropdown,
)

@rx.page(route="/case_study")
def case_study_page() -> rx.Component:
    return rx.box(
        navbar_dropdown(),
        rx.box(
        rx.vstack(
            # Header
            rx.heading(
                "Case Study — Unlocking a Yeast Lab's Hidden Knowledge",
                size=FontSizes.SECTION_HEADER,
                text_align="center",
                margin_bottom="1rem",
                color=Colors.TEXT,
            ),
            rx.text.em(
                "How BioDataWorks helped a virus–host research lab unlock years of experimental data.",
                font_size=FontSizes.MAIN_TEXT,
                text_align="center",
                max_width="800px",
                margin_x="auto",
                margin_bottom="2rem",
                color=Colors.TEXT,
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
            rx.heading("🚀 The BioDataWorks Solution", size=FontSizes.SECTION_HEADER, margin_top="2rem", color=Colors.TEXT),
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
            rx.heading("🔥 Outcomes", size=FontSizes.SECTION_HEADER, margin_top="2rem", color=Colors.TEXT),
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
                    "Let's modernize your lab's knowledge — without disrupting what works.",
                    font_size=FontSizes.MAIN_TEXT,
                    font_weight="600",
                    text_align="center",
                    margin_bottom="1rem",
                    color=Colors.TEXT,
                ),
                rx.hstack(
                    contact_button("/contact"),
                    justify="center",
                ),
                margin_top="2rem",
            ),

            max_width="900px",
            margin_x="auto",
            padding=Spacing.PAGE_SIDE,
            ),
        padding_top=Spacing.PAGE_TOP,
        ),
        background_color=Colors.BACKGROUND,
    )

# --- Reusable Helper Components ---

def section(title: str, text: str) -> rx.Component:
    return rx.box(
        rx.heading(title, size=FontSizes.SECTION_HEADER, margin_top="2rem", margin_bottom="1rem", color=Colors.JADE),
        rx.text(text, font_size=FontSizes.MAIN_TEXT, line_height="1.6", color=Colors.TEXT),
        padding_bottom="2rem",
    )

def phase(title: str, bullets: list[str], result: str) -> rx.Component:
    return rx.box(
        rx.heading(title, size=FontSizes.SUBSECTION_HEADER, margin_top="1.5rem", margin_bottom="1rem", color_scheme="teal"),
        rx.box(
            rx.vstack(
                rx.list.unordered(
                    *[rx.list_item(b, font_size=FontSizes.SMALL_TEXT, color=Colors.TEXT) for b in bullets],
                    style={"margin-left": "1.5rem", "margin-top": "0.5rem"}
                ),
                rx.text(f"📌 {result}", font_size=FontSizes.SMALL_TEXT, margin_top="1rem", font_style="italic", color=Colors.TEXT),
                padding_bottom="2rem",
            ),
            padding_left=Spacing.PAGE_SIDE,
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
            f"\"{text}\"",
            font_size=FontSizes.MAIN_TEXT,
            text_align="center",
            padding="2rem",
            max_width="700px",
            margin_x="auto",
            margin_top="2rem",
            color=Colors.JADE,
        )
    )
