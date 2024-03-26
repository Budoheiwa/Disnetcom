#!/usr/bin/python3
from scapy.all import *
import subprocess
import time

def intercept_packets(interface, filter_expression, timeout):
    start_time = time.time()
    packets = []
    first_packet_received = False
    
    print(f"Intercepting packets on interface {interface} for {timeout} seconds...")
    while time.time() - start_time < timeout:
        timeout_func = timeout - (time.time() - start_time)
        captured_packets = sniff(iface=interface, filter=filter_expression, timeout=timeout_func)
        if captured_packets:
            packets += captured_packets
            if not captured_packets:
                print("First packet intercepted. Starting timer...")
                start_time = time.time()  # Reset the start time
                first_packet_received = False
        else:
            break
    return packets

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
    interface = ["eth0", "lo", "br-508d6f4743bc"]   # Select your network interfaces 
    filter_expression = "port 21 or (portrange 30000-30010)" # Select your filter expression, ports, etc...
    timeout = 20  # Set a timer in Seconds

    captured_packets = intercept_packets(interface, filter_expression, timeout)
    if captured_packets:
        wrpcap("ftps_capturestocker.pcap", captured_packets) # pcap file is stored
        parse_pcap("ftps_capturestocker.pcap") # Load and read the pcap file
        print('\n' + "--End of the parsing--" + '\n')
        print("--Beginning of the pcap file filtering--" + '\n')
        pcap_filter_packets("ftps_capturestocker.pcap", "ftps_filtered_capturestocker.pcap") # The second pcap output is filtered

