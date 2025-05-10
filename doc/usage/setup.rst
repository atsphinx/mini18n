=====
Setup
=====

To first build, you should runs two step.

Install
=======

.. warning:: After publish first version package.

This is published on PyPI.
You can install by ``pip`` command or your package management tools.

.. tabs::

   .. tab:: pip-command

      .. code:: console

         pip install atsphinx-mini18n

   .. tab:: pyproject.toml

      .. code:: toml

         [project]
         dependencies = [
             "atsphinx-mini18n",
         ]

Configuration
=============

At first, register extension into your ``conf.py`` of documentation.

.. code-block:: python
   :name: conf.py

   extensions = [
       "atsphinx.mini18n",
   ]

First build
===========

After setup, documentation has new builder ``mini18n-html`` and ``mini18n-dirhtml``.

Please build document by new builders.

.. code:: console

   $ make mini18n-html
   $ ls _build/mini18n-html
   index.html en
