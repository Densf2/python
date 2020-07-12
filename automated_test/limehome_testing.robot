*** Settings ***
Documentation    Tests to verification filling last name on the main page
...              filling the all fields, choosing the date, change the nationality to Denmark on booking details page
...              and redirect to the confirmation page

Library     SeleniumLibrary
Test Teardown  Close Browser

*** Test Cases ***
Change The Birthdate, Natinoality On Booking Details Page
    [Tags]    DEBUG
    Open The Main Page
    Fill The Last Name, Booking Reference, Click Submit
    Redirect To Booking Details Page Success
    Open Calemdar
    Sleep  1s
    Choose Birthdate As Adult User
    Choose Nationality Denmark
    Date Selected Successfully
    Nationality Denmark Selected Successfully

*** Variables ***
${MAIN_URL}      https://limehome-qa-task.herokuapp.com
${BROWSER}        Chrome
${LAST_NAME_TEXT}      Test Last Name
${LAST_NAME_INPUT_FIELD}    css=input[formcontrolname="lastName"]
${BOOKING_REFERENCE_INPUT_FIELD}    css=input[formcontrolname="bookingReference"]
${BOOKING_REFERENCE_NUMBER}         347840
${SUBMIT_BUTTON_ON_MAIN_PAGE}       css=span.mat-button-wrapper

*** Keywords ***
Open The Main Page
    Open Browser        ${MAIN_URL}      ${BROWSER}

Fill The Input
    [Arguments]     ${LOCATOR}      ${TEXT}
    Input Text      ${LOCATOR}    ${TEXT}

Fill The Last Name, Booking Reference, Click Submit
    Fill The Input   ${LAST_NAME_INPUT_FIELD}    ${LAST_NAME_TEXT}
    Fill The Input   ${BOOKING_REFERENCE_INPUT_FIELD}   ${BOOKING_REFERENCE_NUMBER}
    Sleep       1s
    Click Element     ${SUBMIT_BUTTON_ON_MAIN_PAGE}

Redirect To Booking Details Page Success
    Wait Until Element Is Visible   xpath=//span[text()='Your booking details.']

Open Calemdar
    Click Element   css=svg.mat-datepicker-toggle-default-icon

Choose Birthdate As Adult User
    Click Element   css=button.mat-calendar-period-button
    Click ELement   css=div.mat-calendar-arrow
    Click Element   css=button.mat-calendar-previous-button
    Click ELement   css=td[aria-label="2000"]
    Click ELement   css=td[aria-label="May 2000"]
    Click Element   css=td[aria-label="May 10, 2000"]

Choose Nationality Denmark
    Click Element   xpath=//span[text()='German (DE)']
    Click Element   xpath=//span[text()=' Danish (DK) ']

Date Selected Successfully
    Page Should Contain Element     css=input[ng-reflect-model="Wed May 10 2000 00:00:00 GMT+0"]

Nationality Denmark Selected Successfully
    Page Should Contain Element    xpath=//span[text()='Danish (DK)']

