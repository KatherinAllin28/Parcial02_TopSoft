from flask import Flask, render_template_string
import math

app = Flask(__name__)

@app.route('/factorial/<int:num>')
def factorial(num):
    try:
        result = math.factorial(num)
        return render_template_string("""
            <h1>Factorial de {{ num }} es {{ result }}</h1>
        """, num=num, result=result)
    except ValueError:
        return "El número debe ser un entero no negativo", 400

if __name__ == '__main__':
    app.run(debug=True)
