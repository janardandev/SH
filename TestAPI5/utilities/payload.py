import json


def updateUserPayload():
    body = json.dumps({
        "firstname": "jd444",
        "lastname": "sn444",
        "phone": "44444"
    })
    return body


def createUserPayload():
    body = json.dumps({
        "username": "jdsn4",
        "password": "pswd4",
        "firstname": "jd4",
        "lastname": "sn4",
        "phone": "4444"
    })
    return body
