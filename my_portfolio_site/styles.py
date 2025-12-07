"""
Centralized styling system for BioDataWorks portfolio site.
This module contains all colors, fonts, spacing, and component styles.
"""

import reflex as rx

# ========================================
# COLOR PALETTE
# ========================================

class Colors:
    """Color palette for the application."""
    # Primary palette
    MINT = "#bee3b6"
    TEAL_LIGHT = "#8fd4cb"
    BLUE = "#7998cc"
    PURPLE = "#765fb0"
    MAGENTA = "#883689"

    # New dark theme colors
    BLACK = "#000000"
    WHITE = "#ffffff"
    JADE = "#5eead4"          # Teal/jade accent color
    TEAL = "#14b8a6"          # Teal accent color

    # Semantic colors
    BACKGROUND = BLACK        # Main background color (now black)
    TEXT = WHITE             # Main text color (now white)
    DARK_FONT = JADE         # Accent text color (jade/teal for highlights)
    SERVICE_CARD = "#1a1a1a"  # Service card background (dark gray)

    # Aliases for easier usage
    PRIMARY = TEAL
    SECONDARY = BLUE
    ACCENT = PURPLE
    HIGHLIGHT = JADE
    EDUCATION = MAGENTA      # For education timeline items
    WORK = BLUE             # For work timeline items


# ========================================
# TYPOGRAPHY
# ========================================

class FontSizes:
    """Responsive font sizes using Reflex breakpoints."""
    # Headings
    SECTION_HEADER = rx.breakpoints(initial="5", sm="6", md="7", lg="8")
    SUBSECTION_HEADER = rx.breakpoints(initial="3", sm="4", md="5", lg="6")

    # Text
    MAIN_TEXT = ["1.3em", "1.4em", "1.4em"]
    SMALL_TEXT = ["1.0em", "1.1em", "1.3em"]

    # Icons
    ICON = 30


class FontStyles:
    """Common font style combinations."""
    BODY = {
        "font_family": "Arial, sans-serif",
        "line_height": "1.6",
    }

    HEADING = {
        "font_family": "Arial, sans-serif",
        "font_weight": "700",
    }


# ========================================
# SPACING
# ========================================

class Spacing:
    """Standard spacing values for consistent layout."""
    # Page-level padding
    PAGE_TOP = "7em"
    PAGE_BOTTOM = "3em"
    PAGE_SIDE = "2rem"

    # Section spacing
    SECTION_TOP = "2rem"
    SECTION_BOTTOM = "2rem"

    # Component spacing
    MARGIN_SMALL = "1rem"
    MARGIN_MEDIUM = "1.5rem"
    MARGIN_LARGE = "2rem"

    PADDING_SMALL = "1rem"
    PADDING_MEDIUM = "1.5rem"
    PADDING_LARGE = "2rem"


# ========================================
# COMPONENT STYLES
# ========================================

# Base styles applied to all pages
base_style = {
    "font_family": "Arial, sans-serif",
    "line_height": "1.6",
}

# Button styles
button_style = {
    "border_radius": "15px",
    "transition": "background-color 0.3s, color 0.3s",
    #"box_shadow": "0px 4px 8px rgba(0, 0, 0, 0.2)",
}

# Card styles
card_style = {
    "border_radius": "15px",
    "padding": Spacing.PADDING_LARGE,
    "box_shadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",
}

# Image styles
image_rounded_style = {
    "border_radius": "10px",
    "box_shadow": "0px 4px 8px rgba(0, 0, 0, 0.1)",
}

# Navbar styles
navbar_style = {
    "bg": rx.color("teal"),
    "font_color": "white",
    "padding": "1em",
    "width": "100%",
    "position": "fixed",
    "z_index": "1000",
}

# Section container styles
section_container_style = {
    "max_width": "900px",
    "margin_x": "auto",
    "padding": Spacing.PAGE_SIDE,
}

# Content container (narrower for text-heavy pages)
content_container_style = {
    "max_width": "800px",
    "margin": "auto",
}


# ========================================
# THEME CONFIGURATION
# ========================================

# Global app styles (can be applied in rxconfig.py)
app_style = {
    "::selection": {
        "background_color": Colors.BLUE,
        "color": "white",
    },
    "body": {
        "margin": "0",
        "padding": "0",
        "font_family": "Arial, sans-serif",
    },
}
