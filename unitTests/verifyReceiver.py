# Dr. Kaputa
# Receiver test code for ESD II

import time
import mmap
import struct

# open dev mem and see to base address
f = open("/dev/mem", "r+b")
mem = mmap.mmap(f.fileno(), 40, offset=0x40007000)

while(True):
  mem.seek(0) 
  result1 = struct.unpack('l', mem.read(4))[0] 
  result2 = struct.unpack('l', mem.read(4))[0] 
  result3 = struct.unpack('l', mem.read(4))[0] 
  result4 = struct.unpack('l', mem.read(4))[0] 
  result5 = struct.unpack('l', mem.read(4))[0] 
  result6 = struct.unpack('l', mem.read(4))[0] 
  result7 = struct.unpack('l', mem.read(4))[0] 
  result8 = struct.unpack('l', mem.read(4))[0] 
  result9 = struct.unpack('l', mem.read(4))[0] 
  
  ch1 = (result1 - 1024) /1024.0
  ch2 = (result2 - 1024) / 1024.0
  ch3 = -(result3 - 1024) / 1024.0
  ch4 = (result4 - 1024) / 1024.0 
  ch5 = (result5 - 342) / 1364.0
  ch6 = (result6 - 342) / 1364.0
  ch7 = (result7 - 342) / 682.0
  ch8 = (result8 - 342) / 1364.0
  ch9 = (result9 - 342) / 682.0
  
  print "ch 1 [counts]: " + str(ch1)
  print "ch 2 [counts]: " + str(ch2)
  print "ch 3 [counts]: " + str(ch3)
  print "ch 4 [counts]: " + str(ch4)
  print "ch 5 [counts]: " + str(ch5)
  print "ch 6 [counts]: " + str(ch6)
  print "ch 7 [counts]: " + str(ch7)
  print "ch 8 [counts]: " + str(ch8)
  print "ch 9 [counts]: " + str(ch9)
  print ""
  
  time.sleep(1)

mem.close()
f.close()