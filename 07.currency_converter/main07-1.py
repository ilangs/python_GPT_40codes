# 환율에 따라서 화폐를 변환하는 환율 변환기

import requests


def convert_currency(from_currency: str, amount: float, to_currency: str) -> float:
    """
    실시간 환율을 이용해 화폐를 변환하는 함수 (가입/API 키 불필요)

    :param amount: 변환할 금액
    :param from_currency: 기준 통화 (예: 'USD')
    :param to_currency: 변환 대상 통화 (예: 'KRW')
    :return: 변환된 금액
    """

    # exchangerate.host 환율 변환 API 엔드포인트
    url = "https://api.exchangerate.host/convert"

    # API 요청 파라미터
    params = {
        "from": from_currency.upper(),
        "amount": amount,
        "to": to_currency.upper()
       }

    # GET 요청
    response = requests.get(url, params=params)
    response.raise_for_status()  # HTTP 오류 발생 시 예외 처리

    data = response.json()

    # 변환 결과 추출
    if data.get("success"):
        return data["result"]
    else:
        raise ValueError("환율 변환에 실패했습니다.")
    

from_currency = input("기준 통화를 입력하세요 (예: USD): ").upper()
amount = float(input(f"변환할 {from_currency} 금액을 입력하세요: "))
to_currency = input("변환할 통화를 입력하세요 (예: KRW): ").upper()

result = convert_currency(from_currency, amount, to_currency)

print(f"{amount} {from_currency} → {result:.2f} {to_currency}")

