import Scrape

def main():
    members, bot = Scrape.main()
    print(members)

    for member in members:
        print(member)
        #newDM = bot.createDM([member]).json()["id"] 
        bot.sendMessage(member, "hello")
        

if __name__ == "__main__":
    main()


