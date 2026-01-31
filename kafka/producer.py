import json
import time
import requests
import random
from kafka import KafkaProducer
from datetime import datetime
from config import API_KEY, KAFKA_BROKER, TOPIC_NAME, STOCK_SYMBOL

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

USE_MOCK_DATA=True
URL = "https://www.alphavantage.co/query"

def fetch_stock_data():
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": STOCK_SYMBOL,
        "interval": "1min",
        "apikey": API_KEY
    }
    response = requests.get(URL, params=params)
    return response.json()

def send_to_kafka():
    if USE_MOCK_DATA:
        message = {
            "symbol": STOCK_SYMBOL,
            "price": round(random.uniform(150, 200), 2),
            "high": round(random.uniform(200, 210), 2),
            "low": round(random.uniform(140, 150), 2),
            "volume": random.randint(1000, 10000),
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "ingested_at": datetime.utcnow().isoformat()
        }

        producer.send(TOPIC_NAME, message)
        producer.flush()

        print("Sent (MOCK):", message)
        time.sleep(5)
        return

# def send_to_kafka():
#     data = fetch_stock_data()
#     print(data)
#     if "Time Series (1min)" not in data:
#         print("API limit hit. Retrying after cooldown...")
#         time.sleep(60)
#         return

#     time_series = data["Time Series (1min)"]
#     latest_time = list(time_series.keys())[0]
#     latest_data = time_series[latest_time]

#     message = {
#         "symbol": STOCK_SYMBOL,
#         "price": float(latest_data["1. open"]),
#         "high": float(latest_data["2. high"]),
#         "low": float(latest_data["3. low"]),
#         "volume": int(latest_data["5. volume"]),
#         "timestamp": latest_time,
#         "ingested_at": datetime.utcnow().isoformat()
#     }

#     producer.send(TOPIC_NAME, message)
#     producer.flush()
#     print("Sent:", message)

if __name__ == "__main__":
    while True:
        send_to_kafka()
        time.sleep(40)   # safe for free tier
