#!/usr/bin/python3
from scapy.all import *

interfaces = ["eth0", "lo", "br-2c6ea089bf18"]
capture = sniff(iface=interfaces, filter="port 21 or (portrange 21100-21110)", count=90)
wrpcap("capturestocker.pcap", capture)

def parse_pcap(capture_file):
    packets = rdpcap(capture_file)
    raw_data_list = []

    for packet in packets:
        print(packet.summary())
        if Raw in packet:
            raw_data = packet[Raw].load
            print(f"Raw Data: {raw_data}")
            format_raw = f"Raw Data: {raw_data}"+"\n"
            raw_data_list.append(format_raw)

    return raw_data_list

def exifiltr_data(raw_data_list):
    with open("raw_data.txt", "w") as w:
        for packet in raw_data_list:
            w.write(str(packet))

def read_data():
    with open("raw_data.txt", "r") as r:
        read_data_lines = r.readlines()

    return read_data_lines

if __name__ == "__main__":
    packets = parse_pcap("capturestocker.pcap")
    exifiltr_data(packets)  
    read_data()
    print("\r"+"#" * 50 + "\n")
    
