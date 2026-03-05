"""
    Project: MET-2ROBOTICASSISTANT
    File:    Movement.py
    Author:  Justin Tran
    Created: 02/14/2026
    Version: 1.0.0
    Description:
        Movement class for Met^2 Robotic Assitant Project 2026.
        Contains methods for controlling the movement of the robot
"""
from machine import Pin # Pin class for GPIO control
from machine import Timer # Timer class for timing functions
import time # Time module for sleep functions

class Movement:
# Pin Definitions 0-19, 21-23, 25-27, 32-39, Check Board documentation for specific names
    # Pin modes
    O = Pin.OUT 
    I = Pin.IN
    Drive_Power = Pin.DRIVE_2 #PLEASE CHECK 20mA / 30 ohm

    #Place Holder Numbers
    #Motor Pin Numbers
    #Left Motor Pins
    L_Motor_EnaPin = 2      # Enable Pin, turns on motor when low
    L_Motor_DirPin = 5      # Direction Pin, low(0) clockwise, high(1) counterclockwise
    L_Motor_PulPin = 6      # Pulse Pin, step when high, off when low

    #Right Motor Pins
    R_Motor_EnaPin = 3      # Enable Pin, turns on motor when low
    R_Motor_DirPin = 7      # Direction Pin, low(0) clockwise, high(1) counterclockwise
    R_Motor_PulPin = 8      # Pulse Pin, step when high, off when low

    #Arm Motor Pins
    Arm_Motor_EnaPin = 4    # Enable Pin, turns on motor when low
    Arm_Motor_DirPin = 9    # Direction Pin, low(0) clockwise, high(1) counterclockwise
    Arm_Motor_PulPin = 10   # Pulse Pin, step when high, off when low

    #Create IO for left motor
    In_L_EnaPin = Pin(L_Motor_EnaPin, I)        # Take signal from Enable Pin
    In_L_DirPin = Pin(L_Motor_DirPin, I)        # Take signal from Direction Pin
    In_L_PulPin = Pin(L_Motor_PulPin, I)        # Take signal from Pulse Pin

    Out_L_EnaPin = Pin(L_Motor_EnaPin, O)       # Send signal to Enable Pin
    Out_L_DirPin = Pin(L_Motor_DirPin, O)       # Send signal to Direction Pin
    Out_L_PulPin = Pin(L_Motor_PulPin, O)       # Send signal to Pulse Pin

    #Create IO for right motor
    In_R_EnaPin = Pin(R_Motor_EnaPin, I)        # Take signal from Enable Pin
    In_R_DirPin = Pin(R_Motor_DirPin, I)        # Take signal from Direction Pin
    In_R_PulPin = Pin(R_Motor_PulPin, I)        # Take signal from Pulse Pin

    Out_R_EnaPin = Pin(R_Motor_EnaPin, O)       # Send signal to Enable Pin
    Out_R_DirPin = Pin(R_Motor_DirPin, O)       # Send signal to Direction Pin
    Out_R_PulPin = Pin(R_Motor_PulPin, O)       # Send signal to Pulse Pin

    #Create IO for arm motor
    In_Arm_EnaPin = Pin(Arm_Motor_EnaPin, I)    # Take signal from Enable Pin
    In_Arm_DirPin = Pin(Arm_Motor_DirPin, I)    # Take signal from Direction Pin
    In_Arm_PulPin = Pin(Arm_Motor_PulPin, I)    # Take signal from Pulse Pin

    Out_Arm_EnaPin = Pin(Arm_Motor_EnaPin, O)   # Send signal to Enable Pin
    Out_Arm_DirPin = Pin(Arm_Motor_DirPin, O)   # Send signal to Direction Pin
    Out_Arm_PulPin = Pin(Arm_Motor_PulPin, O)   # Send signal to Pulse Pin

    #Create Timer object, 1000ms - 1s
    T = Timer(0)

    """
    Setup Function
    Defaults:
    Left Motor: Forward (Counter Clockwise), Enabled
    Right Motor: Forward (Clockwise), Enabled
    Arm Motor: Clockwise, Enabled
    """
    def setup(self):
        #Turn on and set direction of motors
        Movement.Out_L_EnaPin.value(0)      # Enable left motor
        Movement.Out_L_DirPin.value(1)      # Set left motor direction to forward
        
        Movement.Out_R_EnaPin.value(0)      # Enable right motor
        Movement.Out_R_DirPin.value(0)      # Set right motor direction to forward

        Movement.Out_Arm_EnaPin.value(0)    # Enable arm motor
        Movement.Out_Arm_DirPin.value(0)    # Set arm motor direction to clockwise
    
    def disable_motor(self, pin: str):
        #Stop all motors
        if pin == "left":
            Movement.Out_L_EnaPin.value(1)      # Disable left motor
        elif pin == "right":
            Movement.Out_R_EnaPin.value(1)      # Disable right motor
        elif pin == "arm":
            Movement.Out_Arm_EnaPin.value(1)    # Disable arm motor
        else:
            print("Invalid pin. Use 'left', 'right', or 'arm'.")

    def enable_motor(self, pin: str):
        #Enable all motors
        if pin == "left":
            Movement.Out_L_EnaPin.value(0)      # Enable left motor
        elif pin == "right":
            Movement.Out_R_EnaPin.value(0)      # Enable right motor
        elif pin == "arm":
            Movement.Out_Arm_EnaPin.value(0)    # Enable arm motor
        else:
            print("Invalid pin. Use 'left', 'right', or 'arm'.")

    """
    Movement Functions
    Interaval in milliseconds (1000ms = 1s)
    Delay in microseconds (1.000.000us = 1s)

    Default Intervals: 5000ms (5s)
    Default Delay: 500us (Adjust for speed, lower is faster)
    """

    #Default Intervals
    Def_Interval = 5000 #Default interval of 5000 milliseconds (5s)
    Fast_Interval = 2000 #Short interval of 2000 milliseconds (2s)
    Slow_Interval = 10000 #Long interval of 10000 milliseconds (10s)

    #Default Delays
    Def_Delay = 500 #Default delay of 500 microseconds 
    Fast_Delay = 100 #Fast delay of 100 microseconds
    Slow_Delay = 1000 #Slow delay of 1000 microseconds (1ms)


    #Set Pin Direction
    """
    Direction Options:
    For Tracks: foward, backward, left, right
    For Arm: clockwise, counterclockwise
    """
    def set_dir(self, direction: str, part: str):
        if part == "tracks":
            if direction == "forward":
                self.Out_L_DirPin.value(1)      # Set left motor direction to forward
                self.Out_R_DirPin.value(0)      # Set right motor direction to forward
            elif direction == "backward":
                self.Out_L_DirPin.value(0)      # Set left motor direction to backward
                self.Out_R_DirPin.value(1)      # Set right motor direction to backward
            elif direction == "left":
                self.Out_L_DirPin.value(0)      # Set left motor direction to backward
                self.Out_R_DirPin.value(0)      # Set right motor direction to forward
            elif direction == "right":
                self.Out_L_DirPin.value(1)      # Set left motor direction to forward
                self.Out_R_DirPin.value(1)      # Set right motor direction to backward
            else:
                print("Invalid direction for tracks. Use 'forward', 'backward', 'left', or 'right'.")
        elif part == "arm":
            if direction == "clockwise":
                self.Out_Arm_DirPin.value(0)    # Set arm motor direction to clockwise
            elif direction == "counterclockwise":
                self.Out_Arm_DirPin.value(1)    # Set arm motor direction to counterclockwise
            else:
                print("Invalid direction for arm. Use 'clockwise' or 'counterclockwise'.")
        else:
            print("Invalid part. Use 'tracks' or 'arm'.")

    #For use within a loop
    #Must change direction manually before calling this function
    def movement_loop(self, delay: int):
            self.Out_L_PulPin.value(1)      # Left On
            self.Out_R_PulPin.value(1)      # Right On
            time.sleep_us(delay)            # Delay between steps in microseconds, adjust for speed
            self.Out_L_PulPin.value(0)      # Left Off
            self.Out_R_PulPin.value(0)      # Right Off
            time.sleep_us(delay)            # Delay

    """
    Movement Functions with Interval
    These functions need a specific interval for how long the robot will move
    """
    #Move tracks forward
    def forward(self, interval: int, delay: int):
        self.loop = True
        while self.loop:
            self.Out_L_PulPin.value(1)      # Left Forward
            self.Out_R_PulPin.value(1)      # Right Forward
            time.sleep_us(delay)            # Delay between steps in microseconds, adjust for speed
            self.Out_L_PulPin.value(0)      # Left Off
            self.Out_R_PulPin.value(0)      # Right Off
            time.sleep_us(delay)            # Delay
        
        self.T.init(period= interval, mode= Timer.ONE_SHOT, callback= lambda t: setattr(self, 'loop', False)) #Stop Loop after interval

    #Move tracks backward
    def backward(self, interval: int, delay: int):
        self.loop = True

        self.Out_L_DirPin.value(0)          # Set left motor direction to backward
        self.Out_R_DirPin.value(1)          # Set right motor direction to backward

        while self.loop:
            self.Out_L_PulPin.value(1)      # Left Backward
            self.Out_R_PulPin.value(1)      # Right Backward
            time.sleep_us(delay)            # Delay between steps in microseconds, adjust for speed
            self.Out_L_PulPin.value(0)      # Left Off
            self.Out_R_PulPin.value(0)      # Right Off
            time.sleep_us(delay)            # Delay
        
        self.T.init(period= interval, mode= Timer.ONE_SHOT, callback= lambda t: setattr(self, 'loop', False)) #Stop Loop after interval

    #Turn left
    def turn_L(self, interval: int, delay: int):
        self.loop = True

        self.Out_L_DirPin.value(0)          # Set left motor direction to backward
        self.Out_R_DirPin.value(0)          # Set right motor direction to forward

        while self.loop:
            self.Out_L_PulPin.value(1)      # Left Forward
            self.Out_R_PulPin.value(1)      # Right Forward
            time.sleep_us(delay)            # Delay between steps in microseconds, adjust for speed
            self.Out_L_PulPin.value(0)      # Left Off
            self.Out_R_PulPin.value(0)      # Right Off
            time.sleep_us(delay)            # Delay
        
        self.T.init(period= interval, mode= Timer.ONE_SHOT, callback= lambda t: setattr(self, 'loop', False)) #Stop Loop after interval
        
    #Turn right
    def turn_r(self, interval: int, delay: int):
        self.loop = True

        self.Out_L_DirPin.value(0)          # Set left motor direction to backward
        self.Out_R_DirPin.value(0)          # Set right motor direction to forward

        while self.loop:
            self.Out_L_PulPin.value(1)      # Left Forward
            self.Out_R_PulPin.value(1)      # Right Forward
            time.sleep_us(delay)            # Delay between steps in microseconds, adjust for speed
            self.Out_L_PulPin.value(0)      # Left Off
            self.Out_R_PulPin.value(0)      # Right Off
            time.sleep_us(delay)            # Delay
        
        self.T.init(period= interval, mode= Timer.ONE_SHOT, callback= lambda t: setattr(self, 'loop', False)) #Stop Loop after interval

    

    
