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
    print("Retrieving the premasterkey from SSL/TLS handshake !")
    command = "sudo SSLKEYLOGFILE=./premasterkey.txt LD_PRELOAD=/tmp/libsslkeylog.so ./ftps_upload"
    retrieve_ssl_premasterkey(command)
    print("\r"+"#" * 50 + "\n")
   
    
   
    
    
