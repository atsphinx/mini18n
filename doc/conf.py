from atsphinx.mini18n import __version__ as version

# -- Project information
project = "atsphinx-mini18n"
copyright = "2023, Kazuya Takei"
author = "Kazuya Takei"
release = version

# -- General configuration
extensions = [
    "atsphinx.mini18n",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_tabs.tabs",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for i18n
gettext_compact = False
locale_dirs = ["_locales"]

# -- Options for HTML output
html_theme = "furo"
html_static_path = ["_static"]
html_title = f"{project} v{release}"

# -- Options for extensions
# For sphinx.ext.intersphinx
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
# sphinx.ext.todo
todo_include_todos = True

# atsphinx.mini18n
mini18n_default_language = "ja"


def setup(app):
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
