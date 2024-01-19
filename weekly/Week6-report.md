## Week 6

### MQTT Communication with Modem

#### - Testing MQTT commands on minicom

* First I searched [hivemq](https://www.hivemq.com/mqtt/public-mqtt-broker/) which offers a free mqtt broker. From there I found the link and TCP port to establish MQTT communication. 
* After finding the MQTT broker link and port, I proceeded to test it on minicom. For this test, I referenced the example in [Quectel EG25-G MQTT Application Note](https://www.quectel.com/download_file/82643). The first command I tried on minicom was `AT+QMTOPEN=0, "broker.hivemq.com,1883`. It gave **OK** and **+QMTOPEN: 0,0** as output. But after waiting for a while I got another output and it was **+QMTSTAT: 0,1**. When I investigated this I realized that after opening the connection with `AT+QMTOPEN=0, "broker.hivemq.com,1883` it closes the connection if I don't send **+QMTCONN:** within a certain period of time. So I ran `AT+QMTOPEN=0, "broker.hivemq.com,1883` and `AT+QMTCONN=0, "clientExample"` one after the other. 
* After the `AT+QMTCONN= 0, "clientExample"` command output **OK** and **+QMTCONN: 0,0,0,0"** I knew that it had successfully created the connection. 
* The next step is to **"subscribe "** to a topic. I initially subscribed to **"topic/pub "** in the minicom experiment, but then I tried it with other topicals and it worked fine. I used this command to subscribe to a topical: `AT+QMTSUB= 0,1, "topic/pub",0`. After running the command I got **+QMTSUB: 0,1,0,0,0"** as output, which means it was successful. 
* Now that I have subscribed to a topic, it is time to **"publish "** some data to that topic. For this I used the command `AT+QMTPUBEX= 0,0,0,0,0, "topic/pub",30` where **30** is the **byte length** of the data I want to send. After this command runs successfully, **>** output comes out. After this output, I enter the data I want to send. After entering this data, I get **OK**, **+QMTPUBEX: 0,0,0,0,0** and **+QMTRECV: 0, 0, "topic/pub",30, "This is test data, hello MQTT.** The last of these outputs means that the data I sent worked successfully. 
* Finally, I closed my MQTT connection safely using the `AT+QMTDISC=0` command. This is how I got the output that it was successful **+QMTSTAT: 0.5"**.

Two different successful MQTT connections are shown below.


![full_connection_1](/images/qmt_full_conn_OK.png)
![full_connection_2](/images/qmt_full_conn_OK_2.png)

#### - Developing the Communication with MQTT on Python Library

* After successfully establishing the connection with the miniciom I mentioned above, I started to add this connection to the library I was developing.

```
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
```


* I created a new function for this communication and this function receives a data. If this data is not entered, it returns **"Default Message "** as default value. 
* The function first calculates the length of the input data because we will use this calculation in a future command.
* It stores the libraries to be used later in a directory. 
* It executes these commands in order. If there is a glitch in the execution of this code, it stops executing the code by detecting these errors. 

Below are the working pictures of the library written into the library I developed.

![full_connection_lib_1](/images/lib_qmt_full_input_1.png)
![full_connection_lib_2](/images/lib_qmt_full_input_2.png) 

## Overview of Protocols that Raspberry Pi can Access the Internet via Modem (PPP, QMI/RMNET, ECM)

* Since I finished the MQTT connection without getting too many errors in the week I entered behind the plan I had prepared, I wanted to research and make progress on the remaining 3 protocols in order to move forward. 
* As a result of this research I did, if I summarize all 3 protocols. 
    * **PPP (Point-to-Point Protocol):** It is compatible with the TCP/IP protocol family and usually includes encryption and authentication features. PPP is easy to set up, it is a widely used old protocol.
    ** **QMI/RMNET (Qualcomm MSM Interface/Remote Network Driver Interface):** QMI offers a more accessible and faster connection compared to the PPP protocol. It communicates over USB and uses Qualcomm's proprietary protocols.
    ** **ECM (Ethernet Control Model):** Used in Ethernet-based connections, usually via USB-Ethernet adapters. It establishes a connection via Ethernet adapters over USB.

## Implementing Point-to-Point Protocol 

* While researching about how PPP connection works on Raspberry Pi, I found [the PPP Application Note of the Quectel EG25-G modem](https://www.quectel.com/download_file/1397). I experimented with this document. 
* I learned that I need 3 scripts to provide PPP connection to the modem and [these scripts](https://github.com/Quectel-Community/meta-quectel-community/tree/master/recipes-quectel-community/quectel-ppp/quectel-ppp-0.1) **quectel-chat-connect, quectel-chat-disconnect, quectel-ppp** I found them on github and examined them.
* I updated my connection port and baudrate in **quectel-ppp**. 
* I updated my apn value in **quectel-chat-connect** file. 
* Finally, when I tried to run the scripts with **pppd call quectel-ppp** command, I got **Permission Denied** error and I ran `sudo su` command to solve it. 

![ppp-permission-denied](/images/pppd_call_terminal.png)
* After solving this problem, I ran the **pppd call quectel-ppp** command, but I am getting an error as shown in the picture below and unfortunately I cannot solve it for now. 

![ppp-error](/images/connection_terminated.png)
