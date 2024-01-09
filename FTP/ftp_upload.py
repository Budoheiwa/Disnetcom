#!/usr/bin/python3
from ftplib import FTP
import os

def upload_file(ftp, local_file_path, remote_file_name):
    with open(local_file_path, 'rb') as file:
        ftp.storbinary(f'STOR {remote_file_name}', file)

def upload_files(ftp, files):
    for local_file_path, remote_file_name in files:
        upload_file(ftp, local_file_path, remote_file_name)

def main():
    ftp_server = '172.21.0.2'
    ftp_user = 'admin'
    ftp_password = 'passadmin'

    base_dir = os.path.dirname(os.path.abspath(__file__))
    files_to_upload = [
        (os.path.join(base_dir, 'files', 'test.txt'), 'test.txt'),
        (os.path.join(base_dir, 'files', 'hash.txt'), 'hash.txt'),
        (os.path.join(base_dir, 'files', 'password.txt'), 'password.txt'),
        (os.path.join(base_dir, 'files', 'coucou.txt'), 'coucou.txt'),
        (os.path.join(base_dir, 'files', 'truePassword.txt'), 'truePassword.txt')    
    ]
    ftp = None
    try:
        # Connect to the FTP server
        ftp = FTP(ftp_server)
        ftp.login(user=ftp_user, passwd=ftp_password)

        # Upload the files
        upload_files(ftp, files_to_upload)

        print("Files uploaded successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Disconnect from the FTP server
        if ftp:
            ftp.quit()

if __name__ == "__main__":
    main()
