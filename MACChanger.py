#!/usr/bin/env python
#mushrafmustafa@gmail.com

import subprocess
import optparse


def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i" , "--interface", dest = "interface", help="Add the interface of changing MAC")
	parser.add_option("-m" , "--mac", dest = "new_mac", help="Add the mac of changing MAC")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Kindly specify the Interface, or use --help  for more info")
	elif not options.new_mac:
		parser.error("[-] Kindly specify the Mac Address, or use --help  for more info")
	return options
def mac_change(interface, new_mac):
	print("[+] Changing MAC Address for " + interface +" to "+new_mac)
	subprocess.call("ifconfig "+ interface+ " down", shell=True)
	subprocess.call("ifconfig "+ interface+ " hw ether "+new_mac, shell=True)
	subprocess.call("ifconfig "+ interface+ " up", shell=True)
 
options= get_arguments()
mac_change(options.interface,options.new_mac) 	
