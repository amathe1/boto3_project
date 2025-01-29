import boto3

# Creating  a client session for RDS using region name, aws_access_key_id & aws_secret_access_key
client = boto3.client('rds', region_name="ap-south-1",aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY',aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID')

# Deletig an existing instance
# DB instance ID is enough, make sure to skip final snapshot & delete any automated backup's
response = client.delete_db_instance(
    DBInstanceIdentifier='newpoc',
    SkipFinalSnapshot=True,
    DeleteAutomatedBackups=True
)

# To cross check if any RDS is available
response = client.describe_db_instances()
print(response)

# To create a new RDS in AWS
# DBInstanceIdentifier is the name of RDS
# Engine must be your expected RDBMS name
# Provide user name and password using MasterUsername & MasterUserPassword properties
response = client.create_db_instance(
    DBName='mysqldbtestdb',
    DBInstanceIdentifier='newpoc1',
    AllocatedStorage=20,
    DBInstanceClass='db.t4g.micro',
    Engine='mysql',
    MasterUsername='admin',
    MasterUserPassword='Mypassword.1',
    PubliclyAccessible=True
)
