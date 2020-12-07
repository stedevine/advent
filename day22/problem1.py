
def apply_effects(player, enemy, effects):
    print('Current effects {}'.format(effects))

    player_armor = 0
    for effect in effects.copy().keys():
        if effect == 'Poison':
            print('Poison deals 3 damage')
            enemy['hp'] -= 3
        if effect == 'Recharge':
            print('Mana increase by 101')
            player['mana'] += 101
        if effect == 'Shield':
            print('Shild boosts armor')
            player_armor = 7

        effects[effect] -= 1
        if effects[effect] == 0:
            print('{} expired, removing'.format(effect))
            del effects[effect]
    
    return player_armor

def player_move(player, enemy, effects, move):
    # Apply effects
    apply_effects(player, enemy, effects)

    # Apply player move
    if move == 'Magic Missile':
        enemy['hp'] -= 4
        player['mana'] -= 53
    
    if move == 'Drain':
        enemy['hp'] -= 2
        player['hp'] += 2
        player['mana'] -= 73
    
    if move == 'Shield':
        effects['Shield'] = 6
        player['mana'] -= 113

    if move == 'Poison':
        effects['Poison'] = 6
        player['mana'] -= 173

    if move == 'Recharge':
        effects['Recharge'] = 5
        player['mana'] -= 229

def enemy_move(player,enemy,effects):
    # Apply effects
    player_armor = apply_effects(player, enemy, effects)
    if (enemy['hp'] > 0):
        player['hp'] = player['hp']  - (max(1,enemy['damage'] - player_armor))
    

def game_loop(player, enemy, moves):
    effects = {}
    for move in moves:
        print('player turn')
        player_move(player, enemy, effects, move)
        print('player {} enemy {}'.format(player,enemy))
        if (enemy['hp'] <= 0 ):
            print('Player wins')
            break
        
        print('enemy turn')
        enemy_move(player, enemy, effects)
        print('player {} enemy {}'.format(player,enemy))
        if (player['hp'] <= 0):
            print('Enemy wins')
            break
        if (enemy['hp'] <= 0 ):
            print('Player wins')
            break  


def game():
    # first example
    player = {'hp': 10, 'mana': 250}
    enemy = {'hp': 13, 'damage': 8}
    moves = ['Poison', 'Magic Missile']
    game_loop(player, enemy, moves)

    player = {'hp': 10, 'mana': 250}
    enemy = {'hp': 14, 'damage': 8}
    moves = ['Recharge', 'Shield', 'Drain', 'Poison', 'Magic Missile']
    game_loop(player, enemy, moves)


game()

 
    