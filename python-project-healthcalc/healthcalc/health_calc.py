from abc import ABC, abstractmethod
from healthcalc import InvalidHealthDataException


class HealthCalc(ABC):
    """Interface for the calculator of health parameters."""

    @abstractmethod
    def bmi_classification(self, bmi: float) -> str:
        """Calculate the BMI classification of a person.

        :param bmi: Body Mass Index (kg/m2)
        :return: String classification
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def bmi(self, weight: float, height: float) -> float:
        """Calculate the Body Mass Index (BMI).
        
        :param weight: Weight (kg)
        :param height: Height (m)
        :return: BMI value (kg/m2)
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def ibw(self, height_cm: float, gender: str) -> float:
        """Calculate the Ideal Body Weight (IBW) based on Lorentz Formula.
        
        :param height_cm: Height (cm)
        :param gender: Gender ('man' or 'woman')
        :return: Ideal Body Weight (kg)
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def news2(frecResp: float, oxSat: float, oxSup: bool, preArtSis: float, frecCard: float, consciente: bool, temp: float):
        """Calculate NEWS2 score.
        
        :param frecResp: Respiratory rate (per minute)
        :param oxSat: Oxigen saturation (%)
        :param oxSup: Oxigen support (True/False)
        :param preArtSis: Systolic blood pressure (mmHg)
        :param frecCard: Heart rate (per minute)
        :param consciente: Concience level (True/False)
        :param temp: Temperature (ºC)
        :return: NEWS2 score
        :raises InvalidHealthDataException: If data is out of range
        """
        pass
