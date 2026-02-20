import pytest
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException


class TestBMI:

    @pytest.fixture(autouse=True)  # Equivalente a @BeforeEach en JUnit
    def set_up(self):
        """Se ejecuta antes de cada test."""
        self.health_calc = HealthCalcImpl()

    # --- Tests de Cálculo de la métrica BMI ---
    def test_body_mass_index_valido(self):
        """Cálculo de BMI con valores estándar válidos"""
        weight = 70.0
        height = 1.75
        expected_bmi = 70.0 / (1.75 ** 2)

        result = self.health_calc.body_mass_index(weight, height)

        # pytest.approx es el equivalente a assertEquals con delta (0.01) en JUnit
        assert result == pytest.approx(expected_bmi, abs=0.01)

    def test_body_mass_index_peso_cero(self):
        """Lanzar excepción cuando el peso es cero"""
        weight = 0
        height = 1.70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.body_mass_index(weight, height)

    def test_body_mass_index_altura_cero(self):
        """Lanzar excepción cuando la altura es cero"""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.body_mass_index(70, 0)

    def test_body_mass_index_negativos(self):
        """Lanzar excepción cuando los valores son negativos (Equivalente a assertAll)"""
        weight = -70
        height = 1.70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.body_mass_index(weight, height)

        weight = -70
        height = 1.70
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.body_mass_index(weight, height)

        weight = 70
        height = -1.70
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.body_mass_index(weight, height)

    # --- Tests de Límites e Invalidación para el BMI ---

    @pytest.mark.parametrize("weight", [-10.0, 0.0, 0.99], ids=lambda x: f"Peso mínimo inválido: {x}kg")
    def test_peso_minimo_imposible(self, weight: float):
        """Lanzar excepción cuando el peso es negativo o menor que 1kg."""
        height = 1.70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.body_mass_index(weight, height)

    @pytest.mark.parametrize("weight", [700.1, 1000.0, 5000.0], ids=lambda x: f"Peso máximo inválido: {x}kg")
    def test_peso_maximo_imposible(self, weight: float):
        """Lanzar excepción cuando el peso es extremadamente alto."""
        height = 1.70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.body_mass_index(weight, height)

    @pytest.mark.parametrize("height", [-0.50, 0.0, 0.29], ids=lambda x: f"Altura mínima inválida: {x}m")
    def test_altura_minima_imposible(self, height: float):
        """Lanzar excepción cuando la altura es negativa o menor que 30cm."""
        weight = 70

        with pytest.raises(InvalidHealthDataException):
            self.health_calc.body_mass_index(weight, height)

    @pytest.mark.parametrize("height", [3.01, 3.50, 5.00], ids=lambda x: f"Altura máxima inválida: {x}m")
    def test_altura_maximo_imposible(self, height: float):
        """Lanzar excepción cuando la altura es extremadamente alta."""
        weight = 70
        
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.body_mass_index(weight, height)


    # --- Tests de Clasificación básica a partir del BMI ---
    
    @pytest.mark.parametrize("bmi", [10.0, 18.4, 18.49], ids=lambda x: f"BMI {x} -> Underweight")
    def test_bmi_underweight(self, bmi: float):
        """Cálculo de clasificación BMI para Underweight."""
        assert self.health_calc.bmi_classification(bmi) == "Underweight"

    @pytest.mark.parametrize("bmi", [18.5, 22.0, 24.9, 24.99], ids=lambda x: f"BMI {x} -> Normal weight")
    def test_bmi_normal_weight(self, bmi: float):
        """Cálculo de clasificación BMI para Normal weight."""
        assert self.health_calc.bmi_classification(bmi) == "Normal weight"

    @pytest.mark.parametrize("bmi", [25.0, 27.5, 29.9, 29.99], ids=lambda x: f"BMI {x} -> Overweight")
    def test_bmi_overweight(self, bmi: float):
        """Cálculo de clasificación BMI para Overweight."""
        assert self.health_calc.bmi_classification(bmi) == "Overweight"

    @pytest.mark.parametrize("bmi", [30.0, 35.0, 50.0], ids=lambda x: f"BMI {x} -> Obesity")
    def test_bmi_obesity(self, bmi: float):
        """Cálculo de clasificación BMI para Obesity."""
        assert self.health_calc.bmi_classification(bmi) == "Obesity"

    # --- Tests de Límites e Invalidación para la clasificación BMI ---

    @pytest.mark.parametrize("bmi", [-50.0, -1.0, -0.01], ids=lambda x: f"BMI negativo: {x}")
    def test_bmi_classification_minimo_imposible(self, bmi: float):
        """Lanzar excepción cuando el BMI es negativo."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi_classification(bmi)

    @pytest.mark.parametrize("bmi", [150.1, 200.0, 500.0], ids=lambda x: f"BMI máximo extremo: {x}")
    def test_bmi_classification_maximo_imposible(self, bmi: float):
        """Lanzar excepción cuando el BMI es extremadamente alto."""
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmi_classification(bmi)