# we need a line to start FLDIGI programaticaly
import time
import math
import os# for shut down

math.pi
try:
    import RPi.GPIO as GPIO
except RuntimeError:
        print("fubar gpio")
GPIO.setmode(GPIO.BOARD)
from xmlrpclib import ServerProxy

from tentacle_pi.BMP180 import BMP180# driber for temp/pressure

proxy = ServerProxy("http://localhost:7362/")# setup for fldigi

bmp = BMP180(0x77, "/dev/i2c-1")# yea I2c
proxy.main.tx()# enabke TX on HAMY

proxy.text.add_tx("WX online with BMP180\n  ")#\n is a line feed
proxy.text.clear_rx()# this and the next line is for keeping the program in step with fldigi
while proxy.text.get_rx_length() < len("WX online with BMP180\n"):
    time.sleep(0)
 # need to set up and verify Ham, set a flag bit if failand shut down
 #get permission to TX from Teency
 #need to setup a non maskable int so to detect a shutdown command from teency

    
#try:
print("Read I2c \n")
temp = "Temp: %.2f degC\n" % bmp.temperature()
press = "Press: %f Pa\n" % bmp.pressure()
proxy.text.add_tx("Read I2c \n")
proxy.text.clear_rx()# this and the next line is for keeping the program in step with fldigi
while proxy.text.get_rx_length() < len("Read I2c \n"):
    time.sleep(0)

proxy.text.add_tx("Start Msg  \n")
proxy.text.clear_rx()
while proxy.text.get_rx_length() < len("Start Msg  \n"):
    time.sleep(1)
print("Start Msg  \n")
print(temp)
proxy.text.add_tx(temp)
proxy.text.clear_rx()
while proxy.text.get_rx_length() < len(temp):
    time.sleep(1)

proxy.text.add_tx(press)
proxy.text.clear_rx()
while proxy.text.get_rx_length() < len(press):
    time.sleep(1)
print("Print data\n")
proxy.text.clear_rx()
proxy.text.add_tx("*******************end Msg  \n")
proxy.text.clear_rx()
while proxy.text.get_rx_length() < len("*******************end Msg  \n"):
    time.sleep(2)
proxy.main.abort()            
#except KeyboardInterrupt: #Hit ctrl-c to trigger this program to quit
print("Exiting")

# for shutdown:
#os.system("sudo shutdown -h now")
