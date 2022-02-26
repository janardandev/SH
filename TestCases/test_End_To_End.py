import pytest
import requests
from utilities.configurations import getConfig, getPassword
from utilities.resources import ApiResources
from utilities.payload import createUserPayload, updateUserPayload

url = getConfig()['API']['endpoint']
se = requests.session()
se.headers.update({'Content-Type': 'application/json'})


@pytest.fixture
def get_token():
    response_token = se.get(url + ApiResources.tokenPath, auth=('jdsn', getPassword()))
    return (response_token.json()['token']) == 'token'
    assert response_token.json()['token'] == 'SUCCESS'
    assert response_token == 200


    # Get token of registered user


def test_get_token(get_token):
    pass

    # Get All users Name who are registered


def test_all_user_name(get_token):
    response_allUserName = se.get(url + ApiResources.users, headers={"token": f'{"token"}'})
    assert response_allUserName.status_code == 200

    # Add new users


def test_adduser():
    response_addUser = se.post(url + ApiResources.users, data=createUserPayload())
    assert response_addUser.status_code == 200 or 400


    # Get details of a particular user


def test_get_particular_user(get_token):
    response_singleUser = se.get(url + ApiResources.users + '/jdsn5', headers={"token": f'{"token"}'})
    assert response_singleUser.status_code == 200 or 401

    # Update details of a particular user


def test_update_user(get_token):
    response_updated = se.put(url + ApiResources.users + '/jdsn5', headers={"token": f'{"token"}'}, data=updateUserPayload())
    assert response_updated.status_code == 200 or 401

