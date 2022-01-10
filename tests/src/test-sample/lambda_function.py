import json
import traceback

def lambda_handler(event, context):
    import_status = True

    try:
        import boto3
        import requests
        import redis
    except Exception as e:
        print("Something went wrong while importing :")
        traceback.print_exc()
        print(str(e))
        import_status = False
    
    if import_status:
        body = { "code" : 200, "message" : "All okay."}
    else:
        body = {"code" : 500, "message": "Something went wrong here.."}

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

