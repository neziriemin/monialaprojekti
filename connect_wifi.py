from time import sleep_ms
import network

SSID = "Jungle"
PASSWORD = "pillu123"
wlan = None

try:
    
    def connectWifi(ssid, passwd):  # Connect to wifi

        wlan = network.WLAN(network.STA_IF)  # creating a object
        wlan.active(True)  # Activating the interface
        wlan.disconnect()  # Disconnect the last wifi connection
        wlan.connect(ssid, passwd)  # connect wifi
        while(wlan.ifconfig()[0] == '0.0.0.0'):  # wait for connection
            sleep_ms(1)
        sleep_ms(1000)  # hold on for 1 second
        print("Wifi connected.")

    def main():

        connectWifi(SSID, PASSWORD)
         sensor = HCSR04(trigger_pin=16, echo_pin=0)

    main()

except Exception as e:
    print('Error %s' % e)
