Feature: Creating a new account

  Scenario:
    Given I am on the homepage
      And I am logged out
     When I click "Sign in"
     Then I see the "Authentication" page
     When I enter a random email address
      And I click "Create an account"
     Then I see the "Create an account" page
     When I Select the "Mr" radio button
      And I enter "Paul" into the first name field
      And I enter "Collingwood" into the last name field
      And I enter "40598dfc45" into the password field
      And I set the dropdown "day" to "10"
      And I set the dropdown "month" to "March"
      And I set the dropdown "year" to "2018"
      And I enter the company "Microsoft" for the company field
      And I enter "10 Example street" for the first address field
      And I enter "FirstThings" for the second address field
      And I enter the city "Londinium" for the city field
      And I select "Alabama" for the state field
      And I enter "90201" for the Zip code field
      And I enter "444-555-4444" for the mobile phone number
      And I enter "X1234-Alias" for the alias field
     When I click the Register button
     Then I see the My Account page





