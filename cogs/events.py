import json

import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        await self.bot.process_commands(after)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        with open('guildconfig.json', 'r') as f:
            guildconfig = json.load(f)

        guildconfig[str(guild.id)] = {
            "prefix": "st+"
        }

        with open('guildconfig.json', 'w') as f:
            json.dump(guildconfig, f, indent=4)

        c = self.bot.get_channel(745946456946507807)
        e = discord.Embed(colour=self.bot.colour.Stellar(), title=f'New Guild Joined: {guild}',
                          description=f'**{guild.id}**\
                                      \n**Members:** {len(guild.members)}\
                                      \n**Region:** {str(guild.region).capitalize()}\
                                      \n**Owner: ** {guild.owner}\
                                      \n**Guild Number: ** {len(self.bot.guilds)}')
        e.set_thumbnail(url=guild.icon_url)
        await c.send(embed=e)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('guildconfig.json', 'w') as f:
            guildconfig = json.load(f)

        guildconfig.pop(str(guild.id))

        with open('guildconfig.json', 'r') as f:
            json.dump(guildconfig, f, indent=4)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not len(message.mentions):
            return
        if message.content in ('<@758065684218380350>', '<@!758065684218380350>') and not message.author.bot:
            with open('guildconfig.json', 'r') as f:
                prefixes = json.load(f)
            await message.channel.send(embed=self.bot.Embed(title=f'{message.guild.me.name} » {message.guild.me.id}',
                                                            description=f'`My prefix for {message.guild.name} is {prefixes[str(message.guild.id)]["prefix"]}.`\n`Use {prefixes[str(message.guild.id)]["prefix"]}help to view my command list.`').set_thumbnail(
                url=message.guild.me.avatar_url))


def setup(bot):
    bot.add_cog(Events(bot))
