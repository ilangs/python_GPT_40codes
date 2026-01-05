# 압축 파일 암호 푸는 프로그램

import zipfile
import itertools
import string


def crack_zip_password(zip_path: str, min_len: int = 1, max_len: int = 9):
    """
    ZIP 파일의 암호를 영문자(a-zA-Z) 브루트포스로 찾는 함수

    :param zip_path: 암호가 걸린 ZIP 파일 경로
    :param min_len: 암호 최소 길이 (기본값 1)
    :param max_len: 암호 최대 길이 (기본값 9)
    :return: 암호를 찾으면 문자열 반환, 실패 시 None 반환
    """

    # 사용할 문자 집합: 소문자 + 대문자
    characters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # ZIP 파일 열기
    with zipfile.ZipFile(zip_path, 'r') as zf:
        # ZIP 내부 첫 번째 파일 이름을 가져옴
        # (비밀번호 검증용으로 사용)
        target_file = zf.namelist()[0]

        # 암호 길이를 1부터 max_len까지 순차적으로 증가
        for length in range(min_len, max_len + 1):
            print(f"[INFO] Trying passwords of length {length}")

            # itertools.product를 이용해 모든 문자 조합 생성
            for candidate in itertools.product(characters, repeat=length):
                # 튜플 형태의 문자 조합을 문자열로 변환
                password = ''.join(candidate)

                try:
                    # ZIP 파일에 비밀번호를 bytes 형태로 전달해야 함
                    zf.extract(member=target_file, pwd=password.encode('utf-8'))

                    # 여기까지 왔다면 암호가 맞았다는 의미
                    print(f"[SUCCESS] Password found: {password}")
                    return password

                except RuntimeError:
                    # 비밀번호가 틀렸을 때 발생
                    pass
                except zipfile.BadZipFile:
                    # ZIP 파일 자체가 손상된 경우
                    print("[ERROR] Bad ZIP file.")
                    return None

    # 모든 경우를 시도했지만 실패한 경우
    print("[FAIL] Password not found.")
    return None


zip_file_path = "secret.zip"
result = crack_zip_password(zip_file_path)

if result:
    print("찾은 암호:", result)
else:
    print("암호를 찾지 못했습니다.")