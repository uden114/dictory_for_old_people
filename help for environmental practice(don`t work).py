import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command
async def what_is_ep(ctx):
    await ctx.send(f"Экопросветительская практика — разновидность социальной практики, предполагающая формирование у населения норм, ценностей, образцов экологичного поведения, а также распространение знаний, умений, навыков в сфере практической экологической деятельности, результатом которой является повышение экологической грамотности населения и развитие экологической культуры и сознания.")
@bot.command
async def what_are_TWTRE(ctx):
    await ctx.send(f"Существует множество способов минимизации отходов. Вот несколько из них: Покупайте товары длительного пользования. Выбирайте вещи, которые прослужат годами, а не одноразовые или дешёвые предложения. Откажитесь от спонтанных покупок ненужных вещей. Перед покупкой задумайтесь, как часто вы будете использовать эту вещь и сколько она вам прослужит. Используйте меньше бумаги на кухне и проявляйте заботу об окружающей среде.Замените вредные бытовые чистящие средства и продукты безопасными альтернативами.Если вы живете в частном доме, создайте компостную кучу на заднем дворе. В России около 40 процентов всех твердых бытовых отходов составляют пищевые отходы. Подвозите друг друга на работу, используйте общественный транспорт и велосипеды.")

@bot.command  
async def what_do(ctx):
    await ctx.send(f'Напишите одну из комманд(what_is_ep,  what_are_TWTRE)')

bot.run("Вставь сюда токен своего бота")
