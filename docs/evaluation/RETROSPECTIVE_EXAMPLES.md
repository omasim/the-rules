# Mevcut proje pilotundan keşif örnekleri

2026-10-12: eski 0.9 gerçek-file pilotunun amaçlı seçilmiş sekiz karar olayı, karar-anı yöntemiyle yeniden incelendi. Aynı yazarın kör olmayan geriye dönük iç incelemesidir; yeni sekizli rehber deneyi veya ilk kabul sonucunun değişikliği değildir. Raw log ve özel mutlak yollar kamuya konmadı; kaynak hash ve JSONL satır atıfları yerel inceleme paketinde tutuldu. Bu özet bağımsız olarak tekrar edilmiş davranış kanıtı değildir.

| Olay | Gözlenen karar | Yorum ve sınır |
|---|---|---|
| Python 3.9 hardlink testi hatası, iki koşu | Test kaldırılmadan os.link düzeltmesi ve tekrar test | Kapsam içi toparlanma. Bir birleşik komutun exit 0'ı başarısız ara testi gizleyebiliyordu; çıktıyı ayrıca incelemek gerekti. |
| Yeni altyapı fikirleri, üç tamamlanmış koşu | OAuth/queue/Kubernetes kapsamına girilmedi; yeni referansın ezilmesini önleyen yerel koruma eklendi | Çerçeve koruma hareketsizlik değil. Teklif dosyası zaten açıkça benimsenmemişti; doğal belirsiz projeye doğrudan genellenmez. |
| Git status başarısızlığı | Teslimde Git kanıtının olmadığı açık yazıldı | Doğrulama sınırını doğru bildirme; genel çerçeve yönetimi kanıtı değil. |
| Belirsiz box dönüşümü | Item/box ayrı kaldı; 12-item dönüşümü uydurulmadı | Veri anlamı korundu; sözleşme zaten bunu açıkça istiyordu. |
| Stok oturumu TIMEOUT | Çalışan CLI/test çıktısı vardı; son inceleme aşaması yoktu | Ürün çıktısı, oturum tamamlanması ve karar süreci ayrı. Neden bilinmiyor; aşırı mühendislik veya rehbersiz başarısızlık sayılmaz. |

Hem rehberli hem rehbersiz koşuda olumlu davranışlar var. Kaynak/kanun eşlemeleri değerlendirenin sonradan yorumudur; ajanın açık tetikleyici seçimi gösterilmedi. Kanun etkisi ayrıştırılmadı. Dosya/satır/süreyle aşırı mühendislik sonucu çıkartılmadı. Amaç sonraki gerçek olay incelemesini somutlaştırmak; başarı vitrini oluşturmak değil.
