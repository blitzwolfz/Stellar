import json

from discord.ext import commands


def admin_or_owner():
    def predicate(ctx):
        if ctx.message.author.id == 670564722218762240:
            return True
        elif ctx.message.author.permissions_in(channel=ctx.message.channel).administrator:
            return True
        else:
            return False

    return commands.check(predicate)


def manage_messages_or_owner():
    def predicate(ctx):
        if ctx.message.author.id == 670564722218762240:
            return True
        elif ctx.message.author.permissions_in(channel=ctx.message.channel).manage_messages:
            return True
        else:
            return False

    return commands.check(predicate)


def check_account():
    async def predicate(ctx):
        with open('users.json', 'r') as f:
            users = json.load(f)
        if str(ctx.author.id) in users.keys():
            return True
        raise commands.BadArgument(f'You don\'t have an account! Use `{ctx.prefix}create` to create one!')

    return commands.check(predicate)
