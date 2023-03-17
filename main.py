import discord
from discord.ext import commands

# Create a new bot using the Discord API
bot = commands.Bot(command_prefix='!')

# Store saved links in a dictionary, using the user's Discord ID as the key
saved_links = {}

@bot.command()
async def save(ctx, link: str):
  # Save the provided link using the user's Discord ID as the key
  saved_links[ctx.author.id] = link
  await ctx.send(f"Link saved for {ctx.author.name}!")
  await ctx.author.send(f"Link saved: {link}")

@bot.command()
async def get(ctx):
  # Retrieve the saved link for the user
  link = saved_links.get(ctx.author.id)
  if link:
    await ctx.send(f"Here is the link you saved, {ctx.author.name}: {link}")
  else:
    await ctx.send(f"Sorry, {ctx.author.name}, you haven't saved any links yet.")

bot.run(MTA4NjA4MTY2MjM4NDg4MTc1OA.Gw9_gt.5C6jcLOeasvPLQzfkQpp_uT816jxROxuGbR3DI)
