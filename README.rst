========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://img.shields.io/readthedocs/syntactic
    :target: https://readthedocs.org/projects/syntactic
    :alt: Documentation Status

.. |travis| image:: https://img.shields.io/travis/com/metatooling/syntactic
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/metatooling/syntactic

.. |codecov| image:: https://codecov.io/github/metatooling/syntactic/coverage.svg
    :alt: Coverage Status
    :target: https://codecov.io/github/metatooling/syntactic

.. |version| image:: https://img.shields.io/pypi/v/syntactic.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/pypi/syntactic

.. |commits-since| image:: https://img.shields.io/github/commits-since/metatooling/syntactic/v0.1.3.svg
    :alt: Commits since latest release
    :target: https://github.com/metatooling/syntactic/compare/v0.1.3...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/syntactic.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/pypi/syntactic

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/syntactic.svg
    :alt: Supported versions
    :target: https://pypi.org/pypi/syntactic

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/syntactic.svg
    :alt: Supported implementations
    :target: https://pypi.org/pypi/syntactic


.. end-badges


https://syntactic.readthedocs.io/

Customizable syntax for Python.

Possible uses
==================

- Experimenting with possible language features.
- Boilerplate reduction.





Examples
==========

Unicode lambdas
-------------------

.. code-block:: python

    from __syntax__ import unicode_lambda

    func = λx: x + 1

is equivalent to

.. code-block:: python

    func = lambda x: x + 1

SQL template literals
------------------------

Embedded sql:

.. code-block:: js

  from __syntax__ import sql_literals

  engine.query(sql`SELECT author FROM books WHERE name = {book} AND author = {author}`)

is equivalent to:

.. code-block:: python

    engine.query('SELECT author FROM books WHERE name = ? AND author = ?', [book, author])


Limitations
===============

The example transformers are written in a fragile way. They are intended only as
inspiration rather than production-ready transformers. If you want to add some
production-ready ones, pull-requests are welcome.




Related work
===================

Several projects have explored manipulating Python syntax.

- MacroPy_
- future-fstrings_
- experimental_

.. _MacroPy:  http://macropy3.readthedocs.io/en/latest/
.. _future-fstrings: https://github.com/asottile/future-fstrings
.. _experimental: https://github.com/aroberge/experimental
