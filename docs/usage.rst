=====
Usage
=====


Create a new custom syntax
==============================


1. Make a transformer
--------------------------

Create a function that takes the original unicode source string and returns a new unicode source string.


    .. code-block:: python

        def unicode_lambdas(source: str) -> str:
            """Convert unicode lambdas into regular lambdas."""
            return source.replace("λ", "lambda ")


2. Put that function in a module named ``__syntax__.py``. It may be in a package.


Use a custom syntax
===============================

0. Install ``syntactic``.

1. Install a module that provides a custom syntax plugin.

2. In the module where you want to use the syntax, put the ``syntactic`` coding declaration at the top of the file.

   .. code-block:: python

       # coding: syntactic



3. In the module where you want to use the syntax, import the desired syntax.


   .. code-block:: python

       from __syntax__ import unicode_lambdas


If the module is in a package, namespace the import as normal. For example:

.. code-block:: python

    from syntactic.examples.__syntax__ import unicode_lambdas

4. Write code using the custom syntax. The full module should look like this: ::

    # coding: syntactic

    from __syntax__ import unicode_lambdas

    add_one = λx: x+1

    print(add_one(1))


5. Run the module using the python environment where syntactic is installed. The output should be: ::

     2


View transformed syntax
=========================

View the expanded form of a Python file by using the optional command-line tool.

1. Ensure Syntactic's ``cli`` extra is installed.

2. Use ``python -m syntactic show <filename>``.
