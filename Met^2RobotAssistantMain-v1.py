"""
    Project: Met^2RobotAssistantMain-v1
    File:    Met^2RobotAssistant-v1.py
    Author:  Justin Tran
    Created: 02/02/2026
    Version: 1.0.0
    Description:
        Version 1 of robot main code for Met^2 Robotic Assitant Project 2026.
"""
# Allow for immutable variable type
from typing import final
# MicroPython imports
from machine import Pin
from utime import sleep
class RoboticAssistant:
    
# To Run: Connect ESP32 > run > MicroPico > Run current file on Pico
# VSCode: Press Run at the bottom next to Reset
# Look at MicroPico for more documentation

    """Main class for the Met^2 Robotic Assistant."""
    def main():
        print("Robotic Assistant 2026")


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



