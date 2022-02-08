*** Settings ***
Documentation       A  resource file with reusable keywords and variables.
Library             SeleniumLibrary

*** Variables ***
${user_name}            jdsn
${valid_password}       pswd
${invalid_password}     111
${firstname}            janardan
${lastname}             nimbekar
${phonenumber}          0456455455
${Error_Message_Login}      xpath://header//h1
${valid_message}        xpath://td[@id='username']


*** Keywords ***
open the browser
    open browser   http://localhost:8080/    chrome
close the browser
    Close Browser