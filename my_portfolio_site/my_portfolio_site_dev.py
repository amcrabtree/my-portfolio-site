import reflex as rx
from my_portfolio_site.pages import services, contact, case_study, landing
from my_portfolio_site.utils import contact_button, get_started_button, learn_more_button

# ---------- Color & Theme Settings ----------
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
                #style={"font_family": "Playwrite NO",},
            ),
            rx.heading(
                "AI-Ready Lab Knowledge Systems for Life Sciences", 
                size=section_header_sizing,
                text_align="center",
                margin_top="1rem",
                #style={"font_family": "Playwrite NO",},
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
                learn_more_button("/landing", smaller_text_font_sizing),
                contact_button("/contact", smaller_text_font_sizing),
            ),
            align="center",
            spacing="5"
        ),
        padding=["1em", "1em", "4em"], 
        
        align="center",
    )


def index():
    return rx.box(
        hero_section(), 
    )

# ---------- App Setup ----------
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Playwrite+NO:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
    ],
)

app.add_page(index, title="BioDataWorks | Lab Knowledge Systems")

if __name__ == "__main__":
    app.run()
