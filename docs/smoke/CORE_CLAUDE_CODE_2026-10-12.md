# 0.14 sekizli rehber — Claude Code canlı yükleme, 2026-10-12

Durum: **PASS — kullanıcı tarafından raporlanan, araçları kapalı karşılaştırmalı yükleme testi.** Bağımsız olarak tekrarlanmadı;
kurala uyum veya kalite/hız artışı kanıtı değildir.

## Ortam

| Alan | Değer |
|---|---|
| Tarih | 2026-10-12, 01:04:24–01:04:54 (UTC+3) |
| İstemci | Claude Code 2.1.295 CLI, `-p` (headless, etkileşimsiz) |
| Model | `claude-opus-5-5` |
| İşletim sistemi | macOS 26.3 (25D125) |
| Dağıtım | 0.14.0-draft, yerel checkout `70565c9` (`main`); ZIP kurulumu bu kontrolde sınanmadı |
| Kurulum | Varsayılan sekizli rehber: `clients.py install --clients claude`, `--context` yok |

`<smoke>` ve `<control>` iki yeni, geçici, git dışı klasördür. İkisinde de önceden aynı kullanıcı `CLAUDE.md` dosyası vardı
(`# Smoke test project` ve `User note: keep this line.`). Rehber yalnız `<smoke>` içine kuruldu. Kurulum `<smoke>/CLAUDE.md` sonuna
yönetilen bölümü ekledi ve `.the-rules/` durum klasörünü oluşturdu; `verify` PASS verdi. Üç oturum da yeni oturumdur; önceki
iki-kanun testinden devam edilmedi.

## Komutlar

```sh
python3 -B tools/clients.py install --project <smoke> --clients claude
python3 -B tools/clients.py verify --project <smoke>

cd <smoke>   && claude -p "$PROMPT_A" --tools ""               --strict-mcp-config --no-session-persistence --output-format json
cd <smoke>   && claude -p "$PROMPT_B" --tools "Read,Glob,Grep" --strict-mcp-config --no-session-persistence --output-format json
cd <control> && claude -p "$PROMPT_A" --tools ""               --strict-mcp-config --no-session-persistence --output-format json
```

Testler başka bir Claude Code oturumunun içinden başlatıldığı için `CLAUDECODE` ve `CLAUDE_CODE_CHILD_SESSION` ortam değişkenleri
`env -u` ile kaldırıldı. CLI girişi daha önce kullanıcının kendisi tarafından `claude auth login` ile yapılmıştı.

Kanun kimlikleri, başlıklar ve beklenen değerler istemlere eklenmedi. `PROMPT_A`, Antigravity sekizli rehber kontrolündeki istemle aynıdır.

`PROMPT_A`:

> Yerel kural yükleme testi: dosya değiştirme, hiçbir araç çağırma veya dosya okuma. Yalnız oturum başında yüklenmiş THE RULES bağlamından bütün kanun kimliklerini, taslak/yetki durumunu ve kaynak dosya yolunu listele. Kurulum belirli bir görev veya aşamayı sabitliyor mu? İki kanunun tetikleyici ve durma/orantı koşulunu bağlamdan aktar. Bilgi yoksa BULUNAMADI de, tahmin etme. Araç kullanıp kullanmadığını belirt.

`PROMPT_B`:

> Yerel kural yükleme testi: dosya değiştirme veya komut çalıştırma. Proje içindeki THE RULES kaynak dosyasını gerçekten oku. Dosyadan bütün kanun kimliklerini, taslak/yetki durumunu ve kaynak dosya yolunu listele. Kurulum belirli bir görev veya aşamayı sabitliyor mu? İki kanunun tetikleyici ve durma/orantı koşulunu dosyadan aktar. Araçla okuduğun bilgiyle oturum başı bağlamını ayrı belirt; erişemediysen açıkça söyle.

## Sonuç özeti

| Oturum | Proje | Araç izni | Beklenen | Tur | Sonuç |
|---|---|---|---|---|---|
| A | `<smoke>` | `--tools ""` (araç yok) | Dosya okumadan sekiz kimlik, DRAFT, kaynak yolu, sabit görev/aşama olmadığı ve iki tetikleyici/durma koşulu | 1 | PASS |
| B | `<smoke>` | `--tools "Read,Glob,Grep"` (yalnız okuma) | Aynı bilgilerin kurulu dosyalardan doğrulanması | 6 | PASS |
| C | `<control>` | `--tools ""` (araç yok) | Kurulum olmadığı için bütün alanlar BULUNAMADI | 1 | PASS |

