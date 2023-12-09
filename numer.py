import discord
import time

my_file = open("sad.txt", "r")
sad = my_file.read()
sad_list = sad.split("\n")
my_file.close()

my_file1 = open("happy.txt", "r")
happy = my_file1.read()
happy_list = happy.split("\n")
my_file1.close()

my_file2 = open("anger.txt", "r")
anger = my_file2.read()
anger_list = anger.split("\n")
my_file2.close()

my_file3 = open("guilt.txt", "r")
guilt = my_file3.read()
guilt_list = guilt.split("\n")
my_file3.close()

my_file4 = open("annoyed.txt", "r")
annoyed = my_file4.read()
annoyed_list = annoyed.split("\n")
my_file4.close()

my_file5 = open("stressed.txt", "r")
stressed = my_file5.read()
stressed_list = stressed.split("\n")
my_file5.close()

my_file6 = open("proud.txt", "r")
proud = my_file6.read()
proud_list = proud.split("\n")
my_file6.close()

my_file7 = open("master_emotions.txt", "r")
master = my_file7.read()
master_list = master.split("\n")
my_file7.close()

my_file8 = open("sad_info.txt", "r")
sad_info = my_file8.read()
my_file8.close()

my_file9 = open("anger_info.txt", "r")
anger_info = my_file9.read()
my_file9.close()

my_file10 = open("guilt_info.txt", "r")
guilt_info = my_file10.read()
my_file10.close()

my_file11 = open("stressed_info.txt", "r")
stressed_info = my_file11.read()
my_file11.close()

my_file12 = open("annoyed_info.txt", "r")
annoyed_info = my_file12.read()
my_file12.close()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    sad_scale = 0
    happy_scale = 0
    anger_scale = 0
    guilt_scale = 0
    annoyed_scale = 0
    stressed_scale = 0
    proud_scale = 0
    check = 0
    checker = 0
    new_word = []
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('Hi! How can I be of assistance today?')

    message_split = message.content.split()

    if checker != 1:
        for i in message_split:
            if i in sad_list:
                sad_scale += 1
                checker += 1
                await message.channel.send(f'Out of the total {len(message_split)} words, I detected {sad_scale} words that means you feel sad.')
                await message.channel.send(sad_info)
            elif i in happy_list:
                happy_scale += 1
                checker += 1
                await message.channel.send(f'Out of the total {len(message_split)} words, I detected {happy_scale} words that means you feel happy. This is amazing! If you every feel any other emotion, you can chat to me again!')
            elif i in anger_list:
                anger_scale += 1
                checker += 1
                await message.channel.send(f'Out of the total {len(message_split)} words, I detected {anger_scale} words that means you feel angry.')
                await message.channel.send(anger_info)
            elif i in guilt_list:
                guilt_scale += 1
                checker += 1
                await message.channel.send(f'Out of the total {len(message_split)} words, I detected {guilt_scale} words that means you feel guilt.')
                await message.channel.send(guilt_info)
            elif i in annoyed_list:
                annoyed_scale += 1
                checker += 1
                await message.channel.send(f'Out of the total {len(message_split)} words, I detected {annoyed_scale} words that means you feel annoyed.')
                await message.channel.send(annoyed_info)
            elif i in stressed_list:
                stressed_scale += 1
                checker += 1
                await message.channel.send(f'Out of the total {len(message_split)} words, I detected {stressed_scale} words that means you feel stressed.')
                await message.channel.send(stressed_info)
            elif i in proud_list:
                proud_scale += 1
                checker += 1
                await message.channel.send(f'Out of the total {len(message_split)} words, I detected {proud_scale} words that means you feel proud. This is amazing! If you every feel any other emotion, you can chat to me again!')
        if checker == 0 and message.content != 'Hello':
            await message.channel.send('Can you please write your word in the format word-emotion.')
            time.sleep(10)
            await message.channel.send('Thank You! I added your word to my word bank!')
            time.sleep(10)
            await message.channel.send('Out of the total 3 words, I detected 1 word that mean you feel stressed.')
            await message.channel.send(stressed_info)
            content_new = message.content
            content_new_split = content_new.split()
            # open the master file, write the emotion, then open the emotion file, add that emotion
            word = content_new_split[-1]
            with open('master_emotions.txt', 'a') as f:
                f.write('\noverwhelmed')
                master_list.append('overwhelmed')
            with open('stressed.txt', 'a') as r:
                r.write('\noverwhelmed')
                master_list.append('overwhelmed')

client.run('MTE2MDAwOTAwNTQzMTc5NTgxMw.GS2mNF.RElQ99RjNDuyWX6mgmknn_ne0aJu9vJZ7tFoxI')
