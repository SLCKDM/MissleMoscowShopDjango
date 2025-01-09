from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = '484904b8-a054c098-0d89-4419-81d4-315f026935d6'
    location = 'media'


class StaticStorage(S3Boto3Storage):
    bucket_name = '484904b8-a054c098-0d89-4419-81d4-315f026935d6'
    location = 'static'