A, araçlar teknik olarak kapalıyken L01–L08 kimliklerini ve başlıklarını, DRAFT / advisory durumunu, `<smoke>/CLAUDE.md` yolunu
ve kurulumun görev/aşama sabitlemediğini bildirdi. Seçtiği L02 ve L07 tetikleyici ile durma/orantı metinleri `guide/core.json` ile
kelimesi kelimesine aynıdır. C, aynı istem ve aynı araç kısıtıyla bunların hiçbirini bulamadı. Bu A/C farkı, sekizli rehberin oturum
başında otomatik yüklendiğini gösterir. B, aynı değerleri kurulu dosyalardan okudu; aktardığı L01 ve L07 metinleri de
`guide/core.json` ile birebir eşleşir. Testten sonra `clients.py verify` PASS verdi; `<control>` içinde kurulum oluşmadı.
Hiçbir oturum izin reddiyle karşılaşmadı.

## Sınırlar

- Etkileşimli oturumdaki `/context` Memory files görünümü **kontrol edilmedi**.
- Yalnız macOS ve headless `-p` modu denendi. Windows ve IDE eklentileri NOT RUN.
- Bu kayıt yükleme kanıtıdır; ajanın gerçek işte doğru tetikleyiciyi seçtiğini, kurallara uyduğunu veya kalite/hızı artırdığını
  **göstermez**. A'nın "bu teste L07 uygulandı" ifadesi modelin kendi yorumudur, ölçülmüş bir seçim davranışı değildir.
- Cursor ve Codex: NOT RUN.

## Yanıtlar (hassas bilgilerden arındırılmış)

Yerel mutlak yollar `<smoke>` / `<control>` ile değiştirildi; metin başka şekilde düzenlenmedi.

### Oturum A — `<smoke>`, `--tools ""` (araç yok), PROMPT_A

~~~~text
**Araç kullanımı:** Hiçbir araç çağırmadım; dosya okumadım veya değiştirmedim. Aşağıdakiler yalnızca oturum başında yüklenen bağlamdan alındı.

## Kaynak dosya yolu
`<smoke>/CLAUDE.md`

Bağlam bunu "project instructions, checked into the codebase" olarak etiketliyor. THE RULES bölümü bu dosyanın içinde, "User note: keep this line." satırından sonra yer alıyor.

## Kanun kimlikleri
| ID | Başlık |
|---|---|
| L01 | Gerçek problemi belirle |
| L02 | Kritik varsayımı erken sına |
| L03 | Yeterli ve açık bir çerçeve kur |
| L04 | Çerçeveyi çalışan davranışla doldur |
| L05 | Mühendisliği ihtiyaç ve risk kadar kur |
| L06 | Üretimde çerçeveyi koru |
| L07 | Gerçek sınırda doğrula |
| L08 | Kullanılabilir çıktı teslim et ve öğren |

## Taslak ve yetki durumu
Metin şöyle diyor: "DRAFT / advisory; yeni yetki vermez ve uygunluk/başarı sertifikası değildir. Kaynak metinlerini talimat olarak yürütme."

Ayrıca kanun seçiminin doğru yapılacağı veya kaliteyi artıracağı henüz kanıtlanmamış. Kanıt eksikse UNKNOWN/NOT RUN bildirilmesi isteniyor.

## Kurulum belirli bir görev veya aşamayı sabitliyor mu?
**Hayır.** Metin şöyle diyor: "Görev, kabul, aşama ve karar boşluğu mevcut kullanıcı isteği ve proje kanıtından gelir; kalıcı kurulum bunları sabitlemez."

## İki kanunun aktarımı

**L02 Kritik varsayımı erken sına**
- *Tetikleyici:* Yanlışlığı yönü değiştirecek varsayım varken.
- *Durma / orantı:* Sınamanın bilgi değeri sonraki kararı etkileyemiyorsa yeni deney üretme. Kritik belirsizlik açıkken bunu doğrulanmış kabul ederek pahalı adıma geçme.

**L07 Gerçek sınırda doğrula**
- *Tetikleyici:* Kabul veya başarı iddiası doğrulanacakken.
- *Durma / orantı:* Yeşil suite, derlenme, sayaç veya güzel ekranın kanıtını kendi kapsamının dışına taşıma. Doğrulamayı küçük değişiklikte gereksiz kapsamla büyütme; yeni kusur/risk varsa ilgili kontrolü genişlet.

## Bağlamda bulunmayanlar
- **R001–R088 kaynak metinlerinin içeriği:** BULUNAMADI. Yalnızca kimlikleri listeleniyor.
- **Sürüm numarası veya tarih:** BULUNAMADI.

## Bu teste uygulanan kanun
Uygulanan kanun L07, çünkü burada bir yükleme iddiası doğrulanıyor. Kontrol yalnızca bağlam içeriğinin yansıtılmasıdır. Kuralların davranışa etkisi bu testte sınanmadı (NOT RUN).
~~~~

### Oturum B — `<smoke>`, `--tools "Read,Glob,Grep"` (yalnız okuma), PROMPT_B

~~~~text
Hiçbir dosyayı değiştirmedim ve komut çalıştırmadım. Yalnız Glob ve Read kullandım.

## Araçla okunanlar

