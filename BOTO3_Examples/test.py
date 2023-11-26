import boto3

# Connect to EC2
ec2_client = boto3.client('ec2')

# Start an EC2 instance
response = ec2_client.start_instances(InstanceIds=['Your_Instance_ID'])

# Stop an EC2 instance
response = ec2_client.stop_instances(InstanceIds=['Your_Instance_ID'])

# Terminate an EC2 instance
response = ec2_client.terminate_instances(InstanceIds=['Your_Instance_ID'])


