=====
Usage
=====


Create a new custom syntax
==============================


1. Create a function that takes the original unicode source string and returns a new unicode source string.

    .. code-block:: python

        def convert_double_exclamations(source: str) -> str:
            """Convert double exclamations into a greeting."""
            return source.replace("!!", 'print("hello")')


2. Make a plugin so ``syntactic`` can find your function.



Using setuptools
----------------

Update your ``setup.py`` to include the plugin entry point.

.. code-block:: python

    setuptools.setup(
        ...,
        entry_points={
            "syntactic.transformers": [
                "bangbang_means_hello = my_package.my_module:convert_double_exclamations"
            ]
        },
    )



Using Poetry
-------------

Update your ``pyproject.toml`` to include the entry point.

.. code-block:: toml

    [tool.poetry.plugins."syntactic.transformers"]
    bangbang_means_hello = "my_package.my_module:convert_double_exclamations"




Use a custom syntax
===============================

1. Install a module that provides a custom syntax plugin.

2. In the module where you want to use the syntax, put the ``syntactic`` coding declaration at the top of the file.

   .. code-block:: python

       # coding: syntactic



3. In the module where you want to use the syntax, import the desired syntax.


   .. code-block:: python

       from __syntax__ import bangbang_means_hello


4. Write code using the custom syntax. The full module should look like this:

.. code-block::

    # coding: syntactic

    from __syntax__ import bangbang_means_hello

    print(1+1)
    !!
    print(2+2)


5. Run the module using the python environment where syntactic is installed. The output should be: ::

     1
     hello
     2



View transformed syntax
=========================

View the expanded form of a Python file by using the optional command-line tool.

1. Ensure Syntactic's` ``cli`` extra is installed.

2. Use ``python -m syntactic show file.py``.
