import json
import machine
from machine import Pin, ADC
import time
 

class LDR():
    def __init__(self, pin):
        self.ldr_pin = machine.ADC(Pin(pin), atten=ADC.ATTN_11DB)
        
    def get_raw_value(self):
        return self.ldr_pin.read_u16()
    
    def get_light_percentage(self):
        light =  round(self.get_raw_value()/65535*100,2)
        return {"lightper" : light}
    
class LM35:
    def __init__(self, pin):
        self.ldr_pin = machine.ADC(Pin(pin))
        
    def get_raw_value(self):
        return self.ldr_pin.read_u16()
    
    def get_temp(self):
        return round(self.get_raw_value()/65535*150,2)
 
'''ldr = LDR(15)

while True:
     print(ldr.get_light_percentage())
     time.sleep(1)

     data = {"luz" : ldr.get_light_percentage()}'''
