
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
    Arm_Motor_Pin = 4

    #Create IO for left motor
    In_L_Motor = Pin(L_Motor_Pin, I) # Take signal from Motor Pin
    Out_L_Motor = Pin(L_Motor_Pin, O, drive= Drive_Power) # Send signal to Motor Pin

    #Create IO for right motor
    In_R_Motor = Pin(R_Motor_Pin, I) # Take signal from Motor Pin
    Out_R_Motor = Pin(R_Motor_Pin, O, drive= Drive_Power) # Send signal to Motor Pin

    #Create IO for arm motor
    In_Arm_Motor = Pin(Arm_Motor_Pin, I) # Take signal arm from Motor Pin
    Out_Arm_Motor = Pin(Arm_Motor_Pin, O, drive= Drive_Power) # Send signal to arm Motor Pin

    #Create Timer object, 1000ms - 1s
    T = Timer(0)

    #Initiate function, define parameters for class objects
    def __init__(self):
        pass
    
    #Function to run commands from an array recorded by the recording class
    def runFromArray(self, commands: list):
        pass

    #Hypothetical Methods, NOT ACTUALLY HOW THE MOTORS WILL WORK

    #Turns off current Pin
    def stop(self, pin: Pin):
        pin.off()

    #Move tracks forward
    def forward(self, interval: int):

        Movement.Out_L_Motor.on()   #Forward
        Movement.Out_R_Motor.on()   #Forward

        Movement.T.init(period= interval, mode= Timer.ONE_SHOT, callback= self.stop(self.Out_L_Motor)) #Stop left motor after interval
        Movement.T.init(period= interval, mode= Timer.ONE_SHOT, callback= self.stop(self.Out_R_Motor)) #Stop right motor after interval

    #Move tracks backward
    def backward(self, interval: int):

        Movement.Out_L_Motor.low()  #Reverse
        Movement.Out_R_Motor.low()  #Reverse

        Movement.T.init(period= interval, mode= Timer.ONE_SHOT, callback= self.stop(self.Out_L_Motor)) #Stop left motor after interval
        Movement.T.init(period= interval, mode= Timer.ONE_SHOT, callback= self.stop(self.Out_R_Motor)) #Stop right motor after interval

    #Turn left
    def turn_L(self, interval: int):

        Movement.Out_L_Motor.off()  #Reverse
        Movement.Out_R_Motor.on()   #Forward

        Movement.T.init(period= interval, mode= Timer.ONE_SHOT, callback= self.stop(self.Out_L_Motor)) #Stop left motor after interval
        Movement.T.init(period= interval, mode= Timer.ONE_SHOT, callback= self.stop(self.Out_R_Motor)) #Stop right motor after interval

    #Turn right
    def turn_r(self, interval: int):

        Movement.Out_L_Motor.on()   #Forward
        Movement.Out_R_Motor.off()  #Reverse

        Movement.T.init(period= interval, mode= Timer.ONE_SHOT, callback= self.stop(self.Out_L_Motor)) #Stop left motor after interval
        Movement.T.init(period= interval, mode= Timer.ONE_SHOT, callback= self.stop(self.Out_R_Motor)) #Stop right motor after interval

    

    
