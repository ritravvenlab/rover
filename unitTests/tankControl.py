# Dr. Kaputa
# Remote control of rover via reciever

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
f5 = open("/dev/mem", "r+b")

mem1 = mmap.mmap(f1.fileno(), 32, offset=0x40001000)
mem2 = mmap.mmap(f2.fileno(), 32, offset=0x40002000)
mem3 = mmap.mmap(f3.fileno(), 32, offset=0x40003000)
mem4 = mmap.mmap(f4.fileno(), 32, offset=0x40004000)
mem5 = mmap.mmap(f5.fileno(), 40, offset=0x40007000)

###############################################################################
# setup motors.  disable.. setup... enable
###############################################################################
# motor 1
mem1.seek(0) 
mem1.write(struct.pack('l', 0))
mem1.write(struct.pack('l', 0))
mem1.write(struct.pack('l', 0))
mem1.write(struct.pack('l', 50000))
mem1.seek(0) 
mem1.write(struct.pack('l', 1))

# motor 2
mem2.seek(0) 
mem2.write(struct.pack('l', 0))
mem2.write(struct.pack('l', 0))
mem2.write(struct.pack('l', 0))
mem2.write(struct.pack('l', 50000))
mem2.seek(0) 
mem2.write(struct.pack('l', 1))

# motor 3
mem3.seek(0) 
mem3.write(struct.pack('l', 0))
mem3.write(struct.pack('l', 0))
mem3.write(struct.pack('l', 0))
mem3.write(struct.pack('l', 50000))
mem3.seek(0) 
mem3.write(struct.pack('l', 1))

# motor 4
mem4.seek(0) 
mem4.write(struct.pack('l', 0))
mem4.write(struct.pack('l', 0))
mem4.write(struct.pack('l', 0))
mem4.write(struct.pack('l', 50000))
mem4.seek(0) 
mem4.write(struct.pack('l', 1))

def readReceiver():
  mem5.seek(0) 
  result1 = struct.unpack('l', mem5.read(4))[0] 
  result2 = struct.unpack('l', mem5.read(4))[0] 
  result3 = struct.unpack('l', mem5.read(4))[0] 
  result4 = struct.unpack('l', mem5.read(4))[0] 
  result5 = struct.unpack('l', mem5.read(4))[0] 
  result6 = struct.unpack('l', mem5.read(4))[0] 
  result7 = struct.unpack('l', mem5.read(4))[0] 
  result8 = struct.unpack('l', mem5.read(4))[0] 
  result9 = struct.unpack('l', mem5.read(4))[0] 
  
  ch1 = (result1 - 1024) /1024.0
  ch2 = (result2 - 1024) / 1024.0
  ch3 = -(result3 - 1024) / 1024.0
  ch4 = (result4 - 1024) / 1024.0 
  ch5 = (result5 - 342) / 1364.0
  ch6 = (result6 - 342) / 1364.0
  ch7 = (result7 - 342) / 682.0
  ch8 = (result8 - 342) / 1364.0
  ch9 = (result9 - 342) / 682.0
  
  if (ch1 > .5):
    leftForward()
  elif (ch1 < -.5):
    leftBackwards()
  else:
    leftStop()
    
  if (ch3 > .5):
    rightForward()
  elif (ch3 < -.5):
    rightBackwards()
  else:
    rightStop()

def leftForward():
  #motor 1
  mem1.seek(4) 
  mem1.write(struct.pack('l', 1))   
  mem1.write(struct.pack('l', 0))

  # motor 2
  mem2.seek(4) 
  mem2.write(struct.pack('l', 1))
  mem2.write(struct.pack('l', 0))
  
def leftBackwards():
  #motor 1
  mem1.seek(4) 
  mem1.write(struct.pack('l', 0))   
  mem1.write(struct.pack('l', 50000))

  # motor 2
  mem2.seek(4) 
  mem2.write(struct.pack('l', 0))
  mem2.write(struct.pack('l', 50000))
  
def leftStop():
  #motor 1
  mem1.seek(4) 
  mem1.write(struct.pack('l', 0))   
  mem1.write(struct.pack('l', 0))

  # motor 2
  mem2.seek(4) 
  mem2.write(struct.pack('l', 0))
  mem2.write(struct.pack('l', 0))

def rightForward():
  #motor 3
  mem3.seek(4) 
  mem3.write(struct.pack('l', 1))   
  mem3.write(struct.pack('l', 0))

  # motor 4
  mem4.seek(4) 
  mem4.write(struct.pack('l', 0))
  mem4.write(struct.pack('l', 50000))
  
def rightBackwards():
  #motor 3
  mem3.seek(4) 
  mem3.write(struct.pack('l', 0))   
  mem3.write(struct.pack('l', 50000))

  # motor 4
  mem4.seek(4) 
  mem4.write(struct.pack('l', 1))
  mem4.write(struct.pack('l', 0))
  
def rightStop():
  #motor 3
  mem3.seek(4) 
  mem3.write(struct.pack('l', 0))   
  mem3.write(struct.pack('l', 0))

  # motor 4
  mem4.seek(4) 
  mem4.write(struct.pack('l', 0))
  mem4.write(struct.pack('l', 0))
  
while(True):
  readReceiver()
 
mem1.close()
mem2.close()
mem3.close()
mem4.close()
mem5.close()
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
