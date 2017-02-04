# we need a line to start FLDIGI programaticaly
import time
import math
import os  # for shut down
import pyfldigi  # custom library for communicating with FLDIGI via XML-RPC protocol
import serial  # pyserial, a popular library for talking to a serial port
import weather  # Pyweather, library for Davis weather station and others

fldigi = pyfldigi.Client()  # NOTE: uses default port and localhost IP address


class RadioException(Exception):
    '''This is a custom exception type that should be thrown
    if the radio does someething bad'''
    pass

class TeensyException(Exception):
    '''This is a custom exception that should be thrown when
    the Teensy does something bad'''
    pass

class WeatherStationException(Exception):
    '''This is a custom exception type that should be thrown when
    there is something wrong with the weather station'''


class WeatherData(object):

    '''This class represents a model of the weather data.  It
    can also formatting this data into a text string to be
    transmitted out of the radio'''

    def __init__(self):
        self.temp = None
        self.pressure = None
        self.dewpoint = None
        self.humidity = None
        self.tempf = None
        self.rainin = None
        self.rainday = None
        self.dateutc = None
        self.windspeed = None
        self.winddir = None
        self.windgust= None
        self.windgust_dir = None

    def encode(self):
        '''Encode the data into an FLDI transmit string'''
        s = 'WEATHER : '
        s += 'TEMP={}, '.format(self.temp)
        s += 'PRESSURE={}, '.format(self.pressure)
        s += 'DEWPOINT={}, '.format(self.dewpoint)
        s += 'HUMIDITY={}, '.format(self.humidity)
        s += 'RAIN_RATE={},'.format(self.rainrate)
        s += 'WINDSPEED={},'.format(self.windspeed)
        s += 'WIND_DIR={},'.format(self.winddir)
        s += '{},'.format(self.)
        s += '{},'.format(self.)
        s += '{},'.format(self.)
        s += '{}'.format(self.)
        
        return s


class WeatherStationController(object):

    '''This class is responsible for talking to the weather
    station via serial.'''

    def __init__(self, comport):
        self.comport = comport
        self.interval = 60

    def initialize(self):
        self.station = weather.stations.VantagePro(self.comport)

    def getWeatherData(self):
        '''Reads the weather data from the weather station,
        and returns a WeatherData object'''
        try:
            self.station.parse()  # read weather data
            # sanity check weather data
            wd = WeatherData()
            
            wd.temp = station.fields['TempOut']
            if station.fields['TempOut'] > 200:
                raise WeatherStationException('Out of range temperature value: {}.  Check sensors'.format(temp))
            wd.pressure = self.station.fields['Pressure']
            wd.dewpoint = self.station.fields['DewPoint']
            wd.humidity = self.station.fields['HumOut']
            wd.rainrate = self.station.fields['RainRate']
            wd.rainday = self.station.fields['RainDay']
            wd.dateutc = self.station.fields['DateStampUtc']
            wd.windspeed = self.station.fields['WindSpeed10Min']
            wd.winddir = self.station.fields['WindDir']
            wd.windgust, wd.windgust_dir = WindGust.get(self.station, self.interval)
        except Exception as e:
            # TODO: Add logging and/or exception handling here
            raise WeatherStationException('Could not acces fields')
        return wd
        
    def close(self):
        if self.session.is_open:
            ser.close()


def launchFldigi():
    pass

def checkRadioStatus():
    # read GPIO pin.  True is GOOD, False is BAD.
    pin = True  # This is mock data TBD
    if pin is False:
        raise RadioException('Radio was not happy')
    

def checkTeensyStatus():
    # read GPIO pin or whatever the Teensy status is
    pin = True
    if pin is False:
        raise TeensyException('Teensy was not happy')

def getWeatherData():
    '''Get data from serial port, TBD'''
    pass

def encodeWeatherData():
    '''Encode the weather object into a text block that will be transmitted via fldigi'''
    pass

def transmitData():
    '''Send a string of data via fldigi'''
    pass

def terminateFldigi():
    '''Shut down FLDIGI'''
    pass

def shutdown():
    '''Shutdown the Raspberry Pi'''
    pass


# Now do it!!!!

try:
    launchFldigi()
    checkRadioStatus()
    checkTeensyStatus()
    foo()
except RadioException:
    print('a radio exception occured')

terminateFldigi()
shutdown()



# #################################################################


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
