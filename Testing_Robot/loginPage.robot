*** Settings ***
Documentation   To Validate the Login form
Library     SeleniumLibrary
Test Setup   open the browser
Test Teardown   close the browser
Resource        resource.robot

*** Variables ***
${result}

*** Test Cases ***
Validate Succesful Login
    Fill the form       ${user_name}      ${valid_password}
    wait until it checks and display message    ${valid_message}
    verify message is correct

Validate Unsuccesful Login
    Fill the form       ${user_name}      ${invalid_password}
    wait until it checks and display message    ${Error_Message_Login}

*** Keywords ***
Fill the form
    [arguments]     ${username}     ${password}
    click element       xpath://a[contains(text(),'Log In')]
    Input Text          id:username     ${username}
    Input Password      id:password     ${password}
    Click Button        xpath://input[@value='Log In']

wait until it checks and display message
    [arguments]     ${message}
   Wait Until Element Is Visible       ${message}

verify message is correct
   ${result}=   Get Text    ${valid_message}
    log  ${result}