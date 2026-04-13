import network
import socket
from Movement import Movement

class AccessPoint:

    def __init__(self):
        self.ap = network.WLAN(network.WLAN.IF_AP)  # Create access point interface
        self.ap.config(ssid='ESP-AP')               # Set the SSID of the access point to 'ESP-AP'
        self.ap.config(max_clients=1)               # Limit the number of clients that can connect to the access point to 1 for simplicity and security
        self.ap.config(password='robot')            # Set a password for the access point to prevent unauthorized access
        self.ap.active(True)                        # Activate the access point interface to start broadcasting the SSID and allowing clients to connect

        if Movement is None:
            print("Movement module not found")
            return
        else:
            self.ApMovement = Movement() # Create instance of Movement class to control the robot's movement based on commands received from the station
            self.ApMovement.setup() # Set up the movement controller

    def Get_Connected_Clients(self):
        return self.ap.status('stations') # Return a list of connected clients to the access point
    
    def Open_Socket(self):
        # Open a socket to listen for commands
        s = socket.socket() # Create a new socket for communication
        s.bind(('0.0.0.0', 80)) # Bind the socket to port 80 to listen for incoming connections on that port
        s.listen(1) # Listen for incoming connections, allowing only 1 connection at a time for simplicity
        print('Waiting for a connection...') # Print a message to the console indicating that the access point is waiting for a connection from the station

        client, address = s.accept() # Accept an incoming connection from a client (the station) and get the client's socket and address information
        print('Client connected from:', address) # Print the address of the connected client
        
        global command
        command = client.recv(1024).decode() # Receive data from the client (the station) and decode it from bytes to a string for processing
        print('Received Command:', command) # Print the received command to the console for debugging purposes

    def Get_Command(self): # Listen for commands from station
        while self.ap.status('stations'): # Check if there are any clients currently connected to the access point
            if "/forward" in command: # If a command is received from the station to move forward
                self.ApMovement.set_dir("forward", "tracks") # Set the movement direction to forward for both tracks
                while "/forward" in command: # Continue moving forward as long as the forward command is being received from the station
                    self.ApMovement.movement_loop(self.ApMovement.Def_Delay) # Call the movement loop function with Def_Delay: 500 us to keep the robot moving forward
            elif "/backward" in command: # If a command is received from the station to move backward
                self.ApMovement.set_dir("backward", "tracks") # Set the movement direction to backward for both tracks
                while "/backward" in command: # Continue moving backward as long as the backward command is being received from the station
                    self.ApMovement.movement_loop(self.ApMovement.Def_Delay) # Call the movement loop function with Def_Delay: 500 us to keep the robot moving backward
            elif "/left" in command: # If a command is received from the station to turn left
                self.ApMovement.set_dir("left", "tracks") # Set the movement direction to left for both tracks to turn the robot left
                while "/left" in command: # Continue turning left as long as the left command is being received from the station
                    self.ApMovement.movement_loop(self.ApMovement.Def_Delay) # Call the movement loop function with Def_Delay: 500 us to keep the robot turning left
            elif "/right" in command: # If a command is received from the station to turn right
                self.ApMovement.set_dir("right", "tracks") # Set the movement direction to right for both tracks to turn the robot right
                while "/right" in command: # Continue turning right as long as the right command is being received from the station
                    self.ApMovement.movement_loop(self.ApMovement.Def_Delay) # Call the movement loop function with Def_Delay: 500 us to keep the robot turning right
            else:
                self.ApMovement # If an unrecognized command is received, stop the robot's movement for safety