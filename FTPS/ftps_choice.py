#!/usr/bin/python3 
import subprocess
import os

def upload_ftps_files():
    subprocess.run(["sudo", "python3", "FTPS/ftps_upload.py"])

def retrieve_tls_keys():
    subprocess.run(["sudo", "python3", "FTPS/retrieve_tlskeys.py"])

    command = "sudo openssl s_client -connect 172.21.0.2:21 -starttls ftp > certificate.pem"
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    
    #subprocess.run(["sudo", "openssl", "s_client", "-connect", "172.21.0.2:21", "-starttls", "ftp"])

print("1 ==> Uploading files directly to FTPS server using SSL/TLS secret communications" + '\n' + "2 ==> Retrieving TLS keys and Certificate while uploading files to FTPS server + Decrypting packets" + '\n')
enter = str(input("Choose between 1 and 2:"))

if enter == '1':
    print('\n' + "Code 1: Uploading files to FTPS server")
    upload_ftps_files()

elif enter == '2':
    print('\n' + "Code 2: Retrieving TLS keys and Certificate + Decrypting packets")
    retrieve_tls_keys()

else:
    print("--Exiting the script--")
    print("#" * 50 + "\n")

    