from rcon.source import Client
from disnake import ApplicationCommandInteraction, Embed, Intents
from disnake.ext import commands

intents = Intents.all()
bot = commands.Bot(intents=intents)


@bot.slash_command(description="Send a command to your csgo server (specifying ip, port, passwd)")
async def rcon(ctx, ip: str = None, port: int = None, passwd: str = None, command: str = None):
    channel = bot.get_channel(channel id for admin logs)
    if ctx.author.get_role(admin role id):

        ephemeralEmbed = Embed()
        ephemeralEmbed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar)
        ephemeralEmbed.set_footer(text="Bot by end41r", icon_url="https://cdn.discordapp.com/avatars/410118481132912650/0eef06b3e937c1cab2f127e992bc9531.png?size=1024")   

        if(ip == None or port == None or passwd == None):
            ephemeralEmbed.title = "Execution failed"
            ephemeralEmbed.description = f"Not enough parameters:\nip : `{ip}`\nport : `{port}`\npassword : `{passwd}`"
            ephemeralEmbed.color = 0xff0000

            await ctx.send(embed=ephemeralEmbed, ephemeral=True)

        else:
    
            try: 
                with Client(ip, port, passwd=passwd) as client:
                    answer = client.run(command)
            except:
                answer = "no response"
            logEmbed = Embed(title=f"User {ctx.author} executed a command", description=f"Command\n```{command}```\n\nServer response\n```{answer}```\n\nServer IP\n```{ip}:{port}```", color=0x00ff00)
            logEmbed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar)
            logEmbed.set_footer(text="Bot by end41r", icon_url="https://cdn.discordapp.com/avatars/410118481132912650/0eef06b3e937c1cab2f127e992bc9531.png?size=1024")

            ephemeralEmbed.title = f"{ctx.author}! command executed"
            ephemeralEmbed.description = f"Command\n```{command}```\n\nServer response\n```{answer}```\n\nServer IP\n```{ip}:{port}```"
            ephemeralEmbed.color = 0x00ff00

            await ctx.response.defer()
            await ctx.followup.send(embed=ephemeralEmbed, ephemeral=True)

            await channel.send(embed=logEmbed)
    
    else:
        errEmbed = Embed(title="You dont have enough permissions to do this!", description="Get admin role first", color=0xff0000)
        
        await ctx.response.defer()
        await ctx.followup.send(embed=errEmbed, ephemeral=True)

        await channel.send(embed=Embed(title=f"{ctx.author} tried to execute following command `{command}`", description=f"Following password was used: `{passwd}`"))
        

bot.run("token")
