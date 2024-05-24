Feature: OrangeHRM login
    Scenario: login to OrangeHRM with valid parameters
        Given I launch browser
        When I open application
        And Enter a valid username and password
        And Click on login button
        Then User must successfully login to the dashboard_page

    Scenario: Search user
        Given I launch browser
        When I open application
        And Enter username and password
        And Click on login button
        When navigate to search_page
        Then search_page should display

    Scenario: Advanced search user
        Given I launch browser
        When I open application
        And Enter username and password
        And Click on login button
        When navigate to Advanced_search_page
        Then Advanced_search_page should display