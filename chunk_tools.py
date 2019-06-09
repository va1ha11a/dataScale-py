import hashlib
from chunk_store import get_or_create_bucket, put_chunk, get_chunk


def hash_chunk(chunk):
    m = hashlib.sha256()
    m.update(chunk)
    return m.hexdigest()


def get_chunks(file_name):
    with open(file_name, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            yield chunk


def store_chunk(chunk_data, chunk_hash, chunk_len, bucket_loc):
    bucket = chunk_hash[:8]
    get_or_create_bucket(bucket, bucket_loc)
    put_chunk(bucket, chunk_hash, chunk_data, chunk_len)


def restore_chunk(chunk_hash):
    bucket = chunk_hash[:8]
    return get_chunk(bucket, chunk_hash)