import boto3
import json

def lambda_handler(event, context):
    # Initialize a DynamoDB client
    dynamo_client = boto3.client('dynamodb')

    # Name of the DynamoDB table
    table_name = 'Inventory'

    # Scan the table
    try:
        response = dynamo_client.scan(TableName=table_name)
        items = response['Items']

        return {
            'statusCode': 200,
            'body': json.dumps(items, default=str)  # Use str to handle any special types like Decimal
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
