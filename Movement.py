
from machine import Pin # Pin class for GPIO control
from machine import Timer # Timer class for timing functions
from machine import ADC # ADC class for analog to digital conversion
class Movement:

    # Pin modes
    O = Pin.OUT 
    I = Pin.IN
    Drive_Power = Pin.DRIVE_2 #PLEASE CHECK 20mA / 30 ohm

    #Place Holder Numbers
    #Motor Pin Numbers
    L_Motor_Pin = 2 
    R_Motor_Pin = 3 

    #Create IO for left motor
    In_L_Motor = Pin(L_Motor_Pin, I) # Take signal from Motor Pin
    Out_L_Motor = Pin(L_Motor_Pin, O, value= 0, drive= Drive_Power) # Send signal to Motor Pin

    #Create IO for right motor
    In_R_Motor = Pin(R_Motor_Pin, I) # Take signal from Motor Pin
    Out_R_Motor = Pin(R_Motor_Pin, O, value= 0, drive= Drive_Power) # Send signal to Motor Pin

    #Create Timer object, 1000ms - 1s
    T = Timer(0)

    #Initiate function, define parameters for class objects
    def __init__(self):
        pass
    
    

    #Hypothetical Methods, NOT ACTUALLY HOW THE MOTORS WILL WORK

    #Turns off current Pin
    def stop(pin: Pin):
        pin.off()

    #Move tracks forward
    def forward(interval: int):

        Movement.Out_L_Motor.on()   #Forward
        Movement.Out_R_Motor.on()   #Forward

        Movement.T.init(period= interval, mode= Timer.ONE_SHOT, callback= Movement.stop())

    #Move tracks backward
    def backward(interval: int):

        Movement.Out_L_Motor.low()  #Reverse
        Movement.Out_R_Motor.low()  #Reverse

        Movement.T.init(period= interval, mode= Timer.ONE_SHOT, callback= Movement.stop())

    #Turn left
    def turn_L(interval: int):

        Movement.Out_L_Motor.off()  #Reverse
        Movement.Out_R_Motor.on()   #Forward

        Movement.T.init(period= interval, mode= Timer.ONE_SHOT, callback= Movement.stop())

    #Turn right
    def turn_r(interval: int):

        Movement.Out_L_Motor.on()   #Forward
        Movement.Out_R_Motor.off()  #Reverse

        Movement.T.init(period= interval, mode= Timer.ONE_SHOT, callback= Movement.stop())

    

    
