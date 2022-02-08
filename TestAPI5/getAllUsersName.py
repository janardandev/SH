# Get All users Name who are registered
import requests
import json
from TestAPI5.utilities.configurations import getConfig
from TestAPI5.utilities.resources import ApiResources
from TestAPI5.getToken import getToken

url = getConfig()['API']['endpoint']
se = requests.session()
se.headers.update({'Content-Type': 'application/json'})
headers = {"token": f'{getToken()}'}

response_allUserName = se.get(url + ApiResources.users, headers=headers)

print(response_allUserName.json()['payload'])

