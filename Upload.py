import boto3
import json
import os
from decimal import Decimal
 
AWS_REGION = 'us-east-1'  # Set your region here
dynamodb = boto3.resource('dynamodb',region_name=AWS_REGION)
s3 = boto3.client('s3',region_name=AWS_REGION)
table = dynamodb.Table('Products')
 
BUCKET = 'products-image-bucket-case-study'  # Update to your bucket
 
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError
 
with open('products.json') as f:
    products = json.load(f)
 
for product in products:
    product_id = product['ProductID']
# Check if product already exists in DynamoDB
    try:
        response = table.get_item(Key={'ProductID': product_id})
    except Exception as e:
        print(f"Error fetching product {product_id}: {e}")
        continue
 
    if 'Item' in response:
        print(f"Product {product_id} already exists. Skipping upload.")
        continue  # Skip uploading this product
 
    # Upload image to S3
    image_file = product['ImagePath']
    if not os.path.isfile(image_file):
        print(f"Image file {image_file} does not exist. Skipping product {product_id}.")
        continue
 
    image_key = os.path.basename(image_file)
    try:
        s3.upload_file(image_file, BUCKET, image_key)
    except Exception as e:
        print(f"Failed to upload image {image_file} for product {product_id}: {e}")
        continue
 
    # Add S3 Image URL to product
    image_url = "https://" + BUCKET + ".s3." + AWS_REGION + ".amazonaws.com/" + image_key
    product['ImageURL'] = image_url
 
    # Convert Price to Decimal for DynamoDB
    product['Price'] = Decimal(str(product['Price']))
 
    # Put item in DynamoDB
    try:
        table.put_item(Item=product)
        print(f"Uploaded product {product_id} successfully.")
    except Exception as e:
        print(f"Failed to upload product {product_id} to DynamoDB: {e}")
 
print("Upload process completed.")



