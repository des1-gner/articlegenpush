import json
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2')

# Specify your table name
table_name = 'lazone'
table = dynamodb.Table(table_name)

# Load the JSON data
with open('climate_news_data.json', 'r') as file:
    data = json.load(file)

def process_value(value):
    if isinstance(value, dict):
        if 'S' in value:
            return value['S']
        elif 'N' in value:
            return int(value['N'])
        elif 'BOOL' in value:
            return value['BOOL']
        elif 'M' in value:
            return {k: process_value(v) for k, v in value['M'].items()}
        else:
            return {k: process_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [process_value(item) for item in value]
    else:
        return value

# Function to upload an item to DynamoDB
def upload_item(item):
    try:
        # Ensure articleId is present
        if 'articleId' not in item:
            print(f"Skipping item: Missing articleId")
            return False

        # Create a cleaned item dictionary
        cleaned_item = {}
        
        # Process all fields
        for key, value in item.items():
            cleaned_item[key] = process_value(value)

        # Upload the item
        table.put_item(Item=cleaned_item)
        print(f"Successfully uploaded article {cleaned_item['articleId']}")
        return True
    except ClientError as e:
        print(f"Error uploading article {item.get('articleId', {}).get('N', 'unknown')}: {e.response['Error']['Message']}")
        return False
    except Exception as e:
        print(f"Unexpected error uploading article {item.get('articleId', {}).get('N', 'unknown')}: {str(e)}")
        return False

# Upload each item to DynamoDB
successful_uploads = 0
failed_uploads = 0
for item in data:
    if upload_item(item):
        successful_uploads += 1
    else:
        failed_uploads += 1

print(f"\nUpload Summary:")
print(f"Successfully uploaded: {successful_uploads}")
print(f"Failed uploads: {failed_uploads}")
print(f"Total items processed: {len(data)}")

# Verify the upload by querying the table
try:
    # Query for a specific articleId (using the first article's ID as an example)
    sample_id = int(data[0]['articleId']['N'])
    response = table.query(
        KeyConditionExpression=Key('articleId').eq(sample_id)
    )
    
    if response['Items']:
        print(f"\nVerification successful: Found article with ID {sample_id}")
        print(f"Number of items found: {len(response['Items'])}")
        print("Sample item structure:")
        print(json.dumps(response['Items'][0], indent=2))
    else:
        print(f"\nVerification failed: No article found with ID {sample_id}")
except ClientError as e:
    print(f"\nError querying table: {e.response['Error']['Message']}")
except Exception as e:
    print(f"\nUnexpected error during verification: {str(e)}")
