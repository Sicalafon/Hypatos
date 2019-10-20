from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request

moje_imie = 'Natalia "Nat'
msg = "Hello World!"

@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(msg, moje_imie,
                         output.lower())

@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)

from flask import url_for, redirect

@app.route('/ui')
def ui():
    return redirect(url_for('static', filename='index.html'))
