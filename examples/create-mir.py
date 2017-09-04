#!/usr/bin/env python
from datetime import datetime
import os

import numpy as np # $ pip install numpy
import tables as tb # $ pip install tables
from tzlocal import get_localzone # $ pip install tzlocal


filename = 'random-data.mir'

sample_num_rows = 100
geometry_primitives = [
    # dataset_name , num_vertices
    ('lines'       , 2),
    ('triangles'   , 3),
    ('quads'       , 4),
    ('hexagons'    , 6),
    ('tetrahedrons', 4),
    ('cuboids'     , 8),
]


filters = tb.Filters(complib='zlib', complevel=1, shuffle=True, fletcher32=True)
with tb.open_file(filename, 'w', filters=filters) as fp:
    geometry_layer = fp.create_group(where='/', name='geometry')
    for dataset_name, num_vertices in geometry_primitives:
        num_coordinates = num_vertices * 3 # num_coordinates_per_vertex

        dataset = fp.create_earray(
            where=geometry_layer,
            name=dataset_name,
            atom=tb.Float64Atom(),
            shape=(0, num_coordinates),
        )
        dataset._v_attrs.num_vertices = num_vertices
        dataset._v_attrs.num_coordinates = num_coordinates

        dataset.append(np.random.rand(sample_num_rows, num_coordinates))

    metadata_layer = fp.create_group(where='/', name='metadata')
    metadata_layer._v_attrs.generator_name = __file__
    metadata_layer._v_attrs.generator_version = '1.0'
    metadata_layer._v_attrs.mir_version = '0.1'
    metadata_layer._v_attrs.created_at = datetime.now(get_localzone()).replace(
        microsecond=0
    ).isoformat()
