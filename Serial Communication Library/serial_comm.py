import serial
import time


class Communicate:
    def __init__(self, port=None, baudrate=115200, parity=serial.PARITY_NONE, timeout=None):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.parity = parity

        try:
            self.serial = serial.Serial(port, baudrate, timeout=timeout, parity=parity)
        except serial.SerialException as s:
            print("Connection Failed...\n", s)
            exit(0)

    def is_open(self):
        """
        Checks if the serial port is open.
        :return: True if the serial port is open, False otherwise.
        """
        return self.serial.isOpen()

    def print_result(self, response):
        print(f" Command: {response[0]} \n")
        print(f" Response: \n")

        for i in range(1, len(response) - 1):
            print(f" {response[i]}\n")

    def configure_serial(self, port=None, baudrate=None, parity=None, timeout=None):
        """
        Configures the serial port with the specified parameters.
        :param port: The serial port name (e.g., '/dev/ttyUSB2').
        :param baudrate: The baud rate.
        :param parity: The parity setting.
        :param timeout: The timeout setting.
        """
        if port:
            self.port = port
        if baudrate:
            self.baudrate = baudrate
        if parity:
            self.parity = parity
        if timeout:
            self.timeout = timeout

        try:
            if self.is_open():
                self.serial.close()
            self.serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout, parity=self.parity)
            print(
                f"Updated serial port settings: Port={self.port}, Baudrate={self.baudrate}, Parity={self.parity}, Timeout={self.timeout}")
        except serial.SerialException as s:
            print(f"Error configuring serial port: {s}")

    def send_at_command(self, data):
        """
        Sends an AT command over the serial connection.
        :param data: The AT command to send.
        """
        try:
            if not self.is_open():
                print("Serial port is not open.")
                return None
            data = data + "\r\n"
            self.serial.reset_input_buffer()
            self.serial.write(data.encode())
        except serial.SerialException as s:
            print(f"Error sending AT command: {s}")
            return None

    def get_at_command(self):
        """
        Gets the response from the serial connection after sending an AT command.
        :return: The response received from the serial connection.
        """
        try:
            if not self.is_open():
                print("Serial port is not open.")
                return None
            time.sleep(1)
            response = self.serial.read_all().decode()

            rspn = response.split("\n")
            self.print_result(rspn)

            return rspn[len(rspn) - 2]
        except serial.SerialException as s:
            print(f"Error getting AT command response: {s}")
            return None

    def read_data_HTTP(self):
        self.send_at_command("AT+QHTTPREAD=80")
        time.sleep(2)
        response = self.serial.read_all().decode()
        print(response)

    def get_data_HTTP(self, url):
        self.prep_for_HTTP()

        byte_length = len(url.encode('utf-8'))

        commands = [
            "AT+QIACT?",
            f"AT+QHTTPURL={byte_length},80",
            "AT+QHTTPGET=80"
        ]

        for command in commands:
            self.send_at_command(command)
            result = self.get_at_command().strip()
            if (result == 'CONNECT'):
                time.sleep(3)
                self.send_at_command(url)
                continue
            if (result == 'ERROR'):
                print("Program gives error.\n")
                return None

        print("!!!!!!!! HTTP GET : SUCCESS !!!!!!!!\n")

    def post_data_HTTP(self, url, data):
        data = "Message=" + data
        self.prep_for_HTTP()

        byte_length = len(url.encode('utf-8'))
        data_length = len(data.encode('utf-8'))

        commands = [
            "AT+QIACT?",
            f"AT+QHTTPURL={byte_length},80",
            f"AT+QHTTPPOST={data_length},80,80"
        ]

        for command in commands:
            self.send_at_command(command)
            result = self.get_at_command().strip()
            if (result == 'CONNECT'):
                if ("URL" in command):
                    print("Entering URL")
                    time.sleep(1)
                    self.send_at_command(url)
                    time.sleep(1)
                elif ("POST" in command):
                    print("Entering Data")
                    time.sleep(1)
                    self.send_at_command(data)
                    time.sleep(1)
                self.get_at_command().strip()
            if (result == 'ERROR'):
                print("Program gives error.\n")
                return None

        print("!!!!!!!! HTTP POST : SUCCESS !!!!!!!!\n")

    def prep_for_HTTP(self):
        preps = [
            "AT",
            "AT+QHTTPCFG= \"contextid\",1",
            "AT+QHTTPCFG= \"responseheader\",1",
            "AT+QIACT?",
            "AT+QICSGP=1,1,\"de1.super\",\"\",\"\",1",
            "AT+QIACT=1"
        ]

        for prep in preps:
            self.send_at_command(prep)
            time.sleep(0.5)
            response = self.serial.read_all().decode()

            rspn = response.split("\n")
            self.print_result(rspn)

            if ("+QIACT:" in rspn[1]):
                print("!!!!!!!! Preperations for HTTP is COMPLETED !!!!!!!!\n")
                return None
            if (rspn[len(rspn) - 2].strip() == 'ERROR'):
                print("Program gives error.\n")
                return None

        print("!!!!!!!! Preperations for HTTP is COMPLETED !!!!!!!!\n")

    def communicate_MQTT(self, data="Default Message"):
        data_length = len(data.encode('utf-8'))
        comms = [
            "AT",
            "AT+QMTOPEN=0,\"broker.hivemq.com\",1883",
            "AT+QMTCONN=0,\"Communicate\"",
            "AT+QMTSUB=0,1,\"topic/pub\",0",
            f"AT+QMTPUBEX=0,0,0,0,\"topic/pub\",{data_length}",
            data,
            "AT+QMTDISC=0"
        ]

        for comm in comms:
            self.send_at_command(comm)
            response = self.get_at_command().strip()
            if (response == 'ERROR'):
                print("Program gives error.\n")
                return None
            elif ("QMTSTAT: 0,1" in response):
                print("Program gives error.\n")
                return None

    def close(self):
        """
        Closes the serial communication.
        """
        self.serial.close()
        print("Communication closed...")
