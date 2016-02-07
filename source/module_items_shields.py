from header_operations import store_trigger_param, call_script

from header_items import itp_type_shield, itp_wooden_parry, itp_merchandise, \
    itcf_carry_round_shield, itcf_carry_kite_shield, \
    weight, hit_points, body_armor, spd_rtng, shield_width, difficulty, abundance, \
    pict_factions, irish_factions, saxon_factions, jute_factions, engle_factions, briton_factions
from header_item_modifiers import imodbit_cracked, imodbit_battered, imodbit_thick, imodbit_reinforced
from header_triggers import ti_on_init_item

imodbits_shield = imodbit_cracked | imodbit_battered | imodbit_thick | imodbit_reinforced
imodbits_shield_high = imodbit_cracked | imodbit_battered | imodbit_thick | imodbit_reinforced

NORMAL_SHIELD_WIDTH = 40
HEAVY_SHIELD_WIDTH = 60


# each level contains light, normal and heavy
#   level: represents difficulty and strength of the shield.
#   type: represents heaviness within the level
_shield_attributes = {
    0: {
        'light': {'hp': 100, 'weight': 1, 'speed': 100},
        'normal': {'hp': 150, 'weight': 2, 'speed': 80},
        'heavy': {'hp': 200, 'weight': 3, 'speed': 60},
    },
    1: {
        'light': {'hp': 200, 'weight': 1, 'speed': 100},
        'normal': {'hp': 250, 'weight': 2, 'speed': 80},
        'heavy': {'hp': 300, 'weight': 3, 'speed': 60},
    },
    2: {
        'light': {'hp': 200, 'weight': 1, 'speed': 100},
        'normal': {'hp': 250, 'weight': 2, 'speed': 80},
        'heavy': {'hp': 300, 'weight': 3, 'speed': 60},
    },
    3: {
        'light': {'hp': 300, 'weight': 1, 'speed': 100},
        'normal': {'hp': 350, 'weight': 2, 'speed': 80},
        'heavy': {'hp': 400, 'weight': 3, 'speed': 60},
    },
}

shield_type_to_int = {'light': 0, 'normal': 1, 'heavy': 2}


def shield_armor(lvl, shield_type):
    return 3 * lvl + shield_type_to_int[shield_type]


def shield_attributes(lvl, width, weight=0, hp=0, armor=0, speed=0):
    if width <= NORMAL_SHIELD_WIDTH:
        shield_type = 'light'
    elif width <= HEAVY_SHIELD_WIDTH:
        shield_type = 'normal'
    else:
        shield_type = 'heavy'

    if lvl not in _shield_attributes:
        raise NotImplementedError("Shield level '%d' not implemented.")

    attributes = _shield_attributes[lvl][shield_type].copy()

    attributes['weight'] += weight
    attributes['hp'] += hp
    attributes['armor'] = shield_armor(lvl, shield_type) + armor
    attributes['speed'] += speed
    attributes['lvl'] = lvl
    attributes['type'] = shield_type
    return attributes


def shield_difficulty(lvl, shield_type):
    # light +0; normal +1; heavy +2
    return 3 * lvl + shield_type_to_int[shield_type]


def shield_cost(attrs):
    extra = shield_type_to_int[attrs['type']]
    return 2**attrs['lvl'] * (100 + 100 * extra)


def shield_properties(lvl, width, is_merchandize=False, is_kite=False, **kwargs):
    properties = itp_type_shield | itp_wooden_parry
    if is_merchandize:
        # todo: make abundance dependent on something (lvl?)
        properties |= itp_merchandise | abundance(60)

    attrs = shield_attributes(lvl, width, **kwargs)
    cost = shield_cost(attrs)

    _difficulty = shield_difficulty(lvl, attrs['type'])

    itcf = itcf_carry_round_shield
    if is_kite:
        itcf = itcf_carry_kite_shield

    return [properties, itcf, cost,
            weight(attrs['weight']) |
            hit_points(attrs['hp']) |
            body_armor(attrs['armor']) |
            spd_rtng(attrs['speed']) |
            shield_width(width) |
            difficulty(_difficulty),
            imodbits_shield]


def set_banner(tableau):
    return [(ti_on_init_item,
             [(store_trigger_param, ":agent_no", 1),
              (store_trigger_param, ":troop_no", 2),
              (call_script, "script_shield_item_set_banner", tableau, ":agent_no", ":troop_no")]
            )]


