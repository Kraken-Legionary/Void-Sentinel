import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

# Замените 'your_actual_bot_token_here' на токен вашего бота
TOKEN = 'MTIzMDQ2NDE3Njc0NTQ4MDI1NA.G7uu_g.sihXhDevpS1wXkvTmYE0eneW9qspNA-MHffask'

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

@bot.tree.command(name="статус", description="Check the bot's latency")
async def status(interaction: discord.Interaction):
    latency = bot.latency * 1000  # Latency in milliseconds
    await interaction.response.send_message(f'Задержка бота: {latency:.2f}ms')

# Запуск бота
bot.run(TOKEN)
