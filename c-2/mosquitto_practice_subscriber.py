import paho.mqtt.client as mqtt
import json
import sqlite3

# DB -> 단순히 subcriber가 데이터를 수신하는 것만이 아닌 실제 IoT 구현을 위함.
conn = sqlite3.connect("sensor_practice.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS sensor (
    time TEXT,
    temperature REAL,
    humidity REAL
)
""")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    print("수신:", data)

    cur.execute(
        "INSERT INTO sensor VALUES (?, ?, ?)",
        (data["timestamp"], data["temperature"], data["humidity"])
    )

    conn.commit()

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883)
client.subscribe("iot/sensor/env")

print("Subscriber 대기 중...")

client.loop_forever()
