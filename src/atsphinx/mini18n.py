"""Sphinx builder for i18n site on single deployment."""

from subprocess import PIPE, run

from sphinx.application import Sphinx
from sphinx.builders.dummy import DummyBuilder

__version__ = "0.0.0"


class Mini18nBuilderBase(DummyBuilder):
    """Abstract bridge builder to build multi-language settings."""

    name_prefix = "mini18n-"

    def init(self):  # noqa: D102
        self.app.connect("build-finished", self.build_i18_contents)

    def build_i18_contents(self, app, err):
        """Run build for coufigured multi-languages."""
        cmd_base = [
            "sphinx-build",
            "-b",
            self.name[len(self.name_prefix) :],
            "-d",
            app.doctreedir,
            app.srcdir,
        ]
        for lang in [app.config.language]:
            cmd = cmd_base + ["/".join([self.outdir, lang]), "-D", f"laungage={lang}"]
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


def setup(app: Sphinx):  # noqa: D103
    register_i18n_builders(app)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
