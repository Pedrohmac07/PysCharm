import discord
from discord.ext import commands
import yt_dlp
import asyncio


intents = discord.Intents.default()
intents.message_content = True  # Garante que o bot leia os comandos
bot = commands.Bot(command_prefix="!", intents=intents)

# Playlist e volume
playlist = []
volume = 0.2

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def tocar(ctx, *, pesquisa):
    """Adiciona uma música ou playlist à fila e toca a primeira música se estiver vazia."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': False,
        'quiet': True,
        'extract_flat': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(pesquisa, download=False)

            if 'entries' in info:
                # Se for uma playlist
                for entry in info['entries']:
                    url = entry['url']
                    title = entry['title']
                    duration = entry.get('duration', 0)  # Usa 0 se a duração não estiver presente
                    playlist.append((title, url, duration))
                await ctx.send(f'Adicionadas {len(info["entries"])} músicas à playlist.')
            else:
                # Se for um vídeo
                url = info['url']
                title = info['title']
                duration = info.get('duration', 0)  # Usa 0 se a duração não estiver presente
                playlist.append((title, url, duration))
                await ctx.send(f'Adicionada à playlist: {title}')

        except Exception as e:
            await ctx.send(f'Erro ao buscar vídeo ou playlist ❌: {e}')
            return

    if len(playlist) == 1 and not ctx.voice_client:
        if ctx.author.voice and ctx.author.voice.channel:
            canal = ctx.author.voice.channel
            await canal.connect()

            await tocar_proxima_musica(ctx)

        else:
            await ctx.send('Você precisa estar em um canal de voz para usar este comando 📻!')

@bot.command()
async def pular(ctx):
    """Pula a música atual."""
    if ctx.voice_client and len(playlist) > 0:
        ctx.voice_client.stop()
        playlist.pop(0)
        await tocar_proxima_musica(ctx)
        await ctx.send('Música pulada! ⏭️')
    else:
        await ctx.send('Não há músicas para pular ❌.')

@bot.command()
async def volume(ctx, v: int):
    """Ajusta o volume do bot. O valor deve estar entre 0 e 100."""
    global volume
    if 0 <= v <= 100:
        volume = v / 100
        if ctx.voice_client:
            ctx.voice_client.source.volume = volume
        await ctx.send(f'🔊 Volume ajustado para {v}%')
    else:
        await ctx.send('O volume deve estar entre 0 e 100 ❌.')

@bot.command()
async def fila(ctx):
    """Exibe as músicas na fila, mostrando o nome, a posição e a duração."""
    if len(playlist) > 0:
        fila_msg = "🎶Músicas na fila🎶:\n"
        for i, (title, _, duration) in enumerate(playlist):
            minutos = duration // 60
            segundos = duration % 60
            fila_msg += f"🎵 {i + 1}. {title} - {minutos:02}:{segundos:02}\n"
        await ctx.send(fila_msg)
    else:
        await ctx.send('A fila está vazia.')

async def tocar_proxima_musica(ctx):
    """Toca a próxima música na playlist."""
    if len(playlist) > 0:
        title, url, _ = playlist[0]
        vc = ctx.voice_client
        vc.play(discord.FFmpegPCMAudio(url), after=lambda e: print(f'Erro: {e}') if e else None)
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = volume  # Aplica o volume ajustado
        await ctx.send(f'▶️ Tocando: {title}')
    else:
        await ctx.send('A playlist terminou ❌.')

@bot.command()
async def sair(ctx):
    """Faz o bot sair do canal de voz."""
    if ctx.voice_client:
        playlist.clear()
        await ctx.voice_client.disconnect()
        await ctx.send('Sai do canal de voz! ⬅️')
    else:
        await ctx.send('Não estou em um canal de voz ❌.')

# sincronização com o bot do discord
TOKEN = "INSIRA O TOKEN DO SEU BOT AQUI"
bot.run(TOKEN)
