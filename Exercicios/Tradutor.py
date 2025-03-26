from googletrans import Translator
import asyncio
import discord

async def traduzir():
    translator = Translator()
    result = await translator.translate('Demonstração', src='pt', dest='en')
    print(result.text)

asyncio.run(traduzir())
