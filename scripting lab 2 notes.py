
To-do #2	print_cheer 
	print(f"Let's go {team['city']} {team['name']}!")

To-do #3 print list of players
print()
print(f"{team['city']} {team['name']} team roster:")

for player_name in team['players']:
	print(f'- {players_name.capitalize()}')
        
def add_players_to_team(team, new_players)
    team['players'].extend(new_players)
    
    # To-Do: capitalize first letter
    for i, player_name in enumerate(team['players']):
        team['players'][i] = player_name.capitalize()
    
    # To-Do: Sort the player list alphabetically
    team['players'].sort()
    return
    
def print_opponents(team)

    print(f"\nThe {team['city]}{team['name]} have played games against", end=' ')
    
    #To-Do: print comma-seperated list of opponent names
    for i, game in enumerate(team['games']):
        if i < len(team['games']) - 1:
            print(game['opponent'], end=', ')
        else:
            print(game['opponent'], end='.')
            
    #Alt
    opponent_names = [game['opponent'] for game in team['games']]
    print(', '.join(opponent_names), end='.')
    
    
def add_game(team, opp, gf, ga)
    #To-Do: append 
    new_game = {
        'opponent': opp,
        'goals for': gf,
        'goals against': ga
    }
    team['games'].append(new_game)

# Notes
[ ] can contain lists
list.append()

if confused on a script, utilize a breakpoint and work through it step by step

# Look into lightweight coreboot linux laptop

# soylent green