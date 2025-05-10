#!/usr/bin/env python
"""Wapper to ``age`` CLI.

age cannot copy and move files in updating process.
"""

import argparse
import shutil
from pathlib import Path
from subprocess import run

from atsphinx.mini18n import __version__ as version

project_root = Path(__file__).parent.parent
archive_to = project_root / "doc" / "changelogs"

parser = argparse.ArgumentParser()
parser.add_argument("age_args", nargs="+")  # All arguments are passed to age-cli.


def main(args: argparse.Namespace):  # noqa: D103
    # Move changelog into document to use as old logs.
    changes_rst = project_root / "CHANGES.rst"
    shutil.move(str(changes_rst), archive_to / f"{version}.rst")
    changes_rst.write_text("TEMPLATE")
    # Run age.
    run(["age"] + args.age_args)


if __name__ == "__main__":
    main(parser.parse_args())
