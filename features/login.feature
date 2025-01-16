Feature: Login funtionality

#  @login #@only #@pom1 #  @completed
#  Scenario: Login with valid credentials
#    Given I navigate to login page
##    When I enter valid email address and valid password into the fields
#    When I enter valid email address as "amotooriapril2023@gmail.com" and valid password as "12345" into the fields
#    And I click on login button
#    Then I should get logged in

    @login #@only #@pom1 #  @completed
  Scenario Outline: Login with valid credentials
    Given I navigate to login page
#    When I enter valid email address and valid password into the fields
#    When I enter valid email address as "amotooriapril2023@gmail.com" and valid password as "12345" into the fields
    When I enter valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on login button
    Then I should get logged in
    Examples:
      |email                          |password    |
      |amotoorisampleone@gmail.com    |secondone   |
      |amotoorisampletwo@gmail.com    |secondtwo   |
      |amotoorisamplethree@gmail.com  |secondthree |

#  @login #@pom2 #  @completed
#  Scenario: Login with invalid email and valid password
#    Given I navigate to login page
#    When I enter invalid email and valid password into the fields
#    And I click on login button
#    Then I should get a proper warning message

  @login #@pom2 #  @completed
  Scenario: Login with invalid email and valid password
    Given I navigate to login page
#    When I enter invalid email and valid password into the fields
    When I enter invalid email and valid password say "12345" into the fields
    And I click on login button
    Then I should get a proper warning message

#  @login #@pom3 #  @completed
#  Scenario: Login with valid email and invalid password
#    Given I navigate to login page
#    When I enter valid email and invalid password into the fields
#    And I click on login button
#    Then I should get a proper warning message

  @login #@pom3 #  @completed
  Scenario: Login with valid email and invalid password
    Given I navigate to login page
#    When I enter valid email and invalid password into the fields
    When I enter valid email say "amotooriapril2023@gmail.com" and invalid password say "1234567" into the fields
    And I click on login button
    Then I should get a proper warning message

#  @login #@pom4 #  @completed
#  Scenario: Login with invalid credentials
#    Given I navigate to login page
#    When I enter invalid email and invalid password into the fields
#    And I click on login button
#    Then I should get a proper warning message

  @login #@pom4 #  @completed
  Scenario: Login with invalid credentials
    Given I navigate to login page
    When I enter invalid email and invalid password say "1234567" into the fields
    And I click on login button
    Then I should get a proper warning message

  @login #  @completed
  Scenario: Login without entering any credentials
    Given I navigate to login page
    When I dont enter anything into email and password fields
    And I click on login button
    Then I should get a proper warning message