Feature: Signing in as an existing user

  Scenario: Log in
    Given I am on the homepage
      And I am logged out
     When I click "Sign in"
     Then I see the "Authentication" page
     When I enter "existing@example.com" into the signup email field
      And I enter "40958730497856" into the signup password field
      And I click the "Sign in" button
     Then I see I am logged in as "Peter Pan"





