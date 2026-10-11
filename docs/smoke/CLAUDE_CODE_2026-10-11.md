# Claude Code canlı yükleme kaydı — 2026-10-11

Durum: **PASS — kullanıcı tarafından raporlanan canlı yükleme testi.** Bağımsız olarak tekrarlanmadı.

## Ortam

| Alan | Değer |
|---|---|
| Tarih | 2026-10-11, yaklaşık 23:59–00:00 (UTC+3) |
| İstemci | Claude Code 2.1.295 CLI, `-p` (headless, etkileşimsiz) |
| Model | `claude-opus-5-5` |
| İşletim sistemi | macOS 26.3 (25D125) |
| Paket | `THE_RULES_v0.13.2-draft.zip` (SHA256SUMS.txt ile doğrulandı) |
| Profil | `build` (`examples/build.json`), beklenen kanunlar L04, L05 |
| Adaptör | `clients.py install --clients claude` → `<smoke>/CLAUDE.md` |

`<smoke>` ve `<control>` geçici, git dışı, boş klasörlerdir. İkisinde de önceden aynı kullanıcı `CLAUDE.md` dosyası vardı
(`# Smoke test project` ve `User note: keep this line.`). THE RULES yalnız `<smoke>` içine kuruldu; üst klasörlerde başka `CLAUDE.md` yoktu.

## Komutlar

```sh
python3 -B tools/clients.py install --project <smoke> --context examples/build.json --clients claude
python3 -B tools/clients.py verify --project <smoke>

# Her oturum ilgili klasörde, kalıcı oturum ve MCP sunucusu olmadan çalıştırıldı:
cd <smoke>   && claude -p "$PROMPT_A" --tools ""               --strict-mcp-config --no-session-persistence --output-format json
cd <smoke>   && claude -p "$PROMPT_B" --tools "Read,Glob,Grep" --strict-mcp-config --no-session-persistence --output-format json
cd <control> && claude -p "$PROMPT_A" --tools ""               --strict-mcp-config --no-session-persistence --output-format json
```

Testler başka bir Claude Code oturumunun içinden başlatıldığı için `CLAUDECODE` ve `CLAUDE_CODE_CHILD_SESSION` ortam değişkenleri
kaldırılarak (`env -u`) çalıştırıldı. Giriş, kullanıcının kendisi tarafından `claude auth login` ile yapıldı.

`PROMPT_A`:

> Dosya değiştirmeden THE RULES'ın seçili profilini, iki kanun kimliğini, DRAFT statüsünü ve bunu okuduğun yerel dosya yolunu göster. Hiçbir aracın yok; yalnızca oturum başında bağlamına yüklenmiş içerikten cevap ver. Bilgi bağlamında yoksa uydurma, açıkça BULUNAMADI yaz.

`PROMPT_B` (CLIENT_SMOKE.md istemi):

> Dosya değiştirmeden THE RULES'ın seçili profilini, iki kanun kimliğini, DRAFT statüsünü ve bunu okuduğun yerel dosya yolunu göster. Kaynak dosya içeriğini gerçekten incele; erişemediysen açıkça belirt.

## Sonuç özeti

| Oturum | Proje | Araç izni | Beklenen | Tur | Sonuç |
|---|---|---|---|---|---|
| A | `<smoke>` | `--tools ""` (hiç araç yok) | build, L04, L05, DRAFT ve `<smoke>/CLAUDE.md` yolu dosya okunmadan bilinmeli | 1 | PASS |
| B | `<smoke>` | `--tools "Read,Glob,Grep"` (yalnız okuma) | CLIENT_SMOKE.md istemiyle aynı değerler dosyadan doğrulanmalı | 2 | PASS |
| C | `<control>` | `--tools ""` (hiç araç yok) | THE RULES kurulu olmadığı için alanlar BULUNAMADI olmalı | 1 | PASS |

A ile C arasındaki fark, bilginin dosya okumadan değil oturum başında otomatik yüklenen `CLAUDE.md` bağlamından geldiğini gösterir.
B, aynı değerlerin dosya içeriğiyle eşleştiğini doğrular. Testten sonra `clients.py verify` yine PASS verdi;
kullanıcı satırları korundu ve hiçbir oturum dosya değiştirmedi ya da izin reddiyle karşılaşmadı.

