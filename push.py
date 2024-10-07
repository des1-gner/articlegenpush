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

# Function to upload an item to DynamoDB
def upload_item(item):
    try:
        # Ensure articleId is present
        if 'articleId' not in item:
            print(f"Skipping item: Missing articleId")
            return False

        # Create a cleaned item dictionary
        cleaned_item = {}
        
        # Handle the articleId separately to ensure it's a number
        cleaned_item['articleId'] = int(item['articleId']['N'])
        
        # Handle all other fields
        for key, value in item.items():
            if key != 'articleId':  # Skip articleId as we've already handled it
                if isinstance(value, dict):
                    if 'S' in value:  # Handle string type
                        cleaned_item[key] = value['S']
                    # Add more type handlers here if needed
                else:
                    cleaned_item[key] = value

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
    else:
        print(f"\nVerification failed: No article found with ID {sample_id}")

except ClientError as e:
    print(f"\nError querying table: {e.response['Error']['Message']}")
except Exception as e:
    print(f"\nUnexpected error during verification: {str(e)}")
