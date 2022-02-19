from twitchio.ext import commands

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


bot = Bot()
bot.run()
