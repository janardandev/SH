# Get details of a particular user
import requests
import json
from TestAPI5.getToken import getToken
from utilities.resources import ApiResources
from TestAPI5.utilities.configurations import *

url = getConfig()['API']['endpoint']
se = requests.session()
se.headers.update({'Content-Type': 'application/json'})

headers = {"token": f'{getToken()}'}

response_singleUser = se.get(url + ApiResources.users + '/jdsn4', headers=headers)
assert response_singleUser.json()['message'] == "retrieval succesful"
print(response_singleUser.json()['payload'])
