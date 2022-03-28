import boto3
from pprint import pprint
from botocore.exceptions import ClientError


def get_movie(title, year):
    db = boto3.resource("dynamodb")
    table = db.Table("Movies")
    try:
        response = table.get_item(Key={"year": year, "title": title})
    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        return response["Item"]


if __name__ == "__main__":
    movie = get_movie("The Boondock Saints", 1999)
    if movie:
        pprint(movie)
