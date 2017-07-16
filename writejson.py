import json
import serial
import time

name = 1
dict = {}
f = open('test.json','w')
s = serial.Serial('/dev/ttyACM0',9600)
for num in range(100):
    str = s.read(5)
    dict[name] = str
    name += 1

print dict

json.dump(dict,f,ensure_ascii=False,sort_keys=True,indent=4)
