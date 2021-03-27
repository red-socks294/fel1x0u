# This is a discord bot. It's prefix is &
# install modules: pip install asyncio discord



# Start of code
import discord
import random
from discord.ext import commands, tasks
import os
from itertools import cycle
#import youtube_dl
import json
import asyncio
import shutil
from discord.utils import get
from os import system
from time import sleep

client = commands.Bot(command_prefix = '&', intents=discord.Intents.default())
prefix = '&'

@client.event
async def on_ready():
        print('Bot is ready.')
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("I am an bot"))
        print(f"The bot's prefix is {prefix}\n")
	#Tanks to meme for solving the join issue
	#aka  worship him
        print('Logs start here')





@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
	responses = ['It is certain.',
				 'It is decidlely so.',
				 'Without a doubt.'
				 'Yes - definitely.'
				 'You may rely on it.',
				 'As I see it, yes.',
				 'Most likely.',
				 'Outloock good.',
				 'Yes',
				 'Signs point to yes.',
				 'Reply hazy, try again.',
				 'Ask again later.',
				 'Better not tell you now.',
				 'Cannot predict now.',
				 'Just owo with it.',
				 'Dont count on it.',
				 'My reply is no.',
				 'My resources say no.',
				 'Yahoo piece of shit.',
				 'Very doubtful.',
				 'shut the fuck up.',
				 'No you',
                                 'Shut up']

	await ctx.send(f'The 8ball says: {random.choice(responses)}')

@client.command()
async def clearmsg(ctx, amount : int):
	await ctx.channel.purge(limit=amount+1)
	print(f"The bot has cleared {amount+1} messages!")
	sleep(5)
	await ctx.channel.purge(1)
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
#	print(f"The bot has kicked {member} for {reason}!")
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member.mention}')
	print(f"The bot banned {member} for {reason}.")
@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user

		if(user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
			print(f'The bot unbanned {user.name}#{user.discriminator}!')
			return

client.run("")
# Put your token here
