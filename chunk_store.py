import io
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

import settings as st

# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio(st.minio_server,
                    access_key=st.minio_access_key,
                    secret_key=st.minio_secret_key,
                    secure=st.minio_secure)


def get_or_create_bucket(bucket_name,
                         bucket_location,
                         minio_connection=minioClient):
    if not minio_connection.bucket_exists(bucket_name):
        minio_connection.make_bucket(bucket_name, location=bucket_location)
        return bucket_name
    else:
        return bucket_name


def put_chunk(bucket,
              chunk_name,
              chunk_data,
              chunk_len,
              minio_connection=minioClient):
    try:
        minio_connection.put_object(bucket, chunk_name, io.BytesIO(chunk_data),
                                    chunk_len)
    except ResponseError as err:
        raise


def get_chunk(bucket, chunk_name, minio_connection=minioClient):
    try:
        chunk = minio_connection.get_object(bucket, chunk_name)
    except ResponseError as err:
        raise
    return chunk.data


if __name__ == "__main__":
    pass
