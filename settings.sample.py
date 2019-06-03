"""
File to use as template for settings.
Replace all double squigly bracket varibles with true varibles in a given environment.
Reanme file to settings.py

"""
source_file_name = '{{SOURCE_FILENAME}}'
restore_file_name = '{{RESTORE_FILENAME}}'
bucket_location = '{{BUCKET_LOC}}'

minio_server = '{{MINIO_SERVER_NAME_IP}}:{{MINIO_SERVER_PORT_INT}}'
minio_access_key = "{{MINIO_ACCESS_KEY}}"
minio_secret_key = "{{MINIO_SECRET_KEY}}"
minio_secure = {{MINIO_SECURE_BOOL}}
# TODO: Workout what needs to happen to make secure true.

meta_server = '{{META_SERVER_NAME_IP}}'
meta_port = {{META_SERVER_PORT_INT}}
