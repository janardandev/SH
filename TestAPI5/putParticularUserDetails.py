# Update details of a particular user
import requests
import json
from TestAPI5.getToken import getToken
from TestAPI5.utilities.resources import ApiResources
from TestAPI5.utilities.configurations import *
from TestAPI5.utilities.payload import updateUserPayload

url = getConfig()['API']['endpoint']
se = requests.session()
se.headers.update({'Content-Type': 'application/json'})
headers = {"token": f'{getToken()}'}

response_updated = se.put(url + ApiResources.users + '/jdsn4', headers=headers, data=updateUserPayload())
response_updated.status_code == 200
assert response_updated.json()['message'] == 'Updated'
print(response_updated.text)
