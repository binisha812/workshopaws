import boto3

rekognition_client = boto3.client('rekognition')
# rekognition_client = boto3.client('rekognition', aws_session_token="",
#                                aws_access_key_id = "", aws_secret_access_key = "", region_name = 'us-east-1')

file = open('', 'rb').read()
CollectionId = ""

response = rekognition_client.index_faces(
    CollectionId=CollectionId,
    Image={
        'Bytes': file
    },
    ExternalImageId=""
)
print(response)
