

Feature: Orange HRM Logo

    Scenario: logo presence on OrangeHRM home_page
        Given launch chrom_browser
        When open OrangeHRM home_page
        Then verify that the Logo presence on home_page
        And close chrom_browser

