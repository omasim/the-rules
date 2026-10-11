# THE RULES

AI ile yazılım üretimi için deneysel, kaynak izli bir çalışma rehberi. Yeterli planlama, ihtiyaç kadar mühendislik ve doğrulanmış teslim hedeflenir. **Ek kalite veya hız faydası henüz gösterilmedi.**

Ürün sekiz çekirdek kanundur: her birinin tetikleyicisi, kontrolü ve durma/orantı koşulu vardır. Güncel görev, kabul ve aşama canlı oturumdan gelir; kurulumda sabitlenmez. Küçük işte tüm aşamaları baştan yürütmek gerekmez. Ajanın doğru kanunu seçtiği varsayılmaz; bu da sınanmalıdır.

```sh
python3 -B tools/clients.py install --project /projenin/tam/yolu --clients claude,cursor,antigravity
python3 -B tools/clients.py verify --project /projenin/tam/yolu
python3 -B tools/clients.py remove --project /projenin/tam/yolu
```

Codex için aynı araçta --clients codex kullan. Tek araç seçilebilir; Codex'i Cursor/Antigravity ile birlikte seçme, ortak AGENTS keşfi çift yüklemeye yol açabilir. Profil değişimi için kurulum söküp takmak artık gerekmez; yeni varsayılan görev/aşama taşımıyor.

library/ içindeki diğer 236 kayıt benimsenmemiş araştırma/aday arşividir; yeni varsayılan bağlama yüklenmez. Tarihsel katalog ve profiller korunur. Eski kurulumlar otomatik değiştirilmez; [geçiş belgesini](docs/MIGRATION_0.14.md) izle.

Önceki Claude/Antigravity yükleme sonuçları iki-kanun build profiline aittir. Yeni sekizli rehberin canlı yüklemesi henüz NOT RUN. Lisans eklenmedi; genel yeniden kullanım hakkı veya açık kaynak iddiası yok.

[Tam kullanım](README.md) · [Kanıtlar](docs/EVIDENCE.md) · [Yeni deney önerisi](docs/NEXT_EXPERIMENT.md).
