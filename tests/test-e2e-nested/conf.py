# noqa: D100
from atsphinx.mini18n import get_template_dir

extensions = [
    "atsphinx.mini18n",
]

html_sidebars = {"**": [f"{get_template_dir()}/mini18n/snippets/select-lang.html"]}

mini18n_default_language = "en"
mini18n_support_languages = ["en", "ja"]
mini18n_build_style = "nested"
