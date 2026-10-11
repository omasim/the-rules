# THE RULES

AI ile yazılım üretimi için kaynak izli bir kanun kütüphanesi. Amaç: problemi araştırmak, kritik varsayımı ucuzca sınamak, yeterli çerçeveyi kurmak, kapsamı koruyarak çalışan prototipe ulaşmak ve gerçek çıktıyı doğrulayarak teslim etmek.

**Deneysel / DRAFT.** Gereksiz planlama ve mimariyi azaltmayı hedefler; gereken mühendisliği atlamayı önermez. Ek kalite veya hız faydası henüz gösterilmedi.

Claude Code, Cursor, Antigravity ve Codex için yerel adaptörler var. Kütüphane 244 taslak kayıt içerir; her aşamada iki ilgili çekirdek kanun seçilir. Yeni yetki vermez, AI davranışını zorunlu kılmaz.

Python 3.9+ ve standart kütüphane yeterli. examples/build.json içindeki task ve decision_gap alanlarını gerçek işinle düzenle. Paket klasöründe:

```sh
python3 -B tools/clients.py install --project /projenin/tam/yolu --context examples/build.json --clients claude,cursor,antigravity
python3 -B tools/clients.py verify --project /projenin/tam/yolu
```

Tek araç için --clients claude, cursor veya antigravity kullan. Codex için aynı hedefte diğer kurulumu yapmadan tools/integrate.py aracını --agents ile kullan. Mevcut dosyalar korunur; aynı adlı adaptör üzerine yazılmaz. Dosyalar sonradan düzenlenmişse kaldırma silmeden durur.

Araştırma: discover; çerçeve: frame; üretim: build; değişiklik: change; teslim: deliver. Örneklerin her biri examples/ altında. Profil otomatik tahmin edilmez, bütün aşamalar küçük işte baştan yürütülmez.

[Tam kullanım](README.md) · [Kanıt özeti](docs/EVIDENCE.md) · [Gerçek istemci kontrolü](docs/CLIENT_SMOKE.md).

Henüz lisans eklenmedi; proje açık kaynak lisanslı olarak duyurulmamalı. Kanunlar ve yeni tasarım kararları benimsenmiş zorunlu politika değil, taslak/öneridir.
