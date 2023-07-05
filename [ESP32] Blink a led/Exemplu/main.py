from machine import Pin, Timer
import time

led = Pin(2, Pin.OUT) #definire led pe pinul 2 (led-ul de pe ESP32)

timer = Timer(0) #definire timer
toggle = 1 #variabila pentru starea ledului

def blink(timer): #functie principala
    global toggle #folosirea variabilei globale toggle
    if toggle == 1: #daca toggle == 1 => ledul trebuie stins
        led.value(0) #stingere led
        toggle = 0
    else:
        led.value(1) #aprindere led
        toggle = 1

timer.init(freq=2, mode=Timer.PERIODIC, callback=blink) #time = 1s/freq, in cazul de fata delay-ul e de 500ms.