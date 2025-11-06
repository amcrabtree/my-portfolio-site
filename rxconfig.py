import reflex as rx
from pathlib import Path 
import os

config = rx.Config(
    app_name="my_portfolio_site",
    cors_allowed_origins=[
        "https://my-portfolio-site-s173.onrender.com",
        "http://localhost:3000",
    ],
    allowed_hosts=[
        "https://my-portfolio-site-s173.onrender.com",
        "http://localhost:3000",
    ],
    disable_plugins=['reflex.plugins.sitemap.SitemapPlugin'],
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    rx.run(config, host="0.0.0.0", port=port)