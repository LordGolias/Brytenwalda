from .header_items import *
from .header_item_modifiers import *

imodbits_horse_basic = imodbit_swaybacked | imodbit_lame | imodbit_spirited | imodbit_heavy | imodbit_stubborn
imodbits_horse_good = imodbit_spirited | imodbit_heavy

type_to_int = {
    'light': 0,
    'normal': 1,
    'heavy': 2,
}


def horse_properties(lvl, horse_type):
    type_int = type_to_int[horse_type]
    return [itp_merchandise | itp_type_horse, 0,
            2000 * (type_int + 1) * (lvl + 1),
            abundance(60) |
            hit_points(50 + 20 * lvl + 10 * type_int) |  # [50, 120]
            body_armor(5 + 7 * type_int) |  # [5, 21]
            difficulty(2 * lvl + type_int) |  # [0, 6]
            horse_speed(45 + 2 * lvl - 5 * type_int) |  # [45, 35]
            horse_maneuver(45 + 2 * lvl - 5 * type_int) |  # [45, 35]
            horse_charge(5 + 7 * type_int) |  # [5, 21]
            horse_scale(85 + 5 * lvl),
            imodbits_horse_basic]


# lvl 3
# HalfCata2



# Pictish1 Pictish2

# lvl 2


horses = {
    0: {'light': [], 'normal': [], 'heavy': []},
    1: {'light': [], 'normal': [], 'heavy': []},
    2: {'light': [], 'normal': [], 'heavy': []},
}

horses[0]['light'] = [
    ["horse_0l_1", "Traveler's Horse", [("normal_horse2", 0)]] + horse_properties(0, 'light'),
    ["horse_0l_2", "Traveler's Horse", [("normal_horse3", 0)]] + horse_properties(0, 'light'),
    ["horse_0l_3", "Traveler's Horse", [("normal_horse4", 0)]] + horse_properties(0, 'light'),
    ["horse_0l_4", "Traveler's Horse", [("normal_horse13", 0)]] + horse_properties(0, 'light'),
    ["horse_0l_5", "Traveler's Horse", [("normal_horse14", 0)]] + horse_properties(0, 'light'),
]
horses[0]['normal'] = [
    ["horse_0n_1", "Farm Horse", [("normal_horse15", 0)]] + horse_properties(0, 'normal'),
    ["horse_0n_2", "Farm Horse", [("normal_horse16", 0)]] + horse_properties(0, 'normal'),
    ["horse_0n_3", "Farm Horse", [("normal_horse17", 0)]] + horse_properties(0, 'normal'),
    ["horse_0n_4", "Farm Horse", [("normal_horse18", 0)]] + horse_properties(0, 'normal'),
    ["horse_0n_5", "Farm Horse", [("normal_horse19", 0)]] + horse_properties(0, 'normal'),
]
horses[0]['heavy'] = [
    ["horse_0h_1", "Heavy Farm Horse", [("gallic_horse_1", 0)]] + horse_properties(0, 'heavy'),
    ["horse_0h_2", "Heavy Farm Horse", [("gallic_horse_2", 0)]] + horse_properties(0, 'heavy'),
]

horses[1]['light'] = [
    ["horse_1l_1", "Light Horse", [("normal_horse5", 0)]] + horse_properties(1, 'light'),
    ["horse_1l_2", "Light Horse", [("normal_horse6", 0)]] + horse_properties(1, 'light'),
    ["horse_1l_3", "Light Horse", [("normal_horse7", 0)]] + horse_properties(1, 'light'),
    ["horse_1l_4", "Light Horse", [("normal_horse8", 0)]] + horse_properties(1, 'light'),
    ["horse_1l_5", "Light Horse", [("normal_horse9", 0)]] + horse_properties(1, 'light'),
]

