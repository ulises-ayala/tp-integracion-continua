from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Obtiene el modelo de sintetizador de la URL (por defecto es 'dashboard')
    modelo = request.args.get('model', 'dashboard')
    
    # Valida que no pongan cualquier cosa en la URL
    modelos_permitidos = ['dashboard', 'minimoog', 'juno', 'prophet', 'dx7']
    if modelo not in modelos_permitidos:
        modelo = 'dashboard'
        
    return render_template('index.html', model=modelo)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')