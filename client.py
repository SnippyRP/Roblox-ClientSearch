import os
import time
import pythonroblox
import webbrowser
import random
import requests
print("Thanks for using me! Type 'commands' for help!")
while 0 < 1:
    cmddr = input("Enter a valid command: ")
    #group info
    if cmddr == "groupsearch":
        grpr = input("Group ID here: ")
        try:
            groups = pythonroblox.Groups()
            result = groups.search_id(grpr)
            groupmem = result.member_count
            groupname = result.name
            groupid = result.id
            descg = result.description
            groupown = result.owner_name
            print("Searching..")
            time.sleep(1)
            print("[" + groupname + "]", "Member Count:", groupmem, "| Group Owner:", groupown, "| Description:", descg, "| Group ID:", groupid)
        except:
            print("Error while loading group. This usually happens if the group is unclaimed or locked, please try again")
        #user searching
    if cmddr == "usersearch":
        searchval: str = input("User ID here: ")
        try:
            user = pythonroblox.User()
            resultt = user.search_id(searchval)
            username = resultt.name
            date = resultt.created_date
            des = resultt.description
            banned = resultt.banned
            userid = resultt.id
            print("Searching..")
            time.sleep(1)
            print("[" + username + "]", "UserId:", userid, "| Account Creation:", date, "| Description:", des, "| Banned:", banned)
        except:
            print("Error while searching user. Searching the user again will fix this issue")
    if cmddr == "itemsearch":
        searchvall: str = input("Item ID here: ")
        try:
            market = pythonroblox.MarketPlace()
            resulttt = market.Catalog()
            res = resulttt.search_id(searchvall)
            creator = res.creator_name
            name = res.name
            price = res.price_in_robux
            sales = res.sales
            desc = res.description
            print("Searching..")
            time.sleep(1)
            print("[" + name + "]", "By:", creator, "| Price:", price, "| Description:", desc, "| Sales:", sales)
        except:
            print("Error while searching for this item. Please try again.")
    if cmddr == "commands":
        try:
            print("________________________________________________________________")
            print("groupsearch // searches for information about a group")
            print("usersearch // searches for information about a user")
            print("itemsearch // searches for information about a hat/item")
            print("play // redirects to the roblox website")
            print("playlink // redirects to a vip server link")
            print("randomgame // redirects to a random game")
            print("commands // shows a list of commands")
            print("credits // shows the list of credits")
            print("________________________________________________________________")
        except:
            print("An unknown error occurred.")
    if cmddr == "play":
        try:
            webbrowser.open('https://roblox.com/home')
        except:
            print("An error occurred while trying to start browser.")
    if cmddr == "playlink":
        try:
            weburl = input("VIP server link here: ")
            webbrowser.open(weburl)
        except:
            print("error while redirecting")
    if cmddr == "randomgame":
        loadr = random.randint(0, 6055993180)
        print("Redirected to https://roblox.com/games/"+str(loadr))
        webbrowser.open('https://roblox.com/games/'+str(loadr))
    if cmddr == "credits":
        print("________________________________________________________________")
        print("Scripted by SnippyRO")
        print("Most scripts run with pyrhonroblox")
        print("Could not of been done without the people at stackoverflow :)")
        print("________________________________________________________________")
    else:
        print("Invalid command, check 'commands'")
