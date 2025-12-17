#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f"<h2>You entered: {param}</h2>"

@app.route('/count/<int:number>')
def count(number):
    output = ""
    for i in range(number):
        output += f"{i}<br>"
    return output

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation.lower() == 'div':
        if num2 == 0:
            return "<h2>Error: Division by zero!</h2>"
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return "<h2>Error: Modulo by zero!</h2>"
        result = num1 % num2
    else: 
        return "<h2>Error: Invalid operation. Use +, -, *, div, or %.</h2>"
    
    return f"<h2>Result: {num1} {operation} {num2} = {result}</h2>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
