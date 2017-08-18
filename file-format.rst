MIR file format
===============

MIR is backed up by the `HDF5 <https://www.hdfgroup.org/hdf5/>`_ data file
format.

HDF5 is an extensible and open standard, comprised of platform independent
technologies which are available under Open Source licenses. HDF5 format has
been designed with the objective of creating data storages that are
self-descriptive, flexible, and have extremely fast and efficient access
patterns to the stored data.

.. note::

    Although not mandatory, MIR data files should have the ``.mir`` extension
    (lowercase), for easier identification on the file system.

HDF5 key concepts
-----------------

Although HDF5 key concepts are best explained by the `HDF5 User's Guide
<https://support.hdfgroup.org/HDF5/doc/UG/HDF5_Users_Guide-Responsive%20HTML5/>`_,
a quick overview is given bellow for readers convenience:

Group
    A collection of HDF5 objects (including other groups).

    As suggested by its name "Hierarchical Data Format", an HDF5 file is
    hierarchically structured, like a tree. This tree structure is very similar
    to the file system structures employed on UNIX systems, with directories
    and files. HDF5 groups are analogous to the directories, HDF5 datasets are
    analogous to the files.

    Every HDF5 data file has at least one object, the root group. All other
    objects (including groups) are either members of the root group or its
    descendants.

Dataset
    A multidimensional array of data elements, together with supporting
    metadata.

    An HDF5 dataset is an object composed of a collection of data elements and
    metadata that stores a description of the data elements, data layout, and
    all other information necessary to write, read, and interpret the stored
    data.

Data type
    A description of a specific class of data element including its storage
    layout as a pattern of bits.

    HDF5 data types implement a flexible, extensible, and portable mechanism
    for specifying and discovering the storage layout of the data elements,
    determining how to interpret the elements (for example, as float­ing point
    numbers), and for transferring data from different compatible layouts.

    Atomic data types are indivisible. Composite data types are composed of
    multiple elements of atomic data types.

    In addition to the standard types, users can define additional custom data
    types.

Attribute
    A small metadata object attached to a group or a dataset.

    Attributes are a critical part of what makes HDF5 a "self-describing"
    format. They are small named pieces of data attached directly to group or
    dataset objects. This is the official way to store metadata in HDF5.

Mapping MIR concepts onto HDF5
------------------------------

In general, MIR concepts map cleanly onto their HDF5 counterparts:

=========  =========
MIR        HDF5
=========  =========
Data type  Data type
Attribute  Attribute
Dataset    Dataset
Layer      Group
=========  =========

Detailed MIR/HDF5 data type map:

- integer numbers are stored as 32-bit signed integers, using the
  ``H5T_STD_I32LE`` HDF5 data type
- floating point numbers are stored as IEEE 754 binary64, using the
  ``H5T_IEEE_F64LE`` HDF5 data type
- all Unicode strings are UTF-8 encoded

Additionally, each MIR layer (HDF5 group) is a child of the root HDF5 group.
