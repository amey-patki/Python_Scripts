import boto3

s3_client = boto3.client('s3')

# Create a new S3 bucket
s3_client.create_bucket(Bucket='my-new-bucket')

# Upload a file to S3
s3_client.upload_file('local-file.txt', 'my-new-bucket', 'remote-file.txt')
