*** Settings ***
Documentation   Registration Form to fill the login details
Library     SeleniumLibrary
Test Setup   open the browser
Test Teardown   close the browser
Resource        resource.robot

*** Variables ***

*** Test Cases ***
Validate Registration Details

    Fill the login Form


*** Keywords ***

Fill the login Form
    click element       xpath://a[contains(text(),'Register')]
    Input Text          id:username      ${user_name}
    Input Password      id:password      ${valid_password}
    Input Text          id:firstname     ${firstname}
    Input Text          id:lastname      ${lastname}
    Input Text          id:phone         ${phonenumber}
    Click Button        xpath://input[@value='Register']


