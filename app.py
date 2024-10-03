from flask import Flask, render_template, request

app = Flask(__name__)

# Function for basic arithmetic operations
def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation!"

# Route for the calculator page
@app.route("/", methods=["GET", "POST"])
def calculate():
    result = ""
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]
        result = calculator(num1, num2, operation)
    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)