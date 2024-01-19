import serial_comm

device = serial_comm.Communicate("/dev/ttyUSB2", timeout=5)

#device.send_at_command("ATE1")
device.communicate_MQTT("Hello from Main. 18.01.2024")

device.close()