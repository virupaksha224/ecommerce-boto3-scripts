import boto3
from decimal import Decimal
region = 'us-east-1'
dynamodb = boto3.resource('dynamodb',region_name=region)
table = dynamodb.Table('Products')
product_id = "101"
new_price = Decimal("9.99")
response = table.update_item(
    Key={'ProductID': product_id},
    UpdateExpression="set Price = :p",
    ExpressionAttributeValues={':p': new_price},
    ReturnValues="UPDATED_NEW"
)
print("Price updated:", response['Attributes'])
