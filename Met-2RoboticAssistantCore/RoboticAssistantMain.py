"""
    Project: MET-2ROBOTICASSISTANT
    File:    RoboticAssistantMain.py
    Author:  Justin Tran
    Created: 02/02/2026
    Version: 1.0.0
    Description:
        Main class for Met^2 Robotic Assistant Project 2026.
"""
# MicroPython imports
    # Some imports will be removed if not used, but are included for future functionality and testing
from Sensors.ColorSensor import ColorSensor
from machine import Pin # Pin class for GPIO control
from machine import Timer # Timer class for timing functions
from machine import ADC # ADC class for analog to digital conversion
from machine import SoftSPI # Software SPI communication (Serial Peripheral Interface)
from machine import SPI # Hardware SPI communication
from machine import SoftI2C # Software I2C communication (Inter-Integrated Circuit)
from machine import I2C # Hardware I2C communication
from machine import RTC # Real Time Clock class for tracking time
import machine  # Import machine module for deepsleep (machine.deepsleep())
from utime import sleep # Sleep function for delays
import time  # For timing the blue detection period

# Class Imports
import Movement # Import Movement class for controlling robot movement

class RoboticAssistant:
# To Run: Connect ESP32 > run > MicroPico > Run current file on Pico
# VSCode: Press Run at the bottom next to Reset
# Look at MicroPico for more documentation

# ESP 32 UIDs
    # Get from actual ESP when connected
    Access_Point_UID = b'\x00\x00\x00\x00\x00\x00' # Placeholder UID for the Access Point, will be set to the actual UID of the ESP32 when the Access Point is initialized
    Station_UID = b'\x00\x00\x00\x00\x00\x00' # Placeholder UID for the Station, will be set to the actual UID of the ESP32 when the Station is initialized

# Pin modes
    O = Pin.OUT 
    I = Pin.IN

# Pin Definitions 0-19, 21-23, 25-27, 32-39, Check Board documentation for specific names (In discord resources)

    """Main class for the Met^2 Robotic Assistant."""
    @staticmethod
    def main():
        uid = machine.unique_id() # Get unique ID of the ESP32 for identification
        print("Unique ID:", uid) # Print the unique ID to the console

        Main_Movement = Movement.Movement() # Create instance of Movement class
        Main_Movement.setup() # Set up pins and directions for movement

        Color_Sensor = ColorSensor(34, []) # Create instance of ColorSensor class on pin 34 with an empty data list

        Color_Sensor.running[0] = True # Set the running flag for the color sensor loop to True to start collecting data
        Color_Sensor.loop_sensor_bool() # Start the color sensor loop that collects RGB values and adds them to the data list while .running[0] is True

        # Initial Line Following
        """
        Set direction to forward
        While blue is detected, keep moving forward
        If blue not deteced, spin right until blue is detected again
        If red is deteced or blue is not detected for 5 seconds, stop movement entirely and stop the color sensor loop
        """
        while(Color_Sensor.running): #While color sensor is on
            Main_Movement.set_dir("forward", "tracks") # Set movement direction to forward for both tracks
            while(Color_Sensor.detected((0, 0, 255))): # Detects blue
                Main_Movement.movement_loop(Main_Movement.Def_Delay) # Call the movement loop function with Def_Delay: 500 us 
                last_blue_detected = time.time()  # Get last time blue was found 
            if(not Color_Sensor.detected((0, 0, 255))): # If blue is not detected
                Main_Movement.set_dir("right", "tracks")
                while(not Color_Sensor.detected((0, 0, 255))): # While blue is not detected
                    Main_Movement.movement_loop(Main_Movement.Def_Delay) # Spins right until blue is detected again
                    if(Color_Sensor.detected((255, 0, 0)) or (time.time() - last_blue_detected > 5)): # Stop if red detected or blue not detected for 5 seconds
                        Main_Movement.stop() # Stop movement if red is detected or blue lost for too long
                        Color_Sensor.running[0] = False # Stop the color sensor loop

        
            

                
        
       



if __name__ == "__main__":
    RoboticAssistant.main() # Run the main function of the RoboticAssistant class on startup

    



