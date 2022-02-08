import json
import requests
from TestAPI5.utilities.configurations import getConfig, getPassword
from TestAPI5.utilities.resources import ApiResources

from TestAPI5.utilities.payload import createUserPayload, updateUserPayload

url = getConfig()['API']['endpoint']
se = requests.session()
se.headers.update({'Content-Type': 'application/json'})


# Get token of registered user
def get_token():
    response_token = se.get(url + ApiResources.tokenPath, auth=('jdsn', getPassword()))
    response_token.json()['token'] == 'SUCCESS'
    return (response_token.json())['token']


get_token()

headers = {"token": f'{get_token()}'}

# Get All users Name who are registered

response_allUserName = se.get(url + ApiResources.users, headers=headers)
print(response_allUserName.json()['payload'])

# Add new users

response_addUser = se.post(url + ApiResources.users, data=createUserPayload())
print(response_addUser.json())

# Get details of a particular user

response_singleUser = se.get(url + ApiResources.users + "/jdsn4", headers=headers)
assert response_singleUser.json()['message'] == "retrieval succesful"
print(response_singleUser.json()['payload'])

# Update details of a particular user

response_updated = se.put(url + ApiResources.users + '/jdsn4', headers=headers, data=updateUserPayload())
response_updated.status_code == 200
assert response_updated.json()['message'] == 'Updated'
print(response_updated.json())
