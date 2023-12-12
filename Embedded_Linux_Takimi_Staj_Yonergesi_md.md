# Gömülü Linux Takımı Staj - İlk Proje

## Amaçlar
* Gömülü Linux sistemlerine giriş yapmak.
* Raspberry Pi ile çalışabilmek.
* Temel linux komutlarını kullanabilmek.
* Python'da OOP yaklaşımı ile okunaklı, sürdürülebilir kod yazabilmek.
* Git ve Github kullanabilmek.
* Proje planlaması ve yönetimi yapabilmek.
* Doküman oluşturabilmek.
* Gantt şeması hazırlayabilmek.
* Hücresel ağ modemleri ile ilgili temel bilgileri öğrenmek. Modem kullanarak temel protokollerde veri gönderebilmek ve alabilmek.

## Proje İsterleri
* Modem ile konuşmak, ayarlarını değiştirmek, veri göndermek ve almak için bir Python kütüphanesi yazılacak. Kütüphane modem ile konuşmak için AT komutları gönderebilmeli ve modemden gelen cevapları işleyebilmeli.
  * Ekstra: Modem seri portu otomatik tanıma.
  * Ekstra: Seri port, baudrate, parity vb. seri port ayarlarını özelleştirme.
* Modem üzerinden [webhook.site](http://webhook.site)'a HTTP GET ve POST istekleri gönderen örnek bir kod yazılacak. Bu kod daha öncesinde yazdığımız kütüphaneyi kullanacak.
* Modem üzerinden ücretsiz ve açık bir MQTT broker olan [hivemq](https://www.hivemq.com/mqtt/public-mqtt-broker/) üzerinde bir topic'e MQTT mesajı gönderen örnek bir kod yazılacak. Aynı topic'e subscribe olunarak buraya gönderilen mesajın tekrar modem tarafından okunması sağlanacak. Bu kod daha öncesinde yazdığımız kütüphaneyi kullanacak.
* Raspberry Pi'nin modem üzerinden internete çıkması sağlanacak.
  * PPP protokolü ile
  * QMI/RMNET protokolü ile
  * ECM protokolü ile
* Bu 3 protokol ile kurulan bağlantıların hızları ölçülecek ve protokollerin genel bir karşılaştırması yapılacak.

## Hareket Planı
### Hafta 1
* Temel git komutlarının öğrenilmesi.
* Çalışmaların yapılacağı github reposunun oluşturulması.
* Markdown ile nasıl doküman oluşturulacağının öğrenilmesi.
* Raspberry Pi 3B+ ilk kurulumlar, işletim sistemini hazır hale getirme, temel bash komutlarını öğrenme.
* Proje planının hazırlanması. Projenin maks 6 haftalık bir sürede tamamlanması planlanıyor. Bu 6 haftalık süreç için haftalık olarak yapılacak işlerin belirlenmesi.
* Gantt şemasının hazırlanması. Bu şemayı github reposuna görüntülenebilir bir formatta eklemelisiniz.
* Raporlama
  
### Hafta 2, 3, 4, 5, 6, 7
Proje planına göre haftalık olarak yapılacak işlerin yapılması ve haftalık şekilde raporlanması.

## Kullanılacak Araçlar
### Yazılım Araçları, Teknolojileri ve Dilleri
* **Python:** Programlama dili olarak kullanılacak.
* **Linux:** İşletim sistemi olarak kullanılacak.
* **Bash:** Linux üzerinde komut satırı arayüzü olarak kullanılacak.
* **Git/Github:** Proje yönetimi ve takibi için kullanılacak.
* **Markdown:**  Doküman oluşturmak, rapor hazırlamak vb. işler için kullanılacak.
* **Gantt Şeması**: Proje yönetimi/takvimi için kullanılacak.

### Donanımlar
* [Raspberry Pi 3B+ Set](https://sixfab.com/product/raspberry-pi-3-kit/)
  * Raspberry Pi 3B+
  * SD Kart
  * SD Kart Okuyucu
  * 5V Adaptör
* [Sixfab 4G/LTE Cellular Modem Kit](https://sixfab.com/product/raspberry-pi-4g-lte-modem-kit/)
  * Sixfab Base HAT
  * Quectel EG25-G Modem
  * Antenler
  * Sixfab SIM Kart

## Raporlama
* Haftalık raporlar github reposunda `weekly` dizini altında oluşturulacak.
* Haftalık raporlar markdown(.md) formatında olmalıdır.
* Haftalık raporlar görseller ve tablolar ile desteklenebilir.
* Haftalık raporlarda özellikle araştırma kısmında edinilen bilgiler için kaynakça eklenmelidir.

## Haftalık Takım Toplantıları
* Her hafta takım toplantısı yapılacak. 1 saatle sınırlı olacak.
* Gösterilmesi gereken demo vb. şeyler varsa toplantıda gösterilecek. Genel durum değerlendirmesi yapılacak. Yapılan işler ve yapılacak işler konuşulacak. Bir değişiklik olmazsa bu toplantıları her hafta pazartesi 20:00'da yapmaya devam edebiliriz.