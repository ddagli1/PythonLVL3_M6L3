# 🤖 Alışkanlık Takip Botu — Proje Mimarisi

**Kullanılan Teknolojiler:** `discord.py` + `sqlite3`

---

## 📁 Dosya Yapısı

```
aliskanlik-botu/
│
├── bot.py          → Botun ana dosyası, komutlar burada
├── database.py     → Veritabanı işlemleri (kaydet, oku, sil)
└── habits.db       → SQLite veritabanı dosyası (otomatik oluşur)
```

---

## 🗄️ Veritabanı (database.py)

Tek bir tablo kullanıyoruz:

```
habits tablosu:
┌────────────────────────────────────────────┐
│ id          → Otomatik numara (1, 2, 3...) │
│ user_id     → Discord kullanıcı ID'si      │
│ habit_name  → Alışkanlık adı ("Spor")      │
│ date        → Tarih ("2025-06-09")         │
└────────────────────────────────────────────┘
```

---

## ⚙️ Bot Komutları (bot.py)

| Komut | Ne yapar? |
|---|---|
| `!ekle spor` | Bugün "spor" yaptın diye kaydeder |
| `!listele` | O günkü tüm alışkanlıklarını gösterir |
| `!sil spor` | "spor" kaydını siler |

---

## 🔄 Nasıl Çalışır? (Akış)

```
Kullanıcı Discord'da komut yazar
        ↓
bot.py komutu yakalar
        ↓
database.py'deki fonksiyonu çağırır
        ↓
SQLite veritabanına yazar / okur
        ↓
Bot sonucu Discord'a gönderir
```

---

## 👥 Takım Görev Dağılımı (Örnek)

| Kişi | Sorumluluk |
|---|---|
| **Kişi 1** | `database.py` → Tablo oluşturma, kaydetme, listeleme fonksiyonları |
| **Kişi 2** | `bot.py` → `!ekle` ve `!sil` komutlarını yazma |
| **Kişi 3** | `bot.py` → `!listele` komutunu yazma + botu test etme |

---

## 🚀 Başlangıç Adımları

1. `discord.py` kütüphanesini kur → `pip install discord.py`
2. Discord Developer Portal'dan bot oluştur, token al
3. `database.py` dosyasını yaz (önce veritabanı hazır olmalı)
4. `bot.py` dosyasını yaz ve botu çalıştır
5. Test et, hataları düzelt

---

> 💡 **İpucu:** Önce `database.py`'yi yazın ve Python'da tek başına test edin. Bot olmadan veritabanının çalıştığını gördükten sonra `bot.py`'ye geçin.
