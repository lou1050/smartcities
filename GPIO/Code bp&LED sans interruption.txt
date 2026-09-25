import machine
import utime

LED = machine.Pin(16,machine.Pin.OUT)
BUTTON = machine.Pin(18,machine.Pin.IN)
val = 0
nbrbt = 0
LED.value(0)

while True:
    if BUTTON.value() == 1:
        nbrbt = nbrbt+1
        
    while BUTTON.value() == 1:
        utime.sleep(0.01)
    
    if nbrbt == 1:
        LED.value(1)
        utime.sleep(2)
        LED.value(0)
        utime.sleep(2)
    elif nbrbt == 2:
        print("looser")
    elif nbrbt ==3:
        nbrbt=0
