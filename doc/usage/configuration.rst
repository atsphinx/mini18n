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

   If this is ``None`` , auto-calcurate from these:

   * :confval:`sphinx:language`
   * Directory names of :confval:`sphinx:locale_dirs`
