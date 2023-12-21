##  1
									Akif Artun 14.12.2023
### Raspberry Pi 3B Setup

* Firstly, I downloaded the [Raspberry Pi  Systenıia](https://aspberrypi.com/software/operating-systems/) that I will install into the SD card inside the Raspberry Pi 3B set.
* After downloading the Raspberry Pi  Systenia, this media needed to be loaded onto the SD card to be ready for installation, and I used the [BalenaEtcher application](https://etcher.balena.io/) to make it ready.
* SD kartını hazırladığım için bir sonraki adım olan Raspberry Pi 3B için gerekli bağlantıların yapılmasına başladım. Bu bağlantılar;
	* Raspberry Pi' a ekran üzerinden erişilmesi için monitörün HDMI kablosu bağlantısı,
	* Mouse bağlantısı,
	* Klavye bağlantısı, 
	* İlk kurulumda gerekli internet için LAN kablosu bağlantısıdır.
* Bu adımlardan sonra artık adaptör aracılığıyla Raspberry Pi'a güç verdim.
* Son olarak kurulum işlemlerini sırasıyla yaptıktan sonra Raspberry Pi kullanıma hazır hale geldi. 

### Sixfab 4G/LTE Cellular Modem Kit Kurulumu 

* İlk olarak modem kitinin kurulumu için referans alacağım [siteyi](https://docs.sixfab.com/docs/raspberry-pi-4g-lte-cellular-modem-kit-getting-started) buldum.
* Bu sitedeki donanımsal olarak gerekli bütün adımları dikkatli bir şekilde yaptım.
* Donanımsal gereklilikler bittikten sonra https://connect.sixfab.com/#/ sitesi üzerinden giriş yaparak burdan elde ettiğim *"sudo bash -c "$(curl -sN https://install.connect.sixfab.com)" -- -t YOUR_TOKEN_APPEARS_HERE -r emea"* satırını Raspberry Pi terminal ekranında çalıştırdıktan sonra cihazımı Sixfab Core ile başarıyla bağladım. 

### Github Repo Açma ve Git komutları 

* İlk olarak Github hesabımdan "staj" adında bir repository oluşturdum.
* Bu reponun içinde weekly dizini olması gerektiği için bir tane boş markdown dosyasını weekly dizini altında oluşturdum.
* Git komutlarını anlamak ve anladıklarımı uygulamak için README dosyasını bilgisayarda oluşturduğum "sixfab" dizini içerisinde aşağıda belirttiğim kodlar ile repoya ekledim. 
	* cd Desktop
	* cd sixfab
	* git init
	* git add README.md
	* git commit -m "README file"
	* git remote add origin https://github.com/Akifartun/staj.git
	* git push -u origin master
* Git komutlarını öğrendikten sonra bu raporumu da git komutlarıyla githuba yükledim. 

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTczNTA4MDEwLC0zOTY1NjMwNTVdfQ==
-->