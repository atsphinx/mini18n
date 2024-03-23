from atsphinx.mini18n import __version__ as version

# -- Project information
project = "atsphinx-mini18n"
copyright = "2023, Kazuya Takei"
author = "Kazuya Takei"
release = version

# -- General configuration
extensions = [
    "sphinx.ext.todo",
    "sphinx_tabs.tabs",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "furo"
html_static_path = ["_static"]
html_title = f"{project} v{release}"

# -- Options for extensions
# sphinx.ext.todo
todo_include_todos = True
