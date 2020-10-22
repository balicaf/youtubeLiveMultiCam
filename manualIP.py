import subprocess
import xml.etree.ElementTree as ET#findMacAdress
from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
import re

def write2File():
	file1 = open("ip.txt","a") 
	file1.write(out2.group(1) + "\n")
	file1.close()
#ipId = subprocess.call(,shell=True) #&& sleep 0.1
#print(ipId[3:len(ipId)-5])

cmd = """adb -d shell ip -f inet addr show wlan0 """
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
output=proc.communicate()[0]
tmp = output.decode("utf-8")
out2 = re.search("inet\ (.*)\/", tmp)
print(out2.group(1))
write2File()
subprocess.call("adb -d tcpip 5555",shell=True)
subprocess.call("adb -d connect " + out2.group(1),shell=True)

