MIR concepts
============

.. warning::

    A valid MIR data file must contain all of the :ref:`layers <mir-layers>`,
    :ref:`datasets <mir-datasets>` and :ref:`attributes <mir-attributes>`
    defined by this specification, even if some of them are empty.

Identifiers
-----------

Identifiers (also referred to as *names*) are described by the following lexical
definitions:

.. productionlist::
    identifier : `first_word` ("_" `word`)*
    first_word : `letter` [`word`]
    word       : (`letter` | `digit`)+
    letter     : "a"..."z"
    digit      : "0"..."9"

where :token:`letter` has to be a lowercase ASCII character.

.. _non-standard-identifiers:

Non-standard identifiers
^^^^^^^^^^^^^^^^^^^^^^^^

Non-standard or vendor specific identifiers must have their names prefixed with
``_x_``:

.. productionlist::
    non_standard_identifier : "_x_" `identifier`

.. _mir-data-types:

Data types
----------

MIR specification defines the following atomic data types:

- integer numbers (signed)
- floating point numbers
- Unicode strings

Data elements using non-standard or vendor specific data types must use a
:ref:`non-standard identifier <non-standard-identifiers>` for their name and
are beyond the scope of MIR specification.

.. _mir-attributes:

Attributes
----------

An attribute is a small metadata object attached directly to a :ref:`dataset
<mir-datasets>` or a :ref:`layer <mir-layers>`, used to describe their nature
and/or intended usage.

Non-standard or vendor specific attributes must use a :ref:`non-standard
identifier <non-standard-identifiers>` for their name and are beyond the scope
of MIR specification.

.. _mir-datasets:

Datasets
--------

A dataset is a rectangular 2D array (generally known as a *matrix*) of data
elements, arranged in rows and columns.

A dataset may use different data types for each column, but all data elements
within a single column must be of the same data type.

Non-standard or vendor specific datasets must use a :ref:`non-standard
identifier <non-standard-identifiers>` for their name and are beyond the scope
of MIR specification.

.. _mir-layers:

Layers
------

Layers are used to organize individual features and properties of a MIR data
file into separate logical groups.

Non-standard or vendor specific layers must use a :ref:`non-standard identifier
<non-standard-identifiers>` for their name and are beyond the scope of MIR
specification.

A MIR data file is composed of the following layers:

.. toctree::

   layers/geometry
   layers/metadata
