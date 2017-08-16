``metadata`` layer
==================

The ``metadata`` layer has no datasets, and instead uses the following
attributes to further describe the MIR data file:

``generator_name``
    Name of the program that created the file, stored as a Unicode string.

    For example: ``foobar``

``generator_version``
    Version of the program that created the file, stored as a Unicode string.

    For example: ``1.0.3``

``mir_version``
    Version of MIR specification used when creating the file, stored as a
    Unicode string.

    For example: ``1.12.3``

``created_at``
    Date and time at which the file was created, stored as a Unicode string in
    ISO 8601 format.

    For example: ``2017-08-15T13:51:02+02:00``
