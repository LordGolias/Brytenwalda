from header_troops import *
from header_skills import *

from module_items_shields import shields as items_shields
from module_items_horses import horses as items_horses
from module_items_footwear import footwear as items_footwear


_troop_attributes = {
    0: {
        # recruit
        'infantry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor,
            'attrs': def_attrib | level(16),
            'wp': wp(100),
            'skills': knows_warrior_basic,
            'footwear': items_footwear[0]['civilian'],
        },

        # archer
        'archer': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_ranged,
            'attrs': basic_ranged_attrib|level(16),
            'wp': wp_archer(54),
            'skills': knows_warrior_basic | knows_power_draw_2 | knows_power_throw_1,
            'footwear': items_footwear[0]['military'],
         },
    },

    1: {
        # weak infantry (no shield guaranteed)
        'infantry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor,
            'attrs': def_attrib2 | level(20),
            'wp': wp(140),
            'skills': knows_warrior_basic,
            'footwear': items_footwear[0]['military'],
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
            'footwear': items_footwear[1]['military'],
            'shields': [(1, 'heavy')],
        },

        # good archers (attributes)
        'archer': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_ranged,
            'attrs': veteran_ranged_attrib | str_14 | level(24),
            'wp': wp(70) | wp_archery(150),
            'footwear': items_footwear[0]['military'],
            'skills': knows_warrior_normal | knows_power_draw_6,
        },

        # light cavalry (attributes, no helmet)
        'cavalry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield | tf_guarantee_horse | tf_mounted |
                     tf_guarantee_ranged,
            'attrs': def_attrib2 | level(24),
            'wp': wp(180),
            'skills': knows_warrior_normal,
            'footwear': items_footwear[0]['military'],
            'horses': items_horses[0]['normal'],
        }
    },

    3: {
        # strong infantry (all of lvl 2 + helmet, no gloves guaranteed)
        'infantry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield | tf_guarantee_helmet,
            'attrs': def_attrib3 | level(28),
            'wp': wp(220),
            'skills': knows_warrior_veteran,
            'footwear': items_footwear[1]['military'],
            'shields': [(2, 'heavy')]
        },

        # saxon_horseman1
        'cavalry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield | tf_guarantee_helmet |
                     tf_guarantee_gloves | tf_guarantee_ranged | tf_guarantee_horse | tf_mounted,
            'attrs': def_attrib3 | level(28),
            'wp': wp(220),
            'skills': knows_warrior_veteran,
            'footwear': items_footwear[1]['military'],
            'shields': [(1, 'normal')],
            'horses': items_horses[0]['heavy'],
        },

        # saxon_messenger
        'messenger': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_gloves | tf_guarantee_horse | tf_mounted,
            'attrs': def_attrib3|agi_21|level(28),
            'wp': wp(200),
            'skills': knows_common | knows_riding_7 | knows_power_throw_2,
            'footwear': items_footwear[0]['military'],
            'shields': items_shields['banner'][1]['normal'],
            'horses': items_horses[2]['light'],
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
            'footwear': items_footwear[2]['military'],
            'shields': ['itm_shield_banner_heavy_3'],
        },

        # elite cavalry (fully equipped, lvl 3 banner shield)
        'cavalry': {
            'flags': tf_guarantee_boots | tf_guarantee_armor | tf_guarantee_shield | tf_guarantee_helmet |
                     tf_guarantee_gloves | tf_guarantee_horse | tf_mounted,
            'attrs': def_attrib3 | level(32),
            'wp': wp(260),
            'skills': knows_warrior_elite,
            'footwear': items_footwear[1]['military'],
            'shields': items_shields['banner'][3]['normal'],
            'horses': items_horses[1]['heavy'],
        },
    },
}


def troop_properties(lvl, type, culture, other_items, flags=None, skills=None, shields=None, faction=None):
    attrs = _troop_attributes[lvl][type]

    horses = attrs.get('horses', [])
    footwear = attrs['footwear']

    possible_shields = []
    # if troop requires shields
    if shields is None and 'shields' in attrs:
        for shield_prop in attrs['shields']:
            if isinstance(shield_prop, tuple):
                shield_lvl = shield_prop[0]
                shield_type = shield_prop[1]
                possible_shields += items_shields[culture][shield_lvl][shield_type]
            else:
                possible_shields += attrs['shields']
    elif shields is not None:
        possible_shields = shields

    if faction is None:
        faction = 'fac_neutral'
    if flags is None:
        flags = attrs['flags']
    if skills is None:
        skills = attrs['skills']

    return [flags,
            no_scene, reserved, faction,
            other_items + footwear + possible_shields + horses, attrs['attrs'], attrs['wp'],
            skills]


