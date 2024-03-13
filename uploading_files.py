#!/usr/bin/python3
import subprocess
import os

def exec_ftp_upload():
    command = "sudo python3 FTP/ftp_upload.py"
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    
def exec_ftps_upload():
    command = "sudo python3 FTPS/ftps_choice.py"
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

if __name__ == "__main__":
    print("--Code 1: Executing the ftp_upload.py--"+"\n")
    exec_ftp_upload()
    print("\r"+"#" * 50 + "\n")
    
    print("--Code 2: Executing the ftps_upload.py--"+"\n")
    exec_ftps_upload()
    print("#" * 50 + "\n")
    
    print("Files uploaded successfully."+"\n")
    print("\r"+"--End of the process--")
    print("\r"+"#" * 50 + "\n")