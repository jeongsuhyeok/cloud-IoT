import paho.mqtt.client as mqtt
import json
import random
import time

# MQTT 클라이언트 생성
client = mqtt.Client()

# 브로커 연결, PORT 번호 1883 -> 국제 규약을 맺은 PORT 번호
client.connect("localhost", 1883)

print("Publisher 시작")

# 1. 데이터 생성
data = {
    "device_id": "rpi5-001",
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    "temperature": round(random.uniform(20, 30), 2),
    "humidity": round(random.uniform(40, 60), 2)
}

# 2. JSON 변환 -> subscriber와의 규약 준수
payload = json.dumps(data)

# 3. 메시지 전송
client.publish("iot/sensor/env", payload)

print("전송 완료:", payload)

# 4. 연결 종료
client.disconnect()
