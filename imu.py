import math
import serial
import time

ser = serial.Serial ('/dev/ttyUSB0')
ser.baudrate = 3000000
# ser.timeout = 0.003
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = serial.EIGHTBITS
# ser.set_buffer_size (rx_size = 32768, tx_size = 512)

# ser.timeout = 0
# ser.parity = serial.PARITY_EVEN

print (ser)

print (math.e)

# filename = "GPS-%4d-%02d-%02d-%02d-%02d-%02d.csv" % time.localtime()[0:6]
filename = "test.csv"
bad_chunks = 0
f = open (filename, 'w')
while True :
# line = ser.read (640)
    line = ser.read_until (expected = b'\x01\xf0',  size = 65)
    if len (line) != 64:
       bad_chunks += 1 
    f.write (line.hex())
    f.write('\n')
    print (line.hex(' ', 2))
    print ('number bad chunk :', bad_chunks)
    # print (ser)

ser.close()
