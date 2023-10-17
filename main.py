import discord
from discord.ext import commands
import os
import asyncio

bot = commands.Bot(command_prefix=".",self_bot=True)

@bot.event
async def on_ready():
    print("\033[94m" + """
███╗░░░███╗░█████╗░███████╗██╗░█████╗░
████╗░████║██╔══██╗██╔════╝██║██╔══██╗
██╔████╔██║███████║█████╗░░██║███████║
██║╚██╔╝██║██╔══██║██╔══╝░░██║██╔══██║
██║░╚═╝░██║██║░░██║██║░░░░░██║██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
""" + "\033[0m" + "Made By @Mafiayt69")



    cloneguildid = int(input("\nWhich Guild You Want To Clone Guild Id : "))
    ownguildid = int(input("Where You Want To Clone Guild Id : "))
  
    cloneguild = bot.get_guild(cloneguildid)
    ownguild = bot.get_guild(ownguildid)

    for role in ownguild.roles:
        if role.name != "@everyone":
            await role.delete()
            await asyncio.sleep(1)
    for channel in ownguild.channels:
        await channel.delete()
        # await asyncio.sleep(1)


    roles = {}
    for role in cloneguild.roles[::-1]:
        permissions = role.permissions
        color = role.color
        role = await ownguild.create_role(name=role.name, permissions=permissions,color=color)
        roles[role.id] = role
        # await asyncio.sleep(1)

 
    for category in cloneguild.categories:
        categorys = await ownguild.create_category(category.name, overwrites=category.overwrites)
        # await asyncio.sleep(1)

        for channel in category.channels:
            if isinstance(channel, discord.TextChannel):
                channelss = await categorys.create_text_channel(channel.name, overwrites=channel.overwrites)
            elif isinstance(channel, discord.VoiceChannel):
                channelss = await categorys.create_voice_channel(channel.name, overwrites=channel.overwrites)
                # await asyncio.sleep(1)

            await channelss.edit(sync_permissions=True)
            # await asyncio.sleep(1)
            
        if role.name != "@everyone":
            await role.delete()
            

    rolename = ", ".join([role.name for role in roles.values()])
    categoryname = ", ".join([category.name for category in ownguild.categories])
    channelname = ", ".join([channelss.name for channelss in ownguild.text_channels])


    print(f"roles : {rolename}")
    print(f"category : {categoryname}")
    print(f"channel : {channelname}")
  
    




bot.run(os.environ.get("token"),bot=False)