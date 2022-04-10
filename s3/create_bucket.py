import boto3
from pprint import pprint
from botocore.exceptions import ClientError

bucket = boto3.resource('s3')

response = bucket.create_bucket(
    Bucket='boto3lesson',
    ACL='private',
)

print(response)
