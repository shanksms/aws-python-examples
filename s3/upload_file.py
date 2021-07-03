from s3.secrets import access_secret, access_key
import boto3
import os

client = boto3.client('s3', aws_access_key_id=access_key,
                      aws_secret_access_key=access_secret)
bucket_name = 'testuploadshanks'


def upload():
    bucket_name = 'testuploadshanks'
    upload_file_key = 'test/test.txt'
    client.upload_file('test.txt', bucket_name, upload_file_key)


def download():
    with open('file_from_s3.txt', 'wb') as f:
        client.download_fileobj(bucket_name, "test/test.txt", f)


if __name__ == '__main__':
    download()

