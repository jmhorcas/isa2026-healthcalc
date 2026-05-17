Feature: Basal Metabolic Rate (WHO)
  As a fitness enthusiast
  I want to calculate my BMR
  So that I know my daily calorie needs at rest

  Scenario: Calculate standard BMR
    Given a person with 70.0 kg, 25.0 years old and gender "male"
    When the BMR is calculated using the WHO formula
    Then the BMR result should be 1724.0