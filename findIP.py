import subprocess
import xml.etree.ElementTree as ET#findMacAdress
from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
import PySimpleGUI as sg
ip1, ip2, ip3, ip4 = "192.168.0.34", "192.168.0.24", "192.168.0.16", "192.168.0.28"

def brand_to_ip(argument): 
	global ip1, ip2, ip3, ip4
	switcher = { 

		"s7": ip1, 
		"xz": ip2, 
		"wf": ip3, 
		"lg": ip4,
	} 
	return switcher.get(argument, "nothing")
	  
previousCam = "s7"
newCam = "xz"
def swichCamera(previousCam, newCam):
	#first launch the new cam
	subprocess.call("adb -s " + brand_to_ip(newCam) + ":5555 shell \"input keyevent 25 && sleep 1 && exit\"",shell=True)
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
	if (newCam != event):
		previousCam = newCam
		newCam = event
		swichCamera(previousCam, newCam)

window.close()