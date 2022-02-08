# Add new users
import requests
import json
from TestAPI5.utilities.configurations import getConfig
from TestAPI5.utilities.resources import ApiResources
from TestAPI5.utilities.payload import createUserPayload

url = getConfig()['API']['endpoint']
se = requests.session()
se.headers.update({'Content-Type': 'application/json'})

response_addUser = se.post(url + ApiResources.users, data=createUserPayload())

print(response_addUser.json())
