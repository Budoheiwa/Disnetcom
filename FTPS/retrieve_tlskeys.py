#!/usr/bin/python3 

from scapy.all import *
import subprocess
import os
    
def retrieve_tls_keys(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
 
if __name__ == "__main__":
    print("Retrieving the traffic secrets from SSL/TLS handshake !" + '\n')
    command = "sudo SSLKEYLOGFILE=./tlskeys.txt LD_PRELOAD=./libsslkeylog.so ./ftps_upload.py"
    retrieve_tls_keys(command)
    print("\r"+"#" * 50 + "\n")
    print("--File tlskeys.txt generated--"+'\n')
    print("\r"+"#" * 50 + "\n")
   
    
   
    
    
