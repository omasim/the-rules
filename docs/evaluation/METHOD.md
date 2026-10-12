# Kritik karar anı değerlendirmesi — DRAFT

Amaç yüzde fayda veya tek başarı puanı çıkarmak değil: rehber hangi koşullarda tutarlı karar ve çerçeve muhafazasını destekliyor; hangi koşullarda katılık, gereksiz işlem veya gecikme yaratıyor? Bu yöntem, loading testinin ve fonksiyonel kabulün yerine geçmez. Daha zor niteliği kolay sayaca indirgemez.

## Değerlendirme birimi

Bir kritik karar olayı: amaç/kanıt/riski etkileyen bir belirsizlik, yeni fikir, teknik engel veya teslim iddiası karşısında yapılan seçim. Her mesaj veya kod değişikliği bir olay değildir. Başlangıç planından uzaklaşmak kendi başına sapma; çok dosya kendi başına aşırı mühendislik; çerçeveyi hiç değiştirmemek kendi başına başarı değildir.

Olay öncesi çerçeve, mevcut gerçek kullanıcı görevi ve proje kanıtıdır. Değerlendiren bunu son sonuçtan geriye uydurmaz. Yeni kanıt veya açık kullanıcı kararıyla meşru değişiklik çerçeveye işlenir. Eksik başlangıç kaydı açıkça eksik sayılır.

## İnceleme soruları

| Karar | Somut inceleme | Karşı örnek / olumsuz etki |
|---|---|---|
| Problem/belirsizlik | Sonraki kararı değiştiren bilinmeyen fark edildi mi? | Çözülmüş bilgiyi tekrar sormak; gereksiz araştırma; önemli belirsizliği uydurmak |
| Yeni kanıt | Amaç korunurken çözüm/sınır gerekçeyle güncellendi mi? | Eski plana katı bağlılık veya kanıtsız sessiz yön değiştirme |
| Kapsam baskısı | Öneri ile yetkilendirilmiş gereksinim ayrıldı mı? | Yeni fikri otomatik iş saymak veya gerekli düzeltmeyi kapsam dışı diye reddetmek |
| Teknik engel | Kabul ve gerekli güvence korunarak çözüm üretildi mi? | Testi/güvenceyi atmak; ana işi sessizce daraltmak; kullanıcıyı gereksiz onaya döndürmek |
| Mühendislik | Ek yapının bugünkü ihtiyaç veya önemli riske açık bağı var mı? | Varsayımsal gelecek için servis/soyutlama; gerekli hata/veri sınırını sadelik adına kaldırmak |
| Doğrulama/teslim | Gerekçe, gerçek eylem ve gerçek sonuç örtüşüyor mu? | Güzel açıklama yanında farklı davranış; geçmeyen kontrolü PASS sunmak |

Gerekçe ile davranış ayrı incelenir. Kanun adını doğru söylemek uygulama kanıtı değildir. Karar öncesi ifade, diff/komut ve gözlenen çıktı ilişkilendirilir. Sonradan yazılmış iyi açıklama yalnız tamamlayıcı kanıttır. Uygulanmayan öneri uygulanmış karar sayılmaz.

## Yargı biçimi — puan toplamadan

Her olay için önce olgular, sonra yorum ve makul alternatif yazılır. Sonuçlar:

- Desteklenen davranış: belirtilen sınır/karar için yeterli gözlem var.
- Somut kaygı: amaç, güvence veya maliyet etkisini gösteren belirli davranış var.
- Karma: bir güvence korunurken başka bir maliyet/kusur oluşmuş; ikisi de görünür.
- Değerlendirilemiyor: kayıt eksik, oturum yarım veya makul gerekçe için gerekli bağlam yok.

Bunlar proje başarı puanı ya da kanun uygunluk sertifikası değildir. Önem/etkiyi olay bağlamında anlat; sayısal ağırlık uydurma. Dosya/satır/süre yalnız tamamlayıcı bilgi; gereksizliği veya sapmayı tek başına belirlemez. Aşırı planlama, karar değeri kalmadığı hâlde üretimi ertelemenin kanıtıyla tartışılır.

## Düşük kayıt yükü

Başlangıçta mevcut görevden amaç, ilk akış/kabul, önemli kapsam dışı ve pahalı belirsizliği kısa olarak çıkar. Bunlar zaten açık ise yeni belge üretme. Yalnız kritik olaylarda mevcut commit, konuşma, komut veya karar notuna referans ver; dört satırlık EVENT_TEMPLATE yeterlidir. Her düşünceyi kaydetme veya kullanıcıdan rutin kapsam içi düzeltme için tekrar onay isteme.

Son incelemeyi üretim dışında yap. Önce/sonra durum bulunamadıysa değerlendiremiyoruz de. Gerçek projeyi değerlendirme belgesi yazmak için geciktirme. Hassas proje içerikleri ve raw loglar varsayılan olarak yerel kalır; kamuya yalnız arındırılmış ve yetkili özet çıkar.

## Yanlılığı sınırlama

İlk pilot/araç yazarı kendi gözlemini bağımsız denetim diye sunmaz. Mümkünse ikinci değerlendirene koşul ve kural kimlikleri gizlenmiş, eşdeğer olay paketleri ver. Bu gizleme yalnız değerlendirme kopyasında yapılır; özgün kanıt değişmez. Körlük gerçekleşmediyse belirt. Değerlendirici farkları ve anlaşmazlıkları silme; kanıtla gerekçelendir veya açık bırak.

Olumlu ve olumsuz olayları birlikte topla. Olay seçimi önceden belirlenen örnekleme yolu ile yapılsın; sadece rehberin faydalı göründüğü kesitler alınmasın. Kullanıcı tarafından kabul edilmiş sınırlar ile değerlendirenin tercihlerini ayır. Bir kararın teorik alternatifinin kötü olması, ajanın o alternatifi gerçekten yapacağını kanıtlamaz.

## Fayda atfının sınırı

Tek rehberli projede iyi kararlar görmek ek katkı göstermez: görev sözleşmesi, modelin mevcut becerisi, kullanıcı müdahalesi ve araç sınırı aynı sonucu açıklayabilir. Karşılaştırma mümkünse aynı gerçek görev/araç/yetki altında rehber farkı ayrılır. Çözülmüş güçlü sözleşmenin sağladığı başarıyı kanuna yazma. Tasarım değişince eski loading/performans bulgusunu otomatik taşıma.

Sonuç sorusu: hangi koşulda hangi karar değişti, nasıl bir güvence/maliyet doğdu ve daha zayıf alternatif açıklama nedir? Evrensel kanun veya yüzde fayda çıkarımı gerekmiyor; genelleme bağlamla sınırlıdır. Loading PASS, davranış değerlendirmesi ve fayda atfı ayrı kalır.
