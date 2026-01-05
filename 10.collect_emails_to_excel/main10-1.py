# 특정 웹사이트에서 이메일 주소를 수집하여 엑셀 파일로 저장하는 함수
    
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup


def collect_emails_to_excel(
    url: str,
    output_excel_path: str
):
    """
    특정 웹사이트에서 이메일 주소를 수집하여
    엑셀 파일로 저장하는 함수

    :param url: 이메일을 수집할 웹사이트 URL
    :param output_excel_path: 저장할 엑셀 파일 경로
    """

    # 1. 웹페이지 요청
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # 요청 실패 시 예외 발생

    # 2. HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 페이지 전체 텍스트 추출
    text = soup.get_text()

    # 3. 이메일 정규식 패턴
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # 정규식을 이용해 이메일 추출
    emails = re.findall(email_pattern, text)

    # 중복 제거
    unique_emails = sorted(set(emails))

    # 4. 엑셀 저장용 데이터프레임 생성
    df = pd.DataFrame(unique_emails, columns=["Email"])

    # 5. 엑셀 파일로 저장
    df.to_excel(output_excel_path, index=False)

    print("===== 수집 완료 =====")
    print(f"URL: {url}")
    print(f"수집된 이메일 수: {len(unique_emails)}")
    print(f"저장 파일: {output_excel_path}")

    
url = "https://example.com"
output_file = "emails.xlsx"

collect_emails_to_excel(url, output_file)
