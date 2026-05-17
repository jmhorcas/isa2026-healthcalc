from .health_hospital_adapter import HealthHospital, HealthHospitalAdapter

# Interfaz HealthStats para exponer las métricas requeridas por el hospital.
class HealthStats:
    def alturaMedia(self) -> float: pass
    def pesoMedio(self) -> float: pass
    def imcMedio(self) -> float: pass
    def numSexoH(self) -> int: pass
    def numSexoM(self) -> int: pass
    def numTotalPacientes(self) -> int: pass

# Utilizamos el patrón Proxy para capturar todas las estadísticcas de forma transparente al cliente, sin modificar la lógica del hospital:
class HealthHospitalProxy(HealthHospital, HealthStats):
    def __init__(self):
        self._real_service = HealthHospitalAdapter()
        
        # Inicializamos variables para acumular datos de pacientes
        self._total_altura = 0.0
        self._total_peso = 0.0
        self._total_imc = 0.0
        self._conteo_hombres = 0
        self._conteo_mujeres = 0
        self._total_pacientes = 0

    def _interceptar_y_registrar(self, altura: float, peso_gramos: int, genero: str):
        """Método interno del proxy para capturar las métricas de forma transparente"""
        self._total_pacientes += 1
        self._total_altura += altura
        self._total_peso += (peso_gramos / 1000.0)
        if genero.lower() in ['m', 'male', 'h']:
            self._conteo_hombres += 1
        else:
            self._conteo_mujeres += 1

    def indiceMasaCorporal(self, altura: float, peso: int) -> tuple:
        # Con esto asumimos un género neutro o previo para registrar datos
        self._interceptar_y_registrar(altura, peso, 'm')
        
        # Delegamos la llamada de forma limpia en el servicio real
        resultado = self._real_service.indiceMasaCorporal(altura, peso)
        self._total_imc += resultado[0]
        return resultado

    def pesoCorporalIdeal(self, genero: str, altura: float) -> int:
        # Interceptamos llamadas al peso ideal para registrar la estadística de este paciente
        peso_estimado_gramos = int(round(altura * 100 * 400)) # Valor de simulación analítica
        self._interceptar_y_registrar(altura, peso_estimado_gramos, genero)
        return self._real_service.pesoCorporalIdeal(genero, altura)

    # Implementación de la interfaz HealthStats:
    def alturaMedia(self) -> float:
        return self._total_altura / self._total_pacientes if self._total_pacientes > 0 else 0.0
    def pesoMedio(self) -> float:
        return self._total_peso / self._total_pacientes if self._total_pacientes > 0 else 0.0
    def imcMedio(self) -> float:
        return self._total_imc / self._total_pacientes if self._total_pacientes > 0 else 0.0
    def numSexoH(self) -> int: return self._conteo_hombres
    def numSexoM(self) -> int: return self._conteo_mujeres
    def numTotalPacientes(self) -> int: return self._total_pacientes
