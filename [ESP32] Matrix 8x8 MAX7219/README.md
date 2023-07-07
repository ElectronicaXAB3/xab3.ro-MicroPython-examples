# Display matricial 4 in 1 cu MAX 7219
Display-ul de fata este alcatuit din 4 matrice de cate 64 led-uri, dispuse 8X8, avand fiecare cate un driver MAX 7219. Toate circuitele MAX7219 sunt interconectate intre cu ajutorul interfetei seriale specifice acestui driver. Poate fi pilotat cu usurinta folosind Arduino, iar pentru interconectare se folosesc doar 3 linii de date.

## Detalii tehnice

### ESP32
- CPU: Xtensa dual-core
- Performanta: 160 or 240 MHz si pana la 600 DMIPS
- Memorie: 520 KiB SRAM
- Bluetooth: V4.2 BR/EDR & BLE
- Wi-Fi: 802.11 b/g/n
- Power: 5uA deep sleep

### MAX7219
- Driver: MAX7219
- Culoare fata: negru
- Lentile: Led epoxy ALB (difuze)
- LED-uri: 4 matrice a cate 8x8 
- Culoare LED: rosu
- Alimentare: 5V
- Interfata: Serial- SPI


## Link resurse
- [max7219.py](https://github.com/mcauser/micropython-max7219)
- [MAX7219](https://www.xab3.ro/produse/matrice-4-in-1-max-7219), [ESP32](https://www.xab3.ro/produse/esp32-devkit-wh)