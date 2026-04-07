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
    running = [True] # List to hold the running state of the sensor loop, using a list to allow modification inside callback functions, modify using Sensor.running[0] = True or False
                     # Specific per sensor class, so that each sensor can be controlled independently

    Sensor_Pin = 0 
    Sensor = Pin(Sensor_Pin, Pin.IN) # Set sensor pin as input
    data= []

    def __init__(self, pin:int, data:list):
        self.Sensor_Pin = pin
        self.Sensor = Pin(self.Sensor_Pin, Pin.IN)   
        self.data = data

    def detected(self, value:int) -> bool: # Returns a boolean if the sensor detects the value
        if self.Sensor.value() == value:
            return True
        else:
            return False
    
    def loop_sensor_interval(self, interval:int) -> list: # Interval in milliseconds
        self.loop = True
        self.T.init(period=interval, mode=Timer.ONE_SHOT, callback=lambda t: setattr(self, 'loop', False))  #Stop Loop after interval
        while self.loop:
            time.sleep_ms(100)                      # Sleep for 100 milliseconds
            self.data.append(self.Sensor.value())   # Read the sensor value
        return self.data # Return the list of sensor values collected during the loop
    
    def loop_sensor_bool(self):
        self.loop = Sensor.running[0] # 'Sensor.running' is a boolean flag that controls whether the sensor loop should run
        while self.loop:
            time.sleep_ms(100)                      # Sleep for 100 milliseconds
            self.data.append(self.Sensor.value())   # Read the sensor value and add to data list

    @abstractmethod  
    def read(self) -> int: # Returns a value from the sensor
        pass

    @abstractmethod
    def get_data_list(self): # Return the data list containing values collected from the sensor
        pass

    @abstractmethod
    def print_data_list(self): # Print a list of data collected from the sensor
        pass

    @abstractmethod
    def print_data(self): # Print formatted data from the sensor
        pass
        
