import machine, onewire, ds18x20, time

sensor_pin = machine.Pin(4) #definire pin senzor
sensor = ds18x20.DS18X20(onewire.OneWire(sensor_pin)) #initializare senzor DS18B20 cu ajutorul librariilor DS18X20 si OneWire

sensors_list = sensor.scan() #scanarea tuturor senzorilor de acest tip (pot fi legati mai multi senzori pe acelasi pin)
#returneaza o lista de adrese pentru fiecare senzor

while True:
  sensor.convert_temp() #citire temperatura pentru toti senzorii
  time.sleep_ms(750) #asteptare 750ms pana la afisarea lor
  k = 0 #initializare contor
  for addr in sensors_list: #parcurgerea listei de adrese si afisarea temperaturii din senzorul de pe adresa specifica
    print(k, ":", sensor.read_temp(addr)) #afisarea temperaturii masurate de senzorul de pe adresa addr
    k += 1