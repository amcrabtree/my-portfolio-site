import reflex as rx
from my_portfolio_site.pages import contact, about, services, case_study
from my_portfolio_site.utils import contact_button, about_me_button, get_started_button, case_study_button


#------------------------------------------------
#                  COLOR & THEME
#------------------------------------------------
palette_color_1 = "#bee3b6"
palette_color_2 = "#8fd4cb"
palette_color_3 = "#7998cc"
palette_color_4 = "#765fb0"
palette_color_5 = "#883689"
service_card_color = "#ccf7f0"
background_color = palette_color_2
dark_font_color = "#183E43"

# Font sizing
section_header_sizing = rx.breakpoints(initial="5", sm="6", md="7", lg="8",)
services_header_sizing = rx.breakpoints(initial="3", sm="4", md="5", lg="6",)
main_text_font_sizing = ["1.3em", "1.4em", "1.4em"]
smaller_text_font_sizing = ["1.0em", "1.1em", "1.3em"]
icon_link_sizing = 30
#------------------------------------------------

def ProblemsSection():
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
    return rx.vstack(
        rx.heading("Common Pain Points for Labs", size=services_header_sizing),
        *[
            rx.hstack(
                rx.text(icon, font_size=main_text_font_sizing),
                rx.vstack(
                    rx.text(title, font_weight="bold"),
                    rx.text(desc),
                ),
                padding="1em"
            )
            for (icon, title, desc) in items
        ],
        padding="2em 1em"
    )

def HowItWorksSection():
    phases = [
        ("Phase 1 — Lab Diary & New Data Capture", 
         "Daily logging of experiments, assay metadata, strain IDs, uploaded images/data — all stored in structured JSON."),
        ("Phase 2 — Stock & Strain Registry", 
         "Link physical yeast / cell stocks with genotype/phenotype metadata and track usage across experiments."),
        ("Phase 3 — Historical Data Rescue", 
         "Optionally digitize old gels, notes, images; OCR / metadata tagging / file linking."),
        ("Phase 4 — LLM-Ready Knowledge Base & Query Interface", 
         "Vector embeddings + search interface so you can ask any LLM “What did we do with strain X?”"),
        ("Phase 5 — Optional Analytics & Dashboard", 
         "Trend detection, gap analysis, experiment history summaries, and more.")
    ]
    return rx.vstack(
        rx.heading("How It Works — Step by Step", size=services_header_sizing),
        *[
            rx.vstack(
                rx.heading(phase, size=services_header_sizing),
                rx.text(desc, font_size=main_text_font_sizing),
                padding="1em"
            )
            for phase, desc in phases
        ],
        get_started_button("/services", smaller_text_font_sizing),
        padding="2em"
    )

def WhyUsSection():
    return rx.vstack(
        rx.heading("Why Choose This Service", size=services_header_sizing),
        rx.text("""
            ✔️ Keeps your existing lab workflows — no need to replace notebooks or protocols.  
            ✔️ Delivers immediate value — searchable, organized data from day one.  
            ✔️ Lab-agnostic and LLM-agnostic — works with any dataset, any LLM.  
            ✔️ Scalable: start small (diary) → expand to full archive.  
            ✔️ Built for scientists, by someone who understands lab pain points.
            """, 
        white_space="pre-wrap"
        ),
        case_study_button("/case_study"),
        padding="2em"
    )

def ContactSection():
    return rx.vstack(
        rx.heading("Contact", fontsize=main_text_font_sizing),
        rx.text("Let’s talk about your lab’s needs. I build custom plans for labs of any size."),
        contact_button("/contact"),
        about_me_button("/about"),
        padding="2em"
    )


@rx.page(route="/landing")
def index():
    return rx.box(
        ProblemsSection(),
        HowItWorksSection(),
        WhyUsSection(),
        ContactSection()
    )

app = rx.App()

app.add_page(index, title="BioDataWorks | Lab Knowledge Systems")

