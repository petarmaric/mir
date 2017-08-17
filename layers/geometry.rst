``geometry`` layer
==================

The ``geometry`` layer has the following geometry primitives, each stored in a
separate dataset:

================  ========  =====  =====  ==========
Dataset name      Vertices  Edges  Faces  Dimensions
================  ========  =====  =====  ==========
``lines``         2         1      0      1
``triangles``     3         3      1      2
``quads``         4         4      1      2
``hexagons``      6         6      1      2
``tetrahedrons``  4         6      4      3
``cuboids``       8         12     6      3
================  ========  =====  =====  ==========

A vertex is a point in 3D space whose coordinates are defined as a ``(x, y,
z)`` triplet, while a single coordinate is represented by a floating point
number.

Each dataset stores a single geometry primitive per row, and has 3 times as
many columns as its corresponding geometry primitive has vertices. This is
because only the coordinates are stored, and each vertex is defined by 3
coordinates.

For example, the ``quads`` dataset requires 12 columns to store its
coordinates, as it has 4 vertices. A single row of this dataset would be layed
out like so:

.. code-block:: python

    # Vertex "A"    Vertex "B"    Vertex "C"    Vertex "D"
    # x   y   z     x   y   z     x   y   z     x   y   z

     1.1 1.2 1.3   2.1 2.2 2.3   3.1 3.2 3.3   4.1 4.2 4.3

Each dataset also has the following attributes attached to it:

``num_vertices``
    Number of vertices, stored as an integer number.

``num_coordinates``
    Number of coordinates, stored as an integer number.

    Equal to: ``num_vertices * 3``
