import discord
import aiohttp  # Используем aiohttp для асинхронных запросов

TOKEN = 'MTIzMDQ2NDE3Njc0NTQ4MDI1NA.G7uu_g.sihXhDevpS1wXkvTmYE0eneW9qspNA-MHffask'
GUILD_ID = 828749346505490503
CHANNEL_ID = 942706177417052160
WEBHOOK_URL = 'https://discord.com/api/webhooks/1261847932743847936/CRfRuEnb5zs8-n6CqzeSLiQC5OniIpPBPPF7qaHtUQvOyFzwwtC3Mvug4Wzyj-JDfC1X'
GIF_URL = 'https://media.tenor.com/Z4qdmT3xzJ4AAAAM/welcome-server.gif'
IMAGE_URL = 'https://cdn.discordapp.com/attachments/1135596941208731740/1225024888893341737/c24a13f91b7bff36adcd904f4e2e2c01-removebg-preview.png?ex=669c3615&is=669ae495&hm=4399b705a62647a7e3a0afd4b2bcd16aeafdc7b4e8aef17480facf61a0e05bf5&'

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_member_join(member):
    if member.guild.id == GUILD_ID:
        webhook_data = {
            "content": f"Приветствую {member.mention}!",
            "embeds": [
                {
                    "color": 15597568,
                    "thumbnail": {
                        "url": IMAGE_URL
                    },
                    "fields": [
                        {
                            "name": "Соблюдайте правила!",
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

client.run(TOKEN)
