"""
    Project: Met^2RobotAssistantMain-v1
    File:    Met^2RobotAssistant-v1.py
    Author:  Justin Tran
    Created: 02/02/2026
    Version: 1.0.0
    Description:
        Version 1 of robot main code for Met^2 Robotic Assitant Project 2026.
"""
# MicroPython imports
from machine import Pin # Pin class for GPIO control
from machine import Timer # Timer class for timing functions
from machine import ADC # ADC class for analog to digital conversion
from machine import SoftSPI # Software SPI communication (Serial Peripheral Interface)
from machine import SPI # Hardware SPI communication
from machine import SoftI2C # Software I2C communication (Inter-Integrated Circuit)
from machine import I2C # Hardware I2C communication
from machine import RTC # Real Time Clock class for trachking time
from machine import DEEPSLEEP # Deep sleep mode for turning off the robot
from utime import sleep # Sleep function for delays


class RoboticAssistant:
    
# To Run: Connect ESP32 > run > MicroPico > Run current file on Pico
# VSCode: Press Run at the bottom next to Reset
# Look at MicroPico for more documentation

# Pin modes
    O = Pin.OUT 
    I = Pin.IN

# Pin Definitions 0-19, 21-23, 25-27, 32-39, Check Board documentation for specific names
    # Pass in pin number and mode
    p0 = Pin(0, O)  # Output on GPIO0 (Pin 0)
    LED = Pin("LED", O)  # Onboard LED pin


    """Main class for the Met^2 Robotic Assistant."""
    def main():
        # Setup LED pin to flash
        pin = Pin("LED", Pin.OUT)

        print("LED starts flashing...")
        while True:
            try:
                pin.value(not pin.value())
                sleep(1) # sleep 1sec
            except KeyboardInterrupt:
                break
        pin.off()
        print("Finished.")
        



        


    main()



