import boto3
from django.conf import settings

from h_dubbed.settings import BASE_DIR


class Bucket:
    access_key = 'bl8ddcmgima61cpg'
    secret_key = '85d332c1-93ee-4c41-b33d-606d80237de1'
    endpoint_url = 'https://storage.iran.liara.space'
    bucket_name = 'shop-key'
    local_storage = f'{BASE_DIR}/aws/'
    """CDN BUCKET MANAGER

    INIT METHOD CREATES CONNECTION.
    NOTE:
    none of these method are async
    """
    def __init__(self):
        session = boto3.session.Session()
        self.conn = session.client(
            service_name='s3',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            endpoint_url=self.endpoint_url,
        )

    def get_objects(self):
        result = self.conn.list_objects_v2(Bucket=self.bucket_name)
        if result['KeyCount']:
            return result['Contents']
        else:
            return None

    def delete_object(self, key):
        self.conn.delete_object(Bucket=self.bucket_name, Key=key)
        return True

    def download_object(self, key):
        with open(self.local_storage + key, 'wb') as f:
            self.conn.download_fileobj(self.bucket_name, key, f)


bucket = Bucket()