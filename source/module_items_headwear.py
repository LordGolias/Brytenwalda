from .header_items import *
from .header_item_modifiers import *

imodbits_none = 0
imodbits_cloth = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_plate = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | \
                 imodbit_reinforced | imodbit_lordly


_headwear = {
    'common': {
        0: {'civilian': [], 'military': []},
        1: {'civilian': [], 'military': []},
        2: {'civilian': [], 'military': []},
    },

    'pict': {
        0: {'civilian': [], 'military': []},
        1: {'civilian': [], 'military': []},
        2: {'civilian': [], 'military': []},
    },
    'briton': {
        0: {'military': []},
        1: {'military': []},
        2: {'military': []},
    },
    'saxon': {
        0: {'military': []},
        1: {'military': []},
        2: {'military': []},
    },

    'assassin': [],
    'traveler': [],
}


type_to_int = {
    'civilian': 0,
    'military': 1,
}


def headwear_properties(lvl, type, extra_flags=0, extra_attrs=0):
    is_military = type is 'military'

    flags = itp_merchandise | itp_type_head_armor | itp_attach_armature | itp_fit_to_head
    if not is_military:
        flags |= itp_civilian
    flags |= extra_flags

    return [flags, 0, 500 * (lvl + 1),
            weight(1 + is_military * 0.5 * lvl) |
            abundance(60) |
            head_armor(1 + is_military * (4 + 10 * lvl)) |
            difficulty(is_military * 4**lvl) |
            extra_attrs,
            imodbits_cloth]


# assassin
_headwear['assassin'] = [
    ["headwear_2c_assassin_1", "Hood", [("pictish_hood", 0)]] + headwear_properties(2, 'civilian'),
    ["headwear_2c_assassin_2", "Hood", [("youhou_assassin_hood", 0)]] + headwear_properties(2, 'civilian'),
    ["headwear_2c_assassin_3", "Red Hood", [("youhou_assassin_hood_red", 0)]] + headwear_properties(2, 'civilian'),
]

# travelers
for index, mesh_name in enumerate(['capalost1', 'capaslost2', 'cloak10', 'cloak11', 'cloak12',
                                   'cloak30', 'cloak27', 'cloak28', 'cloak29']):
    _headwear['traveler'].append(
        ['headwear_0c_traveler_%d' % index, "Travellers Coat", [(mesh_name, 0)]] +
        headwear_properties(0, 'civilian', extra_flags=itp_doesnt_cover_hair | itp_fit_to_head, extra_attrs=body_armor(1))
    )

# hood is military 0; woolen_cap is civilian 0
for mesh in ['hood', 'woolen_cap']:
    for color in ['blu', 'red', 'grn', 'blk', 'wht']:
        is_military = (mesh is 'hood')
        if is_military:
            type = 'military'
        else:
            type = 'civilian'

        mesh_name = "%s_new%s" % (mesh, color)
        id = "headwear_0%s_%s_%s" % (type[0], mesh, color)
        name = "%s %s" % ({'blu': 'Blue', 'red': 'Red', 'grn': 'Green', 'blk': 'Black', 'wht': 'White'}[color],
                          {'woolen_cap': 'Phrygian Cap', 'hood': 'Hood'}[mesh])

        _headwear['common'][0][type].append(
             [id, name, [(mesh_name, 0)]] + headwear_properties(0, type)
        )


# lvl 0: BL_coat01, BL_coat01c, BL_coat01b, BL_coat02, BL_coat03b, BL_coat04
# lvl 1: BL_coat03c, BL_coat04b, BL_coat06b, BL_coat06c
# lvl 2: BL_coat08b, BL_coat08c, BL_coat09b, BL_coat09c, BL_coat04X, BL_coat04X1
# lvl 0 battle: BL_boar, BL_boar_fur, BL_boar_hat


