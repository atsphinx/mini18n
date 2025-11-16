===========
Build style
===========

When ``mini18n-*`` builder runs, it generates contents with two different style by :confval:`mini18n_build_style`.

Flat style
==========

.. note:: If configuration is not set, builder uses this.

This style generates contents of all multiple languages into children folders.
And root of build is custom ``index.html`` to redirect to selected language document.

Example
-------

.. code-block:: python
    :caption: conf.py

    mini18n_default_language = "en"
    mini18n_support_languages = ["en", "ja"]
    mini18n_build_style = "flat"

.. code-block:: text

    /
    + index.html     <-- Custom index page (empty content and JavaScript code to jump to language page)
    + en/
      + index.html  <-- Document index page (en)
      + usage.html
      + _static/
    + ja/
      + index.html  <-- Document index page (ja)
      + usage.html
      + _static/

Nested style
============

This style generates contents of default language into root of document multiple languages into children folders.

Example
-------

.. code-block:: python
    :caption: conf.py

    mini18n_default_language = "en"
    mini18n_support_languages = ["en", "ja"]
    mini18n_build_style = "nested"

.. code-block:: text

    /
    + index.html    <-- Document index page (en)
    + usage.html
    + _static/
    + ja/
      +/index.html  <-- Document index page (ja)
      + usage.html
      + _static/


Which style should you use?
===========================

If you manage document for single language, you should use "Nested style".

* Pros: Nested style does not change URL of current contents.
* Cons: It cannot accept docname as same as language code (e.g. ``ja.rst`` )

If you initialize new document and you have will to keep i18n contents,
I recommend to use "Flat style".

* Pros: All contents have URL prefix used language code.
* Cons: If you already manage document, you need to change URL of default language.
