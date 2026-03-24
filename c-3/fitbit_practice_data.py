import pandas as pd
import json
import glob
import os

# ================================================================
# fitbit_practice_data.py
# 목적: Fitbit 공식 데이터 내보내기(ZIP 해제 후)에서
#       심박수 JSON 파일들을 읽어 CSV로 통합 저장한다.
#
# 실행 전 준비:
#   1. https://www.fitbit.com/settings/data/export 에서 데이터 요청
#   2. 수신된 ZIP 파일 해제
#   3. 해제된 폴더를 프로젝트 루트 아래 FitbitExport/ 에 위치
#
# 출력: fitbit_heart_rate.csv
# ================================================================
# Fitbit 내보내기 ZIP 해제 후 심박수 파일이 위치하는 경로
# 실제 Fitbit 내보내기 폴더 구조:
#   FitbitExport/
#   └── Physical Activity/
#       ├── heart_rate-yyyy-mm-dd.json
#       └── ...

# Fitbit 내보내기 ZIP 해제 후 실제 경로 구조에 맞게 작성
base_path = "./FitbitExport/Physical Activity/"

# 해당 경로가 존재하지 않으면 오류 메시지 출력 후 종료
if not os.path.exists(base_path):
    print(f"[오류] 경로를 찾을 수 없습니다: {base_path}")
    print("FitbitExport/ 폴더가 프로젝트 루트에 위치하는지 확인하세요.")
    exit(1)

# 심박수 데이터 로드
hr_files = glob.glob(os.path.join(base_path, "heart_rate-*.json"))

if not hr_files:
    print(f"[오류] 심박수 파일을 찾을 수 없습니다: {base_path}")
    print("heart_rate-yyyy-mm-dd.json 형식의 파일이 존재하는지 확인하세요.")
    exit(1)

hr_data = []

for f in hr_files:
    with open(f, encoding="utf-8") as fp:
        entries = json.load(fp)
        for entry in entries:
            hr_data.append({
                "datetime": entry["dateTime"],
                "bpm": entry["value"]["bpm"],
                "confidence": entry["value"]["confidence"]
            })

df_hr = pd.DataFrame(hr_data)
df_hr["datetime"] = pd.to_datetime(df_hr["datetime"])
df_hr = df_hr.sort_values("datetime")

df_hr.to_csv("fitbit_data.csv", index=False)

print("Fitbit 데이터 생성 완료")