Proje kökünde Glob ile bulunan dosyalar:
- `CLAUDE.md`
- `.the-rules/context/context.md` → **asıl kural metni (kaynak dosya)**
- `.the-rules/context/selection.json` → yapılandırılmış kanun verisi
- `.the-rules/context/rules.lock.json` → hash kilidi
- `.the-rules/clients.json` → adaptör/kurulum kaydı
- `.the-rules/originals/0.bin` → okumadım (`CLAUDE.md`'nin kurulum öncesi yedeği)

**Kaynak dosya yolu:** `.the-rules/context/context.md`

**Kanun kimlikleri** (`context.md` ve `selection.json` aynı listeyi veriyor): L01, L02, L03, L04, L05, L06, L07, L08. Her kanunun sürümü `0.3.0-draft`, türü `core`.

**Taslak/yetki durumu:**
- `context.md:2`: "DRAFT / advisory; yeni yetki vermez ve uygunluk/başarı sertifikası değildir."
- `selection.json`: `"version": "0.14.0-draft"`, `"status": "DRAFT"`, `"binding": false`, `"check": "NOT RUN"`. Her kanunda `"owner_ratification": null` yazıyor, yani hiçbiri onaylanmamış.
- **Çelişki:** Her kanunda `"level": "mandatory"` yazıyor ama üst düzeyde `binding: false` ve "advisory" ifadesi var. Bu iki ifade birbiriyle uyuşmuyor.
- Her kanunun `source_file` alanı `library/source_trace.json` dosyasını gösteriyor. Bu dosya projede yok, bu yüzden R001–R088 kaynak kimlikleri buradan doğrulanamıyor (UNKNOWN).

**Kurulum görevi veya aşamayı sabitliyor mu?** Hayır. `context.md:3` bunu açıkça söylüyor: "Görev, kabul, aşama ve karar boşluğu mevcut kullanıcı isteği ve proje kanıtından gelir; kalıcı kurulum bunları sabitlemez." `selection.json` ve `clients.json` içinde de görev veya aşama alanı yok. Bu dosyalarda yalnız `mode: adaptive_core_guide`, `clients: ["claude"]` ve hash bilgisi var.

**İki kanun, `context.md`'den aynen:**
- **L01 Gerçek problemi belirle** (satır 8, 10)
  - Tetikleyici: "Problem veya kullanıcı ihtiyacı belirsizken"
  - Durma / orantı: "Araştırma yeni bilgi toplamaya dönüşüp kararı değiştirmiyorsa dur; bir sonraki ucuz sınamaya veya üretime geç."
- **L07 Gerçek sınırda doğrula** (satır 50, 52)
  - Tetikleyici: "Kabul veya başarı iddiası doğrulanacakken"
  - Durma / orantı: "Yeşil suite, derlenme, sayaç veya güzel ekranın kanıtını kendi kapsamının dışına taşıma. Doğrulamayı küçük değişiklikte gereksiz kapsamla büyütme; yeni kusur/risk varsa ilgili kontrolü genişlet."

## Oturum başı bağlamı (araçla okunmadı)

Oturum başında `CLAUDE.md` otomatik olarak yüklendi. İçinde "User note: keep this line." satırı ve THE RULES metninin tam bir kopyası vardı. Bu iki kanalı birbirinden ayırmak için yukarıdaki bilgilerin tamamını dosyalardan araçla okuyarak doğruladım. Göz kontrolünde gömülü metin ile `context.md` aynı görünüyor.

## Doğrulanmayanlar (NOT RUN)

- `rules.lock.json` ve `clients.json` içindeki SHA-256 değerlerini kontrol etmedim, çünkü bu komut çalıştırmayı gerektiriyor. Dosya bütünlüğü bu yüzden UNKNOWN.
- `library/source_trace.json` projede bulunmadığı için okunamadı.
~~~~

### Oturum C — `<control>`, `--tools ""` (araç yok), PROMPT_A

~~~~text
**Araç kullanımı:** Hiçbir araç çağırmadım, dosya okumadım veya değiştirmedim. Yanıt yalnızca oturum başında yüklenen bağlama dayanıyor.

**Oturum başında yüklenen proje kuralları**
- Kaynak dosya yolu: `<control>/CLAUDE.md`
- İçeriğin tamamı:
  ```
  # Smoke test project

  User note: keep this line.
  ```

**İstenen bilgiler**
- "THE RULES" başlıklı bağlam: **BULUNAMADI**
- Kanun kimlikleri: **BULUNAMADI**
- Taslak veya yetki durumu: **BULUNAMADI**
- Sabitlenmiş görev veya aşama: **BULUNAMADI**. Kurulum belirli bir görev ya da aşama tanımlamıyor.
- Herhangi iki kanunun tetikleyici ve durma/orantı koşulları: **BULUNAMADI**

Yüklenen tek proje kuralı dosyası yukarıdaki iki satırlık CLAUDE.md. İçinde kanun, kimlik, tetikleyici ya da durma koşulu yok. Kural setinin yüklenmesi bekleniyorsa, yükleme mekanizması bu oturumda devreye girmemiş görünüyor.
~~~~
