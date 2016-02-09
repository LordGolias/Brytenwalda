from header_troops import *
from header_skills import *

from module_items_shields import shields as items_shields


_troop_attributes = {
    0: {
        # recruit
        'infantry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor,
            'attrs': def_attrib | level(16),
            'wp': wp(100),
            'skills': knows_warrior_basic,
        },

        # archer
        'archer': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_ranged,
            'attrs': basic_ranged_attrib|level(16),
            'wp': wp_archer(54),
            'skills': knows_warrior_basic | knows_power_draw_2 | knows_power_throw_1,
            'name': '(Missile)',
         },
    },

    1: {
        # weak infantry (no shield guaranteed)
        'infantry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor,
            'attrs': def_attrib2 | level(20),
            'wp': wp(140),
            'skills': knows_warrior_basic,
            'shields': [(0, 'light')],
        },
    },

    2: {
        # standard infantry (heavy shield, no helmet guaranteed)
        'infantry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield,
            'attrs': def_attrib2|level(24),
            'wp': wp(180),
            'skills': knows_warrior_normal,
            'shields': [(1, 'heavy')],
        },

        # good archers (attributes)
        'archer': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_ranged,
            'attrs': veteran_ranged_attrib | str_14 | level(24),
            'wp': wp(70) | wp_archery(150),
            'skills': knows_warrior_normal | knows_power_draw_6,
        }
    },

    3: {
        # strong infantry (all of lvl 2 + helmet, no gloves guaranteed)
        'infantry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield | tf_guarantee_helmet,
            'attrs': def_attrib3 | level(28),
            'wp': wp(220),
            'skills': knows_warrior_veteran,
            'shields': [(2, 'heavy')]
        },

        # saxon_horseman1
        'cavalry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield | tf_guarantee_helmet |
                     tf_guarantee_gloves | tf_guarantee_ranged | tf_guarantee_horse | tf_mounted,
            'attrs': def_attrib3 | level(28),
            'wp': wp(220),
            'skills': knows_warrior_veteran,
            'shields': [(1, 'normal')]
        },

        # saxon_messenger
        'messenger': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_gloves | tf_guarantee_horse | tf_mounted,
            'attrs': def_attrib3|agi_21|level(28),
            'wp': wp(200),
            'skills': knows_common | knows_riding_7 | knows_power_throw_2,
            'shields': items_shields['banner'][1]['normal'],
        },
    },

    4: {
        # elite infantry (fully equipped, lvl 3 heavy banner shield)
        'infantry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield | tf_guarantee_helmet |
                     tf_guarantee_gloves,
            'attrs': def_attrib3 | level(32),
            'wp': wp(260),
            'skills': knows_warrior_elite,
            'shields': ['itm_shield_banner_heavy_3'],
        },

        # elite cavalry (fully equipped, lvl 3 banner shield)
        'cavalry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield | tf_guarantee_helmet |
                     tf_guarantee_gloves | tf_guarantee_horse | tf_mounted,
            'attrs': def_attrib3 | level(32),
            'wp': wp(260),
            'skills': knows_warrior_elite,
            'shields': items_shields['banner'][3]['normal'],
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
    troop_properties(0, 'infantry', 'saxon', items_saxon_recruit) +
    [vaegir_face_younger_1, vaegir_face_middle_2],

    ["saxon_footmant2", "Kotsetla Seaxe (Lig. I.)", "Kotsetlas Seaxna"] +
    troop_properties(1, 'infantry', 'saxon', items_saxon_footmant2) +
    [vaegir_face_young_1, vaegir_face_middle_2],

    ["saxon_archer", "Sceotand Seaxe (Missile)", "Sceotandas Seaxna"] +
    troop_properties(0, 'archer', 'saxon', items_saxon_archer) +
    [vaegir_face_young_1, vaegir_face_middle_2],

    ["saxon_bannerman", "Tacnberend", "Tacnberend",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_shoes1','itm_shoes1','itm_plaincloakbeige','itm_plaincloakred','itm_plaincloakbrown','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_blue_shorttunic','itm_ptunic13','itm_goatcap1','itm_goat_capbrn','itm_boar_helmet','itm_wessexbanner1','itm_heraldicbannert3','itm_trophy_b','itm_leather_gloves1'],def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1,vaegir_face_old_2],
    ["todos_cuerno", "Hornman", "Hornmen",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_leather_shoes','itm_ankleboots','itm_cheap_shoes','itm_plaincloakbeige','itm_plaincloakred','itm_plaincloakbrown','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_horn1','itm_trophy_a','itm_stones1','itm_knisxclearvert3'] + items_shields['common'][0]['light'],def_attrib2|level(15),wp(115),knows_warrior_normal,vaegir_face_young_1,vaegir_face_old_2],
    ["saxon_sacerdote", "Cleric Seaxe", "Clerics Seaxna",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_noble_shoesorange','itm_shoes1','itm_noble_shoesorange','itm_noble_shoesblue','itm_shoes1blue','itm_monk_robe','itm_blackwht_robe','itm_stones1','itm_staff1'],def_attrib|level(23),wp(170),knows_cleric,sac_face_1,sac_face_2],

    ["saxon_skirmishert3", "Geneata Seaxe (Med. I.)", "Geneatas Seaxna"] +
    troop_properties(1, 'infantry', 'saxon', items_saxon_skirmisher3, shields=items_shields['saxon'][0]['normal']) +
    [vaegir_face_young_1, vaegir_face_old_2],

    ["saxon_infantryt3", "Geoguth Seaxe (Med. I.)", "Geoguthas Seaxna"] +
    troop_properties(2, 'infantry', 'saxon', items_saxon_infantryt3) +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["saxon_skirmishert4", "Beadu rinc Seaxe (Med. I.)", "Beadu rincas Seaxna"] +
    troop_properties(2, 'infantry', 'saxon', items_saxon_skirmisher4, shields=items_shields['saxon'][1]['normal']) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["saxon_horseman1", "Gesith Seaxe (Lig. C.)", "Gesithas Seaxna"] +
    troop_properties(3, 'cavalry', 'saxon', items_saxon_horseman1, shields=items_shields['saxon'][1]['normal']) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["saxon_skirmishert5", "Ridwiga Seaxe (Hv. I.)", "Ridwigas Seaxna"] +
    troop_properties(4, 'infantry', 'saxon', items_saxon_skirmisher5) +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["saxon_infantryt4", "Duguth Seaxe (Hv. I.)", "Duguthas Seaxna"] +
    troop_properties(3, 'infantry', 'saxon', items_saxon_infantryt4) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["saxon_infantryt5", "Hearthweru Seaxe (Elit. I.)", "Hearthweruas Seaxna"] +
    troop_properties(4, 'infantry', 'saxon', items_saxon_infantryt5) +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["saxon_messenger", "Horsweala Seaxe", "Horswealas Seaxna"] +
    troop_properties(3, 'messenger', 'saxon', items_saxon_messenger) +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["saxon_deserter", "Deserter Seaxe", "Deserters Seaxna"] +
    troop_properties(2, 'infantry', 'saxon', items_saxon_deserter, faction='fac_deserters') +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["saxon_prison_guard", "Prison Guard", "Prison Guards"] +
    troop_properties(3, 'infantry', 'saxon', items_saxon_guard, shields=[items_shields['saxon'][1]['normal'][0]]) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["saxon_castle_guard", "Castle Guard", "Castle Guards"] +
    troop_properties(3, 'infantry', 'saxon', items_saxon_guard, shields=[items_shields['saxon'][1]['normal'][0]]) +
    [vaegir_face_middle_1, vaegir_face_older_2],
]

items_jute_recruit = ['itm_maul1h_blunt','itm_stones1','itm_slingrocks','itm_basic_sling','itm_ankleboots','itm_cheap_shoes','itm_woolencap_newblu','itm_woolencap_newblk','itm_woolencap','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_briton_tunic2','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic1','itm_thick_body','itm_knifechp','itm_staff_pitchfork','itm_clubcudgel','itm_spear_sharppitchfork','itm_staff1','itm_sickle']
items_jute_footman = ['itm_maul1h_blunt','itm_axe3','itm_javelins','itm_slingrocks','itm_basic_sling','itm_fustibalus','itm_ankleboots','itm_cheap_shoes','itm_woolencap_newblu','itm_woolencap_newblk','itm_woolencap','itm_plaincloakltblue','itm_plaincloakred','itm_plaincloakbeige','itm_plaincloakbrown','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_merch_furjacketblue','itm_merch_furjacketyelo','itm_merch_furjacketyelo','itm_club3','itm_seaxt4']
items_jute_infantry3 = ['itm_shoes1','itm_shoes1green','itm_shoes1orange','itm_woolencap_newblu','itm_woolencap_newgrn','itm_ptunic13','itm_ptunic13','itm_ptunic14','itm_rawhide_vest_green','itm_rawhide_coat9grey','itm_rawhide_vest_blue','itm_rawhide_coat2','itm_rawhide_coat3','itm_germanlongspeart2','itm_saxon_medium_speart2','itm_saxonsword1']
items_jute_archer = ['itm_arrows1','itm_shortbow','itm_huntingbow','itm_shoes2bare','itm_ankleboots','itm_cheap_shoes','itm_woolencap_newblk','itm_woolencap_newblk','itm_woolencap','itm_ptunic3','itm_ptunicwhite','itm_ptunic11','itm_briton_tunic2','itm_peasant_ftunic','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_clubcudgel','itm_seaxt3','itm_axe_britonbattlet2']
items_jute_skirmisher3 = ['itm_shoes2grey','itm_shoes1green','itm_shoes1orange','itm_woolencap_newblk','itm_woolencap','itm_rawhide_coat7green','itm_rawhide_vest_red','itm_pelt_coat2','itm_germanlongspeart2','itm_saxon_medium_speart2','itm_saxonsword1']
items_jute_skirmisher4 = ['itm_angons','itm_angonst2','itm_shoes2grey','itm_shoes1green','itm_shoes1orange','itm_plaincloakbeige','itm_plaincloakbrown','itm_cloak_boar_furcap','itm_jack_armorpaddedred','itm_jack_armorfadedblue','itm_vae_thickcoat2','itm_vae_thickcoat3','itm_jack_armorgreen','itm_jack_armorgreen','itm_rathos_bowlhelmet','itm_bowlhelmet','itm_leather_helm_tan','itm_hornhelmet3_t2','itm_spangenhelmblight','itm_dena_helmboar2','itm_saxon_medium_speart2','itm_talak_seaxkni','itm_maul1h_blunt','itm_ironhammerlong']
items_jute_horseman = ['itm_angleswordt2','itm_javelins','itm_horsecourser2','itm_roman_horse1','itm_spanish_horset2','itm_frankishhorsecharger','itm_roman_horse2','itm_frankishhorse1','itm_pictish_stallion','itm_leather_gloves1','itm_greaves1','itm_noble_shoesorange','itm_jack_armorgreen','itm_jack_armorfadedblue','itm_jack_armorfadedblue','itm_jack_armorpaddedred','itm_lorica_pink','itm_noblearmor14res','itm_mailnoble_ltbrwnclk','itm_lorica_greyrd','itm_frisian_helm3t2','itm_frisian_helm1','itm_dena_elite_helm1boar','itm_jutehelmt3','itm_hornhelmet3_t2','itm_jutehelmt3','itm_ironhammerlong','itm_spearlong']
items_jute_skirmisher5 = ['itm_throwing_axes','itm_angonst2','itm_leather_gloves1','itm_shoes2green','itm_shoes2grey','itm_greaves1','itm_lorica_eggwht','itm_lorica_ltblue','itm_noblearmor15res','itm_lorica_white','itm_lorica_whitegry','itm_frisian_helm3t2','itm_dena_elite_helm1boar','itm_dena_helmboar5','itm_frisian_helm3t2','itm_dena_helmboar2','itm_leather_helm_grey','itm_khergit_cavalry_helmet','itm_axe_longfrankisht3','itm_decor_axet3','itm_richsword2','itm_saxondenaswordt3','itm_briton_richswordt2']
items_jute_infantryt4 = ['itm_throwing_axes','itm_angonst2','itm_leather_gloves1','itm_shoes2grey','itm_greaves1','itm_noble_shoesorange','itm_leather_captainhelm','itm_leathercap1','itm_hornhelmet2','itm_skullcap_reinforcedt2','itm_lorica_whitbrn','itm_mailshirt_yellow','itm_mailshirt_orange','itm_noblearmor6res','itm_bamburghsword2t2','itm_spear_hvy']
items_jute_infantryt5 = ['itm_angonst2','itm_throwing_axes','itm_leather_gloves1','itm_light_leather_boots','itm_shoes2green','itm_greaves_blue','itm_leather_bootstall','itm_splinted_leather_greaves','itm_lamellar2yellow','itm_lamellarbrown','itm_lamellargrey','itm_mail_wolf_coat1','itm_wolfpelt_mail_coat','itm_mailtunic_brownclk','itm_mailtunic_blk','itm_hornhelmet1','itm_dena_elite_helm2boar','itm_dena_elite_helm2boar','itm_dena_elite_helm2boar','itm_dena_elite_helm2boar','itm_dena_elite_helm1boar','itm_frisian_helm3t2','itm_dena_helmboar2','itm_spear_hvy','itm_maul1h_blunt','itm_richsword2','itm_saxondenaswordt3']
items_jute_messenger = ['itm_javelins','itm_roman_horse1','itm_leather_gloves1','itm_noble_shoesorange','itm_shoes1','itm_noble_shoesorange','itm_noble_shoesblue','itm_shoes1blue','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_spear1','itm_spearlight','itm_langseaxt2']
items_jute_deserter = ['itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_shoes1','itm_shoes1blue','itm_shoes2grey','itm_shoes1green','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_woolencap_newblu','itm_woolencap_red','itm_woolencap_newblk','itm_woolencap','itm_bowlhelmet','itm_hornhelmet2','itm_strawcap','itm_axe_longfrankisht3','itm_saxon_medium_speart2','itm_spearlight','itm_langseaxt2','itm_knisxclearvert3','itm_spearlight']
items_jute_guard = ['itm_angons','itm_leather_gloves1','itm_noble_shoesorange','itm_woolencap_newblu','itm_woolencap_red','itm_leather_captainhelm','itm_leathercap1','itm_bowlhelmet','itm_noblemanshirt1','itm_noblemanshirt2','itm_rawhide_vest_red','itm_jack_armorfadedblue','itm_spear_hasta','itm_langseaxt2']

jute_troops = [
    ["jute_recruit", "Gebur Jute (Lig. I.)", "Geburas Jutes"] +
    troop_properties(0, 'infantry', 'jute', items_jute_recruit) +
    [vaegir_face_younger_1, vaegir_face_middle_2],

    ["jute_footmant2", "Kotsetla Jute (Lig. I.)", "Kotsetlas Jutes"] +
    troop_properties(1, 'infantry', 'jute', items_jute_footman) +
    [vaegir_face_young_1, vaegir_face_middle_2],

    ["jute_archert1", "Sceotand Seaxe (Missile)", "Sceotandas Seaxna"] +
    troop_properties(0, 'archer', 'jute', items_jute_archer) +
    [vaegir_face_young_1, vaegir_face_middle_2],

    ["jute_skirmishert3", "Geneata Jute (Med. I.)", "Geneatas Jutes"] +
    troop_properties(2, 'infantry', 'jute', items_jute_skirmisher3) +
    [vaegir_face_young_1, vaegir_face_old_2],

    ["jute_portaestandarte","Tacnberend","Tacnberend",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_shoes2grey','itm_shoes2grey','itm_shoes1green','itm_shoes1orange','itm_plaincloakbrown','itm_plaincloakltblue','itm_plaincloakred','itm_plaincloakltblue','itm_plaincloakbeige','itm_ptunic3','itm_ptunicwhite','itm_wessex_tunic3','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_goatcap1','itm_goat_capbrn','itm_boar_helmet','itm_spearbanner5','itm_heraldicbannert3','itm_trophy_b'],def_attrib2|level(23),wp_one_handed(170)|wp_polearm(125)|wp(80),knows_warrior_normal,vaegir_face_young_1,vaegir_face_old_2],
    ["jute_cleric","Jute Cleric","Jutes Clerics",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_shoes1green','itm_shoes1orange','itm_shoes1orange','itm_monk_robe','itm_blackwht_robe','itm_stones1','itm_staff1'],def_attrib|level(23),wp(170),knows_cleric,sac_face_1,sac_face_2],

    ["jute_infantryt3", "Geoguth Jute (Med. I.)", "Geoguthas Jutes"] +
    troop_properties(2, 'infantry', 'jute', items_jute_infantry3) +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["jute_skirmishert4", "Beadu rinc Jute (Med. I.)", "Beadu rincas Jutes"] +
    troop_properties(3, 'infantry', 'jute', items_jute_skirmisher4, shields=items_shields['jute'][1]['normal']) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["jute_horsemant4", "Gesith Jute (Lig. C.)", "Gesithas Jutes"] +
    troop_properties(3, 'cavalry', 'saxon', items_jute_horseman) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["jute_skirmishert5", "Ridwiga Jute (Hv. I.)", "Ridwigas Jutes"] +
    troop_properties(4, 'infantry', 'jute', items_jute_skirmisher5) +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["jute_infantryt4", "Duguth Jute (Hv. I.)", "Duguthas Jutes"] +
    troop_properties(3, 'infantry', 'jute', items_jute_infantryt4) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["jute_infantryelitet5", "Hearthweru Jute (Elit. I.)", "Hearthweruas Jutes"] +
    troop_properties(4, 'infantry', 'jute', items_jute_infantryt5) +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["jute_messenger", "Horsweala Jute", "Horswealas Jutes"] +
    troop_properties(3, 'messenger', 'jute', items_jute_messenger) +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["jute_deserter", "Jute Deserter", "Jutes Deserters"] +
    troop_properties(2, 'infantry', 'jute', items_jute_deserter, faction='fac_deserters') +
    [vaegir_face_young_1, vaegir_face_older_2],

    ["jute_prison_guard", "Prison Guard", "Prison Guards"] +
    troop_properties(3, 'infantry', 'jute', items_jute_guard, shields=[items_shields['jute'][0]['normal'][1]]) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["jute_castle_guard", "Castle Guard", "Castle Guards"] +
    troop_properties(3, 'infantry', 'jute', items_jute_guard, shields=[items_shields['jute'][0]['normal'][1]]) +
    [vaegir_face_middle_1, vaegir_face_older_2],
]


# todo: apart from items and faces, the troops are the same as jute. Therefore there is a symmetry to be explored here.
items_engle_recruit = ['itm_stones1','itm_slingrocks','itm_basic_sling','itm_ankleboots','itm_cheap_shoes','itm_woolencap_red','itm_woolencap_newgrn','itm_woolencap_newblk','itm_woolencap','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_briton_tunic2','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic1','itm_thick_body','itm_knifechp','itm_staff_pitchfork','itm_spear_sharppitchfork','itm_quarter_staff','itm_sickle','itm_axe1']
items_engle_footman = ['itm_javelins','itm_slingrocks','itm_basic_sling','itm_fustibalus','itm_ankleboots','itm_cheap_shoes','itm_woolencap_newblu','itm_woolencap_newgrn','itm_plaincloakltblue','itm_plaincloakbeige','itm_plaincloakbrown','itm_ptunic3','itm_wessex_tunic3','itm_mercia_tunicgrn','itm_peasant_ftunic','itm_leather_tunic1','itm_merch_furjacketwhite','itm_merch_furjacket2t3','itm_merch_furjacketyelo','itm_club3','itm_clubcudgel','itm_axe3']
items_engle_infantry3 = ['itm_javelins','itm_shoes1green','itm_shoes1blue','itm_shoes1orange','itm_rawhide_vest_green','itm_rawhide_coat9grey','itm_rawhide_vest_blue','itm_rawhide_coat2','itm_rawhide_coat2','itm_spear1','itm_spearlight','itm_langseaxt2']
items_engle_archer = ['itm_arrows1','itm_shortbow','itm_huntingbow','itm_ankleboots','itm_cheap_shoes','itm_peasant_ftunic','itm_ptunicwhite','itm_ptunic12','itm_briton_tunic2','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic1','itm_clubcudgel','itm_seaxt3','itm_axe2']
items_engle_skirmisher3 = ['itm_javelins','itm_javelins','itm_shoes1','itm_shoes1','itm_shoes1green','itm_shoes1orange','itm_rawhide_coat7green','itm_rawhide_vest_red','itm_pelt_coat2','itm_merch_furjacketyelo','itm_merch_furjacketyelo','itm_germanic_axelongt2','itm_saxon_medium_speart2','itm_spearlight','itm_langseaxt2','itm_knisxclearvert3','itm_spearlight']
items_engle_skirmisher4 = ['itm_angons','itm_javelins','itm_angonst2','itm_shoes1blue','itm_shoes2grey','itm_plaincloakltblue','itm_plaincloakbrown','itm_cloak_boar_furcap','itm_jack_armorpaddedred','itm_jack_armorfadedblue','itm_vae_thickcoat2','itm_vae_thickcoat3','itm_jack_armorgreen','itm_rathos_bowlhelmet','itm_bowlhelmet','itm_leather_helm_tan','itm_hornhelmet3_t2','itm_khergit_cavalry_helmet','itm_seaxt3','itm_saxon_axet2','itm_axe_englet2','itm_spear_hasta','itm_germanic_axelongt2']
items_engle_horseman = ['itm_javelins','itm_javelins','itm_roman_horse1','itm_spanish_horset2','itm_frankishhorsecharger','itm_horsecourser1','itm_horsecourser2','itm_drafthorse1','itm_noble_shoesorange','itm_noble_shoesblue','itm_shoes1blue','itm_jack_armorgreen','itm_jack_armorfadedblue','itm_lorica_pink','itm_noblearmor14res','itm_mailnoble_ltbrwnclk','itm_lorica_greyrd','itm_mierce_helmt3','itm_briton_helm','itm_briton_helmengravedt2','itm_dena_elite_helm1boar','itm_dena_elite_helm2boar','itm_angloblackbrownhelm','itm_hornhelmet1','itm_hornhelmet3_t2','itm_angleswordt2','itm_spearlong','itm_spearwarlong']
items_engle_skirmisher5 = ['itm_angons','itm_angonst2','itm_leather_gloves1','itm_shoes2green','itm_greaves1','itm_lorica_ltblue','itm_lorica_white','itm_noblearmor16res','itm_lorica_whitegry','itm_lorica_yelo','itm_hornhelmet1','itm_hornhelmet2','itm_saxon_helmt2','itm_saxonhelmnoblet4','itm_briton_helmtrimt2','itm_briton_helm_3','itm_dena_elite_helm1boar','itm_dena_helmboar2','itm_seaxt4','itm_angleswordt2','itm_jute_richsword','itm_saxonswordt2','itm_germanicswordt2']
items_engle_infantryt4 = ['itm_angons','itm_angonst2','itm_noble_shoesblue','itm_shoes1blue','itm_greaves1','itm_lorica_whitbrn','itm_mailshirt_yellow','itm_noblearmor6res','itm_leather_captainhelm','itm_rathos_bowlhelmet','itm_leathercap1','itm_skullcap_reinforcedt2','itm_spear_hvy','itm_bamburghsword2t2','itm_langseaxt2']
items_engle_infantryt5 = ['itm_angons','itm_angonst2','itm_leather_gloves1','itm_greaves_blue','itm_shoes2green','itm_splinted_leather_greaves','itm_mailtunic_greycheap','itm_mailnoble_redclk1','itm_mailnoble_greenclk','itm_mailtunic_brownclk','itm_mailtunic_blk','itm_mailtunic_brownclk','itm_mailtunic_grey','itm_mierce_helmt3','itm_briton_helm','itm_briton_helmslvtrimt3','itm_dena_helmboar5','itm_angloblackbrownhelm','itm_dena_elite_helm2boar','itm_briton_helmtrimt2','itm_bronze_warlord_helmetboar','itm_spear_hvy','itm_ornate_seaxt3','itm_angle_swordt3','itm_angleswordt2','itm_germanicswordt2']
items_engle_messenger = ['itm_leather_gloves1','itm_horsecourser2','itm_noble_shoesorange','itm_shoes1','itm_noble_shoesorange','itm_shoes2green','itm_noble_shoesorange','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_spear1','itm_spearlight','itm_langseaxt2']
items_engle_deserter = ['itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_shoes2grey','itm_shoes2grey','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_woolencap_newblu','itm_woolencap_red','itm_woolencap_newblk','itm_woolencap','itm_bowlhelmet','itm_hornhelmet2','itm_strawcap','itm_skullcap_reinforcedt2','itm_germanic_axelongt2','itm_saxon_medium_speart2','itm_spearlight','itm_spearboar','itm_langseaxt2','itm_knisxclearvert3','itm_spearlight']
items_engle_guard = ['itm_angons','itm_leather_gloves1','itm_noble_shoesorange','itm_noblemanshirt3','itm_linen_coatbrown','itm_linen_coatblue','itm_woolencap_red','itm_leather_captainhelm','itm_skullcap_reinforcedt2','itm_spear_hvy','itm_langseaxt2']


engle_troops = [
    ["engle_recruit", "Gebur Engle (Lig. I.)", "Geburas Engles"] +
    troop_properties(0, 'infantry', 'engle', items_engle_recruit) +
    [nord_face_younger_1, nord_face_middle_2],

    ["engle_footmant2", "Kotsetla Engle (Lig. I.)", "Kotsetlas Engles"] +
    troop_properties(1, 'infantry', 'engle', items_engle_footman) +
    [nord_face_young_1, nord_face_middle_2],

    ["engle_archer", "Sceotand Seaxe (Missile)", "Sceotandas Seaxna"] +
    troop_properties(0, 'archer', 'engle', items_engle_archer) +
    [nord_face_young_1, nord_face_middle_2],

    ["engle_skirmishert3", "Geneata Engle (Med. I.)", "Geneatas Engles"] +
    troop_properties(2, 'infantry', 'engle', items_engle_skirmisher3) +
    [nord_face_young_1, nord_face_old_2],

    ["engle_bannerman","Tacnberend","Tacnberend",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_shoes2grey','itm_shoes1green','itm_shoes1orange','itm_shoes1orange','itm_plaincloakbeige','itm_plaincloakltblue','itm_plaincloakred','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_goatcap1','itm_goat_capbrn','itm_boar_helmet','itm_goat_miercehelmt3','itm_cavalrybannert2','itm_heraldicbannert3','itm_spearbannert2','itm_trophy_b','itm_leather_gloves1','itm_helm_leathert2'],def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1,vaegir_face_old_2],
    ["engle_rxpriest","Cleric Engle","Cleric Engles",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_noble_shoesorange','itm_shoes1','itm_noble_shoesorange','itm_noble_shoesblue','itm_shoes1blue','itm_monk_robe','itm_blackwht_robe','itm_stones1','itm_staff1'],def_attrib|level(23),wp(165),knows_cleric,sac_face_1,sac_face_2],

    ["engle_infantryt3", "Geoguth Engle (Med. I.)", "Geoguthas Engles"] +
    troop_properties(2, 'infantry', 'engle', items_engle_infantry3) +
    [nord_face_young_1, nord_face_older_2],

    ["engle_skirmishert4", "Beadu rinc Engle (Med. I.)", "Beadu rincas Engles"] +
    troop_properties(3, 'infantry', 'engle', items_engle_skirmisher4, shields=items_shields['engle'][1]['normal']) +
    [nord_face_middle_1, nord_face_older_2],

    ["engle_horseman", "Gesith Engle (Lig. C.)", "Gesithas Engles"] +
    troop_properties(3, 'cavalry', 'saxon', items_engle_horseman) +
    [nord_face_middle_1, nord_face_older_2],

    ["engle_skirmishert5", "Ridwiga Engle (Hv. I.)", "Ridwigas Engles"] +
    troop_properties(4, 'infantry', 'engle', items_engle_skirmisher5) +
    [nord_face_young_1, nord_face_older_2],

    ["engle_infantryt4", "Duguth Engle (Hv. I.)", "Duguthas Engles"] +
    troop_properties(3, 'infantry', 'engle', items_engle_infantryt4) +
    [nord_face_middle_1, nord_face_older_2],

    ["engle_infantryt5", "Hearthweru Engle (Elit. I.)", "Hearthweruas Engles"] +
    troop_properties(4, 'infantry', 'engle', items_engle_infantryt5) +
    [nord_face_young_1, nord_face_older_2],

    ["engle_messenger", "Horsweala Engle", "Horswealas Engles"] +
    troop_properties(3, 'messenger', 'engle', items_engle_messenger) +
    [nord_face_young_1, nord_face_older_2],

    ["engle_deserter", "Engle Deserter", "Engles Deserters"] +
    troop_properties(2, 'infantry', 'engle', items_engle_deserter, faction='fac_deserters') +
    [nord_face_young_1, nord_face_older_2],

    ["engle_prison_guard", "Prison Guard", "Prison Guards"] +
    troop_properties(3, 'infantry', 'engle', items_engle_guard, shields=[items_shields['engle'][1]['heavy'][1]]) +
    [nord_face_middle_1,nord_face_older_2],

    ["engle_castle_guard", "Castle Guard", "Castle Guards"] +
    troop_properties(3, 'infantry', 'engle', items_engle_guard, shields=[items_shields['engle'][1]['heavy'][1]]) +
    [nord_face_middle_1,nord_face_older_2],
]


items_briton_recruit = ['itm_stones1','itm_slingrocks','itm_basic_sling','itm_leather_shoes','itm_shoes2bare','itm_shoes2bare','itm_hoodnewblk','itm_common_hood','itm_ptunic3','itm_ptunicwhite','itm_ptunic1','itm_briton_tunic2','itm_ptunic2','itm_ptunic3','itm_ptunic3','itm_shirtblue','itm_knifechp','itm_staff_pitchfork','itm_clubcudgel','itm_spear_sharppitchfork','itm_clubsmooth','itm_sickle']
items_briton_footman = ['itm_wooden_javelins','itm_wooden_javelins','itm_slingrocks','itm_basic_sling','itm_fustibalus','itm_shoes2bare','itm_shoes2bare','itm_hoodnewblu','itm_hoodnewblk','itm_hoodnewwht','itm_blackhood','itm_black_cloak','itm_woven_cloak','itm_tunicblue8','itm_ptunic9','itm_ptunic5','itm_german_tunica','itm_ptunic3','itm_peasant_ftunic','itm_peasant_archertunic','itm_farmertunic26','itm_spikedclub','itm_clubsmooth','itm_axe2','itm_spear_britonshortt2']
items_briton_infantry3 = ['itm_javelins','itm_shoes1blue','itm_shoes2grey','itm_shoes1green','itm_plaincloakltblue','itm_plaincloakred','itm_plaincloakbeige','itm_plaincloakbrown','itm_linen_coatwcloak','itm_goatist_tuniccoat','itm_linen_coatblue','itm_spear_britonmedt2','itm_spear_britonlight','itm_knife1','itm_scianshswordt1']
items_briton_infantry4 = ['itm_throwing_spear','itm_noble_shoesblue','itm_shoes2green','itm_shoes2grey','itm_shoes1','itm_mailbyrniegrey','itm_mailbyrniewhitered','itm_mailbyrnieblue','itm_mail_sleevelessbrn','itm_noblearmor7res','itm_mailbyrnie_longfurred','itm_mailcuir_bouilli','itm_mail_largering','itm_linen_coatblue','itm_spear_blade2t2','itm_spear_blade2t2','itm_knife1','itm_britonswordt2','itm_arming_cap','itm_roman_helmlate']
items_briton_infantry5 = ['itm_throwing_spear','itm_leather_gloves1','itm_greaves_blue','itm_greaves_blue','itm_greaves1','itm_noblearmor12res','itm_mailtunic_blk','itm_lorica_stripedred','itm_spangenhelmalight','itm_romanelitehelmt3','itm_spangenhelmb1','itm_briton_helmengravedt2','itm_briton_helm_3','itm_briton_helmslvtrimt3','itm_roman_helmlatet2','itm_spear_blade2t2','itm_bamburghsword2t2','itm_britonswordt2','itm_bamburghsword2t2']
items_briton_archer = ['itm_arrows1','itm_shortbow','itm_huntingbow','itm_leather_shoes','itm_shoes2bare','itm_shoes2bare','itm_hoodnewblu','itm_hoodnewblk','itm_hoodnewwht','itm_blackhood','itm_ptunic3','itm_ptunicwhite','itm_tunicblue8','itm_ptunic9','itm_ptunic3','itm_ptunic5','itm_german_tunica','itm_ptunic3','itm_peasant_etunic','itm_farmertunic26','itm_club_stick','itm_axe2','itm_clubcudgel']
items_briton_longbowman = ['itm_arrows1','itm_longbow','itm_shoes1green','itm_shoes1blue','itm_shoes1blue','itm_shoes2grey','itm_hoodnewwht','itm_blackhood','itm_head_wrappings','itm_common_hood','itm_ptunic3','itm_ptunic12','itm_shirtblue','itm_ptunic3','itm_shirtylw','itm_shirtaqua','itm_shirtgrey','itm_bltunicgrn','itm_peasant_archertunic','itm_farmertunic26','itm_scianshswordbone','itm_scianshswordt1','itm_axe2','itm_axe4']
items_briton_horseman = ['itm_cavaljavelins','itm_gallic_horse1','itm_pictish_mare','itm_roman_horse2','itm_saddle_horse1','itm_roman_horse1','itm_roman_horse1','itm_noble_shoesorange','itm_noble_shoesorange','itm_ankleboots','itm_linen_coatbrown','itm_linen_coattan','itm_scale_bronze_armor','itm_scale_brown_armor','itm_mailbyrniegreen','itm_mailbyrnieyelo','itm_rathos_bowlhelmet','itm_briton_helm','itm_leather_captainhelm','itm_leather_helm_grey','itm_spangenhelma_yellow','itm_spear_briton_longt2','itm_britonswordt2']
items_briton_cavalry = ['itm_javelins','itm_horsecourser1','itm_horsecourser2','itm_drafthorse3t2','itm_frankishhorsechargert3','itm_drafthorse1','itm_frankishhorset2','itm_frankishhorset2','itm_leather_gloves1','itm_shoes2green','itm_shoes2green','itm_greaves1','itm_splinted_leather_greaves','itm_mail_furredt2','itm_mailtunic_blk','itm_noblearmor12res','itm_scaleorangeblkbands','itm_mailbyrniered','itm_scale_bronze_armor','itm_mail_goatist','itm_briton_helm','itm_dux_ridgehelm','itm_leatherneck_helm','itm_spangenhelma_ornate','itm_mierce_helmt3','itm_briton_helmtrimt2','itm_spangenhelmgerm_trim','itm_roman_helmlatet2','itm_spear_briton_longt2','itm_britonswordt2','itm_rich_spathaswordt2']
items_briton_skirmt3 = ['itm_cavaljavelins','itm_cavaljavelins','itm_shoes1','itm_shoes2grey','itm_shoes1green','itm_black_cloak','itm_woven_cloak','itm_plaincloakbrown','itm_vae_thickcoat2','itm_vae_thickcoat3','itm_helm_leathert2','itm_skullcap_reinforcedt1','itm_strawcap','itm_skullcap_reinforcedt2','itm_blackened_axet2','itm_spear_britonshortt2','itm_scianshswordt1']
items_briton_skirmishert4 = ['itm_throwing_spear','itm_throwing_spear','itm_leather_gloves1','itm_noble_shoesorange','itm_noble_shoesblue','itm_shoes1blue','itm_scale_white_armor','itm_mail_sleevelessbrn','itm_mail_furredt2','itm_mailtunic_blk','itm_lorica_stripedblue','itm_spangenhelmalight','itm_spangenhelmblight','itm_briton_helm','itm_rathos_bowlhelmet','itm_arming_cap','itm_roman_helmlate','itm_spear_blade2t2','itm_spear_blade2t2','itm_saxonswordt2','itm_lang_knifet2','itm_noble_shswordt2']
items_briton_messenger = ['itm_leather_gloves1','itm_leather_gloves1','itm_javelins','itm_horsecourser1','itm_noble_shoesorange','itm_shoes1','itm_noble_shoesorange','itm_ptunic3','itm_ptunicwhite','itm_shirtblue','itm_ptunic3','itm_ptunic3','itm_shirtylw','itm_shirtaqua','itm_shirtgrey','itm_bltunicgrn','itm_spear_briton_longt2','itm_spear_briton_longt2','itm_sciansword','itm_scianswordbone','itm_longspeart3','itm_lang_knifet2','itm_knife1']
items_briton_deserter = ['itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_shoes1','itm_shoes1','itm_shoes1green','itm_ptunicwhite','itm_shirtblue','itm_ptunic3','itm_shirtgrey','itm_bltunicgrn','itm_ptunic3','itm_ptunic3','itm_shirtylw','itm_bltunicgrn','itm_leathercap1','itm_skullcap_reinforcedt1','itm_strawcap','itm_skullcap_reinforcedt2','itm_skullcapt1','itm_spear_britonmedt2','itm_spear_britonlight','itm_spear_hasta','itm_langseaxt2','itm_scianshswordt1']
items_briton_guards = ['itm_throwing_spear','itm_leather_gloves1','itm_greaves1','itm_ptunic3','itm_bltunic10','itm_mailtunic_blk','itm_lorica_stripedblue','itm_spangenhelmblight','itm_spangenhelmalight','itm_spear_blade2t2','itm_scianshswordt1']


briton_troops = [
    ["briton_recruit", "Aillt (Lig. I.)", "Aillts"] +
    troop_properties(0, 'infantry', 'briton', items_briton_recruit) +
    [swadian_face_younger_1, swadian_face_middle_2],

    ["briton_footmant2", "Bonheddwr (Lig. I.)", "Bonheddwyr"] +
    troop_properties(1, 'infantry', 'briton', items_briton_footman) +
    [swadian_face_young_1, swadian_face_old_2],

    ["briton_infantryt3", "Pedyt (Med. I.)", "Pedytes"] +
    troop_properties(2, 'infantry', 'briton', items_briton_infantry3) +
    [swadian_face_young_1, swadian_face_old_2],

    ["briton_infantryt4", "Uchelwr (Hv. I.)", "Uchelwyr"] +
    troop_properties(3, 'infantry', 'briton', items_briton_infantry4) +
    [swadian_face_young_1, swadian_face_old_2],

    ["briton_troopelite", "Campgwr (Elit. I.)", "Campgwyr"] +
    troop_properties(4, 'infantry', 'briton', items_briton_infantry5) +
    [swadian_face_middle_1, swadian_face_older_2],

    ["briton_archer", "Bweydd (Missile)", "Bweydds"] +
    troop_properties(0, 'archer', 'briton', items_briton_archer) +
    [swadian_face_young_1, swadian_face_middle_2],

    ["briton_longbowman", "Saethydd (Missile)", "Saethydds"] +
    troop_properties(2, 'archer', 'briton', items_briton_longbowman) +
    [swadian_face_middle_1, swadian_face_older_2],

    ["briton_horseman", "Marchoc (Lig. C.)", "Marcach"] +
    troop_properties(3, 'cavalry', 'briton', items_briton_horseman, shields=items_shields['briton'][1]['heavy']) +
    [swadian_face_young_1, swadian_face_old_2],

    ["briton_cavalry", "Teulu (Elit. C.)", "Teulus"] +
    troop_properties(4, 'cavalry', 'briton', items_briton_cavalry) +
    [swadian_face_middle_1, swadian_face_older_2],

    ["briton_skirmt3", "Gwrda (Skrm.)", "Gwrdas"] +
    troop_properties(2, 'infantry', 'briton', items_briton_skirmt3) +
    [swadian_face_young_1, swadian_face_old_2],

    ["briton_skirmishert4", "Cadwr (Hv. I.)", "Cadwyr"] +
    troop_properties(3, 'infantry', 'briton', items_briton_skirmishert4) +
    [swadian_face_young_1, swadian_face_old_2],

    ["briton_bannerman", "Gwas Ys Tafell", "Gwas Ys Tafell", tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_shoes1blue','itm_shoes2grey','itm_shoes2grey','itm_shoes1green','itm_plaincloakbeige','itm_plaincloakbrown','itm_ptunic3','itm_ptunicwhite','itm_shirtblue','itm_ptunic3','itm_shirtylw','itm_shirtaqua','itm_shirtgrey','itm_bltunicgrn','itm_ptunic11','itm_peasant_ftunic','itm_wessexbanner9','itm_spearbanner4','itm_heraldicbannert3','itm_trophy_b','itm_bluepantsbody_woad05','itm_cloaked_tunic1','itm_jack_armorfadedblue','itm_noblearmor22res','itm_leather_gloves1','itm_helm_leathert2'],def_attrib2|level(23),wp(165),knows_warrior_normal,swadian_face_young_1,swadian_face_old_2],
    ["briton_sacerdote", "Briton Cleric", "Britons Clerics", tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_monk_robe','itm_robe_darkprp','itm_stones1','itm_staff1'],def_attrib|level(23),wp(165),knows_cleric,sac_face_1,sac_face_2],

    ["briton_messenger", "Briton Messenger", "Britons Messengers"] +
    troop_properties(3, 'messenger', 'briton', items_briton_messenger) +
    [swadian_face_young_1, swadian_face_old_2],

    ["briton_deserter", "Briton Deserter", "Britons Deserters"] +
    troop_properties(2, 'infantry', 'briton', items_briton_deserter, shields=items_shields['briton'][2]['heavy'],
                     faction='fac_deserters') +
    [swadian_face_young_1, swadian_face_old_2],

    ["briton_prisoner_guard", "Prison Guard", "Prison Guards"] +
    troop_properties(3, 'infantry', 'briton', items_saxon_guard, shields=[items_shields['briton'][1]['heavy'][0]]) +
    [swadian_face_middle_1, swadian_face_older_2],

    ["briton_castle_guard", "Castle Guard", "Castle Guards"] +
    troop_properties(3, 'infantry', 'briton', items_saxon_guard, shields=[items_shields['briton'][1]['heavy'][0]]) +
    [swadian_face_middle_1, swadian_face_older_2],
]
