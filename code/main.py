import FinalDriftSquad
from FinalDriftSquad import sample
from time import sleep_ms

p2 = Pin(2, Pin.OUT) # on board LED
p13 = Pin(13, Pin.OUT)
p14 = Pin(14, Pin.OUT)
p13.value(0)
p14.value(1)

p12 = Pin(12, Pin.IN)

if p12.value()==1:
    while True:
        p2.value(0)
        sample()
        p2.value(1)
        sleep_ms(10000)