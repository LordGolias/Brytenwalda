from header_troops import *
from header_skills import *

from module_items_shields import shields as items_shields



# knows_warrior_basic = knows_weapon_master_2|knows_ironflesh_2|knows_athletics_2|knows_power_strike_2|knows_shield_2|knows_inventory_management_1|knows_power_throw_2 #cambiado chief # TML Adjusted power strike levels on these a bit. #F123
# knows_warrior_normal = knows_weapon_master_5|knows_ironflesh_5|knows_athletics_6|knows_riding_4|knows_power_strike_3|knows_shield_2|knows_inventory_management_2|knows_power_throw_3 #cambiado chief #F123
# knows_warrior_veteran = knows_weapon_master_7|knows_ironflesh_7|knows_athletics_6|knows_riding_7|knows_power_strike_3|knows_shield_3|knows_inventory_management_3|knows_power_throw_4 #cambiado chief #F123
# knows_warrior_elite = knows_weapon_master_9|knows_ironflesh_9|knows_athletics_6|knows_riding_9|knows_power_strike_4|knows_shield_3|knows_inventory_management_4|knows_power_throw_5 #cambiado chief #F123

# # saxons
# upgrade2(troops, "saxon_recruit", "saxon_footmant2", "saxon_archer")
# upgrade2(troops, "saxon_footmant2", "saxon_skirmishert3", "saxon_infantryt3")
#
# upgrade2(troops, "saxon_skirmishert3", "saxon_skirmishert4", "saxon_horseman1")
# upgrade(troops, "saxon_skirmishert4", "saxon_skirmishert5")
#
# upgrade(troops, "saxon_infantryt3", "saxon_infantryt4")
# upgrade(troops, "saxon_infantryt4", "saxon_infantryt5")


# each level contains light, medium and heavy
#   level: represents difficulty and strength of the shield.
#   type: represents heaviness within the level
_troop_attributes = {
    0: {
        # saxon_recruit
        'infantary': {
            'flags': tf_guarantee_boots | tf_guarantee_armor,
            'attrs': def_attrib | level(16),
            'wp': wp(100),
            'skills': knows_warrior_basic,
        },
        # saxon_archer
        'missile': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_ranged,
            'attrs': basic_ranged_attrib|level(16),
            'wp': wp_archer(54),
            'skills': knows_warrior_basic | knows_power_draw_2 | knows_power_throw_1,
            'name': '(Missile)',
         },
    },

    1: {
        # saxon_footmant2
        'infantary': {
            'flags': tf_guarantee_boots | tf_guarantee_armor,
            'attrs': def_attrib2 | level(20),
            'wp': wp(140),
            'skills': knows_warrior_basic,
            'shields': [(0, 'light')],
        },
    },

    2: {
        # saxon_infantryt3
        'infantary': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield,
            'attrs': def_attrib2|level(24),
            'wp': wp(180),
            'skills': knows_warrior_normal,
            'shields': [(1, 'heavy')],
        },
    },

    3: {
        # saxon_infantryt4
        'infantary': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield | tf_guarantee_helmet,
            'attrs': def_attrib3 | level(28),
            'wp': wp(220),
            'skills': knows_warrior_veteran,
            'shields': [(2, 'heavy')]
        },

        # saxon_horseman1
        'cavalary': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield | tf_guarantee_helmet |
                     tf_guarantee_gloves | tf_guarantee_ranged | tf_guarantee_horse | tf_mounted,
            'attrs': def_attrib3 | level(28),
            'wp': wp(220),
            'skills': knows_warrior_veteran,
            'shields': [(0, 'light')]
        },

        # saxon_messenger
        'messenger': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_gloves | tf_guarantee_horse | tf_mounted,
            'attrs': def_attrib3|agi_21|level(28),
            'wp': wp(200),
            'skills': knows_common | knows_riding_7 | knows_power_throw_2,
            'shields': [(0, 'light')]
        },
    },

    4: {
        # saxon_infantryt5
        'infantary': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield | tf_guarantee_helmet |
                     tf_guarantee_gloves,
            'attrs': def_attrib3 | level(32),
            'wp': wp(260),
            'skills': knows_warrior_elite,
            'shields': ['itm_shield_banner_heavy_3'],
        },
    },
}


