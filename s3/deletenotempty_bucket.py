import boto3

BUCKET_NAME = "parwizforogh7777"

s3 = boto3.resource('s3')

s3_bucket = s3.Bucket(BUCKET_NAME)


def clean_up():

    # delete the object
    for s3_object in s3_bucket.objects.all():
        s3_object.delete()

    # delete bucket versioning

    for s3_object_ver in s3_bucket.object_versions.all():
        s3_object_ver.delete()

    print("S3 bucket cleaned")


# delete the objects in the buckets and their versions
clean_up()

# delete the bucket itself
s3_bucket.delete()

print("The bucket has been deleted")
