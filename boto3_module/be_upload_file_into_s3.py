import boto3 
    

# Create a boto3 client  
client = boto3.client('s3', 
                      region_name="ap-south-1",
                      aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY',
                      aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID')

# To create a new bucket with given name
response = client.create_bucket(

    Bucket='arun9705',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    })

# Getting list of buckets
response = client.list_buckets()  

# Print the bucket names  
for bucket in response['Buckets']:  
    print(bucket['Name']) 

# To delete a bucket with given name
response = client.delete_bucket(
    Bucket='arun9705',
)

