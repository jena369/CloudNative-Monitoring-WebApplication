import boto3
from botocore.exceptions import ClientError

# Create an ECR client
client = boto3.client('ecr', region_name='us-east-1')

# Repository name
repository_name = 'my-coud-native-repo'

def create_repository_if_not_exists(repository_name):
    try:
        # Try to create the repository
        response = client.create_repository(repositoryName=repository_name)
        print(f"Repository created successfully: {response['repository']['repositoryUri']}")
    except ClientError as e:
        if e.response['Error']['Code'] == 'RepositoryAlreadyExistsException':
            print(f"Repository '{repository_name}' already exists.")
        else:
            # Raise the error if it's not the 'RepositoryAlreadyExistsException'
            raise

def main():
    create_repository_if_not_exists(repository_name)

if __name__ == "__main__":
    main()