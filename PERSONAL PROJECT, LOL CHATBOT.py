# the champions json file is not required now.

# Initialising a dictionary for some terms
dict = {
        "beginner" : "League of legends is a 5 vs 5 MOBA game, you have 5 roles which you can play as, namely : TOP, MID, JUNGLE, BOT, SUPPORT. Please enter any one of the role :)",
        "top" : "The top lane in League of Legends is full of fighters, divers, and beefy tanks. You'll mostly have 1 vs 1 in this lane",
        "mid" : "The mid lane is the most important lane in League of Legends. As such, the mid laner plays a pivotal role in how the game pans out. You'll find most of the assassin's, mages here.",
        "jungle" : "A Jungler is a role often seen in Summoner's Rift and Twisted Treeline . A Jungler earns gold and levels up through experience via the neutral creeps located in between the lanes, better known as “the jungle”. It is one of the hardest roles to master as it needs a lot of game sense. Different types of champions can fit in this role.",
        "bot" : "This is a lane in which you'll find all the marksman and they will be supported by the \"SUPPORTS\". it's for those who like 2 vs 2. They are also called AD Carry(ADC)",
        "support" : "As the name suggests you will support your ADC with your kit. As a support you will roam around the summoners rift and place vision wards and help your team to win the game. It's for those who don't want kills but want to assist the team.",
        "reccomendedTopBeg" : ["garen", "mordekaiser", "nasus", "sett", "teemo"],
        "reccomendedMidBeg" : ["malzahar", "annie", "vex", "veigar"],
        "reccomendedJgBeg" : ["masteryi", "warwick", "rammus", "volibear"],
        "reccomendedSupBeg" : ["yuumi", "lux", "lulu", "karma"],
        "reccomendedAdcBeg" : ["missfortune", "caitlyn", "jinx", "ashe"],
}


def main():
    print("Hi! I'm Poro your beginner friendly league of legends chatbot. Please specify wther you are a beginner or experienced player:)")
    text = input().lower().replace("experienced", "exp")
    count = 0
    while "beginner" not in text and "exp" not in text:
        if count > 4:
            print("Since you did not ask any queries I hope there is nothing to solve, thanks for chating with me.")
            break
        if text == "":
            print("Go on, I'm listening")
            count += 1
        if text.find("hi") + 1 or text.find("hello") + 1:
            print("Hello, please specify whether you are a beginner or experienced player")
            count += 1
        if text.find("bye") + 1:
            print("Bye, Have a great time!")
            break
        text = input().lower()

    if "beginner" in text:
        beginner(text)

    elif "exp" in text:
        while True:
            champ = input("Please type the champion name that you want to know about: ")
            print(f"Here is the site in which you can find all the builds for {champ}: https://www.op.gg/champions/{champ}/build/top?region=global&tier=emerald_plus")
            confirmation = input("Do you want information on any other champs(Yes/No): ").lower()
            if confirmation == "yes":
                continue
            else:
                print("Thanks for chosing me, hope I fullfilled your queries.")
                break


#Defining a funciton for beginners reply

def beginner(textParam):
    checker = 0
    print(dict["beginner"])
    text2 = input().lower()
    while "beginner" in textParam:
        if "top" in text2 or "mid" in text2 or "jungle" in text2 or "bot" in text2 or "support" in text2:
            if "top" in text2:
                beginnerRec("top","reccomendedTopBeg")
            if "mid" in text2:
                beginnerRec("mid","reccomendedMidBeg")
            if "jungle" in text2:
                beginnerRec("jungle","reccomendedJgBeg")
            if "bot" in text2:
                beginnerRec("bot", "reccomendedAdcBeg")
            if "support" in text2:
                beginnerRec("support", "reccomendedSupBeg")

            text2 = input().lower()
        else:
            print("Please specify one of the following roles: top, mid, jungle, bot, support")
            text2 = input().lower()

        #Stopping the function if any of the below words are in the text
        endWords = sorted(["done", "thank", "enough", "no","goodbye", "bye", "exit", "quit", "stop", "finish", "over", "close", "end", "farewell", "later", "adios", "ciao", "see you", "ta-ta"])
        for i in endWords:
            if text2.find(i)+1:
                print("It was my pleasure interacting with you. Thanks")
                checker = 1
                break
        if checker == 1:
            break


#Defining a function to print out the beginner recommendations for respective lane called
#Used the below function inside the function "beginner"

def beginnerRec(role,reccomended):
    print(dict[role],"recommended champions are",dict[reccomended], "Please select the champion given in the list")
    recommendedChamp = input()
    #Using a while loop to print op.gg link for a particular champ in the recommended list
    while recommendedChamp in dict[reccomended]:
        print(f"Here is the site in which you can find all the builds for {recommendedChamp}: https://www.op.gg/champions/{recommendedChamp}/build/top?region=global&tier=emerald_plus")
        check = input(f"Any other champs you want to know about in {role} lane?(yes/no):").lower()
        if check == "yes":
            recommendedChamp = input(f"whom do you want to learn more about {dict[reccomended]}: ")
        else:
            print("Any other lanes you want to know about")
            break

if __name__ == "__main__"
    main()
