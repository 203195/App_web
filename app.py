from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)

catalogo = [
    {'id': 1, 'nombre': 'Pan', 'precio': 20},
    {'id': 2, 'nombre': 'Leche', 'precio': 10},
    {'id': 3, 'nombre': 'Huevo', 'precio': 5},
    {'id': 4, 'nombre': 'Queso', 'precio': 30},
    {'id': 5, 'nombre': 'Carne', 'precio': 80},
]

@app.route('/')
def home():
    print(catalogo)
    return render_template('index.html', productos=catalogo)

@app.route('/agregar/<int:id>')
def agregar(id):
    if 'carrito' not in session:
        session['carrito'] = []
    session['carrito'].append(id)
    session.modified = True
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)