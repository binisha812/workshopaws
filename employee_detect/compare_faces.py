import boto3
import json
rekognition_client = boto3.client('rekognition')
file = open('', 'rb').read()
CollectionId = ""

response = rekognition_client.detect_faces(
    Image={
        'Bytes': file
    },

)
print(json.dumps(response, indent=4, sort_keys=True))
