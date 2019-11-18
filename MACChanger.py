#!/usr/bin/env python

import subprocess
import optparse


def mac_change(interface, new_mac):
	print("[+] Changing MAC Address for " + interface +" to "+new_mac)
	subprocess.call("ifconfig "+ interface+ " down", shell=True)
	subprocess.call("ifconfig "+ interface+ " hw ether 00:11:22:33:44:66", shell=True)
	subprocess.call("ifconfig "+ interface+ " up", shell=True)

parser = optparse.OptionParser()
parser.add_option("-i" , "--interface", dest = "interface", help="Add the interface of changing MAC")
parser.add_option("-m" , "--mac", dest = "new_mac", help="Add the mac of changing MAC")

(options, arguments) = parser.parse_args()

interface =options.interface
new_mac = options.new_mac

mac_change(options.interface,options.new_mac) 	