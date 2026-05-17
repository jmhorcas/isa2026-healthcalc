import sys
from pathlib import Path
from flask import Flask, render_template, request

sys.path.insert(0, str(Path(__file__).parent / "python-project-healthcalc"))
from healthcalc.health_calc_impl import HealthCalcImpl

app = Flask(__name__)
calculator = HealthCalcImpl()


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    classification = None
    error = None

    if request.method == "POST":
        try:
            metric = request.form.get("metric")
            height = request.form.get("height")
            weight = request.form.get("weight")
            age = request.form.get("age")
            gender = request.form.get("gender")

            if not metric:
                raise ValueError("Selecciona una métrica antes de calcular.")

            if metric == "bmi":
                if not weight or not height:
                    raise ValueError("Para BMI debes introducir peso y altura.")

                weight = float(weight)
                height = float(height) / 100
                result = round(calculator.bmi(weight, height), 2)
                classification = calculator.bmi_classification(result)

            elif metric == "ibw":
                if not height or not gender:
                    raise ValueError("Para IBW debes introducir altura y género.")

                height = float(height)
                result = round(calculator.ibw_lorentz_metric(height, gender), 2)

            elif metric == "bmr":
                if not weight or not age or not gender:
                    raise ValueError("Para BMR debes introducir peso, edad y género.")

                weight = float(weight)
                age = int(age)
                result = round(calculator.bmr_metric(weight, age, gender), 2)

            else:
                raise ValueError("La métrica seleccionada no es válida.")

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        result=result,
        classification=classification,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)