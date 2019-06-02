# dataScale-py
## Proof of Concept for Data Deduplication.
## Using S3 like storage (minio) and a metatdata db (redisgraph)

This is unlikly to be performant but is for testing the theory (mostly for education pourpouses)

Files are broken into blocks and a hash is generated.
The block and hash (as ID) is stored in the object (block store) if it is not already. The metatdata database tracks what blocks make what file in a given iteration.