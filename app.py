from flask import Flask, render_template, request, jsonify
import pandas as pd
import math

app = Flask(__name__)

# Función para calcular la distancia usando la fórmula de Haversine
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radio de la Tierra en kilómetros
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400
    
    # Procesar el archivo CSV
    data = pd.read_csv(file)
    
    # Calcular distancias entre cada par de puntos
    distances = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            lat1, lon1 = data.iloc[i]['latitude'], data.iloc[i]['longitude']
            lat2, lon2 = data.iloc[j]['latitude'], data.iloc[j]['longitude']
            distance = haversine(lat1, lon1, lat2, lon2)
            distances.append({
                "point1": data.iloc[i]['nombre'],
                "point2": data.iloc[j]['nombre'],
                "distance_km": distance
            })
    
    return jsonify(distances)

if __name__ == '__main__':
    app.run(debug=True)
