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
                return
            data = data + "\r\n"
            self.serial.write(data.encode())
        except serial.SerialException as s:
            print(f"Error sending AT command: {s}")

    def get_at_command(self):
        """
        Gets the response from the serial connection after sending an AT command.

        :return: The response received from the serial connection.
        """
        try:
            if not self.is_open():
                print("Serial port is not open.")
                return
            time.sleep(2)
            response = self.serial.read_all().decode()
            return response
        except serial.SerialException as s:
            print(f"Error getting AT command response: {s}")
            return None

    def close(self):
        """
        Closes the serial communication.
        """
        self.serial.close()
        print("Communication closed...")
