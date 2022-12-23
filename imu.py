import math
import serial
import struct
scaleTime = 0.005
scaleA = (256/2**31) 
scaleW = (512/2**31)
scaleTemp = (128/2**15) 

MY_STRUCT="""typedef struct __attribute__ ((__packed__)){
    uint16_t u16; #header cece
    uint8_t u8; # id
    uint8_t u8; # reserv
    uint32_t u32; # Tsys
    uint16_t u16; # SW
    uint16_t u16; # KW. 12 уже занято
    #Ab Wb 
    int32_t i32; # тут пошли ускорения 32 байта и угловая скорость 32 байта. итого 24 байта занято.
    int32_t i32; 
    int32_t i32;
    int32_t i32;
    int32_t i32;
    int32_t i32; # 36 занято

    #12 нулей каких то iab iwb hfix
    int16_t i16;
    int16_t i16;
    int16_t i16;
    int16_t i16;
    int16_t i16;
    int16_t i16; # 48 занято
    # 6 нулей, возможно магнитометр Magn hfix
    int16_t i16;
    int16_t i16;
    int16_t i16; # 54 занято
    uint16_t u16;# MuxData
    uint8_t u8; #Baro 
    uint8_t u8; # Baro
    uint8_t u8; #Baro
    uint8_t u8; # Reserv2
    uint16_t u16; # CRC16
    uint16_t u16; # Tail 01F0 
} debugInfo;"""

format = 'HBBIHHiiiiiihhhhhhhhhHBBBBHH'
#  B - unsigned char - integer - 1   uint8_t
   # H - unsugned short - integer - 2  uint16_t
   # I - unsigned int - integer - 4   uint32_t
   # L - unsigned long - unteger - 8 
   # l - long - integer - 8   
   # i - int - integer - 4 int32t
   # h - short - integer - 2 int16_t

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
# filename = "test.csv"
bad_chunks = 0
# f = open (filename, 'w')
while True :
# line = ser.read (640)
   line = ser.read_until (expected = b'\x01\xf0',  size = 65)
   if len (line) != 64:
       bad_chunks += 1 
    # f.write (line.hex())
   # f.write('\n')
   else:
       # print (line.hex(' ', 2))
       # print ('number bad chunk :', bad_chunks)
       # print (int.from_bytes (line, 'big'))
       chunk = struct.unpack (format, line)
       chunkTime = scaleTime * chunk [3]
       chunkAx = scaleA * chunk [6]
       chunkAy = scaleA * chunk [7]
       chunkAz = scaleA * chunk [8]
       chunkWx = scaleW * chunk [9]
       chunkWy = scaleW * chunk [10]
       chunkWz = scaleW * chunk [11]
       chunkMuxData = scaleTemp * chunk [21] 
       # print (chunk)
       print ("Time {:9.3f},   ax {:9.4f},  ay {:9.4f},  az {:9.4f},  wx {:9.4f},  wy {:9.4f},  wz {:9.4f},  Temp {:4.2f}".format(chunkTime, chunkAx, chunkAy, chunkAz, chunkWx, chunkWy, chunkWz, chunkMuxData))
       # print ("Time {:9.2f}, wx {:9.4f}, wy {:9.4f}, wz {:9.4f}".format(chunkTime, chunkWx, chunkWy, chunkWz))
       
       # print (chunk[0]) # CECE = 52942. header
       # print (chunk[1]) # 1 Id
       # print (chunk[2]) # 0 Reserv1
       # print (chunk[3]) # System Time
       # print (chunk[4]) # 0 SW
       # print (chunk[5]) # 0 KW
       # print (chunk[6]) # ax?
       # print (chunk[7]) # ay?
       # print (chunk[8]) # az?
       # print (chunk[9]) # wx?
       # print (chunk[10]) # wy?
       # print (chunk[11]) # wz?
       # print (chunk[12]) # 0 ?
       # print (chunk[13]) # 0 ?
       # print (chunk[14]) # 0 ?
       # print (chunk[15]) # 0 ?
       # print (chunk[16]) # 0 ?
       # print (chunk[17]) # 0 ?
       # print (chunk[18]) # 0 Magn?
       # print (chunk[19]) # 0 Magn?
       # print (chunk[20]) # 0 Magn?
       # print (chunk[21]) # MuxData
       # print (chunk[22]) # 0 Baro
       # print (chunk[23]) # 0 Baro
       # print (chunk[24]) # 0 Baro
       # print (chunk[25]) # 0 Reserv2
       # print (chunk[26]) # CRC16
       # print (chunk[27]) # 01F0 = 61441. Tail
ser.close()

