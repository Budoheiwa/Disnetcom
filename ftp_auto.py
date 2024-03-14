#!/usr/bin/python3
from scapy.all import *
import subprocess
import os
    
def start_ftp_server(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def exec_sniff_parse():
    subprocess.run(["sudo", "python3", "sniff-parse/sniff_parse_FTP.py"])

if __name__ == "__main__":
    print("Code 1: Starting FTP server")
    command = "sudo docker restart ftp-server"
    start_ftp_server(command)
    print("\r"+"#" * 50 + "\n")
    
    print("Code 2: Sniffing any FTP packets with parse")
    exec_sniff_parse()
    
    print("\r"+"Code 3: Uploading files to FTP server")
    print("--End of uploading--")
    print("\r"+"#" * 50 + "\n")
    
   
    
   
    
    
