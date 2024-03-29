import aiohttp

from plugin_system import Plugin

plugin = Plugin("Скриншот сайта",
                usage=["скрин [адрес сайта] - сделать скриншот сайта [адрес сайта]"])


@plugin.on_command('скрин')
async def screen(msg, args):
    if not args:
        return await msg.answer('Вы не указали сайт!')

    async with aiohttp.ClientSession() as sess:
        async with sess.get("http://mini.s-shot.ru/1024x768/1024/png/?" + args.pop()) as resp:
            result = await msg.vk.upload_photo(await resp.read())

            return await msg.answer('Держи', attachment=str(result))
