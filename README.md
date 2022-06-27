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
| ----------- | :-------------- | -------------- | ----------- |
| LoPy4      | The LoPy4 is Micropython-programmable quadruple bearer board.  |  ![lopy](https://user-images.githubusercontent.com/50623449/175974259-470f2112-fa5d-4d31-b082-1476a6deab3a.png)| Store       |
| Expansion Board v3.1   | The Expansion Board v3.1 is a  printed circuit board that is insert into a LoPy4 to give it added capabilities. It is compatible with the WiPy 3.0, LoPy4, SiPy, FiPy and Gpy.         |  Pic        | store       |
| Breadboard   | Used for building circuits on.        |   Pic        | Store       |
| Jumpwire (20 st)   | Used to interconnect the components on a breadboard.         |   Pic          |  Store       |
| Temperature Sensor (DS18B20)  | Used to measure extreme cold and heat (-55 to 125 °C).         |   Pic         |  Store      |
| pH Sensor (SEN0161)   | Used to get pH measurements.       |   Pic         |  Store       |
| Resistor (4.7kΩ)   | 4.7kΩ pullup resistor used to limit the current in a circuit.        |   Pic         |  Store       |
| Micro USB cable   | Used for connecting the computer to the Expansion Board v3.1         |   Pic         |  Store      |

*Figure 3: Table with bill of materials*
[ ]
