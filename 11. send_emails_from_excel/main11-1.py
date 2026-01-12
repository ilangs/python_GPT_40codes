import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_emails_from_excel(
    excel_path: str,
    sender_email: str,
    sender_password: str
):
    """
    엑셀 파일을 읽어 이메일 주소로 자동 메일을 발송하는 함수 (Gmail)

    엑셀 구조:
    A열: 번호
    B열: 이름
    C열: 전화번호
    D열: 이메일

    :param excel_path: 엑셀 파일 경로
    :param sender_email: 발신자 이메일 주소
    :param sender_password: 이메일 앱 비밀번호
    """

    # 1. 엑셀 파일 읽기
    df = pd.read_excel(excel_path)

    # 2. SMTP 서버 연결 (Gmail 기준)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # 3. 각 행을 순회하며 이메일 발송
    for index, row in df.iterrows():
        name = row[1]     # B열: 이름
        email = row[3]    # D열: 이메일 주소

        # 메일 제목
        subject = "새해 인사드립니다"

        # 메일 본문 (요청하신 문구 그대로)
        body = (
            f"{name}님, 안녕하십니까?\n\n"
            "새해에는 원하시는 일 모두 이루시고,\n"
            "가족분들 모두에 건강과 행운이 깃드시길 바랍니다.\n\n"
            "새해 복 많이 받으세요."
        )

        # MIME 메일 구성
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain", "utf-8"))

        try:
            # 메일 발송
            server.sendmail(sender_email, email, message.as_string())
            print(f"[성공] {name} ({email}) 전송 완료")
        except Exception as e:
            print(f"[실패] {name} ({email}) - {e}")

    # 4. 서버 종료
    server.quit()
    print("모든 메일 발송 작업이 완료되었습니다.")
    


send_emails_from_excel(
    excel_path="email_list.xlsx",
    sender_email="your_email@gmail.com",
    sender_password="앱비밀번호"
)

# 홍길동님, 안녕하십니까?

# 새해에는 원하시는 일 모두 이루시고,
# 가족분들 모두에 건강과 행운이 깃드시길 바랍니다.

# 새해 복 많이 받으세요.
