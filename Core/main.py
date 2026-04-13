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

import machine
from machine import Pin # Pin class for GPIO control
#import machine  # Import machine module for deepsleep (machine.deepsleep())

try:
    import Movement
except ImportError as e:
    print(f"Error importing Movement module: {e}")


class RoboticAssistant:
# ESP 32 UIDs
    # Get from actual ESP when connected
    Access_Point_UID = b' \xe7\xc8\xbab\xe4' #UID for the Access Point, One with the Dot, this will go in the robot
    Station_UID = b'(\x05\xa5o\xdd\xf0' #UID for the Station, will be the remote

# Pin Definitions 0-19, 21-23, 25-27, 32-39, Check Board documentation for specific names (In discord resources)

    """Main class for the Met^2 Robotic Assistant."""
    @staticmethod
    def main():
        uid = machine.unique_id() # Get unique ID of the ESP32 for identification
        print("Unique ID:", uid) # Print the unique ID to the console
        
        if(uid == RoboticAssistant.Access_Point_UID):
            print("Access Point Initialized")
        if(uid == RoboticAssistant.Station_UID):
            print("Station Initialized")

        print("HELLOOOOOOOOO")

        try:
            RoboticAssistant.init() # Call the initialization function to set up the robot's components
        except Exception as e:
            print(f"Error during initialization: {e}")
        
        
 
        """
        Color_Sensor = ColorSensor(34, []) # Create instance of ColorSensor class on pin 34 with an empty data list

        Color_Sensor.running[0] = True # Set the running flag for the color sensor loop to True to start collecting data
        Color_Sensor.loop_sensor_bool() # Start the color sensor loop that collects RGB values and adds them to the data list while .running[0] is True
        """"""
        # Initial Line Following
        """
        """
        Set direction to forward
        While blue is detected, keep moving forward
        If blue not deteced, spin right until blue is detected again
        If red is deteced or blue is not detected for 5 seconds, stop movement entirely and stop the color sensor loop
        """
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

        """
    @staticmethod
    def init():
        global Main_Movement
        Main_Movement = Movement.Movement() # Create instance of Movement class
        Main_Movement.setup()
                
        
       



if __name__ == "__main__":
    RoboticAssistant.main() # Run the main function of the RoboticAssistant class on startup

    



