import boto3

rekognition_client = boto3.client('rekognition')
# rekognition_client = boto3.client('rekognition', aws_session_token="",
#                                aws_access_key_id = "", aws_secret_access_key = "", region_name = 'us-east-1')


response = rekognition_client.create_collection(
    CollectionId=''
)

print(response)
