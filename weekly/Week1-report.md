##  Week 1
									Akif Artun 14.12.2023
### Raspberry Pi 3B Setup

* Firstly, I downloaded the [Raspberry Pi  OS](https://raspberrypi.com/software/operating-systems/) that I will install into the SD card inside the Raspberry Pi 3B set.
* After downloading the Raspberry Pi  Systenia, this media needed to be loaded onto the SD card to be ready for installation, and I used the [BalenaEtcher application](https://etcher.balena.io/) to make it ready.
* Since I prepared the SD card, I started to make the necessary connections for the next step, Raspberry Pi 3B. These connections;
	* HDMI cable connection for the monitor to access the Raspberry Pi via the display,
	* Mouse connection,
	* Keyboard connection,
	* The LAN cable connection for the internet is required for the first installation.
* After these steps, I now powered the Raspberry Pi via the adapter.
* Finally, after performing the installation processes respectively, Raspberry Pi is ready for use.

### Sixfab 4G/LTE Cellular Modem Kit Installation

* Firstly, I found [site](https://docs.sixfab.com/docs/raspberry-pi-4g-lte-cellular-modem-kit-getting-started) which I will refer to for the installation of the modem kit.
* I have carefully done all the necessary steps on this site hardware.
* After the hardware requirements were completed, I logged in to https://connect.sixfab.com/#/ and ran the line *"sudo bash -c "$(curl -sN https://install.connect.sixfab.com)" -- -t YOUR_TOKEN_APPEARS_HERE -r emea "* on the Raspberry Pi terminal screen and successfully connected my device with Sixfab Core.

### Github Repo Open and Git commands
* Firstly, I created a repository called "staj" from my Github account.
* Since there should be a weekly directory in this repo, I created an empty markdown file under the weekly directory.
* In order to understand git commands and apply what I understand, I added the README file to the repository in the "sixfab" directory I created on the computer with the following codes.
	* cd Desktop
	* cd sixfab
	* git init
	* git add README.md
	* git commit -m "README file"
	* git remote add origin https://github.com/Akifartun/staj.git
	* git push -u origin master
* After learning git commands, I uploaded this report to github with git commands.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUwMjMyMDMwMywxMzIyNTg0MTQxLC0zNj
YxOTU4NjAsMjA5NjU2MjU1NCwtMzk2NTYzMDU1XX0=
-->