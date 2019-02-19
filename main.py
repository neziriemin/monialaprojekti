import connect_wifi
import distance_sensor

def main():
    connect_wifi.main()
    distance_sensor.startReading()

main()
