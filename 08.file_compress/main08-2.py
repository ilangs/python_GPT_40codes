# 암호 지정 압축 프로그램

import pyzipper

def compress_file_with_password(file_path: str, password: int) :
    with open(file_path, "rb") as f :
        data = f.read()
    
    with pyzipper.AESZipFile(file_path+".zip", "w", compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zip_file:
        zip.file.setpassword(password.encode('utf-8'))
        zip_file.writestr(file_path, data)
        
if __name__ == "__main__" :
    compress_file_with_password("file_path", "password")
       
