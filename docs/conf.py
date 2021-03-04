import os

# -- Project information -----------------------------------------------------

project = "example"
copyright = "2021, aiden-jeon"
author = "aiden-jeon"

# The full version, including alpha/beta/rc tags
release = "0.1"


# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_rtd_theme",
    "autoapi.extension",
    "sphinx.ext.napoleon",
]

autoapi_type = "python"
autoapi_dirs = [
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]