###############################################################################
## Motor Encoder Constraints                                                  #
###############################################################################
## Motor 1 encoder constraints
set_property PACKAGE_PIN K17 [get_ports M1_ENC1]
set_property IOSTANDARD LVCMOS33 [get_ports M1_ENC1]

#set_property PACKAGE_PIN K18 [get_ports M1_ENC2]
#set_property IOSTANDARD LVCMOS33 [get_ports M1_ENC2]

## Motor 2 encoder constraints
set_property PACKAGE_PIN M19 [get_ports M2_ENC1]
set_property IOSTANDARD LVCMOS33 [get_ports M2_ENC1]

#set_property PACKAGE_PIN M20 [get_ports M2_ENC2]
#set_property IOSTANDARD LVCMOS33 [get_ports M2_ENC2]

## Motor 3 encoder constraints
set_property PACKAGE_PIN R17 [get_ports M3_ENC1]
set_property IOSTANDARD LVCMOS33 [get_ports M3_ENC1]

#set_property PACKAGE_PIN R16 [get_ports M3_ENC2]
#set_property IOSTANDARD LVCMOS33 [get_ports M3_ENC2]

## Motor 4 encoder constraints
set_property PACKAGE_PIN P16 [get_ports M4_ENC1]
set_property IOSTANDARD LVCMOS33 [get_ports M4_ENC1]

#set_property PACKAGE_PIN P15 [get_ports M4_ENC2]
#set_property IOSTANDARD LVCMOS33 [get_ports M4_ENC2]

###############################################################################
## Motor Control Constraints                                                  #
###############################################################################
## Motor 1 motor control constraints
set_property PACKAGE_PIN K19 [get_ports M1_IN1]
set_property IOSTANDARD LVCMOS33 [get_ports M1_IN1]

set_property PACKAGE_PIN J19 [get_ports M1_IN2]
set_property IOSTANDARD LVCMOS33 [get_ports M1_IN2]

## Motor 2 motor control constraints
set_property PACKAGE_PIN K14 [get_ports M2_IN1]
set_property IOSTANDARD LVCMOS33 [get_ports M2_IN1]

set_property PACKAGE_PIN J14 [get_ports M2_IN2]
set_property IOSTANDARD LVCMOS33 [get_ports M2_IN2]

## Motor 3 motor control constraints
set_property PACKAGE_PIN W16 [get_ports M3_IN1]
set_property IOSTANDARD LVCMOS33 [get_ports M3_IN1]

set_property PACKAGE_PIN V16 [get_ports M3_IN2]
set_property IOSTANDARD LVCMOS33 [get_ports M3_IN2]

## Motor 4 motor control constraints
set_property PACKAGE_PIN W19 [get_ports M4_IN1]
set_property IOSTANDARD LVCMOS33 [get_ports M4_IN1]

set_property PACKAGE_PIN W18 [get_ports M4_IN2]
set_property IOSTANDARD LVCMOS33 [get_ports M4_IN2]

###############################################################################
## LED Constraints                                                            #
###############################################################################
## LED 1 constraints
set_property PACKAGE_PIN G18 [get_ports LED1]
set_property IOSTANDARD LVCMOS33 [get_ports LED1]

## LED 2 constraints
set_property PACKAGE_PIN G19 [get_ports LED2]
set_property IOSTANDARD LVCMOS33 [get_ports LED2]

## LED 3 constraints
set_property PACKAGE_PIN G20 [get_ports LED3]
set_property IOSTANDARD LVCMOS33 [get_ports LED3]

###############################################################################
## Ultrasonic Sensor Constraints                                              #
###############################################################################
## US1
set_property PACKAGE_PIN Y19 [get_ports US1_TRIG_3v3]
set_property IOSTANDARD LVCMOS33 [get_ports US1_TRIG_3v3]

set_property PACKAGE_PIN Y18 [get_ports US1_ECHO_3v3]
set_property IOSTANDARD LVCMOS33 [get_ports US1_ECHO_3v3]

## US2
set_property PACKAGE_PIN P19 [get_ports US2_TRIG_3v3]
set_property IOSTANDARD LVCMOS33 [get_ports US2_TRIG_3v3]

set_property PACKAGE_PIN N18 [get_ports US2_ECHO_3v3]
set_property IOSTANDARD LVCMOS33 [get_ports US2_ECHO_3v3]

## US3
set_property PACKAGE_PIN J16 [get_ports US3_TRIG_3v3]
set_property IOSTANDARD LVCMOS33 [get_ports US3_TRIG_3v3]

set_property PACKAGE_PIN K16 [get_ports US3_ECHO_3v3]
set_property IOSTANDARD LVCMOS33 [get_ports US3_ECHO_3v3]

###############################################################################
## MPU9250 Constraints                                                        #
###############################################################################
## MPU1
set_property PACKAGE_PIN L14 [get_ports mpu9250_1_scl_io]
set_property IOSTANDARD LVCMOS33 [get_ports mpu9250_1_scl_io]

set_property PACKAGE_PIN L15 [get_ports mpu9250_1_sda_io]
set_property IOSTANDARD LVCMOS33 [get_ports mpu9250_1_sda_io]

## MPU2
set_property PACKAGE_PIN N20 [get_ports mpu9250_2_scl_io]
set_property IOSTANDARD LVCMOS33 [get_ports mpu9250_2_scl_io]

set_property PACKAGE_PIN P20 [get_ports mpu9250_2_sda_io]
set_property IOSTANDARD LVCMOS33 [get_ports mpu9250_2_sda_io]

###############################################################################
## Receiver Constraints                                                       #
###############################################################################
set_property PACKAGE_PIN N17 [get_ports RECEIVER]
set_property IOSTANDARD LVCMOS33 [get_ports RECEIVER]

###############################################################################
## ADC Constraints                                                            #
###############################################################################
#set_property PACKAGE_PIN L19 [get_ports MAX_CNVST_N]
#set_property IOSTANDARD LVCMOS33 [get_ports MAX_CNVST_N]

#set_property PACKAGE_PIN L20 [get_ports MAX_EOC_N]
#set_property IOSTANDARD LVCMOS33 [get_ports MAX_EOC_N]

#set_property PACKAGE_PIN M17 [get_ports MAX_CS_N]
#set_property IOSTANDARD LVCMOS33 [get_ports MAX_CS_N]

#set_property PACKAGE_PIN M18 [get_ports MAX_MOSI]
#set_property IOSTANDARD LVCMOS33 [get_ports MAX_MOSI]

#set_property PACKAGE_PIN L16 [get_ports MAX_MISO]
#set_property IOSTANDARD LVCMOS33 [get_ports MAX_MISO]

#set_property PACKAGE_PIN L17 [get_ports MAX_SCLK]
#set_property IOSTANDARD LVCMOS33 [get_ports MAX_SCLK]