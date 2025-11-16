"""Sphinx builder for i18n site on single deployment."""

from __future__ import annotations

from dataclasses import dataclass, field, fields
from pathlib import Path
from subprocess import PIPE, run
from typing import TYPE_CHECKING, ClassVar, Literal

from jinja2 import Template
from sphinx.builders.dummy import DummyBuilder

if TYPE_CHECKING:
    from docutils import nodes
    from sphinx.application import Sphinx
    from sphinx.config import Config


__version__ = "0.5.0"

package_root = Path(__file__).parent.resolve()


@dataclass
class BuildArgs:
    """Parameter class to build other language."""

    app: Sphinx
    builder: str
    lang: str
    use_lang_dir: bool = True


@dataclass
class ExtensionConfig:
    """Config for this extension from Sphinx config object."""

    PREFIX: ClassVar[str] = "mini18n_"

    build_style: Literal["flat", "nested"] = "flat"
    default_language: str | None = None
    support_languages: list[str] = field(default_factory=list)
    basepath: str = "/"
    select_lang_label: str = "Language:"

    @classmethod
    def from_sphinx(cls, config: Config) -> "ExtensionConfig":
        """Create from Sphinx config object."""
        kv = {
            f.name: getattr(config, f"{cls.PREFIX}{f.name}")
            for f in fields(cls)
            if hasattr(config, f"{cls.PREFIX}{f.name}")
        }
        return cls(**kv)


class Mini18nBuilderBase(DummyBuilder):
    """Abstract bridge builder to build multi-language settings."""

    name_prefix = "mini18n-"

    def finish(self):  # noqa: D102
        config = ExtensionConfig.from_sphinx(self.config)
        if config.build_style == "flat":
            self.finish_tasks.add_task(self.build_heading_content)
        if config.default_language:
            self.finish_tasks.add_task(
                build_i18_contents,
                BuildArgs(
                    self.app,
                    self.name[len(self.name_prefix) :],
                    config.default_language,
                    config.build_style == "flat",
                ),
            )
        for lang in config.support_languages:
            if lang == config.default_language:
                continue
            self.finish_tasks.add_task(
                build_i18_contents,
                BuildArgs(self.app, self.name[len(self.name_prefix) :], lang),
            )

    def build_heading_content(self):
        """Generate root index file."""
        ctx = {
            "config": self.app.config,
        }
        out_template = Path(__file__).parent / "templates" / "mini18n" / "index.html"
        template = Template(out_template.read_text())
        out_index = (
            Path("/".join([self.app.outdir, "index.html"]))
            if isinstance(self.app.outdir, str)
            else self.app.outdir / "index.html"
        )
        Path(out_index).write_text(template.render(ctx))


def build_i18_contents(args: BuildArgs):
    """Run build for coufigured language."""
    if args.use_lang_dir:
        lang_out_dir = (
            "/".join([args.app.outdir, args.lang])
            if isinstance(args.app.outdir, str)
            else args.app.outdir / args.lang  # type: ignore[unsupported-operator]
        )
    else:
        lang_out_dir = args.app.outdir
    cmd = [
        "sphinx-build",
        "-b",
        args.builder,
        "-d",
        args.app.doctreedir,
        args.app.srcdir,
        lang_out_dir,
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
        config.mini18n_default_language = config.language  # type: ignore[attr-defined]
    if not config.mini18n_support_languages:
        config.mini18n_support_languages = [config.mini18n_default_language]  # type: ignore[attr-defined]
    if not config.html_context:
        config.html_context = {}  # type: ignore[attr-defined]
    config.html_context["mini18n"] = {
        "basepath": config.mini18n_basepath,
        "support_languages": config.mini18n_support_languages,
        "select_lang_label": config.mini18n_select_lang_label,
    }


# TODO: Find other api to register function.
def bind_pathto_with_lang(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict,
    doctree: nodes.document,
):
    """Add template functions into context."""
    config = ExtensionConfig.from_sphinx(app.config)

    def pathto_with_lang(otheruri: str, lang: str) -> str:
        """Create path info to specified page and language.

        :param otheruri: Target pagename of document.
        :param lang: Target language that is defined on ``mini18n_support_languages``.
        :returns: URL to page as absolute path.
        """
        if config.build_style == "nested" and lang == config.default_language:
            lang = ""
        else:
            lang = f"{lang}/"
        pathto = app.builder.get_target_uri(otheruri)
        return f"{context['mini18n']['basepath']}{lang}{pathto}"

    print(app.config.language, config)
    context["pathto_with_lang"] = pathto_with_lang
    pass


def get_template_dir() -> str:  # noqa: D103
    return str(package_root / "templates")


def setup(app: Sphinx):  # noqa: D103
    app.add_config_value("mini18n_build_style", "flat", "env")
    app.add_config_value("mini18n_default_language", None, "env")
    app.add_config_value("mini18n_support_languages", [], "env")
    app.add_config_value("mini18n_basepath", "/", "env")
    app.add_config_value("mini18n_select_lang_label", "Language:", "env")
    app.connect("config-inited", autocomplete_config)
    app.connect("html-page-context", bind_pathto_with_lang)

    # IMPORTANT!!
    # This is very dirty hack to work it for any builders of third-party extensions.
    _preload_builder = app.preload_builder

    def preload_builder(buildername):
        """Wrap for :meth:`sphinx.application.Sphinx.preload_builder`."""
        register_i18n_builders(app)
        _preload_builder(buildername)

    app.preload_builder = preload_builder  # type: ignore[method-assign]

    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
