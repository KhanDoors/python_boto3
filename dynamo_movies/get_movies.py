import boto3
from pprint import pprint
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

"""You are also able to chain conditions together using the logical operators: & (and), | (or), and ~ (not). For example, this scans for all users whose first_name starts with J and whose account_type is super_user:

response = table.scan(
    FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
)
items = response['Items']
print(items)
"""


def get_movies(year):
    db = boto3.resource("dynamodb")
    table = db.Table("Movies")
    response = table.query(KeyConditionExpression=Key("year").eq(year))
    return response["Items"]


if __name__ == "__main__":
    movie = get_movies(2011)
    for item in movie:
        print(item["year"], item["title"], item["info"]["release_date"])
