from header_items import *
from header_item_modifiers import *

imodbits_horse_basic = imodbit_swaybacked | imodbit_lame | imodbit_spirited | imodbit_heavy | imodbit_stubborn
imodbits_horse_good = imodbit_spirited | imodbit_heavy


north_horse_properties = [itp_merchandise | itp_type_horse, 0, 2000,
                          abundance(60) |
                          hit_points(73) |
                          body_armor(10) |
                          difficulty(1) |
                          horse_speed(44) |
                          horse_maneuver(40) |
                          horse_charge(10) |
                          horse_scale(91),
                          imodbits_horse_basic]

draft_horse_properties = [itp_merchandise | itp_type_horse, 0, 2300,
                          abundance(60) |
                          hit_points(90) |
                          body_armor(16) |
                          difficulty(2) |
                          horse_speed(36) |
                          horse_maneuver(35) |
                          horse_charge(17) |
                          horse_scale(94),
                          imodbits_horse_basic]

greek_horse_properties = [itp_type_horse, 0, 3300,
                          abundance(60) |
                          hit_points(115) |
                          body_armor(22) |
                          difficulty(3) |
                          horse_speed(37) |
                          horse_maneuver(33) |
                          horse_charge(19) |
                          horse_scale(100),
                          imodbits_horse_basic | imodbit_champion]

mesh_good_horse = ("horse_c", imodbits_horse_good)


horses = [
    ["pony_horse", "Pony", [("rus_horse", 0)], itp_merchandise|itp_type_horse, 0, 1800,abundance(60)|hit_points(60)|body_armor(10)|difficulty(1)|horse_speed(37)|horse_maneuver(36)|horse_charge(9)|horse_scale(86),imodbits_horse_basic],

    ["gallic_horse1", "Gallic Horse", [("gallic_horse_1", 0), mesh_good_horse], itp_merchandise|itp_type_horse, 0, 2000,abundance(60)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],
    ["gallic_horse2", "Gallic Horse", [("gallic_horse_2", 0), mesh_good_horse], itp_merchandise|itp_type_horse, 0, 2000,abundance(60)|hit_points(73)|body_armor(10)|difficulty(1)|horse_speed(42)|horse_maneuver(44)|horse_charge(10)|horse_scale(91),imodbits_horse_basic],

    ["saddle_horse1", "North Horse", [("roman_horse_1", 0), mesh_good_horse]] + north_horse_properties,
    ["roman_horse1", "North Horse", [("WRoman1", 0), mesh_good_horse]] + north_horse_properties,
    ["roman_horse2", "North Horse", [("WRoman2", 0), mesh_good_horse]] + north_horse_properties,
    ["pictish_mare", "North Horse", [("Pictish1", 0), mesh_good_horse]] + north_horse_properties,
    ["pictish_stallion", "North Horse", [("Pictish2", 0), mesh_good_horse]] + north_horse_properties,
    ["frankishhorse1", "North Horse", [("roman_horse_2", 0), mesh_good_horse]] + north_horse_properties,
    ["spanish_horset2", "North Horse", [("normal_horse13", 0), mesh_good_horse]] + north_horse_properties,
    ["frankishhorsecharger", "North Horse", [("gallic_horse_3", 0), mesh_good_horse]] + north_horse_properties,
    ["frankishhorset2", "North Horse", [("normal_horse14", 0), mesh_good_horse]] + north_horse_properties,
    ["horsecourser1", "North Horse", [("normal_horse31", 0), mesh_good_horse]] + north_horse_properties,

    ["horsecourser2", "Draft Horse", [("courser", 0)]] + draft_horse_properties,
    ["horsecourser3t2", "Draft Horse", [("normal_horse23", 0)]] + draft_horse_properties,
    ["drafthorse1", "Draft Horse", [("normal_horse4", 0)]] + draft_horse_properties,
    ["drafthorse2", "Draft Horse", [("normal_horse9", 0)]] + draft_horse_properties,
    ["drafthorse3t2", "Draft Horse", [("normal_horse8", 0)]] + draft_horse_properties,
    ["drafthorse8", "Draft Horse", [("normal_horse8", 0)]] + draft_horse_properties,
    ["frankishhorsechargert3", "Draft Horse", [("normal_horse26", 0)]] + draft_horse_properties,

    ["huntinghorset3", "Paraveredus", [("WSumpterChestnut", 0),("hunting_horse", imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 2400,abundance(60)|hit_points(80)|body_armor(12)|difficulty(3)|horse_speed(46)|horse_maneuver(44)|horse_charge(12)|horse_scale(88),imodbits_horse_basic|imodbit_champion],
    ["fastwarhorset3", "Paraveredus", [("WSumpterBrown", 0),("hunting_horse", imodbits_horse_good)], itp_type_horse, 0, 2400,abundance(60)|hit_points(85)|body_armor(12)|difficulty(3)|horse_speed(46)|horse_maneuver(44)|horse_charge(12)|horse_scale(88),imodbits_horse_basic|imodbit_champion],

    ["warhorse1", "Greek armoured horse", [("HalfCata2", 0)]] + greek_horse_properties,
    ["warhorse2", "Greek armoured horse", [("warhorse", 0)]] + greek_horse_properties,

    # donkey
    ["donkey_horse1", "Donkey", [("donkey_mount", 0)], itp_merchandise|itp_type_horse, 0, 800,abundance(60)|hit_points(55)|body_armor(7)|difficulty(0)|horse_speed(32)|horse_maneuver(33)|horse_charge(8)|horse_scale(79),imodbits_horse_basic],
    ["donkey_horse2", "Donkey", [("donkey_mount2", 0)], itp_merchandise|itp_type_horse, 0, 800,abundance(60)|hit_points(55)|body_armor(7)|difficulty(0)|horse_speed(32)|horse_maneuver(33)|horse_charge(8)|horse_scale(79),imodbits_horse_basic],
    ["mulehorse", "Mule", [("mule", 0)], itp_merchandise|itp_type_horse, 0, 1050,abundance(60)|hit_points(65)|body_armor(10)|difficulty(0)|horse_speed(35)|horse_maneuver(35)|horse_charge(8)|horse_scale(86),imodbits_horse_basic],
]
