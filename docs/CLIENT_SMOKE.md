# Gerçek istemci kontrolü

| İstemci | Durum | Kayıt |
|---|---|---|
| Claude Code | PASS — kullanıcı tarafından raporlanan canlı yükleme testi (2.1.295, `claude-opus-5-5`, macOS, `build`) | [CLAUDE_CODE_2026-10-11](smoke/CLAUDE_CODE_2026-10-11.md) |
| Cursor | NOT RUN | — |
| Antigravity | NOT RUN | — |

Claude Code kaydında `/context` Memory files görünümü kontrol edilmedi; otomatik yükleme araçsız oturum ile kurulumsuz kontrol projesinin karşılaştırılmasıyla gösterildi.

Her uygulamada hedef projeyi açıp yeni bir sohbet başlatın. Claude Code'da /context içindeki Memory files listesi, Cursor ve Antigravity'de Rules/Customizations görünümü ile üretilen dosyanın tanındığını kontrol edin. Arayüz ayrıntıları sürüme göre değişebilir.

Şu isteği kullanın: “Dosya değiştirmeden THE RULES'ın seçili profilini, iki kanun kimliğini, DRAFT statüsünü ve bunu okuduğun yerel dosya yolunu göster. Kaynak dosya içeriğini gerçekten incele; erişemediysen açıkça belirt.”

build örneğinde beklenen kimlikler L04 ve L05. Beklenen dosya yolu her istemcinin kendi adaptör yoludur. Yalnız genel bir kanun özeti yeterli kanıt sayılmaz. Uygulama sürümü, profil, görülen dosya, gerçek yanıt ve varsa yükleme hatasını kaydedin. Kontrol doğrudan kütüphane dosyasını isteyerek erişimi de sağlayabildiğinden otomatik başlangıç yüklenmesini tek başına kanıtlamaz; Rules/Memory görünümüyle birlikte değerlendirin.

Bu küçük kontrol erişim/yükleme içindir; kuralların izlendiği veya üretim kalitesinin arttığı anlamına gelmez. Mevcut deney sonuçları değişmez. Cursor ve Antigravity ile henüz gerçek oturum yapılmadı.
