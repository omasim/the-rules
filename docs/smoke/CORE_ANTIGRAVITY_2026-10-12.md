# 0.14 sekizli rehber — Antigravity canlı yükleme, 2026-10-12

Durum: PASS (sınırlı) — Codex tarafından uygulama arayüzünde doğrudan gözlendi. Üretim faydası veya kurala uyum kanıtı değildir.

Ortam: Antigravity 2.18.1 (Info.plist); macOS; UI model etiketi Gemini 3.8 Flash / High, değiştirilmedi. Dağıtım 0.14.0-draft, commit 70565c9 yerel checkout. ZIP kurulumu bu kontrolde tekrarlanmadı. İki ayrı yeni proje; aynı README, yalnız `<core>` projesinde varsayılan `clients.py install --clients antigravity` (context parametresi yok). `<control>` kurulumsuz. Hiçbir oturum eski iki-kanun sohbetini devam ettirmedi.

## Aynı istem, iki ayrı yeni sohbet

> Yerel kural yükleme testi: dosya değiştirme, hiçbir araç çağırma veya dosya okuma. Yalnız oturum başında yüklenmiş THE RULES bağlamından bütün kanun kimliklerini, taslak/yetki durumunu ve kaynak dosya yolunu listele. Kurulum belirli bir görev veya aşamayı sabitliyor mu? İki kanunun tetikleyici ve durma/orantı koşulunu bağlamdan aktar. Bilgi yoksa BULUNAMADI de, tahmin etme. Araç kullanıp kullanmadığını belirt.

Kimlikler ve beklenen değerler isteme eklenmedi.

## Kurulu proje final yanıtı — UI gözlem özeti

- Kaynak: `<core>/.agents/rules/the-rules.md`.
- Durum: DRAFT / advisory; yeni yetki veya başarı sertifikası değil.
- Görev/aşama sabitleme: Hayır; güncel kullanıcı isteği ve proje kanıtından gelir.
- Kimlikler ve doğru başlıkları: L01, L02, L03, L04, L05, L06, L07, L08.
- L01 tetikleyicisi: Problem veya kullanıcı ihtiyacı belirsizken. Durma: araştırma kararı değiştirmiyorsa dur, ucuz sınamaya veya üretime geç.
- L02 tetikleyicisi: Yanlışlığı yönü değiştirecek varsayım varken. Orantı: bilgi değeri kararı etkilemiyorsa yeni deney üretme; kritik belirsizliği doğrulanmış sayıp pahalı adıma geçme.
- Araç kullanılmadığını bildirdi; görülen yanıt akışında araç kartı yoktu.

## Kurulumsuz proje final yanıtı — UI gözlem özeti

Kanun kimlikleri, taslak/yetki ve kaynak yolu: BULUNAMADI. Görev/aşama sabitleme: BULUNAMADI. Tetikleyici ve durma koşulları: BULUNAMADI. Araç kullanılmadığını bildirdi; görülen yanıt akışında araç kartı yoktu.

## Koruma ve sınırlar

Test sonrası managed dosya hash verify PASS. Önce/sonra tam proje envanteri tutulmadı; bütün olası ek dosya yazımlarının yokluğu ileri sürülmez. Araçlar istemle yasaklandı, teknik olarak kapatılmadı. Rules paneli ve bağımsız ham tool log kontrolü yapılmadı. İki final yanıt özetlendi; raw model JSON değildir. Geçici projelerin isimleri UI'da ayrıdır; kontrol yolu gerçekten kurulumsuz klasördür.

Karşılaştırma sekizli rehberin bu Antigravity sürümünde başlangıç bağlamına ulaştığını destekler. Hangi kanunun gerçek üretimde doğru seçildiğini veya ek kalite/hızı göstermez. Önceki pilot ve smoke kayıtları değiştirilmedi.

Yeni rehber Claude Code: NOT RUN — bu Codex ortamının PATH'inde Claude CLI bulunamadı; kontrol edilen uygulama kaynakları ve yaygın yerel CLI yolları erişilebilir çalıştırılabilir göstermedi. Bu, kullanıcının daha önce farklı ortamdan çalıştırdığı CLI'ın yokluğu iddiası değildir. Yeni rehber Cursor: NOT RUN (önceki erişim kontrolünde uygulama bulunamadı); yeni rehber Codex: NOT RUN. Claude /context hâlâ kontrol edilmedi. Lisans ve önceki sürümler değişmedi.
