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
From `sniff_parse.py`, you need to enter which network interfaces, which ports you want to use; and how many packets you want to use for sniffing packets in the network:

![Capture d'écran 2024-01-15 131344](https://github.com/Budoheiwa/PCAP-parser/assets/156065416/3d0decc8-27ef-4db3-9c2b-f97c75437019)

To know which **_network interfaces_** you need to intercept packets, use the command in shell:
```
ip a
ifconfig
```
> Generally, use the **_lo_**, **_eth1_**, and the network interface created for FTP server by docker.

Then, use the file `ftp_automatisation.py` in the **_current shell_** to enable the FTP server and to start sniffing FTP packets:
```
sudo python3 ftp_automatisation.py
```

In **_another shell_**, use the file `ftp_upload.py` from `FTP` folder:
> You need to enter the correct inputs such as the IP address, the username, and the password of FTP server


```
sudo python3 ftp_upload
```

After executing those 2 python scripts, you should have in your current folder the `raw_data.txt` and `capturestocker.pcap` files. 



