# SmartAlarmClock

This project is a smart alarm clock built with a Raspberry Pi 5 that displays the current time, monitors the room temperature, and outside temperature. It features button functionality to switch between inside and outside temperature displays.

## Table of Contents
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)

## Features
- Displays the current time on a TM1637 4 digit 7-segment display.
- Monitors and displays room temperature and humidity using a BME280 sensor.
- Fetches and displays the current outside temperature using an online weather API.
- Button functionality to switch between inside (room) and outside temperature display on an LCD screen.

## Hardware Requirements
- Raspberry Pi 5
- TM1637 7-segment display
- BME280 sensor module (for temperature and humidity)
- I2C-enabled display (e.g., OLED display or LCD)
- Internet connection (for fetching outside temperature)
- Button (momentary push button) with appropriate resistors
- Breadboard and jumper wires for connections

## Software Requirements
- Raspberry Pi OS (or another Linux-based OS compatible with Raspberry Pi)
- Python 3.x
- `adafruit-circuitpython-bme280` library for the BME280 sensor
- `requests` library for API requests
- `gpiod` library for GPIO handling
- `LCDdisplay` library for LCD screen handling
- `datetime` module (part of the standard Python library)
- Custom `tm1637` library for handling the TM1637 display (Forked from online sources)
