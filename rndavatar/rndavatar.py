import discord
from discord.ext import commands
from random import choice, randint
import asyncio
import aiohttp
import glob


class RndAvatar:
    """Changes the bot's image every so often"""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
        self.images = glob.glob("data/rndavatar/*.png")
        self.loop = bot.loop.create_task(self.change_avatar())
        self.status ={
                    "farrukopicture1"    : discord.Status.online,
                    "farrukopicture2"    : discord.Status.dnd,
                    "farrukopicture3"    : discord.Status.idle,
                    "farrukopicture4"    : discord.Status.dnd    
                    "farrukopicture5"    : discord.Status.idle
                    "farrukopicture6"    : discord.Status.online
                    "farrukopicture7"    : discord.Status.dnd
                    "farrukopicture8"    : discord.Status.idle
                    "farrukopicture9"    : discord.Status.dnd
                    "farrukopicture10"    : discord.Status.online
                   }
    
    def __unload(self):
        self.session.close()
        self.loop.cancel()
    
    async def change_avatar(self):
        await self.bot.wait_until_ready()
        while self is self.bot.get_cog("RndAvatar"):
            data = None
            server = self.bot.get_server(id="453713529502171148")
            current_game = server.me.game if server is not None else None

            try:
                # async with self.session.get(choice(self.url)) as r:
                    # data = await r.read()
                new_avatar = choice(self.images)
                image_name = new_avatar.split("/")[-1].split(".")[0]
                with open(new_avatar, "rb") as image:
                    data = image.read()
                if image_name.lower() in self.status:
                    status = self.status.get(image_name.lower(), None)
                    await self.bot.change_presence(status=status, game=current_game)
                print("changing avatar to {}".format(image_name))
                await self.bot.edit_profile(avatar=data)
            except Exception as e:
                print(e)
            await asyncio.sleep(randint(1000, 2000))

def setup(bot):
    n = RndAvatar(bot)
    bot.add_cog(n)
