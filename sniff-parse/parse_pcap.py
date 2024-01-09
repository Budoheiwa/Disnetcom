#!/usr/bin/python3
from scapy.all import *

def parse_pcap(capture):
	packets = rdpcap(capture)
	
	for packet in packets:
		print(packet.summary()) #show

capture = "capturestocker.pcap"
parse_pcap(capture)
