import network
import urequests
import BlynkLib as blynklib
from machine import Pin
from servo import Servo


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

blynk_pin_servo = 1 #virtual pin 1
servo_pin = 22 #gpio 22

wifi = network.WLAN(network.STA_IF) #initializare wifi
wifi.active(True)
wifi.connect(wifi_ssid, wifi_password) #conectare wifi

print("Se incearca conectarea la WiFi. Asigura-te ca ai introdus datele corect.")
while not wifi.isconnected(): #Incercare de conectare la wifi
    pass

print("Conectare reusita.\nIP: ", wifi.ifconfig()) #Afisare mesaj si IP, in cazul in care conexiunea a reusit

blynk = blynklib.Blynk(blynk_token) #initializare blynk

servo = Servo(pin = servo_pin) #initializare servo la pinul GPIO 22

@blynk.on("V" + str(blynk_pin_servo)) #event pentru citirea valorilor de pe platforma, Virtual Pin 1
def servo_read(value):
    #value[0] - numarul citit
    servo.move(int(value[0])) #seteaza unghiul servo-ului la valoarea citita
    

@blynk.on("connected") #event pentru conexiunea la platforma
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')
    blynk.sync_virtual(1)

while True:
    blynk.run()

