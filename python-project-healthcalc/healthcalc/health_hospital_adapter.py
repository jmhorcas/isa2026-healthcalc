

from .health_calc_impl import HealthCalcImpl

# target:
class HealthHospital:

    def indiceMasaCorporal(self, altura: float, peso: int) -> tuple:
        pass

    def pesoCorporalIdeal(self, genero: str, altura: float) -> int:
        pass

# Adapter:
# Los datos que nos proporciona el hospital son convertidos para que nuestra calculadora trabaje con ellos:

class HealthHospitalAdapter(HealthHospital):
    def __init__(self):
        self._adaptee = HealthCalcImpl()

    def indiceMasaCorporal(self, altura: float, peso: int) -> tuple:
        peso_kg = peso / 1000.0
        imc_value = self._adaptee.bmi(peso_kg, altura, weight_unit = "kg", height_unit = "m")
        imc_class = self._adaptee.bmi_classification(imc_value)
        return (imc_value, imc_class) # Devolvemos el valor del IMC y su clasificación en tupla.
    


    def pesoCorporalIdeal(self, genero: str, altura: float) -> int:
        altura_cm = altura * 100.0 # Nuestro método ibw recibe la altura en cm
        genero_map = "male" if genero.lower() in ['m', 'male', 'h'] else "female"

        ibw_value = self._adaptee.ibw_lorentz_metric(altura_cm, genero_map, height_unit = "cm")
        return int(round(ibw_value)) # Devolvemos el peso corporal ideal redondeado a entero.
