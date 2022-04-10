import boto3

s3 = boto3.client('s3')

with open('react.png', 'rb') as f:
    data = f.read()

response = s3.put_object(
    Bucket='boto3lesson',
    ACL='private',
    Body=data,
    Key='react.png',
)

print(response)
