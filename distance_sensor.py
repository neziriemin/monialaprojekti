from machine import I2C, Pin, DAC, PWM
from hcsr04 import HCSR04
from time import sleep_ms

sensor = HCSR04(trigger_pin=16, echo_pin=0)

def startReading():
    while True:
        distance = sensor.distance_cm()  # get the distance
        print('Distance:', distance, 'cm')
        sleep_ms(5000)
