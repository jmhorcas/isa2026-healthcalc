Feature: Ideal Body Weight (Lorentz)
  As a user
  I want to calculate my ideal weight
  So that I have a healthy reference for my height

  Scenario: Calculate IBW for a man
    Given a height of 180 cm and gender "male"
    When the IBW is calculated with Lorentz
    Then the ideal weight should be 72.5