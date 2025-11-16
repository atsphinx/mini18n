v0.5.0
======

:Date: 2025-11-17 (Asia/Tokyo)

Features
--------

* Support "Nested style" output.

  * Previously style is "Flat style".

Others
------

* New version requires Python 3.10 and later.
  Drop python 3.8 and 3.9 from support versions.
* New version requires Sphinx 8.0 and later.
* Update workspace.
 
  * It uses aqua instead of mise.
  * It uses latest actions in workflows.
  * When it generate and update translations,
    it refer environment variables for translator name.
  * It uses ty instead of mypy.
  * It updated dependency configurations.

v0.4.1
======

:Date: 2025-05-20 (Asia/Tokyo)

Fixes
-----

* [ `#6`_ ] Simplify process to build href of page with other languages.

  .. _#6: https://github.com/atsphinx/mini18n/issues/6

Others
------

* Mark to support python 3.13.
* Mark as beta product.
* Update workspace environment.

v0.4.0
======

:Date: 2024-05-16 (JST)

Features
--------

* Widget on document remembers selected language when users select it.
