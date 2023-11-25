import boto3

# Connect to EC2
ec2_client = boto3.client('ec2')

# Start an EC2 instance
response = ec2_client.start_instances(InstanceIds=['i-06e7e79154c9abdf1'])

# Stop an EC2 instance
response = ec2_client.stop_instances(InstanceIds=['i-06e7e79154c9abdf1'])

# Terminate an EC2 instance
response = ec2_client.terminate_instances(InstanceIds=['i-06e7e79154c9abdf1'])


