import boto3
from pprint import pprint
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr


db = boto3.resource("dynamodb")

table = db.Table("boats")


response = table.query(
    KeyConditionExpression=Key("id").eq("04c046ef-7bb9-4582-bfae-6ee0c9fa4e76")
)
items = response["Items"]
print(items)
