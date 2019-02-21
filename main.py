import connect_wifi
import distance_sensor
import send_readings

def main():
    connect_wifi.main()
    #distance_sensor.startReading()
    send_readings.send("testimuuttuja")


main()
