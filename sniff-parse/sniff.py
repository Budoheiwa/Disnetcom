#!/usr/bin/python3
from scapy.all import *


interfaces = ["eth0", "lo", "br-2c6ea089bf18"]
capture = sniff (iface = interfaces, filter = "port 21 or portrange(21100-21110)", count = 150)
wrpcap("capturestocker.pcap", capture)
