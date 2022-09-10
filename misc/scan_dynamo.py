import boto3
from pprint import pprint
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr


db = boto3.resource("dynamodb")

table = db.Table("boats")


response = table.scan(
    FilterExpression=(Attr("title").eq("qs1") | Attr("title").eq("qs2"))
    & Attr("tags").eq("react")
    & (Attr("media_type").eq("video") | Attr("media_type").eq("blog"))
)
items = response["Items"]
pprint(items)
