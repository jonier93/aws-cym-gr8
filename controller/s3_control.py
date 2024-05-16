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

def save_file(id, photo):
    photo_extension = photo.filename.split(".")[1]
    photo_path = "/tmp/" + id + "." + photo_extension
    photo.save(photo_path)
    return photo_path

def upload_file_s3(s3_connection, photo_path):
    bucket_name = "my-repo-images"
    path_s3 = "images/" + photo_path.split("/")[2]
    s3_connection.meta.client.upload_file(photo_path, bucket_name, path_s3)
    

    