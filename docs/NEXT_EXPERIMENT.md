# Sonraki inceleme — karar tutarlılığı ve çerçeve muhafazası

Bu bir çalıştırılmış deney veya ön kayıtlı etkililik çalışması değildir. [Karar-anı yöntemi](evaluation/METHOD.md), kolay sayılabilen hız/test skorunu hedefin yerine koymadan değerlendirme yolunu tanımlar.

## Önce gerçek olayları anlamak

Küçük bir gerçek proje serisinde mevcut görevi çerçeve referansı olarak koru. Üretimde yalnız kritik karar olaylarını dört satırlık kayıt veya mevcut artefakt linkiyle yakala; proje sonrasında gerekçe/eylem/sonuç ilişkisini incele. Bu seri keşif amaçlıdır. Sayı, ilk çalışma hızı veya dosya miktarı başarı puanı değildir.

Olay türleri: karar değiştiren belirsizlik, meşru yeni kanıt, kapsam baskısı, teknik engel, gerekçeli ek mühendislik ve teslim iddiası. Yalnız hataya zorlayan yapay görev seçme. Meşru değişikliklerin de doğru uygulanmasını incele; çerçeve koruma katılık değildir. Gerçek kullanıcı bilgisini eksiltip kontrol grubunu başarısızlığa itme.

## Sonra hedefli karşılaştırma

Keşif hangi durumun ayırt edici olabileceğini gösterirse yeni eşlenmiş görevlerde rehberli/rehbersiz karşılaştırmayı önceden tasarla. Aynı model/ayar, görev, yetki, araç ve bütçe kullan; sıra etkisini sınırla. Kriter ve guide hash'ini çalıştırmadan önce sabitle. Kör ikinci değerlendirici mümkünse artefaktları koşuldan bağımsız incelesin; mümkün değilse kör/bağımsız iddiası kurma.

Çalışan kabul ve önemli hata/veri güvenceleri hâlâ gereklidir, ancak tek sonuç değildir. Karar olayında bağlam kaybı, katılık, gereksiz mimari, çözülmüş bilginin yeniden araştırılması ve gerçek değişikliklerin gerekçeli uygulanması karşı örneklerle tartışılır. Açıklama kalitesi tek başına davranış kalitesi değildir. TIMEOUT veya kayıpsız devam kanıtı olmayan olay değerlendirilemiyor olarak korunur.

İlk seri temsili örneklem veya istatistiksel etki tahmini sağlamaz. Sonuçlardan sonra ölçüt değişirse ilk analiz korunur ve ayrı keşif olarak işaretlenir. Tek olumlu olaydan tüm projelere fayda iddiası çıkarılmaz. Amaç yüzde fayda değil, hangi koşulda hangi kararın neden değiştiğini ve bedelini açıklamaktır.

## Yapılmış ön kalibrasyon (2026-10-12)

Bu yöntemden önce, ikili başarı ölçütüyle yapay iki aşamalı görevler için bir [ön kayıt](PREREGISTRATION.md) donduruldu ve yalnız rehbersiz kolla [Phase 0 kalibrasyonu](CALIBRATION_2026-10-12.md) çalıştırıldı. Üç görevde 9/9 koşu bütün kontrolleri geçti (tavan etkisi). Ayrıca dar Bash izni ajanların değişikliği çalıştırıp doğrulamasını engelledi. Rehber koşulmadı; etki iddiası yoktur. Bu bulgu, yapay baskı görevlerinin bu modelde ayırt edici olmadığını ve hedefli karşılaştırmada gerçek doğrulamaya izin veren bir çalışma ortamı gerektiğini gösteren girdi olarak tutulur. Ön kayıttaki Phase 1 bu hâliyle askıdadır; yukarıdaki karar-anı yaklaşımı önceliklidir.

Görevler, bağımsız değerlendirici ve örnekleme planı henüz seçilmedi. Yeni model çağrısı veya kamuya raw proje verisi yayını başlatılmadı. Önceki pilotlar değişmedi.
