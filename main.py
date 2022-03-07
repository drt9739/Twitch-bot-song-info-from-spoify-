from twitchio.ext import commands

import config
import functions
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
            if request['user'] == '':
                await ctx.send(
                    f'Сейчас играет трек 🎵 {request["name"]} - {request["autor"]}🎵 Ссылка на трек Baseg : '
                    f'{request["url"]}')
            else:
                await ctx.send(
                    f'Сейчас играет трек,  который заказал {request["user"]}:🎵 {request["name"]} - {request["autor"]} '
                    f'🎵 '
                    f'Ссылка на трек Baseg : {request["url"]}')

        else:

            await ctx.send(f'Ничего не играет Okayge')

    @commands.command()
    async def update(self, ctx: commands.Context):

        if ctx.message.author.is_mod:
            spotify_req.data_update()
            await ctx.send(f'Успешно обновлено :)')

        else:
            await ctx.send(f'Эта команда доступна только стримеру и модератором StreamerDoesntKnow')

    @commands.command()
    async def sr(self, ctx: commands.Context):
        global sr_flag
        if ctx.message.content == '&sr' or ctx.message.content == '&sr ':
            await ctx.send(
                f'@{ctx.message.author.name}, чтобы заказать трек нужно скинуть ссылка на spotify, '
                f'навзание трека или ссылку на ютуб '
                f'(не гарантируется что трек найдётся такой какой вы хотите)')
        elif '&sr on' in ctx.message.content.lower() and ctx.message.author.is_mod:
            sr_flag = True
            await ctx.send(
                f'@{ctx.message.author.name}, заказ реквестов включен :-D Чтобы закать трек нужно написать команду &sr '
                f'<ссылка на трек>')
            await ctx.send(f'Ссылка может как и на youtube и spotify. Также трек можно поставить по названию B)')
        elif '&sr off' in ctx.message.content.lower() and ctx.message.author.is_mod:
            sr_flag = False
            await ctx.send(f'@{ctx.message.author.name}, заказ реквестов выключен :( ')
        elif sr_flag:
            result = spotify_req.add_track_to_queue(functions.content_msg(ctx.message.content), ctx.message.author.name)
            await ctx.send(f'@{ctx.message.author.name} {result}')
        else:
            await ctx.send(f'@{ctx.message.author.name}, в данный момент заказ реквестов выключен.')

    @commands.command()
    async def clear(self, ctx: commands.Context):
        if ctx.message.author.is_mod:
            result = spotify_req.clear_playlist(config.spotify_playlist_id)
            await ctx.send(f'@{ctx.author.name}, {result}')
        else:
            await ctx.send(f'@{ctx.author.name}, у вас нет доступа к этой команде')

    @commands.command()
    async def volume(self, ctx: commands.Context, args1):
        try:
            volume = int(args1)
        except ValueError:
            await ctx.send(f'@{ctx.message.author.name}, введено не правильное значение.')
        if volume in range(0, 100) and ctx.message.author.is_mod:
            result = spotify_req.spotify_volume(int(args1))
            await ctx.send(f'@{ctx.message.author.name}, {result}')
        else:
            await ctx.send(f'@{ctx.message.author.name}, у вас нет доступа к этой команде')

    @commands.command()
    async def skip(self, ctx: commands.Context):
        if ctx.message.author.is_mod:
            result = spotify_req.skip()
            await ctx.send(f'@{ctx.message.author.name}, {result}')
        else:
            await ctx.send(f'@{ctx.message.author.name}, у вас нет доступа к этой команде')

    @commands.command()
    async def play(self, ctx: commands.Context):
        if ctx.message.author.is_mod:
            result = spotify_req.play()
            await ctx.send(f'@{ctx.message.author.name}, {result}')

    @commands.command()
    async def stop(self, ctx: commands.Context):
        if ctx.message.author.is_mod:
            result = spotify_req.stop()
            await ctx.send(f'@{ctx.message.author.name}, {result}')

    @commands.command(name='эмоуты')
    async def emotes(self, ctx: commands.Context):
        await ctx.send(f'Расширение для хрома: Betterttv (bttv)- https://betterttv.com/ ; 7tv - https://7tv.app/ ')
        await ctx.send(
            f'Если не хочешь заморачиваться просто скачай chatterino. Если ты с windows, устанавливай обязательно '
            f'windows-x86-64: https://github.com/SevenTV/chatterino7/releases/tag/nightly-build ')


sr_flag = False
bot = Bot()
bot.run()
