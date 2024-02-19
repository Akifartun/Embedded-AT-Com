import time
import serial


class Communicate:
    def __init__(
        self, port=None, baudrate=115200, parity=serial.PARITY_NONE, timeout=None
    ):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.parity = parity

        try:
            self.serial = serial.Serial(port, baudrate, timeout=timeout, parity=parity)
        except serial.SerialException as s:
            print("Connection Failed...\n", s)
            return None

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
            self.serial = serial.Serial(
                self.port, self.baudrate, timeout=self.timeout, parity=self.parity
            )
            print(
                f"Updated serial port settings: "
                f"Port={self.port}, "
                f"Baudrate={self.baudrate}, "
                f"Parity={self.parity}, T"
                f"imeout={self.timeout}"
            )
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

    def is_open(self):
        """
        Checks if the serial port is open.
        :return: True if the serial port is open, False otherwise.
        """
        return self.serial.isOpen()

    def print_result(self, response):
        """
        Prints the result of the AT command.
        :param response: AT command response.
        :return: None
        """
        print(f" Command: {response[0]} \n")
        print(" Response: \n")

        for i in range(1, len(response) - 1):
            print(f" {response[i]}\n")

    def close(self):
        """
        Closes the serial communication.
        """
        self.serial.close()
        print("Communication closed...")


class HttpComm:
    def __init__(self, comm):
        self.comm = comm

    def prep_for_http(self):
        """
        Makes presets for HTTP communication.
        :return: None
        """
        preps = [
            "AT",
            'AT+QHTTPCFG= "contextid",1',
            'AT+QHTTPCFG= "responseheader",1',
            "AT+QIACT?",
            'AT+QICSGP=1,1,"de1.super","","",1',
            "AT+QIACT=1",
        ]

        for prep in preps:
            self.comm.send_at_command(prep)
            time.sleep(0.5)
            response = self.comm.serial.read_all().decode()

            rspn = response.split("\n")
            self.comm.print_result(rspn)

            if "+QIACT:" in rspn[1]:
                print("!!!!!!!! Preperations for HTTP is COMPLETED !!!!!!!!\n")
                return None
            if rspn[len(rspn) - 2].strip() == "ERROR":
                print("Program gives error.\n")
                return None

        print("!!!!!!!! Preperations for HTTP is COMPLETED !!!!!!!!\n")

    def get_data_http(self, url):
        """
        Makes HTTP GET request from the specified URL.
        :param url: URL to make GET request.
        :return: None
        """
        self.prep_for_http()

        byte_length = len(url.encode("utf-8"))

        commands = ["AT+QIACT?", f"AT+QHTTPURL={byte_length},80", "AT+QHTTPGET=80"]

        for command in commands:
            self.comm.send_at_command(command)
            result = self.comm.get_at_command().strip()
            if result == "CONNECT":
                time.sleep(1)
                self.comm.send_at_command(url)
                time.sleep(1)
            if result == "ERROR":
                print("Program gives error.\n")
                return None
        time.sleep(1)

        rspn = self.read_data_http()
        if "ERROR" in rspn[len(rspn) - 2]:
            print("Program gives error.\n")
            return None
        else:
            print("!!!!!!!! HTTP GET : SUCCESS !!!!!!!!\n")

    def post_data_http(self, url, data="Default Message"):
        """
        Makes HTTP POST request to the specified URL.
        :param url: URL to make POST request.
        :param data: POST data (default value: "Default Message").
        :return: None
        """
        data = "Message=" + data
        self.prep_for_http()

        byte_length = len(url.encode("utf-8"))
        data_length = len(data.encode("utf-8"))

        commands = [
            "AT+QIACT?",
            f"AT+QHTTPURL={byte_length},80",
            f"AT+QHTTPPOST={data_length},80,80",
        ]

        for command in commands:
            self.comm.send_at_command(command)
            result = self.comm.get_at_command().strip()
            if result == "CONNECT":
                if "URL" in command:
                    print("Entering URL")
                    time.sleep(1)
                    self.comm.send_at_command(url)
                    time.sleep(1)
                    self.comm.get_at_command().strip()
                elif "POST" in command:
                    print("Entering Data")
                    time.sleep(1)
                    self.comm.send_at_command(data)
                    time.sleep(1)
                    self.comm.get_at_command().strip()
            if result == "ERROR":
                print("Program gives error.\n")
                return None
        time.sleep(1)

        rspn = self.read_data_http()
        if "ERROR" in rspn[len(rspn) - 2]:
            print("Program gives error.\n")
            return None
        print("!!!!!!!! HTTP GET : SUCCESS !!!!!!!!\n")

    def read_data_http(self):
        """
        Reads data over HTTP.
        :return: Data read over HTTP.
        """
        print("\n !!!!!! READING DATA !!!!!!\n\n")
        self.comm.send_at_command("AT+QHTTPREAD=80")
        time.sleep(2)
        response = self.comm.serial.read_all().decode()
        rspn = response.split("\n")
        for i in range(1, len(rspn) - 1):
            print(f" {rspn[i]}\n")
        return rspn


class MqttComm:
    def __init__(self, comm):
        self.comm = comm

    def communicate_mqtt(self, data="Default Message"):
        """
        Performs MQTT communication.
        :param data: MQTT transmitted data (default value: "Default Message").
        :return: None
        """
        data_length = len(data.encode("utf-8"))
        commands = [
            "AT",
            'AT+QMTOPEN=0,"broker.hivemq.com",1883',
            'AT+QMTCONN=0,"Communicate"',
            'AT+QMTSUB=0,1,"topic/pub",0',
            f'AT+QMTPUBEX=0,0,0,0,"topic/pub",{data_length}',
            data,
            "AT+QMTDISC=0",
        ]

        for command in commands:
            self.comm.send_at_command(command)
            response = self.comm.get_at_command().strip()
            if "RECV" in response:
                print("!!!!!! Message succesfully recieved. !!!!!!")
                time.sleep(2)
            if response == "ERROR":
                print("Program gives error.\n")
                return None
            elif "QMTSTAT: 0,1" in response:
                print("Program gives error.\n")
                return None
