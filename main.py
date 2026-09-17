import discord
from discord.ext import commands
import os
import asyncio

# Bật các quyền cần thiết
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã online: {bot.user} | ID: {bot.user.id}")
    print(f"Bot đang ở {len(bot.guilds)} server")
    # Đổi status bot
    await bot.change_presence(activity=discord.Game(name="!help | chạy 12h/ngày"))

@bot.event
async def on_member_join(member):
    # Code chào mừng - SỬA CHỖ NÀY
    channel = member.guild.system_channel
    if channel:
        try:
            await channel.send(f"Chào mừng {member.mention} đã vào server {member.guild.name}! 🎉")
        except:
            pass

@bot.command()
async def ping(ctx):
    """Lệnh kiểm tra bot - bạn sửa code ở đây"""
    await ctx.send(f"Pong! {round(bot.latency*1000)}ms - Bot vẫn sống!")

@bot.command()
async def hello(ctx):
    """Lệnh tự tạo - ví dụ"""
    await ctx.send(f"Hello {ctx.author.mention}! Code bot ở file main.py nè, muốn sửa gì thì sửa ở đây!")

# Đây là chỗ chạy bot - không cần sửa
# Token lấy từ biến môi trường trên Render để bảo mật
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("❌ Lỗi: Chưa có DISCORD_TOKEN! Thêm vào Environment trên Render.")
else:
    bot.run(TOKEN)
