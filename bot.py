import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_message(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN='MTE2MDAwOTAwNTQzMTc5NTgxMw.GdYyHn.jwHTcofWVSYAItnfG8z4V7SHW1GtNrnNcV7Z5s'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    client.run(TOKEN)