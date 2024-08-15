# SmartAlarmClock

A smart alarm clock built with a Raspberry Pi 5 that displays the current time, the room temperature, and the outside temperature.

## Table of Contents
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)

## Features
- Displays the current time in a user-friendly interface.
- Monitors and displays the room temperature and humidity using a BME280 sensor.
- Fetches and displays the current outside temperature using an online weather API.
- Button functionality to switch between inside and outside temperature display.

## Hardware Requirements
- Raspberry Pi 5
- BME280 sensor module
- I2C-enabled display (e.g., OLED display or LCD)
- Internet connection (for fetching outside temperature)
- Button (momentary push button) with appropriate resistors
- Breadboard and jumper wires for connections
- Speaker or buzzer (for alarm functionality)
- RTC (Real-Time Clock) module (optional, for accurate timekeeping without internet)

## Software Requirements
- Raspberry Pi OS (or another Linux-based OS compatible with Raspberry Pi)
- Python 3.x
- `adafruit-circuitpython-bme280` library
- `requests` library (for API requests)
- `datetime` module (part of the standard Python library)
- `RPi.GPIO` library (for button handling)
- Additional libraries for I2C display and sound (e.g., `adafruit-circuitpython-ssd1306`, `pygame`)


