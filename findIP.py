import subprocess
import xml.etree.ElementTree as ET#findMacAdress
from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
import PySimpleGUI as sg
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
def brand_to_ip(argument): 
	global ip1, ip2, ip3, ip4
	switcher = { 

		"s7": ip1, 
		"xz": ip2, 
		"wf": ip3, 
		"lg": ip4,
	} 
	return switcher.get(argument, "nothing")

 
def find_IP_address_from_MAC(mac_address):
	global ip1, ip2, ip3, ip4
	return mac_to_ip(mac_address)#shortcut!!!!		  

s7 = find_IP_address_from_MAC(mac1)
xz = find_IP_address_from_MAC(mac2)
wf = find_IP_address_from_MAC(mac3)
lg = find_IP_address_from_MAC(mac4)
previousCam = "s7"
newCam = "xz"
def swichCamera(previousCam, newCam):
	#first launch the new cam
	subprocess.call("adb -s " + brand_to_ip(newCam) + ":5555 shell \"input keyevent 25 && sleep 5 && exit\"",shell=True)
	subprocess.call("adb -s  " + brand_to_ip(previousCam) + ":5555 shell \"input keyevent 25 && exit\"",shell=True)
#subprocess.call("input keyevent 25",shell=True)
#adb tcpip 5555 adb connect 192.168.0.24 adb shell input keyevent 25



sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Button('s7'),sg.Button('xz')],
            [sg.Button('wf'),sg.Button('lg')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', event)
    previousCam = newCam
    newCam = event
    swichCamera(previousCam, newCam)

window.close()