# Antigravity canlı yükleme — 2026-10-12

Durum: PASS (sınırlı) — Codex tarafından uygulama arayüzünde doğrudan gözlenen kısa yükleme kontrolü. Bağımsız tekrar değil; üretim faydası kanıtı değil.

Antigravity 2.18.1 (uygulama Info.plist), macOS; UI model etiketi Gemini 3.8 Flash / High. Varsayılan model değiştirilmedi. Profil build; dağıtım 0.13.2-draft yerel checkout araçları. Katalog/profil içerikleri değişmedi. Yayın ZIP'inden kurulum bu kontrolde yeniden sınanmadı.

İki ayrı geçici proje: `<smoke>` README ve üçlü istemci aracının yalnız antigravity adaptörüyle kuruldu; `<control>` aynı README, kurulum yok. Değerlendirme öncesi doğru profil ve kimlikler isteme eklenmedi. Uygulama proje seçicisiyle ilgili klasörler açıldı.

## A — kurulu projede başlangıç bağlamı

İstem:

> Bu bir yerel kural yükleme kontrolüdür. Dosya değiştirme, hiçbir araç çağırma ve dosya okuma. Yalnız oturum başında otomatik yüklenmiş bağlamdan THE RULES'ın seçili profilini, iki kanun kimliğini, taslak/benimseme durumunu ve kaynak dosya yolunu bildir. Bilgi bağlamında yoksa her alan için BULUNAMADI yaz; tahmin etme. Araç kullanıp kullanmadığını açıkça belirt.

Tamamlanmış yanıtın görülen alanları: build; L04, L05; DRAFT / advisory; `<smoke>/.agents/rules/the-rules.md`. Araç çağrısı kullanılmadığını bildirdi; bu yanıtın UI kaydında araç kartı görünmedi. Araç izinleri teknik olarak kapatılmadı; araçsız Claude CLI testiyle aynı izolasyon gücü yoktur.

## B — aynı sohbet içinde okuma doğrulaması

İstem:

> Şimdi yalnız proje içindeki .agents/rules/the-rules.md dosyasını oku. Dosya değiştirme veya komut çalıştırma. Dosyadaki başlığa göre seçili profili, iki kanun kimliğini, DRAFT durumunu ve kaynak yolunu bildir; araçla okuma ile otomatik bağlamı ayrı belirt.

UI'da Exploring 1 file / Analyzed the-rules.md#L1-23 gözlendi. Tamamlanmış yanıt build, L04/L05 ve DRAFT/advisory bildirdi; view_file ile okuduğunu söyledi. Otomatik bağlamla disk içeriğinin eşleştiğini belirtti. B yeni bağımsız oturum değildir; A'nın bilgisini sohbet geçmişinde taşır, yalnız dosya erişimi teyididir.

## C — kurulumsuz projede yeni sohbet

A ile aynı istem kullanıldı. Tamamlanmış yanıt: seçili profil BULUNAMADI; iki kimlik BULUNAMADI; taslak/benimseme BULUNAMADI; kaynak yolu BULUNAMADI. Araç çağrısı kullanılmadığını bildirdi; UI'da araç kartı görünmedi.

## Koruma ve sınırlar

Kurulum sonrası ve test sonrası verify PASS; mevcut yönetilen dosyaların hash'leri korundu. Kontrol projesinde kurulum oluşmadı. Proje envanteri önce/sonra ayrıca kaydedilmediğinden bütün olası ek dosya yazımlarının yokluğu ileri sürülmez. Görünen konuşma eylemleri dosya değişikliği/kabuk komutu göstermedi.

A/C farkı bu sürüm ve build profili için otomatik başlangıç yüklemesini destekler. Rules/Customizations listesi ayrıca kontrol edilmedi. Otomatik yüklemenin her sürüm, profil veya IDE yüzeyinde geçerli olduğu söylenmez. Araçlar teknik olarak devre dışı bırakılmadı. Modelin kurallara uyduğunu, kapsamı koruduğunu veya kalite/hızı artırdığını kanıtlamaz. Özgün pilot sonuçları değişmedi.

Cursor: NOT RUN — uygulama envanterinde yok ve uygulama seçimi Invalid app: Cursor döndü; /Applications altında da Cursor bulunamadı. Kurulum veya hesap açma yapılmadı. Claude Code /context görünümü bu kontrolde ele alınmadı.

Yollar yayıma hazırlanırken `<smoke>` ve `<control>` olarak anonimleştirildi. Kayıt final yanıt alanlarının UI gözlem özetidir; raw model JSON veya tam araç-denetim logu değildir.
