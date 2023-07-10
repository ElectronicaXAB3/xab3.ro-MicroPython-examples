import network
import urequests
import BlynkLib as blynklib
from machine import Pin, ADC
import time


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

sensor_pin = Pin(32) #definire sensor pe pin 4
adc = ADC(sensor_pin) #initializare ADC pe sensor
adc.atten(adc.ATTN_11DB) #o atenuare a amplificarii ADC cu 11dB pentru a functiona optim la 0.0 - 3.3V

val_referinta = 1.27 #valoarea se refera la voltajul maxim pe care-l transmite senzorul (1.27V) - trebuie testat.

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
    val = adc.read() #citirea valorii din senzor (de la 0 la 4095)
    val = val * (3.3 / 4095) #converitrea in voltaj, folosind regula de trei simpla, pentru a lucra cu numere mai mici
    #procentajul va fi calculat cu regula de trei simpla, val_referinta = 100%, val = x%
    nivel = val * 100 / val_referinta
    nivel = min([nivel, 100]) #exista cazuri particulare cand variabila nivel poate avea o valoare mai mare decat 100.0, iar in acel caz va trebui considerat 100
    blynk.virtual_write(blynk_pin_sensor, int(nivel))
    time.sleep(1)