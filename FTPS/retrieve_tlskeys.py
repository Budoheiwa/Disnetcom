#!/usr/bin/python3 

from scapy.all import *
import subprocess
import os
    
def retrieve_tls_keys(command, cwd=None):
    try:
        subprocess.run(command, check=True, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
 
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    libsslkeylog = os.path.join(base_dir, "libsslkeylog.so")
    ftps_upload_script = os.path.join(base_dir, "ftps_upload.py")

    print("Retrieving the traffic secrets from SSL/TLS handshake !" + '\n')

    command = f"sudo SSLKEYLOGFILE=./tlskeys.txt LD_PRELOAD={libsslkeylog} {ftps_upload_script}"
    retrieve_tls_keys(command)
    
    print("\r"+"#" * 50 + "\n")
    print("--File tlskeys.txt generated--"+'\n')
    print("\r"+"#" * 50 + "\n")
   
    
   
    
    
