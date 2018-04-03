# Dr. Kaputa
# Encoder test code for ESD II

import time
import mmap
import struct

# pwm_enable            <= slv_reg0(0);
# pwm_dir               <= slv_reg1(0);
# pwm_duty              <= slv_reg2(26 downto 0);
# pwm_period            <= slv_reg3(26 downto 0);
# slv_reg4              <= encoder_blips;

# open dev mem and see to base address
f1 = open("/dev/mem", "r+b")
f2 = open("/dev/mem", "r+b")
f3 = open("/dev/mem", "r+b")
f4 = open("/dev/mem", "r+b")
mem1 = mmap.mmap(f1.fileno(), 32, offset=0x40001000)
mem2 = mmap.mmap(f2.fileno(), 32, offset=0x40002000)
mem3 = mmap.mmap(f3.fileno(), 32, offset=0x40003000)
mem4 = mmap.mmap(f4.fileno(), 32, offset=0x40004000)

encoder1 = 0
encoder2 = 0
encoder3 = 0
encoder4 = 0

while(True):
  time.sleep(1) 
  mem1.seek(16) 
  mem2.seek(16) 
  mem3.seek(16) 
  mem4.seek(16) 
  oldEncoder1 = encoder1
  oldEncoder2 = encoder2
  oldEncoder3 = encoder3
  oldEncoder4 = encoder4
  
  encoder1 = struct.unpack('l', mem1.read(4))[0] 
  encoder2 = struct.unpack('l', mem2.read(4))[0] 
  encoder3 = struct.unpack('l', mem3.read(4))[0] 
  encoder4 = struct.unpack('l', mem4.read(4))[0] 
  
  deltaEncoder1 = encoder1 - oldEncoder1
  deltaEncoder2 = encoder2 - oldEncoder2
  deltaEncoder3 = encoder3 - oldEncoder3
  deltaEncoder4 = encoder4 - oldEncoder4
  
  print "encoder 1 [ticks]: " + str(deltaEncoder1)
  print "encoder 2 [ticks]: " + str(deltaEncoder2)
  print "encoder 3 [ticks]: " + str(deltaEncoder3)
  print "encoder 4 [ticks]: " + str(deltaEncoder4)
  print ""

mem1.close()
mem2.close()
mem3.close()
mem4.close()
f1.close()
f2.close()
f3.close()
f4.close()