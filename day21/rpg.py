from collections import namedtuple
import itertools

Character = namedtuple('Character', 'hit_points damage armor')

def strike(attacker, attacked):
    damage_inflicted = max(1, attacker.damage - attacked.armor)
    return Character(attacked.hit_points - damage_inflicted, attacked.damage, attacked.armor)

def fight_simulation(player, boss):
    while True:
        boss = strike(player, boss)
        if (boss.hit_points < 1):
            return 'player'
        player = strike(boss, player)
        if (player.hit_points < 1):
            return 'boss'

# Get a list of the (gold spend [0] and player[1]) tuple combinations for the following rules:
# You must buy exacly one weapon
def get_weapon_players(gold, player):
    return [
    (gold + 8,  Character(player.hit_points, 4, player.armor)),
    (gold + 10, Character(player.hit_points, 5, player.armor)),
    (gold + 25, Character(player.hit_points, 6, player.armor)),
    (gold + 40, Character(player.hit_points, 7, player.armor)),
    (gold + 74, Character(player.hit_points, 8, player.armor))
    ]

# Armor is optional
def get_armor_players(gold, player):
    return [
    (gold,          Character(player.hit_points, player.damage, player.armor)), # No armor
    (gold + 13,     Character(player.hit_points, player.damage, 1)),
    (gold + 31,     Character(player.hit_points, player.damage, 2)),
    (gold + 53,     Character(player.hit_points, player.damage, 3)),
    (gold + 75,     Character(player.hit_points, player.damage, 4)),
    (gold + 102,    Character(player.hit_points, player.damage, 5))
    ]

# You can buy up to 2 rings, you cannot buy the same ring twice.
# Build a list of the combinations of indices of ring selections :
# (0,0) (no rings)
# (0,1) (one damage 1 ring),
# ...
# (5,6) (2 armor rings).
ring_combinations = [(0,0)]
c = itertools.combinations(iter(range(0,7)),2)
for pair in c:
    ring_combinations.append(pair)

print(ring_combinations)
print(len(ring_combinations))

def apply_ring(gold, player, ring_index):
    return [
        (gold,          Character(player.hit_points, player.damage, player.armor)),  # no ring
        (gold + 25,     Character(player.hit_points, player.damage + 1, player.armor)),
        (gold + 50,     Character(player.hit_points, player.damage + 2, player.armor)),
        (gold + 100,    Character(player.hit_points, player.damage + 3, player.armor)),
        (gold + 20,     Character(player.hit_points, player.damage, player.armor + 1)),
        (gold + 40,     Character(player.hit_points, player.damage, player.armor + 2)),
        (gold + 60,     Character(player.hit_points, player.damage, player.armor + 3)),
    ][ring_index]

def get_ringed_player(gold, player, ring_combination):
    first = apply_ring(gold, player, ring_combination[0])
    return apply_ring(first[0], first[1], ring_combination[1])

def get_player_gold_combinations():
    player_gold_combinations = []
    # Get a weapon for the player
    for w in get_weapon_players(0, Character(100,0,0)):
        # Get armor
        for a in get_armor_players(w[0], w[1]):
            # Get 0 to 2 rings
            for ring_combination in ring_combinations:
                ringed_player = get_ringed_player(a[0], a[1], ring_combination)
                # Player is ready to fight!
                player_gold_combinations.append(ringed_player)

    return player_gold_combinations

# From input
boss = Character(103,9,2)

# Get a list of the amout of gold spent and the result of the fight
results = []
for player_gold_combination in get_player_gold_combinations():
    results.append((fight_simulation(player_gold_combination[1], boss), player_gold_combination[0]))

print('results : {} ({})'.format(results, len(results)))
winning_gold = []
losing_gold = []
for r in results:
    if(r[0] == 'player'):
        winning_gold.append(r[1])
    else:
        losing_gold.append(r[1])

# Problem 1: What's the least amount of gold you can spend and win?
winning_gold.sort()
print(winning_gold[0])
# Problem 2: What's the most amount of gold you can spend and lose?
losing_gold.sort()
print(losing_gold[-1])
