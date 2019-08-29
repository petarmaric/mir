Example programs and data files
===============================

An example MIR data file, filled with random data, is available on `our
GitHub repository <https://github.com/petarmaric/mir>`_, under
``examples/random-data.mir``.

Creating a MIR data file
------------------------

The following Python program creates a MIR data file, filled with random data:

.. literalinclude:: examples/create-mir.py

.. note::

    The ``geometry`` layer, while structurally valid, may not contain valid
    geometry primitives due to randomly generated coordinates.

Reading from a MIR data file
----------------------------

The following Python program reads some data from a MIR data file:

.. literalinclude:: examples/read-mir.py