def troop_properties(lvl, type, culture, other_items, shields=None, faction=None):
    attrs = _troop_attributes[lvl][type]

    possible_shields = []
    # if troop requires shields
    if not shields and 'shields' in attrs:
        for shield_prop in attrs['shields']:
            if isinstance(shield_prop, tuple):
                shield_lvl = shield_prop[0]
                shield_type = shield_prop[1]
                possible_shields += items_shields[culture][shield_lvl][shield_type]
            else:
                possible_shields += attrs['shields']
    elif shields:
        possible_shields = shields

    if faction is None:
        faction = 'fac_neutral'

    return [
        attrs['flags'],
            no_scene, reserved, faction,
            other_items + possible_shields, attrs['attrs'], attrs['wp'],
            attrs['skills']]


items_saxon_recruit = ['itm_stones1','itm_slingrocks','itm_basic_sling','itm_ankleboots','itm_cheap_shoes','itm_woolencap_newgrn','itm_woolencap_newblk','itm_woolencap_newblk','itm_woolencap','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_briton_tunic2','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic1','itm_ptunic12','itm_knifechp','itm_spear_sharppitchfork','itm_clubsmooth','itm_quarter_staff','itm_sickle','itm_axe1','itm_club_stick']
items_saxon_footmant2 = ['itm_javelins','itm_slingrocks','itm_basic_sling','itm_fustibalus','itm_ankleboots','itm_cheap_shoes','itm_woolencap_red','itm_woolencap_newgrn','itm_woolencap_newblk','itm_plaincloakbeige','itm_plaincloakbrown','itm_plaincloakltblue','itm_merch_furjacketwhite','itm_merch_furjacket2t3','itm_merch_furjacketyelo','itm_club_thorny','itm_club3','itm_seaxt4','itm_germanshortspeart2']
items_saxon_infantryt3 = ['itm_javelins','itm_shoes2grey','itm_shoes1green','itm_shoes1orange','itm_woolencap_newblk','itm_woolencap_newblk','itm_rathos_bowlhelmet','itm_rawhide_vest_green','itm_rawhide_coat9grey','itm_rawhide_vest_blue','itm_rawhide_coat2','itm_rawhide_coat2','itm_spear1','itm_langseaxt2']
items_saxon_infantryt4 = ['itm_angons','itm_angonst2','itm_leather_gloves1','itm_noble_shoesorange','itm_greaves1','itm_greaves1','itm_lorica_whitbrn','itm_woolencap_newblu','itm_woolencap_red','itm_woolencap_newblk','itm_woolencap','itm_leather_captainhelm','itm_leathercap1','itm_dena_helmgoat','itm_leathercap1','itm_skullcap_reinforcedt2','itm_bamburghsword2t2','itm_spear_hasta','itm_langseaxt2']
items_saxon_infantryt5 = ['itm_angons','itm_angonst2','itm_leather_gloves1','itm_leather_bootstall','itm_splinted_leather_greaves','itm_mailtunic_brownclk','itm_mailtunic_ltbrown','itm_lorica_greyrd','itm_lorica_stripedblue','itm_wolfpelt_mail_coat','itm_mailtunic_brownclk','itm_mailtunic_blk','itm_mailtunic_brown','itm_mailtunic_blk','itm_mailtunic_brownclk','itm_noblearmor16res','itm_mailtunic_grey','itm_jutehelmt3','itm_jutehelmt3','itm_dena_elite_helm2boar','itm_copper_helmet','itm_saxon_helmt2','itm_spangenhelmb1','itm_dena_helmgoat','itm_spear_hvy','itm_spear_hasta','itm_saxonswordt2','itm_briton_richswordt2','itm_jute_richsword']
items_saxon_archer = ['itm_arrows1','itm_shortbow','itm_huntingbow','itm_leather_shoes','itm_ankleboots','itm_cheap_shoes','itm_woolencap_newblu','itm_woolencap_red','itm_woolencap_newgrn','itm_woolencap','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_briton_tunic2','itm_ptunic2','itm_mercia_tunicgrn','itm_ptunic1','itm_clubcudgel','itm_seaxt3','itm_saxon_axet2']

