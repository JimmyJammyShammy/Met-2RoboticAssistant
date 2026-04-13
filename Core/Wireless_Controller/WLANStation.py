import network
import socket
import time
from machine import Pin

# This class is the ESP32 station that connects to the access point created by the AccessPoint class. 
# It can be used to connect to the AP and communicate with it over Wi-Fi. 
# The station can also scan for available networks and check its connection status.
class WirelessController:

    # Check for actual pin numbers later, these are just placeholders for now. 
    # Button pins for manual control of the robot when connected to the access point (The Robot)
    Forward_Button = Pin(12, Pin.IN, Pin.PULL_UP) # Set up a button on pin 12 to control forward movement
    Backward_Button = Pin(14, Pin.IN, Pin.PULL_UP) # Set up a button on pin 14 to control backward movement
    Left_Button = Pin(27, Pin.IN, Pin.PULL_UP) # Set up a button on pin 27 to control left movement
    Right_Button = Pin(26, Pin.IN, Pin.PULL_UP) # Set up a button on pin 26 to control right movement

    wlan = network.WLAN()       # create station interface (the default, see below for an access point interface)
    wlan.ipconfig('addr4')      # get the interface's IPv4 addresses
    
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    
    def connect(self):
        if not self.wlan.isconnected():
            print('Connecting to Access Point...')
            self.wlan.connect(self.ssid, self.password)
            while not self.wlan.isconnected(): # Prints the connection status every 5 seconds until connected
                print(self.wlan.status())
                print(self.wlan.scan()) # Scan for available networks and print the results to the console
                time.sleep(5)
        print('Network connected:', self.wlan.ipconfig())

    def disconnect(self):
        self.wlan.disconnect() # Disconnect from the access point
        print('Disconnected from Access Point')

    def Get_Status(self):
        return self.wlan.status() # Return the current connection status of the station (e.g., connected, connecting, etc.)
    
    def Get_IP(self):
        return self.wlan.ifconfig()[0] # Return the IP address assigned to the station by the access point once connected
    
    def Controller(self):
        # This function will read the state of the buttons and send corresponding commands to the robot over Wi-Fi when connected to the access point. 
        # It will continuously check the button states and send commands as long as the station is connected to the access point.
        while self.wlan.isconnected():
            if not self.Forward_Button.value():
                print("Forward Button Pressed")
                
                try:
                    address = socket.getaddrinfo(self.wlan.ifconfig()[0], 80)[0][-1] # Get the IP address of the station to send commands to the robot
                    s = socket.socket() # Create a new socket for communication
                    s.connect(address) # Connect to the robot's IP address

                    s.send(b'GET /forward HTTP/1.0\r\n\r\n') # Send a command to the robot to move forward
                    s.close() # Close the socket after sending the command
                except Exception as e:
                    print(f"Error sending Forward command: {e}") # Print any errors that occur during the connection or sending process

                time.sleep_ms(200) # Add a small delay to prevent debounce when holding

            if not self.Backward_Button.value():
                print("Backward Button Pressed")

                try:
                    address = socket.getaddrinfo(self.wlan.ifconfig()[0], 80)[0][-1] # Get the IP address of the station to send commands to the robot
                    s = socket.socket() # Create a new socket for communication
                    s.connect(address) # Connect to the robot's IP address

                    s.send(b'GET /forward HTTP/1.0\r\n\r\n') # Send a command to the robot to move forward
                    s.close() # Close the socket after sending the command
                except Exception as e:
                    print(f"Error sending Forward command: {e}") # Print any errors that occur during the connection or sending process

                time.sleep_ms(200) # Add a small delay to prevent debounce when holding
                
            if not self.Left_Button.value():
                print("Left Button Pressed")
                
                try:
                    address = socket.getaddrinfo(self.wlan.ifconfig()[0], 80)[0][-1] # Get the IP address of the station to send commands to the robot
                    s = socket.socket() # Create a new socket for communication
                    s.connect(address) # Connect to the robot's IP address

                    s.send(b'GET /forward HTTP/1.0\r\n\r\n') # Send a command to the robot to move forward
                    s.close() # Close the socket after sending the command
                except Exception as e:
                    print(f"Error sending Forward command: {e}") # Print any errors that occur during the connection or sending process

                time.sleep_ms(200) # Add a small delay to prevent debounce when holding

            if not self.Right_Button.value():
                print("Right Button Pressed")
                
                try:
                    address = socket.getaddrinfo(self.wlan.ifconfig()[0], 80)[0][-1] # Get the IP address of the station to send commands to the robot
                    s = socket.socket() # Create a new socket for communication
                    s.connect(address) # Connect to the robot's IP address

                    s.send(b'GET /forward HTTP/1.0\r\n\r\n') # Send a command to the robot to move forward
                    s.close() # Close the socket after sending the command
                except Exception as e:
                    print(f"Error sending Forward command: {e}") # Print any errors that occur during the connection or sending process

                time.sleep_ms(200) # Add a small delay to prevent debounce when holding

            time.sleep(0.1) # Add a small delay to prevent excessive CPU usage while checking button states

    