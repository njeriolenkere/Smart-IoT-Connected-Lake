# Smart IoT connected Lake

* Student name: [Njeri Olenkere](https://github.com/njeriolenkere)
* Student username: no222gv
* School: [Linneaus University](https://lnu.se/en/)
* Course:  [Applied Internet of Things](https://lnu.se/en/course/introduction-to-applied-internet-of-things/distance-international-summer/)
* Year: July 2022

## Project Overview
The aim of this project is to create a smart IOT connected lake. Using the temperature sensor (DS18B20) and the pH sensor (SEN0161) to measure and send the data collected via WIFI to an  IoT platform(Ubidots) for visualisation. Depending on your level of skill and hardware or software problems, this project can take between 4-48 hours.

![projectOverview](https://user-images.githubusercontent.com/50623449/175966042-1a00d573-fcf9-4389-ac72-350f675e068d.jpg)
*Figure 1: Project overview*


## Objective
Initially I wanted to create a smart garden, but due to hardware delay and eventual cancellation, I had to create something else. Our lecturer, Fredrik, shared with us, the students, several project inspiration .  One of the project ideas inspired me to create the smart IoT connected lake.
The purpose of this system is to measure and gather the data of the lake named Tröllsjön, in Tranås, Sweden. The temperature is measured to avoid the body from getting a cold water shock when you dive in the first time while the pH is measured to know the pH scale of the water because according to [usgs.gov](https://www.usgs.gov/faqs/can-lakes-near-volcanoes-become-acidic-enough-be-dangerous-people-and-animals) they state that pH of 0.5 is potentially capable of causing burns to human skin. The data collected from the temperature sensor (DS18B20) and the pH sensor (SEN0161) can be viewed on the IOT platform(Ubidots) to help the swimmer know the conditions of the lake before they take a dive.

![ph_scale](https://user-images.githubusercontent.com/50623449/175970185-f554e611-fa88-4576-b9a7-8ab2cc481a02.png)
*Figure 2: PH scale designed using [Inkscape](https://inkscape.org/)*


## Materials: Hardware
To complete the tutorial, you can use any Pycom ESP32 development board that supports WIFI. In this tutorial we focus on [LoPy4](https://docs.pycom.io/products/) If you are environment conscious, you can purchase cheaper second-hand devices for around 600 Swedish crowns at online stores. If you want to buy new devices like this one [Pycom Basic bundle @ Electrokit](https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-fipy-basic-bundle/) , it will cost you up to 1,348 Swedish crowns.

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
I tried using Pycharm IDE but at this time they do not support Pymakr plugin yet hence I download and used Atom IDE for windows because they support the plugin.  Download and install  [Atom (here)](https://atom.io/). Then  download and install [Node js (here)](https://nodejs.org/en/). After installing both Atom and Node.js, restart you computer. Find a detailed tutorial here : [Pycom](https://docs.pycom.io/)  If you want to use another IDE such as Visual Studio Code IDE follow this easy to follow tutorial : [Visual Studio Code set up](https://www.youtube.com/watch?v=fu_O6gtrDG4) Note: All the softwares used in this project are free.

### Step 2: LoPy4 and development board
Connect the Lopy4 to the board 3.1 using pins. Then connect your device (1) to the computer using the USB cable (2). ![getting_started](https://user-images.githubusercontent.com/50623449/176187022-14cae240-89fa-4e1b-aaf0-a0b36debb4b3.png)
*Figure 4: Source: [Pycom.io](https://docs.pycom.io/)*

### Step 3: Firmware update
+ Update your firmware to the latest version to avoid running into issues.  [Upload Firmware for Updating Device (here)](https://docs.pycom.io/updatefirmware/device/). Install the downloaded file and open it. Press Continue.
+ Communication -> type, choose development and press continue.  
+ RESET ->  check the boxes, CONFIG partion  and  NVS Partition, press continue.
+ Advance setting -> on device type, choose your device.  On file system  ->  check the boxes of Erase during update. On LoRa region  ->  choose your country,  press continue. 
+ After a few minutes, you will see results, press done. 

### Step 4: Setting up Atom
Open Atom go to file->settings->install->search for Pymakr and then install it. Step by step guide on [how to install Pymaker in Atom (here)]https://docs.pycom.io/gettingstarted/software/atom/

### Step 5: Add project
On Atom, go to File-> add Project Folder 
Give the Project Folder a name eg. lopy. Right click on your Project Folder ->New File-> write main.py, click enter. Repeat the same procedure inorder create a boot.py file and config.py file.

![3COM](https://user-images.githubusercontent.com/50623449/176190060-31a16201-dd67-4b03-9f83-c1dfd7cdcc48.png)
*Figure 5: Atom project*

Click on the main.py and paste this MicroPython code below and press **ctrl + S** on your keyboard to save it. Important! Always save the file after pasting or writing it before uploading it to avoid errors).
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
If you upload the main.py file but encounter a problem such as >>Upload failed: No project open, check (1) to make sure the Project Folder (lopy) is selected and not pymakr. Click the upload button (3) and it should begin blinking.

![prob1](https://user-images.githubusercontent.com/50623449/176201445-12df694b-68c5-4917-b1b7-e7b39e4a909f.png)
*Figure 6: Troubleshooting*

### Troubleshoot: Problem 2
If the Pymaker console indicates Conecting to ...>> failed to connect (error: Port is not open) Click here to try again, reconnect the micro controller, uninstall and then install the Pymaker. Then upload main.py file. If that doesn't work, it is possible that the Pymarker console did not identify the right COMM port. To solves this, follow this tutorial: [COMM Port Issue solved, Time: 18:25-20:35](https://www.youtube.com/watch?v=BPSxLsorNco&t=1223s)

### Troubleshoot: Problem 3
If you cannot see the console that allows you to upload your file, if you have not installed the Pymakr plugin do so. If you have already installed thePymakr Plugin but still you cannot see the console do this: File-> Settings-> Install ->  search for Pymakr plugin. Diasble then uninstall it. Now reinstall the Pymakr plugin.

### Troubleshoot: Problem 4
If you press the play button(3) and you get a no module named error message eg, ImportError: no module named 'pycom' ,first upload the file into the device by using the upload button. After you can press the play button.


