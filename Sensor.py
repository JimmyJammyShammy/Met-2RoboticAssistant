"""
    Project: MET-2ROBOTICASSISTANT
    File:    Sensor.py
    Author:  Justin Tran
    Created: 02/14/2026
    Version: 1.0.0
    Description:
        Sensor class for Met^2 Robotic Assitant Project 2026.
        Contains methods for detecting and returning sensor values to be used as the parent for all sensors in the project.
"""
from abc import ABC, abstractmethod
from machine import Pin
from machine import Timer
import time

class Sensor(ABC):

    T = Timer(0) # Create a timer object for timing functions

    Sensor_Pin = 0 
    Sensor = Pin(Sensor_Pin, Pin.IN) # Set sensor pin as input

    def __init__(self, pin:int):
        self.Sensor_Pin = pin
        self.Sensor = Pin(self.Sensor_Pin, Pin.IN)

    def detected(self, value:int, sensor:Pin) -> bool: # Returns a boolean if the sensor detects the value
        if sensor.value() == value:
            return True
        else:
            return False
    
    @abstractmethod  
    def read(self, sensor:Pin) -> int: # Returns a value from the sensor
        pass

    def loop_sensor_interval(self, interval:int, sensor:Pin) -> list: # Interval in milliseconds
        self.loop = True
        data = []
        self.T.init(period=interval, mode=Timer.ONE_SHOT, callback=lambda t: setattr(self, 'loop', False))  #Stop Loop after interval
        while self.loop:
            time.sleep_ms(100)      # Sleep for 100 milliseconds
            data.append(sensor.value())   # Read the sensor value
        return data    # Return the last sensor value after the loop ends

    def loop_sensor_bool(self, bool:bool, sensor:Pin) -> list: # Loop until boolean value == false
        self.loop = bool
        data = []
        while self.loop:
            time.sleep_ms(100)      # Sleep for 100 milliseconds
            data.append(sensor.value())   # Read the sensor value
        return data 

    @abstractmethod
    def print_data(self, sensor:Pin): # Print formatted data from the sensor
        pass
        