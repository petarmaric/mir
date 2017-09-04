#!/usr/bin/env python
import tables as tb # $ pip install tables


filename = 'random-data.mir'


with tb.open_file(filename) as fp:
    print 'Loading the `/geometry/quads` dataset...'
    dataset = fp.root.geometry.quads

    print '\nFirst 5 geometry primitives in the dataset:'
    print dataset[:5]

    print '\nLast vertex of the first 5 geometry primitives in the dataset:'
    print dataset[:5, -3:]

    print '\n`num_vertices` dataset attribute:',
    print dataset._v_attrs.num_vertices
