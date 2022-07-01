import time
import pycom
import machine
from machine import Pin, I2C, ADC, PWM
from onewire import DS18X20 #Library for dealing with DS18X20 sensors
from onewire import OneWire #Library for Onewire
from network import WLAN
import urequests as requests  #Call library urequests file
from config import SSID, PASS, TOKEN #Call config file that contains your ssid, password and token


pycom.heartbeat(False) # We disable LED heartbeat to control it manually
pycom.rgbled(0x00FF00)  # Green

# Builds the json to send the request
def build_json(variable1, value1, variable2, value2):
    try:
        data = {variable1: {"value": value1},
                variable2: {"value": value2}}
        return data
    except:
        return None

# Sends the request. Please reference the REST API reference https://ubidots.com/docs/api/
def post_var(device, value1, value2):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json("temperature", value1, "pH", value2)
        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass

# set up pH sensor
adc = machine.ADC(bits=10)# ADC (Analogue to Digital Conversion)
apin = adc.channel(pin='P16') # create an analog pin on P16

# set up Temperature sensor
ow = OneWire(Pin('P22')) # DS18B20 data line connected to pin P22
temp = DS18X20(ow)

# WiFi Declaration
wlan = WLAN(mode=WLAN.STA)
# Assign your own Wi-Fi credentials (SSID and Password = PASS)
wlan.connect(SSID, auth=(WLAN.WPA2, PASS))
while not wlan.isconnected():
    machine.idle()
print("Connected to Wifi\n")

while True:
    millivolts = apin.voltage()  # Reads the voltage in mV
    print(millivolts)
    # Data values
    pH = millivolts / 1024 * 5 * 1.45   # Calculates the pH
    print(pH)
    print("pH is: {}".format(pH))
    time.sleep(5)
    temp.start_conversion()
    time.sleep(1)     # Start the temp conversion on one DS18x20 device
    temperature = temp.read_temp_async()    # Read the temperature of one DS18x20 device if the conversion is complete, otherwise return None.
    while temperature is None:
        temperature = temp.read_temp_async()
    print("Temperature is: {}".format(temperature))

    # Post data to Ubidots
    post_var("pycom", temperature, pH)
    time.sleep(900) #send every 15 mins
