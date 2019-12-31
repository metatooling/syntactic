=====
Usage
=====


Create a new custom syntax
==============================


1. Make a transformer
--------------------------

Create a function that takes the original unicode source string and returns a new unicode source string.


    .. code-block:: python

        def convert_unicode_lambda(source: str) -> str:
            """Convert unicode lambdas into regular lambdas."""
            return source.replace("λ", "lambda ")


2. Make a plugin
------------------------


Make a plugin so ``syntactic`` can find your function.


... if you're using setuptools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update your ``setup.py`` to include the plugin entry point.

.. code-block:: python

    setuptools.setup(
        ...,
        entry_points={
            "syntactic.transformers": [
                "unicode_lambda = my_package.my_module:convert_unicode_lambda"
            ]
        },
    )



... if you're using Poetry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update your ``pyproject.toml`` to include the entry point.

.. code-block:: toml

    [tool.poetry.plugins."syntactic.transformers"]
    unicode_lambda = "my_package.my_module:convert_unicode_lambda"




Use a custom syntax
===============================

0. Install ``syntactic``.

1. Install a module that provides a custom syntax plugin.

2. In the module where you want to use the syntax, put the ``syntactic`` coding declaration at the top of the file.

   .. code-block:: python

       # coding: syntactic



3. In the module where you want to use the syntax, import the desired syntax.


   .. code-block:: python

       from __syntax__ import unicode_lambda


4. Write code using the custom syntax. The full module should look like this: ::

    # coding: syntactic

    from __syntax__ import unicode_lambda

    add_one = λx: x+1

    print(add_one(1))


5. Run the module using the python environment where syntactic is installed. The output should be: ::

     2


View transformed syntax
=========================

View the expanded form of a Python file by using the optional command-line tool.

1. Ensure Syntactic's` ``cli`` extra is installed.

2. Use ``python -m syntactic show <filename>``.