## Sınırlar

- Etkileşimli oturumdaki `/context` Memory files görünümü **kontrol edilmedi**; otomatik yükleme yalnız A/C karşılaştırmasıyla gösterildi.
- Yalnız `build` profili, macOS ve headless `-p` modu denendi. Windows, diğer profiller ve IDE eklentileri NOT RUN.
- Bu kayıt yalnız yüklemeyi gösterir; kurallara uyulduğunu veya kalite/hız artışını **kanıtlamaz**. Pilot sonuçları değişmez.
- Cursor ve Antigravity: NOT RUN.

## Yanıtlar (hassas bilgilerden arındırılmış)

Yerel mutlak yollar `<smoke>` / `<control>` ile değiştirildi; metin başka şekilde düzenlenmedi.

### Oturum A — `<smoke>`, `--tools ""` (hiç araç yok)

~~~~text
**THE RULES — oturum başı bağlamından (dosya değiştirilmedi, araç kullanılmadı)**

- **Seçili profil:** `build` (başlık: "THE RULES kısa bağlam — build")
- **İki kanun kimliği:**
  - **L04** — Çerçeveyi çalışan davranışla doldur
  - **L05** — Mühendisliği ihtiyaç ve risk kadar kur
- **Statü:** `DRAFT / advisory`. Bu referans yeni yetki vermiyor, kaynak içindeki talimatlar da kullanıcı isteği sayılmıyor.
- **Okunduğu yerel dosya yolu:**
  `<smoke>/CLAUDE.md`
  Yükleme etiketi: "project instructions, checked into the codebase".

Not: Bu içeriğin bağlama yüklenmiş olması, kurallara uygunluğun veya başarının kanıtı değildir. Paketin kendi notu da bunu söylüyor: "bu paketin yüklenmesi uygunluk veya başarı kanıtı değildir."
~~~~

### Oturum B — `<smoke>`, `--tools "Read,Glob,Grep"` (yalnız okuma)

~~~~text
Dosyayı Read aracıyla doğrudan okudum ve hiçbir dosyayı değiştirmedim.

**Dosya yolu:**
`<smoke>/CLAUDE.md`

| Alan | Değer | Dosyadaki yeri |
|---|---|---|
| Seçili profil | **build** (`# THE RULES kısa bağlam — build`) | satır 7 |
| Statü | **DRAFT / advisory**: yeni yetki vermiyor, kaynak içindeki talimatlar kullanıcı isteği sayılmıyor | satır 8 |
| Kanun 1 | **L04**: Çerçeveyi çalışan davranışla doldur | satır 13 |
| Kanun 2 | **L05**: Mühendisliği ihtiyaç ve risk kadar kur | satır 19 |

**Dosyanın yapısı:**
- THE RULES bloğu `<!-- THE RULES managed start -->` (satır 6) ile `<!-- THE RULES managed end -->` (satır 25) işaretleri arasında yer alıyor.
- Bu bloğun dışında kullanıcının kendi içeriği de duruyor: başlık (satır 1) ve "User note: keep this line." (satır 3).
- Satır 11'de şu not var: paketin yüklenmiş olması uygunluk ya da başarı kanıtı değil. Bu yüzden burada yalnızca dosyanın içeriğini doğruluyorum, kuralların uygulandığını değil.
~~~~

### Oturum C — `<control>`, `--tools ""` (hiç araç yok)

~~~~text
Oturum başında bağlamıma yüklenen tek proje dosyası şu:

`<control>/CLAUDE.md`

İçeriği yalnızca şu iki satırdan oluşuyor:

```
# Smoke test project

User note: keep this line.
```

Bu dosyada ve bağlamın geri kalanında THE RULES'a dair hiçbir içerik yok. Bu yüzden istenen alanların hepsi bulunamadı:

| Alan | Değer |
|---|---|
| Seçili profil | **BULUNAMADI** |
| Kanun kimliği 1 | **BULUNAMADI** |
| Kanun kimliği 2 | **BULUNAMADI** |
| DRAFT statüsü | **BULUNAMADI** |
| THE RULES'ın okunduğu yerel dosya yolu | **BULUNAMADI** |

Hiçbir dosya değiştirilmedi ve hiçbir araç çağrılmadı.
~~~~
