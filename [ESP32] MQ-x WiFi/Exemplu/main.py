import network
import urequests
import BlynkLib as blynklib
from machine import Pin

# configurari WiFi
wifi_ssid = ""
wifi_password = ""

if len(wifi_ssid) == 0 or len(wifi_password) == 0: #verificare daca datele pentru wifi sunt completate
    print("!!! wifi_ssid sau wifi_password nu trebuie sa fie goale.")
    while True:
        pass

#configurare platforma Blynk
blynk_token = ''
if len(blynk_token) == 0: #verificare daca datele pentru wifi sunt completate
    print("!!! blynk_token nu trebuie sa fie gol.")
    while True:
        pass


blynk_pin_sensor = 0 #virtual pin 0

sensor = Pin(34, Pin.IN) #definire senzor pe pinul GPIO 34


wifi = network.WLAN(network.STA_IF) #initializare wifi
wifi.active(True)
wifi.connect(wifi_ssid, wifi_password) #conectare wifi


print("Se incearca conectarea la WiFi. Asigura-te ca ai introdus datele corect.")
while not wifi.isconnected(): #Incercare de conectare la wifi
    pass

print("Conectare reusita.\nIP: ", wifi.ifconfig()) #Afisare mesaj si IP, in cazul in care conexiunea a reusit


blynk = blynklib.Blynk(blynk_token, insecure=True) #initializare blynk

def sensor_write():
    value = sensor.value() #citire valoare digitala => 1 = gaz nedetectat, 0 = gaz detectat
    blynk.virtual_write(blynk_pin_sensor, 0 if value else 1) #scriere pe platforma blynk (1 va fi afisat daca gazul este detectat)
    

@blynk.on("connected") #event pentru conexiunea la platforma
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')

while True:
    blynk.run()
    sensor_write()


