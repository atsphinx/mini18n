=============
Configuration
=============

Option values
=============

There are some options to customize behavior.

.. confval:: mini18n_default_language

   :Type: ``str``
   :Default: ``None``
   :Exaple: ``"ja"``

   This is defined lauguage to redirect when root of document.

   If this is ``None`` , use :confval:`sphinx:language`.

.. confval:: mini18n_support_languages

   :Type: ``list[str]``
   :Default: ``None``
   :Exaple: ``["en", "ja"]``

   Target list to build document with ``-D language=XX`` argument.
   You should set explicitly to build per languages.

   If this is ``None`` , complete to [:confval:`mini18n_default_language`].

Snippets
========

You can emmbed snippets in document to navigate easily.

Example: set into document used "Furo" theme
--------------------------------------------

.. code-block:: python
   :name: conf.py

   from atsphinx.mini18n import get_template_dir

   # Setup
   extensions = [
       "atsphinx.mini18n",
   ]
   templates_path = [
       # ... Your templates
       get_template_dir(),
   ]

   # atsphinx.mini18n
   mini18n_default_language = "ja"
   mini18n_support_languages = ["en", "ja"]

   # Insert snippets into sidebar of Furo.
   html_sidebars = {
       "**": [
           "sidebar/scroll-start.html",
           "sidebar/brand.html",
           "mini18n/snippets/select-lang.html",
           "sidebar/search.html",
           "sidebar/navigation.html",
           "sidebar/ethical-ads.html",
           "sidebar/scroll-end.html",
       ]
   }
