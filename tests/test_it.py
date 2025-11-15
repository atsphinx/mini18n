"""Standard tests."""

import shutil
from pathlib import Path

import pytest
from bs4 import BeautifulSoup, Tag
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp):
    """Test to pass."""
    app.build()


@pytest.mark.sphinx("mini18n-html")
def test__custom_builder(app: SphinxTestApp):
    """Test to pass."""
    app.build()
    assert (Path(app.outdir) / "en").exists()
    index_html = Path(app.outdir) / "index.html"
    assert index_html.exists()
    soup = BeautifulSoup(index_html.read_text(), "html.parser")
    assert isinstance(soup.title, Tag)
    assert soup.title.get_text() == app.config.html_title


@pytest.mark.sphinx(
    "mini18n-html", freshenv=True, confoverrides={"mini18n_build_style": "nested"}
)
def test__nested_style(app: SphinxTestApp):
    """Test to pass."""
    shutil.rmtree(app.outdir)  # Refresh outputs
    app.build()
    assert (Path(app.outdir) / "en").exists() is False


@pytest.mark.sphinx(
    "mini18n-revealjs",
    confoverrides={"extensions": ["sphinx_revealjs", "atsphinx.mini18n"]},
)
def test__thirdparty_builder(app: SphinxTestApp):
    """Test to pass."""
    app.build()


@pytest.mark.sphinx(
    "mini18n-revealjs",
    confoverrides={"extensions": ["atsphinx.mini18n", "sphinx_revealjs"]},
)
def test__register_lazy(app: SphinxTestApp):
    """Test to pass."""
    app.build()
