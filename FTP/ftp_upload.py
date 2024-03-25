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
    ftp_server = '172.19.0.2' # Modify according to FTP server's IP address
    ftp_user = 'admin' # Modify the credentials according to docker-compose.yml
    ftp_password = 'passadmin'

    base_dir = os.path.dirname(os.path.abspath(__file__))
    files_directory = os.path.join(base_dir, 'files')
    
    all_files = [(os.path.join(files_directory, file), file) for file in os.listdir(files_directory) if os.path.isfile(os.path.join(files_directory, file))]

    ftp = None
    try:
        ftp = FTP(ftp_server)
        ftp.login(user=ftp_user, passwd=ftp_password)
        upload_files(ftp, all_files)
        print("Files uploaded successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if ftp:
            ftp.quit() 

if __name__ == "__main__":
    main()
