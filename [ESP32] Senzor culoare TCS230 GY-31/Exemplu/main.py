from machine import Pin, Timer
import time

#initializare pini
S0 = Pin(4, Pin.OUT)
S1 = Pin(5, Pin.OUT)
S2 = Pin(18, Pin.OUT)
S3 = Pin(19, Pin.OUT)
OUT = Pin(21, Pin.IN)

#setarea frecventei la 20%
# 0% => S0 = S1 = 0
# 2% => S0 = 0, S1 = 1
# 20% => S0 = 1, S1 = 0
# 100% => S0 = S1 = 1
S0.value(1)
S1.value(1)

#setarea culorii pentru care vom citi frecventa
#red: S2 = S3 = 0
#green: S2 = S3 = 1
#blue: S2 = 0, S3 = 1
#clear: S2 = 1, S3 = 0

def set_color(color):
    if color == "red":
        S2.value(0)
        S3.value(0)
    elif color == "green":
        S2.value(1)
        S3.value(1)
    elif color == "blue":
        S2.value(0)
        S3.value(1)
    else:
        S2.value(1)
        S3.value(0)

def read_color(color): #functie pentru citirea frecventelor unei culori
    count = 0 #numarul rezultat din frecvente de la 0 la 255
    set_color(color) #setare culoare
    for i in range(8): #transformarea frecventei in nr
        count += ( 2 ** i ) * OUT.value()
    return count

def main():
    color = (255,255,255)
    for _ in range(5): #minimul de frecventa a 3 citiri
        red = read_color("red") #citire red
        time.sleep(0.1)
        green = read_color("green") #citire green
        time.sleep(0.1)
        blue = read_color("blue") #citire blue
        time.sleep(0.1)
        set_color("clear") #clear filter
        color = (min(color[0], red), min(color[1], green), min(color[2], blue)) #minimul a 3 citiri
    print(color)

while True:
    main()
    time.sleep(0.5)