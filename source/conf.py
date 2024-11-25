# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Art Manager'
copyright = '2024, Cora Weidner'
author = 'Cora Weidner'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# https://www.sphinx-doc.org/en/master/usage/extensions/index.html
extensions = [
    # "sphinx.ext.autodoc",               # Include documentation from docstrings
    "sphinx.ext.autosectionlabel",      # Allow referencing sections by their title
    # "sphinx.ext.autosummary",           # Generate autodoc summaries
    # "sphinx.ext.coverage",              # Collect doc coverage stats
    # "sphinx.ext.doctest",               # Test snippets in the documentation
    # "sphinx.ext.duration",              # Measure durations of Sphinx processing
    # "sphinx.ext.extlinks",              # Markup to shorten external links
    # "sphinx.ext.githubpages",           # Publish HTML docs in GitHub Pages
    "sphinx.ext.graphviz",              # Add Graphviz graphs
    # "sphinx.ext.ifconfig",              # Include content based on configuration
    "sphinx.ext.imgconverter",          # A reference image converter using Imagemagick
    # "sphinx.ext.inheritance_diagram",   # Include inheritance diagrams
    # "sphinx.ext.intersphinx",           # Link to other projects’ documentation
    # "sphinx.ext.linkcode",              # Add external links to source code
    "sphinx.ext.mathjax",               # Render math via JavaScript
    # "sphinx.ext.napoleon",              # Support for NumPy and Google style docstrings
    # "sphinx.ext.todo",                  # Support for todo items
    # "sphinx.ext.viewcode",              # Add links to highlighted source code
    # === Third Party Extensions ===
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

# Figures, tables and code-blocks are automatically numbered if they have a caption.
numfig = True
# A dictionary mapping 'figure', 'table', 'code-block' and 'section' to strings that are used for
# format of figure numbers. The marker %s will be replaced with the figure number.
#numfig_format = {}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# html_logo = "_static/favicon.svg"
html_favicon = "_static/favicon.svg"
html_last_updated_fmt = "%b %d, %Y"
html_show_copyright = True

