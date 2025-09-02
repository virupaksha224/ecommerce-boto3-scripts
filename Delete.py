import boto3
region ='us-east-1'
dynamodb = boto3.resource('dynamodb',region_name=region)
s3 = boto3.client('s3',region_name=region)
table = dynamodb.Table('Products')
bucket = 'products-image-bucket-case-study'
product_id = '101'
# Get item
response = table.get_item(Key={'ProductID': product_id})
item = response['Item']
image_url = item['ImageURL']
image_key = image_url.split('/')[-1]
# Delete from DynamoDB
table.delete_item(Key={'ProductID': product_id})
# Delete image from S3
s3.delete_object(Bucket=bucket, Key=image_key)
print("Product deleted.")
