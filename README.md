# REQUIREMENTS
Before using the PCAP parser project, you need some **_requirements_**:

- Install Kali Linux OS [https://www.kali.org/get-kali/](https://www.kali.org/get-kali/#kali-platforms).

- Make sure that all is update with the command: 
```
sudo apt update && sudo apt upgrade
```
> Especially Python language

- To be sure that **_Python has the best version_**, you can see its version with `which python3` in the **_terminal_**.

- Install docker with the command:
```
sudo apt install -y docker.io
sudo systemctl enable docker --now
```
> Now you can get started with using docker, with sudo.

- If you want to add yourself to the docker group to use docker without sudo, an additional step is needed:
```
sudo usermod -aG docker $USER
```
> The final thing is to **_logout and in again_**

# How to use PCAP Parser project
Use the file `docker-compose.yml` from `FTP` folder with the command in the **_terminal_**:
```
sudo docker-compose build up -d
```
> It will create the container for FTP server.

To enable our FTP server, use the command:
```
sudo docker start ftp-server
```



