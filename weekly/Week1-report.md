## Hafta 1
									Akif Artun 14.12.2023
### Raspberry Pi 3B Kurulumu

* Öncelikle Raspberry Pi 3B setinin içinde bulunan SD kartının içine yükleyeceğim  [Raspberry Pi İşletim Sistemi medyasını](https://www.raspberrypi.com/software/operating-systems/) indirdim. 
* Raspberry Pi İşletim Sistemi medyasını indirdikten sonra bu medyanın kuruluma hazır olması için SD karta yüklenmesi gerekmekteydi ve [BalenaEtcher uygulaması](https://etcher.balena.io/) kullanarak bunun hazır olmasını sağladım. 
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
* Donanımsal gereklilikler bittikten sonra https://connect.sixfab.com/#/ sitesi üzerinden giriş yaparak burdan elde ettiğim *"sudo bash -c "$(curl -sN https://install.connect.sixfab.com)" -- -t Exclaim-Sliding-Defy-Hungrily-Shrank-Unedited -r emea"* satırını Raspberry Pi terminal ekranında çalıştırdıktan sonra cihazımı Sixfab Core ile başarıyla bağladım. 

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
eyJoaXN0b3J5IjpbLTM5NjU2MzA1NV19
-->