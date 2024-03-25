#!/usr/bin/python3
from scapy.all import *

def parse_pcap(capture):
	packets = rdpcap(capture) # Loading and reading the pcap file
	
	for packet in packets:
		print(packet.summary()) # Show the summary for each packet

capture = "capturestocker.pcap" # Select your pcap file
parse_pcap(capture)