shields = {
    'pict': {0: {'light': [], 'normal': [], 'heavy': []},
             1: {'light': [], 'normal': [], 'heavy': []},
             2: {'light': [], 'normal': [], 'heavy': []},
             3: {'light': [], 'normal': [], 'heavy': []},
             },
    'saxon': {0: {'light': [], 'normal': [], 'heavy': []},
              1: {'light': [], 'normal': [], 'heavy': []},
              2: {'light': [], 'normal': [], 'heavy': []},
              3: {'light': [], 'normal': [], 'heavy': []},
             },
    'briton': {0: {'light': [], 'normal': [], 'heavy': []},
               1: {'light': [], 'normal': [], 'heavy': []},
               2: {'light': [], 'normal': [], 'heavy': []},
               3: {'light': [], 'normal': [], 'heavy': []},
              },
    # shields common to all factions
    'common': {0: {'light': [], 'normal': [], 'heavy': []},
               1: {'light': [], 'normal': [], 'heavy': []},
               2: {'light': [], 'normal': [], 'heavy': []},
               3: {'light': [], 'normal': [], 'heavy': []},
              },
    # a type of shield? todo: check if it is worth
    'cantabrian': {0: {'light': [], 'normal': [], 'heavy': []},
                   1: {'light': [], 'normal': [], 'heavy': []},
                   2: {'light': [], 'normal': [], 'heavy': []},
                   3: {'light': [], 'normal': [], 'heavy': []},
                  },
    # shields that allow banners
    'banner': {0: {'light': [], 'normal': [], 'heavy': []},
               1: {'light': [], 'normal': [], 'heavy': []},
               2: {'light': [], 'normal': [], 'heavy': []},
               3: {'light': [], 'normal': [], 'heavy': []},
              },
}

# these are shallow copies because they are always equal so far
shields['irish'] = shields['pict']
shields['jute'] = shields['saxon']
shields['engle'] = shields['saxon']


# lvl 0 light shields
_name = "Small Gaelic Shield"
lvl0_light_shields = [
    ["shield_gaelic_small_1", _name, [("buckler1", 0)]] + shield_properties(0, 30, True),
    ["shield_gaelic_small_6", _name, [("buckler6", 0)]] + shield_properties(0, 30, True),
    ["shield_gaelic_small_7", _name, [("buckler7", 0)]] + shield_properties(0, 30, True),
    ["shield_gaelic_small_8", _name, [("buckler8", 0)]] + shield_properties(0, 30),
    ["shield_gaelic_small_9", _name, [("buckler9", 0)]] + shield_properties(0, 30),
    ["shield_gaelic_small_10", _name, [("buckler16", 0)]] + shield_properties(0, 30),
    ["shield_gaelic_small_11", _name, [("buckler32", 0)]] + shield_properties(0, 30),
    ["shield_gaelic_small_12", _name, [("buckler28", 0)]] + shield_properties(0, 30),
    ["shield_gaelic_small_13", _name, [("buckler42", 0)]] + shield_properties(0, 30),
    ["shield_gaelic_small_17", _name, [("buckler17", 0)]] + shield_properties(0, 30),
    ["shield_gaelic_small_18", _name, [("buckler18", 0)]] + shield_properties(0, 30),
    ["shield_gaelic_small_19", _name, [("buckler19", 0)]] + shield_properties(0, 30),
]
items = lvl0_light_shields
shields['common'][0]['light'] += ['itm_' + x[0] for x in lvl0_light_shields]

# lvl 0/1 normal/heavy
items += [
    ["shield_plain_heavy_1", "Heavy Plain Shield", [("woodenshield_medium", 0)]] + shield_properties(0, 70, True),

    ["shield_plain_heavy_2", "Heavy Plain Shield", [("leathershield_medium_d", 0)]] + shield_properties(1, 70, True),
    # ["shield_plain_heavy_3", "Heavy Plain Shield", [("leathershield_medium", 0)]] + shield_properties(1, 70, True),
    # ["shield_plain_heavy_4", "Heavy Plain Shield", [("leathershield_medium_y", 0)]] + shield_properties(1, 70, True),
    # ["shield_plain_heavy_5", "Heavy Plain Shield", [("leathershield_medium_b", 0)]] + shield_properties(1, 70, True),

    ["shield_plain_1", "Plain Shield", [("woodenshield_small", 0)]] + shield_properties(0, 60, True),
    ["shield_plain_2", "Plain Shield", [("woodenshield_small_d", 0)]] + shield_properties(0, 60, True),

    ["shield_plain_3", "Plain Shield", [("leathershield_small_b", 0)]] + shield_properties(1, 60, True),
    # ["shield_plain_4", "Plain Shield", [("leathershield_small_d", 0)]] + shield_properties(1, 60, True),
]
shields['common'][0]['normal'] += ['itm_shield_plain_1', 'itm_shield_plain_2']
shields['common'][0]['heavy'] += ['itm_shield_plain_heavy_1']
shields['common'][1]['normal'] += ['itm_shield_plain_3']
shields['common'][1]['heavy'] += ['itm_shield_plain_heavy_2']

