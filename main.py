import settings as st

from meta import create_file_meta, create_chunk_node, redis_graph
from chunk_tools import hash_chunk, get_chunks, store_chunk, restore_chunk
from redisgraph import Node, Edge, Graph

if __name__ == "__main__":
    source_file_name = st.source_file_name
    restore_file_name = st.restore_file_name

    meta_file_obj = create_file_meta(source_file_name)

    cnks = get_chunks(source_file_name)
    for order, cnk in enumerate(cnks):
        hsh = hash_chunk(cnk)
        cnk_len = len(cnk)
        store_chunk(cnk, hsh, cnk_len, st.bucket_location)
        create_chunk_node(hsh, order, cnk_len, meta_file_obj)

    redis_graph.commit()

    query = """MATCH (f:file)-[h:has_chunk]->(c:chunk)
            RETURN f.name, h.seq, c.hash ORDER BY h.seq"""

    result = redis_graph.query(query)

    # Print resultset
    result.pretty_print()

    with open(restore_file_name, 'wb') as f:
        for row in result.result_set[1:]:
            chunk = restore_chunk(row[2].decode("utf-8"))
            f.write(chunk)

    # All done, remove graph.
    redis_graph.delete()