from Sensor import Sensor
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
    running = [True] # List to hold the running state of the sensor loop, using a list to allow modification inside callback functions, modify using ColorSensor.running[0] = True or False


    def __init__(self, pin:int, data:list):
        super().__init__(pin, data) # Call the parent constructor to initialize the sensor pin and data list

    """
    Uses RGB_Value, not original sensor value, 
    returns a boolean if the RGB value from the sensor matches the given value tuple (R, G, B)
        Add in margin of error later
    """
    # Override
    # Compares given RGB tuple with current sensor RGB
    def detected(self, value: tuple) -> bool: 
        RGB = self.RGB_Value()
        if RGB == value:
            return True
        else:
            return False
    
    # Override
    def read(self) -> int: # Returns the raw sensor RGB value
        return self.Sensor.value()
    
    # Override
    def get_data_list(self) -> list: # Return the data list containing RGB values collected from the sensor
        return self.data

    def RGB_Value(self) -> tuple: # Returns the RGB value as a tuple (R, G, B)
        value = self.read()
        R = (value >> 16) & 0xFF   # Extract the red value from the sensor reading, moves the value 16 bits to the right and masks with 0xFF to get the last 8 bits
        G = (value >> 8) & 0xFF    # Extract the green value from the sensor reading, moves the value 8 bits to the right and masks with 0xFF to get the last 8 bits
        B = value & 0xFF           # Extract the blue value from the sensor reading, masks with 0xFF to get the last 8 bits
        return (R, G, B) # Return the RGB values as a tuple

    # Override
    def loop_sensor_interval(self, interval: int) -> list: # Loop and return RGB values at a specified interval in milliseconds
        self.loop = True
        self.T.init(period=interval, mode=Timer.ONE_SHOT, callback=lambda t: setattr(self, 'loop', False))  #Stop Loop after interval
        self.data.append([255, 255, 255]) # Marks a break in the data list to indicate a new interval of data collection
        while self.loop:
            time.sleep_ms(100)                   # Sleep for 100 milliseconds
            self.data.append(self.RGB_Value())   # Read the sensor value
        return self.data
    
    # Override
    def loop_sensor_bool(self):
        self.loop = ColorSensor.running[0] # 'ColorSensor.running' is a boolean flag that controls whether the sensor loop should run
        self.data.append([255, 255, 255]) # Marks a break in the data list to indicate a new interval of data collection
        while self.loop:
            time.sleep_ms(100)                   # Sleep for 100 milliseconds
            self.data.append(self.RGB_Value())   # Read the sensor value and add to data list

    # Override 
    # Print list of RGB values collected from the sensor in a formatted string
    def print_data_list(self):
        value = self.get_data_list()
        print("Color Sensore Data List(255, 255, 255 is a break marker):")
        for RGB in value:
            print("Color Sensor Value: R: " + str(RGB[0]) + ", G: " + str(RGB[1]) + ", B: " + str(RGB[2])) # Print the RGB values in a formatted string

    #Override
    def print_data(self): # Print the current RGB value in a formatted string
        value = self.RGB_Value()
        print("Color Sensor Value: R: " + str(value[0]) + ", G: " + str(value[1]) + ", B: " + str(value[2])) # Print the RGB values in a formatted string
