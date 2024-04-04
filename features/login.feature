Feature: Login funtionality

  @login #@pom1 #  @completed
  Scenario: Login with valid credentials
    Given I navigate to login page
    When I enter valid email address and valid password into the fields
    And I click on login button
    Then I should get logged in

  @login #@pom2 #  @completed
  Scenario: Login with invalid email and valid password
    Given I navigate to login page
    When I enter invalid email and valid password into the fields
    And I click on login button
    Then I should get a proper warning message

  @login #@pom3 #  @completed
  Scenario: Login with valid email and invalid password
    Given I navigate to login page
    When I enter valid email and invalid password into the fields
    And I click on login button
    Then I should get a proper warning message

  @login #@pom4 #  @completed
  Scenario: Login with invalid credentials
    Given I navigate to login page
    When I enter invalid email and invalid password into the fields
    And I click on login button
    Then I should get a proper warning message

  @login #  @completed
  Scenario: Login without entering any credentials
    Given I navigate to login page
    When I dont enter anything into email and password fields
    And I click on login button
    Then I should get a proper warning message