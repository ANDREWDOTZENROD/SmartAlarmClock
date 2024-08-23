import time
import gpiod
import signal
import sys

# TM1637 Constants
TM1637_CMD1 = 0x40
TM1637_CMD2 = 0xC0
TM1637_CMD3 = 0x80
TM1637_DOT = 0x80
TM1637_BLINK = 0x00
TM1637_DISPLAY = 0x08

# Digit encoding
digits = {
    '0': 0b00111111,
    '1': 0b00000110,
    '2': 0b01011011,
    '3': 0b01001111,
    '4': 0b01100110,
    '5': 0b01101101,
    '6': 0b01111101,
    '7': 0b00000111,
    '8': 0b01111111,
    '9': 0b01101111,
    '0:': 0b10111111,
    '1:': 0b10000110,
    '2:': 0b11011011,
    '3:': 0b11001111,
    '4:': 0b11100110,
    '5:': 0b11101101,
    '6:': 0b11111101,
    '7:': 0b10000111,
    '8:': 0b11111111,
    '9:': 0b11101111,
    
}

class TM1637:
    def __init__(self, clk_pin, dio_pin):
        self.clk_pin = clk_pin
        self.dio_pin = dio_pin

        # Set up GPIO
        self.chip = gpiod.Chip('/dev/gpiochip0')
        self.clk = self.chip.get_line(self.clk_pin)
        self.dio = self.chip.get_line(self.dio_pin)
        self.clk.request(consumer='tm1637', type=gpiod.LINE_REQ_DIR_OUT)
        self.dio.request(consumer='tm1637', type=gpiod.LINE_REQ_DIR_OUT)

    def _start(self):
        self.dio.set_value(0)
        self.clk.set_value(0)

    def _stop(self):
        self.dio.set_value(0)
        self.clk.set_value(1)
        self.dio.set_value(1)

    def _write_byte(self, data):
        for i in range(8):
            if (data & (1 << i)):
                self.dio.set_value(1)
            else:
                self.dio.set_value(0)
            self.clk.set_value(1)
            self.clk.set_value(0)

        self.dio.set_value(1)
        self.clk.set_value(1)
        self.clk.set_value(0)
        self.dio.set_value(0)

    def _send_command(self, cmd):
        self._start()
        self._write_byte(cmd)
        self._stop()

    def display(self, data):
        self._send_command(TM1637_CMD1)
        self._send_command(TM1637_CMD2)
        self._start()
        for byte in data:
            self._write_byte(byte)
        self._stop()
        self._send_command(TM1637_CMD3 | TM1637_DISPLAY)

    def cleanup(self):
        self.clk.release()
        self.dio.release()
        self.chip.close()

def signal_handler(sig, frame):
    print("Exiting...")
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    tm = TM1637(18, 22)  # CLK and DIO pins
    try:
        while True:
            # Display "10:30"
            tm.display([ digits['0'], digits['3'], digits['0:'], digits['3'], digits['0']])
            time.sleep(1)  # Update every second
    except KeyboardInterrupt:
        pass
    finally:
        tm.cleanup()
