# Dr. Kaputa
# Ultrasonic test code for ESD II

import time
import mmap
import struct

# slv_reg0    -- sync     [bit 0]    -- 0
# slv_reg1    -- ultrasonic1
# slv_reg2    -- ultrasonic2
# slv_reg3    -- ultrasonic3

# open dev mem and see to base address
f = open("/dev/mem", "r+b")
mem = mmap.mmap(f.fileno(), 32, offset=0x40008000)

while(True): 
  mem.seek(0) 
  mem.write(struct.pack('l', 1))
  time.sleep(1) 
  mem.seek(4) 
  result1 = struct.unpack('l', mem.read(4))[0] 
  mem.seek(8) 
  result2 = struct.unpack('l', mem.read(4))[0] 
  mem.seek(12) 
  result3 = struct.unpack('l', mem.read(4))[0] 
  
  # microseconds / 59 is distance in cmp
  # every tick is 20 ns.
  distance1 = (result1/50.0)/59.0
  distance2 = (result2/50.0)/59.0
  distance3 = (result3/50.0)/59.0
  
  print "distance 1 [cm]: " + str(distance1)
  print "distance 2 [cm]: " + str(distance2)
  print "distance 3 [cm]: " + str(distance3)
  print ""

mem.close()
f.close()
