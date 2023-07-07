import max7219
from machine import Pin, SPI
import time

spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2)) #definire SPI, CLK = pin 4, DIN = pin 2
cs = Pin(5, Pin.OUT) #definire CS pin 5
nr_matrix = 4 #definire numar matrixi pe modul (de pilda 4)
display = max7219.Matrix8x8(spi, cs, nr_matrix) #initializare modul


def show(text): #functie pentru afisarea unui text
    display.fill(0) #curatare afisaj
    display.text(text[:nr_matrix],0,0,1)  #pe matrice incap 4 litere (in cazul exemplului cu matrixe 4 in 1)
    display.show() #afisare text

while True:
    show('xab3')