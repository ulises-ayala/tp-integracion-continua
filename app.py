from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Una lista temática para darle onda
    canciones = [
        "Shine On You Crazy Diamond - Pink Floyd",
        "Firth of Fifth - Genesis",
        "Canción para mi muerte - Sui Generis",
        "Génesis - Vox Dei",
        "Have a Cigar - Pink Floyd"
    ]
    cancion_elegida = random.choice(canciones)
    return render_template('index.html', cancion=cancion_elegida)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')