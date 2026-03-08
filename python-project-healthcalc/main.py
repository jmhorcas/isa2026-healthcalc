from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException

def main():
    calc = HealthCalcImpl()
    print("Advanced Health Calculator (HealthCalc)")
    
    try:
        weight = float(input("Enter your weight (kg): "))
        height_m = float(input("Enter your height (m): "))
        height_cm = height_m * 100  # Convert to cm for the other metrics
        age = int(input("Enter your age: "))
        
        # The implementation expects exactly "male" or "female"
        gender_input = input("Enter your gender ('m' for male, 'f' for female): ").lower()
        if gender_input in ['m', 'male']:
            gender = "male"
        elif gender_input in ['f', 'female']:
            gender = "female"
        else:
            gender = "unknown"

        print("\nResults")
        
        # 1. BMI Calculation and Classification
        bmi_val = calc.bmi(weight, height_m, weight_unit="kg", height_unit="m")
        bmi_class = calc.bmi_classification(bmi_val)
        print(f"BMI: {bmi_val:.2f} ({bmi_class})")

        # 2. Ideal Body Weight (IBW) - Lorentz Formula
        ibw_val = calc.ibw_lorentz_metric(height_cm, gender, height_unit="cm")
        print(f"Ideal Body Weight (Lorentz): {ibw_val:.2f} kg")

        # 3. Basal Metabolic Rate (BMR) - WHO Equations
        bmr_val = calc.bmr_metric(weight, age, gender, weight_unit="kg")
        print(f"Basal Metabolic Rate (WHO): {bmr_val:.2f} kcal/day")

    except ValueError:
        print("\nError: Please enter valid numeric values.")
    except InvalidHealthDataException as e:
        print(f"\nHealth validation error: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()