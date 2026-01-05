# 영어 파일을 읽어서 한글 번역 후 파일로 저장하는 프로그램

from googletrans import Translator


def translate_file_to_korean(input_file_path: str,output_file_path: str):
    """
    영어 텍스트 파일을 읽어서 한글로 번역한 후
    새로운 파일로 저장하는 함수

    :param input_file_path: 영어 텍스트 파일 경로
    :param output_file_path: 번역된 한글 파일 저장 경로
    """

    # Translator 객체 생성
    translator = Translator()

    # 1. 영어 파일 읽기
    with open(input_file_path, "r", encoding="utf-8") as f:
        english_text = f.read()

    # 2. 영어 → 한국어 번역
    # src='en' : 원문 언어 (영어)
    # dest='ko': 번역 언어 (한국어)
    translated = translator.translate(
        english_text,
        src='en',
        dest='ko'
    )

    korean_text = translated.text

    # 3. 번역된 내용을 파일로 저장
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(korean_text)

    print("[완료] 번역문서가 성공적으로 저장되었습니다.")
    print(f"입력 파일: {input_file_path}")
    print(f"출력 파일: {output_file_path}")
