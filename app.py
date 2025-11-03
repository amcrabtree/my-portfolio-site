import reflex as rx

class State(rx.State):
    pass

app = rx.App(state=State)

def homepage():
    return rx.vstack(
        rx.heading("Angela Crabtree - BioDataWorks"),
        rx.text("AI and ML tools for biological research")
    )

app.add_page(homepage, route="/")
app.compile()
