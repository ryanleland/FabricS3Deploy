import os
from fabric.operations import prompt
from s3_storage import S3Storage

# Configuration...
STATIC_DIR = 'static'
AWS_KEY = '14624K6PYCZ4HY8BFF82'
AWS_SECRET = 'kKiV60A9SJfrXsbMBLjjXXZkcpyp7fOhIL9dF6h6'
AWS_BUCKET = 'fabric-s3-deploy'

def deploy_static_files(tag):
    s3_storage = S3Storage(AWS_KEY, AWS_SECRET, AWS_BUCKET)

    for root, _, files in os.walk(STATIC_DIR):
        for f in files:
            file_origin = os.path.join(root, f)
            key_name = tag + "/" + file_origin.split('/', 1)[1]

            s3_storage.create_key_from_file(file_origin, key_name)

def deploy():
    tag = prompt('Please enter tag: ')

    deploy_static_files(tag)