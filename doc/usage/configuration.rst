=============
Configuration
=============

Option values
=============

There are some options to customize behavior.

.. confval:: mini18n_build_style

    :Type: ``str`` ( ``"flat"`` or ``"nested"`` )
    :Default: ``"flat"``
    :Example: ``"nested""`

    Folder structure of output by builder.

    For detail, please see :doc:`./build-style`.


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

.. confval:: mini18n_basepath

   :Type: ``str``
   :Default: ``/``
   :Exaple: ``"/mini18n/"``

   This is used to build navigate URL on root document.
   You edit it if document is deployed on sub-directory of domains.

   .. note:: Value must be end with slash.

.. confval:: mini18n_select_lang_label

   :Type: ``str``
   :Default: ``"Language:"``
   :Example: ``"Lang:"``

   This is used as label text for language select-box on snippet.

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

Example: for "PyData Sphinx Theme"
----------------------------------

.. code-block:: python
   :name: conf.py

   from atsphinx.mini18n import get_template_dir

   # Setup
   templates_path = [
       # ... Your templates
       get_template_dir(),
   ]

   # Insert snippets into header.
   html_theme_options = {
       # Override it.
       "navbar_start": [
           "navbar-logo",
           "mini18n/snippets/select-lang",
       ],
   }
