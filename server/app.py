#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<text>')
def print_text(text):
    # also print to console (tests capture stdout)
    print(text)
    return text


@app.route('/count/<int:n>')
def count(n):
    # return numbers from 0..n-1 each on its own line
    if n <= 0:
        return ''
    return '\n'.join(str(i) for i in range(n)) + '\n'


@app.route('/math/<int:x>/<op>/<int:y>')
def math_op(x, op, y):
    # support +, -, *, div (float division), and %
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == 'div':
        # produce float for division
        result = x / y
    elif op == '%':
        result = x % y
    else:
        return 'Unsupported operation', 400

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
