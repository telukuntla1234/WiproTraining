*** Settings ***
Library     SeleniumLibrary
Library     ../Libraries/ProductPage.py

Resource    ../Resources/login_page.resource

Suite Setup     Open Browser To Login Page
Suite Teardown  Close Browser

*** Test Cases ***
Verify Product Price Total
    Login To Application    standard_user    secret_sauce

    ${driver}=    Get Webdriver Instance

    ${price1}=    Get Product Price By Name
    ...    ${driver}
    ...    Sauce Labs Backpack

    ${price2}=    Get Product Price By Name
    ...    ${driver}
    ...    Sauce Labs Bike Light

    ${total}=     Evaluate    ${price1}+${price2}

    Should Be Equal As Numbers    ${total}    39.98