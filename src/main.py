import boto3
import os
from dotenv import load_dotenv

load_dotenv()

BUCKET = os.getenv('S3_BUCKET_NAME')
FILE_PATH = 'sales-data-set.json'
S3_KEY = 'sales-data-set.json'


def create_dynamodb_table():
    dynamodb = boto3.resource('dynamodb')

    table_creation_resp = dynamodb.create_table(
        TableName='SalesDataSet',
        KeySchema=[
            {
                'AttributeName': 'Uid',
                'KeyType': 'HASH'  # Partition Key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Uid',
                'AttributeType': 'N'  # string data type
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    print(table_creation_resp)


def upload_to_s3(bucket_name, file_path, s3_key):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f"File uploaded to S3: s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")


if __name__ == '__main__':

    #create_dynamodb_table()
    upload_to_s3(BUCKET, FILE_PATH, S3_KEY)
