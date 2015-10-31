import serial
port = serial.Serial("/dev/ttyAMA0", baudrate = 19200, timeout = 2)
port.write("SELFT")
port.write("\r")
port.close()

port = serial.Serial("/dev/ttyAMA0", baudrate = 19200, timeout = 2)
data = port.read(100)
print data
print "fuck"