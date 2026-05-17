from .health_calc_impl import HealthCalcImpl

# Strategy Methods

class IdiomaStrategy:
    """Interfaz estratégica para todos los idiomas, definde método de construcción del mensaje final"""
    def construir_mensaje(self, altura: float, peso: float, imc: float, u_alt: str, u_pes: str) -> str:
        raise NotImplementedError("Debe implementar el método construir_mensaje")


class IdiomaEspanol(IdiomaStrategy):
    """Traducción a español"""
    def construir_mensaje(self, altura: float, peso: float, imc: float, u_alt: str, u_pes: str) -> str:
        return f"La persona con altura {altura} {u_alt} y peso {peso} {u_pes} tiene un IMC de {imc:.2f}."


class IdiomaIngles(IdiomaStrategy):
    """Traducción al inglés"""
    def construir_mensaje(self, altura: float, peso: float, imc: float, u_alt: str, u_pes: str) -> str:
        return f"The person with height {altura} {u_alt} and weight {peso} {u_pes} has a BMI of {imc:.2f}."
    
# FACTORY METHODS:
class CalculadoraRegional:
    """Clase base para las calculadoras del mundo"""
    def __init__(self, idioma: IdiomaStrategy):
        self.idioma = idioma  # Guardamos el idioma introducido por el usuario
        self._calculadora = HealthCalcImpl()  # singleton de la calculadora original, que se encargará de los cálculos reales

    def calcular_imc_con_mensaje(self, altura: float, peso: float) -> str:
        raise NotImplementedError("Obligatorio programarlo en la europea/americana")


class CalculadoraEuropea(CalculadoraRegional):
    """Configuración para Europa (espera unidades en metros y gramos)"""
    def calcular_imc_con_mensaje(self, altura: float, peso: float) -> str:
        # El enunciado dice que viene en gramos, así que pasamos a kilos para nuestra calculadora
        peso_kg = peso / 1000.0
        
        # Llamamos a nuestro bmi normal (que ya recibe kg y metros):
        imc = self._calculadora.bmi(peso_kg, altura, weight_unit="kg", height_unit="m")
        
        # Le pasamos el mensaje al idioma para que lo construya con las unidades correctas:
        return self.idioma.construir_mensaje(altura, peso, imc, "metros", "gramos")


class CalculadoraAmericana(CalculadoraRegional):
    """Configuración para USA (espera unidades enpies y libras)"""
    def calcular_imc_con_mensaje(self, altura: float, peso: float) -> str:
        # La altura viene dada en pies (ft). Nuestra calculadora trabaja en modo imperial 
        # Espera pulgadas (in). Multiplicamos por 12 porque 1 pie son 12 pulgadas.
        pulgadas = altura * 12.0
        
        # Tiramos de la calculadora original pasándole lb e in
        imc = self._calculadora.bmi(peso, pulgadas, weight_unit="lb", height_unit="in")
        
        return self.idioma.construir_mensaje(altura, peso, imc, "pies", "libras")
