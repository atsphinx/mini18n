"""Tests for JavaScript layer."""

import http.server
import socket
import threading
import time
from pathlib import Path
from typing import Tuple

import pytest
from playwright.sync_api import Page
from sphinx.testing.util import SphinxTestApp


class ServerOnPytest(http.server.ThreadingHTTPServer):
    """Wrapper class to work using pytest tmpdir and random port."""

    def _is_port_in_use(self, port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(("localhost", port)) == 0

    def __init__(self, directory: Path, port_range: Tuple[int, int] = (49152, 60999)):
        """Initialize server with found usable port.

        Default port-range is ephemeral ports.
        """
        self.directory = directory
        for v in range(port_range[0], port_range[1] + 1):
            if not self._is_port_in_use(v):
                self.port = v
                break
            raise ValueError("All ports are already used.")
        return super().__init__(("", self.port), http.server.SimpleHTTPRequestHandler)

    def finish_request(self, request, client_address):  # noqa: D102
        self.RequestHandlerClass(
            request, client_address, self, directory=self.directory
        )

    def __enter__(self):  # noqa: D105
        self._thread = threading.Thread(target=self.serve_forever)
        self._thread.daemon = True
        self._thread.start()
        return super().__enter__()

    def __exit__(self, *args, **kwargs):  # noqa: D105
        print(args, kwargs)
        super().__exit__()
        self.shutdown()


@pytest.mark.sphinx("mini18n-html", testroot="e2e")
def test__root(app: SphinxTestApp, page: Page):
    app.build()
    with ServerOnPytest(app.outdir) as server:
        url = f"http://localhost:{server.port}/"
        page.goto(url)
        time.sleep(0.5)
        assert page.url.endswith("/en/")


@pytest.mark.sphinx("mini18n-html", testroot="e2e")
def test__select_language(app: SphinxTestApp, page: Page):
    app.build()
    with ServerOnPytest(app.outdir) as server:
        url = f"http://localhost:{server.port}/"
        page.goto(url)
        time.sleep(0.5)
        assert page.url.endswith("/en/")
        assert not page.context.cookies()
        element = page.get_by_label("Language:")
        element.select_option(label="ja")
        element.evaluate(
            "elm => elm.dispatchEvent(new Event('change', {bubbles: true}))"
        )
        time.sleep(0.5)
        assert page.url.endswith("/ja/index.html")
        cookies = page.context.cookies()
        assert cookies[0]["name"] == "lang"
        assert cookies[0]["value"] == "ja"
        page.goto(url)
        time.sleep(0.5)
        assert page.url.endswith("/ja/")
