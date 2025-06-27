import json


def hello(event, context):
    body = {
        "message": "Hello jiiii",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response