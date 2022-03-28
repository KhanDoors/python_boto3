import os
import logging
import json
import boto3
from botocore.exceptions import ClientError
from boto3.s3.transfer import TransferConfig
import requests

# s3 = boto3.client('s3')
# s3.upload_file('C:/Users/syyad/Pictures/tech/slider-5.png',
#                'khandoor', 'test1.png')

bucket_name = "khandoor"
region_name = "us-east-1"


def list_buckets(region=None):
    # Create bucket
    s3_client = boto3.client('s3')
    try:
        if region is not None:
            s3_client = boto3.client('s3', region_name=region)
        response = s3_client.list_buckets()
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')
    except ClientError as e:
        logging.error(e)
        return False
    return True


list_buckets(region_name)

