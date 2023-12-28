import serial_comm

device = serial_comm.Communicate("/dev/ttyUSB2", timeout=5)

device.send_at_command("AT")
result = device.get_at_command()
print("Recieved Data: ", result)

device.configure_serial(port="/dev/ttyUSB5")
device.send_at_command("AT")
result = device.get_at_command()
print("Recieved Data: ", result)

device.close()