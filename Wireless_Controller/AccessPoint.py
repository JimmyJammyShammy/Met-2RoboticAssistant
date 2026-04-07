import network
import machine

class AccessPoint:

    
    def __init__(self, ssid='ESP-AP', max_clients=1):
        self.ap = network.WLAN(network.WLAN.IF_AP)
        self.ap.config(ssid=ssid)
        self.ap.config(max_clients=max_clients)
        self.ap.active(True)

    
