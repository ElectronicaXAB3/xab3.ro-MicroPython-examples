import dht
import ssd1306
from machine import Pin, Timer, I2C
import time

dht11 = dht.DHT11(Pin(14)) #definire DHT11 pe pin 14
i2c = I2C(sda=Pin(4), scl=Pin(5)) #definire I2C pe SDA = 4, SCL = 5
display = ssd1306.SSD1306_I2C(128, 64, i2c) #initializare display

timer = Timer(0) #initializare timer

def show(temp, hum): #functie pentru afisarea datelor pe display
    display.fill(0) #clear la toate datele afisate anterior
    display.text("Temp: " + str(temp) + " *C", 0, 0, 2) #scriere pe display
    display.text("Hum: " + str(hum) + "%", 0, 15, 2)
    display.show() #afisare

def main(timer):
    dht11.measure() #masurare date de pe DHT11/DHT22
    temp = dht11.temperature() #obtinere date temperatura
    hum = dht11.humidity() #obtinere date umiditate
    show(temp, hum) #afisare temperatura si umiditate pe display

timer.init(freq=2, mode=Timer.PERIODIC, callback=main) #initializare loop pentru functia main()