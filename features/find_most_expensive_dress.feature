Feature: Adding the most expensive dress and checking it persists in the cart

  Scenario Add the dress and log out and in again:
    Given I am logged in as "Peter Pan"
     When I visit the dresses page
      And I add the most expensive dress to the cart
      And I log out
      And I log in again as "Peter Pan"
     Then I can see the most expensive dress is still in the cart
