"""Sphinx builder for i18n site on single deployment."""

from dataclasses import dataclass
from pathlib import Path
from subprocess import PIPE, run

from jinja2 import Template
from sphinx.application import Sphinx
from sphinx.builders.dummy import DummyBuilder
from sphinx.config import Config

__version__ = "0.1.0"

package_root = Path(__file__).parent.resolve()


@dataclass
class BuildArgs:
    """Parameter class to build other langage."""

    app: Sphinx
    builder: str
    lang: str


class Mini18nBuilderBase(DummyBuilder):
    """Abstract bridge builder to build multi-language settings."""

    name_prefix = "mini18n-"

    def finish(self):  # noqa: D102
        self.finish_tasks.add_task(self.build_heading_content)
        for lang in self.app.config.mini18n_support_languages:
            self.finish_tasks.add_task(
                build_i18_contents,
                BuildArgs(self.app, self.name[len(self.name_prefix) :], lang),
            )

    def build_heading_content(self):
        """Generate root index file."""
        ctx = {
            "config": self.app.config,
        }
        out_index = self.app.outdir + "/index.html"
        out_template = Path(__file__).parent / "templates" / "mini18n" / "index.html"
        template = Template(out_template.read_text())
        Path(out_index).write_text(template.render(ctx))


def build_i18_contents(args: BuildArgs):
    """Run build for coufigured language."""
    cmd = [
        "sphinx-build",
        "-b",
        args.builder,
        "-d",
        args.app.doctreedir,
        args.app.srcdir,
        "/".join([args.app.outdir, args.lang]),
        "-D",
        f"language={args.lang}",
    ]
    run(cmd, stdout=PIPE, stderr=PIPE)


def register_i18n_builders(app: Sphinx):
    """Create and register dynamic builder for html output."""
    new_builders = []
    for name, Builder in app.registry.builders.items():
        if Builder.format != "html":
            continue

        class Mini18nBuilder(Mini18nBuilderBase):
            pass

        Mini18nBuilder.name = f"mini18n-{name}"

        new_builders.append(Mini18nBuilder)
    for builder_class in new_builders:
        app.add_builder(builder_class)


def autocomplete_config(app: Sphinx, config: Config):
    """Calucrate extension's config values."""
    if not config.mini18n_default_language:
        config.mini18n_default_language = config.language
    if not config.mini18n_support_languages:
        config.mini18n_support_languages = [config.mini18n_default_language]
    if not config.html_context:
        config.html_context = {}
    config.html_context["mini18n"] = {
        "support_languages": config.mini18n_support_languages,
    }


def get_template_dir() -> str:  # noqa: D103
    return str(package_root / "templates")


def setup(app: Sphinx):  # noqa: D103
    register_i18n_builders(app)
    app.add_config_value("mini18n_default_language", None, "env")
    app.add_config_value("mini18n_support_languages", [], "env")
    app.connect("config-inited", autocomplete_config)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
