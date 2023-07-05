import network
import urequests
import BlynkLib as blynklib
from machine import Pin
import dht

dht11 = dht.DHT11(Pin(13)) #declarare modul la pinul GPIO 13

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

blynk_pin_temp = 0 #virtual pin 0
blynk_pin_hum = 2 #virtual pin 2

wifi = network.WLAN(network.STA_IF) #initializare wifi
wifi.active(True)
wifi.connect(wifi_ssid, wifi_password) #conectare wifi

print("Se incearca conectarea la WiFi. Asigura-te ca ai introdus datele corect.")
while not wifi.isconnected(): #Incercare de conectare la wifi
    pass

print("Conectare reusita.\nIP: ", wifi.ifconfig()) #Afisare mesaj si IP, in cazul in care conexiunea a reusit

blynk = blynklib.Blynk(blynk_token) #initializare blynk

@blynk.on("connected") #event pentru conexiunea la platforma
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')


while True:
    blynk.run()
    try:
        dht11.measure() #masurare umiditate si temperatura
        blynk.virtual_write(blynk_pin_temp, dht11.temperature()) #afisare temperatura pe virtual pin 0
        blynk.virtual_write(blynk_pin_hum, dht11.humidity()) #afisare umiditate pe virtual pin 2
        
    except:
        pass
