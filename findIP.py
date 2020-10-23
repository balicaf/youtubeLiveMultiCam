import subprocess
import xml.etree.ElementTree as ET#findMacAdress
from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
import re
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
import PySimpleGUI as sg
import time
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
	time.sleep(1)
	subprocess.call("adb -s  " + brand_to_ip(previousCam) + ":5555 shell \"input keyevent 25 && exit\"",shell=True)


def closeCamera(newCam):
	#first launch the new cam
	subprocess.call("adb -s " + brand_to_ip(newCam) + ":5555 shell \"input keyevent 25 && exit\"",shell=True) #&& sleep 0.1
def switchS7():
	subprocess.call("adb -s " + brand_to_ip("s7") + ":5555 shell \"input tap 150 720 && exit\"",shell=True) #&& sleep 0.1

def readState(newCam):
	proc = subprocess.Popen("adb -s "+ brand_to_ip(newCam) + ":5555 shell \"dumpsys activity top | grep androidx.appcompat.widget.AppCompatTextView\"", shell=True, stdout=subprocess.PIPE)
	output=proc.communicate()[0]
	tmp = output.decode("utf-8")
	regexTmp = tmp.splitlines()[3]#G or V
	return(re.search('\w*(?=\.ED)', regexTmp).group(0))
	#for line in tmp.splitlines():
	#	print(re.search('\w*(?=\.ED)', line).group(0))
	#out2 = re.search('\w*(?=\.)', tmp)
	#print(out2.group(1),out2.group(2),out2.group(3))

	#regex = re.compile('\w*(?=\.ED)')
	#for line in tmp:
	#	print(line)
	#	out2 = regex.search(line)
	#	print(out2.group(0))
	#	result = regex.search(line)

def graphInterface():
	global previousCam, newCam
	sg.theme('DarkAmber')   # Add a touch of color
	# All the stuff inside your window.
	layout = [  [sg.Button('s7', font=('courier', 100)),sg.Button('xz', font=('courier', 100)), sg.Button('s71', font=('courier', 50)),sg.Button('xz1', font=('courier', 50))],
				[sg.Output(size=(50,10), key='-OUTPUT-')],
				[sg.Button('wf', font=('courier', 100)),sg.Button('lg', font=('courier', 100)), sg.Button('wf1', font=('courier', 50)),sg.Button('lg1', font=('courier', 50))],
				[sg.Button('switchS7', font=('courier', 100))],
				[sg.Button('Ok'), sg.Button('Cancel')] ]

	# Create the Window
	window = sg.Window('Window Title', layout)

	# Event Loop to process "events" and get the "values" of the inputs
	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
			break
		print('You entered ', event)
		if event == 'switchS7':
			switchS7()
		if (newCam != event):
			#refresh indicative values
			#window.FindElement('_output_').Update('')
			
			#print("xz "+readState("xz"))
			#print("wf "+readState("wf"))
			
			if (len(event)==3):
				newCam = event[0:2]
				closeCamera(newCam)
				print("lg "+readState("lg"))
				print("S7 "+readState("s7"))
			else:
				previousCam = newCam
				newCam = event
				swichCamera(previousCam, newCam)
				print("lg "+readState("lg"))
				print("S7 "+readState("s7"))

	window.close()

if __name__ == '__main__':
	getIP()
	graphInterface()