items_saxon_skirmisher3 = ['itm_javelins','itm_javelins','itm_shoes1blue','itm_shoes2grey','itm_shoes1green','itm_shoes1orange', 'itm_rawhide_coat6white','itm_rawhide_vest_red','itm_pelt_coat2','itm_merch_furjacketyelo', 'itm_axe_longfrankisht3','itm_saxon_medium_speart2','itm_spearlight','itm_langseaxt2', 'itm_knisxclearvert3']
items_saxon_skirmisher4 = ['itm_angons','itm_javelins','itm_angonst2','itm_leather_gloves1','itm_shoes1','itm_shoes1green','itm_plaincloakltblue','itm_plaincloakbrown','itm_plaincloakbeige','itm_jack_armorpaddedred','itm_jack_armorfadedblue','itm_jack_armorfadedblue','itm_vae_thickcoat3','itm_leather_helm_tan','itm_hornhelmet3_t2','itm_rathos_bowlhelmet','itm_spangenhelmblight','itm_langseaxt2','itm_spearlight','itm_axe4','itm_axe2_crude','itm_germanic_axelongt2']
items_saxon_skirmisher5 = ['itm_angons','itm_angonst2','itm_leather_gloves1','itm_noble_shoesorange','itm_shoes1', 'itm_noble_shoesorange','itm_lorica_eggwht','itm_lorica_olive','itm_noblearmor16res', 'itm_lorica_yelo','itm_mailshirt_3_trig','itm_spangenhelmalight','itm_spangenhelma1', 'itm_frisian_helm3t2','itm_dena_helmboar3','itm_briton_helm','itm_copper_helmet', 'itm_jutehelmt3','itm_battle_axe2ht2','itm_saxonswordt2','itm_germanicswordt2']
items_saxon_horseman1 = ['itm_javelins','itm_horsecourser2','itm_roman_horse1','itm_roman_horse2','itm_frankishhorse1','itm_pictish_stallion','itm_horsecourser1','itm_horsecourser2','itm_drafthorse1','itm_shoes1blue','itm_shoes2green','itm_greaves1','itm_noble_shoesorange','itm_jack_armorgreen','itm_jack_armorgreen','itm_lorica_pink','itm_noblearmor14res','itm_mailnoble_ltbrwnclk','itm_lorica_greyrd','itm_spangenhelmb1','itm_frisian_helm3t2','itm_saxon_helmt2','itm_spangenhelma_yellow','itm_hornhelmet2','itm_hornhelmet1','itm_hornhelmet3_t2','itm_maul1h_blunt','itm_spearlong','itm_saxonswordt2','itm_germanicswordt2']
items_saxon_messenger = ['itm_leather_gloves1','itm_javelins','itm_roman_horse1','itm_shoes2green','itm_shoes2grey','itm_greaves1','itm_noble_shoesorange','itm_greaves1','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_spear1','itm_spearlight','itm_langseaxt2']
items_saxon_deserter = ['itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_shoes1','itm_shoes1blue','itm_shoes2grey','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_woolencap_newblu','itm_woolencap_red','itm_woolencap_newblk','itm_woolencap','itm_leather_captainhelm','itm_leathercap1','itm_bowlhelmet','itm_hornhelmet2','itm_leathercap1','itm_axe_longfrankisht3','itm_saxon_medium_speart2','itm_spearlight','itm_spearboar','itm_langseaxt2','itm_knisxclearvert3','itm_spearlight']
items_saxon_guard = ['itm_angons','itm_leather_gloves1','itm_greaves1','itm_rawhide_coat7green','itm_linen_coatbrown','itm_linen_coatblue','itm_woolencap_newblk','itm_woolencap','itm_bowlhelmet','itm_hornhelmet2','itm_leathercap1','itm_spear_hvy','itm_langseaxt2']

