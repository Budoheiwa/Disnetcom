#!/usr/bin/python3 

from scapy.all import *
import subprocess
import os
    
def retrieve_ssl_premasterkey(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

if __name__ == "__main__":
    print("Retrieving the traffic secrets from SSL/TLS handshake !")
    command = "sudo SSLKEYLOGFILE=./tlskeys.txt LD_PRELOAD=./libsslkeylog.so ./ftps_upload.py"
    retrieve_ssl_premasterkey(command)
    print("\r"+"#" * 50 + "\n")
   
    
   
    
    
