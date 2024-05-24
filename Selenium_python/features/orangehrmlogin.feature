Feature: OrangeHRM login

    Scenario: login to OrangeHRM with valid parameters
        Given I launch chrom_browser
        When I open OrangeHRM home_page
        And Enter username "Admin" and password "admin123"
        And Click on login button
        Then User must successfully login to the dashboard_page
        
    Scenario Outline: login to OrangeHRM with multiple parameters
        Given I launch chrom_browser
        When I open OrangeHRM home_page
        And Enter username "<username>" and password "<password>"
        And Click on login button
        Then User must successfully login to the dashboard_page

        Examples:
        |username|password|
        |Admin|admin123|
        |admin123|admin|
        |adminxyz|admin123|
        |admin|adminxyz|
        