import reflex as rx
from pathlib import Path 
import os

config = rx.Config(
    app_name="my_portfolio_site",
    allowed_hosts=["my-portfolio-site-s173.onrender.com", "localhost",],
    cors_allowed_origins=["https://my-portfolio-site-s173.onrender.com", "http://localhost:3000",],
    disable_plugins=['reflex.plugins.sitemap.SitemapPlugin'],
)