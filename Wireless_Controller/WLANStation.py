import network
import machine

# This class is the ESP32 station that connects to the access point created by the AccessPoint class. 
# It can be used to connect to the AP and communicate with it over Wi-Fi. 
# The station can also scan for available networks and check its connection status.
class WirelessController:

    wlan = network.WLAN()       # create station interface (the default, see below for an access point interface)
    wlan.active(True)           # activate the interface
    wlan.scan()                 # scan for access points
    wlan.isconnected()          # check if the station is connected to an AP
    wlan.connect('ssid', 'key') # connect to an AP
    wlan.config('mac')          # get the interface's MAC address
    wlan.ipconfig('addr4')      # get the interface's IPv4 addresses
    
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    

    def connect(self):
        if not self.wlan.isconnected():
            print('Connecting to network...')
            self.wlan.connect(self.ssid, self.password)
            while not self.wlan.isconnected():
                machine.idle()  # save power while waiting
        print('Network connected:', self.wlan.ifconfig())

    