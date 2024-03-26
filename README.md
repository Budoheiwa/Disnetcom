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
sudo python3 ftp_upload.py
```
> You need to enter the correct inputs such as the IP address, the username, and the password of FTP server.

![ftp_upload.py](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/8f0822a4-8c3d-482d-89f1-dff413ae8876)

If you want to see the current IP address of your FTP server, simply use the command below: 
```
sudo docker exec ftp-server hostname -I
``` 

After executing those 2 python scripts, you should have in your current folder the `ftp_rawdata.txt` and `ftp_capturestocker.pcap` files. 

## Sniffing FTPS packets
Use `docker-compose.yml` file from `FTPS` folder with the command in the **terminal**:
```
sudo docker-compose build up -d
```
> Remember that you can customize its settings with the port range, the username and the password.
> Also remember to create the private key and the certificate in kali folder /etc/ssl/private and move them to FTPS server folder ftps/ssl/ based on [Github - stilliard](https://github.com/stilliard/docker-pure-ftpd#tls).

![FTPS server docker-compose.yml](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/de706cb2-cb74-456e-8a3a-6618f7f1dada)

> It will create a container for the FTPS server.

To enable our FTPS server, use the command:
```
sudo docker start ftps-server
```
From `sniff_parse_FTPS.py` in `FTPS` folder, you need to enter which network interfaces, which filter expressions you want to use; and set a timer for how long you want sniff packets in the network:
![sniff_parse_FTPS.py](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/80607772-1d89-42a6-9458-91f9d7d6c4c2)
To know which **network interfaces** you need to intercept packets, use these commands in shell:
```
ip a
ifconfig
```
> Generally, use the **lo**, **eth0**, and the network interface created for FTPS server by docker.

Then, use the file `ftps_auto.py` in the **current shell** to enable the FTPS server and start sniffing FTPS packets:
```
sudo python3 ftps_auto.py
```
In **another shell**, use the file `ftps_choice.py` from `FTPS` folder:
```
sudo python3 ftps_choice.py
```
> You have 2 choices. One will be to upload files with TLS protocol by using the script `ftps_upload.py`. The second one will be to retrieve TLS keys while uploading files with TLS protocol, in order to decrypt the packets with the script `retrieve_tlskeys.py`. 

### With `ftps_upload.py`
> Be sure to install first [lftp](https://doc.ubuntu-fr.org/lftp) package which is an FTP client. 
> You need to enter the correct inputs such as the IP address, the username, and the password of FTPS server.

![ftps_upload.py](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/ac4a4830-3abd-4f19-a032-38ee01176457)

If you want to see the current IP address of your FTPS server, simply use the command below: 
```
sudo docker exec ftps-server hostname -I
``` 
After executing those 2 python scripts, you should have in your current folder the `ftps_capturestocker.pcap` and `ftps_filtered_capturestocker.pcap` files. 

### With `retrieve_tlskeys.py`
> You need to download the repo from [fxb-cocacoding](https://github.com/fxb-cocacoding/ssl_decrypt/blob/master/sslkeylog.c)
> Compile the `sslkeylog.c` script to create a library called `libsslkeylog.so`
> And move it to `FTPS` folder

![retrieve_tlskeys.py](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/bedccff8-5154-45c6-951e-8b6b5c7438e1)

