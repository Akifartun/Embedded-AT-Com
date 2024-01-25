import serial_comm

device = serial_comm.Communicate("/dev/ttyUSB2", timeout=5)
http_comm = serial_comm.HTTP_COMM(device)
mqtt_comm = serial_comm.MQTT_COMM(device)

# AT COMMANDS DEMO
# device.send_at_command("AT")
# device.get_at_command()

# device.send_at_command("ATE1")      # Echo open
# device.get_at_command()

# HTTP COMMUNICATION DEMO
# http_comm.post_data_HTTP("https://webhook.site/7a663762-6795-441d-bfb6-574c5fb79916", "Hello from 24.01.2024")
# http_comm.post_data_HTTP("https://webhook.site/7a663762-6795-441d-bfb6-574c5fb79916")
# http_comm.get_data_HTTP("https://webhook.site/7a663762-6795-441d-bfb6-574c5fb79916")

# MQTT COMMUNICATION DEMO
# mqtt_comm.communicate_MQTT("Hello from 23.01.2024.")
# mqtt_comm.communicate_MQTT()

# ECM
# device.send_at_command("AT+QCFG=\"usbnet\"")
# device.get_at_command()
# device.send_at_command("AT+CGDCONT=1,\"IP\",\"de1.super\"")
# device.get_at_command()
# device.send_at_command("AT+QCFG=\"usbnet\",1")
# device.get_at_command()
# device.send_at_command("AT+CFUN=1,1")

device.close()