import pandas as pd
from faker import Faker
import random


def create_fake_address_book(count: int = 100):
    """
    가짜 이름, 성별, 이메일, 전화번호를 무작위로 생성하여
    엑셀 파일(주소록.xlsx)로 저장하는 함수
    """

    fake = Faker("ko_KR")  # 한국어 데이터 기반
    Faker.seed(0)

    data = []

    for i in range(1, count + 1):
        gender = random.choice(["남성", "여성"])
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()

        data.append([
            i,        # 번호
            name,     # 이름
            gender,   # 성별
            email,    # 이메일
            phone     # 전화번호
        ])

    # 데이터프레임 생성
    df = pd.DataFrame(
        data,
        columns=["번호", "이름", "성별", "이메일", "전화번호"]
    )

    # 엑셀 파일로 저장 (현재 경로)
    file_name = "주소록.xlsx"
    df.to_excel(file_name, index=False)

    print(f"[완료] 가짜 주소록 {count}개 생성")
    print(f"저장 파일: {file_name}")


# 실행
if __name__ == "__main__":
    create_fake_address_book(100)
