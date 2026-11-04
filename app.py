from flask import Flask, render_template, request

app = Flask(__name__)

def calculate(a, b, op):
    if op == "add":
        return a + b
    if op == "sub":
        return a - b
    if op == "mul":
        return a * b
    if op == "div":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    raise ValueError("Unknown operation")

@app.route("/", methods=["GET", "POST"])
def index():
    result = error = None

    if request.method == "POST":
        try:
            a = float(request.form["num1"])
            b = float(request.form["num2"])
            result = calculate(a, b, request.form["operation"])
            result = int(result) if result == int(result) else round(result, 4)
        except ZeroDivisionError as e:
            error = str(e)
        except ValueError:
            error = "Please enter valid numbers"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)