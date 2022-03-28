import boto3
from pprint import pprint
from botocore.exceptions import ClientError


def delete_movie(title, year):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("Movies")
    try:
        response = table.delete_item(Key={"year": year, "title": title})
    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        print("DeleteItem succeeded:")
        pprint(response)


if __name__ == "__main__":
    delete_movie("Rush", 2013)
