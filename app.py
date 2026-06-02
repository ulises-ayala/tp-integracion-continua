from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Lista de configuraciones para el Minimoog
    presets = [
        {
            "nombre": "Lead Clásico - Shine On You Crazy Diamond",
            "osciladores": "Osc 1: Square 8' | Osc 2: Saw 8' (Detune +2) | Osc 3: Tri 4'",
            "filtro": "Cutoff 40% - Resonancia 10%",
            "modulacion": "Glide On (30%) - LFO a Pitch",
            "nota": "Ideal para solos con mucha expresividad."
        },
        {
            "nombre": "Bajo Pesado - Have a Cigar",
            "osciladores": "Osc 1: Saw 16' | Osc 2: Square 16' (Detune -1) | Osc 3: Saw 32'",
            "filtro": "Cutoff 20% - Resonancia 30% - Env Amount 70%",
            "modulacion": "Glide Off - Ataque rápido",
            "nota": "Un bajo bien gordo y percusivo para marcar el ritmo."
        },
        {
            "nombre": "Sui Generis Flute Lead",
            "osciladores": "Osc 1: Triangle 8' | Osc 2: Triangle 8' (Detune leve)",
            "filtro": "Cutoff 60% - Resonancia 0%",
            "modulacion": "Glide Off - Modulación sutil de amplitud",
            "nota": "Tono suave, parecido a una flauta traversa."
        },
        {
            "nombre": "Brass Progresivo",
            "osciladores": "Osc 1: Saw 8' | Osc 2: Saw 8' (Detune -3) | Osc 3: Saw 4'",
            "filtro": "Cutoff 50% - Resonancia 20% - Env Amount 50%",
            "modulacion": "Ataque medio (Fade in) - Glide Off",
            "nota": "Perfecto para acordes majestuosos."
        }
    ]
    
    preset_elegido = random.choice(presets)
    return render_template('index.html', preset=preset_elegido)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')