# Shields with banners
items += [
    ["shield_banner_1", "Weak Shield", [("tableau_shield_small_round_3", 0)]] + shield_properties(0, 60, True) + [set_banner("tableau_small_round_shield_3")],
    ["shield_banner_2", "Simple Shield", [("tableau_shield_small_round_1", 0)]] + shield_properties(1, 60, True) + [set_banner("tableau_small_round_shield_1")],
    ["shield_banner_3", "Shield", [("tableau_shield_small_round_2", 0)]] + shield_properties(2, 60, True) + [set_banner("tableau_small_round_shield_2")],

    ["shield_banner_heavy_0", "Weak H. Shield", [("tableau_shield_round_3", 0)]] + shield_properties(0, 70, True) + [set_banner("tableau_round_shield_3")],
    ["shield_banner_heavy_1", "Simple H. Shield", [("tableau_shield_round_2", 0)]] + shield_properties(1, 70, True) + [set_banner("tableau_round_shield_2")],
    ["shield_banner_heavy_2", "H. Shield", [("tableau_shield_round_1", 0)]] + shield_properties(2, 70, True) + [set_banner("tableau_round_shield_1")],
    ["shield_banner_heavy_3", "Elite H. Shield", [("tableau_shield_round_4", 0)]] + shield_properties(3, 70, True) + [set_banner("tableau_round_shield_4")],

    ["shield_banner_kite_0", "Weak Kite", [("tableau_shield_kite_1", 0)]] + shield_properties(0, 50, True, is_kite=True) + [set_banner("tableau_kite_shield_1")],
    ["shield_banner_kite_1", "Kite", [("tableau_shield_kite_3", 0)]] + shield_properties(1, 50, True, is_kite=True) + [set_banner("tableau_kite_shield_3")],
]
shields['banner'][1]['normal'] += ['itm_shield_banner_1']
shields['banner'][2]['normal'] += ['itm_shield_banner_2']
shields['banner'][3]['normal'] += ['itm_shield_banner_3']

shields['banner'][0]['heavy'] += ['itm_shield_banner_heavy_0']
shields['banner'][1]['heavy'] += ['itm_shield_banner_heavy_1']
shields['banner'][2]['heavy'] += ['itm_shield_banner_heavy_2']
shields['banner'][3]['heavy'] += ['itm_shield_banner_heavy_3']

shields['banner'][0]['light'] += ['itm_shield_banner_kite_0']
shields['banner'][1]['light'] += ['itm_shield_banner_kite_1']


######################### Picts #########################

# lvl 0 light shields
_name = "Small Gaelic Shield"
lvl0_pict_light_shields = [
    ["shield_gaelic_small_2", _name, [("buckler2", 0)]] + shield_properties(0, 30, True) + [[], pict_factions + irish_factions],
    ["shield_gaelic_small_3", _name, [("buckler3", 0)]] + shield_properties(0, 30, True) + [[], pict_factions + irish_factions],
    ["shield_gaelic_small_4", _name, [("buckler4", 0)]] + shield_properties(0, 30, True) + [[], pict_factions + irish_factions],
    ["shield_gaelic_small_5", _name, [("buckler5", 0)]] + shield_properties(0, 30, True) + [[], pict_factions + irish_factions],
]
items += lvl0_pict_light_shields
shields['pict'][0]['light'] += ['itm_' + x[0] for x in lvl0_pict_light_shields]

# lvl 0 normal shields
_name = "Gaelic Shield"
lvl0_pict_normal_shields = [
    ["shield_gaelic_a", _name, [("shield_gaelic_a", 0)]] + shield_properties(0, 60, True) + [[], pict_factions + irish_factions],
    ["shield_gaelic_b", _name, [("shield_gaelic_b", 0)]] + shield_properties(0, 60, True) + [[], pict_factions + irish_factions],
    ["shield_gaelic_c", _name, [("shield_gaelic_c", 0)]] + shield_properties(0, 60, True) + [[], pict_factions + irish_factions],
    ["shield_gaelic_d", _name, [("shield_gaelic_d", 0)]] + shield_properties(0, 60) + [[], pict_factions + irish_factions],
    ["shield_gaelic_e", _name, [("shield_gaelic_e", 0)]] + shield_properties(0, 60) + [[], pict_factions + irish_factions],
    ["shield_gaelic_f", _name, [("shield_gaelic_f", 0)]] + shield_properties(0, 60) + [[], pict_factions + irish_factions],
    ["shield_gaelic_g", _name, [("shield_gaelic_g", 0)]] + shield_properties(0, 60) + [[], pict_factions + irish_factions],
    ["shield_gaelic_h", _name, [("shield_gaelic_h", 0)]] + shield_properties(0, 60) + [[], pict_factions + irish_factions],
    ["shield_gaelic_i", _name, [("shield_gaelic_i", 0)]] + shield_properties(0, 60) + [[], pict_factions + irish_factions],
    ["shield_gaelic_j", _name, [("shield_gaelic_j", 0)]] + shield_properties(0, 60) + [[], pict_factions + irish_factions],
]
items += lvl0_pict_normal_shields
shields['pict'][0]['normal'] = ['itm_' + x[0] for x in lvl0_pict_normal_shields]

