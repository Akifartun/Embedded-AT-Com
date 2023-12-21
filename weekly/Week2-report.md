## Week 2
									Akif Artun 21.12.2023

### Reinstalling with Raspberry Pi Imager
* Thanks to a [video](https://www.youtube.com/watch?v=nZyyfJYOhbM&t=137s) I discovered that in order to make SSH and VNC connections for Raspberry Pi, I first need to make some settings with the Raspberry Pi Imager. The steps from here on are made with reference to this video.

* First of all, I entered the SSH setting and WI-FI information from the Raspberry Pi Imager setup screen as shown in the picture below. (Unfortunately, I could not upload it because I could not upload images).

* After making these settings, I switched to SSH and VNC connection.

### Connecting to Raspberry Pi with SSH and VNC
*	Raspberry Pi works like a computer with mouse, screen and keyboard. But since I was using a laptop, it was not easy to access this hardware. Therefore, I had to activate the SSH protocol, one of the protocols that provides remote access to the Raspberry Pi. SSH allows me to remotely access the command line screen of the Raspberry Pi. For SSH and VNC connection, it must be on the same WI-FI. For the SSH connection, I typed *ssh akif@ipaddress* on the command line on my computer and then entered the password to establish the connection.

* I learnt that VNC (Virtual Network Computing) is a graphical desktop sharing system that is used to remotely control another computer. First of all, I enabled the VNC field in the Interfaces section in the Raspberry Pi Configuration. After this setting is enabled, the RealVNC server should be automatically active. But unfortunately RealVNC did not work because there was an error on my Raspberry Pi. So I used TigerVNC instead. 
* After doing research for TigerVNC [this site](https://picockpit.com/raspberry-pi/tigervnc-and-realvnc-on-raspberry-pi-bookworm-os/#:~:text=TigerVNC%20is%20another%20popular%20VNC,it%20presents%20a%20security%20risk.) After completing the steps, the Raspberry Pi part for VNC was completed.

* There are two steps left for the connection. The first step is to access the modem interface and access the Raspberry Pi IP. After completing this step and getting the IP address, I installed TigerVNC Viewer.
* For TigerVNC installation, I first connected to Raspberry Pi via ssh, after connecting, I made Raspberry Pi ready for VNC by typing *tigervncserver*. After this stage, I opened the TigerVNC Viewer on my computer and entered the IP address and password, then I completed my connection with VNC.

### Learning AT Commands
* I firstly learnt what AT commands are by searching the internet and came across [sixfab documentation](https://docs.sixfab.com/page/sending-at-commands). I proceeded with this documentation as a reference.
* I got an error while downloading the *atcom* package with pip. When I investigated this error, I found out that the downloaded location was not added to the PATH. After adding this directory to PATH, I was able to continue with the other steps.
* After successfully downloading the library, the test part remained. When I ran this command *atcom --port /dev/ttyUSB2 AT*, I got this error *[ERR] Couldn't open serial communication* and I changed with all three available /dev/ttyUSB*. And i am still struggling to solve this error.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI5Nzg5NzExMCwxNzIwOTk3NTQ0XX0=
-->