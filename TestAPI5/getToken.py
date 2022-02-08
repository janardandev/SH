# Get token of registered user
import requests
import json
from TestAPI5.utilities.configurations import getConfig, getPassword
from TestAPI5.utilities.resources import ApiResources

url = getConfig()['API']['endpoint']
se = requests.session()
se.headers.update({'Content-Type': 'application/json'})


def getToken():
    response_token = se.get(url + ApiResources.tokenPath, auth=('jdsn', getPassword()))
    response_token.json()['token'] == 'SUCCESS'
    return (response_token.json())['token']


getToken()
