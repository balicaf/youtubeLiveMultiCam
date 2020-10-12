import subprocess
import xml.etree.ElementTree as ET#findMacAdress
from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
ip1, ip2, ip3, ip4 = "192.168.0.34", "192.168.0.24", "192.168.0.16", "192.168.0.28"
mac1='B0:72:BF:4E:02:7E' #s7
mac2='84:C7:EA:97:0F:9E'#xz
mac3='F6:DO:13:19:43:03'#wileyfox
mac4='A0:39:F7:53:95:94'#lg

def mac_to_ip(argument): 
	global ip1, ip2, ip3, ip4
	switcher = { 

		mac1: ip1, 
		mac2: ip2, 
		mac3: ip3, 
		mac4: ip4,
	} 
	return switcher.get(argument, "nothing")
  
	# get() method of dictionary data type returns  
	# value of passed argument if it is present  
	# in dictionary otherwise second argument will 
	# be assigned as default value of passed argument 
	return switcher.get(argument, "nothing") 
def scan_for_hosts(ip_range):
	"""Scan the given IP address range using Nmap and return the result
	in XML format.
	"""
	nmap_args = ['nmap', '-n', '-sP', '-oX', '-', ip_range]
	#nmap_args = ['nmap', '-sn', ip_range]
	return subprocess.check_output(nmap_args)


def find_ip_address_for_mac_address(xml, mac_address):
	"""Parse Nmap's XML output, find the host element with the given
	MAC address, and return that host's IP address (or `None` if no
	match was found).
	"""
	host_elems = ET.fromstring(xml).iter('host')
	print(host_elems)
	host_elem = find_host_with_mac_address(host_elems, mac_address)
	if host_elem is not None:
		return find_ip_address(host_elem)


def find_host_with_mac_address(host_elems, mac_address):
	"""Return the first host element that contains the MAC address."""
	for host_elem in host_elems:
		if host_has_mac_address(host_elem, mac_address):
			return host_elem


def host_has_mac_address(host_elem, wanted_mac_address):
	"""Return true if the host has the given MAC address."""
	found_mac_address = find_mac_address(host_elem)
	return (
		found_mac_address is not None and
		found_mac_address.lower() == wanted_mac_address.lower()
	)


def find_mac_address(host_elem):
	"""Return the host's MAC address."""
	return find_address_of_type(host_elem, 'mac')


def find_ip_address(host_elem):
	"""Return the host's IP address."""
	return find_address_of_type(host_elem, 'ipv4')


def find_address_of_type(host_elem, type_):
	"""Return the host's address of the given type, or `None` if there
	is no address element of that type.
	"""
	address_elem = host_elem.find('./address[@addrtype="{}"]'.format(type_))
	if address_elem is not None:
		return address_elem.get('addr')

#https://homework.nwsnet.de/releases/9577/
def find_IP_address_from_MAC(mac_address):
	global ip1, ip2, ip3, ip4
	return mac_to_ip(mac_address)#shortcut!!!!
	#mac_address = mac_address #'d0:73:d5:31:ea:4e'
	ip_range = '192.168.0.10-45'

	xml = scan_for_hosts(ip_range)
	ip_address = find_ip_address_for_mac_address(xml, mac_address)

	if ip_address:
		print('Found IP address {} for MAC address {} in IP address range {}.'
			  .format(ip_address, mac_address, ip_range))
		return ip_address
	else:
		print('No IP address found for MAC address {} in IP address range {}.'
			  .format(mac_address, ip_range))
		return mac_to_ip(mac_address)
		

#192.168.0.34
#192.168.0.28			  

s7 = find_IP_address_from_MAC(mac1)
xz = find_IP_address_from_MAC(mac2)
wf = find_IP_address_from_MAC(mac3)
lg = find_IP_address_from_MAC(mac4)
print(s7)
#device1 = AdbDeviceTcp(s7, 5555, default_transport_timeout_s=9.)
#device1.connect( auth_timeout_s=0.1)

#outside the loop
#subprocess.call("adb -s 192.168.0.34:5555 kill-server",shell=True)

#inside the loop
#subprocess.call("adb connect 192.168.0.34",shell=True)
subprocess.call("adb -s 192.168.0.24:5555 shell \"input keyevent 25 && exit\"",shell=True)
subprocess.call("adb -s 192.168.0.28:5555 shell \"input keyevent 25 && exit\"",shell=True)
#subprocess.call("input keyevent 25",shell=True)
#adb tcpip 5555 adb connect 192.168.0.24 adb shell input keyevent 25
