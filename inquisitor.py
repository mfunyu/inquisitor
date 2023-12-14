#!/usr/bin/python3
import argparse

def error_exit(msg):
	print(f"Error: {msg}")
	exit(1)

def is_valid_ip(ip):
	try:
		nums = ip.split('.')
		if len(nums) != 4:
			return False
		for n in nums:
			if int(n) < 0 or 255 < int(n):
				return False
		return True
	except:
		return False

def is_valid_mac(mac):
	return True

def validate_args(args):
	if not is_valid_ip(args.ip_src):
		error_exit("Invalid IP-src")
	if not is_valid_mac(args.mac_src):
		error_exit("Invalid MAC-src")
	if not is_valid_ip(args.ip_target):
		error_exit("Invalid IP-target")
	if not is_valid_mac(args.mac_target):
		error_exit("Invalid MAC-target")

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
	print(args)

if __name__ == '__main__':
	main()