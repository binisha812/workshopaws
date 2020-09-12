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

if len(response["FaceDetails"]) > 0:
    res = rekognition_client.search_faces_by_image(
        CollectionId=CollectionId,
        Image={
            'Bytes': file
        },


    )
    if len(res["FaceMatches"]) > 0:
        print(res["FaceMatches"][0]["Face"]["ExternalImageId"])
    else:
        print("Doesnt exist")


else:
    print("No face detected")