# lvl 1 light shields
_name = "Pictish Shield"
lvl1_pict_light_shields = [
    # meshes vae_h_shield{i} with i=1,2,7,10 do not exist
    # ["shield_pict_a_1", _name, [("vae_h_shield1", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    # ["shield_pict_a_2", _name, [("vae_h_shield2", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_a_3", _name, [("vae_h_shield3", 0)]] + shield_properties(1, 50, True) + [[], pict_factions + irish_factions],
    ["shield_pict_a_4", _name, [("vae_h_shield4", 0)]] + shield_properties(1, 50, True) + [[], pict_factions + irish_factions],
    ["shield_pict_a_5", _name, [("vae_h_shield5", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_a_6", _name, [("vae_h_shield6", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    # ["shield_pict_a_7", _name, [("vae_h_shield7", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_a_8", _name, [("vae_h_shield8", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_a_9", _name, [("vae_h_shield9", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    # ["shield_pict_a_10", _name, [("vae_h_shield10", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_a_11", _name, [("vae_h_shield11", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_a_12", _name, [("vae_h_shield12", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],

    # below are similar shields, just rotated and rounded
    ["shield_pict_b_1", _name, [("tarcza_harfa_vae_1", 0)]] + shield_properties(1, 50, True) + [[], pict_factions + irish_factions],
    ["shield_pict_b_2", _name, [("tarcza_harfa_vae_2", 0)]] + shield_properties(1, 50, True) + [[], pict_factions + irish_factions],
    ["shield_pict_b_3", _name, [("tarcza_harfa_vae_3", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_b_4", _name, [("tarcza_harfa_vae_4", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_b_5", _name, [("tarcza_harfa_vae_5", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_b_6", _name, [("tarcza_harfa_vae_6", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_b_7", _name, [("tarcza_harfa_vae_7", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    # ["shield_pict_b_8", _name, [("tarcza_harfa_vae_8", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    # ["shield_pict_b_9", _name, [("tarcza_harfa_vae_9", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_b_10", _name, [("tarcza_harfa_vae_10", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_b_11", _name, [("tarcza_harfa_vae_11", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_b_12", _name, [("tarcza_harfa_vae_12", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_b_13", _name, [("tarcza_harfa_vae_13", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_b_14", _name, [("tarcza_harfa_vae_14", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    # ["shield_pict_b_15", _name, [("tarcza_harfa_vae_15", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_b_16", _name, [("tarcza_harfa_vae_16", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    # ["shield_pict_b_17", _name, [("tarcza_harfa_vae_17", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    # ["shield_pict_b_18", _name, [("tarcza_harfa_vae_18", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_b_19", _name, [("tarcza_harfa_vae_19", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    # ["shield_pict_b_20", _name, [("tarcza_harfa_vae_20", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
    ["shield_pict_b_21", _name, [("tarcza_harfa_vae_21", 0)]] + shield_properties(1, 50) + [[], pict_factions + irish_factions],
]
items += lvl1_pict_light_shields
shields['pict'][1]['light'] = ['itm_' + x[0] for x in lvl1_pict_light_shields]

# lvl 1 normal shields
_name = "Celtic Shield"
lvl1_pict_normal_shields = [
    # ["celtic_shield_smalla", _name, [("celtic_shield_small_round_a", 0)]] + shield_properties(1, 60, True) + [[], pict_factions + irish_factions],
    # ["celtic_shield_smallb", _name, [("celtic_shield_small_round_b", 0)]] + shield_properties(1, 60, True) + [[], pict_factions + irish_factions],
    # ["celtic_shield_smallc", _name, [("celtic_shield_small_round_c", 0)]] + shield_properties(1, 60, True) + [[], pict_factions + irish_factions],
    # ["celtic_shield_smalld", _name, [("celtic_shield_small_round_d", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],
    # ["celtic_shield_smalle", _name, [("celtic_shield_small_round_e", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],
    # ["celtic_shield_smallf", _name, [("celtic_shield_small_round_f", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],
    # ["christian_lenticularshield0", _name, [("shield_small_round", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],

    ["shield_celtic_1", _name, [("celtic_vae_shield1", 0)]] + shield_properties(1, 60, True) + [[], pict_factions + irish_factions],
    ["shield_celtic_2", _name, [("celtic_vae_shield2", 0)]] + shield_properties(1, 60, True) + [[], pict_factions + irish_factions],
    # ["dceltic_vae_shield3", _name, [("celtic_vae_shield3", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],
    # ["dceltic_vae_shield4", _name, [("celtic_vae_shield4", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],
    # ["dceltic_vae_shield5", _name, [("celtic_vae_shield5", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],
    ["shield_celtic_6", _name, [("celtic_vae_shield6", 0)]] + shield_properties(1, 60, True) + [[], pict_factions + irish_factions],
    ["shield_celtic_7", _name, [("celtic_vae_shield7", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],
    ["shield_celtic_8", _name, [("celtic_vae_shield8", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],
    ["shield_celtic_9", _name, [("celtic_vae_shield9", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],
    ["shield_celtic_10", _name, [("celtic_vae_shield10", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],
]
items += lvl1_pict_normal_shields
shields['pict'][1]['normal'] = ['itm_' + x[0] for x in lvl1_pict_normal_shields]

# lvl 2 light shields
_name = "Pict Square Shield"
lvl2_pict_light_shields = [
    ["shield_square_1", _name, [("vae_cuadrado_1", 0)]] + shield_properties(2, 40, True) + [[], pict_factions + irish_factions],
    ["shield_square_2", _name, [("vae_cuadrado_2", 0)]] + shield_properties(2, 40, True) + [[], pict_factions + irish_factions],
    ["shield_square_3", _name, [("vae_cuadrado_3", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_4", _name, [("vae_cuadrado_4", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_5", _name, [("vae_cuadrado_5", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_6", _name, [("vae_cuadrado_6", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_7", _name, [("vae_cuadrado_7", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_8", _name, [("vae_cuadrado_8", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_9", _name, [("vae_cuadrado_9", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_10", _name, [("vae_cuadrado_10", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_11", _name, [("vae_cuadrado_11", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_12", _name, [("vae_cuadrado_12", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_13", _name, [("vae_cuadrado_13", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_14", _name, [("vae_cuadrado_14", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_15", _name, [("vae_cuadrado_15", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_16", _name, [("vae_cuadrado_16", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_17", _name, [("vae_cuadrado_17", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_18", _name, [("vae_cuadrado_18", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_19", _name, [("vae_cuadrado_19", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_20", _name, [("vae_cuadrado_20", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_21", _name, [("vae_cuadrado_21", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_22", _name, [("vae_cuadrado_22", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_23", _name, [("vae_cuadrado_22", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_24", _name, [("vae_cuadrado_22", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_25", _name, [("vae_cuadrado_25", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_26", _name, [("vae_cuadrado_26", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_27", _name, [("vae_cuadrado_27", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
    ["shield_square_28", _name, [("vae_cuadrado_28", 0)]] + shield_properties(2, 40) + [[], pict_factions + irish_factions],
]
items += lvl2_pict_light_shields
shields['pict'][2]['light'] = ['itm_' + x[0] for x in lvl2_pict_light_shields]

# lvl 2 normal shields
_name = "Pict Shield"
lvl2_pict_normal_shields = [
    # ["shield_caledonian_dog", _name, [("caledonian_shield_dog", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],
    # ["shield_caledonian_raven", _name, [("caledonian_shield_raven", 0)]] + shield_properties(1, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_1", _name, [("vae_caledonian_shield1", 0)]] + shield_properties(2, 60, True) + [[], pict_factions + irish_factions],
    ["shield_caledonian_2", _name, [("vae_caledonian_shield2", 0)]] + shield_properties(2, 60, True) + [[], pict_factions + irish_factions],
    ["shield_caledonian_3", _name, [("vae_caledonian_shield3", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_4", _name, [("vae_caledonian_shield4", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_5", _name, [("vae_caledonian_shield5", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_6", _name, [("vae_caledonian_shield6", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_7", _name, [("vae_caledonian_shield7", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_8", _name, [("vae_caledonian_shield8", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_9", _name, [("vae_caledonian_shield9", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_10", _name, [("vae_caledonian_shield10", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_11", _name, [("vae_caledonian_shield11", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_12", _name, [("vae_caledonian_shield12", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_13", _name, [("vae_caledonian_shield13", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_14", _name, [("vae_caledonian_shield14", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_caledonian_15", _name, [("vae_caledonian_shield15", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],

    ["shield_pict_c_1", _name, [("vae_scyld1", 0)]] + shield_properties(2, 60, True) + [[], pict_factions + irish_factions],
    ["shield_pict_c_2", _name, [("vae_scyld2", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_pict_c_3", _name, [("vae_scyld3", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_pict_c_4", _name, [("vae_scyld4", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_pict_c_5", _name, [("vae_scyld5", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_pict_c_6", _name, [("vae_scyld6", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_pict_c_7", _name, [("vae_scyld7", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],

    ["shield_godelic_1", _name, [("godelic_shield1", 0)]] + shield_properties(2, 60, True) + [[], pict_factions + irish_factions],
    ["shield_godelic_2", _name, [("godelic_shield2", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
    ["shield_godelic_3", _name, [("godelic_shield3", 0)]] + shield_properties(2, 60) + [[], pict_factions + irish_factions],
]
items += lvl2_pict_normal_shields
shields['pict'][2]['normal'] = ['itm_' + x[0] for x in lvl2_pict_normal_shields]

# lvl 3 light shields
_name = "Pict Rectangular Shield"
lvl3_pict_light_shields = [
    ["shield_rectangle_1", _name, [("vae_escudo_picto", 0)]] + shield_properties(2, 50, True) + [[], pict_factions + irish_factions],
    ["shield_rectangle_2", _name, [("vae_escudo_picto2", 0)]] + shield_properties(2, 50, True) + [[], pict_factions + irish_factions],
    # ["shield_rectangle_3", _name, [("vae_escudo_picto3", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    ["shield_rectangle_4", _name, [("vae_escudo_picto4", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    ["shield_rectangle_5", _name, [("vae_escudo_picto5", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    # ["shield_rectangle_6", _name, [("vae_escudo_picto6", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    ["shield_rectangle_7", _name, [("vae_escudo_picto7", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    ["shield_rectangle_8", _name, [("vae_escudo_picto8", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    ["shield_rectangle_9", _name, [("vae_escudo_picto9", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    # ["shield_rectangle_10", _name, [("vae_escudo_picto10", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    # ["shield_rectangle_11", _name, [("vae_escudo_picto11", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    # ["shield_rectangle_12", _name, [("vae_escudo_picto12", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    ["shield_rectangle_13", _name, [("vae_escudo_picto13", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    ["shield_rectangle_14", _name, [("vae_escudo_picto14", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    ["shield_rectangle_15", _name, [("vae_escudo_picto15", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    ["shield_rectangle_27", _name, [("vae_escudo_picto27", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    ["shield_rectangle_28", _name, [("vae_escudo_picto28", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
    # ["shield_rectangle_t2", _name, [("Shield_IP", 0)]] + shield_properties(2, 50) + [[], pict_factions + irish_factions],
]
items += lvl3_pict_light_shields
shields['pict'][3]['light'] = ['itm_' + x[0] for x in lvl3_pict_light_shields]

######################### saxon_factions + jute_factions + engle_factions #########################

# lvl 0 light shield
_name = "Small Saxon Shield"
lvl0_saxon_light_shields = [
    ["shield_gaelic_small_23", _name, [("buckler23", 0)]] + shield_properties(0, 30, True) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_gaelic_small_24", _name, [("buckler26", 0)]] + shield_properties(0, 30, True) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_gaelic_small_25", _name, [("buckler27", 0)]] + shield_properties(0, 30, True) + [[], saxon_factions + jute_factions + engle_factions],
]
items += lvl0_saxon_light_shields
shields['saxon'][0]['light'] = ['itm_' + x[0] for x in lvl0_saxon_light_shields]

# lvl 0 normal shield
_name = "Weak Saxon Shield"
lvl0_saxon_normal_shields = [
    ["shield_round_1", _name, [("BL_Roundshields_03", 0)]] + shield_properties(0, 60, True) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_2", _name, [("BL_Roundshields_04", 0)]] + shield_properties(0, 60, True) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_3", _name, [("BL_Roundshields_20", 0)]] + shield_properties(0, 60, True) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_4", _name, [("BL_Roundshields_02", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_5", _name, [("BL_Roundshields_05", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_6", _name, [("BL_Roundshields_18", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_7", _name, [("BL_Roundshields_15", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_8", _name, [("BL_Roundshields_10", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_9", _name, [("BL_Roundshields_09", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_10", _name, [("BL_Roundshields_14", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_11", _name, [("BL_Roundshields_19", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_12", _name, [("BL_Roundshields_13", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_13", _name, [("BL_Roundshields_06", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_round_14", _name, [("BL_Roundshields_01", 0)] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
]
items += lvl0_saxon_normal_shields
shields['saxon'][0]['normal'] = ['itm_' + x[0] for x in lvl0_saxon_normal_shields]


# lvl 1 normal shield
_name = "Basic Saxon Shield"
lvl1_saxon_normal_shields = [
    ["shield_round_15", _name, [("BL_Roundshields_22", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_16", _name, [("BL_Roundshields_21", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_17", _name, [("BL_Roundshields_17", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_18", _name, [("BL_Roundshields_07", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_19", _name, [("BL_Roundshields_08", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_round_20", _name, [("BL_Roundshields_16", 0)]] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_round_21", _name, [("BL_Roundshields_11", 0)] + shield_properties(0, 60) + [[], saxon_factions + jute_factions + engle_factions],
]
items += lvl1_saxon_normal_shields
shields['saxon'][1]['normal'] = ['itm_' + x[0] for x in lvl1_saxon_normal_shields]


# lvl 1 heavy shield
_name = "Standard Saxon Shield"
lvl1_saxon_heavy_shields = [
    ["shield_viking_1", _name, [("ad_viking_shield_round_01", 0)]] + shield_properties(1, 70, True) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_2", _name, [("ad_viking_shield_round_02", 0)]] + shield_properties(1, 70, True) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_3", _name, [("ad_viking_shield_round_03", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_4", _name, [("ad_viking_shield_round_04", 0)]] + shield_properties(1, 70, True) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_5", _name, [("ad_viking_shield_round_05", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_6", _name, [("ad_viking_shield_round_06", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_7", _name, [("ad_viking_shield_round_07", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_8", _name, [("ad_viking_shield_round_08", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_9", _name, [("ad_viking_shield_round_09", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_10", _name, [("ad_viking_shield_round_10", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_11", _name, [("ad_viking_shield_round_11", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_12", _name, [("ad_viking_shield_round_12", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_13", _name, [("ad_viking_shield_round_13", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_15", _name, [("ad_viking_shield_round_15", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_16", _name, [("ad_viking_shield_round_16", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_17", _name, [("ad_viking_shield_round_17", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_18", _name, [("ad_viking_shield_round_18", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_19", _name, [("ad_viking_shield_round_19", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_20", _name, [("ad_viking_shield_round_20", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_21", _name, [("ad_viking_shield_round_21", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_22", _name, [("ad_viking_shield_round_22", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_23", _name, [("ad_viking_shield_round_23", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_24", _name, [("ad_viking_shield_round_24", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_25", _name, [("ad_viking_shield_round_25", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_26", _name, [("ad_viking_shield_round_26", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_27", _name, [("ad_viking_shield_round_27", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_28", _name, [("ad_viking_shield_round_28", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_29", _name, [("ad_viking_shield_round_29", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_30", _name, [("ad_viking_shield_round_30", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_31", _name, [("ad_viking_shield_round_31", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_32", _name, [("ad_viking_shield_round_32", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_33", _name, [("ad_viking_shield_round_33", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_34", _name, [("ad_viking_shield_round_34", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_35", _name, [("ad_viking_shield_round_35", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_36", _name, [("ad_viking_shield_round_36", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_37", _name, [("ad_viking_shield_round_37", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_38", _name, [("ad_viking_shield_round_38", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_39", _name, [("ad_viking_shield_round_39", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_40", _name, [("ad_viking_shield_round_40", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_viking_41", _name, [("ad_viking_shield_round_41", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_42", _name, [("ad_viking_shield_round_42", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_viking_43", _name, [("ad_viking_shield_round_43", 0)]] + shield_properties(1, 70) + [[], saxon_factions + jute_factions + engle_factions],
]
items += lvl1_saxon_heavy_shields
shields['saxon'][1]['heavy'] = ['itm_' + x[0] for x in lvl1_saxon_heavy_shields]

# lvl 2 heavy shields
_name = "Adv. Saxon Shield"
lvl2_saxon_heavy_shields = [
    ["shield_saxon_1", _name, [("saxon_adorno_1", 0)]] + shield_properties(2, 70, True) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_2", _name, [("saxon_adorno_2", 0)]] + shield_properties(2, 70, True) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_3", _name, [("saxon_adorno_3", 0)]] + shield_properties(2, 70, True) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_4", _name, [("saxon_adorno_4", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_5", _name, [("saxon_adorno_5", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_6", _name, [("saxon_adorno_6", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_saxon_7", _name, [("saxon_adorno_7", 0)]] + shield_properties(2, 70) + [], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_8", _name, [("saxon_adorno_8", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_saxon_9", _name, [("saxon_adorno_9", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_saxon_10", _name, [("saxon_adorno_10", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_11", _name, [("saxon_adorno_11", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_12", _name, [("saxon_adorno_12", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    # ["shield_saxon_13", _name, [("saxon_adorno_13", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_14", _name, [("saxon_adorno_14", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_15", _name, [("saxon_adorno_15", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_16", _name, [("saxon_adorno_16", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_17", _name, [("saxon_adorno_17", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_18", _name, [("saxon_adorno_18", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_19", _name, [("saxon_adorno_19", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
    ["shield_saxon_20", _name, [("saxon_adorno_20", 0)]] + shield_properties(2, 70) + [[], saxon_factions + jute_factions + engle_factions],
]
items += lvl2_saxon_heavy_shields
shields['saxon'][2]['heavy'] = ['itm_' + x[0] for x in lvl2_saxon_heavy_shields]


######################### briton_factions #########################

# lvl 0 light shield
_name = "Small Briton Shield"
lvl0_saxon_light_shields = [
    ["shield_gaelic_small_20", _name, [("buckler20", 0)]] + shield_properties(0, 30, True) + [[], briton_factions],
    ["shield_gaelic_small_21", _name, [("buckler21", 0)]] + shield_properties(0, 30, True) + [[], briton_factions],
    ["shield_gaelic_small_22", _name, [("buckler22", 0)]] + shield_properties(0, 30, True) + [[], briton_factions],
]
items += lvl0_saxon_light_shields
shields['briton'][0]['light'] = ['itm_' + x[0] for x in lvl0_saxon_light_shields]

# lvl 0 heavy
_name = "Simple Briton Shield"
lvl0_briton_heavy_shields = [
    ["shield_celtic_adorno_1", _name, [("celticsaxon_adorno_1", 0)]] + shield_properties(0, 70, True) + [[], briton_factions],
    ["shield_celtic_adorno_2", _name, [("celticsaxon_adorno_2", 0)]] + shield_properties(0, 70, True) + [[], briton_factions],
    ["shield_celtic_adorno_3", _name, [("celticsaxon_adorno_3", 0)]] + shield_properties(0, 70, True) + [[], briton_factions],
    ["shield_celtic_adorno_4", _name, [("celticsaxon_adorno_4", 0)]] + shield_properties(0, 70) + [[], briton_factions],
    ["shield_celtic_adorno_5", _name, [("celticsaxon_adorno_5", 0)]] + shield_properties(0, 70) + [[], briton_factions],
]
items += lvl0_briton_heavy_shields
shields['briton'][0]['heavy'] = ['itm_' + x[0] for x in lvl0_briton_heavy_shields]

# lvl 1 heavy
_name = "Standard Briton Shield"
lvl1_briton_heavy_shields = [
    ["shield_celtic_adorno_6", _name, [("celticsaxon_adorno_6", 0)]] + shield_properties(0, 70) + [[], briton_factions],
    ["shield_celtic_adorno_7", _name, [("celticsaxon_adorno_7", 0)]] + shield_properties(0, 70) + [[], briton_factions],
    ["shield_celtic_adorno_8", _name, [("celticsaxon_adorno_8", 0)]] + shield_properties(0, 70) + [[], briton_factions],
    ["shield_celtic_adorno_9", _name, [("celticsaxon_adorno_9", 0)]] + shield_properties(0, 70) + [[], briton_factions],
    ["shield_celtic_adorno_10", _name, [("celticsaxon_adorno_10", 0)]] + shield_properties(0, 70) + [[], briton_factions],
]
items += lvl1_briton_heavy_shields
shields['briton'][1]['heavy'] = ['itm_' + x[0] for x in lvl1_briton_heavy_shields]

# lvl 2 heavy
_name = "Heavy Briton Shield"
lvl2_briton_heavy_shields = [
    ["shield_briton_1", _name, [("shield_round_01", 0)]] + shield_properties(1, 70, True) + [[], briton_factions],
    ["shield_briton_2", _name, [("shield_round_02", 0)]] + shield_properties(1, 70, True) + [[], briton_factions],
    ["shield_briton_3", _name, [("shield_round_03", 0)]] + shield_properties(1, 70, True) + [[], briton_factions],
    ["shield_briton_4", _name, [("shield_round_04", 0)]] + shield_properties(1, 70) + [[], briton_factions],
    ["shield_briton_5", _name, [("shield_round_05", 0)]] + shield_properties(1, 70) + [[], briton_factions],
    ["shield_briton_6", _name, [("shield_round_06", 0)]] + shield_properties(1, 70) + [[], briton_factions],
    ["shield_briton_7", _name, [("shield_round_07", 0)]] + shield_properties(1, 70) + [[], briton_factions],
    ["shield_briton_8", _name, [("shield_round_08", 0)]] + shield_properties(1, 70) + [[], briton_factions],
]
items += lvl2_briton_heavy_shields
shields['briton'][2]['heavy'] = ['itm_' + x[0] for x in lvl2_briton_heavy_shields]

_name = "Cantabrian Shield"
lvl3_cantabrian_heavy_shields = [
    ["shield_cantabro_1", _name, [("cantabro_shield_1", 0)]] + shield_properties(3, 70),
    ["shield_cantabro_2", _name, [("cantabro_shield_2", 0)]] + shield_properties(3, 70),
    ["shield_cantabro_3", _name, [("cantabro_shield_3", 0)]] + shield_properties(3, 70),
    ["shield_cantabro_4", _name, [("cantabro_shield_4", 0)]] + shield_properties(3, 70),
    ["shield_cantabro_5", _name, [("cantabro_shield_5", 0)]] + shield_properties(3, 70),
    ["shield_cantabro_6", _name, [("cantabro_shield_6", 0)]] + shield_properties(3, 70),
    ["shield_cantabro_7", _name, [("cantabro_shield_7", 0)]] + shield_properties(3, 70),
    ["shield_cantabro_8", _name, [("cantabro_shield_8", 0)]] + shield_properties(3, 70),
    ["shield_cantabro_9", _name, [("cantabro_shield_9", 0)]] + shield_properties(3, 70),
    ["shield_cantabro_10", _name, [("cantabro_shield_10", 0)]] + shield_properties(3, 70),
]
items += lvl3_cantabrian_heavy_shields
shields['cantabrian'][3]['heavy'] = ['itm_' + x[0] for x in lvl3_cantabrian_heavy_shields]


# erase empty dictionaries so the compiler errors when the user asks for an empty list
to_delete = []
for culture in shields:
    for lvl in [0, 1, 2]:
        for type in ['light', 'normal', 'heavy']:
            if not shields[culture][lvl][type]:
                to_delete.append((culture, lvl, type))

for x in to_delete:
    # it may have been already deleted since the dict are shallow copies
    if x[2] in shields[x[0]][x[1]]:
        # if not, delete it
        del shields[x[0]][x[1]][x[2]]
