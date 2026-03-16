from Sensor import Sensor, Pin
from machine import Pin
from machine import Timer
import time

"""
R, G, B
255, 0, 0 = Red
0, 255, 0 = Green
0, 0, 255 = Blue
255, 255, 0 = Yellow
255, 0, 255 = Magenta
0, 255, 255 = Cyan
0, 0, 0 = Black
255, 255, 255 = White
"""

class ColorSensor(Sensor):

    T = Timer(0) # Create a timer object for timing functions

    def __init__(self, pin:int):
        super().__init__(pin) 

    """
    Uses RGB_Value, not original sensor value, 
    returns a boolean if the RGB value from the sensor matches the given value tuple (R, G, B)
    """
    # Override
    def detected(self, value: tuple, sensor: Pin) -> bool: 
        if self.RGB_Value(sensor) == value:
            return True
        else:
            return False
    
    # Override
    def read(self, sensor:Pin) -> int: # Returns the raw sensor RGB value
        return sensor.value()

    def RGB_Value(self, sensor:Pin) -> tuple: # Returns the RGB value as a tuple (R, G, B)
        R = (self.read(sensor) >> 16) & 0xFF   # Extract the red value from the sensor reading, moves the value 16 bits to the right and masks with 0xFF to get the last 8 bits
        G = (self.read(sensor) >> 8) & 0xFF    # Extract the green value from the sensor reading, moves the value 8 bits to the right and masks with 0xFF to get the last 8 bits
        B = self.read(sensor) & 0xFF           # Extract the blue value from the sensor reading, masks with 0xFF to get the last 8 bits
        return (R, G, B) # Return the RGB values as a tuple

    # Override
    def loop_sensor_interval(self, interval: int, sensor: Pin) -> list: # Loop and return RGB values at a specified interval in milliseconds
        self.loop = True
        data = []
        self.T.init(period=interval, mode=Timer.ONE_SHOT, callback=lambda t: setattr(self, 'loop', False))  #Stop Loop after interval
        while self.loop:
            time.sleep_ms(100)      # Sleep for 100 milliseconds
            data.append(self.RGB_Value(sensor))   # Read the sensor value
        return data
    
    # Override
    def loop_sensor_bool(self, bool: bool, sensor: Pin) -> list:
        self.loop = bool
        data = []
        while self.loop:
            time.sleep_ms(100)      # Sleep for 100 milliseconds
            data.append(self.RGB_Value(sensor))   # Read the sensor value
        return data

    # Override 
    def print_data(self, value: tuple, sensor:Pin): # Print formatted data from the sensor
        print("Color Sensor Value: R: " + str(value[0]) + ", G: " + str(value[1]) + ", B: " + str(value[2])) # Print the RGB values in a formatted string