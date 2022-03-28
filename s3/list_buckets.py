import boto3
from pprint import pprint


"""

s3 = boto3.client('s3')

res = s3.list_buckets()

for bucket in res['Buckets']:
    print(bucket['Name'])
"""

s3 = boto3.resource('s3')
iterator = s3.buckets.all()
for bucket in iterator:
    print(bucket.name)