# lvl 0 coats
for index, mesh_name in enumerate(['BL_coat01', 'BL_coat02', 'BL_coat03b', 'BL_coat04', 'BL_coat11',
                                   'BL_coat12', 'BL_coat14', 'BL_coat16', 'BL_coat19', 'BL_coat013']):
    _headwear['common'][0]['civilian'].append(
        ['headwear_0c_coat_%d' % index, "Cheap coat", [(mesh_name, 0)]] +
        headwear_properties(0, 'civilian', extra_flags=itp_doesnt_cover_hair | itp_fit_to_head, extra_attrs=body_armor(1))
    )


# lvl 1 coats
for index, mesh_name in enumerate(['BL_coat09b', 'BL_coat08b', 'BL_coat06b', 'BL_coat06c', 'BL_coat11c', 'BL_coat013a']):
    _headwear['common'][1]['civilian'].append(
        ['headwear_1c_coat_%d' % index, "Coat", [(mesh_name, 0)]] +
        headwear_properties(1, 'civilian', extra_flags=itp_doesnt_cover_hair | itp_fit_to_head, extra_attrs=body_armor(1))
    )


# lvl 2 coats
for index, mesh_name in enumerate(['BL_coat03c', 'BL_coat04b', 'BL_coat08c', 'BL_coat09c', 'BL_coat04X1',
                                   'BL_coat12b', 'BL_coat14b', 'BL_coat19c']):
    _headwear['common'][2]['civilian'].append(
        ['headwear_2c_coat_%d' % index, "Expensive Coat", [(mesh_name, 0)]] +
        headwear_properties(2, 'civilian', extra_flags=itp_doesnt_cover_hair | itp_fit_to_head, extra_attrs=body_armor(1))
    )


_headwear['furs'] = [
    ["cloak_boar_fur", "Fur Cloak", [("BL_boar_fur", 0)],
     itp_type_head_armor | itp_attach_armature | itp_fit_to_head | itp_doesnt_cover_hair, 0, 300,
     weight(1.5) | abundance(60) | head_armor(5) | body_armor(15) | leg_armor(0) | difficulty(4), imodbits_cloth,
     [], saxon_factions + jute_factions + engle_factions],

    ["cloak_boar_furcap", "Boar Fur", [("BL_boar", 0)], itp_type_head_armor | itp_attach_armature | itp_fit_to_head, 0,
     1580, weight(3) | abundance(60) | head_armor(5) | body_armor(13) | leg_armor(0) | difficulty(4), imodbits_cloth,
     [], saxon_factions + jute_factions + engle_factions],

    ["boar_helmet", "Boar Hat", [("BL_boarhelmet", 0)], itp_type_head_armor | itp_civilian, 0, 700,
     weight(2) | abundance(60) | head_armor(5) | body_armor(2) | leg_armor(0) | difficulty(3), imodbits_cloth],
    ["goatcap1", "Goat Cap", [("goat_cap", 0)], itp_type_head_armor | itp_civilian, 0, 700,
     weight(2) | abundance(60) | head_armor(5) | body_armor(2) | leg_armor(0) | difficulty(3), imodbits_cloth],
    ["goat_capbrn", "Goat Hat", [("goat_bascinet", 0)], itp_type_head_armor | itp_civilian, 0, 700,
     weight(2) | abundance(60) | head_armor(5) | body_armor(2) | leg_armor(0) | difficulty(3), imodbits_cloth],
]


_headwear['common'][0]['civilian'] += [
    ["headwear_straw_hat", "Straw Hat", [("straw_hat_new_bry", 0)]] + headwear_properties(0, 'civilian')
]


