import boto3
from pprint import pprint


def create_movie_table(db=None):
    if not db:
        db = boto3.resource("dynamodb")
    table = db.create_table(
        TableName="Movies",
        KeySchema=[
            {"AttributeName": "year", 
            "KeyType": "HASH"}, 
            {"AttributeName": "title", 
            "KeyType": "RANGE"}
            ],
        AttributeDefinitions=[
            {"AttributeName": "year", 
            "AttributeType": "N"},
            {"AttributeName": "title", 
            "AttributeType": "S"},
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 10, 
            "WriteCapacityUnits": 10
            },
    )

    return table


if __name__ == "__main__":
    movie_table = create_movie_table()
    print(movie_table.item_count)
