#!/usr/bin/python3 
import subprocess
import os

def upload_ftps_files():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, "ftps_upload.py")
    subprocess.run(["sudo", "python3", script_path])

def retrieve_tls_keys():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, "retrieve_tlskeys.py")
    subprocess.run(["sudo", "python3", script_path])
    
    print("--Retrieving the certificate Client/Server TLS/FTP traffic--"+"\n")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    certificate_path = os.path.join(base_dir,"certificate.pem")
    
    command = f"sudo openssl s_client -connect 172.21.0.2:21 -starttls ftp -showcerts </dev/null | openssl x509 -out {certificate_path}"
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

print("1 ==> Uploading files directly to FTPS server using SSL/TLS secret communications" + '\n' + "2 ==> Retrieving TLS keys and Certificate while uploading files to FTPS server + Decrypting packets" + '\n')
enter = str(input("Choose between 1 and 2: "))

if enter == '1':
    print('\n' + "Code 1: Uploading files to FTPS server")
    upload_ftps_files()

elif enter == '2':
    print('\n' + "Code 2: Retrieving TLS keys and Certificate + Decrypting packets")
    retrieve_tls_keys()

else:
    print("--Exiting the script--")
    print("#" * 50 + "\n")

print("\n"+"--Exiting the script--"+"\n")
print("#" * 50 + "\n")
    