############## Common ##############
_headwear['common'][0]['military'] += [
    ["headwear_0m_1", "Leather Helmet", [("leather_cap_a_new_bry", 0)]] + headwear_properties(0, 'military'),
    ["headwear_0m_2", "Leather Helmet", [("skull_cap_new_b_bry", 0)]] + headwear_properties(0, 'military'),
    ["headwear_0m_3", "Leather Helmet", [("skull_cap_new_a_bry", 0)]] + headwear_properties(0, 'military'),
    ["headwear_0m_4", "Leather Helmet", [("skull_cap_new_c", 0)]] + headwear_properties(0, 'military'),
    ["headwear_0m_5", "Leather Helmet with Plum", [("helm_captainA", 0)]] + headwear_properties(0, 'military'),
    ["headwear_0m_6", "Leather Helmet with Plum", [("rath_spangenlord3", 0)]] + headwear_properties(0, 'military'),
    ["headwear_0m_7", "Leather Helmet", [("rath_spangenlord2", 0)]] + headwear_properties(0, 'military'),
    ["headwear_0m_8", "Leather Helmet", [("rath_spangenlord5", 0)]] + headwear_properties(0, 'military'),
]

_headwear['common'][1]['military'] += [
    ["headwear_1m_1", "Bowl Helmet", [("Rathos_bowl_helmet", 0)]] + headwear_properties(1, 'military'),
    ["headwear_1m_2", "Bowl Helmet", [("bowl_helmet_nasal", 0)]] + headwear_properties(1, 'military'),
    ["headwear_1m_3", "Bowl Helmet", [("bowl_helmet", 0)]] + headwear_properties(1, 'military'),
    ["headwear_1m_4", "Roman Helmet", [("old_spangenhelm", 0)]] + headwear_properties(1, 'military'),
    ["headwear_1m_5", "Roman Helmet", [("old_spangenhelmcheek", 0)]] + headwear_properties(1, 'military'),
    ["headwear_1m_6", "Helmet", [("barf_helm", 0)]] + headwear_properties(1, 'military'),
    ["headwear_1m_7", "Helmet", [("helmetx2", 0)]] + headwear_properties(1, 'military'),
]

_headwear['common'][2]['military'] += [
    ["headwear_2m_1", "Elite Roman Helmet", [("spangenhelm_a", 0)]] + headwear_properties(2, 'military'),
    ["headwear_2m_2", "Elite Roman Helmet", [("spangenhelm_a_trim", 0)]] + headwear_properties(2, 'military'),
    ["headwear_2m_3", "Elite Roman Helmet", [("spangenhelm_a_ornate", 0)]] + headwear_properties(2, 'military'),
    ["headwear_2m_4", "Elite Roman Helmet", [("old_spangenhelmaven", 0)]] + headwear_properties(2, 'military'),
]

############## Briton ##############
_headwear['briton'][1]['military'] = [
    ["headwear_1m_briton_1", "Briton Helmet", [("briton_helm", 0)]] + headwear_properties(1, 'military') +
    [[], briton_factions],
    ["headwear_1m_briton_2", "Briton Helmet", [("briton_helm2", 0)]] + headwear_properties(1, 'military') +
    [[], briton_factions],
    ["headwear_1m_briton_3", "Briton Helmet", [("briton_helm3", 0)]] + headwear_properties(1, 'military') +
    [[], briton_factions],
    ["headwear_1m_briton_4", "Briton Helmet", [("briton_helm4", 0)]] + headwear_properties(1, 'military') +
    [[], briton_factions],
    ["headwear_1m_briton_5", "Briton Helmet", [("briton_helm5", 0)]] + headwear_properties(1, 'military') +
    [[], briton_factions],
]

_headwear['briton'][2]['military'] = [
    ["headwear_2m_briton_1", "Elite Briton Helmet", [("briton_helm6", 0)]] + headwear_properties(2, 'military') +
    [[], briton_factions],
    ["headwear_2m_briton_2", "Elite Briton Helmet", [("briton_helm7", 0)]] + headwear_properties(2, 'military') +
    [[], briton_factions],
    ["headwear_2m_briton_3", "Elite Briton Helmet", [("dux_ridge_helm", 0)]] + headwear_properties(2, 'military') +
    [[], briton_factions],
]

