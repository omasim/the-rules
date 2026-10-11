# Uyumluluk dayanakları — 2026-10-11

Claude Code proje CLAUDE.md dosyalarını bağlam olarak okur; bunlar zorlayıcı güvenlik mekanizması değildir. Adaptör mevcut dosyaya kısa içeriği ekler; @ import davranışına ihtiyaç duymaz. [Anthropic resmî belgesi](https://code.claude.com/docs/en/memory).

Cursor proje kuralları .cursor/rules altında .mdc uzantısı ve metadata kullanır. Referans @file içeriği otomatik inline etmez; bu yüzden seçili kısa metin doğrudan rule body içinde tutulur. [Cursor resmî belgesi](https://prod.cursor.com/docs/rules).

Antigravity güncel belgelerinde .agents/rules/*.md için geçerli trigger frontmatter gerekir; eksik/yanlış değer kuralın atlanmasına neden olabilir. Bu adaptör always_on kullanır. Belgelenmiş eski .agent yolu yerine güncel .agents yolu hedeflenir. [Google resmî belgesi](https://www.antigravity.google/docs/rules/).

Bunlar dokümantasyona dayalı dosya adaptörleridir; kurulu uygulama sürümleriyle canlı uyumluluk sertifikası değildir. Daha eski Antigravity sürümü yalnız legacy yolu kullanıyorsa yerel Rules paneliyle doğrulayın; iki dizine aynı kuralları otomatik kopyalamıyoruz. Yeni sürüm değişiklikleriyle belge/adapter testi yenilenmelidir.
