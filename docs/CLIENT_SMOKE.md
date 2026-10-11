# Gerçek istemci yükleme kontrolleri

Bu kontroller yalnız kural dosyasının istemci tarafından yüklendiğini gösterir. Ajanın doğru tetikleyiciyi seçtiğini, kurallara uyduğunu veya üretim kalitesini artırdığını göstermez. Pilot sonuçları değişmez.

## 0.14 sekizli rehber (güncel kurulum)

| İstemci | Durum | Kayıt |
|---|---|---|
| Claude Code | PASS — kullanıcı tarafından raporlanan, araçları kapalı karşılaştırmalı yükleme testi (2.1.295, `claude-opus-5-5`, macOS, headless `-p`) | [CORE_CLAUDE_CODE_2026-10-12](smoke/CORE_CLAUDE_CODE_2026-10-12.md) |
| Antigravity | PASS (sınırlı) — doğrudan UI gözlemi; araçlar teknik olarak kapatılmadı (2.18.1, Gemini 3.8 Flash High, macOS) | [CORE_ANTIGRAVITY_2026-10-12](smoke/CORE_ANTIGRAVITY_2026-10-12.md) |
| Cursor | NOT RUN | — |
| Codex | NOT RUN | — |

Claude Code'da etkileşimli `/context` Memory files görünümü kontrol edilmedi; otomatik yükleme, araçsız kurulu proje ile araçsız kurulumsuz kontrol projesinin karşılaştırılmasıyla gösterildi.

Yeni kontrol için: biri kurulu, biri kurulumsuz iki yeni proje açın; ikisinde de yeni sohbette, kanun kimliklerini veya beklenen değerleri içermeyen aynı istemi kullanın. Mümkünse araçları teknik olarak kapatın; kapatılamıyorsa bunu kayıtta sınır olarak belirtin. İstem ve kayıt biçimi için yukarıdaki kayıtlara bakın. İstemci sürümü, model, işletim sistemi, araç izinleri, görülen dosya yolu ve gerçek yanıtı kaydedin.

## Tarihsel: iki-kanun build profili (0.13)

Bu kayıtlar eski build profiline aittir. Buradaki PASS durumları sekizli rehbere aktarılmaz.

| İstemci | Durum | Kayıt |
|---|---|---|
| Claude Code | PASS — kullanıcı tarafından raporlanan canlı yükleme testi (2.1.295, `claude-opus-5-5`, macOS, `build`) | [CLAUDE_CODE_2026-10-11](smoke/CLAUDE_CODE_2026-10-11.md) |
| Cursor | NOT RUN | — |
| Antigravity | PASS (sınırlı) — doğrudan UI gözlemi (2.18.1, Gemini 3.8 Flash High, macOS, build; araçlar teknik olarak kapatılmadı) | [ANTIGRAVITY_2026-10-12](smoke/ANTIGRAVITY_2026-10-12.md) |

Claude Code kaydında `/context` Memory files görünümü kontrol edilmedi; otomatik yükleme araçsız oturum ile kurulumsuz kontrol projesinin karşılaştırılmasıyla gösterildi.

Her uygulamada hedef projeyi açıp yeni bir sohbet başlatın. Claude Code'da /context içindeki Memory files listesi, Cursor ve Antigravity'de Rules/Customizations görünümü ile üretilen dosyanın tanındığını kontrol edin. Arayüz ayrıntıları sürüme göre değişebilir.

Şu isteği kullanın: “Dosya değiştirmeden THE RULES'ın seçili profilini, iki kanun kimliğini, DRAFT statüsünü ve bunu okuduğun yerel dosya yolunu göster. Kaynak dosya içeriğini gerçekten incele; erişemediysen açıkça belirt.”

build örneğinde beklenen kimlikler L04 ve L05. Beklenen dosya yolu her istemcinin kendi adaptör yoludur. Yalnız genel bir kanun özeti yeterli kanıt sayılmaz. Uygulama sürümü, profil, görülen dosya, gerçek yanıt ve varsa yükleme hatasını kaydedin. Kontrol doğrudan kütüphane dosyasını isteyerek erişimi de sağlayabildiğinden otomatik başlangıç yüklenmesini tek başına kanıtlamaz; Rules/Memory görünümüyle birlikte değerlendirin.

Bu küçük kontrol erişim/yükleme içindir; kuralların izlendiği veya üretim kalitesinin arttığı anlamına gelmez. Mevcut deney sonuçları değişmez. Cursor ile henüz gerçek oturum yapılmadı. Antigravity kısa kontrolü ve sınırları yukarıdaki kayıttadır.
