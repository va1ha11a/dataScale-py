import settings as st

from meta import create_file_meta, create_chunk_node, redis_graph
from chunk_tools import hash_chunk, get_chunks, store_chunk, restore_chunk
from redisgraph import Node, Edge, Graph
from pypher import Pypher

# TODO Work out proper way to handle the graph object


def store_file(filename, bucket_loc, graph_obj):
    try:
        meta_file_obj = create_file_meta(filename)
        cnks = get_chunks(filename)
        for order, cnk in enumerate(cnks):
            hsh = hash_chunk(cnk)
            cnk_len = len(cnk)
            store_chunk(cnk, hsh, cnk_len, bucket_loc)
            create_chunk_node(hsh, order, cnk_len, meta_file_obj)
        graph_obj.commit()
    except:
        raise
    else:
        return True


def restore_file(filename, graph_obj):
    try:
        query = Pypher()
        query.Match.node('f',
                         labels='file').rel_out('h', labels='has_chunk').node(
                             'c',
                             labels='chunk').RETURN('f.name', 'h.seq',
                                                    'c.hash').OrderBy('h.seq')
        result = graph_obj.query(str(query))
        #result.pretty_print()
        with open(filename, 'wb') as f:
            for row in result.result_set[1:]:
                chunk = restore_chunk(row[2].decode("utf-8"))
                f.write(chunk)
    except:
        raise
    else:
        return True
