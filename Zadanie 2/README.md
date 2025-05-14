# 📊 Zadanie 2 - Strumieniowanie danych w Apache Spark

## 📝 Opis
Implementacja zadań z laboratorium 7 dotyczących strumieniowania danych, agregacji i segmentacji klientów w czasie rzeczywistym przy użyciu Apache Spark Structured Streaming.

## 📥 Pobranie repozytorium

Aby pobrać to repozytorium, wykonaj następujące kroki:

```bash
# Klonuj repozytorium
git clone https://github.com/bsobkowicz1096/Real_Time_Analysis.git

# Przejdź do katalogu projektu
cd Real_Time_Analysis/Zadanie\ 2
```

## 📂 Struktura projektu
- `generator.py` - Generator danych JSON do ćwiczeń
- `rate_source.py` - Wykorzystanie rate jako źródła kontrolowanego strumienia
- `filtering.py` - Filtrowanie danych bez agregacji (append mode)
- `json_source.py` - Odczyt strumieniowy z plików JSON
- `counting.py` - Bezstanowe zliczanie zdarzeń
- `time_windows.py` - Agregacja w tumbling windows (stałe okna czasowe)
- `sliding_window.py` - Agregacja w sliding windows (przesuwne okna czasowe)
- `segmentation.py` - Segmentacja klientów w czasie rzeczywistym
- `requirements.txt` - Lista wymaganych bibliotek

## ⚙️ Funkcjonalności
- Generowanie kontrolowanych strumieni danych
- Przetwarzanie danych JSON w czasie rzeczywistym
- Filtrowanie i agregacja danych strumieniowych
- Implementacja okien czasowych (tumbling, sliding)
- Segmentacja klientów na podstawie ich zachowań
- Różne tryby wyjściowe: append, update, complete

## 🛠️ Wymagania
- 🐍 Python 3.x
- ⚡ Apache Spark
- 📦 PySpark
- 🔄 Kafka-Python

Wszystkie wymagane biblioteki Pythona można zainstalować za pomocą:
```bash
pip install -r requirements.txt
```

## 🚀 Instrukcja uruchomienia

### 1. Instalacja zależności:
```bash
# Instalacja wymaganych bibliotek
pip install -r requirements.txt
```

### 2. Generator danych (dla zadań z JSON):
```bash
# Utwórz katalog dla danych strumieniowych
mkdir -p data/stream

# Uruchom generator w tle
python generator.py &
```

### 3. Uruchomienie zadań:
```bash
# Uruchom wybrane zadanie
spark-submit rate_source.py
```

## 📊 Opis zadań

### 1. Rate Source 📈
Generuje strumień danych z określoną prędkością (5 wierszy/sekundę) i dodaje kolumny identyfikujące użytkownika i typ zdarzenia.

### 2. Filtering 🔍
Filtruje dane strumieniowe, wyświetlając tylko zdarzenia typu "purchase".

### 3. JSON Source 📄
Odczytuje dane JSON generowane w czasie rzeczywistym przez generator.py.

### 4. Counting 🔢
Zlicza zdarzenia pogrupowane według typu.

### 5. Time Windows ⏰
Grupuje zdarzenia w 5-minutowych oknach czasowych i zlicza je dla każdego typu zdarzenia.

### 6. Sliding Window 🔄
Grupuje zdarzenia w przesuwających się 5-minutowych oknach czasowych z 1-minutowym przesunięciem.

### 7. Segmentation 👥
Segmentuje użytkowników na kategorie "Buyer", "Cart abandoner" i "Lurker" w oparciu o ich zachowanie.

## 💡 Uwagi
- Generator tworzy pliki JSON w katalogu `data/stream` co 5 sekund
- Wszystkie programy automatycznie zatrzymują się po przetworzeniu 5 partii danych
- Dane są przetwarzane strumieniowo w czasie rzeczywistym
- Watermark pozwala na zarządzanie opóźnionymi danymi i zwalnianie pamięci
- Błąd "SparkContext has been shutdown" po 5 partiach jest oczekiwanym zachowaniem, ponieważ aplikacja celowo zatrzymuje Spark po tej liczbie przetworzonych partii

## 🔧 Technologie
- 🐍 Python
- ⚡ Apache Spark
- 📊 Structured Streaming
- 📦 PySpark