horses[1]['normal'] = [
    # others available: 25-28, 30
    ["horse_1n_1", "Draft Horse", [("normal_horse20", 0)]] + horse_properties(1, 'light'),
    ["horse_1n_2", "Draft Horse", [("normal_horse21", 0)]] + horse_properties(1, 'light'),
    ["horse_1n_3", "Draft Horse", [("normal_horse22", 0)]] + horse_properties(1, 'light'),
    ["horse_1n_4", "Draft Horse", [("normal_horse23", 0)]] + horse_properties(1, 'light'),
    ["horse_1n_5", "Draft Horse", [("normal_horse24", 0)]] + horse_properties(1, 'light'),
]

horses[1]['heavy'] = [
    ["horse_1h_1", "North Horse", [("roman_horse_1", 0)]] + horse_properties(1, 'heavy'),
    ["horse_1h_2", "North Horse", [("roman_horse_2", 0)]] + horse_properties(1, 'heavy'),
]

horses[2]['light'] = [
    ["horse_2l_1", "Fast Horse", [("normal_horse11", 0)]] + horse_properties(2, 'light'),
    ["horse_2l_2", "Fast Horse", [("normal_horse12", 0)]] + horse_properties(2, 'light'),
    ["horse_2l_3", "Fast Horse", [("normal_horse29", 0)]] + horse_properties(2, 'light'),
    ["horse_2l_4", "Fast Horse", [("normal_horse31", 0)]] + horse_properties(2, 'light'),
]

horses[2]['normal'] = [
    ["horse_2n_1", "Army's Horse", [("WSumpterChestnut", 0)]] + horse_properties(2, 'normal'),
    ["horse_2n_2", "Army's Horse", [("WSumpterBrown", 0)]] + horse_properties(2, 'normal'),
    ["horse_2n_3", "Army's Horse", [("gallic_horse_3", 0)]] + horse_properties(2, 'normal'),

    ["horse_2n_4", "Pict Horse", [("Pictish1", 0)]] + horse_properties(2, 'normal') + [[], pict_factions],
    ["horse_2n_5", "Pict Horse", [("Pictish2", 0)]] + horse_properties(2, 'normal') + [[], pict_factions],
]

horses[2]['heavy'] = [
    ["horse_2h_1", "Lord's Horse", [("WRoman1", 0)]] + horse_properties(2, 'heavy'),
    ["horse_2h_2", "Lord's Horse", [("WRoman2", 0)]] + horse_properties(2, 'heavy'),
]

horses['donkeys'] = [
    ["horse_pony", "Pony", [("rus_horse", 0)], itp_merchandise | itp_type_horse, 0, 1800,
     abundance(60) | hit_points(60) | body_armor(10) | difficulty(1) | horse_speed(37) | horse_maneuver(
         36) | horse_charge(3) | horse_scale(86), 0],

    # donkey
    ["horse_donkey_1", "Donkey", [("donkey_mount", 0)], itp_merchandise | itp_type_horse, 0, 800,
     abundance(60) | hit_points(55) | body_armor(0) | difficulty(0) | horse_speed(35) | horse_maneuver(35) | horse_charge(3) | horse_scale(79), 0],
    ["horse_donkey_2", "Donkey", [("donkey_mount2", 0)], itp_merchandise | itp_type_horse, 0, 800,
     abundance(60) | hit_points(55) | body_armor(0) | difficulty(0) | horse_speed(35) | horse_maneuver(35) | horse_charge(3) | horse_scale(79), 0],
    ["horse_mule_1", "Mule", [("mule", 0)], itp_merchandise | itp_type_horse, 0, 1000,
     abundance(60) | hit_points(55) | body_armor(0) | difficulty(0) | horse_speed(35) | horse_maneuver(35) | horse_charge(3) | horse_scale(86), 0],
]

items = []
for lvl in [0, 1, 2]:
    for type in ['light', 'normal', 'heavy']:
        items += horses[lvl][type]

items += horses['donkeys']


for lvl in [0, 1, 2]:
    for type in ['light', 'normal', 'heavy']:
        horses[lvl][type] = ['itm_%s' % x[0] for x in horses[lvl][type]]
horses['donkeys'] = ['itm_%s' % x[0] for x in horses['donkeys']]
