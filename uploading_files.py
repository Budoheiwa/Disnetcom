#!/usr/bin/python3
import subprocess
import os

def exec_ftp_upload():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ftp_upload_script = os.path.join(base_dir, "FTP", "ftp_upload.py")
    command = f"sudo python3 {ftp_upload_script}"
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    
def exec_ftps_upload():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ftps_choice_script = os.path.join(base_dir, "FTPS", "ftps_choice.py")
    command = f"sudo python3 {ftps_choice_script}"
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