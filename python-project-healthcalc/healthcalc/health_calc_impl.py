from healthcalc import HealthCalc, InvalidHealthDataException


class HealthCalcImpl(HealthCalc):

    def bmi_classification(self, bmi: float) -> str:
        if bmi < 0:
            raise InvalidHealthDataException("BMI cannot be negative.")
        if bmi > 150:
            raise InvalidHealthDataException("BMI must be within a possible biological range [0-150].")
        
        result = "Obesity"
        if bmi < 18.5:
            result = "Underweight"
        elif bmi < 25:
            result = "Normal weight"
        elif bmi < 30:
            result = "Overweight"
        return result

    def bmi(self, weight: float, height: float) -> float:
        if weight <= 0:
            raise InvalidHealthDataException("Weight must be positive.")
        if height <= 0:
            raise InvalidHealthDataException("Height must be positive.")
        if weight < 1 or weight > 700:
            raise InvalidHealthDataException("Weight must be within a possible biological range [1-700] kg.")
        if height < 0.30 or height > 3.00:
            raise InvalidHealthDataException("Height must be within a possible biological range [0.30-3.00] m.")
            
        return weight / (height ** 2)
    
    def ibw(self, height_cm: float, gender: str) -> float:
        if height_cm <= 0:
            raise InvalidHealthDataException("Height must be positive.")
        if height_cm < 30 or height_cm > 300:
            raise InvalidHealthDataException("Height must be within a possible biological range [30-300] cm.")

        gender_lower = gender.lower().strip()
        if gender_lower in ["man", "hombre", "m"]:
            result = (height_cm - 100) - ((height_cm - 150) / 4.0)
        elif gender_lower in ["woman", "mujer", "f", "w"]:
            result = (height_cm - 100) - ((height_cm - 150) / 2.0)
        else:
            raise InvalidHealthDataException("Gender must be 'man' or 'woman'.")
        return result
    
    def news2(self, frecResp: float, oxSat: float, oxSup: bool, preArtSis: float, frecCard: float, consciente: str, temp: float):
        news2 = 0
        
        # Frecuencia respiratoria
        if (frecResp >= 25 or frecResp <= 8):
            news2 = news2 + 3
        elif (frecResp >= 21 or frecResp <= 24):
            news2 = news2 + 2
        elif (frecResp >= 9 or frecResp <= 11):
            news2 = news2 + 1

        # Saturacion de oxigeno
        if (oxSat <= 91):
            news2 = news2 + 3
        elif (oxSat <= 93):
            news2 = news2 + 2
        elif (oxSat <= 95):
            news2 = news2 + 1

        # Oxigeno suplementario
        if (oxSup == True):
            news2 = news2 + 2

        # Presion arterial sistolica
        if (preArtSis <= 90 or preArtSis >= 220):
            news2 = news2 + 3
        elif (preArtSis <= 100):
            news2 = news2 + 2
        elif (preArtSis <= 110):
            news2 = news2 + 1

        # Frecuencia cardiaca
        if (frecCard <= 40 or frecCard >= 131):
            news2 = news2 + 3
        elif (frecCard >= 111):
            news2 = news2 + 2
        elif (frecCard <= 50 or frecCard >= 91):
            news2 = news2 + 1

        # Nivel de consciencia
        if (consciente == "cvpu"):
            news2 = news2 + 3

        # Temperatura
        if (temp <= 35):
            news2 = news2 + 3
        elif (frecCard > 39):
            news2 = news2 + 2
        elif (frecCard <= 36 or frecCard > 38):
            news2 = news2 + 1

        if frecResp <= 0 or frecResp >= 100:
            raise InvalidHealthDataException("Respiratory rate must be between 0 - 100.")
        if oxSat <= 0 or oxSat >= 100:
            raise InvalidHealthDataException("Oxigen saturation rate must be between 0 - 100 bpm.")
        if preArtSis <= 0 or preArtSis >= 100:
            raise InvalidHealthDataException("Systolic blood pressure must be between 0 -100 mmHg.")
        if frecCard <= 0 or frecCard >= 300:
            raise InvalidHealthDataException("Heart rate rate must be between 0 - 300 bpm.") 
        if temp <= 20 or temp >= 50:
            raise InvalidHealthDataException("Oxigen saturation rate must be between 20 - 50 ºC.")
        
        if news2 >= 5:
            #result = "Red alert: score of " + str(news2)
            result = news2
        else:
            result = news2
        
        return result