# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
from datetime import date

# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "RC-HPC"
# logo = "_static/logo-square.png"
copyright = f"{date.today().year}, RC"
author = "Research Computing, NU"

# The full version, including alpha/beta/rc tags
release = "3.0.0"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # "myst_nb",
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinxcontrib.spelling",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_design",  # https://pypi.org/project/sphinx_design/
    # "sphinx_tabs.tabs",
    "sphinx_togglebutton",
    # https://sphinx-togglebutton.readthedocs.io/en/latest/use.html
    # "sphinxcontrib.bibtex",
    # "sphinxext.opengraph",
    # For the kitchen sink
    # Our custom extension, only meant for Furo's own documentation.
    "furo.sphinxext",
    # External stuff
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "sphinx.ext.duration",
]

# Prefix document path to section labels, to use:
# `path/to/file:heading` instead of just `heading`
autosectionlabel_prefix_document = True

intersphinx_mapping = {"python": ("https://docs.python.org/3", None),
                       "sphinx": ("https://www.sphinx-doc.org/en/master", None)}

# -- Options for TODOs -------------------------------------------------------
#
todo_include_todos = True

# -- Options for Markdown files ----------------------------------------------
#

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
]

# We need headers to be linkable to so ask MyST-Parser to autogenerate anchor IDs for
# headers up to and including level 3.
myst_heading_anchors = 3
myst_deflist_enable = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["using-ood/cps_ood.md",
                    "_snippets/*",
                    "build",
                    "Thumbs.db",
                    ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
html_title = "RC RTD"

html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/northeastern-rc/rc-public-documentation",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
    # "announcement": """
    # <a style=\"text-decoration: none; color: white;\"
    #    href=\"https://github.com/sponsors/urllib3\">
    #    <img src=\"_static/image/logo-square.png\"/> Submit a ticket for support
    # </a>
    # """,
    "sidebar_hide_name": True,
    # add logo to the upper left in the help system
    "light_logo": "image/nu-logo-light.png",
    "dark_logo": "image/nu-logo-dark.png",
}

# custom css file
html_css_files = ["../css/custom.css"]

# If true, “(C) Copyright …” is shown in the HTML footer. Default is True.
html_show_copyright = True
# If true, “Created using Sphinx” is shown in the HTML footer. Default is True.
html_show_sphinx = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", "_static/video"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

source_suffix = [".rst", ".md"]

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "hpcdoc"

# -- Options for LaTeX output ------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "rcdocs.tex",
        "Documentation for NU-HPC",
        "Research Computer and contributors to the HPC Documentation",
        "manual",
    )
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "rcdocs", "Documentation for NU-HPC", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "RCDocs",
        "Documentation for NU-HPC",
        author,
        "RCDocs",
        "NU-HPC Documentation",
        "Miscellaneous",
    )
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# Warn about all references to unknown targets
nitpicky = True
