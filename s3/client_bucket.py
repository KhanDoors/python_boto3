import boto3

client - boto3.client('s3')

response = client.create_bucket(
    Bucket='boto3lesson2',
    ACL='private',
)

print(response)
