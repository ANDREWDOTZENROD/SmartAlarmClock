import smartClockProj.LCDdisplay as LCD
import time

LCD.init(0x27,1)
x = 0
try:
    while True:
        for x in range(1,16,.5):
            LCD.write(x,0,'0')
            LCD.write(0,1,'BITCH')
            time.sleep(.15)
            LCD.clear()

except KeyboardInterrupt:
    time.sleep(.2)
    LCD.clear()
    print (" RBP has been reset")