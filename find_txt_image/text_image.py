import boto3
import json

file = open('', 'rb').read()

rekognition_client = boto3.client('rekognition')
# rekognition_client = boto3.client('rekognition', aws_session_token="",
#                                aws_access_key_id = "", aws_secret_access_key = "", region_name = 'us-east-1')


response = rekognition_client.detect_text(
    Image={
        'Bytes': file
    }
)
print(json.dumps(response, indent=4, sort_keys=True))
