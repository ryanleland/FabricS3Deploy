import os

from boto.s3.connection import S3Connection
from boto.s3.key import Key

S3_HOST = "s3.amazonaws.com"
DEFAULT_ACL = "public-read"

class S3Storage(object):
    def __init__(self, key, secret, bucket):
        self._aws_key = key
        self._aws_secret = secret
        self._aws_bucket = bucket

    def create_key_from_file(self, file_origin, key_name):
        # Get bucket
        conn = S3Connection(self._aws_key, self._aws_secret)
        bucket = conn.get_bucket(self._aws_bucket)

        # Create a key...
        key = Key(bucket)
        
        # Populate it!
        key.key = key_name
        key.set_contents_from_filename(file_origin, reduced_redundancy=True)

        # Set ACL
        key.set_acl(DEFAULT_ACL)

        archive_url = "http://%s.s3.amazonaws.com/%s" % (self._aws_bucket, key.key)
        return archive_url