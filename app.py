import reflex as rx

# 1. Define your app
app = rx.App()

# 2. Define your state (optional)
class State(rx.State):
    pass

# 3. Define your pages
def homepage():
    return rx.vstack(
        rx.heading("Angela Crabtree - BioDataWorks"),
        rx.text("AI and ML tools for biological research")
    )

# 4. Add page to app
app.add_page(homepage, route="/")

# 5. Compile app
app.compile()
