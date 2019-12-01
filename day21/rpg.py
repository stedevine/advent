from collections import namedtuple

Character = namedtuple('Character', 'hit_points damage armor')

def strike(attacker, attacked):
    damage_inflicted = max(1, attacker.damage - attacked.armor)
    return Character(attacked.hit_points - damage_inflicted, attacked.damage, attacked.armor)

def fight_simulation(player, boss):
    winner = None
    while True:
        boss = strike(player, boss)
        print('boss {}'.format(boss.hit_points))
        if (boss.hit_points < 1):
            print('player wins')
            return 'player'
        player = strike(boss, player)
        print('player {}'.format(player.hit_points))
        if (player.hit_points < 1):
            print('boss wins')
            return 'boss'

player = Character(8, 5, 5)
boss = Character(120, 7, 2)

fight_simulation(player, boss)
