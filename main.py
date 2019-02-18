import connect_wifi
import distance_censor

def main():
    connect_wifi.main()
    distance_censor.startReading()

main()
