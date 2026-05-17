Feature: Cálculo del BMI
  As a user I want to calculate my BMI...

  Scenario: Cálculo exitoso
    Given a weight of 75 and height of 1.80...
    When the BMI is calculated
    Then the result should be 23.15