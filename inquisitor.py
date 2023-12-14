#!/usr/bin/python3
import argparse

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
	print(args)

if __name__ == '__main__':
	main()
