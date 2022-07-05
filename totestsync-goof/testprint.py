import boto3
import os

if __name__ == "__main__":
    myrole = os.getenv('AWS_CONTAINER_CREDENTIALS_RELATIVE_URI', "")
    print("myrole:" + myrole)
    client = boto3.client('ecs')
    print("Test print")
