import reflex as rx
from pathlib import Path 

config = rx.Config(
    app_name="my_portfolio_site",
    cors_allowed_origins=[
        "https://my-portfolio-site-69zu.onrender.com",
        "https://my-portfolio-site-1.onrender.com",
        "http://localhost:3000",
    ],
    allowed_hosts=[
        "https://my-portfolio-site-69zu.onrender.com",
        "https://my-portfolio-site-1.onrender.com",
        "http://localhost:3000",
    ],
    disable_plugins=['reflex.plugins.sitemap.SitemapPlugin'],
)