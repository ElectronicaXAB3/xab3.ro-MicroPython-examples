from hx711 import HX711

hx711 = HX711(5, 4) #definire senzor DT = 5, SCK = 4

hx711.tare() #initializare
while True:
    value = hx711.read() #citire valoare, trebuie calibrat.
    value = hx711.get_value()
    #value = ... --- valoarea trebuie calibrata
    print(value) #afisare valoare