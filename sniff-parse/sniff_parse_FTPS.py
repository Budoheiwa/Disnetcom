#!/usr/bin/python3
from scapy.all import *

interfaces = ["eth0", "lo", "br-fb9de0832914"]
capture = sniff(iface=interfaces, filter="port 21 or (portrange 30000-30009)", count=200)
wrpcap("capturestocker.pcap", capture)

def parse_pcap(capture_file):
    packets = rdpcap(capture_file)
    raw_data_list = []

    for packet in packets:
        if Raw in packet:
            raw_data = packet[Raw].load

            # Check for TLS handshake messages
            if raw_data.startswith(b'\x16') and len(raw_data) > 5:
                # Extract the TLS version
                tls_version = raw_data[1:3]
                # Extract the handshake message type
                handshake_type = raw_data[5]

                # Client Hello message
                if handshake_type == 1:
                    raw_data_list.append('TLS Client Hello:')
                # Server Hello message
                elif handshake_type == 2:
                    raw_data_list.append('TLS Server Hello:')
                # Other handshake messages
                else:
                    raw_data_list.append('TLS Handshake Message:')

                raw_data_list.append('--Start--')
                raw_data_list.append(raw_data)
                raw_data_list.append('--End--')
                raw_data_list.append('\n')
             
            elif raw_data.startswith(b'\x17\x03'):
                raw_data_list.append('TLS Application Data:')
                raw_data_list.append('--Start--')
                raw_data_list.append(raw_data)
                raw_data_list.append('--End--')
                raw_data_list.append('\n')
                
    print("RAW DATA LIST: ", raw_data_list)

    return raw_data_list


def exifiltr_data(raw_data_list):
    with open("FTPS/FTPS_rawdata.txt", "w") as w:  # Open the file in text mode for writing
        for data in raw_data_list:
            if isinstance(data, bytes):
                # If data is in bytes format, convert it to a string representation
                formatted_data = repr(data)
            else:
                # If data is already a string, keep it as is
                formatted_data = data

            # Write the formatted data to the file
            w.write(formatted_data + '\n')
 
def read_data():
    with open("FTPS/FTPS_rawdata.txt", "r") as r:  
        read_data_content = r.readlines()  

    return read_data_content

if __name__ == "__main__":
    packets = parse_pcap("capturestocker.pcap")
    exifiltr_data(packets)
    read_data()  
    print("\r" + "#" * 50 + "\n")
