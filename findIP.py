import subprocess
import xml.etree.ElementTree as ET#findMacAdress
from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
import PySimpleGUI as sg
ip1, ip2, ip3, ip4 = "192.168.0.28", "192.168.0.25", "192.168.0.24", "192.168.0.34"
previousCam = "s7"
newCam = "xz"
#ip1, ip2, ip3, ip4 = "192.168.11.101", "192.168.11.102", "192.168.11.103", "192.168.11.104"
def getIP():
	global ip1, ip2, ip3, ip4
	#file1 = open("ip.txt")
	with open("ip.txt") as file1: 
		ip1 = file1.readline().rstrip('\n')
		ip2 = file1.readline().rstrip('\n')
		ip3 = file1.readline().rstrip('\n')
		ip4 = file1.readline().rstrip('\n')
		print(ip1, ip2, ip3, ip4)
	#file1.close()


def brand_to_ip(argument): 
	global ip1, ip2, ip3, ip4
	switcher = { 

		"s7": ip1, 
		"xz": ip2, 
		"wf": ip3, 
		"lg": ip4,
	} 
	return switcher.get(argument, "nothing")
	  

def swichCamera(previousCam, newCam):
	#first launch the new cam
	subprocess.call("adb -s " + brand_to_ip(newCam) + ":5555 shell \"input keyevent 25 && exit\"",shell=True) #&& sleep 0.1
	subprocess.call("adb -s  " + brand_to_ip(previousCam) + ":5555 shell \"input keyevent 25 && exit\"",shell=True)
	#density = subprocess.call("adb -s  " + brand_to_ip(newCam) + ":5555 shell \"wm size\"",shell=True)
	#print(density[-8:])
#subprocess.call("input keyevent 25",shell=True)
#adb tcpip 5555 adb connect 192.168.0.24 adb shell input keyevent 25


def graphInterface():
	global previousCam, newCam
	sg.theme('DarkAmber')   # Add a touch of color
	# All the stuff inside your window.
	layout = [  [sg.Button('s7', font=('courier', 100)),sg.Button('xz', font=('courier', 100))],
				[sg.Button('wf', font=('courier', 100)),sg.Button('lg', font=('courier', 100))],
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

if __name__ == '__main__':
	getIP()
	graphInterface()


