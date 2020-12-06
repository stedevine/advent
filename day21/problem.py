# Must buy:
# at least one weapon
# zero or one item of armor
# zero, one or two rings

# Assemble combinations of the above, starting with the cheapest, 
# find the first one that beats the enemy

import itertools

def fight(player, enemy, player_hp, enemy_hp):
    # player goes first
    # decrease hp by player damage - enemy armor (at least 1)
    while (player_hp > 0):
        
        enemy_hp = enemy_hp - max(1, (player[0] - enemy[1]))
        # player wins
        if enemy_hp <= 0:
            return True
        player_hp = player_hp - max(1, (enemy[0] - player[1]))

    # enemy wins
    return False

# Test with player hp 8, enemy hp 12
# print(fight((5,5),(7,2)))

def get_ring_combinations():
    for damage_ring in ((0,0), (25,1), (50,2), (100,3)):
        for defence_ring in ((0,0), (20,1), (40,2), (80,3)):
            yield((damage_ring[0] + defence_ring[0], damage_ring[1], defence_ring[1]))


def get_rings():
    # ring (cost, damage, armor)
    rings_in_store = [(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]
    # take 0,1 or 2 of any ring
    for i in range(0,3):
        for rings in itertools.combinations(rings_in_store,i):
            combined_rings = (sum([ring[0] for ring in rings]), sum([ring[1] for ring in rings]), sum([ring[2] for ring in rings]))
            yield combined_rings
            

def get_loadouts():
    player_loadouts = []
    for weapon in ((8,4), (10,5), (25,6),(40,7), (74,8)):
        for armor in ((0,0), (13,1), (31,2), (53,3), (75,4), (102,5)):

            for ring in get_rings():
                
                total_damage = weapon[1] + ring[1]
                total_armor = armor[1] + ring[2]
                gold = weapon[0] + armor[0] + ring[0] 
                player = (total_damage, total_armor, gold)
                player_loadouts.append(player)
    
    player_loadouts.sort(key=lambda x: x[2])
    return player_loadouts

def spend_least_gold_to_beat_enemy(player_hp, enemy_hp, enemy_loadout):
    for loadout in get_loadouts():
        if fight((loadout[0],loadout[1]),enemy_loadout, player_hp, enemy_hp):
            print(loadout[2])
            break

def spend_most_gold_loose_to_enemy(player_hp, enemy_hp, enemy_loadout):
    load_outs = get_loadouts()
    load_outs.reverse()
    for loadout in load_outs:
        if not fight((loadout[0],loadout[1]),enemy_loadout, player_hp, enemy_hp):
            print(loadout[2])
            break

enemy_loadout = (9,2)
enemy_hitpoints = 103
spend_least_gold_to_beat_enemy(100, 103, enemy_loadout)
spend_most_gold_loose_to_enemy(100, 103, enemy_loadout)
