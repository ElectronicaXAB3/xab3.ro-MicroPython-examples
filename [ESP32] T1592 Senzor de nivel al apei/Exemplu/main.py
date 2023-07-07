from machine import Pin, ADC
import time

sensor = Pin(4) #definire senzor pe pin 4

adc = ADC(sensor) #initializare senzor ca ADC
adc.atten(adc.ATTN_11DB) #o atenuare a amplificarii ADC cu 11dB pentru a functiona optim la 0.0 - 3.3V

val_referinta = 1.27 #valoarea se refera la voltajul maxim pe care-l transmite senzorul (1.27V) - trebuie testat.

while True:
    val = adc.read() #citirea valorii din senzor (de la 0 la 4095)
    val = val * (3.3 / 4095) #converitrea in voltaj, folosind regula de trei simpla, pentru a lucra cu numere mai mici
    #procentajul va fi calculat cu regula de trei simpla, val_referinta = 100%, val = x%
    nivel = val * 100 / val_referinta
    print(nivel, "%")
    time.sleep(1)
    