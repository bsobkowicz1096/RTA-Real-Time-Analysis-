from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API z regula decyzyjna. Uzyj /api/v1.0/predict z parametrami num1 i num2."})

@app.route('/api/v1.0/predict')
def predict():
    # Pobranie parametrów z zapytania GET
    # Jeśli parametry nie są podane, domyślnie ustawia wartość 0
    num1 = request.args.get('num1', default=0, type=float)
    num2 = request.args.get('num2', default=0, type=float)
    
    # Zastosowanie reguły decyzyjnej
    sum_values = num1 + num2
    prediction = 1 if sum_values > 5.8 else 0
    
    # Przygotowanie odpowiedzi
    response = {
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    }
    
    return jsonify(response)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)