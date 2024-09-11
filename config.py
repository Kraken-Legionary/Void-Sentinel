import os

# Получаем токен и другие параметры из переменных окружения
DISCORD_TOKEN = ('MTIzMDQ2NDE3Njc0NTQ4MDI1NA.G7uu_g.sihXhDevpS1wXkvTmYE0eneW9qspNA-MHffask')
GUILD_ID = int(('828749346505490503'))
CHANNEL_ID = int(('942706177417052160'))
WEBHOOK_URL = ('https://discord.com/api/webhooks/1261847932743847936/CRfRuEnb5zs8-n6CqzeSLiQC5OniIpPBPPF7qaHtUQvOyFzwwtC3Mvug4Wzyj-JDfC1X')
GIF_URL = ('https://media.tenor.com/Z4qdmT3xzJ4AAAAM/welcome-server.gif')
IMAGE_URL = ('https://cdn.discordapp.com/attachments/1135596941208731740/1225024888893341737/c24a13f91b7bff36adcd904f4e2e2c01-removebg-preview.png?ex=669c3615&is=669ae495&hm=4399b705a62647a7e3a0afd4b2bcd16aeafdc7b4e8aef17480facf61a0e05bf5&')

# Проверка наличия необходимых переменных
def check_config():
    if not all([DISCORD_TOKEN, GUILD_ID, CHANNEL_ID, WEBHOOK_URL, GIF_URL, IMAGE_URL]):
        raise ValueError("Не все переменные окружения установлены")
