import discord
from discord.ext import commands
import os
from flask import Flask
import threading

# --- PHẦN 1: TẠO WEB GIẢ ĐỂ RENDER KHÔNG TẮT BOT (QUAN TRỌNG) ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot SuperX đang chạy 24/7!"

def run_web():
    # Render sẽ cấp PORT tự động
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Chạy web ở 1 luồng riêng
threading.Thread(target=run_web).start()

# --- PHẦN 2: CODE BOT DISCORD CỦA BẠN (ĐÃ HOÀN THIỆN) ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã online: {bot.user} | ID: {bot.user.id}")
    print(f"Bot đang ở {len(bot.guilds)} server - Sẵn sàng 24/7!")
    await bot.change_presence(activity=discord.Game(name="!help | chạy 24/7"))

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        try:
            await channel.send(f"Chào mừng {member.mention} đã vào **{member.guild.name}**! 🎉")
        except:
            pass

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! {round(bot.latency*1000)}ms")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}! Mình là SuperX Bot, đang chạy 24/7 nè!")

# Chạy bot
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("❌ Lỗi: Chưa có DISCORD_TOKEN! Bạn phải thêm vào Render > Environment")
else:
    bot.run(token)
