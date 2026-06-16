import discord
from discord.ext import commands
import database

# Botun ön eki (prefix) ve gerekli izin ayarları
intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriğini okuyabilmek için şart
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    """Bot başarıyla açıldığında tetiklenir."""
    # Veritabanını kontrol et ve yoksa oluştur
    database.init_db()
    print(f"🤖 Bot başarıyla giriş yaptı: {bot.user.name}")
    print("🗄️ Veritabanı kontrol edildi/oluşturuldu.")

@bot.command(name="ekle")
async def ekle_komutu(ctx, *, habit_name: str = None):
    """Kullanım: !ekle spor"""
    if habit_name is None:
        await ctx.send("❌ Lütfen eklemek istediğiniz alışkanlığın adını yazın. Örnek: `!ekle spor`")
        return

    user_id = ctx.author.id
    database.add_habit(user_id, habit_name)
    await ctx.send(f"✅ **{habit_name}** alışkanlığı bugün için başarıyla kaydedildi, harikasın! 🎉")

@bot.command(name="listele")
async def listele_komutu(ctx):
    """Kullanım: !listele"""
    user_id = ctx.author.id
    habits = database.get_habits_by_date(user_id)

    if not habits:
        await ctx.send("🤷‍♂️ Bugün henüz hiç alışkanlık kaydetmemişsin. Harekete geçme zamanı! `!ekle <alışkanlık>`")
    else:
        # Alışkanlıkları listelerken şık durması için numaralandırıyoruz
        liste_metni = "\n".join([f"🔹 {h.capitalize()}" for h in habits])
        await ctx.send(f"📋 **Bugünkü Alışkanlıkların:**\n{liste_metni}")

@bot.command(name="sil")
async def sil_komutu(ctx, *, habit_name: str = None):
    """Kullanım: !sil spor"""
    if habit_name is None:
        await ctx.send("❌ Lütfen silmek istediğiniz alışkanlığın adını yazın. Örnek: `!sil spor`")
        return

    user_id = ctx.author.id
    basarili = database.delete_habit(user_id, habit_name)

    if basarili:
        await ctx.send(f"🗑️ Bugün yaptığın **{habit_name}** kaydı başarıyla silindi.")
    else:
        await ctx.send(f"🔍 Bugün için **{habit_name}** adında bir kayıt bulunamadı.")

# Projeyi başlatmak için tokenınızı buraya yapıştırın
bot.run("TOKEN_BURAYA_GELECEK")
