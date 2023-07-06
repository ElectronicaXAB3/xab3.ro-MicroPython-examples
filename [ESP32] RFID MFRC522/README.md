# Modul RFID cu MFRC522
Programul, scris in Micropython, are rolul de a citi tagurile si de a verifica daca tagul citit are permisiune de acces (daca se afla intr-un whitelist).

## Detalii tehnice

### ESP32
- CPU: Xtensa dual-core
- Performanta: 160 or 240 MHz si pana la 600 DMIPS
- Memorie: 520 KiB SRAM
- Bluetooth: V4.2 BR/EDR & BLE
- Wi-Fi: 802.11 b/g/n
- Power: 5uA deep sleep

### RFID MFRC522
- Tensiune de lucru: 2.5-3.3V
- Consum: Sleep ≈80uA, Idle ≈10-13mA, Working ≈30-100mA
- Frecventa antena: 13.56 MHz
- Comunicare: UART/I2C/SPI @ 3.3V Logic level
- Carduri suportate: Mifare 1k, 4k, Ultralight, and DesFire,MF1xxS20, MF1xxS70 si MF1xxS50
- Dimensiune cablaj: 40x60mm

## Observatii
Libraria mentionata in [Link resurse](#link-resurse) a fost putin modificata in exemplu, pentru a rula pe platforma ESP32. Mai precis, expresia din structura `elif board == 'esp8266'` a fost modificata in `elif board == 'esp8266' or board == 'esp32'`. Clasa MFRC522 functioneaza atat pentru platforma ESP8266, cat si pentru ESP32, asadar nu exista nicio problema pentru folosirea librariei pe aceasta platforma de dezvoltare.

## Link resurse
- [ESP32](https://www.xab3.ro/produse/esp32-devkit-wh)
- [RFID](https://www.xab3.ro/produse/rfid-rc522)
- [mfrc522.py](https://github.com/wendlers/micropython-mfrc522)