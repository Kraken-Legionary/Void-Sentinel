import discord
from discord.ext import commands
import aiohttp
import os
from config import DISCORD_TOKEN, GUILD_ID, CHANNEL_ID, WEBHOOK_URL, GIF_URL, IMAGE_URL, check_config

# Проверяем наличие переменных окружения
check_config()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Создаём объект бота с префиксом команд и включенными интентами
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        # Регистрация команд для глобального применения
        await bot.tree.sync()
        print('Application commands synced.')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

@bot.event
async def on_member_join(member):
    if member.guild.id == GUILD_ID:
        webhook_data = {
            "content": f"Добро пожаловать на сервер клана Legion Of The Damned {member.mention}!",
            "embeds": [
                {
                    "color": 15597568,
                    "thumbnail": {
                        "url": IMAGE_URL
                    },
                    "fields": [
                        {
                            "name": "Соблюдайте правила сервера!",
                            "value": ""
                        }
                    ],
                    "image": {
                        "url": GIF_URL
                    }
                }
            ]
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(WEBHOOK_URL, json=webhook_data) as response:
                if response.status != 204:
                    print(f"Failed to send webhook message: {response.status}, {await response.text()}")
                else:
                    print("Webhook message sent successfully")

@bot.tree.command(name="задержка", description="Check the bot's latency")
async def status(interaction: discord.Interaction):
    latency = bot.latency * 1000  # Latency in milliseconds
    await interaction.response.send_message(f'Задержка бота: {latency:.2f}ms')

# Запуск бота
bot.run(DISCORD_TOKEN)
