from machine import I2C, Pin, DAC, PWM
from hcsr04 import HCSR04
from time import sleep_ms
import send_readings

sensor = HCSR04(trigger_pin=16, echo_pin=0)

def startReading():
    while True:
        try:
            distance = sensor.distance_cm()  # get the distance
        except Exception as e:
            print("Could not read the distance")
        print('Distance:', distance, 'cm')
        send_readings.send(distance)
        sleep_ms(5000)
