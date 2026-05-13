*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}                 https://www.saucedemo.com
${BROWSER}             chrome

${USERNAME_FIELD}      id:user-name
${PASSWORD_FIELD}      id:password
${LOGIN_BUTTON}        id:login-button

${PRODUCT_TITLE}       xpath://span[text()='Products']

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Login To Application
    [Arguments]    ${username}    ${password}

    Input Text    ${USERNAME_FIELD}    ${username}
    Input Password    ${PASSWORD_FIELD}    ${password}
    Click Button    ${LOGIN_BUTTON}

Verify Successful Login
    Wait Until Element Is Visible    ${PRODUCT_TITLE}    10s