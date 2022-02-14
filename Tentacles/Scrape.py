import discum
import os



def close_after_fetching(resp:object, guild_id:str, bot:object) -> None:
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched:int = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id:str, channel_id:str, bot:object) -> None:
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id, 'bot':bot}})
    bot.gateway.run()
    bot.gateway.resetSession()
    
    
    return bot.gateway.session.guild(guild_id).members
    

def main() -> list:
    global bot
    
    
    TOKEN = 'OTMyNzI5MjM5MzI3ODc1MTcz.YeXN1w.1CkI44lTQXDy8H7brLdDz83JQ9g'
    GUILD = '538047436581765127'
    SERVER = '538048710417055745'

    bot = discum.Client(token=TOKEN, log=True)
    members = get_members(GUILD, SERVER, bot)
    
    
    
    os.system('cls')
    print(f'Fetched : {len(members)}')
    return members, bot


if __name__ == '__main__':
    main()