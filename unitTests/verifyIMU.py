# Dr. Kaputa
# IMU test code for ESD II

import time
import mmap
import struct

# 32768 is 2g => 16384 is 1g 
# 32768 is 500dps => 16.384 is 1dps 
    
# slv_reg0    -- x accel
# slv_reg1    -- y accel
# slv_reg2    -- z accel
# slv_reg3    -- wx
# slv_reg3    -- wy
# slv_reg3    -- wz

# open dev mem and see to base address
f = open("/dev/mem", "r+b")
mem = mmap.mmap(f.fileno(), 32, offset=0x40006000)

while(True): 
  mem.seek(0) 
  result1 = struct.unpack('l', mem.read(4))[0] 
  mem.seek(4) 
  result2 = struct.unpack('l', mem.read(4))[0] 
  mem.seek(8) 
  result3 = struct.unpack('l', mem.read(4))[0] 
  mem.seek(12) 
  result4 = struct.unpack('l', mem.read(4))[0] 
  mem.seek(16) 
  result5 = struct.unpack('l', mem.read(4))[0] 
  mem.seek(20) 
  result6 = struct.unpack('l', mem.read(4))[0] 

  if result1 >  32767: 
    result1 = -1 * (65536 - result1)
  if result2 >  32767: 
    result2 = -1 * (65536 - result2)
  if result3 >  32767: 
    result3 = -1 * (65536 - result3)
  if result4 >  32767: 
    result4 = -1 * (65536 - result4)
  if result5 >  32767: 
    result5 = -1 * (65536 - result5)
  if result6 >  32767: 
    result6 = -1 * (65536 - result6)
 
  ax = result1/16384.0
  ay = result2/16384.0
  az = result3/16384.0
  wx = result4/65.536
  wy = result5/65.536
  wz = result6/65.536

  print "ax [g]: " + str(ax)
  print "ay [g]: " + str(ay)
  print "az [g]: " + str(az)
  print "wx [dps]: " + str(wx)
  print "wy [dps]: " + str(wy)
  print "wz [dps]: " + str(wz)
  print "" 
  time.sleep(1)
  
mem.close()
f.close()