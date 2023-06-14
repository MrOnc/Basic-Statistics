# Username: Onc 
# Password : OncOnc
Bu Python kodu, PyQt5 kütüphanesini kullanarak bir hesaplama uygulaması oluşturur. Uygulama, kullanıcıların istatistiksel hesaplamalar yapmalarına ve malzeme/stok yönetimi ile ilgili bazı hesaplamaları gerçekleştirmelerine olanak tanır. İşlevselliği üç farklı bölümde toplanmıştır:

Giriş Ekranı:

Kullanıcı adı ve şifre isteyen bir giriş ekranıdır.
Doğru kullanıcı adı ("Onc") ve şifre ("OncOnc") girilmediği sürece uygulamaya erişim sağlanamaz.
İstatistiksel Hesaplamalar:

Bu bölüm, kullanıcının girdiği veri seti üzerinde istatistiksel hesaplamalar yapar.
Kullanıcı, virgülle ayrılmış verileri girerek ortalama, standart sapma, varyans, mod, medyan ve diğer istatistiksel değerleri hesaplayabilir.
Malzeme ve Stok:

Bu bölüm, malzeme ve stok yönetimi ile ilgili hesaplamaları gerçekleştirir.
Kullanıcı, talep miktarı, sipariş maliyeti, elde tutma maliyeti ve süre gibi parametreleri girerek EOQ (Ekonomik Sipariş Miktarı), toplam maliyet ve TBO (Talep Belirleme Süresi) gibi değerleri hesaplayabilir.
Bu uygulama, PyQt5 arayüz kütüphanesi kullanılarak oluşturulmuştur. PyQt5, Python dilinde GUI (Grafiksel Kullanıcı Arayüzü) uygulamaları geliştirmek için kullanılan popüler bir kütüphanedir. Uygulama, kullanıcı dostu bir arayüz sunmak için PyQt5'in sunduğu çeşitli bileşenleri (QLabel, QLineEdit, QPushButton, QDialog, QVBoxLayout, QFormLayout vb.) ve düzenleme yöntemlerini kullanmaktadır.
