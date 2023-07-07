from machine import Pin
import time

senzor_pin = Pin(4, Pin.IN) #definire senzor PIR pe pinul GPIO 4
releu_pin = Pin(23, Pin.OUT) #definire releu pe pinul GPIO 23

time_on = 0 #variabila pentru stocarea timpului cand senzorul a detectat ultima miscare
now = 0 #variabila pentru stocarea timpului curent
while True:
    now = time.time() #obtinerea timpului curent
    if senzor_pin.value() == 1: #daca senzorul a detectat miscare
        releu_pin.value(1) #ON relay
        time_on = now #stocam timpul de la ultima miscare
    else: #daca nu s-a detectat nicio miscare
        if now - time_on >= 5: #daca au trecut 5 secunde (de pilda) de la ultima miscare, releul va fi oprit
            releu_pin.value(0) #OFF relay
    time.sleep(0.1)