saxon_troops = [
    ["saxon_recruit", "Gebur Seaxe (L. Inf.)", "Geburas Seaxna"] +
    troop_properties(0, 'infantary', 'saxon', items_saxon_recruit) +
    [vaegir_face_younger_1, vaegir_face_middle_2],

    ["saxon_footmant2", "Kotsetla Seaxe (Lig. I.)", "Kotsetlas Seaxna"] +
    troop_properties(1, 'infantary', 'saxon', items_saxon_footmant2) +
    [vaegir_face_young_1, vaegir_face_middle_2],

    ["saxon_archer", "Sceotand Seaxe (Missile)", "Sceotandas Seaxna"] +
    troop_properties(0, 'missile', 'saxon', items_saxon_archer) +
    [vaegir_face_young_1, vaegir_face_middle_2],

    ["saxon_bannerman", "Tacnberend", "Tacnberend",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_shoes1','itm_shoes1','itm_plaincloakbeige','itm_plaincloakred','itm_plaincloakbrown','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_blue_shorttunic','itm_ptunic13','itm_goatcap1','itm_goat_capbrn','itm_boar_helmet','itm_wessexbanner1','itm_heraldicbannert3','itm_trophy_b','itm_leather_gloves1'],def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1,vaegir_face_old_2],
    ["todos_cuerno", "Hornman", "Hornmen",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_leather_shoes','itm_ankleboots','itm_cheap_shoes','itm_plaincloakbeige','itm_plaincloakred','itm_plaincloakbrown','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_horn1','itm_trophy_a','itm_stones1','itm_knisxclearvert3'] + items_shields['common'][0]['light'],def_attrib2|level(15),wp(115),knows_warrior_normal,vaegir_face_young_1,vaegir_face_old_2],
    ["saxon_sacerdote", "Cleric Seaxe", "Clerics Seaxna",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_noble_shoesorange','itm_shoes1','itm_noble_shoesorange','itm_noble_shoesblue','itm_shoes1blue','itm_monk_robe','itm_blackwht_robe','itm_stones1','itm_staff1'],def_attrib|level(23),wp(170),knows_cleric,sac_face_1,sac_face_2],

    ["saxon_skirmishert3", "Geneata Seaxe (Med. I.)", "Geneatas Seaxna"] +
    troop_properties(1, 'infantary', 'saxon', items_saxon_skirmisher3, shields=items_shields['saxon'][0]['normal']) +
    [vaegir_face_young_1, vaegir_face_old_2],

    ["saxon_infantryt3", "Geoguth Seaxe (Med. I.)", "Geoguthas Seaxna"] +
    troop_properties(2, 'infantary', 'saxon', items_saxon_infantryt3) +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["saxon_skirmishert4", "Beadu rinc Seaxe (Med. I.)", "Beadu rincas Seaxna"] +
    troop_properties(2, 'infantary', 'saxon', items_saxon_skirmisher4, shields=items_shields['saxon'][1]['normal']) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["saxon_horseman1", "Gesith Seaxe (Lig. C.)", "Gesithas Seaxna"] +
    troop_properties(3, 'cavalary', 'saxon', items_saxon_horseman1, shields=items_shields['saxon'][1]['normal']) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["saxon_skirmishert5", "Ridwiga Seaxe (Hv. I.)", "Ridwigas Seaxna"] +
    troop_properties(4, 'infantary', 'saxon', items_saxon_skirmisher5) +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["saxon_infantryt4", "Duguth Seaxe (Hv. I.)", "Duguthas Seaxna"] +
    troop_properties(3, 'infantary', 'saxon', items_saxon_infantryt4) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["saxon_infantryt5", "Hearthweru Seaxe (Elit. I.)", "Hearthweruas Seaxna"] +
    troop_properties(4, 'infantary', 'saxon', items_saxon_infantryt5) +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["saxon_messenger", "Horsweala Seaxe", "Horswealas Seaxna"] +
    troop_properties(3, 'messenger', 'saxon', items_saxon_messenger) +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["saxon_deserter", "Deserter Seaxe", "Deserters Seaxna"] +
    troop_properties(2, 'infantary', 'saxon', items_saxon_deserter, faction='fac_deserters') +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["saxon_prison_guard", "Prison Guard", "Prison Guards"] +
    troop_properties(3, 'infantary', 'saxon', items_saxon_guard, shields=[items_shields['saxon'][1]['normal'][0]]) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["saxon_castle_guard", "Castle Guard", "Castle Guards"] +
    troop_properties(3, 'infantary', 'saxon', items_saxon_guard, shields=[items_shields['saxon'][1]['normal'][0]]) +
    [vaegir_face_middle_1, vaegir_face_older_2],
]
