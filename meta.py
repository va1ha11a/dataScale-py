import redis

from redisgraph import Node, Edge, Graph

r = redis.Redis(host='localhost', port=6379)
redis_graph = Graph('chunks', r)

def create_file_meta(file_name, graph_obj=redis_graph):
    this_file = Node(label='file', properties={'name': file_name})
    graph_obj.add_node(this_file)
    return this_file

def create_chunk_node(chunk_hash, chunk_seq, chunk_len, file_obj):
    this_cnk = Node(label='chunk', properties={'hash': chunk_hash, 'length': chunk_len})
    redis_graph.add_node(this_cnk)
    this_edge = Edge(file_obj, 'has_chunk', this_cnk, properties={'seq': chunk_seq})
    redis_graph.add_edge(this_edge)
    return this_cnk, this_edge

