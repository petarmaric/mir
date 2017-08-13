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
