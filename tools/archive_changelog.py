#!/usr/bin/env python
"""Archive changelog tool."""

import shutil
from pathlib import Path

from atsphinx.mini18n import __version__ as version

project_root = Path(__file__).parent.parent
archive_to = project_root / "doc" / "changelogs"


def main():  # noqa: D103
    changes_rst = project_root / "CHANGES.rst"
    shutil.move(changes_rst, archive_to / f"{version}.rst")
    changes_rst.write_text("TEMPLATE")


if __name__ == "__main__":
    main()
