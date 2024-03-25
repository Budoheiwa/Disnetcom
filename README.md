# REQUIREMENTS
Before using the PCAP parser project, you need some **requirements**:

- Install [Kali Linux OS](https://www.kali.org/get-kali/#kali-platforms).

- Or WSL from Windows [](url)

- Make sure that all is update with the command: 
```
sudo apt update && sudo apt upgrade && sudo apt full-upgrade
```
> Especially Python language

- To be sure that **Python has the best version**, you can see its version with `which python3` in the **terminal**.

- Install docker with the command:
```
sudo apt install -y docker.io
sudo systemctl enable docker --now
```
- Or get some documentations on [Docker](https://www.docker.com/)

> Now you can get started using docker, with sudo.

- If you want to add yourself to the docker group to use docker without sudo, an additional step is needed:
```
sudo usermod -aG docker $USER
```
> The final thing is to **logout and in again**

# How to use PCAP Parser project
## Sniffing FTP packets
Use the file `docker-compose.yml` from `FTP` folder with the command in the **terminal**:
```
sudo docker-compose build up -d
```
> Remember that you can customize its settings with the port range, the username and the password.

![FTP server docker-compose.yml](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/5635d705-68c1-4eb7-91fd-b7a59775a7fd)

> It will create a container for the FTP server.

To enable our FTP server, use the command:
```
sudo docker start ftp-server
```
From `sniff_parse_FTP.py` in `FTP` folder, you need to enter which network interfaces, which filter expressions you want to use; and set a timer for how long you want sniff packets in the network:

![sniff_parse_FTP.py](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/f7a4d7e6-554b-4c86-915b-981a3153612f)

To know which **network interfaces** you need to intercept packets, use these commands in shell:
```
ip a
ifconfig
```
> Generally, use the **lo**, **eth0**, and the network interface created for FTP server by docker.

Then, use the file `ftp_auto.py` in the **current shell** to enable the FTP server and start sniffing FTP packets:
```
sudo python3 ftp_auto.py
```
In **another shell**, use the file `ftp_upload.py` from `FTP` folder:
```
sudo python3 ftp_upload
```
> You need to enter the correct inputs such as the IP address, the username, and the password of FTP server.

![ftp_upload.py](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/8f0822a4-8c3d-482d-89f1-dff413ae8876)

If you want to see the current IP address of your FTP server, simply use the command below: 
```
sudo docker exec ftp-server hostname -I
``` 

After executing those 2 python scripts, you should have in your current folder the `ftp_rawdata.txt` and `ftp_capturestocker.pcap` files. 

## Sniffing FTPS packets

