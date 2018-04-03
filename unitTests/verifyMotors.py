# Dr. Kaputa
# Motor test code for ESD II
# spins each motor for 2 seconds. [1,2,3,4]
# note: motors might be connected with varying polarities.  Double check polarity with tracks off

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

# motor 1
mem1.seek(4) 
mem1.write(struct.pack('l', 0))   
mem1.seek(8) 
mem1.write(struct.pack('l', 25000))
mem1.seek(12) 
mem1.write(struct.pack('l', 50000))
mem1.seek(0) 
mem1.write(struct.pack('l', 1))
time.sleep(2)
mem1.seek(0)
mem1.write(struct.pack('l', 0))

# motor 2
mem2.seek(4) 
mem2.write(struct.pack('l', 0))
mem2.seek(8) 
mem2.write(struct.pack('l', 25000))
mem2.seek(12) 
mem2.write(struct.pack('l', 50000))
mem2.seek(0) 
mem2.write(struct.pack('l', 1))
time.sleep(2)
mem2.seek(0)
mem2.write(struct.pack('l', 0))

# motor 3
mem3.seek(4) 
mem3.write(struct.pack('l', 0))
mem3.seek(8) 
mem3.write(struct.pack('l', 25000))
mem3.seek(12) 
mem3.write(struct.pack('l', 50000))
mem3.seek(0) 
mem3.write(struct.pack('l', 1))
time.sleep(2)
mem3.seek(0)
mem3.write(struct.pack('l', 0))

# motor 4
mem4.seek(4) 
mem4.write(struct.pack('l', 0))
mem4.seek(8) 
mem4.write(struct.pack('l', 25000))
mem4.seek(12) 
mem4.write(struct.pack('l', 50000))
mem4.seek(0) 
mem4.write(struct.pack('l', 1))
time.sleep(2)
mem4.seek(0)
mem4.write(struct.pack('l', 0))

mem1.close()
mem2.close()
mem3.close()
mem4.close()
f1.close()
f2.close()
f3.close()
f4.close()
