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
> If you choose the second option. The script will also retrieve the public certificate `certificate.pem` with `openssl`.

![certificate.pem in ftps_choice.py](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/39f13ca6-aec0-4beb-9359-f9fd26fce7f0)

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
> You need to download the repo from [fxb-cocacoding](https://github.com/fxb-cocacoding/ssl_decrypt/blob/master/sslkeylog.c).
> Compile the `sslkeylog.c` script to create a library called `libsslkeylog.so`.
> And move it to `FTPS` folder.

![retrieve_tlskeys.py](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/bedccff8-5154-45c6-951e-8b6b5c7438e1)

After executing those 2 python scripts, you should have in your current folder the `ftps_capturestocker.pcap`, `ftps_filtered_capturestocker.pcap`, `tlskeys.txt` and `certificate.pem` files. 
> Open **Wireshark** with:
```
wireshark ftps_filtered_capturestocker.pcap
```
> Go to **Edit > Preferences > Protocols (list them all) > TLS > (Pre)-Master-Secret log filename**. Import the `tlskeys.txt` file and click on **ok** to save it.
> Now TLS/FTP packets should be decrypted !

## Sniffing HTTP packets
Run the `sniff_http.py` script in `HTTP` folder, from a **terminal** with the command:
```
sudo python3 sniff_http.py
```
![sniff_http.py](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/e35fb489-8a3d-4c35-8123-b0574bbc3fc2)
> Don't forget to modify the network interfaces and output files according to your preferences.

In another shell, run the script `Server.js` to deploy the webserver that includes `index.html`.
> You need to install first the `node` package before running the JS script.

```
sudo node Server.js
```
> When the webserver is running, it will provide you an URL link to connect it such as `http:/localhost:3000/`. Click it and it will redirect you in a web page.
> ![Server.js](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/0c0bdf7e-ef50-43f0-b428-232c38c1d391)
> ![Web page for credentials](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/4a5bc574-cbf8-4cf7-b720-eb00052bf982)
> 
> Enter some credentials in **Username** and **Password**, then click on **Log in**

After executings those commands, you need to quit the `sniff_http.py` program by pressing `Ctrl+C`.
In the end, you will have 3 output files, `http_capturestocker.pcap`, `Not_filtered_output.txt`, and `Filtered_output.txt`. 

## Sniffing TELNET packets
> First, check the text file `User guide - Telnet.txt`, it tells you which requirements you need to have before executing the python script `sniff_telnet.py`.

Once done, run the program `sniff_telnet.py` with this command:
```
sudo python3 sniff_telnet.py
```
> Don't forget to check the IP addresses and network interfaces on both machines with:
> ```
> ip a
> ifconfig
> ```
> And add them as parameters

![sniff_telnet.py](https://github.com/Budoheiwa/pcap-parser-secretnetworkcom/assets/156065416/2656d5eb-6862-4029-a876-ea2b054f0f4c)

# FTP and FTPS automatization
We build an all-in-one python script in the main folder called `all_auto.py` to automate all scripts of our project. 
> Although we were successful with the FTP and FTPS protocols for restarting the servers and sniffing, we encountered difficulties when attempting to upload files with the script `uploading_files.py`.
