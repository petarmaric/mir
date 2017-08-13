MIR concepts
============

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

.. _mir-layers:

Layers
------

Layers are used to organize individual features and properties of a MIR data
file into separate logical groups.

Non-standard or vendor specific layers must use a :ref:`non-standard identifier
<non-standard-identifiers>` for their name and are beyond the scope of MIR
specification.
