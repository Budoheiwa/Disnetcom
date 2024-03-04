#!/usr/bin/python3
import subprocess
import os

def send_files_to_ftps(local_folder_path, ftps_server, ftps_user, ftps_password):
    # Generate lftp commands to connect and send files
    commands = [
        f'lftp -e "set ftp:ssl-force true; set ssl:verify-certificate no; connect {ftps_server}; login {ftps_user};{ftps_password}; mput {local_folder_path}; exit"'
    ]

    # Execute lftp commands
    for command in commands:
        subprocess.run(command, shell=True)

def main():
    local_folder_path = 'files/*'
    ftps_server = '172.21.0.2'
    ftps_user = 'username'
    ftps_password = 'mypass'

    send_files_to_ftps(local_folder_path, ftps_server, ftps_user, ftps_password)

if __name__ == "__main__":
    main()

