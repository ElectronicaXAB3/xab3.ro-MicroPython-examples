from machine import Pin, Timer, I2C
from hcsr04 import HCSR04
import ssd1306
import time

timer = Timer(0) #initializare timer
senzor = HCSR04(trigger_pin=22, echo_pin=23)
i2c = I2C(sda=Pin(4), scl=Pin(5)) #definire I2C pe SDA = 4, SCL = 5
display = ssd1306.SSD1306_I2C(128, 64, i2c) #initializare display

def show(dist): #functie pentru afisarea datelor pe display
    display.fill(0) #clear la toate datele afisate anterior
    display.text("Distanta: " + str(dist) + " cm", 0, 0, 2) #scriere pe display
    display.show() #afisare

def main(timer):
    distance = senzor.distance_cm()
    show(int(distance))

timer.init(freq=2, mode=Timer.PERIODIC, callback=main) #initializare loop pentru functia main()
