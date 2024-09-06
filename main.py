from flask import Flask, render_template
from datos import productos

app = Flask (__name__)

@app.route("/")
def index():
    return render_template('index.html', productos = productos)


@app.route("/producto/<string:nombre>")
def producto (nombre):
    prod=[p for p in productos if p['nombre']==nombre]
    return render_template('producto.html', producto=prod[0] )

app.run(host= '0.0.0.0', port = 8000, debug=True )
