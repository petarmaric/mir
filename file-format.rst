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

Recommended optimizations
-------------------------

.. _hdf5-chunking:

Chunked storage layout
^^^^^^^^^^^^^^^^^^^^^^

What is chunking:

    The storage layout defines how the raw data values in the dataset are
    physically stored on disk. There are three ways that a dataset can be
    stored: contiguous, chunked, and compact.

    If the storage layout is contiguous, then the raw data values will be
    stored physically adjacent to each other in the HDF5 file (in one
    contiguous block). This is the default layout for a dataset.

    With a chunked storage layout the data is stored in equal-sized blocks or
    chunks of a pre-defined size. The HDF5 library always writes and reads the
    entire chunk. Each chunk is stored as a separate contiguous block in the
    HDF5 file. There is a chunk index which keeps track of the chunks
    associated with a dataset.

    Chunked storage makes it possible to resize datasets, and because the data
    is stored in fixed-size chunks, to use compression filters.

    -- https://support.hdfgroup.org/HDF5/Tutor/layout.html

Although not mandatory, it's still strongly advised to use the chunked storage
layout when creating MIR data files to improve processing performance:

    It is commonly used when subsetting very large datasets. Using the chunking
    layout can greatly improve performance when subsetting large datasets,
    because only the chunks required will need to be accessed. However, it is
    easy to use chunking without considering the consequences of the chunk
    size, which can lead to strikingly poor performance.

    If a very small chunk size is specified for a dataset it can cause the
    dataset to be excessively large and it can result in degraded performance
    when accessing the dataset. The smaller the chunk size the more chunks that
    HDF5 has to keep track of, and the more time it will take to search for a
    chunk.

    An entire chunk has to be read and uncompressed before performing an
    operation. There can be a performance penalty for reading a small subset,
    if the chunk size is substantially larger than the subset.

    -- https://support.hdfgroup.org/HDF5/Tutor/layout.html

Compression and error detection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When an HDF5 dataset is created, optional filters can be specified. These
filters are added to the data transfer pipeline when data is read or written.
The HDF5 standard library includes filters to implement transparent
compression, data shuffling, and error detection code.

.. warning::

    To apply a filter to an HDF5 dataset it must be created with a
    :ref:`chunked storage layout <hdf5-chunking>`.

Although not mandatory, it's still strongly advised to apply the following
filters when creating MIR data files to minimize disk storage requirements and
improve processing performance:

Compression
    Enable the transparent compression filter to save storage space.

    Data is compressed on the way to disk, and automatically decompressed when
    read. Once the dataset is created with a particular compression filter
    applied, data may be read and written as normal with no special steps
    required.

    Although many interesting `3rd party compression filters are supported
    <https://support.hdfgroup.org/services/filters.html>`_, HDF5 itself
    provides only 2 pre-defined filters for compression by default: ZLIB and
    SZIP. SZIP can't be used freely due to licensing issues, therefore ZLIB is
    recommended for maximum portability.

    For best overall ZLIB performance the `PyTables optimization guide
    <http://www.pytables.org/usersguide/optimization.html#compression-issues>`_
    advises the lowest compression level (1) to be used.

Shuffle
    Enable the shuffle filter to improve the compression ratio.

    Block-oriented compressors work better when presented with runs of similar
    values. The shuffle filter rearranges the bytes in the chunk and may
    improve compression ratio. No significant speed penalty.

Fletcher32
    Adds an error detection checksum to each chunk to detect data corruption.

    Attempts to read corrupted chunks will fail with an error. No significant
    speed penalty.
