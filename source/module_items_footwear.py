from .header_items import *
from .header_item_modifiers import *

imodbits_cloth = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened

type_to_int = {
    'civilian': 0,
    'military': 1,
}


def footwear_properties(lvl, footwear_type):
    type_int = type_to_int[footwear_type]

    flags = itp_merchandise | itp_type_foot_armor | itp_attach_armature
    if footwear_type == 'civilian':
        flags |= itp_civilian

    return [flags, 0, 100 * (lvl + 1),
            weight(1 + type_int * 0.5 * lvl) |
            abundance(60) |
            leg_armor(1 + type_int * (4 + 10 * lvl)) |
            difficulty(type_int * 3**lvl),
            imodbits_cloth]


_footwear = {
    0: {'civilian': [], 'military': []},
    1: {'civilian': [], 'military': []},
    2: {'civilian': [], 'military': []},
}

_footwear[0]['civilian'] = [
    ['footwear_0c_1', "Bare Carbatinae", [("carbatinae_1_bare", 0)]] + footwear_properties(0, 'civilian'),
    ['footwear_0c_2', "Bare Carbatinae", [("carbatinae_2_bare", 0)]] + footwear_properties(0, 'civilian'),
]

for color in ['', '_green', '_blue', '_grey', '_orange', '_red']:
    # lvl 1 civilian
    for number in [1, 2]:
        mesh = 'carbatinae_%d%s' % (number, color)
        id = 'footwear_1c_%d' % len(_footwear[1]['civilian'])
        _footwear[1]['civilian'].append(
            [id, "Carbatinae", [(mesh, 0)]] + footwear_properties(1, 'civilian')
        )

    # lvl 2 civilian
    mesh = 'decorated_leather_shoes%s' % color
    id = 'footwear_2c_%d' % len(_footwear[2]['civilian'])
    _footwear[2]['civilian'].append(
        [id, "Leather Shoes", [(mesh, 0)]] + footwear_properties(2, 'civilian'),
    )


_footwear[0]['military'] = [
    ['footwear_0m_1', "Wrapping Boots", [("ankle_boots_a_new_bry", 0)]] + footwear_properties(0, 'military'),
    ['footwear_0m_2', "Wrapping Boots", [("wrapping_boots_a_bry", 0)]] + footwear_properties(0, 'military'),
]


# lvl 1 military
for color in ['', '_grey', '_green']:  # , '_blue', '_orange', '_red']:
    for number in [1, 2]:
        mesh = 'carbatinae_%d_greaves%s' % (number, color)
        id = 'footwear_1m_%d' % len(_footwear[1]['military'])
        _footwear[1]['military'].append(
            [id, "Army Carbatinae", [(mesh, 0)]] + footwear_properties(1, 'military')
        )


_footwear[2]['military'] = [
    ['footwear_2m_1', "Greaves", [('rus_splint_greaves', 0)]] + footwear_properties(2, 'military'),
    ['footwear_2m_2', "Greaves", [('splinted_greaves_a_bry', 0)]] + footwear_properties(2, 'military'),
    ['footwear_2m_3', "Greaves", [('spl_greaves', 0)]] + footwear_properties(2, 'military'),
]


# this dictionary contains the 'itm_*', that can be mentioned in troops and etc.
footwear = {
    0: {'civilian': [], 'military': []},
    1: {'civilian': [], 'military': []},
    2: {'civilian': [], 'military': []},
}

items = []
for type in ['civilian', 'military']:
    for lvl in [0, 1, 2]:
        items += _footwear[lvl][type]
        footwear[lvl][type] = ['itm_%s' % x[0] for x in _footwear[lvl][type]]
