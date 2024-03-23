================
atsphinx-mini18n
================

.. image:: https://github.com/atsphinx/mini18n/actions/workflows/main.yml/badge.svg?branch=main
   :target: https://github.com/atsphinx/mini18n/actions/workflows/main.yml

Sphinx builder for i18n site on single deployment.

Overview
========

This provides custom builders that generate html document per translated languages on to outdir.

.. code:: console

   $ cd /path/to/doc
   $ cat conf.py
   ...
   mini18n_support_languages = ["en", "ja"]
   ...

   $ make mini18n-html
   $ ls _build/mini18n-html
   en index.html ja

Getting started
===============

You should ready for i18n configurations and manage translated files.

Install
-------

.. code:: console

   pip install atsphinx-mini18n

Configuration
-------------

.. code:: python

   extensions = [
       "atsphinx.mini18n",
   ]

   mini18n_default_language = "en"
   mini18n_support_languages = ["en", "ja"]

Run build
---------

.. code:: console

   $ make mini18n-html

   OR

   $ make mini18n-dirhtml
