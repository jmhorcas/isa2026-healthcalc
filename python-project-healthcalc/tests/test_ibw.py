import pytest
from healthcalc import HealthCalcImpl


class TestIBW:

    def setup_method(self):
        self.health_calc = HealthCalcImpl()

    # --- IBW calculation tests ---

    def test_ibw_male(self):
        height = 180
        result = self.health_calc.ibw_lorentz_metric(height, "male")

        expected = (180 - 100) - ((180 - 150) / 4.0)

        assert result == pytest.approx(expected, abs=0.01)

    def test_ibw_female(self):
        height = 165
        result = self.health_calc.ibw_lorentz_metric(height, "female")

        expected = (165 - 100) - ((165 - 150) / 2.0)

        assert result == pytest.approx(expected, abs=0.01)

    # --- error tests ---

    def test_invalid_gender(self):
        with pytest.raises(Exception):
            self.health_calc.ibw_lorentz_metric(170, "other")

    def test_height_too_low(self):
        with pytest.raises(Exception):
            self.health_calc.ibw_lorentz_metric(30, "male")

    def test_height_too_high(self):
        with pytest.raises(Exception):
            self.health_calc.ibw_lorentz_metric(350, "female")