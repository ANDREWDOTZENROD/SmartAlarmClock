import gpiod
import time
import LCDdisplay as LCD
import requests

BUTTON_PIN = 17
ButtonCount = 0
LCD.init(0x27,1)
apiKey = "7b91ce078db9405fbe9165153241508"
baseURL = "http://api.weatherapi.com/v1/current.json?key=" + apiKey + "&q="
cityName = input("Enter your city: ")
completeURL = baseURL + cityName + "&aqi=no"

# Initialize the GPIO chip and request the button line
chip = gpiod.Chip('gpiochip0')
button_line = chip.get_line(BUTTON_PIN)
button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

try:
    response = requests.get(completeURL)
    response.raise_for_status()  # Raise an error if the request failed
    data = response.json()
    Temp = data["current"]["temp_f"]
    Wind = data["current"]["wind_mph"]
    Humidity = data["current"]["humidity"]
    LCD.write(2,0,'Click Button')
    LCD.write(4,1,'To Start')
    while True:
        button_state = button_line.get_value()
        if button_state == 1:  # Pressed
            ButtonCount += 1
            LCD.clear()
            if ButtonCount > 3:
                ButtonCount = 1
            
            if ButtonCount == 1:
                LCD.write(0,1,'Temp: ')
                LCD.write(6,1,str(Temp))
            elif ButtonCount == 2:
                LCD.write(0,1,'Wind: ')
                LCD.write(6,1,str(Wind))
                LCD.write(10,1,'MPH')
            elif ButtonCount == 3:
                LCD.write(0,1,'Humidity : ')
                LCD.write(12,1,str(Humidity))
                LCD.write(14,1,'%')

            LCD.write(0,0,'City: ')
            LCD.write(5,0,str(cityName))

        time.sleep(0.2)

finally:
   button_line.release()
