import discord  # install module
import time
import os

"""
secret_TOKEN -> discord API link to bot
trash_ID -> numerical ID for designated 'trash channel'
"""

client = discord.Client()


# Messages repository
friday_message = """ :letsgo: :letsgo: :letsgo: 
https://www.youtube.com/watch?v=1TewCPi92ro"""
saturday_message = """ :letsgo: :letsgo: :letsgo: 
:video_game: :video_game: :video_game: 
https://www.youtube.com/watch?v=Y962JdA32lk"""
activation_message = """>>> Bot is *ONLINE* -- Hacking the mainframe...
   Auto post Mufasa ------ Friday, 8 AM
   Auto post Futurama ---- Saturday, 7 PM"""


# Custom function for scheduling
async def start_Auto_Messages(message):

    target_channel = message.channel
    trash_channel = client.get_channel(trash_ID)



    # Send message to the target channel indicating bot activation
    await target_channel.send(activation_message)


    # ---------- Set important variables ---------- #
    # Set reminder - target friday
    current_time = int( time.time() )
    starting_friday = 1654866003        # epoch time for Fri-June 10, 2022 @ 8am+3seconds
    friday = starting_friday

    # Target Satuday
    starting_saturday = 1654992003      # epoch time for Sat-June 11, 2022 @ 7pm+3seconds
    saturday = starting_saturday

    # increment by 1 week until target days are greater than current_time
    while friday < current_time:
        friday += 604800      # 1 week = 604800 seconds
    while saturday < current_time:
        saturday += 604800
    


    # Enter infinite loop that constantly checks the time and posts message at appropriate time    
    while True:
        
        try:
            current_time = int( time.time() )

            if current_time >= friday:
                # Send Friday message at 8am
                await target_channel.send(friday_message)
                friday += 604800
            
            elif current_time >= saturday:
                # Send Saturday message at 7pm
                await target_channel.send(saturday_message)
                saturday += 604800
                
            
            # change channel number
            await trash_channel.send("keeping bot online...")
            time.sleep(50)
        
        # Exit condition via KeyboardInterrupt
        except KeyboardInterrupt:
            break
    
    # Implement in the future
    """
    # Terminate/exit the script
    print("Weekend Messenger bot shutting down...")
    print( time.ctime() )
    try:
        exit(0)
    except SystemExit:
        os._exit(0)
    """


# on_ready event when client goes ONLINE
@client.event
async def on_ready():
    print( "{0.user} is online!".format(client) )


# perform certain actions based on chat command
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!startWeekend'):
        await start_Auto_Messages(message) 
    
    
    # Upcoming features
    """
    if message.content.startswith('!friday'):
        await message.channel.send(friday_message)
    
    if message.content.startswith('!saturday'):
        await message.channel.send(saturday_message)
    """


# run the client and connect to discord API via token
client.run(secret_TOKEN)