items_pict_recruit = ['itm_stones1','itm_slingrocks','itm_basic_sling','itm_looseblackhood','itm_head_wrappings','itm_ptunic7','itm_farmertunic26','itm_ptunic3','itm_ptunic1','itm_ptunic2','itm_ptunic12','itm_german_tunic2','itm_ptunic3','itm_ptunic2','itm_knifechp','itm_clubcudgel','itm_stones1','itm_clubsmooth','itm_quarter_staff','itm_sickle','itm_club_stick']
items_pict_woman = ['itm_cavaljavelins','itm_cavaljavelins','itm_slingrocks','itm_basic_sling','itm_pictpaintfemale1','itm_pictpaintfemale2','itm_pictpaintfemale3','itm_pictpaintfemale4','itm_pictpaintfemale2','itm_pictpaintfemale2','itm_pictpaintfemale3','itm_pictpaintfemale4','itm_pictpaintfemale3','itm_pictpaintfemale4','itm_pictish_waraxet2','itm_medium_speaript3']
items_pict_archer = ['itm_arrows1','itm_bolts','itm_shortbow','itm_huntingbow','itm_pict_crossbow','itm_hoodnewblu','itm_hoodnewblk','itm_hoodnewwht','itm_ptunic10','itm_tunicsleevelessgreen7','itm_tunicsleevelessgreenred','itm_tunicsleeveless2','itm_tunicsleeveless2','itm_tunicsleeveless2','itm_tunicsleevelessc','itm_tunicsleevelessc','itm_redpantsbody_woad11','itm_bluepantsbody_woadhvy12t2','itm_pictish_waraxet2','itm_clubcudgel','itm_scianshswordt1','itm_scianshswordbone']
items_pict_footman = ['itm_javelins','itm_darts','itm_looseblackhood','itm_head_wrappings','itm_common_hood','itm_ptunic3','itm_tunicsleevelessc','itm_ptunic5','itm_tunicsleeveless2','itm_cloaked_leathertunict2','itm_ptunic7','itm_pictish_waraxet2','itm_medium_speaript3']
items_pict_skirmisher3 = ['itm_cavaljavelins','itm_cavaljavelins','itm_slingrocks','itm_basic_sling','itm_fustibalus','itm_war_paintbody_two','itm_bluepantsbody_woad05','itm_bluepantsbody_woad04','itm_bluepantsbody_woad02t2','itm_celtcloakedbody01','itm_celtcloakedbody02','itm_celtcloakedbody03','itm_picto_paintfat1','itm_war_paintbody4','itm_pelt_coat1','itm_pictish_waraxet2','itm_medium_speaript3','itm_scianshswordbone','itm_scianshswordt1']
items_pict_horsesquire3 = ['itm_javelins','itm_pelt_coat2','itm_bluepantsbody_woad04','itm_greypantsbody_woad01','itm_blackpantsbody_woad10','itm_redpantsbody_woad11','itm_war_paintbody13','itm_war_paintbody4','itm_war_paintbody6','itm_spear_lightgael','itm_warspear_godelict3','itm_twohand_speart3','itm_scianshswordbone','itm_scianshswordt1','itm_sciansword']
items_pict_skirmisher4 = ['itm_javelins','itm_javelins','itm_byrnietunicb','itm_scale_vest_red','itm_linen_coatbrown','itm_skullcap_reinforcedt2','itm_skullcapt1','itm_rathos_bowlhelmet','itm_bowlhelmet','itm_spear_briton2ht3','itm_hunting_spear','itm_warspear_godelict3','itm_twohand_speart3','itm_irish_shsword','itm_scianshswordt1']
items_pict_infantry4 = ['itm_javelins','itm_leather_gloves1','itm_richlong_tunic3','itm_linen_coatwhite','itm_linen_coatblue','itm_mailbyrniered','itm_skullcap_reinforcedt1','itm_skullcap_reinforcedt2','itm_bowl_helmet_nasal','itm_bowlhelmet','itm_irish_shsword','itm_noble_shswordt2','itm_rich_shswordt3','itm_scianshswordbone']
items_pict_infantry5 = ['itm_throwing_spear','itm_leather_gloves1','itm_mailtunic_brownclk','itm_mailtunic_wht','itm_mail_goatist','itm_lorica_brightgreen','itm_lorica_dirtygrn','itm_lorica_whitbrn','itm_scale_vest_red','itm_mailtunic_redbrown','itm_mailtunic_blk','itm_briton_helm','itm_mierce_helmt3','itm_briton_helm_3','itm_szpadelhelm3t2','itm_szpadelhelm4engravedt3','itm_szpadelhelm5engravedt3','itm_pictish_longsword1','itm_gaelicsword1','itm_celtic_sword','itm_scianshswordt1']
items_pict_horseman = ['itm_cavaljavelins','itm_cavaljavelins','itm_bluepantsbody_woad02t2','itm_picto_paintfat2','itm_hide_coat1','itm_hide_coat6','itm_vae_thickcoat3','itm_vae_thickcoat2','itm_vae_thickcoat1','itm_pelt_coat1','itm_pelt_coat2','itm_longspeart3','itm_spear_briton_longt2','itm_scianswordbone','itm_axe2','itm_irish_longsword']
items_pict_noblecavalry = ['itm_cavaljavelins','itm_cavaljavelins','itm_scale_bronze_blueorange','itm_scale_vest_red','itm_lorica_brightgreen','itm_rathos_bowlhelmet','itm_briton_helmslvtrimt3','itm_szpadelhelm2engraved','itm_mierce_helmt3','itm_longspeart3','itm_scianshswordt1','itm_gaelicsword1','itm_irish_longsword']
items_pict_messenger = ['itm_javelins','itm_celtcloakedbody01','itm_celtcloakedbody02','itm_celtcloakedbody03','itm_bluepantsbody_woad04','itm_bluepantsbody_woad04','itm_bluepantsbody_woad05','itm_bluepantsbody_woad04','itm_spear_briton_longt2','itm_scianshswordbone','itm_scianshswordt1','itm_sciansword']
items_pict_deserter = ['itm_cavaljavelins','itm_cavaljavelins','itm_cavaljavelins','itm_tunicsleevelessgreen7','itm_tunicsleeveless2','itm_war_paintbody_two','itm_picto_paintfat2','itm_bluepantsbody_woad02t2','itm_bluepantsbody_woad02t2','itm_greypantsbody_woad01','itm_blackpantsbody_woad10','itm_leather_captainhelm','itm_rathos_bowlhelmet','itm_bowl_helmet_nasal','itm_hunting_spear','itm_warspear_godelict3','itm_twohand_speart3','itm_scianshswordbone','itm_scianshswordt1']
items_pict_guard = ['itm_javelins','itm_leather_gloves1','itm_cloaked_tunic2','itm_ladytunicgodelic','itm_cloaked_tunic2','itm_linen_coatblue','itm_bowlhelmet','itm_irish_shsword','itm_scianshswordt1']

