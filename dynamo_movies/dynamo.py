import boto3
from pprint import pprint

db = boto3.client("dynamodb")
# db = boto3.resource("dynamodb")

# table = db.Table("projects")
# res = db.describe_table(TableName="boats")
res = db.list_tables()
# res = db.get_item(TableName="projects", Key={"id": {"S": "1"}})
# res = table.scan()
# data = res["Items"]

pprint(res["TableNames"])
