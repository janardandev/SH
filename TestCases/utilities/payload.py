import json


def updateUserPayload():
    body = json.dumps({
        "firstname": "jd5",
        "lastname": "sn5",
        "phone": "5"
    })
    return body


def createUserPayload():
    body = json.dumps({
        "username": "jdsn6",
        "password": "pswd6",
        "firstname": "jd6",
        "lastname": "sn6",
        "phone": "6666"
    })
    return body

def createUserPayload2():
    body = json.dumps({
        "username": "jdsn6",
        "password": "pswd6",
        "firstname": "jd6",
        "lastname": "sn7",
        "phone": "7777"
    })
    return body