pict_troops = [
    ["pict_recruit", "Petta (Lig. I.)", "Pettas"] +
    troop_properties(0, 'infantry', 'pict', items_pict_recruit) +
    [khergit_face_younger_1, khergit_face_old_2],

    ["pict_woman", "Sept woman (Lig. I.)", "Sept women"] +
    troop_properties(2, 'infantry', 'pict', items_pict_woman, flags=tf_female|tf_guarantee_armor|tf_guarantee_ranged,
                     shields=[]) +
    [khergit_woman_face_1, khergit_woman_face_6],

    ["pict_archer", "Saiogdear Picti (Missile)", "Saiogdears Picti"] +
    troop_properties(0, 'archer', 'pict', items_pict_archer) +
    [khergit_face_younger_1, khergit_face_old_2],

    ["pict_footmant2", "Boaire (Lig. I.)", "Boaires"] +
    troop_properties(1, 'infantry', 'pict', items_pict_footman) +
    [khergit_face_young_1, khergit_face_older_4],

    ["pict_skirmishert3", "Fuidir (Skrm.)", "Fuidirs"] +
    troop_properties(1, 'infantry', 'pict', items_pict_skirmisher3, shields=items_shields['pict'][1]['light']) +
    [khergit_face_young_1, khergit_face_older_4],

    ["picto_portaestandarte","Samhladh","Samhladh",tf_guarantee_armor,0,0,'fac_neutral',['itm_war_paintbodyus','itm_war_paintbody1','itm_war_paintbody2','itm_war_paintbody3','itm_war_paintbody5','itm_war_paintbody6','itm_bluepantsbody_woad04','itm_war_paintbody_two','itm_wessexbanner6','itm_heraldicbannert3','itm_war_paintbody_two','itm_war_paintbodyus','itm_trophy_b'] + items_footwear[1]['military'],def_attrib2|level(23),wp(165),knows_warrior_normal,khergit_face_young_1,khergit_face_older_4],
    ["picto_cuerno","Hornman","Hornmen",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_war_paintbody8','itm_war_paintbody11','itm_war_paintbody7','itm_war_paintbody8','itm_war_paintbody10','itm_war_paintbody11','itm_war_paintbody12','itm_horn1','itm_trophy_a'] + items_shields['common'][0]['light']  + items_footwear[0]['military'],def_attrib2|level(15),wp(110),knows_warrior_normal,khergit_face_young_1,khergit_face_older_4],
    ["picto_sacerdote","Cleric","Clergy",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_monk_robe','itm_robe_beige','itm_stones1','itm_staff1'] + items_footwear[0]['military'],def_attrib|level(23),wp(165),knows_cleric,khergit_face_young_1,khergit_face_older_4],

    ["pict_horsesquiret3", "Creach Sluagh (Med. I.)", "Creach Sluagh"] +
    troop_properties(2, 'infantry', 'pict', items_pict_horsesquire3, shields=items_shields['pict'][2]['light']) +
    [khergit_face_middle_1, khergit_face_older_4],

    ["pict_skirmishert4", "Diuberr (Hv. I.)", "Diuberrs"] +
    troop_properties(3, 'infantry', 'pict', items_pict_skirmisher4, shields=items_shields['pict'][2]['light'],
                     skills=knows_warrior_veteran|knows_ironflesh_5|knows_power_strike_5) +
    [khergit_face_middle_1, khergit_face_older_4],

    ["pict_infantryt4", "Bruide (Hv. I.)", "Bruides"] +
    troop_properties(3, 'infantry', 'pict', items_pict_infantry4, shields=items_shields['pict'][2]['light'],
                     skills=knows_warrior_veteran|knows_ironflesh_5|knows_power_strike_5) +
    [khergit_face_young_1, khergit_face_older_4],

    # todo: why young face?
    ["pict_infantryt5", "Gaisgidh (Elit. I.)", "Gaisgidhs"] +
    troop_properties(4, 'infantry', 'pict', items_pict_infantry5, shields=items_shields['pict'][3]['light'],
                     skills=knows_warrior_elite|knows_ironflesh_10|knows_power_strike_5) +
    [khergit_face_young_1, khergit_face_older_4],

    # todo: why young face?
    ["pict_horseman", "Each Raidh (Lig. C.", "Each Raidhs"] +
    troop_properties(2, 'cavalry', 'pict', items_pict_horseman, shields=items_shields['pict'][2]['normal'],
                     skills=knows_warrior_normal|knows_ironflesh_4|knows_power_strike_4) +
    [khergit_face_young_1, khergit_face_older_4],

    # todo: why young face?
    ["pict_noblecavalry", "Airig (Hv. C.)", "Arras"] +
     troop_properties(3, 'cavalry', 'pict', items_pict_noblecavalry, shields=items_shields['pict'][3]['light'][:2],
                      skills=knows_warrior_veteran|knows_riding_5|knows_ironflesh_5|knows_power_strike_5) +
    [khergit_face_young_1, khergit_face_older_4],

    ["pict_messenger","Picti Messenger","Picti Messengers"] +
    troop_properties(3, 'messenger', 'pict', items_pict_messenger, shields=items_shields['pict'][2]['light']) +
    [khergit_face_young_1, khergit_face_older_4],

    ["pict_deserter", "Picti Deserter", "Picti Deserters"] +
    troop_properties(2, 'infantry', 'pict', items_pict_deserter, faction='fac_deserters',
                     shields=items_shields['pict'][2]['light'][:2] + items_shields['pict'][3]['light'][:2]) +
    [khergit_face_young_1, khergit_face_older_4],

    ["pict_prison_guard", "Prison Guard", "Prison Guards"] +
    troop_properties(3, 'infantry', 'pict', items_pict_guard, shields=[items_shields['pict'][2]['normal'][0]]) +
    [vaegir_face_middle_1, vaegir_face_older_2],

    ["pict_castle_guard", "Castle Guard", "Castle Guards"] +
    troop_properties(3, 'infantry', 'pict', items_pict_guard, shields=[items_shields['pict'][2]['normal'][0]]) +
    [khergit_face_middle_1, khergit_face_older_4],
]

items_irish_recruit = ['itm_stones1','itm_slingrocks','itm_basic_sling','itm_hoodnewwht','itm_blackhood','itm_ptunicwhite','itm_german_tunic2','itm_ptunic7','itm_ptunic3','itm_ptunic7','itm_shirtblue','itm_ptunic1','itm_thick_body','itm_knifechp','itm_staff_pitchfork','itm_clubcudgel','itm_spear_sharppitchfork','itm_quarter_staff','itm_sickle']
items_irish_archer = ['itm_arrows1','itm_shortbow','itm_huntingbow','itm_hoodnewwht','itm_blackhood','itm_head_wrappings','itm_common_hood','itm_celtcloakedbody06','itm_bluepantsbody_woad04','itm_bluepantsbody_woad04','itm_german_tunic2','itm_ptunic7','itm_cloaked_leathertunict2','itm_german_tunic2','itm_ptunic1','itm_tunicsleeveless3','itm_tunicblue8','itm_clubsmooth','itm_scianshswordt1','itm_scianshswordbone']
items_irish_footman = ['itm_slingrocks','itm_basic_sling','itm_blackhood','itm_common_hood','itm_celta_cloak1','itm_celta_cloak1','itm_red_cloak','itm_ptunic9','itm_ptunic3','itm_briton_tunic2','itm_ptunic7','itm_redpantsbody_woad11','itm_bluepantsbody_woad05','itm_tunicsleeveless6','itm_tunicsleeveless8','itm_tunicsleevelessc','itm_scianshswordbone','itm_scianshswordt1','itm_clubcudgel']
items_irish_infantry3 = ['itm_javelins','itm_gaelic_jacketgray','itm_gaelic_jacketgray','itm_ptunic7','itm_bltunic08','itm_bltunic11','itm_bltunic05','itm_scianshswordbone','itm_axe_1hlongt2','itm_pictish_boar_speart2','itm_hunting_spear']
items_irish_skirmisher3 = ['itm_darts','itm_wooden_javelins','itm_cavaljavelins','itm_gaelic_jacketgray','itm_gaelic_jacketgrn','itm_cloaked_tunicorange','itm_cloaked_tunicgreen','itm_vae_thickcoat1','itm_gatheredcloaks4','itm_byrnietunice','itm_leathercap1','itm_skullcap_reinforcedt1','itm_head_wrappings','itm_scianshswordt1','itm_axe_1hlongt2','itm_spear_lightgael']
items_irish_skirmisher4 = ['itm_cavaljavelins','itm_cavaljavelins','itm_byrnietunice','itm_vaelicus_tunic27','itm_scale_bronze_blueorange','itm_scale_bronze_fadedgrn','itm_mail_sleevelessgrn','itm_mail_sleevelessbrn','itm_mail_sleevelessgrnorange','itm_skullcap_reinforcedt1','itm_skullcapt1','itm_bronzebowlhelmet','itm_ironceltbowlhelmet','itm_scianshswordbone','itm_pommel_swordt2','itm_pommel_swordt3','itm_godelic_swordt2','itm_godelic_swordt3']
items_irish_infantry4 = ['itm_javelins','itm_skullcap_reinforcedt1','itm_leathercap1','itm_bowlhelmet','itm_scale_brown_armor','itm_noblearmor5res','itm_scianshswordbone','itm_warspear_godelict3','itm_godelic_swordt3']
items_irish_infantry5 = ['itm_throwing_spear','itm_leather_gloves1','itm_scale_brown_armor','itm_noblearmor5res','itm_mailnoble_dkgrnclk','itm_mailnoble_brwngryclk','itm_szpadelhelm1','itm_szpadelhelm2engraved','itm_szpadelhelm3t2','itm_szpadelhelm4engravedt3','itm_szpadelhelm5engravedt3','itm_red_cloak_hood','itm_scianshswordt1','itm_pommel_swordt2','itm_pommel_swordt3','itm_gaelicsword1','itm_warspear_godelict3','itm_celtic_sword','itm_britonswordt2']
items_irish_horseman = ['itm_cavaljavelins','itm_cavaljavelins','itm_linen_coatbrown','itm_linen_coatblue','itm_linen_coattan','itm_linen_coatwcloak','itm_helm_leathert2','itm_leathercap1','itm_bronzebowlhelmet','itm_ironceltbowlhelmet','itm_scianswordbone','itm_pommel_swordt2','itm_spearlong','itm_spear_briton_longt2']
items_irish_noblecavalry = ['itm_javelins','itm_javelins','itm_scale_brown_armor','itm_lorica_whitbrn','itm_scale_bronzegreen','itm_mail_sleevelessgrn','itm_mailnoble_brwnwhtclk','itm_mailnoble_ltbrwnclk','itm_spangenhelmgerm_trim','itm_romanelitehelmt3','itm_szpadelhelm1','itm_szpadelhelm3t2','itm_espada_kirkburn','itm_pict_princep_swordt3res','itm_gaelicsword1','itm_spearlong']
items_irish_messenger = ['itm_leather_gloves1','itm_javelins','itm_nobleman_outfit','itm_gaelic_jacketgrn','itm_saxon_tunic7','itm_saxon_tunic7','itm_saxon_tunic7','itm_vaelicus_tunic35','itm_vaelicus_tunic36','itm_scianshswordt1','itm_scianshswordbone','itm_axe_1hlongt2','itm_spear_lightgael','itm_warspear_godelict3']
items_irish_deserter = ['itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_cloaked_leathertunict2','itm_german_tunic2','itm_ptunic1','itm_tunicsleeveless3','itm_tunicblue8','itm_german_tunic5','itm_saxon_tunic7','itm_skullcap_reinforcedt1','itm_skullcap_reinforcedt2','itm_bronzebowlhelmet','itm_scianshswordbone','itm_axe_1hlongt2','itm_spear_lightgael','itm_warspear_godelict3']
items_irish_guard = ['itm_javelins','itm_noblearmor7res','itm_noblearmor8res','itm_wealthytunic5','itm_leathercap1','itm_rathos_bowlhelmet','itm_scianshswordbone','itm_warspear_godelict3']


irish_troops = [
    ["irish_recruit", "Bothach (Lig. I.)", "Bothach"] +
    troop_properties(0, 'infantry', 'irish', items_irish_recruit) +
    [rhodok_face_younger_1, rhodok_face_old_2],

    ["irish_archer", "Saiogdear Goidel (Missile)", "Saiogdears Goidels"] +
    troop_properties(0, 'archer', 'irish', items_irish_archer) +
    [rhodok_face_younger_1, rhodok_face_old_2],

    ["irish_footmant2", "Ceither (Lig. I.)", "Ceithers"] +
    troop_properties(1, 'infantry', 'irish', items_irish_footman) +
    [khergit_face_young_1, khergit_face_older_4],

    ["irish_infantryt3", "Cliarthaire (Med. I.)", "Cliarthaires"] +
    troop_properties(2, 'infantry', 'irish', items_irish_infantry3, shields=items_shields['irish'][1]['light']) +
    [rhodok_face_young_1, rhodok_face_older_2],

    ["irish_bannerman","Meirgeach","Meirgeach",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_celta_cloak1','itm_celta_cloak1','itm_nobleman_outfit','itm_gaelic_jacketgrn','itm_saxon_tunic7','itm_saxon_tunic7','itm_saxon_tunic7','itm_vaelicus_tunic35','itm_vaelicus_tunic36','itm_wessexbanner7','itm_wessexbanner8','itm_heraldicbannert3','itm_trophy_b'] + items_footwear[1]['military'],def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1,vaegir_face_old_2],
    ["irish_priest","Cleric Goidel","Cleric Goidels",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_monk_robe','itm_blackwornrobe','itm_stones1','itm_knifechp'] + items_footwear[0]['military'],def_attrib|level(23),wp(165),knows_cleric,sac_face_1,sac_face_2],

    ["irish_skirmishert3", "Fian (Skrm.)", "Fianna"] +
    troop_properties(1, 'infantry', 'irish', items_irish_skirmisher3, shields=items_shields['irish'][0]['normal']) +
    [rhodok_face_young_1, rhodok_face_older_2],

    ["irish_skirmishert4", "Deaisbard (Elit. Skrm.)", "Deaisbards"] +
    troop_properties(3, 'infantry', 'irish', items_irish_skirmisher4, shields=items_shields['irish'][1]['normal']) +
    [rhodok_face_young_1, rhodok_face_older_2],

    ["irish_infantryt4", "Ocaire (Med. I.)", "Ocaires"] +
    troop_properties(3, 'infantry', 'irish', items_irish_infantry4, shields=items_shields['irish'][2]['normal']) +
    [rhodok_face_young_1, rhodok_face_older_2],

    ["irish_infantryt5", "Airig (Hv. I.)", "Arras"] +
    troop_properties(4, 'infantry', 'irish', items_irish_infantry5, shields=items_shields['irish'][3]['light']) +
    [rhodok_face_middle_1, rhodok_face_older_2],

    ["irish_horseman", "Marcach (Lig. C.)", "Marcachs"] +
    troop_properties(3, 'cavalry', 'irish', items_irish_horseman, shields=items_shields['irish'][2]['light']) +
    [rhodok_face_middle_1, rhodok_face_older_2],

    ["irish_noblecavalry", "Curraidh (Elit. C.)", "Curraidhs"] +
     troop_properties(4, 'cavalry', 'irish', items_irish_noblecavalry, shields=items_shields['pict'][3]['light'][:2]) +
    [rhodok_face_middle_1, rhodok_face_older_2],

    ["irish_messenger", "Gael Messenger", "Gaels Messengers"] +
    troop_properties(3, 'messenger', 'irish', items_irish_messenger, shields=items_shields['pict'][2]['light']) +
    [rhodok_face_young_1, rhodok_face_older_2],

    ["irish_deserter", "Goidels Deserter", "Goidels Deserters"] +
    troop_properties(2, 'infantry', 'irish', items_irish_deserter, faction='fac_deserters',
                     shields=items_shields['irish'][2]['normal'][:2] + items_shields['irish'][2]['light'][:2]) +
    [rhodok_face_young_1, rhodok_face_older_2],

    ["irish_prison_guard", "Prison Guard", "Prison Guards"] +
    troop_properties(3, 'infantry', 'irish', items_irish_guard, shields=[items_shields['irish'][1]['normal'][2]]) +
    [rhodok_face_young_1, rhodok_face_older_2],

    ["irish_castle_guard", "Castle Guard", "Castle Guards"] +
    troop_properties(3, 'infantry', 'irish', items_irish_guard, shields=[items_shields['irish'][1]['normal'][2]]) +
    [rhodok_face_young_1, rhodok_face_older_2],
]

items_saxon_recruit = ['itm_stones1','itm_slingrocks','itm_basic_sling','itm_woolencap_newgrn','itm_woolencap_newblk','itm_woolencap_newblk','itm_woolencap','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_briton_tunic2','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic1','itm_ptunic12','itm_knifechp','itm_spear_sharppitchfork','itm_clubsmooth','itm_quarter_staff','itm_sickle','itm_axe1','itm_club_stick']
items_saxon_footmant2 = ['itm_javelins','itm_slingrocks','itm_basic_sling','itm_fustibalus','itm_woolencap_red','itm_woolencap_newgrn','itm_woolencap_newblk','itm_plaincloakbeige','itm_plaincloakbrown','itm_plaincloakltblue','itm_merch_furjacketwhite','itm_merch_furjacket2t3','itm_merch_furjacketyelo','itm_club_thorny','itm_club3','itm_seaxt4','itm_germanshortspeart2']
items_saxon_infantryt3 = ['itm_javelins','itm_woolencap_newblk','itm_woolencap_newblk','itm_rathos_bowlhelmet','itm_rawhide_vest_green','itm_rawhide_coat9grey','itm_rawhide_vest_blue','itm_rawhide_coat2','itm_rawhide_coat2','itm_spear1','itm_langseaxt2']
items_saxon_infantryt4 = ['itm_angons','itm_angonst2','itm_leather_gloves1','itm_lorica_whitbrn','itm_woolencap_newblu','itm_woolencap_red','itm_woolencap_newblk','itm_woolencap','itm_leather_captainhelm','itm_leathercap1','itm_dena_helmgoat','itm_leathercap1','itm_skullcap_reinforcedt2','itm_bamburghsword2t2','itm_spear_hasta','itm_langseaxt2']
items_saxon_infantryt5 = ['itm_angons','itm_angonst2','itm_leather_gloves1','itm_mailtunic_brownclk','itm_mailtunic_ltbrown','itm_lorica_greyrd','itm_lorica_stripedblue','itm_wolfpelt_mail_coat','itm_mailtunic_brownclk','itm_mailtunic_blk','itm_mailtunic_brown','itm_mailtunic_blk','itm_mailtunic_brownclk','itm_noblearmor16res','itm_mailtunic_grey','itm_jutehelmt3','itm_jutehelmt3','itm_dena_elite_helm2boar','itm_copper_helmet','itm_saxon_helmt2','itm_spangenhelmb1','itm_dena_helmgoat','itm_spear_hvy','itm_spear_hasta','itm_saxonswordt2','itm_briton_richswordt2','itm_jute_richsword']
items_saxon_archer = ['itm_arrows1','itm_shortbow','itm_huntingbow','itm_woolencap_newblu','itm_woolencap_red','itm_woolencap_newgrn','itm_woolencap','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_briton_tunic2','itm_ptunic2','itm_mercia_tunicgrn','itm_ptunic1','itm_clubcudgel','itm_seaxt3','itm_saxon_axet2']

items_saxon_skirmisher3 = ['itm_javelins','itm_javelins', 'itm_rawhide_coat6white','itm_rawhide_vest_red','itm_pelt_coat2','itm_merch_furjacketyelo', 'itm_axe_longfrankisht3','itm_saxon_medium_speart2','itm_spearlight','itm_langseaxt2', 'itm_knisxclearvert3']
items_saxon_skirmisher4 = ['itm_angons','itm_javelins','itm_angonst2','itm_leather_gloves1','itm_plaincloakltblue','itm_plaincloakbrown','itm_plaincloakbeige','itm_jack_armorpaddedred','itm_jack_armorfadedblue','itm_jack_armorfadedblue','itm_vae_thickcoat3','itm_leather_helm_tan','itm_hornhelmet3_t2','itm_rathos_bowlhelmet','itm_spangenhelmblight','itm_langseaxt2','itm_spearlight','itm_axe4','itm_axe2_crude','itm_germanic_axelongt2']
items_saxon_skirmisher5 = ['itm_angons','itm_angonst2','itm_leather_gloves1', 'itm_lorica_eggwht','itm_lorica_olive','itm_noblearmor16res', 'itm_lorica_yelo','itm_mailshirt_3_trig','itm_spangenhelmalight','itm_spangenhelma1', 'itm_frisian_helm3t2','itm_dena_helmboar3','itm_briton_helm','itm_copper_helmet', 'itm_jutehelmt3','itm_battle_axe2ht2','itm_saxonswordt2','itm_germanicswordt2']
items_saxon_horseman1 = ['itm_javelins','itm_jack_armorgreen','itm_jack_armorgreen','itm_lorica_pink','itm_noblearmor14res','itm_mailnoble_ltbrwnclk','itm_lorica_greyrd','itm_spangenhelmb1','itm_frisian_helm3t2','itm_saxon_helmt2','itm_spangenhelma_yellow','itm_hornhelmet2','itm_hornhelmet1','itm_hornhelmet3_t2','itm_maul1h_blunt','itm_spearlong','itm_saxonswordt2','itm_germanicswordt2']
items_saxon_messenger = ['itm_leather_gloves1','itm_javelins','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_spear1','itm_spearlight','itm_langseaxt2']
items_saxon_deserter = ['itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_woolencap_newblu','itm_woolencap_red','itm_woolencap_newblk','itm_woolencap','itm_leather_captainhelm','itm_leathercap1','itm_bowlhelmet','itm_hornhelmet2','itm_leathercap1','itm_axe_longfrankisht3','itm_saxon_medium_speart2','itm_spearlight','itm_spearboar','itm_langseaxt2','itm_knisxclearvert3','itm_spearlight']
items_saxon_guard = ['itm_angons','itm_leather_gloves1','itm_rawhide_coat7green','itm_linen_coatbrown','itm_linen_coatblue','itm_woolencap_newblk','itm_woolencap','itm_bowlhelmet','itm_hornhelmet2','itm_leathercap1','itm_spear_hvy','itm_langseaxt2']

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

    ["saxon_bannerman", "Tacnberend", "Tacnberend",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_plaincloakbeige','itm_plaincloakred','itm_plaincloakbrown','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_blue_shorttunic','itm_ptunic13','itm_goatcap1','itm_goat_capbrn','itm_boar_helmet','itm_wessexbanner1','itm_heraldicbannert3','itm_trophy_b','itm_leather_gloves1'] + items_footwear[1]['military'],def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1,vaegir_face_old_2],
    ["todos_cuerno", "Hornman", "Hornmen",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_plaincloakbeige','itm_plaincloakred','itm_plaincloakbrown','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_horn1','itm_trophy_a','itm_stones1','itm_knisxclearvert3'] + items_shields['common'][0]['light'] + items_footwear[0]['military'],def_attrib2|level(15),wp(115),knows_warrior_normal,vaegir_face_young_1,vaegir_face_old_2],
    ["saxon_sacerdote", "Cleric Seaxe", "Clerics Seaxna",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_monk_robe','itm_blackwht_robe','itm_stones1','itm_staff1'] + items_footwear[0]['military'],def_attrib|level(23),wp(170),knows_cleric,sac_face_1,sac_face_2],

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

items_jute_recruit = ['itm_maul1h_blunt','itm_stones1','itm_slingrocks','itm_basic_sling','itm_woolencap_newblu','itm_woolencap_newblk','itm_woolencap','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_briton_tunic2','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic1','itm_thick_body','itm_knifechp','itm_staff_pitchfork','itm_clubcudgel','itm_spear_sharppitchfork','itm_staff1','itm_sickle']
items_jute_footman = ['itm_maul1h_blunt','itm_axe3','itm_javelins','itm_slingrocks','itm_basic_sling','itm_fustibalus','itm_woolencap_newblu','itm_woolencap_newblk','itm_woolencap','itm_plaincloakltblue','itm_plaincloakred','itm_plaincloakbeige','itm_plaincloakbrown','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_merch_furjacketblue','itm_merch_furjacketyelo','itm_merch_furjacketyelo','itm_club3','itm_seaxt4']
items_jute_infantry3 = ['itm_woolencap_newblu','itm_woolencap_newgrn','itm_ptunic13','itm_ptunic13','itm_ptunic14','itm_rawhide_vest_green','itm_rawhide_coat9grey','itm_rawhide_vest_blue','itm_rawhide_coat2','itm_rawhide_coat3','itm_germanlongspeart2','itm_saxon_medium_speart2','itm_saxonsword1']
items_jute_archer = ['itm_arrows1','itm_shortbow','itm_huntingbow','itm_woolencap_newblk','itm_woolencap_newblk','itm_woolencap','itm_ptunic3','itm_ptunicwhite','itm_ptunic11','itm_briton_tunic2','itm_peasant_ftunic','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_clubcudgel','itm_seaxt3','itm_axe_britonbattlet2']
items_jute_skirmisher3 = ['itm_woolencap_newblk','itm_woolencap','itm_rawhide_coat7green','itm_rawhide_vest_red','itm_pelt_coat2','itm_germanlongspeart2','itm_saxon_medium_speart2','itm_saxonsword1']
items_jute_skirmisher4 = ['itm_angons','itm_angonst2','itm_plaincloakbeige','itm_plaincloakbrown','itm_cloak_boar_furcap','itm_jack_armorpaddedred','itm_jack_armorfadedblue','itm_vae_thickcoat2','itm_vae_thickcoat3','itm_jack_armorgreen','itm_jack_armorgreen','itm_rathos_bowlhelmet','itm_bowlhelmet','itm_leather_helm_tan','itm_hornhelmet3_t2','itm_spangenhelmblight','itm_dena_helmboar2','itm_saxon_medium_speart2','itm_talak_seaxkni','itm_maul1h_blunt','itm_ironhammerlong']
items_jute_horseman = ['itm_angleswordt2','itm_javelins','itm_leather_gloves1','itm_jack_armorgreen','itm_jack_armorfadedblue','itm_jack_armorfadedblue','itm_jack_armorpaddedred','itm_lorica_pink','itm_noblearmor14res','itm_mailnoble_ltbrwnclk','itm_lorica_greyrd','itm_frisian_helm3t2','itm_frisian_helm1','itm_dena_elite_helm1boar','itm_jutehelmt3','itm_hornhelmet3_t2','itm_jutehelmt3','itm_ironhammerlong','itm_spearlong']
items_jute_skirmisher5 = ['itm_throwing_axes','itm_angonst2','itm_leather_gloves1','itm_lorica_eggwht','itm_lorica_ltblue','itm_noblearmor15res','itm_lorica_white','itm_lorica_whitegry','itm_frisian_helm3t2','itm_dena_elite_helm1boar','itm_dena_helmboar5','itm_frisian_helm3t2','itm_dena_helmboar2','itm_leather_helm_grey','itm_khergit_cavalry_helmet','itm_axe_longfrankisht3','itm_decor_axet3','itm_richsword2','itm_saxondenaswordt3','itm_briton_richswordt2']
items_jute_infantryt4 = ['itm_throwing_axes','itm_angonst2','itm_leather_gloves1','itm_leather_captainhelm','itm_leathercap1','itm_hornhelmet2','itm_skullcap_reinforcedt2','itm_lorica_whitbrn','itm_mailshirt_yellow','itm_mailshirt_orange','itm_noblearmor6res','itm_bamburghsword2t2','itm_spear_hvy']
items_jute_infantryt5 = ['itm_angonst2','itm_throwing_axes','itm_leather_gloves1','itm_lamellar2yellow','itm_lamellarbrown','itm_lamellargrey','itm_mail_wolf_coat1','itm_wolfpelt_mail_coat','itm_mailtunic_brownclk','itm_mailtunic_blk','itm_hornhelmet1','itm_dena_elite_helm2boar','itm_dena_elite_helm2boar','itm_dena_elite_helm2boar','itm_dena_elite_helm2boar','itm_dena_elite_helm1boar','itm_frisian_helm3t2','itm_dena_helmboar2','itm_spear_hvy','itm_maul1h_blunt','itm_richsword2','itm_saxondenaswordt3']
items_jute_messenger = ['itm_javelins','itm_leather_gloves1','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_spear1','itm_spearlight','itm_langseaxt2']
items_jute_deserter = ['itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_woolencap_newblu','itm_woolencap_red','itm_woolencap_newblk','itm_woolencap','itm_bowlhelmet','itm_hornhelmet2','itm_strawcap','itm_axe_longfrankisht3','itm_saxon_medium_speart2','itm_spearlight','itm_langseaxt2','itm_knisxclearvert3','itm_spearlight']
items_jute_guard = ['itm_angons','itm_leather_gloves1','itm_woolencap_newblu','itm_woolencap_red','itm_leather_captainhelm','itm_leathercap1','itm_bowlhelmet','itm_noblemanshirt1','itm_noblemanshirt2','itm_rawhide_vest_red','itm_jack_armorfadedblue','itm_spear_hasta','itm_langseaxt2']

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

    ["jute_portaestandarte","Tacnberend","Tacnberend",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_plaincloakbrown','itm_plaincloakltblue','itm_plaincloakred','itm_plaincloakltblue','itm_plaincloakbeige','itm_ptunic3','itm_ptunicwhite','itm_wessex_tunic3','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_goatcap1','itm_goat_capbrn','itm_boar_helmet','itm_spearbanner5','itm_heraldicbannert3','itm_trophy_b'] + items_footwear[1]['military'],def_attrib2|level(23),wp_one_handed(170)|wp_polearm(125)|wp(80),knows_warrior_normal,vaegir_face_young_1,vaegir_face_old_2],
    ["jute_cleric","Jute Cleric","Jutes Clerics",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_monk_robe','itm_blackwht_robe','itm_stones1','itm_staff1'] + items_footwear[0]['military'],def_attrib|level(23),wp(170),knows_cleric,sac_face_1,sac_face_2],

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
items_engle_recruit = ['itm_stones1','itm_slingrocks','itm_basic_sling','itm_woolencap_red','itm_woolencap_newgrn','itm_woolencap_newblk','itm_woolencap','itm_ptunic3','itm_ptunicwhite','itm_ptunic12','itm_briton_tunic2','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic1','itm_thick_body','itm_knifechp','itm_staff_pitchfork','itm_spear_sharppitchfork','itm_quarter_staff','itm_sickle','itm_axe1']
items_engle_footman = ['itm_javelins','itm_slingrocks','itm_basic_sling','itm_fustibalus','itm_woolencap_newblu','itm_woolencap_newgrn','itm_plaincloakltblue','itm_plaincloakbeige','itm_plaincloakbrown','itm_ptunic3','itm_wessex_tunic3','itm_mercia_tunicgrn','itm_peasant_ftunic','itm_leather_tunic1','itm_merch_furjacketwhite','itm_merch_furjacket2t3','itm_merch_furjacketyelo','itm_club3','itm_clubcudgel','itm_axe3']
items_engle_infantry3 = ['itm_javelins','itm_rawhide_vest_green','itm_rawhide_coat9grey','itm_rawhide_vest_blue','itm_rawhide_coat2','itm_rawhide_coat2','itm_spear1','itm_spearlight','itm_langseaxt2']
items_engle_archer = ['itm_arrows1','itm_shortbow','itm_huntingbow','itm_peasant_ftunic','itm_ptunicwhite','itm_ptunic12','itm_briton_tunic2','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic1','itm_clubcudgel','itm_seaxt3','itm_axe2']
items_engle_skirmisher3 = ['itm_javelins','itm_javelins','itm_rawhide_coat7green','itm_rawhide_vest_red','itm_pelt_coat2','itm_merch_furjacketyelo','itm_merch_furjacketyelo','itm_germanic_axelongt2','itm_saxon_medium_speart2','itm_spearlight','itm_langseaxt2','itm_knisxclearvert3','itm_spearlight']
items_engle_skirmisher4 = ['itm_angons','itm_javelins','itm_angonst2','itm_plaincloakltblue','itm_plaincloakbrown','itm_cloak_boar_furcap','itm_jack_armorpaddedred','itm_jack_armorfadedblue','itm_vae_thickcoat2','itm_vae_thickcoat3','itm_jack_armorgreen','itm_rathos_bowlhelmet','itm_bowlhelmet','itm_leather_helm_tan','itm_hornhelmet3_t2','itm_khergit_cavalry_helmet','itm_seaxt3','itm_saxon_axet2','itm_axe_englet2','itm_spear_hasta','itm_germanic_axelongt2']
items_engle_horseman = ['itm_javelins','itm_javelins','itm_jack_armorgreen','itm_jack_armorfadedblue','itm_lorica_pink','itm_noblearmor14res','itm_mailnoble_ltbrwnclk','itm_lorica_greyrd','itm_mierce_helmt3','itm_briton_helm','itm_briton_helmengravedt2','itm_dena_elite_helm1boar','itm_dena_elite_helm2boar','itm_angloblackbrownhelm','itm_hornhelmet1','itm_hornhelmet3_t2','itm_angleswordt2','itm_spearlong','itm_spearwarlong']
items_engle_skirmisher5 = ['itm_angons','itm_angonst2','itm_leather_gloves1','itm_lorica_ltblue','itm_lorica_white','itm_noblearmor16res','itm_lorica_whitegry','itm_lorica_yelo','itm_hornhelmet1','itm_hornhelmet2','itm_saxon_helmt2','itm_saxonhelmnoblet4','itm_briton_helmtrimt2','itm_briton_helm_3','itm_dena_elite_helm1boar','itm_dena_helmboar2','itm_seaxt4','itm_angleswordt2','itm_jute_richsword','itm_saxonswordt2','itm_germanicswordt2']
items_engle_infantryt4 = ['itm_angons','itm_angonst2','itm_lorica_whitbrn','itm_mailshirt_yellow','itm_noblearmor6res','itm_leather_captainhelm','itm_rathos_bowlhelmet','itm_leathercap1','itm_skullcap_reinforcedt2','itm_spear_hvy','itm_bamburghsword2t2','itm_langseaxt2']
items_engle_infantryt5 = ['itm_angons','itm_angonst2','itm_leather_gloves1','itm_mailtunic_greycheap','itm_mailnoble_redclk1','itm_mailnoble_greenclk','itm_mailtunic_brownclk','itm_mailtunic_blk','itm_mailtunic_brownclk','itm_mailtunic_grey','itm_mierce_helmt3','itm_briton_helm','itm_briton_helmslvtrimt3','itm_dena_helmboar5','itm_angloblackbrownhelm','itm_dena_elite_helm2boar','itm_briton_helmtrimt2','itm_bronze_warlord_helmetboar','itm_spear_hvy','itm_ornate_seaxt3','itm_angle_swordt3','itm_angleswordt2','itm_germanicswordt2']
items_engle_messenger = ['itm_leather_gloves1','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_spear1','itm_spearlight','itm_langseaxt2']
items_engle_deserter = ['itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_ptunic13','itm_woolencap_newblu','itm_woolencap_red','itm_woolencap_newblk','itm_woolencap','itm_bowlhelmet','itm_hornhelmet2','itm_strawcap','itm_skullcap_reinforcedt2','itm_germanic_axelongt2','itm_saxon_medium_speart2','itm_spearlight','itm_spearboar','itm_langseaxt2','itm_knisxclearvert3','itm_spearlight']
items_engle_guard = ['itm_angons','itm_leather_gloves1','itm_noblemanshirt3','itm_linen_coatbrown','itm_linen_coatblue','itm_woolencap_red','itm_leather_captainhelm','itm_skullcap_reinforcedt2','itm_spear_hvy','itm_langseaxt2']


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

    ["engle_bannerman","Tacnberend","Tacnberend",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_plaincloakbeige','itm_plaincloakltblue','itm_plaincloakred','itm_ptunicwhite','itm_ptunic12','itm_wessex_tunic3','itm_ptunic2','itm_mercia_tunicgrn','itm_blue_shorttunic','itm_goatcap1','itm_goat_capbrn','itm_boar_helmet','itm_goat_miercehelmt3','itm_cavalrybannert2','itm_heraldicbannert3','itm_spearbannert2','itm_trophy_b','itm_leather_gloves1','itm_helm_leathert2'] + items_footwear[1]['military'],def_attrib2|level(23),wp(170),knows_warrior_normal,vaegir_face_young_1,vaegir_face_old_2],
    ["engle_rxpriest","Cleric Engle","Cleric Engles",tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_monk_robe','itm_blackwht_robe','itm_stones1','itm_staff1'] + items_footwear[0]['military'],def_attrib|level(23),wp(165),knows_cleric,sac_face_1,sac_face_2],

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


items_briton_recruit = ['itm_stones1','itm_slingrocks','itm_basic_sling','itm_hoodnewblk','itm_common_hood','itm_ptunic3','itm_ptunicwhite','itm_ptunic1','itm_briton_tunic2','itm_ptunic2','itm_ptunic3','itm_ptunic3','itm_shirtblue','itm_knifechp','itm_staff_pitchfork','itm_clubcudgel','itm_spear_sharppitchfork','itm_clubsmooth','itm_sickle']
items_briton_footman = ['itm_wooden_javelins','itm_wooden_javelins','itm_slingrocks','itm_basic_sling','itm_fustibalus','itm_hoodnewblu','itm_hoodnewblk','itm_hoodnewwht','itm_blackhood','itm_black_cloak','itm_woven_cloak','itm_tunicblue8','itm_ptunic9','itm_ptunic5','itm_german_tunica','itm_ptunic3','itm_peasant_ftunic','itm_peasant_archertunic','itm_farmertunic26','itm_spikedclub','itm_clubsmooth','itm_axe2','itm_spear_britonshortt2']
items_briton_infantry3 = ['itm_javelins','itm_plaincloakltblue','itm_plaincloakred','itm_plaincloakbeige','itm_plaincloakbrown','itm_linen_coatwcloak','itm_goatist_tuniccoat','itm_linen_coatblue','itm_spear_britonmedt2','itm_spear_britonlight','itm_knife1','itm_scianshswordt1']
items_briton_infantry4 = ['itm_throwing_spear','itm_mailbyrniegrey','itm_mailbyrniewhitered','itm_mailbyrnieblue','itm_mail_sleevelessbrn','itm_noblearmor7res','itm_mailbyrnie_longfurred','itm_mailcuir_bouilli','itm_mail_largering','itm_linen_coatblue','itm_spear_blade2t2','itm_spear_blade2t2','itm_knife1','itm_britonswordt2','itm_arming_cap','itm_roman_helmlate']
items_briton_infantry5 = ['itm_throwing_spear','itm_leather_gloves1','itm_noblearmor12res','itm_mailtunic_blk','itm_lorica_stripedred','itm_spangenhelmalight','itm_romanelitehelmt3','itm_spangenhelmb1','itm_briton_helmengravedt2','itm_briton_helm_3','itm_briton_helmslvtrimt3','itm_roman_helmlatet2','itm_spear_blade2t2','itm_bamburghsword2t2','itm_britonswordt2','itm_bamburghsword2t2']
items_briton_archer = ['itm_arrows1','itm_shortbow','itm_huntingbow','itm_hoodnewblu','itm_hoodnewblk','itm_hoodnewwht','itm_blackhood','itm_ptunic3','itm_ptunicwhite','itm_tunicblue8','itm_ptunic9','itm_ptunic3','itm_ptunic5','itm_german_tunica','itm_ptunic3','itm_peasant_etunic','itm_farmertunic26','itm_club_stick','itm_axe2','itm_clubcudgel']
items_briton_longbowman = ['itm_arrows1','itm_longbow','itm_hoodnewwht','itm_blackhood','itm_head_wrappings','itm_common_hood','itm_ptunic3','itm_ptunic12','itm_shirtblue','itm_ptunic3','itm_shirtylw','itm_shirtaqua','itm_shirtgrey','itm_bltunicgrn','itm_peasant_archertunic','itm_farmertunic26','itm_scianshswordbone','itm_scianshswordt1','itm_axe2','itm_axe4']
items_briton_horseman = ['itm_cavaljavelins','itm_linen_coatbrown','itm_linen_coattan','itm_scale_bronze_armor','itm_scale_brown_armor','itm_mailbyrniegreen','itm_mailbyrnieyelo','itm_rathos_bowlhelmet','itm_briton_helm','itm_leather_captainhelm','itm_leather_helm_grey','itm_spangenhelma_yellow','itm_spear_briton_longt2','itm_britonswordt2']
items_briton_cavalry = ['itm_javelins','itm_leather_gloves1','itm_mail_furredt2','itm_mailtunic_blk','itm_noblearmor12res','itm_scaleorangeblkbands','itm_mailbyrniered','itm_scale_bronze_armor','itm_mail_goatist','itm_briton_helm','itm_dux_ridgehelm','itm_leatherneck_helm','itm_spangenhelma_ornate','itm_mierce_helmt3','itm_briton_helmtrimt2','itm_spangenhelmgerm_trim','itm_roman_helmlatet2','itm_spear_briton_longt2','itm_britonswordt2','itm_rich_spathaswordt2']
items_briton_skirmt3 = ['itm_cavaljavelins','itm_cavaljavelins','itm_black_cloak','itm_woven_cloak','itm_plaincloakbrown','itm_vae_thickcoat2','itm_vae_thickcoat3','itm_helm_leathert2','itm_skullcap_reinforcedt1','itm_strawcap','itm_skullcap_reinforcedt2','itm_blackened_axet2','itm_spear_britonshortt2','itm_scianshswordt1']
items_briton_skirmishert4 = ['itm_throwing_spear','itm_throwing_spear','itm_leather_gloves1','itm_scale_white_armor','itm_mail_sleevelessbrn','itm_mail_furredt2','itm_mailtunic_blk','itm_lorica_stripedblue','itm_spangenhelmalight','itm_spangenhelmblight','itm_briton_helm','itm_rathos_bowlhelmet','itm_arming_cap','itm_roman_helmlate','itm_spear_blade2t2','itm_spear_blade2t2','itm_saxonswordt2','itm_lang_knifet2','itm_noble_shswordt2']
items_briton_messenger = ['itm_leather_gloves1','itm_leather_gloves1','itm_javelins','itm_ptunic3','itm_ptunicwhite','itm_shirtblue','itm_ptunic3','itm_ptunic3','itm_shirtylw','itm_shirtaqua','itm_shirtgrey','itm_bltunicgrn','itm_spear_briton_longt2','itm_spear_briton_longt2','itm_sciansword','itm_scianswordbone','itm_longspeart3','itm_lang_knifet2','itm_knife1']
items_briton_deserter = ['itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_javelins','itm_ptunicwhite','itm_shirtblue','itm_ptunic3','itm_shirtgrey','itm_bltunicgrn','itm_ptunic3','itm_ptunic3','itm_shirtylw','itm_bltunicgrn','itm_leathercap1','itm_skullcap_reinforcedt1','itm_strawcap','itm_skullcap_reinforcedt2','itm_skullcapt1','itm_spear_britonmedt2','itm_spear_britonlight','itm_spear_hasta','itm_langseaxt2','itm_scianshswordt1']
items_briton_guards = ['itm_throwing_spear','itm_leather_gloves1','itm_ptunic3','itm_bltunic10','itm_mailtunic_blk','itm_lorica_stripedblue','itm_spangenhelmblight','itm_spangenhelmalight','itm_spear_blade2t2','itm_scianshswordt1']


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

    ["briton_bannerman", "Gwas Ys Tafell", "Gwas Ys Tafell", tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_plaincloakbeige','itm_plaincloakbrown','itm_ptunic3','itm_ptunicwhite','itm_shirtblue','itm_ptunic3','itm_shirtylw','itm_shirtaqua','itm_shirtgrey','itm_bltunicgrn','itm_ptunic11','itm_peasant_ftunic','itm_wessexbanner9','itm_spearbanner4','itm_heraldicbannert3','itm_trophy_b','itm_bluepantsbody_woad05','itm_cloaked_tunic1','itm_jack_armorfadedblue','itm_noblearmor22res','itm_leather_gloves1','itm_helm_leathert2'] + items_footwear[1]['military'],def_attrib2|level(23),wp(165),knows_warrior_normal,swadian_face_young_1,swadian_face_old_2],
    ["briton_sacerdote", "Briton Cleric", "Britons Clerics", tf_guarantee_boots|tf_guarantee_armor,0,0,'fac_neutral',['itm_monk_robe','itm_robe_darkprp','itm_stones1','itm_staff1'] + items_footwear[0]['military'],def_attrib|level(23),wp(165),knows_cleric,sac_face_1,sac_face_2],

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
