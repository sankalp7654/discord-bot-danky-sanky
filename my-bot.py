import discord
from discord.ext import commands
import requests
import time

TOKEN = open("./token.txt", "r").readline()

description = "My godfather is @sankalp_saxena. OMG you know him? I know he is amazing! Come on now, donate him some ethers here: 0xe8F59171FBFfbcf3AfF78bf7AB7035f210523249"

bot = commands.Bot(command_prefix=["sanky ", "SANKY ", "Sanky "], description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True, aliases=["Fact", "FACT"])
async def fact(context, *args):
    '''ask me a fact - [bird, dog, cat, panda, fox]'''

    args_length = len(args)

    if args_length == 1:
        # Calling API for the dog fact 
        if args[0].lower() == 'dog': 
            url = "https://some-random-api.ml/facts/dog"
            response = requests.request("GET", url)
            await context.send('Here is a :dog: fact:')
            
        # Calling API for the cat fact 
        elif args[0].lower() == 'cat':
            url = "https://some-random-api.ml/facts/cat"
            response = requests.request("GET", url)
            await context.send('Here is a :cat: fact:')

        # Calling API for the panda fact
        elif args[0].lower() == 'panda':
            url = "https://some-random-api.ml/facts/panda"
            response = requests.request("GET", url)
            await context.send('Here is a :panda_face: fact:')

        # Calling API for the bird fact
        elif args[0].lower() == 'bird':
            url = "https://some-random-api.ml/facts/bird"
            response = requests.request("GET", url)
            await context.send('Here is a :bird: fact:')

        # Calling API for the fox fact
        elif args[0].lower() == 'fox':
            url = "https://some-random-api.ml/facts/fox"
            response = requests.request("GET", url)
            await context.send('Here is a :fox: fact:')

        elif args[0].lower() == 'sankalp':
            await context.send('He is my creator! Follow him on twitter: @sankalp_saxena')

        else:
            await context.send("My master didn't told how to respond for "+ "**"+args[0]+"**")
            return

        if response.status_code == 200:
            fact_url = response.json()
            fact = fact_url['fact']
            await context.send('**'+fact+'**')
        elif response.status_code == 400:
            await context.send("Oops! I'm tired... Can't load the fact!")
    else:
        await context.send("Oops! idk what to do!")

@bot.command(pass_context=True, aliases=['PLS', 'Pls', 'pLs'])
async def pls(context, *args):
    '''shows a meme - [meme]'''
    print(args[0])
    if args[0] in ['meme', 'MEME', 'Meme']:
        url = "https://some-random-api.ml/meme"
        response = requests.request("GET", url)
        await context.send('Here is a meme for you...')
        time.sleep(1)
        if response.status_code == 200:
            meme_url = response.json()
            meme = meme_url['image']
            await context.send(meme)
        elif response.status_code == 400:
            await context.send("Oops! I'm tired enough to load the meme!")
        else:
            await context.send("My master didn't told how to respond for "+ "**"+args[0]+"**")
    else: 
        await context.send("Um! I don't respond to "+ "**"+args[0]+"**")


@bot.command(pass_context=True, aliases=['POKEDEX', 'Pokedex'])
async def pokedex(context, arg1):
    '''fetch you a pokemon - [pikachu, raichu, ...]'''
    url = "https://some-random-api.ml/pokedex?pokemon="+arg1
    response = requests.request("GET", url)
    if response.status_code == 200:
        pokemon = response.json()
        await context.send(  
        "\n" +"**pokémon:** " + pokemon['name'] + 
        "\n" +"**description:** " + pokemon['description'] + 
        "\n" + "**type:** " + ' '.join(str(x) for x in pokemon['type']) + 
        "\n" + "**height:** " + pokemon['height'] +
        "\n" + "**weight:** " + pokemon['weight'] +
        "\n" + "**xp:** " + pokemon['stats']['total'])
        await context.send(pokemon['sprites']['animated'])
     
    elif response.status_code == 400:
        await context.send("Pokedex can't recognize the pokémon!")
    
    else: 
        await context.send("I can't find pokemon named "+ "**" + arg1 + "**")

@bot.command(aliases=['PING', 'Ping'])
async def ping(ctx):
    '''Sends you pong along with latency'''
    await ctx.send(f"Pong! {bot.latency}")


bot.run(TOKEN)






        