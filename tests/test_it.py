"""Standard tests."""

from pathlib import Path

import pytest
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
