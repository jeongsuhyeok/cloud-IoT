"""
    시스템 구성
    - 버튼 입력(임의의 난수 데이터 생성): 실제 버튼 하드웨어 대신 난수를 이용해 버튼이 눌린 상황과 눌리지 않은 상황을 가상으로 생성한다. 이를 통해 GPIO 입력 신호가 들어오는 흐름을 소프트웨어적으로 모의 실험한다.

    - LED 상태 제어: 생성된 버튼 입력값에 따라 LED의 ON/OFF 상태를 변경하도록 구현한다. 이를 통해 입력 신호가 출력 장치 제어로 이어지는 GPIO 동작 구조를 확인한다.

    - 센서 데이터 생성 (온도/습도): 온도와 습도 값을 난수 범위로 생성하여 실제 센서값처럼 처리한다. 이를 통해 IoT 환경에서 주기적으로 발생하는 센서 데이터 흐름을 실습한다.

    - CSV 저장: 생성된 센서 데이터와 LED 상태 등의 결과를 CSV 파일로 저장한다. 이를 통해 수집된 IoT 데이터를 기록하고, 이후 분석 가능한 형태로 남기는 과정을 학습한다.

    """

from gpiozero import LED
import random
import time
import csv

# LED 설정 (가상 GPIO)
led = LED(17)

# CSV 파일 생성
filename = "c1_sensor_data.csv"

with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "button", "led_state", "temperature", "humidity"])

    print("실습 시작... (Ctrl+C로 종료)")

    try:
        for i in range(10):  # 10회 반복

            # 1. 가상 버튼 입력 (0 또는 1)
            button = random.choice([0, 1])

            # 2. 버튼이 눌렸으면 LED 토글
            if button == 1:
                led.toggle()

            # LED 상태 확인
            led_state = led.is_lit

            # 3. 센서 데이터 생성
            temperature = round(random.uniform(20, 30), 2)
            humidity = round(random.uniform(40, 60), 2)

            # 현재 시간 -> 실제 csv에 저장하기 위함
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")

            # 출력
            print(f"[{current_time}] 버튼:{button} LED:{led_state} 온도:{temperature} 습도:{humidity}")

            # 4. CSV 저장
            writer.writerow([current_time, button, led_state, temperature, humidity])

            # 5초 대기
            time.sleep(5)

    except KeyboardInterrupt:
        print("실습 종료")
