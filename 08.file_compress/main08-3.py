# 디렉터리(폴더) 전체를 ZIP으로 압축하는 함수

import zipfile, os

def compress_directory(dir_path: str, zip_path: str):
    """
    디렉터리(폴더) 전체를 ZIP으로 압축하는 함수

    :param dir_path: 압축할 폴더 경로
    :param zip_path: 생성될 ZIP 파일 경로
    """

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # os.walk를 이용해 폴더 내부를 재귀적으로 순회
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                full_path = os.path.join(root, file)

                # ZIP 내부에서의 상대 경로 유지
                arcname = os.path.relpath(full_path, start=dir_path)

                zipf.write(full_path, arcname=arcname)

    print(f"[완료] {dir_path} → {zip_path}")
    
if __name__ == "__main__" :
    compress_directory("my_folder", "my_folder.zip")