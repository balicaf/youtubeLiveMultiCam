# youtubeLiveMultiCam
Simplest setup to do multicam on youtube Live with Android
What do you need:
-larix broadcast and usb debugging enabled on every phone
-one computer with adb shell

 To enable usb debugging, 10 tap on parameter about phone baseband, then developper option enable usb debugging.
 
(ps for multiple phone, type "adb devices" then copy deviceId, then add "-e deviceId" after "adb" e.g. "adb -s 192.168.0.16:5555 shell"or if physically connected: "adb -d shell")
adb -d tcpip 5555                         #enable adb through wifi
#adb -d kill-server                       #if it's not working
adb -d shell ip -f inet addr show wlan0   #get Ip Adress
adb connect 192.168.0.24                  #use the ip you've got from last command line
adb shell -s 192.168.0.24                 #open adb shell
input keyevent 25                         #virtually press volume down button

The last line activates the volume down button. So in order to switch camera, you first activate "input keyevent 25"(start recording) on the second camera, you have two stream to youtube with the same keys. youtube will continue to show the oldest one. Then on the first(oldest) camera you "input keyevent 25" (stop recording)

instructions described in this video
https://youtu.be/HVNFL1jNtog?t=74
application for streaming to youtube
https://play.google.com/store/apps/details?id=com.wmspanel.larix_broadcaster&hl=fr
youtube live
https://studio.youtube.com/channel/UClKvyJpGlPZkGdNWeIn8ZyQ/livestreaming/manage

#ToDo: create a configurable interface to automatically start and stop recording from GUI input
