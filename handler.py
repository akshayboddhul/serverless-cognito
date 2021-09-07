import json


def hello(event, context):
    body = {
        "message": "Go Serverless v2.0! You're registered user!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Access-Control-Allow-Origin": "https://example.com",
            "Access-Control-Allow-Credentials": True
        }
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


def guest(event, context):
    body = {
        "message": "You're guest user!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
