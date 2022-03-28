import boto3
from pprint import pprint
from decimal import Decimal
from botocore.exceptions import ClientError


def update_movie(title, year, rating, plot):
    db = boto3.resource("dynamodb")
    table = db.Table("Movies")
    try:
        response = table.update_item(
            Key={"year": year, "title": title},
            UpdateExpression="set info.rating = :r, info.plot=:p",
            ExpressionAttributeValues={":r": Decimal(rating), ":p": plot},
            ReturnValues="UPDATED_NEW",
        )
    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        return response["Attributes"]


if __name__ == "__main__":
    movie = update_movie("Insidious: Chapter 2", 2013, 5.5, "A classic movie")
    if movie:
        pprint(movie)
