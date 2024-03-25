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

![image](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/d4ad2c89-ab72-441e-8520-d04c81d81333)

> It will create a container for the FTP server.

To enable our FTP server, use the command:
```
sudo docker start ftp-server
```
From `sniff_parse_FTP.py` in `FTP` folder, you need to enter which network interfaces, which filter expressions you want to use; and set a timer for how long you want sniff packets in the network:

![image](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/c4d3df6c-ada2-494c-9547-a6d101cdd45e)

To know which **network interfaces** you need to intercept packets, use these commands in shell:
```
ip a
ifconfig
```
> Generally, use the **lo**, **eth0**, and the network interface created for FTP server by docker.

Then, use the file `ftp_automatisation.py` in the **current shell** to enable the FTP server and to start sniffing FTP packets:
```
sudo python3 ftp_automatisation.py
```

In **another shell**, use the file `ftp_upload.py` from `FTP` folder:
> You need to enter the correct inputs such as the IP address, the username, and the password of FTP server.

If you want to see the current IP address of your FTP server, simply use the command `sudo docker exec ftp-server hostname -I`. 

![image](https://github.com/Budoheiwa/PCAP-parser/assets/156065416/8fd525bf-c16b-49bd-bef4-ad2409d55228)

```
sudo python3 ftp_upload
```
After executing those 2 python scripts, you should have in your current folder the `raw_data.txt` and `capturestocker.pcap` files. 



