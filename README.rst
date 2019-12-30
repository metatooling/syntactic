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

.. |docs| image:: https://readthedocs.org/projects/python-syntactic/badge/?style=flat
    :target: https://readthedocs.org/projects/python-syntactic
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/metatooling/python-syntactic.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/metatooling/python-syntactic

.. |codecov| image:: https://codecov.io/github/metatooling/python-syntactic/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/metatooling/python-syntactic

.. |version| image:: https://img.shields.io/pypi/v/syntactic.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/pypi/syntactic

.. |commits-since| image:: https://img.shields.io/github/commits-since/metatooling/python-syntactic/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/metatooling/python-syntactic/compare/v0.1.0...master

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

An example package. Generated with cookiecutter-pylibrary.

* Free software: MIT License

Installation
============

::

    pip install syntactic

Documentation
=============


https://python-syntactic.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
