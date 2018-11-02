import serial
import time

Chip = serial.Serial('/dev/tty50', 19200, timeout=3)
print Chip.name

Test = 'Test'.encode('utf-8')
print Test
Chip.write(Test)

x=Chip.read()
print 'The String on the RFID card = ' + x
Chip.close()
