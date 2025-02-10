import boto3
import os
from werkzeug.utils import secure_filename

s3_client = boto3.client('s3',
                         aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                         aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

def upload_file_to_s3(file):
    filename = secure_filename(file.filename)
    s3_client.upload_fileobj(file, os.getenv('AWS_BUCKET_NAME'), filename)
    return f"https://{os.getenv('AWS_BUCKET_NAME')}.s3.amazonaws.com/{filename}"

def delete_file_from_s3(filename):
    s3_client.delete_object(Bucket=os.getenv('AWS_BUCKET_NAME'), Key=filename)
