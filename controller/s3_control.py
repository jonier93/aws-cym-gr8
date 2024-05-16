from boto3.session import Session
from botocore.exceptions import ClientError
from keys import ACCESS_KEY, SECRET_KEY

def connection_s3():
    try:
        sesion_aws = Session(ACCESS_KEY, SECRET_KEY)
        s3_connection = sesion_aws.resource('s3')
        print("Succesfull connection to s3")
        return s3_connection
    except ClientError as err:
        print("Error connecting to s3", err)
        return None

def upload_file_s3(s3_connection):
    path_local = "requirements.txt"
    bucket_name = "my-repo-images"
    path_s3 = "images/" + path_local
    s3_connection.meta.client.upload_file(path_local, bucket_name, path_s3)