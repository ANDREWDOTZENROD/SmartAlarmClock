import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

# Create I2C bus object
i2c = busio.I2C(board.SCL, board.SDA)

# Create BME280 sensor object with the correct I2C address
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

while True:
    try:
        # Read sensor data
        temperature_c = bme280.temperature
        humidity = bme280.humidity
        pressure = bme280.pressure
        
        # Convert temperature to Fahrenheit
        temperature_f = temperature_c * 9 / 5 + 32
        
        # Print sensor data
        print(f"Temperature: {temperature_f:.2f} °F")
        print(f"Humidity: {humidity:.2f} %")
        print(f"Pressure: {pressure:.2f} hPa")
        
        # Wait before reading again
        time.sleep(1)
        
    except KeyboardInterrupt:
        print(" Program stopped")
        break
