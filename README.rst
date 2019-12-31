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

.. |docs| image:: https://readthedocs.org/projects/syntactic/badge
    :target: https://readthedocs.org/projects/syntactic
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/metatooling/syntactic.svg
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/metatooling/syntactic

.. |codecov| image:: https://codecov.io/github/metatooling/syntactic/coverage.svg
    :alt: Coverage Status
    :target: https://codecov.io/github/metatooling/syntactic

.. |version| image:: https://img.shields.io/pypi/v/syntactic.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/pypi/syntactic

.. |commits-since| image:: https://img.shields.io/github/commits-since/metatooling/syntactic/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/metatooling/syntactic/compare/v0.1.0...master

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

Customizable syntax for Python.


https://syntactic.readthedocs.io/


Examples
==========

Unicode lambdas
-------------------

.. code-block:: python

    # coding: syntactic

    from __syntax__ import unicode_lambda

    func = λ x: x + 1

    assert func(1) == 2
