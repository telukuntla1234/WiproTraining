*** Settings ***
Resource    ../Resources/login_page.resource

Suite Setup     Open Browser To Login Page
Suite Teardown  Close Browser

*** Test Cases ***
Valid Login Test
    Login To Application    standard_user    secret_sauce
    Verify Successful Login