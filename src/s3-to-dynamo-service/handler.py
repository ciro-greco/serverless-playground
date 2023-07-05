import boto3
import json


def lambda_handler(event, context):
    # Get the S3 bucket name and key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Create a DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    s3 = boto3.client('s3')


    # Specify the DynamoDB table name
    table_name = 'SalesDataSet'
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        json_data = response['Body'].read().decode('utf-8')
        items = json.loads(json_data)

        # Write each item in the JSON to DynamoDB
        table = dynamodb.Table(table_name)
        with table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': 'Data successfully written to DynamoDB'
        }

    except Exception as e:
        return {
        'statusCode': 500,
        'body': f'Error: {str(e)}'
    }