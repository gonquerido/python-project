# define rooms and items
cave = {
    "name": "cave",
    "type": "door",
}
vines = {
    "name": "vines",
    "type": "door",
}
river = {
    "name": "river",
    "type": "door",
}
cliff = {
    "name": "cliff",
    "type": "door",
}
torch = {
    "name": "torch",
    "type": "key",
    "target": cave,
}
machete = {
    "name": "machete",
    "type": "key",
    "target": vines,
}
raft = {
    "name": "raft",
    "type": "key",
    "target": river,
}
confidence = {
    "name": "confidence elixir",
    "type": "key",
    "target": cliff,
}
coconut_tree = {
    "name": "coconut tree",
    "type": "furniture",
}
plane_wreck = {
    "name": "plane wreck",
    "type": "furniture",
}
tomb = {
    "name": "tomb",
    "type": "furniture",
}
rupest_painting = {
    "name": "rupest painting",
    "type": "furniture",
}
pile_of_wood = {
    "name": "pile of wood",
    "type": "furniture",
}
rock = {
    "name": "rock of fallen soldiers",
    "type": "furniture",
}
jungle = {
    "name": "middle of the jungle",
    "type": "room",
}
great_cave = {
    "name": "The Great Cave of Jumanji",
    "type": "room",
}
tomb_otrera = {
    "name": "Ancient Tomb of Queen Otrera",
    "type": "room",
}
bay_warriors = {
    "name": "Bay of Warriors",
    "type": "room",
}
outside = {
  "name": "outside"
}
all_rooms = [jungle, outside, great_cave, tomb_otrera, bay_warriors ]

all_doors = [cave, vines, river, cliff]
# define which items/rooms are related

object_relations = {
    "middle of the jungle": [coconut_tree, plane_wreck, cave],
    "plane wreck": [torch],
    "outside": [cave],
    "cave": [jungle, great_cave],
#bedroom1
    "The Great Cave of Jumanji": [rupest_painting, cave, vines, river],
    "rupest painting": [machete],
    #"outside": [vines, river],
    "vines": [great_cave, tomb_otrera],
    "river": [bay_warriors, great_cave],
#bedroom2
    "Ancient Tomb of Queen Otrera": [vines, pile_of_wood, tomb],
    #"outside": [vines],
    "pile of wood": [raft],
    "tomb": [confidence],
#living_room
    "Bay of Warriors": [rock, cliff, river],
    "cliff": [bay_warriors, outside],
    #"outside": [river, door_d]
}
# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.
INIT_GAME_STATE = {
    "current_room": jungle,
    "keys_collected": [],
    "target_room": outside
}

#defining functions for the riddles

#RIDDLE1 Guess the answer for torch (plane wrecked location)
def torch_riddle():
    
    print("You thought it would be this easy? To go to the next level, you need to prove your worth!")
    print("The tallest tree in the world is the sequoia tree. What is the average height of a sequoia tree ?\na = Around 93 meters (Statue of Liberty)\nb = Between 300 and 324 meters (Eiffel Tower)\nc = Between 50 and 85 meters (Salazar's Bridge aka 25 de abril)")
    a = "Around 93 meters (Statue of Liberty)"
    b = "Between 300 and 324 meters (Eiffel Tower)"
    c = "Between 50 and 85 meters (Salazar's Bridge aka 25 de abril)"
    response = input("What would you like to answer? Type 'a', 'b' or 'c'?").strip()
    while response != "c":
        print("Nice try, but it is incorrect. Try again\nPlease answer a or b or c")
        response = input("What would you like to answer? Type 'a', 'b' or 'c'?").strip()
        response = response.lower()
    else:
        if(response == "c"):
            print(" c- is the right answer ! Congratulations!")
            fact_curiosity = input("Did you know that per year we, HUMANS, chop around 3.5 billion and 7 billion trees, I believe that's a lot...Right? type 'a lot' or 'not at all'").strip()
            if(fact_curiosity == "a lot"):
                print("Awesome, you won a torch and a matchbox! Go further")
            else:
                print("Now you know! take care of all trees you can! By the way You won a torch and a matchbox, keep up with a good game!")
                
#RIDDLE2 Guess the letters with numbers (paintings location Cave)
def machete_riddle():
    print("You are now facing the rock carvings of the Great Cave of Jumanji.\nThe rupest painting contains a clue to the next level. Unfortunately, a word has been eroded. See if you can discover what was written a long time ago....\nThe letters that are still visible have numbers attached to them\nD-A-T-A    T-E-C-H\n4-1-20-1    20-5-3-8\nNow, find the missing word with the following clues : 13-1-3-8-5-20-5 \n ")
    answer2=input("Type your guess : ")
    answer2=answer2.lower()
    while answer2!="machete":
        print("Sorry, this is not the right guess. Try again")
        answer2=input("Type your answer : ")
        answer2=answer2.lower()
    else :
        if (answer2 == "machete"):
            print("Correct, the word was MACHETE.\nA machete is a broad blade that is frequently used to cut through rainforest undergrowth and for agricultural purposes (like cutting sugar cane).\nWell, guess what, there is a machete behind the foliage, it is now yours!")
    
                
                
                
