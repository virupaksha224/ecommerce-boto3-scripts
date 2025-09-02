import boto3
from datetime import datetime, timedelta

region = 'us-east-1'  # Change to your region
instance_id = 'i-0acef99e30249d57b'  # Replace with your EC2 instance ID

cloudwatch = boto3.client('cloudwatch', region_name=region)
ec2 = boto3.client('ec2', region_name=region)

# Define time range for metrics (last 24 hours)
end_time = datetime.utcnow()
start_time = end_time - timedelta(days=1)

# Get CPU Utilization metrics
metrics = cloudwatch.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
    StartTime=start_time,
    EndTime=end_time,
    Period=300,  # 5 minutes
    Statistics=['Average']
)
print("CPU Metrics:")
for datapoint in metrics['Datapoints']:
    print(f"Time: {datapoint['Timestamp']}, Average CPU: {datapoint['Average']}%")

# List CloudWatch alarms
alarms = cloudwatch.describe_alarms()
print("\nCloudWatch Alarms:")
for alarm in alarms['MetricAlarms']:
    print(f"Name: {alarm['AlarmName']}, State: {alarm['StateValue']}")
