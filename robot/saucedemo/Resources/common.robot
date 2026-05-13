*** Settings ***
Library    SeleniumLibrary
Library    DateTime

*** Keywords ***
Start Browser
    Open Browser    https://www.saucedemo.com    chrome
    Maximize Browser Window

Close Browser Session
    Run Keyword If Test Failed    Capture Failure Screenshot
    Close Browser

Capture Failure Screenshot
    ${timestamp}=    Get Current Date    result_format=%Y%m%d_%H%M%S

    Capture Page Screenshot
    ...    failure_${TEST_NAME}_${timestamp}.png