#RIDDLE3 GUESS THE WORD (pile of wood location)
def wood_riddle():
    print("To get branches and a rope, you will have to solve this riddle :\nWhat always runs, yet doesn't walk,\noften murmurs but doesn't talk,\nhas a bed but doesn't sleep,\nhas a mouth but never eats.")
    answer3=input("Type your answer : ")
    answer3=answer3.lower() #answer is transformed into lowercase to accept capital letters
    while answer3!="river" and answer3!="a river":
        print("Sorry, this is not the expected answer. Try again")
        answer3=input("Type your answer : ")
        answer3=answer3.lower()
    else :
        if (answer3 == "river")|(answer3 == "a river"): #to accept -a river or -river as correct answers
            print("Hooray, RIVER is the correct answer. You won the branches and the rope. It might be useful in the future.")

#RIDDLE4 Rock,Paper,Scissor
def rps_riddle():
    #defining options for the game
    from random import choice
    gestures = ['rock', 'paper', 'scissors']
    #choosing the number of rounds possible of a winner(without a tie)
    n_rounds = input("As you open the tomb, the protector monkeys of Otrera appear. Now you will have to play a game of Rock, Paper, Scissors against their leader. If you win or tie you will be rewarded, if not, I hope you enjoy life in captivity\n(Enter an odd number, the monkeys suggest 1 or 3) : ")
    try:
        n_rounds = int(n_rounds)
        if n_rounds % 2 == 0:
            print("Choose an odd number, please.")
            n_rounds = 0
        elif n_rounds > 10:
            print("Choose a lower number, please.")
            n_rounds = 0
        else:
            print("Let's play ", int(n_rounds), " rounds.")
    except ValueError:
        print("To play ", n_rounds, " would be impossible.")
        n_rounds = 0

#store the number of rounds that a player must win to win the game
    import math
    rounds_to_win = math.ceil(n_rounds/2)

#two variables to store the number of rounds won
    cpu_score = 0
    player_score = 0

#function to simulate the gesture choice of the computer.
    def computer(w):
        return choice(w)

#function that asks the player which is the gesture
    def hand(x):
        player = 0
        while player == 0:
            player = input("Please choose: " + str(x) + " : ")
            if player in x:
                return player
            else:
                print("You heathen. Play by the rules.")
                player = 0

#function that checks who won a round
    João = {'rock':['scissors'], 'paper':['rock'], 'scissors':['paper']}
    def winner(y):
        player = {'rock':['scissors'], 'paper':['rock'], 'scissors':['paper']}
        outcome = 2
        if player == master_player:
            outcome = 0
        elif player in y[master_player]:
            outcome = 1
        return outcome

#function that prints the choice of the computer,
#the choice of the player and a message that announces who won the current round
    def roundin(z):
        result = {0:'Tie',1:'I won.',2:'You won.'}
        print('You chose ' + player)
        print('I chose ' + master_player)
        print(result[z])

#execute game using the functions and variables defined above
    rounds_done = 0
    while rounds_done < n_rounds and cpu_score < rounds_to_win and player_score < rounds_to_win:
        player = hand(gestures)
        master_player = computer(gestures)
        outcome = winner(João)
        roundin(outcome)
        rounds_done += 1
        if outcome == 1:
            cpu_score += 1
        elif outcome == 2:
            player_score += 1
            
#Show's the winner
    if player_score >= cpu_score:
        print("Lucky you! Congratulations!")
    elif cpu_score >= player_score:
        print("I win!")
    else:
        print("Tie. Try again.")
        
def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("You open your eyes. Your head is hurting, your ears are ringing and you’re feeling a bit dizzy. You stand up, look around and suddenly realise you are now in the middle of the jungle. The last thing you remember is having plugged in a very old videogame called Jumanji. You feel disoriented, yet you sense unknown danger is approaching, and you must get out of this jungle. NOW!")
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congratulations! You have used your wits and skills to take the final leap! The cliff was the acess point to the portal which took you back to your home! You are now safe!\nThank you for playing :) ")
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You are now able to go to the next location."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "You cannot go to the next location since you are unprepared to face the danger that awaits."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    if item["name"]== "plane wreck":
                        torch_riddle()
                    elif item["name"]== "rupest painting":
                        machete_riddle()
                    elif item["name"]== "pile of wood":
                        wood_riddle()
                    elif item["name"]== "tomb":
                        rps_riddle()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:  
                    if (item["name"] == "coconut tree"):
                        output += "This is indeed a very tall tree. But this isn't the tallest tree in the world. Appreciate its beauty and try doing something else."
                    else:
                        if (item["name"] == "rock of fallen soldiers"):
                            output += "This is the rock of fallen soldiers. A tribute to all of those who have fought for the freedom of Jumanji throughout the years. Pay your respects and try doing something else."
                        else:
                            output += "There isn't literally anything interesting about it. Try something else."
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in your current location.")
    
    if(next_room and input("Do you want to go to the next location? Enter 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)
        
game_state = INIT_GAME_STATE.copy()

start_game()