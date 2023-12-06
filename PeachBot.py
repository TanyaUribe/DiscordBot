# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:31:59 2023

@author: HP
"""

#client ID 1181707525872156782
#app ID 1181707525872156782
#public key 350baef1f25de8b3edae8c6c2ea2a15f86138df71776290c4f602a8c5d926707
#tkn MTE4MTcwNzUyNTg3MjE1Njc4Mg.G2BFV9.71C5vJwqRR6b2onrz3TTY8n3xmfVZAOODw0nlg
#INTEGER 67648

#https://discordapp.com/oauth2/authorize?client_id={CLIENTID}&scope=bot&permissions={PERMISSIONINT}

#perm integer 335743040
#https://discordapp.com/oauth2/authorize?client_id=1181707525872156782&scope=bot&permissions=335743040

#https://discordapp.com/oauth2/authorize?client_id=1181707525872156782&scope=bot&permissions=67648


import discord
import random
from discord.ext import commands
from typing import List



print(discord.__version__)  # check to make sure at least once you're on the right version!

import nest_asyncio
nest_asyncio.apply()

token = open("token.txt", "r").read()  # I've opted to just save my token to a text file. 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

peach_guild = client.get_guild(1181707525872156782)

@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'He entrado a Discord como {client.user}')  # notification of login.


@client.event
async def on_message(message):  # event that happens per any message.
    
    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    
   # if str(mention.author) == "@Peachbot#5965" and "hola" in message.content.lower(): 
   #     await message.channel.send('qué.')
        
    if str(message.author) == "tanyadinosaur#5344" and "hola" in message.content.lower(): 
        await message.channel.send('Hola. ¿Cómo te va?')
        
    elif str(message.author) == "elmatarreyes" and "hola" in message.content.lower():
        await message.channel.send('Hola. ¿Cómo te trata la vida?')
        
    elif "salgase pich" == message.content.lower():
        await client.close()
    
    elif "peach" == message.content.lower():
        await message.channel.send('Mi nombre es PeachBot')
    

    
@client.event
async def on_member_join(member):
    # Manejar cuando un miembro se une al servidor
    print(f'{member} se unió al servidor.')
    
# Defines a custom Select containing colour options
# that the user can choose. The callback function
# of this class is called when the user changes their choice
class Dropdown(discord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label='Red', description='Your favourite colour is red', emoji='🟥'),
            discord.SelectOption(label='Green', description='Your favourite colour is green', emoji='🟩'),
            discord.SelectOption(label='Blue', description='Your favourite colour is blue', emoji='🟦'),
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='Choose your favourite colour...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        await interaction.response.send_message(f'Your favourite colour is {self.values[0]}')


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


bot = Bot()


@bot.command()
async def colour(ctx):
    """Sends a message with our dropdown containing colours"""
    
    # Create the view containing our dropdown
    view = DropdownView()

    # Sending a message containing our view
    await ctx.send('Pick your favourite colour:', view=view)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

    
client.run(token)  # recall my token was saved!

        
        