############## saxon_factions + jute_factions + engle_factions ##############
_headwear['saxon'][0]['military'] = [
    ["headwear_0m_saxon_1", "Horn Helmet", [("Horn_Helmet", 0)]] + headwear_properties(0, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_0m_saxon_2", "Horn Helmet", [("Horn_Helmet_2", 0)]] + headwear_properties(0, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_0m_saxon_3", "Horn Helmet", [("Horn_Helmet_3", 0)]] + headwear_properties(0, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
]

_name = 'Valsgarde Helmet'
_headwear['saxon'][1]['military'] = [
    ["headwear_1m_saxon_1", _name, [("BL_01_Valsgarde04", 0)]] + headwear_properties(1, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_1m_saxon_2", _name, [("BL_02_Valsgarde04", 0)]] + headwear_properties(1, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_1m_saxon_3", _name, [("BL_03_Valsgarde04", 0)]] + headwear_properties(1, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_1m_saxon_4", _name, [("BL_04_Valsgarde04", 0)]] + headwear_properties(1, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_1m_saxon_5", _name, [("BL_01_Valsgarde05", 0)]] + headwear_properties(1, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_1m_saxon_6", _name, [("BL_02_Valsgarde05", 0)]] + headwear_properties(1, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_1m_saxon_7", _name, [("BL_03_Valsgarde05", 0)]] + headwear_properties(1, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_1m_saxon_8", _name, [("BL_04_Valsgarde05", 0)]] + headwear_properties(1, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_1m_saxon_9", _name, [("BL_01_Valsgarde07", 0)]] + headwear_properties(1, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_1m_saxon_10", _name, [("BL_02_Valsgarde07", 0)]] + headwear_properties(1, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_1m_saxon_11", _name, [("BL_03_Valsgarde07", 0)]] + headwear_properties(1, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_1m_saxon_12", _name, [("BL_04_Valsgarde07", 0)]] + headwear_properties(1, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
]

_name = 'Elite Valsgarde Helmet'
_headwear['saxon'][2]['military'] = [
    ["headwear_2m_saxon_1", _name, [("Valsgarde_guards", 0)]] + headwear_properties(2, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_2m_saxon_2", _name, [("Valsgarde_guards2", 0)]] + headwear_properties(2, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_2m_saxon_3", _name, [("Valsgarde_small", 0)]] + headwear_properties(2, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_2m_saxon_4", _name, [("Valsgarde_new", 0)]] + headwear_properties(2, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_2m_saxon_5", 'Elite Jute Helmet', [("vendel_helmet", 0)]] + headwear_properties(2, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_2m_saxon_6", 'Elite Jute Helmet', [("vendel", 0)]] + headwear_properties(2, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_2m_engle_1", "Elite Anglo Helmet", [("talak_spangenhelm", 0)]] + headwear_properties(2, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
    ["headwear_2m_engle_2", "Elite Anglo Helmet", [("talak_ped_mercian2", 0)]] + headwear_properties(2, 'military') +
    [[], saxon_factions + jute_factions + engle_factions],
]

# ["frisian_helm1", "Frisian Helmet", [("frisian_helmet_mesh", 0)],
#  itp_merchandise | itp_type_head_armor | itp_fit_to_head, 0, 1720,
#  weight(1.5) | abundance(60) | head_armor(30) | body_armor(0) | leg_armor(0) | difficulty(6), imodbits_plate,
#  [], saxon_factions + jute_factions + engle_factions],
# ["jutehelmt3", "Jute Helmet", [("vendel14", 0)], itp_type_head_armor | itp_fit_to_head, 0, 2980,
#  weight(1.5) | abundance(60) | head_armor(45) | body_armor(0) | leg_armor(0) | difficulty(6), imodbits_plate,
#  [], saxon_factions + jute_factions + engle_factions],
# este da problemas con los lods, puede causar fallos vigilar
# ["saxon_helmt2", "Saxon Helm", [("spangenhelm_helm", 0)], itp_type_head_armor | itp_fit_to_head, 0, 1760,
#  weight(2) | abundance(60) | head_armor(34) | body_armor(0) | leg_armor(0) | difficulty(8), imodbits_plate,
#  [], saxon_factions + jute_factions + engle_factions],
# mercios, tambien vale para britones cercanos a mercia, este da problemas con los lods, puede causar fallos vigilar
# ["mierce_helmt3", "Wollaston Mierce helmet", [("wollaston_mercian", 0)],
#  itp_merchandise | itp_type_head_armor | itp_fit_to_head, 0, 1980,
#  weight(2) | abundance(60) | head_armor(39) | body_armor(0) | leg_armor(0) | difficulty(8), imodbits_plate,
#  [], ['fac_kingdom_9']],
# # con goat en cabeza
# ["goat_miercehelmt3", "Goat Wollaston Mierce helmet", [("wollaston_mercian2", 0)],
#  itp_type_head_armor | itp_fit_to_head, 0, 1180,
#  weight(2) | abundance(60) | head_armor(40) | body_armor(0) | leg_armor(0) | difficulty(8), imodbits_plate,
#  [], ['fac_kingdom_9']],

# ["spangenhelma1", "Helm", [("Rathos_Spangenhelm_a", 0)], itp_type_head_armor | itp_fit_to_head, 0, 760,
#  weight(2) | abundance(60) | head_armor(34) | body_armor(0) | leg_armor(0) | difficulty(8), imodbits_plate,
#  [], briton_factions],
# ["spangenhelmb1", "Helm", [("Rathos_Spangenhelm_b", 0)], itp_merchandise | itp_type_head_armor | itp_fit_to_head, 0,
#  760, weight(2) | abundance(60) | head_armor(34) | body_armor(0) | leg_armor(0) | difficulty(8), imodbits_plate,
#  [], briton_factions],
# ["spangenhelmalight", "Light Helm", [("Rathos_Spangenhelm_a_light", 0)],
#  itp_merchandise | itp_type_head_armor | itp_fit_to_head, 0, 720,
#  weight(1.75) | abundance(60) | head_armor(30) | body_armor(0) | leg_armor(0) | difficulty(4), imodbits_plate,
#  [], briton_factions],
# ["spangenhelmblight", "Light Helm", [("Rathos_Spangenhelm_b_light", 0)],
#  itp_merchandise | itp_type_head_armor | itp_fit_to_head, 0, 720,
#  weight(1.75) | abundance(60) | head_armor(30) | body_armor(0) | leg_armor(0) | difficulty(4), imodbits_plate,
#  [], briton_factions],
# # ["spangenhelm_plumed", "Chief Helm", [("Rathos_Spangenhelm_yellow_plum",0)], itp_type_head_armor|itp_fit_to_head ,0, 760 , weight(2)|abundance(60)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,
# # [], briton_factions],
# ["spangenhelma_yellow", "Chief Helm", [("Rathos_Spangenhelm_a_yellow2", 0)], itp_type_head_armor | itp_fit_to_head,
#  0, 2760, weight(2) | abundance(60) | head_armor(34) | body_armor(0) | leg_armor(0) | difficulty(8), imodbits_plate,
#  [], briton_factions],

# # rey juto
# ["jute_king_helm", "King Jute Helmet", [("vendel14_3", 0)], itp_type_head_armor | itp_fit_to_head, 0, 2280,
#  weight(1.5) | abundance(60) | head_armor(50) | body_armor(0) | leg_armor(0) | difficulty(9), imodbits_plate,
#  [], jute_factions],
# # Rey anglo
# ["sutton_hoo_saxonface", "Saxon Prince Helmet", [("talak_sutton_hoo", 0)], itp_type_head_armor | itp_fit_to_head, 0,
#  2320, weight(2.5) | abundance(60) | head_armor(51) | body_armor(0) | leg_armor(0) | difficulty(10),
#  imodbits_plate],
# # rey sajon o juto, o dena pirate
# ["scandza_helm", "Scandza Helmet", [("valsgarde_new", 0)], itp_type_head_armor | itp_fit_to_head | itp_covers_head,
#  0, 2400, weight(3) | abundance(60) | head_armor(52) | body_armor(0) | leg_armor(0) | difficulty(14),
#  imodbits_plate],


############## pict_factions + irish_factions ##############
_headwear['pict'][1]['military'] = [
    ["headwear_1m_pict_1", "Godelic Helmet", [("celtycka_lebka", 0)]] + headwear_properties(1, 'military') +
    [[], pict_factions + irish_factions],
    ["headwear_1m_pict_2", "Godelic Helmet", [("celtycka_iron", 0)]] + headwear_properties(1, 'military') +
    [[], pict_factions + irish_factions],
]


_headwear['pict'][2]['military'] = [
    ["headwear_2m_pict_1", "Elite Godelic Helmet", [("szpadelhelmet", 0)]] + headwear_properties(2, 'military') +
    [[], pict_factions + irish_factions],
    ["headwear_2m_pict_2", "Elite Godelic Helmet", [("szpadelhelmet1", 0)]] + headwear_properties(2, 'military') +
    [[], pict_factions + irish_factions],
    ["headwear_2m_pict_3", "Elite Godelic Helmet", [("szpadelhelmet2", 0)]] + headwear_properties(2, 'military') +
    [[], pict_factions + irish_factions],
    ["headwear_2m_pict_4", "Elite Godelic Helmet", [("szpadelhelmet3", 0)]] + headwear_properties(2, 'military') +
    [[], pict_factions + irish_factions],
    ["headwear_2m_pict_5", "Elite Godelic Helmet", [("szpadelhelmet4", 0)]] + headwear_properties(2, 'military') +
    [[], pict_factions + irish_factions],
    ["headwear_2m_pict_6", "Elite Godelic Helmet", [("szpadelhelmet5", 0)]] + headwear_properties(2, 'military') +
    [[], pict_factions + irish_factions],
    ["headwear_2m_pict_7", "Elite Godelic Helmet", [("szpadelhelmet6", 0)]] + headwear_properties(2, 'military') +
    [[], pict_factions + irish_factions],
]


_crowns = [
    ["headwear_crown_lombardy", "Crown", [("sib_Lombardy", 0)],
     itp_type_head_armor | itp_no_pick_up_from_ground | itp_civilian | itp_doesnt_cover_hair, 0, 10000,
     weight(1) | head_armor(1) | body_armor(0) | leg_armor(0) | difficulty(0), imodbits_none],
    # britones#Pictos#Irish
    ["headwear_crown_couronne", "Crown", [("sib_couronne", 0)],
     itp_type_head_armor | itp_no_pick_up_from_ground | itp_civilian | itp_doesnt_cover_hair, 0, 10000,
     weight(1) | head_armor(1) | body_armor(0) | leg_armor(0) | difficulty(0), imodbits_none],
]


# populate headwear with respective 'itm_*' and items with all items
headwear = dict()
items = _crowns


for culture in ['assassin', 'traveler']:
    items += _headwear[culture]
    headwear[culture] = ['itm_%s' % s[0] for s in _headwear[culture]]


for type in ['civilian', 'military']:
    for culture in ['common', 'briton', 'saxon', 'pict']:
        headwear[culture] = dict()
        for lvl in [0, 1, 2]:
            if type not in _headwear[culture][lvl]:
                continue  # some cultures do not have 'civilian'
            items += _headwear[culture][lvl][type]
            if lvl not in headwear[culture]:
                headwear[culture][lvl] = dict()
            headwear[culture][lvl][type] = ['itm_%s' % s[0] for s in _headwear[culture][lvl][type]]


items += [
    # This helmet is used in decapitation mod to "remove" the head from the agent.
    # It is an empty transparent mesh that fits the head
    ["headwear_nohead", "No head", [("no_head", 0)],
     itp_type_head_armor | itp_fit_to_head | itp_covers_head | itp_no_pick_up_from_ground, 0, 1,
     weight(0) | abundance(60) | head_armor(0) | body_armor(0) | leg_armor(0) | difficulty(0), imodbits_none],
]
