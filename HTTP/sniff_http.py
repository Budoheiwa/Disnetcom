#!/usr/bin/python3
import subprocess
from scapy.all import *

def sniff_packets(interface, output_file):
    command = f"sudo tcpdump -i {interface} -w {output}"
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def parse_line(line):
    try:
        if b':' in line:
            field, value = line.split(b':', 1)
            return field.strip().decode("utf-8").title(), value.strip().decode("utf-8")
        else:
            return None, None
    except UnicodeDecodeError:
        return None, None
        
def parse_pcap(file_path):
    raw_data_list = []
    try:
        packets = rdpcap(file_path)
        for packet in packets:
            if Raw in packet:
                field, value = parse_line(packet[Raw].load)
                if field is not None:
                    raw_data_list.append(f'{field}: {value}')
    except Exception as e:
        print(f"Error parsing pcap file: {e}")
    return raw_data_list

def write_data(file_path, data_list):
    try:
        with open(file_path, "w") as file:
            for data in data_list:
                file.write(data + '\n')
    except Exception as e:
        print(f"Error writing data to file: {e}")

def filter_content(input_file, output_file, keywords):
    try:
        lines_written = set()
        words_written = set()
        with open(input_file, 'r') as file_in:
            with open(output_file, 'w') as file_out:
                for line in file_in:
                    if ("<" not in line) and any(keyword in line for keyword in keywords):
                        words = line.strip().split()
                        first_word = words[0] if words else None
                        if first_word not in words_written:
                            if line not in lines_written:
                                file_out.write(line)
                                lines_written.add(line)
                            words_written.add(first_word)
        print("Filtered content written to", output_file)
    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    interface = "lo"
    output = "http_capturestocker.pcap"
    not_filtered_output_file = "Not_filtered_output.txt"
    filtered_output_file = "Filtered_output.txt"

    print("#" * 10 + " Code 1: Sniffing Packets " + "#" * 10)
    sniff_packets(interface, output)
    print("#" * 50 + "\n")

    print("#" * 10 + " Code 2: Parsing Packets " + "#" * 10)
    packets_data = parse_pcap(output)
    print("#" * 50 + "\n")

    print("#" * 10 + " Code 3: Writing not Filtered Data " + "#" * 10)
    write_data(not_filtered_output_file, packets_data)
    print("#" * 50 + "\n")
    
    print("#" * 10 + " Code 4: Writing Filtered Data " + "#" * 10)
    keywords = ["username", "password", "Host", "Date"]
    filter_content(not_filtered_output_file, filtered_output_file, keywords)
    print("#" * 50 + "\n")
