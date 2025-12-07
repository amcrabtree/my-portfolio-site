import reflex as rx
from my_portfolio_site.utils import contact_button, get_started_button, case_study_button
from my_portfolio_site.pages import about, case_study, contact, services

# Font sizing
section_header_sizing = rx.breakpoints(initial="5", sm="6", md="7", lg="8",)
services_header_sizing = rx.breakpoints(initial="3", sm="4", md="5", lg="6",)
main_text_font_sizing = ["1.3em", "1.4em", "1.4em"]
smaller_text_font_sizing = ["1.0em", "1.1em", "1.3em"]


# ---------- Section components ----------

def hero_section():
    return rx.center(
        rx.vstack(
            rx.image(
                src="/biodataworks_logo_smallest.png",
                width=["150px", "200px", "300px"],
                height="auto",
            ),
            rx.heading(
                "BioDataWorks",
                size=rx.breakpoints(initial="6", sm="7", md="8", lg="9",),
                text_align="center",
                margin_top="1rem",
                color_scheme="jade",
            ),
            rx.heading(
                "AI-Ready Lab Knowledge Systems for Life Sciences", 
                size=section_header_sizing,
                text_align="center",
                margin_top="1rem",
            ),
            rx.text(
                "Transform your lab’s data, images, and notebook history into a single searchable, future-proof knowledge base — usable with any LLM.",
                font_size=main_text_font_sizing,
                text_align="center",
                max_width="700px",
                margin_top="1rem",
                padding_bottom=["1em", "1em", "2em"], 
            ),
            rx.hstack(
                get_started_button("/services", smaller_text_font_sizing),
                contact_button("/contact", smaller_text_font_sizing),
            ),
            align="center",
            spacing="5"
        ),
        padding_bottom=["1em", "1em", "4em"], 
        align="center",
    )

def problems_section():
    items = [
        ("📄", "Lost experiments & repeated work", 
         "Track experiments, assays, images and data — without hoping someone remembers."),
        ("🧪", "Scattered files & unlabeled stocks", 
         "Connect yeast stocks, samples, gels, dsRNA assays, and data files with metadata."),
        ("📚", "Handwritten notebooks = locked history", 
         "Add a lightweight lab-diary + metadata layer so nothing gets lost again."),
        ("🔍", "Hard to search across years of work", 
         "Enable instant search, filter, and retrieval — even decades old files.")
    ]
    return rx.box(
        rx.vstack(
            rx.heading("No more lost data.", size=section_header_sizing),
            align="center",
        ),
        rx.box(
            *[
            rx.hstack(
                rx.text(icon, font_size=main_text_font_sizing),
                rx.vstack(
                    rx.text(title, font_weight="bold", font_size=main_text_font_sizing),
                    rx.text(desc, font_size=smaller_text_font_sizing),
                ),
                padding="1em",
                padding_left="8em",
            )
            for (icon, title, desc) in items
            ],
        ),
        padding_top="5em"
    )

def how_it_works_section():
    phases = [
        ("Phase 1 — Lab Diary & New Data Capture", 
         "Daily logging of experiments, assay metadata, strain IDs, uploaded images/data — all stored in structured JSON."),
        ("Phase 2 — Stock & Strain Registry", 
         "Link physical cell stocks with genotype/phenotype metadata and track usage across experiments."),
        ("Phase 3 — Historical Data Rescue", 
         "Optionally digitize old gels, notes, images; OCR / metadata tagging / file linking."),
        ("Phase 4 — LLM-Ready Knowledge Base & Query Interface", 
         "Vector embeddings + search interface so you can ask any LLM “What did we do with strain X?”"),
        ("Phase 5 — Optional Analytics & Dashboard", 
         "Trend detection, gap analysis, experiment history summaries, and more.")
    ]
    return rx.box(
        rx.vstack(
            rx.heading("How it works", size=section_header_sizing),
            align="center",
        ),
        rx.box(
            *[
            rx.hstack(
                rx.vstack(
                    rx.heading(phase, size=services_header_sizing, color_scheme="teal",),
                    rx.text(desc, font_size=smaller_text_font_sizing),
                ),
                padding="2em",
                padding_left="8em",
            )
            for (phase, desc) in phases
            ],
        ),
        padding_top="5em",
    )

def why_us_section():
    return rx.box(
        rx.vstack(rx.heading("Why Choose This Service", size=section_header_sizing), align="center"),
        rx.vstack(
            rx.list(
                rx.list.item("✔️ Keeps your existing lab workflows — no need to replace notebooks or protocols."),
                rx.list.item("✔️ Delivers immediate value — searchable, organized data from day one."),
                rx.list.item("✔️ Lab-agnostic and LLM-agnostic — works with any dataset, any LLM.  "),
                rx.list.item("✔️ Scalable: start small (diary) → expand to full archive.  "),
                rx.list.item("✔️ Built for scientists, by someone who understands lab pain points."),
                font_size=main_text_font_sizing,
                spacing="5",
            ),
            
            padding="2em",
            padding_left="8em",
        ),
        rx.vstack(
            case_study_button("/case_study"),
            align="center",
        ),
        padding_top="5em",
    )


def index():
    return rx.box(
        hero_section(),
        problems_section(),
        how_it_works_section(),
        why_us_section(),
        padding="4em",
    )


# ---------- App Setup ----------
app = rx.App()

app.add_page(index, title="BioDataWorks | Lab Knowledge Systems")

if __name__ == "__main__":
    app.run()
