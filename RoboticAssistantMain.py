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

# Class Imports
import Movement # Import Movement class for controlling robot movement

class RoboticAssistant:
# To Run: Connect ESP32 > run > MicroPico > Run current file on Pico
# VSCode: Press Run at the bottom next to Reset
# Look at MicroPico for more documentation

# Pin modes
    O = Pin.OUT 
    I = Pin.IN

# Pin Definitions 0-19, 21-23, 25-27, 32-39, Check Board documentation for specific names (In discord resources)

    """Main class for the Met^2 Robotic Assistant."""
    @staticmethod
    def main():
        Main_Movement = Movement.Movement() # Create instance of Movement class
        Main_Movement.setup() # Set up pins and directions for movement

        Main_Movement.forward(2000, Main_Movement.Def_Delay) # Move forward for 2 seconds at Def_Delay, 500 microseconds delay between steps


if __name__ == "__main__":
    RoboticAssistant.main() # Run the main function of the RoboticAssistant class on startup

    



