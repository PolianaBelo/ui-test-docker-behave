Feature: Authentication

Scenario: Failed authentication
    Given I am on login page
    When  I log in as "invalid-user-credentials"
    Then  I see an error message