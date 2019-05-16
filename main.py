import hashlib

from meta import create_file_meta, create_chunk_node, redis_graph
from block import get_or_create_bucket, put_chunk, get_chunk
import settings as st

from redisgraph import Node, Edge, Graph

def hash_chunk(chunk):
    m = hashlib.sha256()
    m.update(chunk)
    return m.hexdigest()

def get_chunks(file_name):
    with open(file_name, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            yield chunk

def store_chunk(chunk_data, chunk_hash, chunk_len, bucket_loc=st.bucket_location):
    bucket = chunk_hash[:8]
    get_or_create_bucket(bucket, bucket_loc)
    put_chunk(bucket, chunk_hash, chunk_data, chunk_len)

def restore_chunk(chunk_hash):
    bucket = chunk_hash[:8]
    return get_chunk(bucket, chunk_hash)

if __name__ == "__main__":
    source_file_name = st.source_file_name
    restore_file_name = st.restore_file_name

    meta_file_obj = create_file_meta(source_file_name)

    cnks = get_chunks(source_file_name)
    for order, cnk in enumerate(cnks):
        hsh = hash_chunk(cnk)
        cnk_len = len(cnk)
        store_chunk(cnk, hsh, cnk_len)
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