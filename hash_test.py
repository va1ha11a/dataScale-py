import hashlib

# m = hashlib.sha256()
# m.update(b"Nobody inspects")
# m.update(b" the spammish repetition")
# print(m.hexdigest(), m.hexdigest()[:8])

data_file = 'data/test.blk'


def hash_chunk(chunk):
    m = hashlib.sha256()
    m.update(chunk)
    return m.hexdigest()


with open(data_file, 'rb') as f:
    for chunk in iter(lambda: f.read(4096), b''):
        print(hash_chunk(chunk), len(chunk))
