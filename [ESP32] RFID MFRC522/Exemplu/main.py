from machine import Pin
from mfrc522 import MFRC522
import time

#definire pini
sck = 18
mosi = 23
miso = 19
rst = 22
sda = 21

rfid = MFRC522(sck, mosi, miso, rst, sda) #initializare rfid

whitelist = ("aa5918b1") #lista cu uid-uri ce au permisiune

red_led = Pin(5, Pin.OUT) #initializare red led (exemplu, daca tagul nu are permisiune de acces => red led)
green_led = Pin(4, Pin.OUT) #initializare green led (exemplu, daca tagul are permisiune de acces => green led)

on_value = 0 #valoare pentru permisiune de acces (se poate modifica in functie de modulele de output)
off_value = 1 #valoare pentru lipsa permisiune (se poate modifica in functie de modulele de output)

while True:
    red_led.value(off_value) #oprire leduri
    green_led.value(off_value)
    (stat, tag_type) = rfid.request(rfid.REQIDL) #citire tag
    if stat == rfid.OK:
        (stat, raw_uid) = rfid.anticoll() #citire uid de pe tag
        if stat == rfid.OK: #daca tagul s-a citit corect
            tag = "%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]) #transformarea celor 4 coduri din uid intr-un cod hex si convertirea in string
            #exemplu de cod hex convertit in string se afla la variabila "whitelist".
            
            if tag in whitelist: #daca uid-ul tag-ului se afla in lista tagurilor cu permisiune
                red_led.value(off_value) #ledul verde se aprinde, iar cel rosu se stinge
                green_led.value(on_value)
            else: #in caz contrar, tagul nu are permisiune
                red_led.value(on_value) #ledul rosu se aprinde, iar cel verde se stinge
                green_led.value(off_value)
            time.sleep(1)