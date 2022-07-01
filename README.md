# Smart IoT connected Lake

* Student name: [Njeri Olenkere](https://github.com/njeriolenkere)
* Student username: no222gv
* School: [Linneaus University](https://lnu.se/en/)
* Course:  [Applied Internet of Things](https://lnu.se/en/course/introduction-to-applied-internet-of-things/distance-international-summer/)
* Year: July 2022

## Project Overview
The aim of this project is to teach how to create a smart IoT connected lake. Using the temperature sensor (DS18B20) and the pH sensor (SEN0161) to measure and send the data collected via WIFI to an  IoT platform(Ubidots) for visualisation. Depending on your level of skill and hardware or software problems, this project can take between 4-48 hours.

![projectOverview](https://user-images.githubusercontent.com/50623449/175966042-1a00d573-fcf9-4389-ac72-350f675e068d.jpg)
*Figure 1: Project overview*


## Objective
Initially I wanted to create a smart garden, but due to hardware delay and eventual cancellation, I had to create something else. Our lecturer, Fredrik, shared with us, the students, several project inspiration .  One of the project ideas inspired me to create the smart IoT connected lake.
The purpose of this system is to measure and gather the data of the lake named Tröllsjön, in Tranås, Sweden. The temperature is measured to avoid the body from getting a cold water shock when you dive in the first time while the pH is measured to know the pH scale of the water because according to [usgs.gov](https://www.usgs.gov/faqs/can-lakes-near-volcanoes-become-acidic-enough-be-dangerous-people-and-animals) they state that pH of 0.5 is potentially capable of causing burns to human skin. The data collected from the temperature sensor (DS18B20) and the pH sensor (SEN0161) can be viewed on the IOT platform(Ubidots) to help the swimmer know the conditions of the lake before they take a dive.

![ph_scale](https://user-images.githubusercontent.com/50623449/175970185-f554e611-fa88-4576-b9a7-8ab2cc481a02.png)
*Figure 2: PH scale designed using [Inkscape](https://inkscape.org/)*


## Materials: Hardware
To complete the tutorial, you can use any Pycom ESP32 development board that supports WIFI. In this tutorial we focus on [LoPy4](https://docs.pycom.io/products/). If you are environment conscious, you can purchase cheaper second-hand devices for around 600 Swedish crowns at online stores. If you want to buy new devices like this one [Pycom Basic bundle @ Electrokit](https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-fipy-basic-bundle/) , it will cost you up to 1,348 Swedish crowns.

| Name        | Specifications | Picture        | Store       |
| :----------- | :-------------- | -------------- | :----------- |
| LoPy4      | The LoPy4 is Micropython-programmable quadruple bearer board.  |  ![lopy](https://user-images.githubusercontent.com/50623449/175974259-470f2112-fa5d-4d31-b082-1476a6deab3a.png)| [Pycom](https://pycom.io/product/lopy4/)     |
| Expansion Board v3.1   | The Expansion Board v3.1 is a  printed circuit board that is insert into a LoPy4 to give it added capabilities. It is compatible with the WiPy 3.0, LoPy4, SiPy, FiPy and Gpy.         |  ![expansionBoard](https://user-images.githubusercontent.com/50623449/176181995-538b92d5-510c-4575-a9e7-9041344a0d10.png) | [Pycom](https://pycom.io/product/expansion-board-3-0//)    |
| Breadboard   | Used for building circuits on.        | ![breadb](https://user-images.githubusercontent.com/50623449/176182048-a0141aa7-a436-4b46-969c-90a449c49ddb.png) | [HiTechChain](https://hitechchain.se/arduinokompatibel/tillbehor/kopplingsdack-breadboard-83x55cm)    |
| Jumpwire (20 st)   | Used to interconnect the components on a breadboard.         |  ![jumpercables](https://user-images.githubusercontent.com/50623449/176182102-033f2d21-c7aa-464d-b01f-6030ce509f8b.jpeg) |  [HiTechChain](https://hitechchain.se/arduinokompatibel/tillbehor/kopplingsdack-breadboard-jumper-wire)       |
| Temperature Sensor (DS18B20)  | Used to measure extreme cold and heat (-55 to 125 °C).   |  ![temp](https://user-images.githubusercontent.com/50623449/176182195-b4792e2f-0378-47b2-a1d7-36e9ff9df7a8.png)|  [HiTechChain](https://hitechchain.se/iot/ttgo/ttgo-waterproof-ds18b20-temperature-probe-temperature-sensor-18b20-stainless-steel-package)     |
| pH Sensor (SEN0161)   | Used to get pH measurements.     |  ![ph](https://user-images.githubusercontent.com/50623449/176182244-ca31dfb1-f3c6-4e15-936c-ee86f3a12891.png) | [Arduino](https://store.arduino.cc/products/gravity-analog-ph-sensor-meter-kit?queryID=undefined)      |
| Resistor (4.7kΩ)   | 4.7kΩ pullup resistor used to limit the current in a circuit.    |![resistor](https://user-images.githubusercontent.com/50623449/176184543-5a4d1d40-dddc-4e56-a6d5-964702ef40be.jpg) | [Electrokit](https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-fipy-basic-bundle/)       |
| Micro USB cable   | Used for connecting the computer to the Expansion Board v3.1  |  ![usbCable](https://user-images.githubusercontent.com/50623449/176182383-f7fbeae1-55e9-4e13-b9a9-f548f738cd8a.png) |  [Electrokit](https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-fipy-basic-bundle/)      |

*Figure 3: Table with bill of materials*


## Computer set up
### Step 1: Choosing IDE(Integrated Development Environment)
I tried using Pycharm IDE but at this time they do not support Pymakr plugin yet hence I download and used Atom IDE for windows because they support the plugin.  Download and install  [Atom (here)](https://atom.io/). Then  download and install [Node js (here)](https://nodejs.org/en/). After installing both Atom and Node.js, restart you computer. Find a detailed tutorial here : [Pycom](https://docs.pycom.io/).  If you want to use another IDE such as Visual Studio Code IDE follow this easy to follow tutorial : [Visual Studio Code set up](https://www.youtube.com/watch?v=fu_O6gtrDG4). **Note:** All the softwares used in this project are free.

### Step 2: LoPy4 and development board
Connect the Lopy4 to the board 3.1 using pins. Then connect your device (1) to the computer using the USB cable (2). ![getting_started](https://user-images.githubusercontent.com/50623449/176187022-14cae240-89fa-4e1b-aaf0-a0b36debb4b3.png)
*Figure 4: Source: [Pycom.io](https://docs.pycom.io/)*

### Step 3: Firmware update
Update your firmware to the latest version to avoid running into issues.  
+ [Download Firmware for Updating Device (here)](https://docs.pycom.io/updatefirmware/device/), Install the downloaded file and open it. Press Continue.
+ Communication -> type, choose **development** and press continue.  
+ RESET ->  check the boxes, **CONFIG Partition  and  NVS Partition**, press continue.
+ Advance setting -> on device type, **choose your device**.  On file system  ->  check the boxes of **Erase during update**. On LoRa region  ->  **choose your country**,  press continue. 
+ After a few minutes, you will see results, press done. 

### Step 4: Setting up Atom
Open Atom go to file->settings->install->search for Pymakr and then install it. Step by step guide on [how to install Pymaker in Atom (here)](https://docs.pycom.io/gettingstarted/software/atom/).

### Step 5: Add project
On Atom, go to File-> add Project Folder 
Give the Project Folder a name eg. lopy. Right click on your Project Folder ->New File-> write main.py, click enter. Repeat the same procedure inorder create a boot.py file and config.py file.

![3COM](https://user-images.githubusercontent.com/50623449/176190060-31a16201-dd67-4b03-9f83-c1dfd7cdcc48.png)
*Figure 5: Atom project*

Click on the main.py and paste this MicroPython code below and press **ctrl + S** on your keyboard to save it. **Important!!!** Always save the file after pasting or writing it before uploading it to avoid errors).
```MicroPython
import pycom
import time

pycom.heartbeat(False)
while True:
    #colors in hexadecimal (0xRRGGBB)
    pycom.rgbled(0xFF0000)  # LED turns Red
    time.sleep(1)
    pycom.rgbled(0x00FF00)  # LED turns Green
    time.sleep(1)
    pycom.rgbled(0x0000FF)  # LED turns Blue
    time.sleep(1) 
   ```
    
Click on the upload button to feed the code to your device. If your device is connected and working properly, the LED light on the Lopy4 will start blinking red, green and blue every second. To stop the blinking of the LED use **ctrl + C** to cancel the while loop.

### Troubleshoot: Problem 1 
If you upload the main.py file but encounter a problem such as >>Upload failed: No project open, check Project Folder (1) to make sure that (lopy) is selected and not pymakr. Click the upload button (3) and your device Pycom should begin blinking.

![prob1](https://user-images.githubusercontent.com/50623449/176201445-12df694b-68c5-4917-b1b7-e7b39e4a909f.png)

*Figure 6: Troubleshooting*

### Troubleshoot: Problem 2
If the Pymaker console indicates Conecting to ...>> failed to connect (error: Port is not open) Click here to try again, reconnect the micro controller, uninstall and then install the Pymaker. Then upload main.py file. If that doesn't work, it is possible that the Pymarker console did not identify the right COMM port. To solves this, follow this tutorial: [COMM Port Issue solved, Time: 18:25-20:35](https://www.youtube.com/watch?v=BPSxLsorNco&t=1223s)

### Troubleshoot: Problem 3
If you cannot see the console that allows you to upload your file, if you have not installed the Pymakr plugin do so. If you have already installed thePymakr Plugin but still you cannot see the console do this: File-> Settings-> Install ->  search for Pymakr plugin. Disable then uninstall it. Now reinstall the Pymakr plugin.

### Troubleshoot: Problem 4
If you press the play button(3) and you get a no module named error message eg, ImportError: no module named 'pycom', no worries. Upload the file into the device by using the upload button. After that you can press the play button.

### Troubleshoot: Problem 5
If the Pymakr console is greyed out, or if you click on the upload button or any button on the console it does not respond, do this. Close the Atom IDE, reopen again and it should work. Sometimes you have to restart the computer for the error to be fixed.

## Putting everything together: Wiring sensors

![circuitFritzing2](https://user-images.githubusercontent.com/50623449/176835647-4f959a45-efa3-4bcb-9920-134b1f95ca0b.png)

*Figure 7: Circuit diagram* 

After successful completion of all the above steps, it is time to connect sensors and power them up. The data transfer cord (yellow) of pH sensor (SEN0161) connected to pin 16, while temperature sensor (DS18B20) data transfer cord (yellow) is connected to Pin 22. To learn more about Pins, [read LoPy Datasheet (here)](https://docs.pycom.io/gitbook/assets/lopy4-pinout.pdf). 
The temperature sensor (DS18B20) requires a pull-up resistor (4.7 Ohm) that will be connected between the data transfer cord and the power pin(red).  The reson why we use a pull-up resistor is because  temperature sensor (DS18B20) is a one wire device. One wire devices require resistors to be connected to the data signal line sothat data is read correctly by the sensor.
The power cord(red) and ground cord (black)of the pH sensor (SEN0161) and the temperature sensor (DS18B20) are connected at the lower lane. The black cord(GND) and the the red cord(3v 3) from the expansion board is connected to the breadboard at the lower lane to power up the whole lower lane with 3.3v power.
Check the datasheet of the hardware you have to determine things like the power requirement, resistor and the pins allocation.

## IoT visualisation Platform
I chose Ubidots since it offers both free (Ubidots STEM ) for students and personal use and paid subscription(For Business). The free Ubidots STEM is good for beginners since it has tutorials, offer 3 devices connection for free, no plugins required in-order to get started, neat real-time dashboard with many different widgets types, hosted on the cloud, good user interface design and easy to create events that triggers notifications via Email, SMS, Telegram, Voice calls, Webhooks or Slack notifications.  

![ubidots](https://user-images.githubusercontent.com/50623449/176404955-bb6d9ba2-3b66-4363-ae2c-a673ea5e76f6.png)

*Figure 8: IoT  visualisation platform | Ubidots*

The paid subscription(For Business) offers multiple device connection among other many important features that are good for Entrepreneurs , Professionals and Industries.

## The code : Software
We will use this libraries; urequest.py library is for Ubidots, while onewire.py library is for temperature sensor (DS18B20). So create a library file by right clicking on the Project Folder(lopy)  -> New folder. Name it lib.  Right click on lib  ->New File write urequests.py, click enter. Repeat the same procedure in-order create a onewire.py file.  
On Atom, click the urequests.py file and [copy this urequests.py code](https://github.com/njeriolenkere/Smart-IoT-Connected-Lake/blob/main/urequests.py) paste it and save. Click the onewire.py  file, [copy this onewire.py code](https://github.com/njeriolenkere/Smart-IoT-Connected-Lake/blob/main/onewire.py) paste it and save it.   Find the full code here: [Smart-IoT-Connected-Lake code (here)](https://github.com/njeriolenkere/Smart-IoT-Connected-Lake).  If you have done everything correctly, the your code structure should be organised as showned on *Figure 9*.

![lib](https://user-images.githubusercontent.com/50623449/176406650-57082fa6-8855-4b2a-8ab9-cd8396dcc1db.png)

*Figure 9: The code structure*

### main.py code
This main.py code does the following, imports libraries, set up network, collects data from the pH sensor (SEN0161) and the temperature sensor (DS18B20) and send that data to Ubidots via WIFI.

```MicroPython
import time
import pycom
import machine
from machine import Pin, I2C, ADC, I2C, PWM
from onewire import DS18X20 #Library for dealing with DS18X20 sensors
from onewire import OneWire #Library for Onewire
from network import WLAN
import urequests as requests  #Call library urequests file
from config import SSID, PASS, TOKEN #Call config file that contains your ssid, password and token


pycom.heartbeat(False) # We disable LED heartbeat to control it manually
pycom.rgbled(0x00FF00)  # LED turns Green

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
    time.sleep(900) #sends data to ubidots every 15 mins
   ```
## Transmitting data

The wireless protocol used in this project is WIFI. WIFI allows devices to connect to internet via a router. WIFI has high bit rate which is good to send data fast, it is short range and consumes more power. Since the device is connect to computer via USB charger, high power consumption is OK.
In this project we use WIFI at 2.4GHz that provide internet to large area but alittle bit slow compared to 5 Ghz. **Note:** If your wireless router does not support 2.4GHZ, you can use your phone as a WIFI hotspot. Read more on [How to Connect to Mobile WIFI (here)](https://www.businessinsider.com/what-is-mobile-hotspot?r=US&IR=T). The transport protocol used is WebHook (HTTPs) that packages data as JSON object and sends that data to Ubidot every 15 minutes. 

![CommTech](https://user-images.githubusercontent.com/50623449/176409605-35d3f4a1-2855-4ca8-9a1a-cbde1c4249df.jpg)

*Figure 10: Communication technologies [source: avsystem.com](https://www.avsystem.com/blog/iot-connectivity/)*

## Presenting data
Congratulations! You finally made it! This is the last part of the tutorial. Follow this guide to learn how to create dashboards and widgets in Ubidots.  [Guide on how to create Dashboards and Widgets (here)](https://help.ubidots.com/en/articles/2400308-create-dashboards-and-widgets). Below is how data is represented in Ubidots dashboard.

![dashboardDevices](https://user-images.githubusercontent.com/50623449/176837032-9b0d3f75-5a05-4b45-bdf7-ad87aef38bef.png)

*Figure 11:  Dashboard*

-----------
![dashboardIOT](https://user-images.githubusercontent.com/50623449/176837361-542f5359-40fa-45fc-9405-d4fab0111801.png)

*Figure 12: Sensors information on dashboard*

-----------
![eventsIOT](https://user-images.githubusercontent.com/50623449/176837443-c6888678-6126-43e2-9c1d-704f3fa90fa0.png)

*Figure 13: Events that sends triggers alerts*

-----------
The device automatically sends data after every 15 minutes which triggers the alerts that are sent via email. The data sent is stored for a month at the Ubidots which is a Cloud service. Check their help Center: [Ubidots data storage info (here)](https://help.ubidots.com/en/articles/636669-how-long-is-my-data-stored-for)

![alerts](https://user-images.githubusercontent.com/50623449/176837655-432246f8-2111-4855-b2d8-b498ed9509ad.png)

*Figure 14: Email alerts*

## The final project
Here is the final project.
![finalProject1](https://user-images.githubusercontent.com/50623449/176839215-f296a076-8dec-4608-95b6-d82727f9e342.jpg)

*Figure 15: Tröllsjön, Tranås in Sweden*

-----------

![finalProject2](https://user-images.githubusercontent.com/50623449/176839342-21dbfb0b-eb89-4885-84e4-8cf2108e95ac.jpg)

*Figure 16: Smart IoT connected Lake (Tröllsjön)*

-----------

![finalProject3](https://user-images.githubusercontent.com/50623449/176839465-4ebb2251-47c5-42d8-857d-58986d050b39.jpg)

*Figure 17: Real-time data visualisation on the dashboard*

-----------

![finalProject4](https://user-images.githubusercontent.com/50623449/176839548-55014f10-3f40-4bda-94cb-c6d2e455d613.jpg)

*Figure 18: Sensors in the water*

### Future
I would recommend anyone interested in Internet of Things (IoT), smart things to study [Applied Internet of Things](https://lnu.se/en/course/introduction-to-applied-internet-of-things/distance-international-summer/)  at the [Linneaus University](https://lnu.se/en/). The flexible workshops, guest lectures, amazing lecturers and TAs, quick help and fast feedback made the course excellent. The course opened me up to opportunities on what can be achieved with IoT. In the future, I hope to expand more on this project by adding more devices such as Oled display and sensors. I plan to also create other smart devices e.g. the Smart Garden.

Have a Smart Summer!
