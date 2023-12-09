def handle_message(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey There!'
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')