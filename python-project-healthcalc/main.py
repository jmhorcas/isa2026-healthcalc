from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException
from healthcalc.health_stats_proxy import HealthHospitalProxy
from healthcalc.StrategyAndFactory import CalculadoraEuropea, CalculadoraAmericana, IdiomaEspanol, IdiomaIngles

def main():

    # 1. Comprobación del Singleton
    print("\n[1] Probando Singleton:")
    calc1 = HealthCalcImpl()
    calc2 = HealthCalcImpl()
    print("Dirección de memoria 1:", id(calc1))
    print("Dirección de memoria 2:", id(calc2))
    print("¿Son el mismo objeto?:", calc1 is calc2)

    # 2. Comprobación del Proxy y Adaptador del Hospital
    print("\n[2] Probando Proxy y Adaptador:")
    hospital = HealthHospitalProxy()
    
    # Metemos datos en las unidades del hospital (metros y gramos)
    hospital.indiceMasaCorporal(1.85, 90000)  # Paciente 1 (1.85m, 90kg)
    hospital.pesoCorporalIdeal('m', 1.85)
    
    hospital.indiceMasaCorporal(1.60, 52000)  # Paciente 2 (1.60m, 52kg)
    hospital.pesoCorporalIdeal('f', 1.60)

    # Pedimos las estadísticas que el proxy ha ido guardando
    print("Estadísticas del Proxy:")
    print("Total pacientes:", hospital.numTotalPacientes())
    print("Altura media:", round(hospital.alturaMedia(), 2), "m")
    print("IMC medio:", round(hospital.imcMedio(), 2))
    print(f"Hombres: {hospital.numSexoH()} | Mujeres: {hospital.numSexoM()}")

    # 3. Comprobación de las fábricas de idiomas y regiones
    print("\n[3] Probando Calculadoras Regionales e Idiomas:")
    calc_eu_es = CalculadoraEuropea(IdiomaEspanol())
    calc_usa_en = CalculadoraAmericana(IdiomaIngles())
    
    print("Europa + ES:", calc_eu_es.calcular_imc_con_mensaje(1.78, 75000))
    print("USA + EN:   ", calc_usa_en.calcular_imc_con_mensaje(6.0, 160))
    
    # 4. Código original de la P1 para introducir datos a mano
    print("--- ENTRADA MANUAL DE DATOS (PRÁCTICA 1) ---")

    calc = HealthCalcImpl() # Usa el Singleton automáticamente
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