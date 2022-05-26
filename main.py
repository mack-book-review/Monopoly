import random
import time

board = ["Go","Mediterranean Avenue","Baltic Avenue","Reading Railroad","Oriental Avenue","Jail"]
property_info = {
    'Mediterranean Avenue': {
        'cost' : 100,
        'rent' : 50,
        'ownerID' : 0
    },

    'Baltic Avenue': {
        'cost' : 150,
        'rent' : 70,
        'ownerID' : 0
    },

    'Reading Railroad': {
        'cost': 175,
        'rent': 50,
        'ownerID': 0
    },

    'Oriental Avenue': {
        'cost': 200,
        'rent': 75,
        'ownerID': 0
    },
}

player = {
    'position': 0,
    'money': 600,
    'playerID': 1
}

computer = {
    'position' : 0,
    'money' : 600,
    'playerID' : 2
}

game_over =  False

def player_move(player):
    global game_over,board
    spaces = random.randint(1,6)
    player['position'] = (player['position']+spaces) % len(board)
    print("You rolled a {} and landed on {}".format(
        spaces,board[player['position']]
    ))
    if board[player['position']] in property_info:
        if property_info[board[player['position']]]['ownerID'] == 0:
            answer = input("You have ${}.  Would you like to buy {} for ${}? (y or n)".format(
                player['money'],board[player['position']],property_info[board[player['position']]]['cost']))
            if answer == 'y':
                property_info[board[player['position']]]['ownerID'] = player['playerID']
                player['money'] -= property_info[board[player['position']]]['cost']
                print("You bought {}.  You now have ${}".format(board[player['position']],player['money']))
            else:
                print("You passed up a great opportunity")

        elif property_info[board[player['position']]]['ownerID'] != player['playerID']:
            player['money'] -= property_info[board[player['position']]]['rent']
            computer['money'] += property_info[board[player['position']]]['rent']
            if player['money'] < 0:
                game_over = True
                print("You could not afford rent and went bankrupt.  The computer wins.")
                return
            print("Rent is ${}.  You now have ${}".format(
                property_info[board[player['position']]]['rent'],
                player['money']
            ))
    elif board[player['position']] == 'Go':
        player['money'] += 200
        print("You collected $200.  You now have a ${}".format(player['money']))
    elif board[player['position']] == "Jail":
        print("You are in jail, but you are just visiting though.")
    print()

def ai_move(computer):
    global game_over
    spaces = random.randint(1,6)
    computer['position'] = (computer['position']+spaces) % len(board)
    print("The computer rolled a {} and landed on {}".format(
        spaces,board[computer['position']]
    ))
    if board[computer['position']] in property_info:
        if property_info[board[computer['position']]]['ownerID'] == 0:
            if computer['money'] > property_info[board[computer['position']]]['cost']:
                property_info[board[computer['position']]]['ownerID'] = player['playerID']
                computer['money'] -= property_info[board[computer['position']]]['cost']
                property_info[board[computer['position']]]['ownderID'] = computer['playerID']
                print("The computer bought {} for ${} and now has ${}".format(
                    board[computer['position']],
                    property_info[board[computer['position']]]['cost'],
                    computer['money']
                ))

        elif property_info[board[computer['position']]]['ownerID'] != computer['playerID']:
            computer['money'] -= property_info[board[computer['position']]]['rent']
            player['money'] += property_info[board[computer['position']]]['rent']
            if computer['money'] < 0:
                game_over = True
                print("The computer could not afford rent and went bankrupt.  You win.")
                return
            print("Rent is ${}.  The computer now has ${}".format(
                property_info[board[computer['position']]]['rent'],
                computer['money']
            ))
    elif board[computer['position']] == 'Go':
        computer['money'] += 200
        print("The computer collected $200.  The computer now has a ${}".format(computer['money']))
    elif board[computer['position']] == "Jail":
        print("The computer is in jail, but it is just visiting.")
    print()


def main():
    print("Welcome to Monopoly \n")
    while not game_over:
        input("press enter to continue")
        print()
        player_move(player)
        if game_over:
            break
        time.sleep(5)
        ai_move(computer)
        time.sleep(0.5)

if __name__ == '__main__':
    main()

