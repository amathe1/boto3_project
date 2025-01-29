import boto3

# Create a boto3 session  
session = boto3.Session(  
    aws_access_key_id='YOUR_AWS_ACCESS_KEY_ID',  
    aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY',  
    region_name='ap-south-1'  
)  


# Create an S3 client  
s3 = session.client('s3') 

# List all the buckets in your account  
response = s3.list_buckets()  

# Print the bucket names  
for bucket in response['Buckets']:  
    print(bucket['Name'])  