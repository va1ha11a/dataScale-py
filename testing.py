from pypher import Pypher

q = Pypher()
q.Match.node('mark', labels='Person').WHERE.mark.property('name') == 'Mark'
q.RETURN.mark

p = Pypher()
p.Match.node('f', labels='file').rel_out('h', labels='has_chunk').node(
    'c', labels='chunk').RETURN('f.name', 'h.seq', 'c.hash').OrderBy('h.seq')
print(p)
"""MATCH (f:file)-[h:has_chunk]->(c:chunk)
            RETURN f.name, h.seq, c.hash ORDER BY h.seq"""