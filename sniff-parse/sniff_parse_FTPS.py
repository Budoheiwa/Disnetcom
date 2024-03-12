#!/usr/bin/python3
from scapy.all import *
import subprocess

interfaces = ["eth0", "lo", "br-fb9de0832914"]
capture = sniff(iface=interfaces, filter="port 21 or (portrange 30000-30009)", count=170)
wrpcap("capturestocker.pcap", capture)

def parse_pcap(capture_file):
    packets = rdpcap(capture_file)
    for packet in packets:
        print(packet.summary())

def pcap_filter_packets(capture_file, filtered_pcap_file):
    # Check if the input capture file exists
    if not os.path.exists(capture_file):
        print(f"Error: Capture file '{capture_file}' not found.")
        return
    
    # Define the tshark command to filter FTP and TLS packets
    tshark_command = [
        "tshark",
        "-r", capture_file,  # Input pcap file
        "-Y", "(ftp || tls)",  # Filter for FTP or TLS packets
        "-V",  # Include packet details (including payload)
        "-w", filtered_pcap_file  # Output pcap file
    ]

    # Execute the tshark command
    try:
        subprocess.run(tshark_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

if __name__ == "__main__":
    capture_file = "capturestocker.pcap"
    filtered_pcap_file = "filtered_capturestocker.pcap"

    parse_pcap(capture_file)
    print('\n' + "--End of the parsing--" + '\n')
    print("--Beginning of the pcap file filtering--" + '\n')
    pcap_filter_packets(capture_file, filtered_pcap_file)
    print("#" * 50 + "\n")
