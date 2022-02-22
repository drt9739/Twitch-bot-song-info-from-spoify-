import json

from twitchio.ext import commands
from twitchio.ext import eventsub
import urllib

import config
import spotify_req


# This is the main code, do not touch anything to avoid problems

class Bot(commands.Bot):

    def __init__(self):

        super().__init__(token=config.TOKEN_TWITCH, prefix=config.PREFIX, initial_channels=config.channels)

    async def event_ready(self):

        print(f'Logged in as | {self.nick} | in channel {config.channels}')

    async def event_message(self, message):

        if message.echo:
            return

        print(message.content)

        await self.handle_commands(message)

    @commands.command()
    async def song(self, ctx: commands.Context):

        request = spotify_req.spotify_request()

        if spotify_req.status():

            await ctx.send(
                f'Сейчас играет трек 🎵 {request["name"]} - {request["autor"]}. Ссылка на трек VeryBased : {request["url"]}')

        else:

            await ctx.send(f'Ничего не играет Okayge')

    @commands.command()
    async def update(self, ctx: commands.Context):

        url = f"https://tmi.twitch.tv/group/user/{''.join(config.channels)}/chatters"
        req = urllib.request.Request(url, headers={"accept": "/"})
        res = urllib.request.urlopen(req).read()
        data = json.loads(res)

        if ctx.message.author.name in data['chatters']['broadcaster'] or ctx.message.author.name in data['chatters'][
            'moderators']:

            spotify_req.data_update()
            await ctx.send(f'Успешно обновлено :)')

        else:

            await ctx.send(f'Эта команда доступна только стримеру и модератором StreamerDoesntKnow')


bot = Bot()
bot.run()
