# 🔍 Zadanie 1 - Model z regułą decyzyjną

## 📝 Opis
Prosty serwis API implementujący regułę decyzyjną zgodnie z wymaganiami zadania. API obsługuje endpoint `/api/v1.0/predict` i przyjmuje dwie liczby. Jeśli suma dwóch liczb jest większa niż 5.8, zwraca jako predykcję wartość 1, w przeciwnym razie zwraca 0.

## 📂 Struktura projektu
- `app.py` - główny plik aplikacji Flask
- `requirements.txt` - zależności projektu
- `Dockerfile` - konfiguracja kontenera Docker
- `README.md` - dokumentacja projektu

## ⚙️ Funkcjonalności
- Obsługa endpointu `/api/v1.0/predict` przyjmującego parametry `num1` i `num2`
- Zastosowanie domyślnej wartości 0 dla niepodanych parametrów
- Implementacja reguły decyzyjnej: jeśli suma > 5.8 zwraca 1, w przeciwnym razie 0
- Zwracanie odpowiedzi w formacie JSON z kluczami "prediction" i "features"

## 🛠️ Wymagania
- 🐍 Python 3.11
- 🌶️ Flask 3.0.3
- 🐳 Docker

## 🚀 Uruchomienie aplikacji

### Lokalnie (bez Dockera)
```bash
# Instalacja zależności
pip install -r requirements.txt

# Uruchomienie aplikacji
flask run
```

### Z użyciem Dockera 🐳
```bash
# Budowanie obrazu
docker build -t decision-rule-api .

# Uruchomienie kontenera
docker run -p 5000:5000 decision-rule-api
```

## 📊 Przykłady użycia

### Przykład 1: Suma większa niż 5.8 ✅
```
GET http://localhost:5000/api/v1.0/predict?num1=3&num2=4
```

Odpowiedź:
```json
{
  "prediction": 1,
  "features": {
    "num1": 3.0,
    "num2": 4.0
  }
}
```

### Przykład 2: Suma mniejsza niż 5.8 ❌
```
GET http://localhost:5000/api/v1.0/predict?num1=2&num2=3
```

Odpowiedź:
```json
{
  "prediction": 0,
  "features": {
    "num1": 2.0,
    "num2": 3.0
  }
}
```

### Przykład 3: Z domyślnymi wartościami 🔄
```
GET http://localhost:5000/api/v1.0/predict
```

Odpowiedź:
```json
{
  "prediction": 0,
  "features": {
    "num1": 0.0,
    "num2": 0.0
  }
}
```

## 🔧 Technologie
- 🐍 Python
- 🌶️ Flask
- 🐳 Docker
