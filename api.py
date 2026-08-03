Python
import requests

# 1. 아마란스 10 도메인 주소 (회사 ERP 접속 주소로 변경 필요)
BASE_URL = "https://gw.fsn.co.kr/" 
API_PATH = "/apiproxy/api16S08"  # 회사등록조회 API

# 2. 제공해주신 인증 키 적용
headers = {
    "AccessToken": "rBTUrWZA4klwucYIrVoyqlb9dzC37z",
    "HashKey": "80338340471996318389875569045954485561741835",
    "Content-Type": "application/json; charset=utf-8"
}

# 3. API 호출
try:
    response = requests.get(BASE_URL + API_PATH, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print("✅ 데이터 연결 성공!")
        print(result)
    else:
        print(f"❌ 호출 실패 (상태코드: {response.status_code})")
        print(response.text)

except Exception as e:
    print(f"오류 발생: {e}")
