import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280
import gpiod
import LCDdisplay as LCD
import requests
import sys
import datetime
from tm1637_display import TM1637, digits  # Import TM1637 class and digits dictionary

# Create I2C bus object using board
i2c = busio.I2C(board.SCL, board.SDA)

# Create BME280 sensor object with the correct I2C address
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# Pin and button count set
BUTTON_PIN = 17
ButtonCount = 0

# Initialize the LCD display
LCD.init(0x27, 1)

# URL for API Weather Data
apiKey = "7b91ce078db9405fbe9165153241508"
baseURL = "http://api.weatherapi.com/v1/current.json?key=" + apiKey + "&q="
cityName = input("Enter your city: ")
completeURL = baseURL + cityName + "&aqi=no"

# Initialize the GPIO chip and request the button line
chip = gpiod.Chip('gpiochip0')
button_line = chip.get_line(BUTTON_PIN)
button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

# Initialize TM1637 display with CLK pin 18 and DIO pin 22
tm = TM1637(clk_pin=18, dio_pin=22)

try:
    response = requests.get(completeURL)
    response.raise_for_status()  # Raise an error if the request failed
    data = response.json()
    Temp = data["current"]["temp_f"]
    Wind = data["current"]["wind_mph"]
    Humidity = data["current"]["humidity"]

    LCD.write(2, 0, 'Click Button')
    LCD.write(4, 1, 'To Start')

    while True:
        # Read sensor data
        temperature_cRoom = bme280.temperature
        humidityRoom = bme280.humidity
        pressureRoom = bme280.pressure
        
        # Convert temperature to Fahrenheit
        temperature_fRoom = temperature_cRoom * 9 / 5 + 32
        
        # Format temperatures to one decimal place
        Temp_formatted = f"{Temp:.1f}"
        temperature_fRoom_formatted = f"{temperature_fRoom:.1f}"
        
        # Check button state
        button_state = button_line.get_value()
        
        if button_state == 1:  # Button pressed
            ButtonCount += 1
            LCD.clear()
            
            if ButtonCount > 2:
                ButtonCount = 1
            
            if ButtonCount == 1:
                LCD.write(0, 1, 'Temp: ')
                LCD.write(6, 1, Temp_formatted)
                LCD.write(2, 0, cityName)
                LCD.write(10, 1, 'F')
            elif ButtonCount == 2:
                LCD.write(0, 1, 'Temp: ')
                LCD.write(6, 1, temperature_fRoom_formatted)
                LCD.write(10, 1, 'F')
                LCD.write(4, 0, 'Bedroom')
        
        # Display the current time on the TM1637
        current_time = datetime.datetime.now().strftime("%H%M")  # Get the current time in HHMM format
        data = [
            digits[current_time[0]],
            digits[current_time[0]],
            digits[current_time[1] + ':'],
            digits[current_time[2]],  # Display ':' between hours and minutes
            digits[current_time[3]]
        ]
        tm.display(data)

        time.sleep(1)  # Wait for a second before updating the display

finally:
    button_line.release()
    tm.cleanup()  # Ensure TM1637 display GPIO lines are released
