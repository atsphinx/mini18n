import os

from atsphinx.mini18n import __version__ as version
from atsphinx.mini18n import get_template_dir as get_mini18n_template_dir

# -- Project information
project = "atsphinx-mini18n"
copyright = "2023, Kazuya Takei"
author = "Kazuya Takei"
release = version

# -- General configuration
extensions = [
    "atsphinx.mini18n",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_tabs.tabs",
]
templates_path = ["_templates", get_mini18n_template_dir()]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for i18n
gettext_compact = False
if "SPHINX_LAST_TRANSLATOR" in os.environ:
    gettext_last_translator = os.environ["SPHINX_LAST_TRANSLATOR"]
locale_dirs = ["_locales"]

# -- Options for HTML output
html_theme = "furo"
html_static_path = ["_static"]
html_title = f"{project} v{release}"
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]
html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/atsphinx/mini18n",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
}
html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "mini18n/snippets/select-lang.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}

# -- Options for extensions
# For sphinx.ext.intersphinx
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
# sphinx.ext.todo
todo_include_todos = True

# atsphinx.mini18n
mini18n_default_language = "en"
mini18n_support_languages = ["en", "ja"]
mini18n_basepath = "/mini18n/"


def setup(app):
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
