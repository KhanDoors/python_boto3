import boto3


def list_policies():
    iam = boto3.client("iam")

    paginator = iam.get_paginator("list_policies")

    for response in paginator.paginate():
        for policy in response["Policies"]:
            print(policy["PolicyName"])


list_policies()
