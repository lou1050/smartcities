import machine
import utime

LED = machine.Pin(16, machine.Pin.OUT)
BUTTON = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)

nbrbt = 0
LED.value(0)

# Fonction appelée automatiquement à chaque appui sur le bouton
def compte_appui(pin):
    global nbrbt
    nbrbt = nbrbt + 1
    if nbrbt > 2:
        nbrbt = 0

# Configuration de l'interruption sur le front montant
BUTTON.irq(trigger=machine.Pin.IRQ_RISING, handler=compte_appui)

while True:
    if nbrbt == 1:
        LED.value(1)
        utime.sleep(2)
        LED.value(0)
        utime.sleep(2)
        print("vitesse1")
    elif nbrbt == 2:
        LED.value(1)
        utime.sleep(0.5)
        LED.value(0)
        utime.sleep(0.5)
        print("vitesse2")
    else:
        LED.value(0)
        utime.sleep(0.1)
