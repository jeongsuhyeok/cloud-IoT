import pandas as pd
import random
import time

data = []

# 실제 fitbit처럼 wearable하도록 24시간을 가정하고 24개의 mock 데이터 구현
for i in range(24):

    record = {
        "time": i,
        "heart_rate": random.randint(60, 120),
        "steps": random.randint(0, 500),
        "calories": random.randint(50, 200)
    }

    data.append(record)

df = pd.DataFrame(data)

df.to_csv("fitbit_data.csv", index=False)

print("Fitbit 데이터 생성 완료")