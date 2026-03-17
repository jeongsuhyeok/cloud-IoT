import pandas as pd
import matplotlib.pyplot as plt

# 먼저 fitbit_practice_plt.py가 csv 데이터 생성 시 이를 사용자에게 시각화 데이터를 제공하기 위함.
df = pd.read_csv("fitbit_data.csv")

# 그래프 생성
plt.figure()

plt.plot(df["time"], df["heart_rate"], label="Heart Rate")
plt.plot(df["time"], df["steps"], label="Steps")

plt.xlabel("Time (hour)")
plt.ylabel("Value")
plt.title("Fitbit Data Analysis")

plt.legend()
plt.show()