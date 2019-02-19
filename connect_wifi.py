from time import sleep_ms
import network
import micropython
from hcsr04 import HCSR04


SSID = "embbubembbu"
PASSWORD = "teretulemasta"
wlan = None

def connectWifi(ssid, passwd):  # Con§nect to wifi

    wlan = network.WLAN(network.STA_IF)  # creating a object
    wlan.active(True)  # Activating the interface
    wlan.disconnect()  # Disconnect the last wifi connection
    wlan.connect(ssid, passwd)  # connect wifi
    while(wlan.ifconfig()[0] == '0.0.0.0'):  # wait for connection
        sleep_ms(1000)
    sleep_ms(1000)  # wait for 1 second
    print("Wifi connected.")

def main():

    try:
        connectWifi(SSID, PASSWORD)

    except Exception as e:
        print('Error %s' % e)
    sensor = HCSR04(trigger_pin=16, echo_pin=0)

main()
