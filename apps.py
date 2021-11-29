#  GOING FOR EXCEEDS, REJECT IF NOT

import constants
import copy
import sys

players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)

panthers = []
bandits = []
warriors = []
experienced = []
inexperienced = []
teams = [panthers, bandits, warriors]
num_teams = len(teams)

title_1 = "Basketball Team Stats Tool"
title_2 = "Teams"
result_1 = "Team: Panthers Stats"
result_2 = "Team: Bandits Stats"
result_3 = "Team: Warriors Stats"
exit_msg = "  Goodbye"


def clean_data():
    for player in players_copy:
        player["height"] = int(player["height"][:2])
        player["guardians"] = (", ".join(player["guardians"].split(" and ")))
        if player["experience"] == "YES":
            player["experience"] = True
            experienced.append(player)
        else:
            player["experience"] = False
            inexperienced.append(player)


def balance_teams():
    for num in range(len(experienced)):
        teams[num % num_teams].append(experienced[num])
    for num in range(len(inexperienced)):
        teams[num % num_teams].append(inexperienced[num])


def stats(team):
    num_players = len(team)
    name_player = []
    name_guardian = []
    num_experienced = 0
    num_inexperienced = 0
    team_height = 0
    for player in team:
        name_player.append(player["name"])
        name_guardian.append(player["guardians"])
        team_height += player["height"]
        if player["experience"] == True:
            num_experienced += 1
        else:
            num_inexperienced += 1
    avg_height = round(team_height / len(team))
    print(f"Total Players: {num_players}")
    print(f"Experienced Players: {num_experienced}")
    print(f"Inexperienced Players: {num_inexperienced}")
    print(f"Average Height: {avg_height} inches")
    print("\nPlayers on Team:\n", ', '.join(name_player))
    print("\nGuardians:\n", ', '.join(name_guardian))


def cont():
    enter = input("\nPress ENTER to continue... \n")
    if enter == " ":
        menu()
    else:
        menu()


def menu():
    print("-" * len(title_1))
    print(title_1)
    print("-" * len(title_1))
    print("\n", "-" * 4, "MENU", "-" * 4)
    while True:
        print("\nHere are your choices:\n1) Display Team Stats\n2) Quit\n")
        try:
            choice_1 = int(input("Enter your choice > "))
            if choice_1 == 1:
                print()
                print("-" *len(title_2))
                print(title_2)
                print("-" *len(title_2))
                while True:
                    print("\nChoose a team:\n1) Panthers\n2) Bandits\n3) Warriors\n")
                    try:
                        choice_2 = int(input("Enter your choice > "))
                        if choice_2 == 1:
                            print()
                            print(result_1)
                            print("-" * len(result_1))
                            stats(panthers)
                            cont()
                        elif choice_2 == 2:
                            print()
                            print(result_2)
                            print("-" * len(result_2))
                            stats(bandits)
                            cont() 
                        elif choice_2 == 3:
                            print()
                            print(result_3)
                            print("-" * len(result_3))
                            stats(warriors)
                            cont() 
                        else:
                            print("\nPlease choose a valid option")
                    except ValueError:
                        print("\nPlease choose a valid option")
            elif choice_1 == 2:
                print("\n", "-" * len(exit_msg))
                sys.exit(print(exit_msg, "\n" , "-" * len(exit_msg)))
            else:
                print("\nPlease choose a valid option")
        except ValueError:
                print("\nPlease choose a valid option")


if __name__ == "__main__":
    clean_data()
    balance_teams()
    menu()
