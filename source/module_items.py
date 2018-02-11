from .header_operations import *
from .header_common import *
from .header_items import *
from .header_item_modifiers import *
from .header_triggers import ti_on_missile_hit, ti_on_weapon_attack, ti_on_init_item

from . import module_items_shields, module_items_horses, module_items_footwear, module_items_headwear

# for the tutorial_shield
imodbits_shield = imodbit_cracked | imodbit_battered | imodbit_thick | imodbit_reinforced
####################################################################################################################
# Each item record contains the following fields:
# 1) Item id: used for referencing items in other files.
# The prefix itm_ is automatically added before each item id.
# 2) Item name. Name of item as it'll appear in inventory window
# 3) List of meshes. Each mesh record is a tuple containing the following fields:
#  3.1) Mesh name.
#  3.2) Modifier bits that this mesh matches.
# Note that the first mesh record is the default.
# 4) Item flags. See header_items.py for a list of available flags.
# 5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
# 6) Item value.
# 7) Item stats: Bitwise-or of various stats about the item such as:
# weight, abundance(60)fficulty, head_armor, body_armor,leg_armor, etc...
# 8) Modifier bits: Modifiers that can be applied to this item.
# 9) [Optional] Triggers: List of simple triggers to be associated with the item.
# 10) [Optional] Factions: List of factions that item can be found as merchandise.
# 11) [Optional] Factions ????????????????????????????????????????????????
####################################################################################################################
# blunt weapons 
#missingmeshespeasant_dressblue_new
# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_polearm_high = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_sword  = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high  = imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe  = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_axe_high  = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace  = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick  = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
#imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbits_sword_high
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbits_sword_high
imodbits_missile  = imodbit_bent | imodbit_large_bag
imodbits_thrown  = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good  = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad  = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

## CC distancia de tiro chief commander#gdw causing probelms?
missile_distance_trigger = [
 (ti_on_missile_hit, 
  [
 (store_trigger_param_1, ":shooter_agent"),
 
 (eq, "$g_report_shot_distance", 1),
 (get_player_agent_no, ":player_agent"),
 (try_begin),
  (eq, ":shooter_agent", ":player_agent"),
  (agent_get_position, pos2, ":shooter_agent"),
  (agent_get_horse, ":horse_agent", ":player_agent"),
  (try_begin),
   (gt, ":horse_agent", -1),
   (position_move_z, pos2, 220),
  (else_try),
   (position_move_z, pos2, 150),
  (try_end),
  (get_distance_between_positions, ":distance", pos1, pos2),
  (store_div, reg61, ":distance", 100),
  (store_mod, reg62, ":distance", 100),
  (try_begin),
   (lt, reg62, 10),
   (str_store_string, s1, "@{reg61}.0{reg62}"),
  (else_try),
   (str_store_string, s1, "@{reg61}.{reg62}"),
  (try_end),
  # (display_message, "@Shot distance: {s1} meters.", 0xCCCCCC), #hemos pues off chief porque igual es algo pesado.
 (try_end),
  ])]
## CC
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
 ["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],
 ["tutorial_spear", "Spear",  [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 , pierce),imodbits_polearm ],
 ["tutorial_club", "Club",  [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_axe1h, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 , pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe",  [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 , pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 1,weight(3)|abundance(60)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile,missile_distance_trigger],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(60)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile,missile_distance_trigger],
 ["tutorial_short_bow", "Short Bow",  [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 , pierce ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow",  [("crossbow",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)| shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers",  [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 , cut)|max_ammo(14)|weapon_length(0),imodbits_missile,missile_distance_trigger ],
 ["tutorial_saddle_horse", "Saddle Horse",  [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(60)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Round Shield",  [("leathershield_small_b",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff",  [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff",  [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
 ["tutorial_sword", "Sword",  [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 , pierce),imodbits_sword ],
 ["tutorial_axe", "Axe",  [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 , pierce),imodbits_axe ],
 ["tutorial_dagger","Dagger",  [("hunting_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],
 ["horse_meat","Horse Meat",  [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],

####################################################################################################################
# Items before this point are hardwired into the game and their order should not be changed!
####################################################################################################################

################## arena items ##################
["practice_sword","Practice Sword",  [("pattern_spatha",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 900 , weight(1.25)|difficulty(1)|spd_rtng(82) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(10 , pierce),imodbits_none ],
["practice_axe", "Long Hand Axe", [("le_werkaxt1",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_axe1h|itcf_carry_axe_left_hip,457 , weight(2)|difficulty(1)|spd_rtng(72) | weapon_length(80)|swing_damage(31 , pierce) | thrust_damage(0 , pierce),imodbits_axe ],
["practice_seaxe", "Arena Long Knife", [("langseax",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 900 , weight(1.25)|difficulty(0)|spd_rtng(82) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(10 , pierce),imodbits_sword_high ],
["practice_axe_two_handed", "War Axe", [("01tveirhendr_hedmarkox",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 620 , weight(3)|difficulty(1)|spd_rtng(71) | weapon_length(100)|swing_damage(42 , pierce) | thrust_damage(0 , pierce),imodbits_axe ],
["practice_sling",   "Arena fustibalus", [("05krokaspjott1",0)],itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 420 , weight(4)|abundance(60)|difficulty(1)|spd_rtng(92) | weapon_length(160)|swing_damage(16 , blunt) | thrust_damage(26 , pierce),imodbits_polearm ],
["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 180 , weight(2.25)|difficulty(1)|spd_rtng(82) | weapon_length(145)|swing_damage(15 , blunt) | thrust_damage(28 , blunt),imodbits_polearm],
["practice_spear","Practice Spear", [("05krokaspjott1",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 180 , weight(2.25)|difficulty(1)|spd_rtng(82) | weapon_length(145)|swing_damage(15 , blunt) | thrust_damage(28 , pierce),imodbits_polearm],
["practice_bow","Practice Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)],itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 267 , weight(1)|difficulty(0)|spd_rtng(70) | shoot_speed(45) | thrust_damage(14 , pierce)|accuracy(65),imodbits_bow ],
["practice_javelin_40amount", "Practice Javelinsavelinr", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 100, weight(2)|difficulty(0)|spd_rtng(60) | shoot_speed(28) | thrust_damage(21 , pierce)|max_ammo(6)|weapon_length(65),imodbits_thrown,missile_distance_trigger ],
["practice_javelin_40amount_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff, 100, weight(2)|difficulty(0)|spd_rtng(70) |swing_damage(4, cut)| thrust_damage(19, pierce)|weapon_length(65),imodbits_polearm ],
["throwing_axes_40amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(4, blunt)|max_ammo(40)|weapon_length(0),imodbits_thrown ],
["throwing_axes_40amount_melee", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(6, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown,missile_distance_trigger ],
["practice_arrows_75amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(75),imodbits_none],
["practice_slingrocks_100amount","Practice Lead Sling Stones", [("hunting_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_seax|itcf_carry_dagger_front_left, 60 , weight(0.5)|difficulty(0)|spd_rtng(97) | weapon_length(40)|swing_damage(11 , cut) | thrust_damage(11 , pierce),imodbits_none ],
["practice_arrows_100amount","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile,missile_distance_trigger],

["arena_shieldred", "Shield", [("ad_viking_shield_round_41",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 700 , weight(4.5)|hit_points(300)|body_armor(20)|spd_rtng(65)|shield_width(70)|difficulty(0),imodbits_shield ],
["arena_shieldblue", "Shield", [("leathershield_medium_b",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 700 , weight(4.5)|hit_points(300)|body_armor(20)|spd_rtng(65)|shield_width(70)|difficulty(0),imodbits_shield ],
["arena_shieldgreen", "Shield", [("ad_viking_shield_round_39",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 700 , weight(4.5)|hit_points(300)|body_armor(20)|spd_rtng(65)|shield_width(70)|difficulty(0),imodbits_shield ],
["arena_shieldyellow", "Shield", [("leathershield_medium_y",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 700 , weight(4.5)|hit_points(300)|body_armor(20)|spd_rtng(65)|shield_width(70)|difficulty(0),imodbits_shield ],
["arena_shieldwhite", "Shield", [("ad_viking_shield_round_21",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 700 , weight(4.5)|hit_points(300)|body_armor(20)|spd_rtng(65)|shield_width(70)|difficulty(0),imodbits_shield ],

# arena armor (only red used)
["arena_armor_red", "Arena Armor", [("arena_tunicR_new",0)], itp_type_body_armor |itp_covers_legs ,0, 600 , weight(4)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["arena_tunic_white", "Tunic White ", [("arena_tunicW_new",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 140 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(2), imodbits_cloth ],
["arena_tunic_red", "Tunic Red", [("arena_tunicR_new",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 140 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(2), imodbits_cloth ],#cambiado chief
["arena_tunic_blue", "Tunic Blue", [("arena_tunicB_new",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 140 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(2), imodbits_cloth ],#cambiado chief
["arena_tunic_green", "Tunic Green", [("arena_tunicG_new",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 140 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(2), imodbits_cloth ],#cambiado chief
["arena_tunic_yellow", "Tunic Yellow", [("arena_tunicY_new",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 140 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(2), imodbits_cloth ],#cambiado chief

# helms
["arena_helm_white", "Tourney Helm", [("Rathos_Spangenhelm_a",0)], itp_type_head_armor|itp_fit_to_head,0, 600 , weight(2)|abundance(60)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ], #cambiar chief
["arena_helm_red", "Tourney Helm", [("Rathos_Spangenhelm_a",0)], itp_type_head_armor|itp_fit_to_head,0, 600 , weight(2)|abundance(60)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ], #cambiar chief
["arena_helm_blue", "Tourney Helm", [("Rathos_Spangenhelm_a",0)], itp_type_head_armor|itp_fit_to_head,0, 600 , weight(2)|abundance(60)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ], #cambiar chief
["arena_helm_green", "Tourney Helm", [("Rathos_Spangenhelm_a",0)], itp_type_head_armor|itp_fit_to_head,0, 600 , weight(2)|abundance(60)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ], #cambiar chief
["arena_helm_yellow", "Tourney Helm", [("Rathos_Spangenhelm_yellow_plum",0)], itp_type_head_armor|itp_fit_to_head,0, 600 , weight(2)|abundance(60)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ], #cambiar chief
["arena_skullcap_red", "Capskull_cap_new_cd", [("skull_cap_new_c",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(60)|head_armor(9)|body_armor(0)|leg_armor(0), imodbits_plate ], #cambiar chief

################## Books ##################
# marked as books begin
["book_tactics","History of the Peloponnesian War (tactics)", [("book_a",0)], itp_type_book, 0, 4500,weight(2)|abundance(60),imodbits_none],
["book_persuasion","Rhetorica ad Herennium (persuasion)", [("book_b",0)], itp_type_book, 0, 4600,weight(2)|abundance(60),imodbits_none],
["book_leadership","The Life of Alexander the Great (leadership)", [("book_d",0)], itp_type_book, 0, 3780,weight(2)|abundance(60),imodbits_none], #cambiar chief
["book_intelligence","Paedeia (intelligence)", [("book_e",0)], itp_type_book, 0, 4500,weight(2)|abundance(60),imodbits_none],
["book_pathfinding","Guiding Pilgrim Travellers (pathfinding)", [("book_f",0)], itp_type_book, 0, 3600,weight(2)|abundance(60),imodbits_none],
["book_weapon_mastery", "Polity of the Lacedaemonians, of Xenofonte (weaponsmaster)", [("book_d",0)], itp_type_book, 0, 4500,weight(2)|abundance(60),imodbits_none],
["book_engineering","De architectura, of Vitrivius (engineering)", [("book_open",0)], itp_type_book, 0, 4500,weight(2)|abundance(60),imodbits_none],
["book_charisma","Motivational Daily Readings (charisma)", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(60),imodbits_none],
["book_surgery","Synopsis of Aelius Galenus (surgery)", [("book_c",0)], itp_type_book, 0, 3600,weight(2)|abundance(60),imodbits_none],
["book_training","Epitoma Rei Militaris (training)", [("book_open",0)], itp_type_book, 0, 3600,weight(2)|abundance(60),imodbits_none],
# Reference books (books that can give points by being in the inventory
# market as reference book begin
["book_wound_treatment_reference","De Materia Medica, of Dioscorides", [("book_c",0)], itp_type_book, 0, 3600,weight(2)|abundance(60),imodbits_none],
["book_looting_reference","Swords of King Arthur's Court", [("book_c",0)], itp_type_book, 0, 3600,weight(2)|abundance(60),imodbits_none],
["book_firstaid_reference","Convalescence shortened", [("book_c",0)], itp_type_book, 0, 3600,weight(2)|abundance(60),imodbits_none],
["book_trade_reference","Merchant's Ledger", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(60),imodbits_none],

#puesto chief quest
["book_slot","Read Latin Every Day to Remember", [("book_open",0)], itp_type_book, 0, 600,weight(2)|abundance(60),imodbits_none],#set to musketfor now#only available from abbots

["relic1","Vulgata Biblia", [("book_e",0)],itp_type_book, 0, 5500,weight(2)|abundance(60),imodbits_none],#type_book to prevent game from assignign at game start
["relic2","Slot for Relic2", [("book_e",0)], itp_type_book, 0, 5500,weight(2)|abundance(60),imodbits_none],#type_book to prevent game from assignign at game start
["relic3","Slot for Relic3", [("book_e",0)], itp_type_book, 0, 5500,weight(2)|abundance(60),imodbits_none],#type_book to prevent game from assignign at game start

################## Trade goods ##################
# market as trade good start
["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 800,weight(30)|abundance(60)|max_ammo(20),imodbits_none,[],jute_factions],
["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0, 300,weight(55)|abundance(60),imodbits_none,[],['fac_kingdom_6','fac_kingdom_4'],['fac_kingdom_16','fac_kingdom_9','fac_kingdom_11']],
["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 700,weight(50)|abundance(60)|max_ammo(20),imodbits_none,[],['fac_kingdom_8']],
["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 225,weight(50)|abundance(60),imodbits_none,[],['fac_kingdom_9','fac_kingdom_3'],['fac_kingdom_5','fac_kingdom_16','fac_kingdom_11','fac_kingdom_4','fac_kingdom_15','fac_kingdom_14']],
["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 200,weight(40)|abundance(60),imodbits_none,[],['fac_kingdom_4'],['fac_kingdom_17','fac_kingdom_5','fac_kingdom_19','fac_kingdom_27','fac_kingdom_28','fac_kingdom_29','fac_kingdom_30','fac_kingdom_31']],
["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0, 450,weight(40)|abundance(60),imodbits_none,[],['fac_kingdom_28'],['fac_kingdom_26','fac_kingdom_15','fac_kingdom_20']],
["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 225,weight(40)|abundance(60),imodbits_none,[],['fac_kingdom_14','fac_kingdom_19']],
["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 350,weight(40)|abundance(60),imodbits_none,[],['fac_kingdom_12','fac_kingdom_31']],
["rare_fabric","Italian Fabric", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0, 1000,weight(30)|abundance(60),imodbits_none,[],['fac_kingdom_16','fac_kingdom_9','fac_kingdom_11','fac_kingdom_15','fac_kingdom_14','fac_kingdom_20','fac_kingdom_18','fac_kingdom_13','fac_kingdom_12']],
["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 400,weight(10)|abundance(60),imodbits_none,[],['fac_kingdom_3','fac_kingdom_5','fac_kingdom_11','fac_kingdom_17','fac_kingdom_28','fac_kingdom_30']],
["velvet","Fine Cloth", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 650,weight(40)|abundance(60),imodbits_none,[],['fac_kingdom_1','fac_kingdom_2','fac_kingdom_3','fac_kingdom_5']],
["iron","Pig Iron", [("iron_bar",0)], itp_merchandise|itp_type_goods, 0,300,weight(60)|abundance(60),imodbits_none,[],['fac_kingdom_2','fac_kingdom_7','fac_kingdom_8','fac_kingdom_6','fac_kingdom_21','fac_kingdom_22','fac_kingdom_23','fac_kingdom_24','fac_kingdom_25','fac_kingdom_26','fac_kingdom_10']],
["mineral","Copper-Tin", [("ore_iron",0)], itp_merchandise|itp_type_goods, 0,150,weight(30)|abundance(60),imodbits_none,[],['fac_kingdom_27','fac_kingdom_28','fac_kingdom_29','fac_kingdom_30','fac_kingdom_31','fac_kingdom_17','fac_kingdom_6','fac_kingdom_7','fac_kingdom_8']],
["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0, 450,weight(50)|abundance(60),imodbits_none,[],['fac_kingdom_2','fac_kingdom_4','fac_kingdom_5','fac_kingdom_19','fac_kingdom_22','fac_kingdom_23','fac_kingdom_24','fac_kingdom_26','fac_kingdom_9','fac_kingdom_11']],
["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0, 300,weight(40)|abundance(60),imodbits_none,[],['fac_kingdom_12','fac_kingdom_13','fac_kingdom_18','fac_kingdom_20']],
["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 400,weight(30)|abundance(60),imodbits_none,[],['fac_kingdom_13','fac_kingdom_18','fac_kingdom_20','fac_kingdom_29']],
["jewelry","Gold", [("ore_gold",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 325,weight(30)|abundance(60)|food_quality(30)|max_ammo(50),imodbits_none ],
["silver","Silver", [("ore_silver",0)], itp_merchandise|itp_type_goods, 0, 475,weight(30)|abundance(60),imodbits_none,[],['fac_kingdom_6','fac_kingdom_7','fac_kingdom_8','fac_kingdom_21','fac_kingdom_22','fac_kingdom_23','fac_kingdom_24','fac_kingdom_25','fac_kingdom_26']],
["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 350,weight(40)|abundance(60),imodbits_none,[],['fac_kingdom_13','fac_kingdom_18','fac_kingdom_20']],
["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 400,weight(25)|abundance(60)|food_quality(10)|max_ammo(40),imodbits_none,[],['fac_kingdom_1','fac_kingdom_8']],
["ale","Beer", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 250,weight(30)|abundance(60)|food_quality(30)|max_ammo(50),imodbits_none,[],['fac_kingdom_4','fac_kingdom_9']],
["mead","Mead", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 325,weight(30)|abundance(60)|food_quality(30)|max_ammo(50),imodbits_none,[],['fac_kingdom_11','fac_kingdom_9','fac_kingdom_21','fac_kingdom_22','fac_kingdom_26','fac_kingdom_23','fac_kingdom_25','fac_kingdom_24','fac_kingdom_10']],
["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 90,weight(15)|abundance(60)|food_quality(50)|max_ammo(120),imodbits_none],
["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 100,weight(6)|abundance(60)|food_quality(40)|max_ammo(90),imodbits_none],
["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 225,weight(5)|abundance(60)|food_quality(40)|max_ammo(90),imodbits_none],
["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 60,weight(10)|abundance(60)|food_quality(40)|max_ammo(120),imodbits_none],
["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 40,weight(15)|abundance(60)|food_quality(40)|max_ammo(150),imodbits_none],
["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(15)|abundance(60)|food_quality(70)|max_ammo(150),imodbits_none],
["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(20)|abundance(60)|food_quality(40)|max_ammo(150),imodbits_none],
["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(60)|food_quality(10)|max_ammo(30),imodbits_none], #x2 for wine
["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 150,weight(40)|abundance(60)|food_quality(10)|max_ammo(30),imodbits_none], #x3 for oil
["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 20,weight(30)|abundance(60)|food_quality(40)|max_ammo(150),imodbits_none],
["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 125,weight(20)|abundance(60)|food_quality(80)|max_ammo(150),imodbits_none],
["bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(60)|food_quality(40)|max_ammo(150),imodbits_none],
["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 80,weight(10)|abundance(60)|food_quality(40)|max_ammo(150),imodbits_none],
["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 100,weight(15)|abundance(60)|food_quality(70)|max_ammo(150),imodbits_none],
["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 100,weight(6)|abundance(60)|food_quality(40)|max_ammo(90),imodbits_none],
# todo what are these for?
["itemslot1","ritemslot1", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 100,weight(6)|abundance(60)|food_quality(40)|max_ammo(90),imodbits_none],
["itemslot2","ritemslot2", [("jug",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 100,weight(6)|abundance(60)|food_quality(40)|max_ammo(90),imodbits_none],

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting chief Mod begin#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
["deer_meat","Venison", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(30)|abundance(60)|food_quality(40)|max_ammo(30),imodbits_none],
["boar_meat","Boar Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 175,weight(30)|abundance(60)|food_quality(80)|max_ammo(50),imodbits_none],
["wolf_meat","Wolf Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(60)|food_quality(30)|max_ammo(50),imodbits_none],
["goat_meat","Goat Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 125,weight(30)|abundance(60)|food_quality(30)|max_ammo(50),imodbits_none],
["goatb_meat","Mutton Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 100,weight(30)|abundance(60)|food_quality(30)|max_ammo(50),imodbits_none],
["wilddonkey_meat","Wild Donkey Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 200,weight(30)|abundance(60)|food_quality(30)|max_ammo(50),imodbits_none],
["unassigned_meat","Wild Donkey Meat", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 200,weight(30)|abundance(60)|food_quality(30)|max_ammo(50),imodbits_none],

################## Other goods ##################
# market as the goods end
["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(60),imodbits_none],

["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
]

items += module_items_horses.items

items += [

################## Horses end ##################
# marked as horses end
["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_new",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("pil_hood",0)], 0| itp_type_head_armor |itp_civilian ,0, 35 , weight(1.25)|abundance(60)|head_armor(4)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

################## armor begin ##################
# handwear
# marked as armor begin
["leather_gloves1","Leather Gloves", [("leather_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 190, weight(0.25)|abundance(60)|body_armor(10)|difficulty(0),imodbits_cloth],
["coarse_gloves","Coarse Gloves", [("wantus1_L",0)], itp_merchandise|itp_type_hand_armor,0, 190, weight(0.25)|abundance(60)|body_armor(5)|difficulty(0),imodbits_cloth],
["lamellar_arm_gloves","Light Archer Gauntlets", [("scale_gauntlets_a_L",0)], itp_unique|itp_type_hand_armor,0, 800, weight(1.5)|abundance(60)|body_armor(13)|difficulty(0),imodbits_armor,[], ['fac_merc1']],
["scale_arm_gloves","rScale_Arm_Gauntlets", [("scale_gauntlets_b_L",0)], itp_unique|itp_type_hand_armor,0, 800, weight(1.5)|abundance(60)|body_armor(17)|difficulty(0),imodbits_armor,[], ['fac_merc1']],
["mail_gloves","reservCoarse Gloves", [("gauntlets_Lx",0)], itp_type_hand_armor,0, 190, weight(0.25)|abundance(60)|body_armor(12)|difficulty(0),imodbits_cloth,[], ['fac_merc2']],
["slot_gloveselite","slotCoarse Gloves", [("gauntlets_L",0)], itp_type_hand_armor,0, 190, weight(0.25)|abundance(60)|body_armor(12)|difficulty(0),imodbits_cloth],
# handwear ends
]

items += module_items_footwear.items

items += [

# pick
["richlong_tunic1", "Long Tunic", [("outaa1",0)], itp_merchandise |itp_type_body_armor |itp_covers_legs|itp_civilian,0, 560 , weight(1)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(4), imodbits_cloth ,[], pict_factions + irish_factions],
["richlong_tunic2", "Long Tunic", [("outaa2",0)], itp_merchandise |itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 560 , weight(1)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(4), imodbits_cloth ,[], pict_factions + irish_factions],
["richlong_tunic3", "Long Tunic", [("outaa3",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 560 , weight(1)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(4), imodbits_cloth ,[], pict_factions + irish_factions],
["richlong_tunic4", "Long Tunic", [("outaa4",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 560 , weight(1)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(4), imodbits_cloth ,[], pict_factions + irish_factions],
# irish
["courtly_outfit", "Long Tunic", [("merchant_outf1",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 430 , weight(1)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(4), imodbits_cloth ,[], pict_factions + irish_factions],
["nobleman_outfit", "Long Tunic", [("merchant_outf2",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 430 , weight(1)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(4), imodbits_cloth ,[], pict_factions + irish_factions],

# merchants
["merch_tunicwt", "Merchant White Tunic", [("coarse_tunic_wt",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["merch_tunicred", "Merchant Red Tunic", [("coarse_tunic_rd",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["merch_tunicgreen", "Merchant Green Tunic", [("coarse_tunic_verde",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 800 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["merch_tunicbrownt2", "Merchant Rawhide Tunic", [("coarse_tunic_brn",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["merch_tunicolive", "Merchant Green Tunic", [("coarse_tunic_grn",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(3), imodbits_cloth ],
["merch_furjacketwhite", "Fur Jacket", [("idi_furjacket1",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(3)|abundance(60)|head_armor(0)|body_armor(19)|leg_armor(4)|difficulty(4) ,imodbits_cloth ],
["merch_furjacket2t3", "Fur Jacket", [("idi_furjacket2",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(3)|abundance(60)|head_armor(0)|body_armor(19)|leg_armor(4)|difficulty(4) ,imodbits_cloth ],
["merch_furjacketblue", "Fur Jacket", [("idi_furjacket4",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(3)|abundance(60)|head_armor(0)|body_armor(19)|leg_armor(4)|difficulty(4) ,imodbits_cloth ],
["merch_furjacket6t3", "Fur Jacket", [("idi_furjacket6",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(3)|abundance(60)|head_armor(0)|body_armor(19)|leg_armor(4)|difficulty(4) ,imodbits_cloth ],
["merch_furjacketyelo", "Fur Jacket", [("idi_furjacket5",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(3)|abundance(60)|head_armor(0)|body_armor(19)|leg_armor(4)|difficulty(4) ,imodbits_cloth ],
["wealthytunic5", "Long Tunic", [("merchant_outf5",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 430 , weight(1)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(4), imodbits_cloth ,[], pict_factions + irish_factions],
["leather_aprontunic", "Leather Apron", [("leather_apron",0)], itp_type_body_armor|itp_attach_armature|itp_civilian |itp_covers_legs ,0,161 , weight(3)|abundance(60)|head_armor(0)|body_armor(3)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],

# ####sacerdotes

# ###robes derivadas de la sarranida, para comerciantes y village elders 
["blackwornrobe", "Worn Robe", [("sar_robegrn",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs ,0, 363 , weight(1)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["blackwht_robe", "Worn Robe", [("sar_robeylw",0)], itp_type_body_armor |itp_covers_legs ,0, 363 , weight(1)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["slotfor_robewht", "slotblackwornrobe", [("sar_robewht",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs ,0, 363 , weight(1)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["robe_darkprp", "Worn Robe", [("sar_robeprp",0)], itp_type_body_armor |itp_covers_legs ,0, 363 , weight(1)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["robe2", "drobe_beige", [("sar_robewht",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs ,0, 363 , weight(1)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
#robes chief acaba

# pagans
["robe_beige", "Worn Robe", [("sar_robe_bbge",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0, 363 , weight(1)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["robe1", "Robe", [("sar_robered",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0, 363 , weight(1)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],

# christians
["monk_robe", "Monk Robe", [("priest_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 170 , weight(4)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["bishop_robe1", "Bishop Robe", [("priest_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 975 , weight(5)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["bishop_robe2", "Bishop Robe", [("priest_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 975 , weight(5)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["bishop_robe3", "Bishop Robe", [("priest_3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 975 , weight(5)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],

# celts
["white_robe", "White Worn Robe", [("sarranid_jellaba_white",0)], itp_type_body_armor |itp_covers_legs ,0, 363 , weight(1)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
#irishrobe
["robe_jellablue", "Blue Worn Robe", [("sarranid_jellaba_blue",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs ,0,
 363 , weight(1)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(4)|difficulty(0) ,imodbits_cloth ,
[], pict_factions + irish_factions],
# others
["pocketed_robe", "Galeno's Tunic", [("surgeon",0)], itp_type_body_armor |itp_covers_legs ,0, 397 , weight(7)|abundance(60)|head_armor(0)|body_armor(7)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],

# Tunics

# Britons
["cloaked_tunic1", "Cloaked Tunic", [("BL_NT_Blue06COAT",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,[], pict_factions + irish_factions],
["cloaked_tunic2", "Cloaked Tunic", [("BL_NT_Green11COAT",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,[], pict_factions + irish_factions],
["cloaked_leathertunict2", "Cloaked Tunic", [("BL_NT_Red12COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,[], pict_factions + irish_factions],
# picts
["cloaked_tunicwhite", "Cloaked Tunic", [("BL_NT_Blue04COAT",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,[], pict_factions + irish_factions],
["cloaked_tunic3", "Cloaked Tunic", [("BL_NT_Blue08COAT",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,[], pict_factions + irish_factions],
["cloaked_tunicblue", "Cloaked Tunic", [("BL_NT_Red04COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,[], pict_factions + irish_factions],
# irish
["cloaked_tunicorange", "Cloaked Tunic", [("BL_NT_Blue11COAT",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,[], pict_factions + irish_factions],
["cloaked_tunicgreen", "Cloaked Tunic", [("BL_NT_Green10COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 400 , weight(2)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,[], pict_factions + irish_factions],

# picts and irish
["wessex_tunic1", "Red Tunic", [("BL_NT_Red04",0)],itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 210 , weight(2)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,[], pict_factions + irish_factions],
["german_tunica", "Woolen Tunic", [("woolen_tunic_a",0)],itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 210 , weight(2)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,[], pict_factions + irish_factions],
["german_tunic5", "Woolen Tunic ", [("woolen_tunic_c",0)],itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 210 , weight(2)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,[], pict_factions + irish_factions],

["saxon_tunic7", "Short Tunic ", [("BL_NT_Green03",0)], itp_merchandise|itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 210 , weight(2)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,[], pict_factions + irish_factions],
["briton_tunic2", "Cloak Dirty Tunic", [("BL_TunicR02_2",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ,[], saxon_factions + jute_factions + engle_factions],
["german_tunic3", "Cloak Red Tunic", [("BL_TunicR03",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ,[], saxon_factions + jute_factions + engle_factions],
["german_tunic2", "Red Tunic", [("BL_TunicR03_2",0)],itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ,[], saxon_factions + jute_factions + engle_factions],

# simple tunic for everyone
["ptunicwhite", "Poor Shirt", [("roman_shirt",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian ,0,110 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],
["ptunic1", "Poorman Tunic", [("BL_TunicR01",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],
["ptunic2", "Dirty Tunic", [("BL_TunicR02",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],
["ptunic3", "Green tunic", [("shirtb",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],
["ptunic4", "White tunic", [("shirtc",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],
["ptunic5", "Poor Tunic", [("shirt_a_bry",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],
["ptunic6","Cloak Poorman Tunic", [("BL_TunicR01_2",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],

# irish and
["ptunic7", "Poor Irish Tunic", [("koszula_gaelicka",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth,[], pict_factions + irish_factions],
#Quest-specific - perhaps can be used for prisoners, 
["ptunic8", "Burlap Tunic", [("shirt",0)], itp_type_body_armor |itp_covers_legs ,0,
 25 , weight(1)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(1)|difficulty(0) ,imodbits_armor ],
["ptunic9", "Narrow Tunic", [("armor_9",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ],
["ptunic10", "slotictish Tunic", [("shirte",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], pict_factions], 
["ptunic11", "Arena Fan Jersey", [("arena_tunicY_new",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],
#lowerclass anywhere
["ptunic12", "Poorman tunic", [("fattiglinenskjortir",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions], 
["ptunic13", "Rustic Engle Tunic", [("BL_TunicLeather",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions],
["ptunic14", "Rustic Engle Tunic", [("BL_TunicLeather_2",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions],
["ptunic15", "Cloak Engle Rustic Tunic", [("BL_TunicLeather_3",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions],
["ptunic16", "poor tunic slot", [("arena_tunicB_new",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],

#peasant con capucha britones, e invadores
["peasant_archertunic", "Farmer tunic", [("peasant_archer",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["farmertunic26", "Farmer tunic", [("armor_26",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
#["farmertunic26", "Farmer tunic", [("armor_27",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["peasant_ctunic", "Farmer tunic", [("peasant_man_c",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["peasant_dtunic", "Farmer tunic", [("peasant_man_d",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["peasant_etunic", "Farmer tunic", [("peasant_man_e",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["peasant_ftunic", "Farmer tunic", [("peasant_man_f",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["tunicblue8", "Blue Tunic", [("armor_8",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 200 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth],


###clase alta o elite pictos o irlandeses
 #clase alta, tunicas de cuadros con capas atras
#pictos
["brazpicttunic", "Long Pictish Tunic", [("braz",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], pict_factions],
["czerwonypicttunic", "Pictish Tunic", [("czerwony",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], pict_factions],
["ladytunicgodelic", "Pictish Tunic", [("vaelicus_t_5",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], pict_factions],
#["striped_tunic26", "Pictish Tunic", [("striped_tunic26",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
#[], pict_factions],
#["ladytunicgodelic", "Pictish Tunic", [("vaelicus_t_5",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
#[], pict_factions],
["yellowtunic1", "Pictish Tunic", [("vaelicus_t_9",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], pict_factions],
["pict_tunicc", "Pictish Tunic", [("byrnie_a_tunic_c",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], pict_factions],
#irlandeses
["byrnietunica", "Godelic Tunic", [("byrnie_a_tunic",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], irish_factions],
["byrnietunicb", "Godelic Tunic", [("byrnie_a_tunic_b",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], irish_factions],
#["vaelicus_tunic27", "Godelic Tunic", [("vaelicus_t_21",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
#[], irish_factions],
["byrnietunice", "Godelic Tunic", [("byrnie_a_tunic_e",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], irish_factions],
["striped_tunic26", "Godelic Tunic", [("vaelicus_t_26",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], irish_factions],
["vaelicus_tunic27", "Godelic Tunic", [("vaelicus_t_27",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 510 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth,
[], irish_factions],
#con pelo
["vaelicus_tunic35", "Godelic Fur Tunic", [("vaelicus_t_35",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 620 , weight(1)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(3), imodbits_cloth,
[], irish_factions],
["vaelicus_tunic36", "Godelic Fur Tunic", [("vaelicus_t_36",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 620 , weight(1)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(3), imodbits_cloth,
[], irish_factions],


# #Tunica abierta arriba, clase media y baja
# #irlandeses#these look just like pictishtunics
#["tunica", "Godelic Tunic", [("tunic_a",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
#[], irish_factions],
#chief irlandeses gaelic jacket, es del siglo VIII o IX asi que usar muy poco, para algun personaje secundario
["gaelic_jacketgrn", "Green Godelic Jacket", [("c_gaelic_jacket",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 300 , weight(4)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,
[], irish_factions],
["gaelic_jacketgray", "Grey Godelic Jacket", [("b_gaelic_jacket",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 300 , weight(4)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(2)|difficulty(0) ,imodbits_cloth ,
[], irish_factions],


["tunicsleevelessc", "Godelic Tunic", [("tunic_c",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], irish_factions],
["tunicsleeveless3", "Godelic Tunic", [("vaelicus_tunic_3",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], irish_factions],
["tunicsleeveless6", "Godelic Tunic", [("vaelicus_tunic_6",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], irish_factions],
["tunicsleeveless8", "Godelic Tunic", [("vaelicus_tunic_8",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], irish_factions],
#["tunicsleeveless8", "Godelic Tunic", [("vaelicus_tunic_9",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
#[], irish_factions],
#Pictos
["tunicsleevelessb", "Pictish Tunic", [("tunic_b",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], pict_factions],
["tunicsleevelessred1", "Pictish Tunic", [("vaelicus_tunic_1",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], pict_factions],
["tunicsleeveless2", "Pictish Tunic", [("vaelicus_tunic_2",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], pict_factions],
#["tunicsleevelessred1", "Pictish Tunic", [("vaelicus_tunic_4",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
#[], pict_factions],
["tunicsleevelessgreenred", "Pictish Tunic", [("vaelicus_tunic_5",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], pict_factions],
["tunicsleevelessgreen7", "Pictish Tunic", [("vaelicus_tunic_7",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
[], pict_factions],

#["ptunic10", "dPictish Tunic", [("vaelicus_tunic_12",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 240 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(4), imodbits_cloth,
#[], pict_factions],
#clase media alta irlandesa
 ["bltunic05", "Godelic Rich Tunic", [("BL_Tunic05",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], pict_factions + irish_factions],
 ["bltunic06", "Godelic Rich Tunic", [("BL_Tunic06",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], pict_factions + irish_factions],
 ["bltunic07", "Godelic Rich Tunic", [("BL_Tunic07",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], pict_factions + irish_factions],
 ["bltunic08", "Godelic Rich Tunic", [("BL_Tunic08",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], pict_factions + irish_factions],
 ["bltunic11", "Godelic Rich Tunic", [("BL_Tunic11",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], pict_factions + irish_factions],


#britones
 #clase media
["leather_tunic1", "Leather tunic", [("ragged_leather_jerkin",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 320 , weight(1)|abundance(60)|head_armor(0)|body_armor(11)|leg_armor(2), imodbits_cloth ],
["shirtblue", "Blue Tunic", [("shirt_blu",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], briton_factions],
["shirtgreen", "Green Tunic", [("shirt_grn",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], briton_factions],
["shirtylw", "Yellow Tunic", [("shirt_ylw",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], briton_factions],
["shirtaqua", "Briton Tunic", [("shirt_tel",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], briton_factions],
["shirtgrey", "Briton Tunic", [("shirt_blk",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], briton_factions],
["bltunicgrn", "Briton Green Tunic", [("BL_Tunic02",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], briton_factions],


#elite o alta
["shirtred", "Red Tunic", [("shirt_red",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], briton_factions],
["bltunic01", "Rich Blue Tunic", [("BL_Tunic01",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], briton_factions],
["bltunic04", "Fancy Rich Tunic", [("BL_Tunic04",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], briton_factions],
["bltunic09", "Rich Red Tunic", [("BL_Tunic09",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], briton_factions],
["bltunic10", "Rich Blue Tunic", [("BL_Tunic10",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], briton_factions],
 
##invasores####
#clase baja
 
["mercia_tunicgrn", "Mercia Tunic", [("BL_NT_Green01",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions],
["blue_shorttunic", "Short Tunic", [("BL_NT_Blue01",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions],
["wessex_tunic3", "Saxon Tunic", [("BL_NT_Red01",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions], 
 ###clase media
["bl_tunicred", "Red Tunic", [("BL_Tunic03",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions],
 ["bluenorthmanshirt", "Blue Shirt", [("bluevikingshirt",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions],
 ["rednorthmanshirt", "Linen Shirt", [("redvikingshirt",0)],itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions],
["blue_shorttunic2", "Linen Tunic", [("linen_tunic_a",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions],
["mercia_tunic10", "Linen Tunic", [("linen_tunic_b",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions],
["wessex_tunic4", "Linen Tunic", [("linen_tunic_c",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions],
["redtunic", "Woolen Tunic", [("woolen_tunic_b",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 210 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(2), imodbits_cloth ,
[], saxon_factions + jute_factions + engle_factions],
#usamos tb: arena_tunic_red, arena_tunic_blue,arena_tunic_green,arena_tunic_yellow (son tunicas para clase media o alta)
#clase alta

#tunicas cortas finales acaba###############
 ############################################
#  ["lamellarpurplereserv", "bronze Lamellar Armor", [("BL_Lamellar06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3510 , weight(10)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(5)|difficulty(10) ,imodbits_armor,
# [], jute_factions + saxon_factions],
#  #["mail_hauberkredt3", "Long Mail Coat", [("mail_hauberk_jco",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 8000 , weight(23)|abundance(60)|head_armor(0)|body_armor(49)|leg_armor(23)|difficulty(13) ,imodbits_armor,
#  #[], pict_factions + irish_factions],
# #["mailtunic_blue1res", 
# #["mailshirt_purpleunder", "Blue Short Mail", [("norman_short_hauberk_blue",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4540 , weight(21)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(6)|difficulty(12) ,imodbits_armor,
#  #[], saxon_factions + jute_factions + engle_factions],
#  ["lorica_ltred", "Blue Lorica", [("byrnie3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
#  [], saxon_factions + jute_factions + engle_factions],
#  ["lorica_bluered", "Blue Lorica", [("byrnie13",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
#  [], saxon_factions + jute_factions + engle_factions],
#  ["mail_long_tunic", "Long Mail Tunic", [("armor_11",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5600 , weight(22)|abundance(60)|head_armor(0)|body_armor(55)|leg_armor(20)|difficulty(14) ,imodbits_armor,
#  [], pict_factions + irish_factions],
#  ["lorica_whitered", "White Lorica", [("byrnie16",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(4)|difficulty(11) ,imodbits_armor,
#  [], saxon_factions + jute_factions + engle_factions],
######vestuario mujeres chief finales
 #mujeres todas las razas plebeyas campesinas, villages
["blue_long_dress", "Long Dress", [("vae_tunica_larga5",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], pict_factions + irish_factions],
["lady_dress_ruby", "Long Shirt", [("vae_tunica_larga6",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], pict_factions + irish_factions],
["woolen_dressplain", "Woolen Dress", [("woolen_dress",0)],  itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 130 , weight(1)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(2)|difficulty(0) ,imodbits_cloth ], 
["peasant_dressblue", "Woman Dress", [("peasant_dress_b_new",0)],  itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 130 , weight(1)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(2)|difficulty(0) ,imodbits_cloth ], 

########mujeres####################
#tunicas largas pictos mujeres plebeyas campesinas
#["lady_dress_blue", "Long Shirt", [("vae_tunica_larga5",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
#[], pict_factions + irish_factions],
["gaelic_long_dress", "Long Shirt", [("vae_tunica_larga1",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], pict_factions + irish_factions],
["gaelic_long_dress2", "Long Shirt", [("vae_tunica_larga2",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], pict_factions + irish_factions],
["gaelic_long_dress3", "Long Shirt", [("vae_tunica_larga3",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], pict_factions + irish_factions],
["gaelic_long_dress4", "Long Shirt", [("vae_tunica_larga4",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], pict_factions + irish_factions],
["lady_dress_green", "Long Shirt", [("vae_tunica_larga7",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], pict_factions + irish_factions],
["lady_dress_blue", "Long Shirt", [("vae_tunica_larga8",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 150 , weight(1)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(3), imodbits_cloth,
[], pict_factions + irish_factions],

##Wealthy dress tunics
["blue_linendress", "Long Tunic", [("shirt_shirt_a",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 430 , weight(1)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(4), imodbits_cloth ,
[], pict_factions + irish_factions],
["white_linendress", "Long Tunic", [("shirt_shirt_c",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 430 , weight(1)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(4), imodbits_cloth ,
[], pict_factions + irish_factions],

#todas las razas, veils para cabezas
#simple
["veila", "Pink Veil", [("veil_a",0)], itp_type_head_armor |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veilb", "Blue Veil", [("veil_b",0)], itp_type_head_armor | itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veild", "Wool Veil", [("veil_d",0)], itp_type_head_armor | itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veilc", "Dark Blue Veil", [("veil_c",0)], itp_type_head_armor |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veile", "White Veil", [("veil_e",0)], itp_type_head_armor |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veilf", "Green Veil", [("veil_f",0)], itp_type_head_armor |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["veilg", "Grey Veil", [("veil_g",0)], itp_type_head_armor |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#el amplio , senoras
#["commonveil_a", "Veil", [("common_veil_a",0)], itp_type_head_armor |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["commonveil_b", "Grey Veil", [("common_veil_b",0)], itp_type_head_armor |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["commonveil_d", "Narrow Veil", [("common_veil_d",0)], itp_type_head_armor |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#["commonveil_c", "Orange Veil", [("common_veil_c",0)], itp_type_head_armor |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["commonveil_e", "Wool Veil", [("common_veil_e",0)], itp_type_head_armor |itp_civilian |itp_attach_armature,0, 100 , weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#mujeres cabeza campesinas irlandesas
["wimplea", "Wimple", [("wimple_a_new_bry",0)],itp_type_head_armor|itp_civilian|itp_fit_to_head,0,90, weight(0.5)|abundance(60)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["wimple_with_veil", "Wimple with Veil", [("wimple_b_new_bry",0)],itp_type_head_armor|itp_civilian|itp_fit_to_head,0,90, weight(0.5)|abundance(60)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

#britonas
["red_dress", "briton_dress", [("briton_dress",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["brown_dress", "Blue Dress", [("briton_dress_b",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["green_dress", "Wool Dress", [("briton_dress_c",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["briton_dress_blue", "briton_dress_dWoman Dress", [("briton_dress_d",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["briton_dress_grey", "briton_dress_eWoman Dress", [("briton_dress_e",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],

#nobles mujeres invasoras
["kentdress", "Woman Dress", [("kenttunik",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["kentdresswvest", "Woman Dress", [("tunikwjac1",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],

#pictas e irlandesas
["longdressaqua", "Woman Dress", [("pictishdressazul",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["longdressltblue", "Woman Dress", [("pictishdress2",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["longolivedress", "Woman Dress", [("pictishdress3",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["fancyplaidprpldress", "Woman Dress", [("pictishdress1",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["plaidgreendress", "Woman Dress", [("pictishdressverde",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["plaidbluedress", "Woman Dress", [("pictishdress",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
####mujeres ropa acaba############
 #####################################
 
#Pictos

#####desnudos pictos finales#############
 ###########################################
["war_paintbody_two", "Pictish naked", [("war_paint_two",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintbodyus", "Pictish naked", [("war_paintus",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintbody1", "Pictish naked", [("BL_Body08_male",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintbody2", "Pictish naked", [("2celtbody",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 10 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(8)|leg_armor(2), imodbits_cloth ],
["war_paintbody3", "Pictish naked", [("3celtbody",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 40 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(9)|leg_armor(3), imodbits_cloth ],
#["war_paintbody5", "Pictish naked", [("5celtbody",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintbody4", "Pictish naked", [("BL_Body01_male",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintbody5", "Pictish naked", [("BL_Body02_male",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintbody6", "Pictish naked", [("6celtbody",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintbody7", "Pictish naked", [("BL_Body03_male",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
#["war_paintbody4", "Pictish naked", [("war_paintus_3",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintbody8", "Pictish naked", [("war_paintus_4",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 450 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(8), imodbits_cloth ],
#["war_paintbody_07", "Pictish naked", [("BL_Body04_male",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintbody9", "Pictish naked", [("BL_Body07_male",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 400 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(13)|leg_armor(7), imodbits_cloth ],
["war_paintbody10", "Pictish naked", [("war_paintus_7",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 300 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(6), imodbits_cloth ],
["war_paintbody11", "Pictish naked", [("war_paintus_8",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintbody12", "Pictish naked", [("war_paintus_10",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintbody13", "Pictish naked", [("war_paintus_11",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["war_paintbody14t2", "Pictish naked", [("BL_Body09_male",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 350 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(7), imodbits_cloth ],
#gordos
["picto_paintfat1", "Big Pictish naked", [("picto_gordo1",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["picto_paintfat2", "Big Pictish naked", [("picto_gordo2",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
#["picto_paintfat3", "Big Pictish naked", [("picto_gordo3",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
#mujeres
["pictpaintfemale1", "Pictish woman naked", [("picta1",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["pictpaintfemale2", "Pictish woman naked", [("picta2",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["pictpaintfemale3", "Pictish woman naked", [("picta3",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
["pictpaintfemale4", "Pictish woman naked", [("picta4",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
#["pictpaintfemale5", "Pictish woman naked", [("picta1",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
#["pictpaintfemale6", "Pictish woman naked", [("picta2",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
#["pictpaintfemale7", "Pictish woman naked", [("picta3",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
#["pictpaintfemale8", "Pictish woman naked", [("picta4",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
#["pictpaintfemale9", "Pictish woman naked", [("picta3",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],
#["pictpaintfemale3t2", "Tier2 Pictish woman paint", [("picta4",0)],itp_no_pick_up_from_ground|itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(5), imodbits_cloth ],


#pictos desnudos con capa y pantalon (pictos)
["celtcloakedbody01", "Cloaked Body", [("BL_Celts01COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 180 , weight(5)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["celtcloakedbody02", "Cloaked Body", [("BL_Celts02COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 180 , weight(5)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["celtcloakedbody03", "Cloaked Body", [("BL_Celts05COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 180 , weight(5)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#["celtcloakedbody04", "Cloaked Body", [("BL_Celts04COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 180 , weight(5)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#["celtcloakedbody04", "dCloaked Body", [("BL_Celts03COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 180 , weight(5)|abundance(60)|head_armor(0)|body_armor(5)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#irlandeses 
["celtcloakedbody06", "Cloaked Body", [("BL_Celts06COAT",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 900 , weight(5)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
 [], pict_factions + irish_factions],
["celtcloakedbodyred", "Cloaked Body Red pants", [("BL_Celts07COAT",0)],itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 900 , weight(5)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
 [], pict_factions + irish_factions],
#["celtcloakedbody08", "Cloaked Body", [("BL_Celts08COAT",0)],itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 880 , weight(5)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(6)|difficulty(0) ,imodbits_cloth,
 #[], pict_factions + irish_factions],
#chief acaba

#pantalones sin camisa chief, irlandeses
#["coat", "Green Pants", [("BL_Celts06",0)], itp_type_body_armor |itp_covers_legs ,0, 400 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth,
# [], pict_factions + irish_factions],
#["red_pantsbody07", "Red Pants", [("BL_Celts07",0)], itp_type_body_armor |itp_covers_legs ,0, 400 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth,
# [], pict_factions + irish_factions],
#["bluepantsbody_08", "Blue Pants", [("BL_Celts08",0)], itp_type_body_armor |itp_covers_legs ,0, 400 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth,
# [], pict_factions + irish_factions],

#pantalones con pintura, pictos 
["bluepantsbody_woad05", "Blue Pants", [("BL_Celts05",0)], itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["bluepantsbody_woad04", "Red Pants", [("BL_Celts04",0)], itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["greenpantsbody_woad03", "Blue Pants", [("BL_Celts03",0)], itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["bluepantsbody_woad02t2", "Blue Pants", [("BL_Celts02",0)], itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["greypantsbody_woad01", "Narrow Pants", [("BL_Celts01",0)], itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["blackpantsbody_woad10", "Blue Pants", [("BL_Celts10",0)], itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["redpantsbody_woad11", "Red Pants", [("BL_Celts11",0)], itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],
["bluepantsbody_woadhvy12t2", "Blue Pants", [("BL_Celts12",0)], itp_type_body_armor |itp_covers_legs ,0, 100 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(6), imodbits_cloth ],

################desnudos pictos finales#####################
 ###############################################################



##############ROPA acaba chief #############################################################

 
############# ARMOR armadura chief finales empieza ###############################################
###################################################################################################




#tunicas con capa para nobles
["noblearmor1res", "Purple Nobleman Girded Tunic p", [("nordiclightarmor65",0)], pnbl,0,1450,weight(6.5)|abundance(60)|head_armor(5)|body_armor(23)|leg_armor(5)|difficulty(8),imodbits_cloth,
[],mercenary_factions],
["noblearmor2res", "Purple Warrior Jacket p", [("kaftang",0)],pnbl,0, 1930,weight(5)|abundance(60)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(4),imodbits_cloth,
[],mercenary_factions],
["noblearmor3res","Blue Noble Mail p", [("BL_VikingByrnie03",0)],pnbl,0,6320,weight(21)|abundance(60)|head_armor(0)|body_armor(56)|leg_armor(8)|difficulty(13),imodbits_armor,
[],mercenary_factions],
["noblearmor4res", "Roman Purple Tunic p", [("romantunic_purple",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,1060,weight(2)|abundance(60)|head_armor(0)|body_armor(12)|leg_armor(3)|difficulty(0),imodbits_cloth,
[],mercenary_factions],
 ##heavy armors
["noblearmor5res", "Bronze Lamellar Tunic purple tunic p", [("BL_Lamellar06",0)],pnbl,0,4010,weight(10)|abundance(60)|head_armor(0)|body_armor(35)|leg_armor(4)|difficulty(9),imodbits_armor,
[],mercenary_factions],
["noblearmor6res", "White Clk Long Mail Tunic p", [("armor_11",0)],pnbl,0,6990,weight(22)|abundance(60)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(12),imodbits_armor,
[],mercenary_factions],
["noblearmor7res","Purple Dark p", [("norman_short_hauberk_blue",0)], pnbl,0,4590,weight(18)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(10)|difficulty(12),imodbits_armor,
[],mercenary_factions],
["noblearmor8res","Long Mail Coat Silver thread red clk p", [("mail_hauberk_jco",0)],pnbl,0,8000,weight(23)|abundance(60)|head_armor(0)|body_armor(55)|leg_armor(20)|difficulty(12),imodbits_armor,
[],mercenary_factions],
 ##################nextpage
["noblearmor9res", "Purple Noble Mail Elk cloak p", [("BL_VikingByrnie14",0)],pnbl,0,7390,weight(20)|abundance(60)|head_armor(6)|body_armor(54)|leg_armor(8)|difficulty(12),imodbits_armor,
[],mercenary_factions],
["noblearmor10res","Purple Noble Mail Red Cloak p", [("BL_VikingByrnie05",0)],pnbl,0,7390,weight(20)|abundance(60)|head_armor(6)|body_armor(54)|leg_armor(8)|difficulty(12),imodbits_armor,
[],mercenary_factions],
["noblearmor11res","Frankish Purple Lorica p", [("byrnie_c_new",0)],pnbl,0,4900,weight(16)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(5)|difficulty(8),imodbits_cloth,
[],mercenary_factions],
["noblearmor12res", "Blue Mail Coat p", [("wei_xiadi_sar_hauberk",0)],pnbl,0,7900,weight(19)|abundance(60)|head_armor(0)|body_armor(48)|leg_armor(11)|difficulty(10),imodbits_armor,
[],mercenary_factions],
["noblearmor13res", "White Blessed Mail Coat p", [("mail_shirt_wht",0)],pnbl,0,9060,weight(24)|abundance(60)|head_armor(7)|body_armor(54)|leg_armor(15)|difficulty(12),imodbits_armor,
[],mercenary_factions],
["noblearmor14res","RedLorica p",[("byrnie3",0)],pnbl,0,4400,weight(16)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(5)|difficulty(11),imodbits_armor,
[],mercenary_factions],
["noblearmor15res", "Blue Lorica p", [("byrnie13",0)],pnbl,0,4440,weight(16)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(5)|difficulty(11),imodbits_armor,
[],mercenary_factions],
["noblearmor16res","Byzantine Armor p",[("khergit_scale_a",0)],pnbl,0,5630,weight(12)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(10),imodbits_armor,
[],mercenary_factions + other_mercenary_factions],
["scale_greyvestelite", "Imported Scale armor p",[("khergit_scale_c",0)],pnbl,0,5730,weight(12)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(11),imodbits_armor,
[], mercenary_factions],
["noblearmor18res", "White Lorica p",[("byrnie16",0)],pnbl,0,4340,weight(16)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(5)|difficulty(10),imodbits_armor,
[],mercenary_factions],
["longmail_coat_king1", "Blue Kingly Mail p",[("mail_vest_blu",0)],pnbl,0,8990,weight(22)|abundance(60)|head_armor(0)|body_armor(61)|leg_armor(18)|difficulty(12),imodbits_armor,
[],mercenary_factions],
["longmail_coat_kingred","Red Kingly Mail p", [("mail_vest_red",0)],pnbl,0,9060,weight(22)|abundance(60)|head_armor(0)|body_armor(61)|leg_armor(18)|difficulty(12),imodbits_armor,
[],mercenary_factions],
["noblearmor21res", "Gold-painted Red Lamellar War Tunic p",[("idi_scale5",0)],pnbl,0,3410,weight(10)|abundance(60)|head_armor(0)|body_armor(39)|leg_armor(7)|difficulty(8),imodbits_cloth,
[],mercenary_factions],
["noblearmor22res","Thick Blue Warrior Jacket p",[("Kaftan3",0)],pnbl,0,1990,weight(5)|abundance(60)|head_armor(0)|body_armor(25)|leg_armor(4)|difficulty(4),imodbits_cloth,
[],mercenary_factions],
["noblearmor23res", "Leather Girded Noble Tunicp",[("nordiclightarmor63",0)],pnbl,0,1410,weight(8)|abundance(60)|head_armor(5)|body_armor(24)|leg_armor(5)|difficulty(11),imodbits_armor],
["noblearmor24res", "Byzantine Scale armor p", [("khergit_scale_c",0)],pnbl,0,4840,weight(19)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(12)|difficulty(11),imodbits_armor],
["scale_goldlongtunicwcape","Rich Gold-plated Scalar p",[("outaa_escalearmor",0)],pnbl,0,3600,weight(15)|abundance(60)|head_armor(5)|body_armor(36)|leg_armor(12)|difficulty(10),imodbits_armor,
[],mercenary_factions],
##Female Noble Armor

["scale_greykhergitfemale", "Byzantine Scale Armor p",[("scale_shirt_a",0)],pnbl,0,4330,weight(16)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(10)|difficulty(16),imodbits_armor,
[],mercenary_factions + other_mercenary_factions],
["scale_greywhitefemale", "Byzantine Scale Armor p",[("scale_shirt_c",0)],pnbl,0,4330,weight(16)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(10)|difficulty(16),imodbits_armor,
[],mercenary_factions + other_mercenary_factions],
# ["scale_greyvestt2", "Scale Armor", [("khergit_scale_a",0)], pnbl ,0, 3130 , weight(12)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
# [], briton_factions],
# ["scale_greyvestelite", "Scale Armor", [("khergit_scale_c",0)], pnbl ,0, 3130 , weight(12)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
# [], briton_factions],

#malla cubre pecho, y piernas, son largas, valen para pictos e irlandeses
#["longmail_coat_king1", "Brown Kingly Mail", [("mail_vest_b",0)], pnbl,0, 10160 , weight(22)|abundance(60)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(14) ,imodbits_armor,
#[], pict_factions + irish_factions],
#rey briton o mejor para el tipo del muro de hadriano
["noblemanshirt1", "Nobleman Shirt blue-red p",[("nordiclightarmor6",0)],itp_type_body_armor|itp_covers_legs|itp_civilian,0,1410,weight(7)|abundance(60)|head_armor(5)|body_armor(21)|leg_armor(5),imodbits_cloth,
 [],saxon_factions + jute_factions + engle_factions],
["noblemanshirt2","Nobleman Shirt gaelic p", [("nordiclightarmor4",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 1400 , weight(6)|abundance(60)|head_armor(5)|body_armor(21)|leg_armor(5), imodbits_cloth ,
 [], saxon_factions + jute_factions + engle_factions],
["noblemanshirt3", "Nobleman shirt gaelic", [("nordiclightarmor5",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 860 , weight(0.5)|abundance(60)|head_armor(4)|body_armor(20)|leg_armor(4), imodbits_cloth ,
 [], saxon_factions + jute_factions + engle_factions],
["noblemanshirt4", "Nobleman shirt", [("nordiclightarmor61",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 660 , weight(0.5)|abundance(60)|head_armor(4)|body_armor(16)|leg_armor(4), imodbits_cloth ,
 [], saxon_factions + jute_factions + engle_factions],
["noblemanshirt5", "Nobleman shirt", [("nordiclightarmor62",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 660 , weight(0.5)|abundance(60)|head_armor(4)|body_armor(16)|leg_armor(4), imodbits_cloth ,
 [], saxon_factions + jute_factions + engle_factions],
["noblemanshirt6", "Nobleman shirt", [("nordiclightarmor64",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 660 , weight(0.5)|abundance(60)|head_armor(4)|body_armor(16)|leg_armor(4), imodbits_cloth ,
 [], saxon_factions + jute_factions + engle_factions],
["noblemanshirt7", "Nobleman shirt", [("nordiclightarmor66",0)],itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 660 , weight(0.5)|abundance(60)|head_armor(4)|body_armor(16)|leg_armor(4), imodbits_cloth ,
 [], saxon_factions + jute_factions + engle_factions],
# ["longmail_coat_king2", "Red Kingly Mail", [("mail_vest_red",0)], pnbl,0, 10160 , weight(22)|abundance(60)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(14) ,imodbits_armor,
#  [], pict_factions + irish_factions],
["longmail_coat_king2", "White Kingly Mail", [("mail_vest_wht",0)], pnbl,0, 7160 , weight(26)|abundance(60)|head_armor(0)|body_armor(62)|leg_armor(20)|difficulty(14) ,imodbits_armor,
 [], pict_factions + irish_factions],
["longmail_coat_king3", "Green Kingly Mail", [("mail_vest_grn",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7160 , weight(26)|abundance(62)|head_armor(0)|body_armor(61)|leg_armor(20)|difficulty(14) ,imodbits_armor,
 [], pict_factions + irish_factions],
["longmail_coat_king4", "Dark Kingly Mail", [("mail_vest_blk",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 7160 , weight(26)|abundance(60)|head_armor(0)|body_armor(61)|leg_armor(20)|difficulty(14) ,imodbits_armor,
 [], pict_factions + irish_factions],
# # malla cubre pecho y piernas, mas bonita, y mejor elaborada, con bolsa. SOLO NOBLES y super elite, no venta en mercados. SAJONES
 
["mailnoble_redclk1", "Red Noble Mail", [("BL_VikingByrnie01",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(4)|body_armor(56)|leg_armor(7)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["mailnoble_greenclk", "Green Noble Mail", [("BL_VikingByrnie04",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(4)|body_armor(56)|leg_armor(7)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
#["mailnoble_greyclk", "Brown Noble Mail", [("BL_VikingByrnie12",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(0)|body_armor(53)|leg_armor(10)|difficulty(13) ,imodbits_armor,
#[], saxon_factions + jute_factions + engle_factions],
["mailnoble_grnbluclk", "Green Noble Mail", [("BL_VikingByrnie02",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(4)|body_armor(56)|leg_armor(7)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["mailnoble_brownblclk", "Brown Noble Mail", [("BL_VikingByrnie09",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(4)|body_armor(56)|leg_armor(7)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["mailnoble_deerbrclk", "Brown Noble Mail", [("BL_VikingByrnie13",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(4)|body_armor(56)|leg_armor(7)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["mailnoble_greyclk", "Noble Mail", [("BL_VikingByrnie06",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(4)|body_armor(56)|leg_armor(7)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
#byrnies con ropa a cuadros para irlandeses y pictos elite y nobles
["mailnoble_dkgrnclk", "Green Noble Mail", [("BL_VikingByrnie07",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(4)|body_armor(56)|leg_armor(7)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["mailnoble_brwngryclk", "Noble Mail", [("BL_VikingByrnie08",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(4)|body_armor(55)|leg_armor(7)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["mailnoble_brwnwhtclk", "Brown Noble Mail", [("BL_VikingByrnie15",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(4)|body_armor(55)|leg_armor(7)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["mailnoble_ltbrwnclk", "Brown Noble Mail", [("BL_VikingByrnie16",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(4)|body_armor(55)|leg_armor(7)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
##para noble briton
["mailnoble_orangebrwnclk", "Noble Mail", [("BL_VikingByrnie10",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(4)|body_armor(55)|leg_armor(7)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["mailnoble_grnclk", " Noble Mail", [("BL_VikingByrnie11",0)],pmail,0, 7020 , weight(20)|abundance(60)|head_armor(4)|body_armor(55)|leg_armor(10)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
 #######malla con piel de lobo, cubre torso y piernas. Lleva pantalones, solo sajones, y puede que britones. ELITE Y NOBLES
["mail_wolf_coat1", "Wolf Lorica", [("leatherovermail_a",0)],pmail,0, 5600 , weight(22)|abundance(60)|head_armor(0)|body_armor(60)|leg_armor(5)|difficulty(14) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["wolfpelt_mail_coat", "Wolf Lorica", [("leatherovermail_b",0)],pmail,0, 5600 , weight(22)|abundance(60)|head_armor(0)|body_armor(60)|leg_armor(5)|difficulty(14) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
####goat mail para britones elite
["mail_goatist", "Goatist Mail", [("goatist_mail",0)],pmail,0, 5600 , weight(22)|abundance(60)|head_armor(0)|body_armor(58)|leg_armor(15)|difficulty(14) ,imodbits_armor,
 [], briton_factions],
###mail coat para todos
["mailtunic_ltbrown", "Mail Coat", [("mail_coat_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(54)|head_armor(0)|body_armor(52)|leg_armor(11)|difficulty(12) ,imodbits_armor ],
["mailtunic_redbrown", "Mail Coat", [("mail_coat_b",0)],pmail,0, 5560 , weight(19)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mailtunic_green1", "Mail Coat", [("mail_coat_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4060 , weight(19)|abundance(54)|head_armor(0)|body_armor(52)|leg_armor(12)|difficulty(12) ,imodbits_armor ],
["mailtunic_brown", "Mail Coat", [("mail_coat_d",0)],pmail,0, 5560 , weight(19)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mailtunic_ltgreen", "Mail Coat", [("mail_coat_e",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(52)|head_armor(0)|body_armor(52)|leg_armor(12)|difficulty(12) ,imodbits_armor ],
["mailtunic_orange", "Mail Coat", [("mail_coat_f",0)],pmail,0, 5560 , weight(19)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
##["mailtunic_black", "Black Mail Coat", [("mail_coat_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(12)|difficulty(14) ,imodbits_armor ],
##["mail_furredt2", "Brown Mail Coat", [("mail_coat_2",0)],pmail,0, 5560 , weight(19)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mailtunic_blkclk", "Dark Mail Coat", [("mail_coat_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(52)|head_armor(0)|body_armor(54)|leg_armor(11)|difficulty(12) ,imodbits_armor ],
["mailtunic_brownclk", "Mail Coat", [("mail_coat_4",0)],pmail,0, 4060 , weight(19)|abundance(60)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(14) ,imodbits_armor ],
["mailtunic_grey", "Whiteraven Coat", [("mail_shirt_brown",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(52)|head_armor(0)|body_armor(54)|leg_armor(12)|difficulty(12) ,imodbits_armor ],
["mailtunic_green2", "Green Mail Coat", [("mail_shirt_green",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(52)|head_armor(0)|body_armor(52)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mailtunic_redclk", "Red Mail Coat", [("mail_shirt_red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(52)|head_armor(0)|body_armor(52)|leg_armor(12)|difficulty(12) ,imodbits_armor ],
["mailtunic_red", "Red Mail Coat", [("mail_shirt_a_copy",0)],pmail,0, 5560 , weight(19)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],

#Cota de malla cubre pecho y piernas, la usamos para nobles de bajo nivel y tropas de elite de todas las facciones, para britones mirar casos concretos, ya que muchos luchaban sin armadura
["mailtunic_grn", "Green Mail Coat", [("mail_shirt_grn",0)], itp_merchandise |itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(60)|head_armor(5)|body_armor(55)|leg_armor(12)|difficulty(12) ,imodbits_armor ],
#["mailtunic_red1resv", "resRed Mail Coat", [("mail_shirt_red",0)], itp_merchandise |itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(12) ,imodbits_armor ],
["mailtunic_olive", "Olive Mail Coat", [("mail_shirt_ylw",0)], itp_merchandise |itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(60)|head_armor(0)|body_armor(52)|leg_armor(12)|difficulty(12) ,imodbits_armor ],
["mailtunic_gry", "Grey Mail Coat", [("mail_shirt_blk",0)], itp_merchandise |itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(60)|head_armor(0)|body_armor(52)|leg_armor(12)|difficulty(12) ,imodbits_armor ],
["mailtunic_wht", "White Mail Coat", [("mail_shirt_wht",0)], itp_merchandise |itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5560 , weight(19)|abundance(60)|head_armor(5)|body_armor(55)|leg_armor(12)|difficulty(12) ,imodbits_armor ],
###mail coat para elite britona, nobles, gran calidad

 
 
########armaduras pesadas byrnie, para invasores solamente
["lorica_pink", "Brown Lorica", [("byrnie1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["lorica_green", "Green Lorica", [("byrnie_d_new",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["lorica_greyrd", "Red Lorica", [("byrnie_f_new",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
#malla, brynie, protege torso y parte de piernas, para los sajones, con capa
["lorica_eggwht", "White Lorica", [("byrnie11",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["lorica_ltblue", "Blue Lorica", [("byrnie12",0)],pmail,0, 3840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],

["lorica_white", "White Lorica", [("byrnie14",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["lorica_olive", "Olive Lorica", [("ragged_armour_e",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(12)|difficulty(11) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],

["lorica_whitegry", "White Lorica", [("byrnie10",0)],pmail,0, 3840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["lorica_yelo", "Olive Lorica", [("byrnie_g_new",0)],pmail,0, 3840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],

####byrnie para britones. Aplicar a una unidad de elite.
["lorica_stripedred", "Striped Lorica", [("byrnie4",0)],pmail,0, 4840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], briton_factions],
["lorica_stripedblue", "Striped Lorica", [("byrnie5",0)],pmail,0, 4840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 [], briton_factions],
##end of noble bonus
##end of noble bonus
["mailtunic_blk", "Black Mail Coat", [("swadian_mail_hauberk",0)], itp_merchandise |itp_type_body_armor|itp_covers_legs|itp_civilian,0, 5500 , weight(19)|abundance(60)|head_armor(0)|body_armor(41)|leg_armor(12)|difficulty(12) ,imodbits_armor ],
["mail_furredt2", "Furred Large ring Mail", [("rough_smallring_fured",0)], itp_merchandise |itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4600 , weight(19)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(16)|difficulty(10) ,imodbits_armor ],
["mailtunic_blkcheap", "Cheap Mail Coat", [("mail_shirt_a_oscuro",0)],pmail,0, 4560 , weight(19)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(13)|difficulty(12) ,imodbits_armor ],
["mailtunic_greycheap", "Cheap Mail Coat", [("hauberk_a_new",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4680 , weight(19)|abundance(60)|head_armor(0)|body_armor(41)|leg_armor(12)|difficulty(12) ,imodbits_armor ],


["mailshirt_3_trig", "Leather over Mail", [("saxon_leather_vest_mail",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4590 , weight(20)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(11)|difficulty(13) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["mailshirt_orange", "Red Short Mail", [("norman_short_hauberk",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4540 , weight(21)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(12) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["mailshirt_yellow", "Yellow Short Mail", [("norman_short_hauberk_yellow",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4540 , weight(21)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(12) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
["lorica_whitbrn", "White Shirt Lorica", [("sarranid_mail_byrnie_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4340 , weight(19)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(8)|difficulty(12) ,imodbits_armor,
 [], saxon_factions + jute_factions + engle_factions],
####byrnie para pictos, aplicar a una unidad de elite.
["lorica_brightgreen", "Squared Lorica", [("byrnie2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(5)|difficulty(11) ,imodbits_armor,
 [], pict_factions],
["lorica_fadedblue", "Squared Lorica", [("byrnie6",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(5)|difficulty(11) ,imodbits_armor,
 [], pict_factions],
["lorica_dirtygrn", "Squared Lorica", [("byrnie8",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4840 , weight(19)|abundance(60)|head_armor(0)|body_armor(43)|leg_armor(5)|difficulty(11) ,imodbits_armor,
 [], pict_factions],

#byrnie solo para reyes irlandeses, es purpura#purple in noble tunics
 # ["lorica_purpleresrv", "resPurple Lorica", [("byrnie_c_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 8000 , weight(19)|abundance(60)|head_armor(0)|body_armor(53)|leg_armor(6)|difficulty(11) ,imodbits_armor,
 # [], pict_factions + irish_factions],

####tunica larga con maya y capa, para nobles irlandeses y pictos

#armaduras raider, anadidas aqui para compatibilidad con savegames
["mailbandit1", "raider_hauberk", [("raider_hauberk",0)], pmailnm,0, 1360 , weight(21)|abundance(60)|head_armor(0)|body_armor(37)|leg_armor(6)|difficulty(10) ,imodbits_armor ],
["mailbanditt2", "raider_hauberk2", [("raider_hauberk2",0)], pmailnm,0, 1360 , weight(21)|abundance(60)|head_armor(0)|body_armor(37)|leg_armor(6)|difficulty(10) ,imodbits_armor ],
["mailbanditblue", "raider_hauberk3", [("raider_hauberk3",0)], pmailnm,0, 1360 , weight(21)|abundance(60)|head_armor(0)|body_armor(37)|leg_armor(6)|difficulty(10) ,imodbits_armor ],

####Mail shirt, la primera lleva capucha de campesino, vale para invasores y britones
["maillong_shirt", "Mail Shirt", [("haubergeon_jco",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3660 , weight(15)|abundance(60)|head_armor(0)|body_armor(40)|leg_armor(7)|difficulty(11) ,imodbits_armor],
["mailbyrnie_longfurred", "Long Byrnie", [("peasant_leather_mail_LS",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4360 , weight(15)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor],

#malla cubre torso, y cuero protege piernas son las cartons banks, anadir a una unidad britonna, restringir su venta.
["mailbyrniered", "Red Byrnie", [("tattered_leather_armor_2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(60)|head_armor(0)|body_armor(48)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mailbyrnieyelo", "Yellow Byrnie", [("tattered_leather_armor_1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(60)|head_armor(0)|body_armor(48)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mailbyrniegreen", "Green Byrnie", [("tattered_leather_armor_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(60)|head_armor(0)|body_armor(48)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mailbyrnieblue", "Blue Byrnie", [("tattered_leather_armor_b",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(60)|head_armor(0)|body_armor(48)|leg_armor(2)|difficulty(12) ,imodbits_armor],
#["mailbyrniewhite", "White Byrnie", [("tattered_leather_armor_w",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(60)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mailbyrniebrown", "Brown Byrnie", [("tattered_leather_armor_5",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mailbyrniesmokey", "Blue Byrnie", [("tattered_leather_armor_bl",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3360 , weight(15)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mailbyrnieolive", "Green Byrnie", [("tattered_leather_armor_4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mailbyrniegrey", "Grey Byrnie", [("tattered_leather_armor_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(2)|difficulty(12) ,imodbits_armor],
["mailbyrniewhitered", "White Byrnie", [("tattered_leather_armor_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(60)|head_armor(0)|body_armor(44)|leg_armor(2)|difficulty(12) ,imodbits_armor],
#["mailbyrniebluegrey", "Blue Byrnie", [("tattered_leather_armor_8",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 3860 , weight(15)|abundance(60)|head_armor(0)|body_armor(49)|leg_armor(2)|difficulty(12) ,imodbits_armor],
#para elite de pictos e irlandeses solamente
["mail_sleevelessbrn", "Sleeveless Mail", [("gallic_armor_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4280 , weight(17)|abundance(60)|head_armor(0)|body_armor(38)|leg_armor(5)|difficulty(10) ,imodbits_armor,
 [], pict_factions + irish_factions],
["mail_sleevelessgrnorange", "Sleeveless Mail", [("gallic_armor_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4280 , weight(17)|abundance(60)|head_armor(0)|body_armor(38)|leg_armor(5)|difficulty(10) ,imodbits_armor,
 [], pict_factions + irish_factions],
["mail_sleevelessgrn", "Sleeveless Mail", [("gallic_armor",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 4280 , weight(17)|abundance(60)|head_armor(0)|body_armor(38)|leg_armor(5)|difficulty(10) ,imodbits_armor,
 [], pict_factions + irish_factions],

#Armadura laminar, protege torso de bronze. Usar para francos, y algun lord de kent y wessex solamente.
["lamellaraqua", "bronze Lamellar Armor", [("BL_Lamellar04",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3110 , weight(10)|abundance(60)|head_armor(0)|body_armor(33)|leg_armor(5)|difficulty(10) ,imodbits_armor,
[], jute_factions + saxon_factions],
["lamellar2blue", "bronze Lamellar Armor", [("BL_Lamellar02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3110 , weight(10)|abundance(60)|head_armor(0)|body_armor(33)|leg_armor(5)|difficulty(10) ,imodbits_armor,
[], jute_factions + saxon_factions],
#["lamellargreen1", "bronze Lamellar Armor", [("BL_Lamellar01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3510 , weight(10)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(5)|difficulty(10) ,imodbits_armor,
#[], jute_factions + saxon_factions],
["lamellarred1", "bronze Lamellar Armor", [("BL_Lamellar03",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3110 , weight(10)|abundance(60)|head_armor(0)|body_armor(33)|leg_armor(5)|difficulty(10) ,imodbits_armor,
[], jute_factions + saxon_factions],
#["lamellargrnred", "bronze Lamellar Armor", [("BL_Lamellar05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3510 , weight(10)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(5)|difficulty(10) ,imodbits_armor,
#[], jute_factions + saxon_factions],

###lamellar metal para tropas francas y de kent, llevan cuadros, quizas solo francos, y algun noble irlandes
["lamellargrey", "Black Lamellar Armor", [("BL_SLamellar03",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3830 , weight(12)|abundance(60)|head_armor(0)|body_armor(37)|leg_armor(2)|difficulty(11) ,imodbits_armor,
 [], jute_factions + saxon_factions],
["lamellarbrown", "Red Lamellar Armor", [("BL_SLamellar01",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3830 , weight(12)|abundance(60)|head_armor(0)|body_armor(38)|leg_armor(2)|difficulty(11) ,imodbits_armor,
 [], jute_factions + saxon_factions],
["lamellar2yellow", "BL_SLamellar02", [("BL_SLamellar02",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3830 , weight(12)|abundance(60)|head_armor(0)|body_armor(37)|leg_armor(2)|difficulty(11) ,imodbits_armor,
 [], jute_factions + saxon_factions],
###importacion lores irlandeses del sur, usar poco.
["lamellarred2", "bronze Lamellar armor", [("BL_Lamellar07",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3310 , weight(10)|abundance(60)|head_armor(0)|body_armor(33)|leg_armor(5)|difficulty(10) ,imodbits_armor,
 [], jute_factions + saxon_factions],
["lamellar08", "BL_Lamellar08", [("BL_Lamellar08",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3310 , weight(10)|abundance(60)|head_armor(0)|body_armor(33)|leg_armor(5)|difficulty(10) ,imodbits_armor,
 [], jute_factions + saxon_factions],
["lamellarallgreen", "bronze Lamellar armor", [("BL_Lamellar09",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3310 , weight(10)|abundance(60)|head_armor(0)|body_armor(33)|leg_armor(5)|difficulty(10) ,imodbits_armor,
 [], jute_factions + saxon_factions],
#orderchangealertgdw
#ring mail vale para todos, incluso invasores
["mailcuir_bouilli", "peasant_leather_ring_LS", [("peasant_leather_ring_LS",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2800 , weight(13)|abundance(60)|head_armor(0)|body_armor(37)|leg_armor(8)|difficulty(8) ,imodbits_armor],
["mail_largering", "peasant_leather_ring_fur_LS", [("peasant_leather_ring_fur_LS",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2800 , weight(13)|abundance(60)|head_armor(0)|body_armor(37)|leg_armor(8)|difficulty(8) ,imodbits_armor],

#Armadura laminar, protege torso. SOLO BRITONES, PICTOS E IRLANDESES
["scale_vestgrey", "Scale Coat", [("scale_shirt",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3020 , weight(14)|abundance(60)|head_armor(0)|body_armor(39)|leg_armor(9)|difficulty(9) ,imodbits_armor,
 [], briton_factions],
["scale_vest_red", "Scale Shirt", [("rod_lamellar_armor_e_copy",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3330 , weight(12)|abundance(60)|head_armor(0)|body_armor(39)|leg_armor(5)|difficulty(12) ,imodbits_armor,
[], briton_factions],
###scale armadura corta
 #["scale_bronze_armor", "Scale Armor", [("idi_scale2",0)],itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(6)|difficulty(11) ,imodbits_armor,
#[], briton_factions],
["scale_brown_armor", "Grey Scale Armor", [("idi_scale6",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(60)|head_armor(0)|body_armor(39)|leg_armor(7)|difficulty(11) ,imodbits_armor,
 [], briton_factions],
["scale_white_armor", "White Scale Armor", [("idi_scale7",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(60)|head_armor(0)|body_armor(39)|leg_armor(7)|difficulty(11) ,imodbits_armor,
 [], briton_factions],
["scaleorangeblkbands", "Scale Armor", [("idi_scale10",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(60)|head_armor(0)|body_armor(39)|leg_armor(7)|difficulty(11) ,imodbits_armor,
 [], briton_factions],
["scale_bronze_armor", "Scale Armor", [("idi_scale12",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(60)|head_armor(0)|body_armor(39)|leg_armor(7)|difficulty(11) ,imodbits_armor,
 [], briton_factions],
["scale_bronzegreen", "Scale Armor", [("idi_scale14",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(60)|head_armor(0)|body_armor(39)|leg_armor(7)|difficulty(11) ,imodbits_armor,
 [], briton_factions],
###irlandeses y pictos
["scale_armor1", "Scale Armor", [("idi_scale1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(60)|head_armor(0)|body_armor(39)|leg_armor(7)|difficulty(11) ,imodbits_armor,
 [], pict_factions + irish_factions],
["scale_bronze_fadedgrn", "Scale Armor", [("idi_scale3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(60)|head_armor(0)|body_armor(39)|leg_armor(7)|difficulty(11) ,imodbits_armor,
 [], pict_factions + irish_factions],
["scale_bronze_blueorange", "Scale Armor", [("idi_scale4",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3130 , weight(12)|abundance(60)|head_armor(0)|body_armor(39)|leg_armor(7)|difficulty(11) ,imodbits_armor,
 [], pict_factions + irish_factions],
 
 #moved to noble armors
#["scale_noblelongtunicres", "idi_scale5", [("idi_scale5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 3420 , weight(12)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(4)|difficulty(11) ,imodbits_armor,
 # [], pict_factions + irish_factions],
#orderchangealertgdw

# ########################################################################################
# ####armaduras pesadas finales acaba chief############################################


# ###################ARMADURAS MEDIAS CHIEF finales###########################################
 
# #gambeson de lino, cubre torso, cualquier faccion
["linen_coatbrown", "Linen Coat", [("ped_padded1_brown",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1170 , weight(4)|abundance(60)|head_armor(0)|body_armor(27)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
["linen_coatwhite", "White Linen Coat", [("armor_15",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1170 , weight(4)|abundance(60)|head_armor(0)|body_armor(27)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
["linen_coatblue", "Blue Linen Coat", [("armor_17",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1170 , weight(4)|abundance(60)|head_armor(0)|body_armor(27)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
["linen_coattan", "Dirty Linen Coat", [("ped_padded1_narrow",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1090 , weight(4)|abundance(60)|head_armor(0)|body_armor(26)|leg_armor(5)|difficulty(6) ,imodbits_armor ],
["linen_coatwcloak", "Linen Coat with Cloak", [("ped_padded1_creme",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1090 , weight(4)|abundance(60)|head_armor(0)|body_armor(26)|leg_armor(5)|difficulty(6) ,imodbits_armor ],

#kaftan
["jack_armorpaddedyelo", "Padded Warrior Jacket", [("Kaftan_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 680 , weight(5)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(4)|difficulty(4) ,imodbits_cloth,
 [], saxon_factions + jute_factions + engle_factions],

["jack_armorpaddedred", "Red Padded Warrior Jacket", [("kaftan_vae_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(5)|abundance(60)|head_armor(0)|body_armor(23)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], saxon_factions + jute_factions + engle_factions],
#["djack_armorblued", "dBlue Warrior Jacket", [("Kaftan4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 #[], saxon_factions + jute_factions + engle_factions],
["jack_armorred", "Red Warrior Jacket", [("Kaftan",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], saxon_factions + jute_factions + engle_factions],
# ["jack_armorblue", "Blue Warrior Jacket", [("Kaftan3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
#  [], saxon_factions + jute_factions + engle_factions],
# ["jack_armorfadedblue", "Blue Warrior Jacket", [("kaftanh",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
#  [], saxon_factions + jute_factions + engle_factions],
["jack_armorgreen", "Green Warrior Jacket", [("kaftani",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], saxon_factions + jute_factions + engle_factions],
["jack_armorfadedblue", "Blue Warrior Jacket", [("kaftan_vae_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 [], saxon_factions + jute_factions + engle_factions],
#["jack_armorred2", "Red Warrior Jacket", [("kaftan2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
 #[], saxon_factions + jute_factions + engle_factions],
["jack_armorbluedark", "Blue Warrior Jacket", [("kaftan_vae_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 520 , weight(4)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(3)|difficulty(4) ,imodbits_cloth,
[], saxon_factions + jute_factions + engle_factions],
#orderchangealertgdwfor purploeone
##kaftan for leather


#armadura de piel de animal sajones y britones
["rawhide_vest_green", "Leather over Tunic", [("saxon_leather_vest_green",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 820 , weight(4)|abundance(60)|head_armor(0)|body_armor(23)|leg_armor(2)|difficulty(6) ,imodbits_cloth ],
["rawhide_coat1tier2", "rawhide_coattier2", [("coat_of_plates1",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ],
["rawhide_vest_blue", "saxon_leather_vest_blue", [("saxon_leather_vest_blue",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 820 , weight(4)|abundance(60)|head_armor(0)|body_armor(23)|leg_armor(2)|difficulty(6) ,imodbits_cloth ],
["rawhide_coat2", "Rawhide Coat", [("coat_of_plates3",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ],
["rawhide_coat3", "Rawhide Coat", [("coat_of_plates4",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ],
["rawhide_coat4", "Rawhide Coat", [("coat_of_plates5",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ],
["rawhide_coat5t3", "Rawhide Coat", [("coat_of_plates1m",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ],
["rawhide_vest_red", "saxon_leather_vest_red", [("saxon_leather_vest_red",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 820 , weight(4)|abundance(60)|head_armor(0)|body_armor(23)|leg_armor(2)|difficulty(6) ,imodbits_cloth ],
["rawhide_coat6white", "Rawhide Coat", [("coat_of_plates3m",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ],
["rawhide_coat7green", "Rawhide Coat", [("coat_of_plates4m",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ],
["rawhide_coat8bluet2", "Rawhide Coat", [("coat_of_plates5m",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ],
["rawhide_coat9grey", "Rawhide Coat", [("coat_of_plates6m",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1020 , weight(6)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(8)|difficulty(6) ,imodbits_cloth ],

["goatist_tuniccoat", "Goatist Tunic", [("goatist_tunic",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 1160 , weight(4)|abundance(60)|head_armor(0)|body_armor(22)|leg_armor(12)|difficulty(6) ,imodbits_cloth ],

##tunica con pellejo piel encima, campesinos
["pelt_coat1", "Pelt Coat", [("thick_coat_a_bry",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 700 , weight(3)|abundance(60)|head_armor(0)|body_armor(18)|leg_armor(2)|difficulty(2) ,imodbits_cloth ],
["pelt_coat2", "Pelt Coat", [("wei_xiadi_rod_thick_coat",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 700 , weight(3)|abundance(60)|head_armor(0)|body_armor(18)|leg_armor(2)|difficulty(2) ,imodbits_cloth ],
#tunica similar a anterior pero con tela dura
["vae_thickcoat1", "Simple Coat", [("vae_thick_coat1",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 700 , weight(3)|abundance(60)|head_armor(0)|body_armor(18)|leg_armor(2)|difficulty(2) ,imodbits_cloth ],
["vae_thickcoat2", "Simple Coat", [("vae_thick_coat2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 800 , weight(3)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(2)|difficulty(2) ,imodbits_cloth ],
["vae_thickcoat3", "Simple Coat", [("vae_thick_coat3",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 700 , weight(3)|abundance(60)|head_armor(0)|body_armor(18)|leg_armor(2)|difficulty(2) ,imodbits_cloth ],
["hide_coat6", "Hide Coat", [("vae_thick_coat6",0)], itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 800 , weight(3)|abundance(60)|head_armor(0)|body_armor(24)|leg_armor(2)|difficulty(2) ,imodbits_cloth ],
["hide_coat1", "Hide Coat", [("vae_thick_coat10",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 700 , weight(3)|abundance(60)|head_armor(0)|body_armor(18)|leg_armor(2)|difficulty(2) ,imodbits_cloth ],
 

####Gathered cloak, los que van en plan miliciano con la capa
["gatheredcloaks1", "Blue Gathered Cloak", [("gatheredcloak1",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(2)|abundance(60)|head_armor(0)|body_armor(17)|leg_armor(6)|difficulty(2) ,imodbits_cloth ],
["gatheredcloaks2", "Green Gathered Cloak", [("gatheredcloak2",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(2)|abundance(60)|head_armor(0)|body_armor(17)|leg_armor(6)|difficulty(2) ,imodbits_cloth ],
["gatheredcloaks3", "Yellow Gathered Cloak", [("gatheredcloak3",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(2)|abundance(60)|head_armor(0)|body_armor(17)|leg_armor(6)|difficulty(2) ,imodbits_cloth ],
["gatheredcloaks4", "Gathered Cloak", [("gatheredcloak4",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(2)|abundance(60)|head_armor(0)|body_armor(17)|leg_armor(6)|difficulty(2) ,imodbits_cloth ],
["gatheredcloaks5", "Blue Gathered Cloak", [("gatheredcloak5",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 740 , weight(2)|abundance(60)|head_armor(0)|body_armor(17)|leg_armor(6)|difficulty(2) ,imodbits_cloth ],
 
###tipo gordo
["thick_body", "Fat Body", [("fat_body",0)], itp_no_pick_up_from_ground| itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 10 , weight(3)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(4) ,imodbits_cloth ],

]

items += module_items_headwear.items

items += [

# # Chief empieza########
# ####ARMAS DE ATAQUE#########


# ###armas de no filo, porras, mazas madera etc... finalizadas
#  #######################
["club_stick",   "Wooden Stick", [("wooden_stick",0)], itp_clb, itc_cleaver,15 , weight(3)|difficulty(0)|spd_rtng(77) | weapon_length(88)|swing_damage(17 , blunt) | thrust_damage(0 , blunt),imodbits_none ],
["clubsmooth",   "Club", [("club",0)], itp_clb, itc_cleaver,70 , weight(1.0)|difficulty(5)|spd_rtng(101) | weapon_length(60)|swing_damage(14 , blunt) | thrust_damage(0 , blunt),imodbits_none ],
["club_one",   "Club", [("club_one",0)], itp_clb, itc_cleaver, 110 , weight(2)|difficulty(6)|spd_rtng(90) | weapon_length(68)|swing_damage(15 , blunt) | thrust_damage(0 , blunt),imodbits_none ],
["club_thorny",   "Wooden Club", [("palka",0)], itp_clb, itc_cleaver,95 , weight(2)|difficulty(6)|spd_rtng(82) | weapon_length(67)|swing_damage(19 , blunt) | thrust_damage(0 , blunt),imodbits_none ],
["clubcudgel",   "Wooden Club", [("palka2",0)], itp_clb, itc_cleaver, 120 , weight(2)|difficulty(6)|spd_rtng(87) | weapon_length(68)|swing_damage(18 , blunt) | thrust_damage(0 , blunt),imodbits_none ],
["club3",   "Wooden Club", [("palka3",0)], itp_clb, itc_cleaver,160 , weight(2)|difficulty(6)|spd_rtng(90) | weapon_length(69)|swing_damage(19 , blunt) | thrust_damage(0 , blunt),imodbits_none ],
# ["club4de",   "deWooden Club", [("palka4",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_axe1h, 
# 100 , weight(2)|difficulty(0)|spd_rtng(87) | weapon_length(65)|swing_damage(20 , blunt) | thrust_damage(0 , pierce),imodbits_none ],
# ["club5de",   "deWooden Club", [("palka5",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_axe1h, 
# 100 , weight(2)|difficulty(0)|spd_rtng(87) | weapon_length(65)|swing_damage(20 , blunt) | thrust_damage(0 , pierce),imodbits_none ],
["spikedclub",   "Studded Club", [("spiked_club",0)], itp_clb, itc_cleaver,200 , weight(3)|difficulty(0)|spd_rtng(80) | weapon_length(83)|swing_damage(22 , blunt) | thrust_damage(0 , pierce),imodbits_none ],
["sickle",   "Sickle", [("sickle",0)], itp_clb, itc_cleaver,100 , weight(1.5)|difficulty(0)|spd_rtng(86) | weapon_length(40)|swing_damage(15 , cut) | thrust_damage(0 , pierce),imodbits_none ],
#####no filo
 ##############################

####cuchillos y seax chief###################
 ###########################################

["knifechp",   "Knife", [("peasant_knife",0)], itp_knif,itc_seax,145 , weight(0.5)|difficulty(0)|spd_rtng(90) | weapon_length(35)|swing_damage(15 , cut) | thrust_damage(15 , pierce),imodbits_sword ],
["butchering_knife", "Butchering Knife", [("khyber_knife",0)], itp_knif,itc_cleaver,145,weight(0.75)|difficulty(0)|spd_rtng(80) | weapon_length(40)|swing_damage(19 , cut) | thrust_damage(9 , pierce),imodbits_sword ],

#todos
["hunting_knife",   "Hunting Seax", [("hunting_dagger",0),("seaxsheath", ixmesh_carry)], itp_knif,itc_seax, 155 , weight(0.5)|difficulty(0)|spd_rtng(90) | weapon_length(53)|swing_damage(16 , cut) | thrust_damage(17 , pierce),imodbits_sword ],
["lang_knifet2", "Simple Long Knife", [("simple_langseax",0),("simple_langseax_scab", ixmesh_carry)],itp_knif,itc_seax, 195 , weight(0.5)|difficulty(0)|spd_rtng(90) | weapon_length(62)|swing_damage(14 , cut) | thrust_damage(19 , pierce),imodbits_sword ],
["knife1",   "Simple Seax", [("simple_seax",0),("simple_seax_scab", ixmesh_carry)], itp_knif,itc_seax, 160 , weight(0.5)|difficulty(0)|spd_rtng(93) | weapon_length(65)|swing_damage(14 , cut) | thrust_damage(19 , pierce),imodbits_sword ],
#irlandeses y pictos
#scians para tropas medias (nivel 20 a 25), son baratos y terribles
["scianshswordt1",   "Short Scian", [("scianshort",0),("scianshort", ixmesh_carry)], itp_knif,itc_seax, 260 , weight(0.8)|difficulty(6)|spd_rtng(94) | weapon_length(71)|swing_damage(18 , cut) | thrust_damage(21 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["scianshswordbone",   "Short Bone Scian", [("scianshortbone",0),("scianshortbone", ixmesh_carry)], itp_knif,itc_seax, 280 , weight(0.8)|difficulty(6)|spd_rtng(90) | weapon_length(71)|swing_damage(18 , cut) | thrust_damage(22 , pierce),imodbits_sword,
[], pict_factions + irish_factions],


#sajones, aglos y jutos
["talak_seaxkni", "Light Seax", [("vikingr_seax",0),("vikingr_seax_scab", ixmesh_carry)], itp_knif,itc_seax,280 , weight(0.5)|difficulty(4)|spd_rtng(92) | weapon_length(65)|swing_damage(14 , cut) | thrust_damage(19 , pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
["saxon_seaxkni", "Saxon Seax", [("saxon_seax",0),("saxon_seax_scab", ixmesh_carry)], itp_knif,itc_seax, 290 , weight(0.5)|difficulty(0)|spd_rtng(94) | weapon_length(67)|swing_damage(14 , cut) | thrust_damage(19 , pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
["langseaxt2", "Lang Seax", [("langseax",0),("langseax_scab", ixmesh_carry)], itp_knif,itc_seax|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 330 , weight(0.5)|difficulty(0)|spd_rtng(88) | weapon_length(74)|swing_damage(14 , cut) | thrust_damage(22 , pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
["ornate_seaxt3", "Ornate Seax", [("ornate_seax",0),("ornate_seax_scab", ixmesh_carry)], itp_knif,itc_seax|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 400 , weight(0.5)|difficulty(0)|spd_rtng(93) | weapon_length(67)|swing_damage(16 , cut) | thrust_damage(21 , pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
["seaxt3",   "Seax", [("seax",0),("seax",ixmesh_carry),("seax",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)],itp_knif,itc_seax|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 340 , weight(0.5)|difficulty(0)|spd_rtng(93) | weapon_length(68)|swing_damage(14 , cut) | thrust_damage(23 , pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
["knisxclearvert3",   "Cleaver Seax", [("cleaver_seax",0),("cleaver_seax_scab", ixmesh_carry)], itp_knif,itc_cleaver, 300 , weight(0.5)|difficulty(0)|spd_rtng(87) | weapon_length(64)|swing_damage(23 , cut) | thrust_damage(14 , pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
["seaxt4",   "Deadly Seax", [("seax_hp_tri",0),("seaxsheath", ixmesh_carry)], itp_knif,itc_seax|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 420 , weight(0.5)|difficulty(0)|spd_rtng(90) | weapon_length(70)|swing_damage(16 , cut) | thrust_damage(23 , pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
["knislotforseax", "unused Seax", [("vikingr_seax",0),("vikingr_seax_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_seax|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 280 , weight(0.5)|difficulty(0)|spd_rtng(92) | weapon_length(65)|swing_damage(14 , cut) | thrust_damage(19 , pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
#leftthese
###############cuchillos y seaxa caba chief#############################


####Espadas chief finales #####################
########################################
#basica todas las culturas, spatha romana
["spathaswordt2", "Cavarly Spatha", [("pattern_spatha",0),("roman_cav_sword_2_scabbard", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 930 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(96)|swing_damage(35 , cut) | thrust_damage(15 , pierce),imodbits_sword ],
["spathaswordt2_alt", "Spatha", [("pattern_spatha",0),("roman_cav_sword_2_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 900 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(14 , pierce),imodbits_sword ],
###otras basicas
["rich_spathaswordt2", "Rich Spatha", [("le_pictishsword2",0),("scab_vikingsw", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.25)|difficulty(9)|spd_rtng(84) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(16 , pierce),imodbits_sword ],
["rich_spathaswordt2_alt", "Rich Spatha", [("le_pictishsword2",0),("scab_vikingsw", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 840 , weight(1.25)|difficulty(9)|spd_rtng(86) | weapon_length(93)|swing_damage(32 , cut) | thrust_damage(14 , pierce),imodbits_sword ],
["spathasword", "Spatha", [("BL_Sword01_01",0),("BL_Sword01_01", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 840 , weight(1.25)|difficulty(8)|spd_rtng(86) | weapon_length(93)|swing_damage(32 , cut) | thrust_damage(15 , pierce),imodbits_sword ],
["spathasword_alt", "spatha", [("BL_Sword01_01",0),("BL_Sword01_01", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 840 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(17 , pierce),imodbits_sword ],
["sword2", "Sword", [("BL_Sword01_02",0),("BL_Sword01_02", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 830 , weight(1.25)|difficulty(8)|spd_rtng(84) | weapon_length(91)|swing_damage(31 , cut) | thrust_damage(17 , pierce),imodbits_sword ],
["sword2_alt", "Sword", [("BL_Sword01_02",0),("BL_Sword01_02", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 830 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(17 , pierce),imodbits_sword ],
["sword3", "Sword1", [("Sword1",0),("Sword1", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 830 , weight(1.25)|difficulty(8)|spd_rtng(85) | weapon_length(90)|swing_damage(30 , cut) | thrust_damage(18 , pierce),imodbits_sword ],
["sword3_alt", "Sword1", [("Sword1",0),("Sword1", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 940 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(18 , pierce),imodbits_sword ],
["sword4t2", "Sword2", [("Sword2",0),("Sword2", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 830 , weight(1.25)|difficulty(8)|spd_rtng(84) | weapon_length(93)|swing_damage(32 , cut) | thrust_damage(18 , pierce),imodbits_sword ],
["sword4t2_alt", "Sword2", [("Sword2",0),("Sword2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 940 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(32 , cut) | thrust_damage(18 , pierce),imodbits_sword ],
#saxonswnot used 
["saxonsword1", "Saxon Sword", [("BL_Sword01_03",0),("BL_Sword01_03", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 825 , weight(1.25)|difficulty(8)|spd_rtng(85) | weapon_length(92)|swing_damage(29 , cut) | thrust_damage(19 , pierce),imodbits_sword,
[], saxon_factions],
["saxonsword_alt", "BL_Sword01_03", [("BL_Sword01_03",0),("BL_Sword01_03", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 825 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(17 , pierce),imodbits_sword ],
#scba problem acaba
["bamburghsword1t2", "le_bamburghsword", [("le_bamburghsword",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 950 , weight(1.25)|difficulty(8)|spd_rtng(86) | weapon_length(94)|swing_damage(33 , cut) | thrust_damage(17 , pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
["bamburghsword1t2_alt", "le_bamburghsword", [("le_bamburghsword",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 950 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(14 , pierce),imodbits_sword ],
["bamburghsword2t2", "Engle Rich Sword", [("BamburghSword2",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 998 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(96)|swing_damage(35 , cut) | thrust_damage(15 , pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
["bamburghsword2t2_alt", "Sword", [("BamburghSword2",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 998 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(36 , cut) | thrust_damage(14 , pierce),imodbits_sword ],
#leave the last few swords for mod-integration
#Invasores
#basica
["saxonswordt2", "Saxon Sword", [("RichSword1",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 940 , weight(1.25)|difficulty(8)|spd_rtng(86) | weapon_length(94)|swing_damage(30 , cut) | thrust_damage(20 , pierce),imodbits_sword,
[], saxon_factions],
["saxonswordt2_alt", "Saxon Sword", [("RichSword1",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 940 , weight(1.25)|difficulty(8)|spd_rtng(83) | weapon_length(95)|swing_damage(32 , cut) | thrust_damage(19 , pierce),imodbits_sword, ],

#scab problem 1 debajo
["germanicswordt2", "Germanic Sword", [("le_richsword1",0),("le_richsword1", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 940 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(94)|swing_damage(33 , cut) | thrust_damage(17 , pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
["germanicswordt2_alt", "Germanic Sword", [("le_richsword1",0),("le_richsword1", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 940 , weight(1.25)|difficulty(9)|spd_rtng(81) | weapon_length(90)|swing_damage(35 , cut) | thrust_damage(14 , pierce),imodbits_sword ],
# tropas elite
["angleswordt2", "Angle Sword", [("Sword3",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 940 , weight(1.25)|difficulty(9)|spd_rtng(87) | weapon_length(90)|swing_damage(29 , cut) | thrust_damage(21, pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
["angleswordt2_alt", "Angle Sword", [("Sword3",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 945 , weight(1.25)|difficulty(9)|spd_rtng(81) | weapon_length(90)|swing_damage(35 , cut) | thrust_damage(14 , pierce),imodbits_sword ],

["jute_richsword", "Rich Frankish Sword", [("le_pictishsword3",0),("Scab_Pict_Sword", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 945 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(94)|swing_damage(33 , cut) | thrust_damage(17 , pierce),imodbits_sword,
[], saxon_factions + jute_factions + engle_factions],
["jute_richsword_alt", "Rich Saxon Sword", [("le_pictishsword3",0),("Scab_Pict_Sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 945 , weight(1.25)|difficulty(9)|spd_rtng(83) | weapon_length(95)|swing_damage(36 , cut) | thrust_damage(15 , pierce),imodbits_sword ],
#ricos nobles y tropas sumun
["briton_richswordt2", "Nobleman Spatha", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 955, weight(1.55)|difficulty(10)|spd_rtng(85) | weapon_length(96)|swing_damage(34 , cut) | thrust_damage(15 , pierce),imodbits_sword_high,
[], briton_factions],
["briton_richswordt2_alt", "Nobleman Spatha", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 955 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(18 , pierce),imodbits_sword_high, ],

#sin uso
["nobleman_sword", "Briton Nobleman Spatha", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.45)|difficulty(8)|spd_rtng(81) | weapon_length(97)|swing_damage(36 , cut) | thrust_damage(14 , pierce),imodbits_sword_high,
[], briton_factions],
["nobleman_sword_alt", "Nobleman Spatha", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(90)|swing_damage(38 , cut) | thrust_damage(19 , pierce),imodbits_sword_high, ],

["angle_swordt3", "Angle Rich Sword", [("Sword4",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1060 , weight(1.25)|difficulty(9)|spd_rtng(86) | weapon_length(94)|swing_damage(33 , cut) | thrust_damage(19 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["angle_swordt3_alt", "Angle Rich Sword", [("Sword4",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1060 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(19 , pierce),imodbits_sword_high, ],

## tropas de elite
["richsword2", "Rich Sword", [("le_richsword2",0),("RichSword3_scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 940 , weight(1.25)|difficulty(9)|spd_rtng(84) | weapon_length(91)|swing_damage(31 , cut) | thrust_damage(19 , pierce),imodbits_sword_high,
[], briton_factions],
["richsword2_alt", "Rich Sword", [("le_richsword2",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 940 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(19 , pierce),imodbits_sword_high,  ],

#sin uso
["richlongsword2", "German Longsword", [("le_richsword2",0),("RichSword3_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(7)|spd_rtng(81) | weapon_length(97)|swing_damage(36 , cut) | thrust_damage(16 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["richlongsword2_alt", "German Longsword", [("le_richsword2",0),("RichSword3_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(7)|spd_rtng(82) | weapon_length(96)|swing_damage(37 , cut) | thrust_damage(17 , pierce),imodbits_sword_high, ],


#sutton hoo sword, reyes y nobles anglos, sajones y jutos
["suttonhoosword", "Richman Sword", [("SuttonSpatha",0),("SuttonSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(9)|spd_rtng(86) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(16 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["suttonhoosword_alt", "Richman Sword", [("SuttonSpatha",0),("SuttonSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(97)|swing_damage(36 , cut) | thrust_damage(17 , pierce),imodbits_sword_high, ],

["germanswordt3", "Lord Sword", [("BL_shSword",0),("SuttonSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1070 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(96)|swing_damage(36 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["germanswordt3_alt", "Lord Sword", [("BL_shSword",0),("SuttonSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1070 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(17 , pierce),imodbits_sword_high, ],

["princep_sword_frankish", "Princep Frankia Sword", [("le_pictishsword7",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 990 , weight(1.25)|difficulty(9)|spd_rtng(88) | weapon_length(90)|swing_damage(34 , cut) | thrust_damage(16 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["princep_sword_frankish_alt", "Princep Frankia Sword", [("le_pictishsword7",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 990 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(17 , pierce),imodbits_sword_high, ],


##jutos, sussex, dena pirates
["saxondenaswordt3", "ValsSword1", [("ValsSword1",0),("ValsSword1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1100 , weight(1.25)|difficulty(8)|spd_rtng(84) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(20 , pierce),imodbits_sword_high,
[], ['fac_kingdom_1', 'fac_kingdom_2', 'fac_kingdom_5']],
["saxondenaswordt3_alt", "ValsSword1", [("ValsSword1",0),("ValsSword1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1100 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(19 , pierce),imodbits_sword_high, ],


###britones
#basicas britones
["britonswordt2", "Briton Sword", [("RichSword3",0),("RichSword3_scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 945 , weight(1.25)|difficulty(8)|spd_rtng(85) | weapon_length(92)|swing_damage(33 , cut) | thrust_damage(19 , pierce),imodbits_sword_high,
[], briton_factions],
["britonswordt2_alt", "Briton Sword", [("RichSword3",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 945 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(17 , pierce),imodbits_sword_high, ],

["britonswordt3", "Briton elite Sword", [("saxon_sword",0),("RichSword1_Scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1065 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(97)|swing_damage(35 , cut) | thrust_damage(19 , pierce),imodbits_sword_high,
[], briton_factions],
["britonswordt3_alt", "Sword", [("saxon_sword",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1065 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(16 , pierce),imodbits_sword_high, ],



# #irlandeses y pictos
# #scians para tropas medias (nivel 20 a 25), son baratos y terribles
["sciansword", "scianlong", [("scianlong",0),("scianlong", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 900 , weight(1.21)|difficulty(6)|spd_rtng(84) | weapon_length(93)|swing_damage(28 , cut) | thrust_damage(22 , pierce),imodbits_sword_high,
[], pict_factions + irish_factions],
["sciansword_alt", "scianlong", [("scianlong",0),("scianlong", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1040 , weight(1.25)|difficulty(6)|spd_rtng(86) | weapon_length(94)|swing_damage(29 , cut) | thrust_damage(25 , pierce),imodbits_sword_high, ],

["scianswordbone", "Scian Long Bone", [("scianlongbone",0),("scianlongbone", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 910 , weight(1.25)|difficulty(6)|spd_rtng(89) | weapon_length(85)|swing_damage(25 , cut) | thrust_damage(25 , pierce),imodbits_sword_high,
[], pict_factions + irish_factions],
["scianswordbone_alt", "Scian Long Bone", [("scianlongbone",0),("scianlongbone", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1040 , weight(1.25)|difficulty(6)|spd_rtng(86) | weapon_length(94)|swing_damage(29 , cut) | thrust_damage(25 , pierce),imodbits_sword_high, ],

 #comun
 #britones, irlandeses y pictos
["irish_longsword", "Celt Long Sword", [("irish_long_sword",0),("irish_long_sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 1100 , weight(2.25)|difficulty(11)|spd_rtng(78) | weapon_length(99)|swing_damage(38 , cut) | thrust_damage(13 , pierce),imodbits_sword_high,
[], pict_factions + irish_factions],
["irish_longsword_alt", "Celt Long Sword", [("irish_long_sword",0),("irish_long_sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 1100 , weight(1.25)|difficulty(8)|spd_rtng(81) | weapon_length(99)|swing_damage(34 , cut) | thrust_damage(8 , pierce),imodbits_sword_high, ],

#corta
["irish_shsword",   "Godelic Short Sword", [("irish_sword",0),("irish_sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee, itc_seax|itcf_carry_sword_left_hip, 810 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(73)|swing_damage(20 , cut) | thrust_damage(31 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["irish_shsword_alt", "Godelic Short Sword", [("irish_sword",0),("irish_sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword|itcf_carry_sword_left_hip, 810 , weight(1.25)|difficulty(8)|spd_rtng(81) | weapon_length(99)|swing_damage(34 , cut) | thrust_damage(8 , pierce),imodbits_sword_high,],

["noble_shswordt2",   "Nobleman Short Sword", [("le_pictishsword6",0),("le_pictishsword6", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary, itc_seax|itcf_carry_sword_left_hip, 920 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(76)|swing_damage(20 , cut) | thrust_damage(33 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["noble_shswordt2_alt",   "Nobleman Short Sword", [("le_pictishsword6",0),("le_pictishsword6", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_seax|itcf_carry_sword_left_hip, 920 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(70)|swing_damage(20 , cut) | thrust_damage(35 , pierce),imodbits_sword,],

["godelic_shsword",   "Celtic2", [("Celtic2",0),("Celtic2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee, itc_seax|itcf_carry_sword_left_hip, 820 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(72)|swing_damage(21 , cut) | thrust_damage(30 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["godelic_shsword_alt",   "Celtic2", [("Celtic2",0),("Celtic2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_seax|itcf_carry_sword_left_hip, 820 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(70)|swing_damage(22 , cut) | thrust_damage(33 , pierce),imodbits_sword,],

["rich_shswordt3",   "Rich Short Sword", [("le_pictishsword5",0),("le_pictishsword5", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee, itc_seax|itcf_carry_sword_left_hip, 990 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(77)|swing_damage(24 , cut) | thrust_damage(30 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["rich_shswordt3_alt",   "Rich Short Sword", [("le_pictishsword5",0),("le_pictishsword5", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_seax|itcf_carry_sword_left_hip, 990 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(70)|swing_damage(22 , cut) | thrust_damage(33 , pierce),imodbits_sword,],
#larga
["pictish_longsword1", "Pictish Longsword", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1105 , weight(1.3)|difficulty(10)|spd_rtng(81) | weapon_length(99)|swing_damage(37 , cut) | thrust_damage(14 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["pictish_longsword1_alt", "Pictish Longsword", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1105 , weight(1.3)|difficulty(8)|spd_rtng(81) | weapon_length(99)|swing_damage(34 , cut) | thrust_damage(13 , pierce),imodbits_sword,],

#media
["godelic_swordt2",   "Godelic Sword", [("Celtic1",0),("CelticShort1_1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee, itc_seax|itcf_carry_sword_left_hip, 930 , weight(2)|difficulty(8)|spd_rtng(85) | weapon_length(83)|swing_damage(29 , cut) | thrust_damage(24 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["godelic_swordt2_alt",   "Godelic Sword", [("Celtic1",0),("CelticShort1_1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_seax|itcf_carry_sword_left_hip, 930 , weight(1)|difficulty(8)|spd_rtng(87) | weapon_length(82)|swing_damage(30 , cut) | thrust_damage(28 , pierce),imodbits_sword,],

["godelic_swordt3",   "Godelic Sword", [("irishword2",0),("gallic_sword_scabbard_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee, itc_seax|itcf_carry_sword_left_hip, 1030 , weight(1)|difficulty(6)|spd_rtng(85) | weapon_length(87)|swing_damage(30 , cut) | thrust_damage(25 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["godelic_swordt3_alt",   "Godelic Sword", [("irishword2",0),("gallic_sword_scabbard_2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_seax|itcf_carry_sword_left_hip, 1030 , weight(1)|difficulty(6)|spd_rtng(87) | weapon_length(86)|swing_damage(30 , cut) | thrust_damage(28 , pierce),imodbits_sword,],
#tipica
["pommel_swordt2", "Wooden pommel Sword", [("CelticV2_1",0),("CelticV2_1_scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.25)|difficulty(8)|spd_rtng(92) | weapon_length(90)|swing_damage(33 , cut) | thrust_damage(14 , pierce),imodbits_sword_high,
[], briton_factions],
["pommel_swordt2_alt", "Wooden pommel Sword", [("CelticV2_1",0),("CelticV2_1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.25)|difficulty(8)|spd_rtng(81) | weapon_length(90)|swing_damage(35 , cut) | thrust_damage(15 , pierce),imodbits_sword_high,],


["pommel_swordt3", "Long wooden pommel Sword", [("CelticV2_2",0),("CelticV2_2_scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1070 , weight(1.25)|difficulty(8)|spd_rtng(89) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(14 , pierce),imodbits_sword_high,
[], briton_factions],
["pommel_swordt3_alt", "Wooden pommel Sword", [("CelticV2_2",0),("CelticV2_2_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1070 , weight(1.25)|difficulty(8)|spd_rtng(81) | weapon_length(90)|swing_damage(35 , cut) | thrust_damage(15 , pierce),imodbits_sword_high,],

#tropas de elite 
["gaelicsword1", "Gaelic Pommel Sword", [("CelticShort1_1",0),("CelticShort1_1_Scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 890 , weight(1.25)|difficulty(8)|spd_rtng(91) | weapon_length(87)|swing_damage(31 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], pict_factions + irish_factions],
["gaelicsword1_alt", "Gaelic Pommel Sword", [("CelticShort1_1",0),("CelticShort1_1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(36 , cut) | thrust_damage(19 , pierce),imodbits_sword_high,],

["celtic_sword", "Celtic Cav Sword", [("CelticShort1_2",0),("CelticShort1_2_Scab", ixmesh_carry)], itp_merchandise|itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 999 , weight(1.25)|difficulty(8)|spd_rtng(81) | weapon_length(97)|swing_damage(37 , cut) | thrust_damage(14 , pierce),imodbits_sword_high,
[], pict_factions + irish_factions],
["celtic_sword_alt", "Celtic Cav Sword", [("CelticShort1_2",0),("CelticShort1_2_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(19 , pierce),imodbits_sword_high,],

 
#irlandeses y pictos nobles y rey
["pict_princep_swordt3res", "resNorthern Princep Sword", [("Pict_sword",0),("Scab_Pict_Sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1060 , weight(1.25)|difficulty(9)|spd_rtng(89) | weapon_length(91)|swing_damage(33 , cut) | thrust_damage(20 , pierce),imodbits_sword_high,
[], pict_factions + irish_factions],
["pict_princep_swordt3res_alt", "resNorthern Princep Sword", [("Pict_sword",0),("Scab_Pict_Sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1080 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(20 , pierce),imodbits_sword_high,],

["espada_kirkburn", "Nobleman Sword", [("Kirkburn",0),("Kirkburn_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itp_next_item_as_melee, 1080 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(18 , pierce),imodbits_sword_high,
[], pict_factions + irish_factions],
["espada_kirkburn_alt", "Nobleman Sword", [("Kirkburn",0),("Kirkburn_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1080 , weight(1.25)|difficulty(9)|spd_rtng(82) | weapon_length(90)|swing_damage(36 , cut) | thrust_damage(18 , pierce),imodbits_sword_high,],

# #champion sword para determinada elite o unidad, es una espada a dos manos
["celticlongsword2ht3", "Goidel Champion Sword", [("gaelic_champion_sword",0),("gaelic_champion_sword", ixmesh_carry)], itp_merchandise|itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_next_item_as_melee, itc_greatsword|itcf_carry_sword_back,
 1190 , weight(2.35)|difficulty(12)|spd_rtng(79) | weapon_length(102)|swing_damage(42 , cut) | thrust_damage(15 , pierce),imodbits_sword_high,
[], pict_factions + irish_factions],
["celticlongsword2ht3_alt", "Goidel Champion Sword", [("gaelic_champion_sword",0),("gaelic_champion_sword", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back,
 1220 , weight(2.35)|difficulty(11)|spd_rtng(81) | weapon_length(110)|swing_damage(44 , cut) | thrust_damage(17 , pierce),imodbits_sword_high ],

["slotsword2", "unusedSword", [("BL_Sword01_02",0),("BL_Sword01_02", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itp_next_item_as_melee, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], jute_factions],
["slotsword2_alt", "unusedSword1", [("Sword1",0),("Sword1", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itp_next_item_as_melee, 1000 , weight(1.25)|difficulty(8)|spd_rtng(82) | weapon_length(95)|swing_damage(33 , cut) | thrust_damage(17 , pierce),imodbits_sword_high ],

["slotshsword",   "unused Short Sword", [("irish_sword",0),("irish_sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_seax|itcf_carry_sword_left_hip, 1080 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(70)|swing_damage(20 , cut) | thrust_damage(35 , pierce),imodbits_sword,
[], jute_factions],
["slotshsword_alt",   "unused Short Sword", [("irish_sword",0),("irish_sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_seax|itcf_carry_sword_left_hip, 1080 , weight(0.8)|difficulty(2)|spd_rtng(92) | weapon_length(70)|swing_damage(20 , cut) | thrust_damage(35 , pierce),imodbits_sword,],
# ################espadas especiales
["espada_beowulf", "Hrunting", [("beowulfsword",0),("beowulfsword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip,
 1260 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(97)|swing_damage(42 , cut) | thrust_damage(25 , pierce),imodbits_sword_high],
["espada_beowulf_alt", "Hrunting", [("beowulfsword",0),("beowulfsword_scab", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip,
 1260 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(97)|swing_damage(42 , cut) | thrust_damage(25 , pierce),imodbits_sword_high],
["espada_hispania","Erudino", [("le_pictishsword6",0),("le_pictishsword6", ixmesh_carry)], itp_type_one_handed_wpn|itp_always_loot|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip,
 1118 , weight(1.25)|difficulty(10)|spd_rtng(82) | weapon_length(85)|swing_damage(24 , cut) | thrust_damage(35 , pierce),imodbits_sword_high],
["espada_hispania_alt","Erudino", [("le_pictishsword6",0),("le_pictishsword6", ixmesh_carry)], itp_type_one_handed_wpn|itp_always_loot|itp_primary, itc_longsword|itcf_carry_sword_left_hip,1118 , weight(1.25)|difficulty(10)|spd_rtng(82) | weapon_length(85)|swing_damage(24 , cut) | thrust_damage(35 , pierce),imodbits_sword_high],

["espada_banditking", "Bandit King Sword", [("ValsSword1",0),("ValsSword1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1220 , weight(1.25)|difficulty(12)|spd_rtng(83) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(20 , pierce),imodbits_sword_high,],
["espada_banditking_alt", "Bandit King Sword", [("ValsSword1",0),("ValsSword1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1220 , weight(1.25)|difficulty(12)|spd_rtng(83) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(20 , pierce),imodbits_sword_high,],

# #falcata
["espada_quest1", "Virio's Falcata", [("mackie_falcata01",0),("mackie_falcata01", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip, 1260 , weight(1)|difficulty(9)|spd_rtng(90) | weapon_length(89)|swing_damage(50 , cut) | thrust_damage(15 , pierce),imodbits_sword_high],
["espada_quest1_alt", "Virio's Falcata", [("mackie_falcata01",0),("mackie_falcata01", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 1260 , weight(1)|difficulty(9)|spd_rtng(90) | weapon_length(89)|swing_damage(50 , cut) | thrust_damage(15 , pierce),imodbits_sword_high],
#king annan
["espada_suttonhoo_saxon", "Cyning Annan's Sword", [("BL_shSword",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1120 , weight(1.25)|difficulty(12)|spd_rtng(82) | weapon_length(95)|swing_damage(36 , cut) | thrust_damage(20 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_suttonhoo_saxon_alt", "Cyning Annan's Sword", [("BL_shSword",0),("RichSpatha_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1120 , weight(1.25)|difficulty(12)|spd_rtng(82) | weapon_length(95)|swing_damage(39 , cut) | thrust_damage(22 , pierce),imodbits_sword_high,],
#siren song
["espada_arthurian1", "Siren Song", [("bamburgh_sword",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.3)|difficulty(12)|spd_rtng(82) | weapon_length(95)|swing_damage(37 , cut) | thrust_damage(13 , pierce),imodbits_sword_high,
[], briton_factions],
["espada_arthurian1_alt", "Siren Song", [("bamburgh_sword",0),("sword_medieval_b_scabbard2", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1000 , weight(1.3)|difficulty(12)|spd_rtng(82) | weapon_length(95)|swing_damage(40 , cut) | thrust_damage(15 , pierce),imodbits_sword_high,],

["espada_engle1", "Widow Maker", [("le_pictishsword7",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2500 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(16 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_engle1_alt", "Widow Maker", [("le_pictishsword7",0),("RichSpatha_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2500 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(37 , cut) | thrust_damage(18 , pierce),imodbits_sword_high ],

["espada_engle2", "Wyrd", [("le_pictishsword7",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1640 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_engle2_alt", "Wyrd", [("le_pictishsword7",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1640 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,],

["espada_germanic",   "Cniht", [("le_pictishsword7",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1640 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_germanic_alt",   "Cniht", [("le_pictishsword7",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1640 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,],

["espada_briton1",   "Ic eom Eanferth", [("le_pictishsword7",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1640 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], briton_factions],
["espada_briton1_alt",   "Ic eom Eanferth", [("le_pictishsword7",0),("RichSword1_Scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1640 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,],

["espada_arthurian2",   "Ri Petroc's Sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], briton_factions],
["espada_arthurian2_alt",   "Ri Petroc's Sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high ],

["espada_briton2",   "Ri Allech's Sword", [("BL_Sword01_02",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], briton_factions],
["espada_briton2_alt",   "Ri Allech's Sword", [("BL_Sword01_02",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high ],

#espada del rey de kent
["espada_frankish",   "Cyning Eadbald's Sword", [("ValsSword1",0),("ValsSword1_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2500 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(16 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_frankish_alt",   "Cyning Eadbald's Sword", [("ValsSword1",0),("ValsSword1_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2500 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(37 , cut) | thrust_damage(18 , pierce),imodbits_sword_high ],
 
#
["espada_saxon2",   "Cyning Cynegils's Sword", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2500 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(16 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_saxon2_alt",   "Cyning Cynegils's Sword", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2000 , weight(1.25)|difficulty(12)|spd_rtng(82) | weapon_length(95)|swing_damage(37 , cut) | thrust_damage(18 , pierce),imodbits_sword_high ],

["espada_pengwern",   "Ri Cynddylan's Sword", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2500 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(34 , cut) | thrust_damage(16 , pierce),imodbits_sword_high,
[], briton_factions],
["espada_pengwern_alt",   "Ri Cynddylan's Sword", [("RichSpatha",0),("RichSpatha_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 2000 , weight(1.25)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(37 , cut) | thrust_damage(18 , pierce),imodbits_sword_high ],
#chief acaba

["espada_historic1",   "Ri Nowy's Sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_historic1_alt1",   "Ri Nowy's Sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high ],

["espada_light",   "Ri Rhiwallon's Sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_light_alt",   "Ri Rhiwallon's Sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,],


["espada_mythic1",   "Decapitator", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_mythic1_alt",   "Decapitator", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high],


["espada_historic2",   "Archangel", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_historic2_alt",   "Archangel", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high ],


["espada_irish1",   "My Lady Sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_irish1_alt",   "My Lady Sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high ],


["espada_quest2",   "Dyrnwyn", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_quest2_alt",   "Dyrnwyn", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high ],


["espada_pict1", "Ruire Rogallach's Sword", [("Pict_sword",0),("Scab_Pict_Sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1580 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(23 , pierce),imodbits_sword_high,
[], pict_factions + irish_factions],
["espada_pict1_alt", "Ruire Rogallach's Sword", [("Pict_sword",0),("Scab_Pict_Sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1580 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(23 , pierce),imodbits_sword_high,],

["espada_scoti", "Toiseach Gartnait's Sword", [("Kirkburn",0),("Kirkburn_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1580 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(36 , cut) | thrust_damage(22 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_scoti_alt", "Toiseach Gartnait's Sword", [("Kirkburn",0),("Kirkburn_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1580 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(36 , cut) | thrust_damage(22 , pierce),imodbits_sword_high],

#champion sword para rey
["espada_gaelichcampion", "Ruire Congal's Sword", [("gaelic_champion_sword",0),("gaelic_champion_sword", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back, 1520 , weight(2.35)|difficulty(12)|spd_rtng(82) | weapon_length(110)|swing_damage(47 , cut) | thrust_damage(18 , pierce),imodbits_sword_high,
[], saxon_factions + jute_factions + engle_factions],
["espada_gaelichcampion_alt", "Ruire Congal's Sword", [("gaelic_champion_sword",0),("gaelic_champion_sword", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_cant_use_on_horseback, itc_greatsword|itcf_carry_sword_back,1520 , weight(2.35)|difficulty(12)|spd_rtng(82) | weapon_length(110)|swing_damage(47 , cut) | thrust_damage(18 , pierce),imodbits_sword_high ],

["espada_godelicchief", "Ard Ruire Domnaill's Sword", [("Pict_sword",0),("Scab_Pict_Sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1580 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(23 , pierce),imodbits_sword_high,
[], pict_factions + irish_factions],
["espada_godelicchief_alt", "Ard Ruire Domnaill's Sword", [("Pict_sword",0),("Scab_Pict_Sword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1580 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(23 , pierce),imodbits_sword_high,],

["espada_slot1",   "slot for future sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high ],
["espada_slot1_alt",   "slot for future sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high ],
["espada_slot2",   "slot for future sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high ],
["espada_slot2_alt",   "slot for future sword", [("BL_Sword01_01",0),("RichSword3_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 1600 , weight(1.25)|difficulty(9)|spd_rtng(85) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(17 , pierce),imodbits_sword_high ],

###########espadas chief acaba

#####Hachas finales#################################
 ####################################################
###########hachas 1m chief#########################
#todos#gdwrearrangealert
["axe1","Hatchet",[("hatchet",0)],itp_axe1h,itc_axe1h,360,weight(2)|spd_rtng(87)|weapon_length(60)|swing_damage(25,pierce)|thrust_damage(0,blunt),imodbits_axe], #chief modificado
["axe1_alt","Hatchet",[("hatchet",0)],itp_axe1halt,itc_axe1h,360,weight(2)|difficulty(2)|spd_rtng(87)|weapon_length(60)|swing_damage(25,blunt)|thrust_damage(0,blunt),imodbits_axe],#chiefmodificado
["axe3","Sharp Hatchet",[("axefaradon2",0)],itp_axe1h,itc_axe1h,490,weight(1.5)|difficulty(6)|spd_rtng(85)|weapon_length(61)|swing_damage(27,pierce)|thrust_damage(0,pierce),imodbits_axe],
["axe3_alt","Sharp Hatchet",[("axefaradon2",0)],itp_axe1h,itc_axe1h,462,weight(1.5)|difficulty(7)|spd_rtng(85)|weapon_length(66)|swing_damage(25,blunt)|thrust_damage(0,blunt),imodbits_axe],
["axe2_crude","Crude Axe",[("axe_2",0)],itp_axe1h,itc_axe1h,455,weight(2.1)|difficulty(8)|spd_rtng(71)|weapon_length(72)|swing_damage(31,pierce)|thrust_damage(0,pierce),imodbits_axe],
["axe2_crude_alt","Crude alt Axe",[("axe_2",0)],itp_axe1halt,itc_axe1h,495,weight(2.1)|difficulty(8)|spd_rtng(71)|weapon_length(70)|swing_damage(31,blunt)|thrust_damage(0,blunt),imodbits_axe],
["axe4","Fighting Axe",[("axe_c",0)],itp_axe1h,itc_axe1h,490,weight(1.5)|difficulty(7)|spd_rtng(83)|weapon_length(70)|swing_damage(28,pierce)|thrust_damage(0,pierce),imodbits_axe],
["axe4_alt","Fighting Axe",[("axe_c",0)],itp_axe1halt,itc_axe1h,490,weight(1.5)|difficulty(8)|spd_rtng(78)|weapon_length(70)|swing_damage(33,blunt)|thrust_damage(0,blunt),imodbits_axe],
#differentmesh!!alert
["axe2","Cheapaxe",[("gallic_axe_1",0)],itp_axe1h,itc_axe1h,400,weight(1.5)|difficulty(5)|spd_rtng(75)|weapon_length(71)|swing_damage(27,pierce)|thrust_damage(0,pierce),imodbits_axe,],
["axe2_alt","Cheapaxe",[("gallic_axe_1",0)],itp_axe1halt,itc_axe1h,433,weight(1.5)|difficulty(5)|spd_rtng(75)|weapon_length(71)|swing_damage(15,blunt)|thrust_damage(0,blunt),imodbits_axe,],
#invasores#t2=29-32 avg speed 80 length73 cost 530
["axe_englet2","EngleAxe",[("axefaradon3",0)],itp_axe1h,itc_axe1h,528,weight(2)|difficulty(7)|spd_rtng(81)|weapon_length(74)|swing_damage(29,pierce)|thrust_damage(0,pierce),imodbits_axe,[],saxon_factions + jute_factions + engle_factions],
["axe_englet2_alt","EngleAxe",[("axefaradon3",0)],itp_axe1halt,itc_axe1h,569,weight(2)|difficulty(9)|spd_rtng(80)|weapon_length(73)|swing_damage(29,blunt)|thrust_damage(0,blunt),imodbits_axe],
["axe_longfrankisht3",    "Frankish Long Axe",[("vikingaxeb",0)],itp_axe1h,itc_axe1h,651,weight(2.5)|difficulty(9)|spd_rtng(75)|weapon_length(83)|swing_damage(33,pierce)|thrust_damage(0 , pierce),imodbits_axe, [], other_combination],
["axe_longfrankisht3_alt","Frankish Long Axe",[("vikingaxeb",0)],itp_axe1halt,itc_axe1h,481,weight(2)|difficulty(9)|spd_rtng(79)|weapon_length(80)|swing_damage(31,blunt)|thrust_damage(0 , blunt),imodbits_axe, [], other_combination],
["axe_britonbattlet2",   "Frankish Axe", [("frankish_Axe2",0)],itp_axe1h,itc_axe1h,550 , weight(2)|difficulty(7)|spd_rtng(80) | weapon_length(77)|swing_damage(29 , pierce) | thrust_damage(0 , blunt),imodbits_axe, [], other_combination],
["axe_britonbattlet2_alt",   "Frankish Axe", [("frankish_Axe2",0)],itp_axe1halt,itc_axe1h,517 , weight(2)|difficulty(7)|spd_rtng(80) | weapon_length(76)|swing_damage(34 , blunt) | thrust_damage(0 , blunt),imodbits_axe, [], other_combination],
["decor_axet3",   "Elite Axe", [("vikingaxe",0)], itp_axe1h,itc_axe1h,617 , weight(2)|difficulty(8)|spd_rtng(83) | weapon_length(76)|swing_damage(32 , pierce) | thrust_damage(0 , pierce),imodbits_axe, [], saxon_factions + jute_factions + engle_factions],
["decor_axet3_alt",   "Elite Axe", [("vikingaxe",0)],itp_axe1halt,itc_axe1h,597 , weight(2)|difficulty(8)|spd_rtng(80) | weapon_length(76)|swing_damage(31 , blunt) | thrust_damage(0 , blunt),imodbits_axe, [], saxon_factions + jute_factions + engle_factions],
["saxon_axet2",   "Saxon Axe", [("p_axe_1",0)],itp_axe1h,itc_axe1h,561 , weight(2)|difficulty(7)|spd_rtng(84) | weapon_length(74)|swing_damage(29 , pierce) | thrust_damage(0 , pierce),imodbits_axe, [], saxon_factions + jute_factions + engle_factions],
["saxon_axet2_alt",   "Saxon Axe", [("p_axe_1",0)],itp_axe1halt,itc_axe1h,461 , weight(2)|difficulty(9)|spd_rtng(80) | weapon_length(76)|swing_damage(32 , blunt) | thrust_damage(0 , blunt),imodbits_axe, [], saxon_factions + jute_factions + engle_factions],
["germanic_axelongt2",   "Germanic Axe", [("lui_battleaxetwoh",0)],itp_axe1h,itc_axe1h,669 , weight(2)|difficulty(9)|spd_rtng(75) | weapon_length(84)|swing_damage(33 , pierce) | thrust_damage(0 , pierce),imodbits_axe, [], saxon_factions + jute_factions + engle_factions],
["germanic_axelongt2_alt","Germanic Axe", [("lui_battleaxetwoh",0)],itp_axe1halt,itc_axe1h,483 , weight(2)|difficulty(9)|spd_rtng(75) | weapon_length(83)|swing_damage(33 , blunt) | thrust_damage(0 , blunt),imodbits_axe, [], saxon_factions + jute_factions + engle_factions],
#elite, Rey o noble Sajon, anglo o juto
["bearded_axet2", "Bearded Hand Axe", [("le_werkaxt1",0)],itp_axe1h,itc_axe1h,557 , weight(2)|difficulty(9)|spd_rtng(75) | weapon_length(75)|swing_damage(32 , pierce) | thrust_damage(0 , pierce),imodbits_axe ], #chief modificado
["bearded_axet2_alt", "Bearded Hand Axe", [("le_werkaxt1",0)],itp_axe1halt,itc_axe1h,457 , weight(2)|difficulty(9)|spd_rtng(75) | weapon_length(75)|swing_damage(30 , blunt) | thrust_damage(0 , blunt),imodbits_axe ], #chief modificado
["elite_axelong1ht3",   "Decorated Elite Axe", [("talak_nordic_axe",0)],itp_axe1h,itc_axe1h,721 , weight(2.6)|difficulty(10)|spd_rtng(80) | weapon_length(87)|swing_damage(33 , pierce) | thrust_damage(0 , pierce),imodbits_axe, [], saxon_factions + jute_factions + engle_factions],
["elite_axelong1ht3_alt",   "Decorated Elite Axe", [("talak_nordic_axe",0)],itp_axe1halt,itc_axe1h,481 , weight(2)|difficulty(9)|spd_rtng(80) | weapon_length(79)|swing_damage(33 , blunt) | thrust_damage(0 , blunt),imodbits_axe, [], saxon_factions + jute_factions + engle_factions],
["nordic_axet3", "War Axe", [("05einhendi_hedmarkrox",0)],itp_axe1h,itc_axe1h,700 , weight(2)|difficulty(9)|spd_rtng(84) | weapon_length(75)|swing_damage(31 , pierce) | thrust_damage(0 , pierce),imodbits_axe ],
["nordic_axet3_alt", "War Axe", [("05einhendi_hedmarkrox",0)],itp_axe1halt,itc_axe1h,480 , weight(2)|difficulty(9)|spd_rtng(80) | weapon_length(70)|swing_damage(32 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["blackened_axet2", "Gaelic Hand Axe", [("talak_bearded_axe",0)],itp_axe1h,itc_axe1h,567 , weight(2)|difficulty(9)|spd_rtng(80) | weapon_length(75)|swing_damage(30 , pierce) | thrust_damage(0 , pierce),imodbits_axe ],
["blackened_axet2_alt", "Gaelic Hand Axe", [("talak_bearded_axe",0)],itp_axe1halt,itc_axe1h,497 , weight(2)|difficulty(8)|spd_rtng(78) | weapon_length(65)|swing_damage(32 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["slotaxe1", "slotfor axe", [("gallic_axe_1",0)],itp_axe1halt,itc_axe1h, 433 , weight(1.5)|difficulty(8)|spd_rtng(80) | weapon_length(63)|swing_damage(30 , pierce) | thrust_damage(0 , pierce),imodbits_axe],
["slotaxe1_alt", "slotfor axe", [("gallic_axe_1",0)],itp_axe1halt,itc_axe1h, 433 , weight(1.5)|difficulty(8)|spd_rtng(80) | weapon_length(63)|swing_damage(30 , blunt) | thrust_damage(0 , blunt),imodbits_axe], 
["slotaxe2", "slotfor axe", [("gallic_axe_1",0)],itp_axe1halt,itc_axe1h, 433 , weight(1.5)|difficulty(8)|spd_rtng(80) | weapon_length(63)|swing_damage(30 , pierce) | thrust_damage(0 , pierce),imodbits_axe],
["slotaxe2_alt", "slotfor axe", [("gallic_axe_1",0)],itp_axe1halt,itc_axe1h, 433 , weight(1.5)|difficulty(8)|spd_rtng(80) | weapon_length(63)|swing_damage(30 , blunt) | thrust_damage(0 , blunt),imodbits_axe], 
# # #pictos
 
["pictish_waraxet2", "Pictish Hatchet", [("pictish_hatchet",0)],itp_axe1h,itc_axe1h,492, weight(1.5)|difficulty(6)|spd_rtng(81)|weapon_length(68)|swing_damage(28, pierce)| thrust_damage(0, pierce),imodbits_axe,
[], pict_factions + irish_factions],
["pictish_waraxet2_alt", "Pictish Hatchet", [("pictish_hatchet",0)],itp_axe1halt,itc_axe1h, 492, weight(1.5)|difficulty(8)|spd_rtng(79)|weapon_length(61)|swing_damage(33, blunt)|thrust_damage(0 , blunt),imodbits_axe],
["axe_1hlongt2", "Fighting Axe", [("cavalry_Axe",0)],itp_axe1h,itc_axe1h, 695, weight(2.5)|difficulty(10)|spd_rtng(70)|weapon_length(91)|swing_damage(33,pierce)|thrust_damage(0 , pierce),imodbits_axe,
[], pict_factions + irish_factions],
["axe_1hlongt2_alt", "Fighting Axe", [("cavalry_Axe",0)],itp_axe1halt,itc_axe1h, 491, weight(1.5)|difficulty(8)|spd_rtng(80) | weapon_length(60)|swing_damage(34 , blunt) | thrust_damage(0 , blunt),imodbits_axe],
#especiales 1 m
["elite_longaxet4reser", "Penda's Axe", [("talak_bearded_axe",0)],itp_axe1h,itc_axe1h,1897,weight(3)|difficulty(12)|spd_rtng(81) | weapon_length(84)|swing_damage(35 , pierce) | thrust_damage(0 , pierce),imodbits_axe ],
["elite_longaxet4reser_alt", "Penda's Axe", [("talak_bearded_axe",0)],itp_axe1halt,itc_axe1h,1897,weight(2)|difficulty(10)|spd_rtng(81) | weapon_length(83)|swing_damage(35 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["elite_shortaxet4reser", "Special Cav Axe very long", [("cavalry_Axe",0)], itp_axe1h,itc_axe1h, 1392 , weight(2.8)|difficulty(12)|spd_rtng(74) | weapon_length(95)|swing_damage(34 , pierce) | thrust_damage(0 , pierce),imodbits_axe,
[], pict_factions + irish_factions],
["elite_shortaxet4reser_alt", "Special Cav Axe very long", [("cavalry_Axe",0)],itp_axe1halt,itc_axe1h, 1392 , weight(1.5)|difficulty(8)|spd_rtng(82) | weapon_length(66)|swing_damage(38 , blunt) | thrust_damage(0 , blunt),imodbits_axe],


# #####Hachas 2M

["tree_axe2h",   "Two Handed Axe", [("einhendi_haloygox",0)], itp_2hax,itc_2hax,570 , weight(3)|difficulty(10)|spd_rtng(66) | weapon_length(97)|swing_damage(36 , pierce) | thrust_damage(0 , pierce),imodbits_axe ],
["tree_axe2h_alt",   "Two Handed Axe", [("einhendi_haloygox",0)],itp_2haxb,itc_2hax,570 , weight(3)|difficulty(10)|spd_rtng(66) | weapon_length(97)|swing_damage(33 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["battle_axe2ht2",   "Two Handed War Axe", [("01tveirhendr_hedmarkox",0)],itp_2hax,itc_2hax,620 , weight(3)|difficulty(11)|spd_rtng(66) | weapon_length(101)|swing_damage(39 , pierce) | thrust_damage(0 , pierce),imodbits_axe ],
["battle_axe2ht2_alt",   "Two Handed War Axe", [("01tveirhendr_hedmarkox",0)],itp_2haxb,itc_2hax,620 , weight(3)|difficulty(11)|spd_rtng(66) | weapon_length(101)|swing_damage(35 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["war_axe2ht2",   "Two hand LONG war Axe", [("long_axe_c",0)], itp_2hax,itc_2hax,620 , weight(4)|difficulty(13)|spd_rtng(60) | weapon_length(105)|swing_damage(43 , pierce) | thrust_damage(0 , pierce),imodbits_axe ],
["war_axe2ht2_alt",   "Two hand LONG war Axe", [("long_axe_c",0)],itp_2haxb,itc_2hax,620 , weight(4)|difficulty(13)|spd_rtng(60) | weapon_length(105)|swing_damage(40 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["2haxelong",   "slotAxe", [("long_axe_c",0)], itp_2haxuq,itc_2hax,620 , weight(5)|difficulty(13)|spd_rtng(64) | weapon_length(108)|swing_damage(43 , pierce) | thrust_damage(0 , pierce),imodbits_axe ],
["2haxelong_alt",   "slotb Long 2H War Axe alt", [("long_axe_c",0)],itp_2haxb,itc_2hax,620 , weight(5)|difficulty(13)|spd_rtng(64) | weapon_length(108)|swing_damage(43 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],

##chief hachas especiales, hacha 2 m de rey
["elite_axe2ht3resv",   "Thunder", [("01einhendi_trondrox",0)], itp_2haxuq,itc_2hax,2000 , weight(4)|difficulty(14)|spd_rtng(70) | weapon_length(100)|swing_damage(45 , pierce) | thrust_damage(0 , pierce),imodbits_axe,
[], mercenary_factions + other_mercenary_factions],
["elite_axe2ht3resv_alt",   "Thunder", [("01einhendi_trondrox",0)], itp_2haxuqb,itc_2hax, 2000 , weight(4)|difficulty(14)|spd_rtng(70) | weapon_length(100)|swing_damage(40 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["elite1_2haxeresrv",   "Woden Fury", [("03einhendi_trondrox",0)],itp_2haxuq,itc_2hax,2000 , weight(4)|difficulty(14)|spd_rtng(70) | weapon_length(100)|swing_damage(46 , pierce) | thrust_damage(0 , pierce),imodbits_axe ],
["elite1_2haxeresrv_alt",   "Woden Fury", [("03einhendi_trondrox",0)],itp_2haxuqb,itc_2hax,2000 , weight(4)|difficulty(14)|spd_rtng(70) | weapon_length(100)|swing_damage(40 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["elite2_2haxeresrv",  "Thunder", [("02tveirhendr_hedmarkox",0)],itp_2haxuq,itc_2hax,2000 , weight(4)|difficulty(14)|spd_rtng(70) | weapon_length(100)|swing_damage(47 , pierce) | thrust_damage(0 , pierce),imodbits_axe ],
["elite2_2haxeresrv_alt",  "Thunder", [("02tveirhendr_hedmarkox",0)],itp_2haxuqb,itc_2hax,2000 , weight(4)|difficulty(14)|spd_rtng(70) | weapon_length(100)|swing_damage(40 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["elite3_2haxeresrv",   "Manslayer", [("05einhendi_trondrox",0)],itp_2haxuq,itc_2hax,2000 , weight(4)|difficulty(14)|spd_rtng(70) | weapon_length(100)|swing_damage(48 , pierce) | thrust_damage(0 , pierce),imodbits_axe ],
["elite3_2haxeresrv_alt",   "Manslayer", [("05einhendi_trondrox",0)],itp_2haxuqb,itc_2hax,2000 , weight(4)|difficulty(14)|spd_rtng(70) | weapon_length(100)|swing_damage(40 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
# #################hachas 2 m acaba chief ############################
["heavypickaxe", "Heavy Pickaxe 1-2h", [("rusty_pick",0)], itp_2hax,itc_sleg, 960, weight(1.3)|difficulty(8)|spd_rtng(82)|weapon_length(99)|swing_damage(36,pierce)|thrust_damage(12,blunt), imodbits_mace, [], pict_factions + irish_factions ],
["heavypickaxe_alt", "rHeavy Pickaxe 1-2h", [("maul_b",0)], itp_2haxb,itc_sleg, 960, weight(1.3)|difficulty(8)|spd_rtng(82)|weapon_length(99)|swing_damage(36,blunt)|thrust_damage(12,blunt), imodbits_mace, [], pict_factions + irish_factions ],
#####################
["maul1h_blunt", "Small Maul", [("axehammer_1",0)],itp_bln, itc_bln, 300 , weight(2.5)|difficulty(7)|spd_rtng(78) | weapon_length(78)|swing_damage(28 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["maul1h_blunt_alt", "Small Maul", [("axehammer_1",0)], itp_2haxb,itc_2hax, 300 , weight(2.4)|difficulty(7)|spd_rtng(87) | weapon_length(78)|swing_damage(31 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["ironhammerlong", "Long Iron Hammer", [("axehammer_2",0)], itp_bln, itc_bln, 407 , weight(2.4)|difficulty(8)|spd_rtng(78) | weapon_length(91)|swing_damage(30 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["ironhammerlong_alt", "Long Axe Hammer2h", [("axehammer_2",0)], itp_2haxb,itc_2hax, 407 , weight(2.5)|difficulty(8)|spd_rtng(84) | weapon_length(91)|swing_damage(33 , blunt) | thrust_damage(0 , blunt),imodbits_axe ],
["commonhammer_blunt",   "Basic Axe Hammer", [("axehammer",0)], itp_clb, itc_cleaver,208 , weight(2)|difficulty(6)|spd_rtng(88) | weapon_length(72)|swing_damage(25 , blunt) | thrust_damage(0 , blunt),imodbits_axe],
["flail1_blunt", "Cavalry_Flail", [("mace_pear",0), ("flail_scab", ixmesh_carry)], itp_bln, itc_bln, 815, weight(3.7)|difficulty(9)|spd_rtng(76)|weapon_length(102)|swing_damage(30,blunt)|thrust_damage(0,blunt), imodbits_mace, 
 [(ti_on_weapon_attack,
  #(play_sound,"snd_chain"),
  [(store_trigger_param_1, ":attacker_agent_no"),
    (try_begin),
            (multiplayer_is_server),
      (get_max_players, ":num_players"),
            (try_for_range, ":current_player_no", 1, ":num_players"),
                (player_is_active, ":current_player_no"),
        (multiplayer_send_int_to_player, ":current_player_no", action_react_to_flail_attack, ":attacker_agent_no"),
            (try_end),
     (else_try),
          (agent_get_wielded_item_slot_no, ":slot_no", ":attacker_agent_no"),
          (val_add, ":slot_no", bmm_item_1),
          (agent_body_meta_mesh_set_vertex_keys_time_point, ":attacker_agent_no", ":slot_no", 10),
          (agent_set_slot, ":attacker_agent_no", "slot_agent_flail_using", 1),
          (agent_play_sound, ":attacker_agent_no", "snd_draw_flail"),
     (try_end),
  ])]],
["flail1_blunt_alt", "rcavalry_flail", [("flanged_mace",0), ("flail_scab", ixmesh_carry)], itp_ax1huqb, itc_sleg, 710, weight(3.7)|difficulty(9)|spd_rtng(78)|weapon_length(104)|swing_damage(35,blunt)|thrust_damage(0,blunt), imodbits_mace ,
 [(ti_on_weapon_attack,
  #(play_sound,"snd_chain"),(play_sound,"snd_chain"),
  [(store_trigger_param_1, ":attacker_agent_no"),
    (try_begin),
            (multiplayer_is_server),
      (get_max_players, ":num_players"),
            (try_for_range, ":current_player_no", 1, ":num_players"),
                (player_is_active, ":current_player_no"),
        (multiplayer_send_int_to_player, ":current_player_no", action_react_to_flail_attack, ":attacker_agent_no"),
            (try_end),
      (else_try),
      (agent_get_wielded_item_slot_no, ":slot_no", ":attacker_agent_no"),
      (val_add, ":slot_no", bmm_item_1),
      (agent_body_meta_mesh_set_vertex_keys_time_point, ":attacker_agent_no", ":slot_no", 10),
      (agent_set_slot, ":attacker_agent_no", "slot_agent_flail_using", 1),
      (agent_play_sound, ":attacker_agent_no", "snd_draw_flail"),
    (try_end)]),
  #[(ti_on_weapon_attack, [(play_sound,"snd_chain"),
 ]],
["flail2_blunt", "Cavalry Chain Flail", [("flail",0), ("flail_scab", ixmesh_carry)], itp_bln, itc_bln, 990, weight(4.1)|difficulty(10)|spd_rtng(74)|weapon_length(107)|swing_damage(33,blunt)|thrust_damage(0,blunt), imodbits_mace, 
 [(ti_on_weapon_attack,
   [(play_sound,"snd_chain"),(store_trigger_param_1, ":attacker_agent_no"),
    (try_begin),
            (multiplayer_is_server),
      (get_max_players, ":num_players"),
            (try_for_range, ":current_player_no", 1, ":num_players"),
                (player_is_active, ":current_player_no"),
        (multiplayer_send_int_to_player, ":current_player_no", action_react_to_flail_attack, ":attacker_agent_no"),
            (try_end),
     (else_try),
          (agent_get_wielded_item_slot_no, ":slot_no", ":attacker_agent_no"),
          (val_add, ":slot_no", bmm_item_1),
          (agent_body_meta_mesh_set_vertex_keys_time_point, ":attacker_agent_no", ":slot_no", 10),
          (agent_set_slot, ":attacker_agent_no", "slot_agent_flail_using", 1),
          (agent_play_sound, ":attacker_agent_no", "snd_draw_flail"),
     (try_end),
  ])]],
["flail2_blunt_alt", "Cavalry Chain Flail", [("flanged_mace",0), ("flail_scab", ixmesh_carry)], itp_ax1huqb, itc_sleg, 1050, weight(4.1)|difficulty(8)|spd_rtng(75)|weapon_length(107)|swing_damage(38,blunt)|thrust_damage(0,blunt), imodbits_mace ,
 [(ti_on_weapon_attack,
  #(play_sound,"snd_chain"),
  [(play_sound,"snd_chain"),(store_trigger_param_1, ":attacker_agent_no"),
    (try_begin),
            (multiplayer_is_server),
      (get_max_players, ":num_players"),
            (try_for_range, ":current_player_no", 1, ":num_players"),
                (player_is_active, ":current_player_no"),
        (multiplayer_send_int_to_player, ":current_player_no", action_react_to_flail_attack, ":attacker_agent_no"),
            (try_end),
    (else_try),
      (agent_get_wielded_item_slot_no, ":slot_no", ":attacker_agent_no"),
      (val_add, ":slot_no", bmm_item_1),
      (agent_body_meta_mesh_set_vertex_keys_time_point, ":attacker_agent_no", ":slot_no", 10),
      (agent_set_slot, ":attacker_agent_no", "slot_agent_flail_using", 1),
      (agent_play_sound, ":attacker_agent_no", "snd_draw_flail"),
    (try_end)]),
  #[(ti_on_weapon_attack, [(play_sound,"snd_chain"),
 ]],
["flailsteel_blunt", "Heavy Steel Chain Flail", [("flail",0), ("flail_scab", ixmesh_carry)], itp_bln, itc_bln, 2250, weight(4.5)|difficulty(8)|spd_rtng(73)|weapon_length(109)|swing_damage(37,blunt)|thrust_damage(0,blunt), imodbits_mace,
 # [(ti_on_init_item, [(play_sound,"snd_draw_flail"),]),
 [(ti_on_weapon_attack,
  
  [(store_trigger_param_1, ":attacker_agent_no"),
    (try_begin),
            (multiplayer_is_server),
        (get_max_players, ":num_players"),
            (try_for_range, ":current_player_no", 1, ":num_players"),
                (player_is_active, ":current_player_no"),
          (multiplayer_send_int_to_player, ":current_player_no", action_react_to_flail_attack, ":attacker_agent_no"),
            (try_end),
     (else_try),
          (agent_get_wielded_item_slot_no, ":slot_no", ":attacker_agent_no"),
          (val_add, ":slot_no", bmm_item_1),
          (agent_body_meta_mesh_set_vertex_keys_time_point, ":attacker_agent_no", ":slot_no", 10),
          (agent_set_slot, ":attacker_agent_no", "slot_agent_flail_using", 1),
          (agent_play_sound, ":attacker_agent_no", "snd_chain"),
     (try_end),
  ])]],
# from flail script
 # (agent_is_active, ":attacker_agent_no"),
 #          (agent_is_alive, ":attacker_agent_no"),
 #          (agent_is_human, ":attacker_agent_no"),
 #          (agent_get_wielded_item_slot_no, ":slot_no", ":attacker_agent_no"),
 #          (val_add, ":slot_no", bmm_item_1),
 #          (agent_body_meta_mesh_set_vertex_keys_time_point, ":attacker_agent_no", ":slot_no", 10),
 #          (agent_set_slot, ":agent_no", "slot_agent_flail_using", 1),
 #          # (agent_get_bone_position,pos1,":attacker_agent_no",hb_item_r, 1),
 #          # (play_sound_at_position, "snd_chain", pos1),
 #          (agent_play_sound, ":attacker_agent_no", "snd_chain"),
  # [(store_trigger_param_2, ":attacker_agent_no",":attacker_agent_no"),
  #   (call_script, "script_flail_strike", ":attacker_agent_no"),      # (multiplayer_is_server),
    #   (get_max_players, ":num_players"),
    #         (try_for_range, ":current_player_no", 1, ":num_players"),
    #             (player_is_active, ":current_player_no"),
    #     (multiplayer_send_int_to_player, ":current_player_no", action_react_to_flail_attack, ":attacker_agent_no"),
    #         (try_end),
    # (try_end)]),
  #[(ti_on_weapon_attack, [(play_sound,"snd_chain"),
  #   (store_trigger_param_1, ":agent_no"),
  # (call_script, "script_explosion_at_pos1", 500, 50, ":agent_no"),
 
["flailsteel_blunt_alt", "resSteel flail", [("flanged_mace",0), ("flail_scab", ixmesh_carry)],itp_ax1huqb,itc_2hax|itc_cleaver, 1460, weight(4.5)|difficulty(8)|spd_rtng(78)|weapon_length(109)|swing_damage(42,blunt)|thrust_damage(12,blunt), imodbits_mace,
 [(ti_on_weapon_attack,
  #(play_sound,"snd_chain"),
  [(play_sound,"snd_chain"),(store_trigger_param_1, ":attacker_agent_no"),
    (try_begin),
            (multiplayer_is_server),
        (get_max_players, ":num_players"),
            (try_for_range, ":current_player_no", 1, ":num_players"),
                (player_is_active, ":current_player_no"),
        (multiplayer_send_int_to_player, ":current_player_no", action_react_to_flail_attack, ":attacker_agent_no"),
            (try_end),
      (else_try),
        (agent_get_wielded_item_slot_no, ":slot_no", ":attacker_agent_no"),
        (val_add, ":slot_no", bmm_item_1),
        (agent_body_meta_mesh_set_vertex_keys_time_point, ":attacker_agent_no", ":slot_no", 10),
        (agent_set_slot, ":attacker_agent_no", "slot_agent_flail_using", 1),
        (agent_play_sound, ":attacker_agent_no", "snd_draw_flail"),
    (try_end)]),
  #[(ti_on_weapon_attack, [(play_sound,"snd_chain"),
 ]],

# #axe_hammer_long mesh for long splitter
 # ["torch",   "Torches", [("torch_h",0)], itp_type_thrown|itp_merchandise |itp_primary ,itcf_throw_axe, 41 , weight(5)|difficulty(1)|spd_rtng(99) | shoot_speed(20) | thrust_damage(15,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown,
 # [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),]),
 # (ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 20, pos1)])]], ###chief fire arrow cambia para asedios 

["maul_blunt", "Maul_1h", [("maul_b",0)], itp_axe1h|itp_type_two_handed_wpn, itc_bln,550, weight(3.5)|difficulty(9)|spd_rtng(70)|weapon_length(83)|swing_damage(33,blunt)|thrust_damage(0,blunt), imodbits_axe, [], pict_factions + irish_factions ],
["maul_blunt_alt", "rMaul_2h", [("maul_b",0)], itp_2haxb,itc_sleg,550, weight(3.5)|difficulty(9)|spd_rtng(79)|weapon_length(83)|swing_damage(36,blunt)|thrust_damage(12,blunt), imodbits_axe, [], pict_factions + irish_factions ],
["greathammer", "Great Hammer", [("maul_d",0)], itp_sleg,itc_sleg, 530, weight(3.9)|difficulty(11)|spd_rtng(84)|weapon_length(81)|swing_damage(36,blunt)|thrust_damage(0,blunt), imodbits_sword, [], pict_factions + irish_factions ],
["greathammerlong","Great LongHammer", [("maul_d",0)], itp_sleg,itc_sleg,699, weight(4.3)|difficulty(12)|spd_rtng(80) | weapon_length(89)|swing_damage(39 , blunt) | thrust_damage(0 , blunt),imodbits_sword,[], pict_factions + irish_factions],
["militaryhammer", "military_hammer", [("military_hammer",0)], itp_bln, itc_bln, 1, weight(3)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(1), imodbits_mace],
["militaryhammer_alt", "military_hammer", [("maul_b",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960, weight(1.3)|difficulty(8)|spd_rtng(82)|weapon_length(99)|swing_damage(36,blunt)|thrust_damage(12,pierce), imodbits_mace, [], pict_factions + irish_factions ],
["minershammer", "Crude 1H Pick", [("rusty_pick",0)], itp_type_two_handed_wpn|itp_primary|itp_secondary|itp_merchandise |itp_next_item_as_melee, itc_morningstar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960, weight(1.3)|difficulty(8)|spd_rtng(82)|weapon_length(99)|swing_damage(36,blunt)|thrust_damage(12,blunt), imodbits_axe, [], pict_factions + irish_factions ],
["minershammer_alt", "rHammer Pick", [("maul_b",0)],itp_2haxb,itc_2hax, 960, weight(1.3)|difficulty(8)|spd_rtng(82)|weapon_length(99)|swing_damage(36,blunt)|thrust_damage(12,blunt), imodbits_axe, [], pict_factions + irish_factions ],
["fightingpickhammer", "Fighting Pick", [("rusty_pick",0)], itp_type_two_handed_wpn|itp_primary|itp_secondary |itp_next_item_as_melee, itc_morningstar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960, weight(1.3)|difficulty(8)|spd_rtng(82)|weapon_length(99)|swing_damage(36,blunt)|thrust_damage(12,blunt), imodbits_axe, [], pict_factions + irish_factions ],
["fightingpickhammer_alt", "rFighting hammer", [("maul_b",0)], itp_type_two_handed_wpn|itp_primary|itp_secondary, itc_nodachi|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960, weight(1.3)|difficulty(8)|spd_rtng(82)|weapon_length(99)|swing_damage(36,blunt)|thrust_damage(12,blunt), imodbits_axe, [], pict_factions + irish_factions ],
["sledgehammer", "Sledge Hammer", [("maul_c",0)], itp_sleg,itc_sleg,310, weight(4.6)|difficulty(9)|spd_rtng(65)|weapon_length(93)|swing_damage(37,blunt)|thrust_damage(0,blunt), imodbits_sword, [], pict_factions + irish_factions ],
["blunt_slot1",   "rnative", [("maul_c",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , blunt) | thrust_damage(12 , blunt),imodbits_sword,[], pict_factions + irish_factions],
["blunt_slot2",   "rnative", [("maul_c",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , blunt) | thrust_damage(12 , blunt),imodbits_sword,[], pict_factions + irish_factions],
#############hachas acaba#########################################
 ####################################################################
 

###############################spears lanzas y armas de asta empiezan###########################################################
 ##########################################################################################################
# ##todos palos
["staff1",   "Staff",  [("wooden_staff",0)], itp_staff, itc_staff, 70 , weight(1.5)|abundance(60)|difficulty(5)|spd_rtng(97) | weapon_length(126)|swing_damage(18, blunt) | thrust_damage(9 ,  blunt),imodbits_polearm ],
["quarter_staff", "Short Staff",  [("staff_new",0)], itp_staff, itc_staff, 90 , weight(2)|abundance(60)|difficulty(0)|spd_rtng(103) | weapon_length(114)|swing_damage(17 , blunt) | thrust_damage(8 ,  blunt),imodbits_polearm ],
#Tempered added polearms chief#stats match crook
["iron_stafft3", "Iron Staff",  [("iron_staff",0)], itp_staff, itc_staff,450,weight(4)|abundance(60)|difficulty(9)|spd_rtng(87)|weapon_length(115)|swing_damage(26 , blunt) | thrust_damage(12 ,  blunt),imodbits_polearm ],
#Tempered added polearms chief##crook thrust damage from grabpull ise it for noswing
["shepherdsstaff", "Shepherd's Crook", [("shepherds_crook",0)], itp_staff, itc_spear,240,weight(3)|difficulty(7)|spd_rtng(82)|weapon_length(136)|swing_damage(15 , blunt) | thrust_damage(23 , blunt),imodbits_polearm ],
["polearm_stafft4", "Polearm_Mace",  [("mace_long_a",0)], itp_staff, itc_staff, 476, weight(5)|difficulty(9)|spd_rtng(73) | weapon_length(127)|swing_damage(32 , blunt) | thrust_damage(17 ,  blunt), imodbits_polearm ],
#campesinos base
["staff_pitchfork", "Pitch Fork",  [("pitchfork_1",0)], itp_staff, itc_staff,60 ,weight(3.5)|difficulty(6)|spd_rtng(74) | weapon_length(119)|swing_damage(17 , blunt) | thrust_damage(15 ,  blunt),imodbit_bent ],
["spear_sharppitchfork",   "testPitch Fork", [("pitchfork_2",0)], itp_spearalt, itc_spear, 70,weight(2)|difficulty(5)|abundance(0)|spd_rtng(90) | weapon_length(100)|swing_damage(19 , blunt) | thrust_damage(21, pierce),imodbits_polearm ],
["spear_sharppitchfork_alt",   "test staff", [("staff_new",0)], itp_test1hspear, itc_staff,70 ,weight(2)|difficulty(5)|abundance(0)|spd_rtng(90) | weapon_length(100)|swing_damage(19 , blunt) | thrust_damage(21 , blunt),imodbits_polearm ],
#medium spear#tier142 tier2:45 tier 3 about 48
["spear_hvy",   "Heavy Spear", [("fjadraspjot",0)], itp_spear, itc_spear,430,weight(4)|abundance(60)|difficulty(9)|spd_rtng(86)|weapon_length(145)|swing_damage(17,blunt)|thrust_damage(25,pierce),imodbits_polearm ],
["spear_hvy_alt",   "Heavy Spear", [("fjadraspjot",0)], itp_spearalt, itc_staff, 420 , weight(4)|abundance(60)|difficulty(9)|spd_rtng(87) | weapon_length(145)|swing_damage(19 , blunt) | thrust_damage(9 , pierce),imodbits_polearm ],
                                                      
["spear1",   "Spear", [("spjot",0)], itp_spear, itc_spear, 400 , weight(1.4)|abundance(60)|difficulty(7)|spd_rtng(90) | weapon_length(133)|swing_damage(15, blunt) | thrust_damage(26 , pierce),imodbits_polearm ],
["spear1_alt",   "Spear alt", [("spjot",0)], itp_spearalt, itc_staff, 440 , weight(1.4)|abundance(60)|difficulty(4)|spd_rtng(92) | weapon_length(133)|swing_damage(17 , blunt) | thrust_damage(9 , pierce),imodbits_polearm ],

["spear2",   "1testspear1", [("saxon2hspear",0)], itp_test2hspear, itc_spear, 400 , weight(1.4)|abundance(6)|spd_rtng(90) | weapon_length(144)|swing_damage(20, blunt) | thrust_damage(22, pierce),imodbits_polearm ],
["spear2_alt",   "2testspear2alt", [("hasta",0)], itp_test2hspear, itc_staff, 440 , weight(1.4)|abundance(0)|difficulty(6)|spd_rtng(90) | weapon_length(144)|swing_damage(17 , blunt) | thrust_damage(23 , pierce),imodbits_polearm ],
["spearlight",   "Light Spear", [("hoggkesja",0)], itp_spear, itc_spear, 165 , weight(1.3)|abundance(67)|difficulty(6)|spd_rtng(102) | weapon_length(125)|swing_damage(13, blunt) | thrust_damage(27 , pierce),imodbits_polearm ],
["spearlight_alt",   "Light Spear alt", [("hoggkesja",0)], itp_spearalt, itc_staff, 160 , weight(1.3)|abundance(67)|difficulty(7)|spd_rtng(102) | weapon_length(125)|swing_damage(15 , blunt) | thrust_damage(9 , pierce),imodbits_polearm ],
["spearboar",   "Boar Spear", [("svia2",0)], itp_spear, itc_spear, 521 , weight(2)|abundance(60)|difficulty(8)|spd_rtng(84) | weapon_length(131)|swing_damage(19 , blunt) | thrust_damage(26, pierce),imodbits_polearm ],
["spearboar_alt",   "Boar Spear", [("svia2",0)], itp_spearalt, itc_staff, 521 , weight(2)|abundance(50)|difficulty(8)|spd_rtng(85) | weapon_length(131)|swing_damage(20 , blunt) | thrust_damage(9, pierce),imodbits_polearm ],
#long spear
["spearlong",   "Basic Cav Spear", [("spjotkesja",0)], itp_spear, itc_spear, 480 , weight(2.10)|abundance(50)|difficulty(8)|spd_rtng(99) | weapon_length(185)|swing_damage(12 , blunt) | thrust_damage(30 , pierce),imodbits_polearm ],
["spearlong_alt",   "Basic Cav Spear", [("spjotkesja",0)], itp_spearalt, itc_staff,  180 , weight(2.1)|abundance(50)|difficulty(8)|spd_rtng(99) | weapon_length(185)|swing_damage(15 , blunt) | thrust_damage(9 , pierce),imodbits_polearm ],
["spearwarlong",   "Long War Spear", [("langr_bryntvari",0)], itp_pike, itc_pike, 570, weight(3.08)|abundance(60)|difficulty(10)|spd_rtng(92) | weapon_length(200)|swing_damage(12 , blunt) | thrust_damage(33 , pierce),imodbits_polearm ],
["spearwarlong_alt",   "Long War Spear", [("langr_bryntvari",0)], itp_spearalt, itc_staff, 495 , weight(3.08)|abundance(30)|difficulty(10)|spd_rtng(95) | weapon_length(200)|swing_damage(13 , blunt) | thrust_damage(9 , pierce),imodbits_polearm ],
#britones lanzas#gdw use the hasta mesh for another speartier2blades
["spear_hasta",   "Hasta", [("hasta",0)], itp_spear, itc_spear, 540, weight(3)|difficulty(10)|spd_rtng(88) | weapon_length(145)|swing_damage(17 , blunt) | thrust_damage(28 , pierce),imodbits_polearm,
[], briton_factions],
["spear_hasta_alt",   "Hasta", [("hasta",0)], itp_spearalt, itc_staff, 510, weight(3)|difficulty(10)|spd_rtng(96) | weapon_length(182)|swing_damage(14 , blunt) | thrust_damage(9 , pierce),imodbits_polearm,],
["spear_blade1t2",   "Blade Spear", [("ped_heavy_spear_long",0)], itp_bladespear, itc_bladespear, 595 , weight(2.5)|difficulty(10)|spd_rtng(88) | weapon_length(132)|swing_damage(23 , cut) | thrust_damage(23 , pierce),imodbits_polearm,
[], briton_factions],
["spear_blade1t2_alt",  "Long Blade Spear", [("ped_heavy_spear_long",0)], itp_spearalt, itc_staff, 470 , weight(2.5)|difficulty(10)|spd_rtng(88) | weapon_length(132)|swing_damage(13 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["spear_blade2t2",   "Roman long hasta 2", [("roman_spear_2",0)], itp_bladespear, itc_bladespear, 569 , weight(3)|difficulty(10)|spd_rtng(86)|abundance(20) | weapon_length(148)|swing_damage(20 , cut) | thrust_damage(26 , pierce),imodbits_polearm,
[], briton_factions],
["spear_blade2t2_alt",   "Roman long hasta 2alt", [("roman_spear_2",0)], itp_spearalt, itc_staff, 567 , weight(3)|difficulty(10)|spd_rtng(86)|abundance(20) | weapon_length(148)|swing_damage(19, blunt) | thrust_damage(11 , pierce),imodbits_polearm],
# #spear de dos manos britona
["spear_briton2ht3",   "Briton Two-Handed Blade Spear", [("langr_hoggspjott1",0)], itp_bladespear, itc_bladespear, 690 , weight(3)|abundance(20)|difficulty(11)|spd_rtng(88) | weapon_length(137)|swing_damage(24 , cut) | thrust_damage(25 , pierce),imodbits_polearm,
[], briton_factions],
["spear_briton2ht3_alt",   "Briton Two-Handed Blade Spear", [("langr_hoggspjott1",0)], itp_spearalt, itc_bladespear, 690 , weight(3)|abundance(20)|difficulty(11)|spd_rtng(88) | weapon_length(137)|swing_damage(20 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["spear_britonshortt2",   "Briton Short Spear", [("01atgeirr1",0)], itp_spear, itc_spear, 380 , weight(1.1)|abundance(40)|difficulty(7)|spd_rtng(112) | weapon_length(118)|swing_damage(13 , blunt) | thrust_damage(31 , pierce),imodbits_polearm,
[], briton_factions],
["spear_britonshortt2_alt",   "Briton Short Spear", [("01atgeirr1",0)], itp_spearalt, itc_staff, 360 , weight(0.69)|abundance(60)|difficulty(0)|spd_rtng(107) | weapon_length(114)|swing_damage(12 , blunt) | thrust_damage(6 , pierce),imodbits_polearm],
["spear_britonmedt2",  "Briton Medium Spear", [("02spjot",0)], itp_spear, itc_spear, 430 , weight(1.4)|abundance(40)|difficulty(8)|spd_rtng(94) | weapon_length(142)|swing_damage(15 , blunt) | thrust_damage(30 , pierce),imodbits_polearm,
[], briton_factions],
["spear_britonmedt2_alt",  "Briton Medium Spear", [("02spjot",0)], itp_spearalt, itc_staff, 440 , weight(1.4)|abundance(60)|difficulty(4)|spd_rtng(94) | weapon_length(142)|swing_damage(16 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["spear_britonlight",   "Briton Light Spear", [("01krokaspjott2",0)], itp_spear, itc_spear, 250 , weight(0.7)|abundance(66)|difficulty(6)|spd_rtng(105) | weapon_length(119)|swing_damage(11 , blunt) | thrust_damage(30 , pierce),imodbits_polearm,
[], briton_factions],
["spear_britonlight_alt",   "Briton Light Spear", [("01krokaspjott2",0)], itp_spearalt, itc_staff, 260 , weight(0.7)|abundance(60)|difficulty(6)|spd_rtng(97) | weapon_length(155)|swing_damage(13 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["spear_briton_longt2", "Briton Cav Spear", [("01langr_bryntvari",0)], itp_pike, itc_spear, 525 , weight(3)|abundance(47)|difficulty(10)|spd_rtng(91) | weapon_length(190)|swing_damage(13 , blunt) | thrust_damage(32 , pierce),imodbits_polearm,
[], briton_factions],
["spear_briton_longt2_alt", "Briton Long Spear", [("01langr_bryntvari",0)], itp_spearalt, itc_staff, 495 , weight(3)|abundance(60)|difficulty(10)|spd_rtng(95) | weapon_length(190)|swing_damage(15 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["longspeart3",   "Briton Pike", [("02spjotkesja",0)], itp_spear, itc_spear, 540 , weight(2.55)|abundance(50)|difficulty(8)|spd_rtng(90) | weapon_length(230)|swing_damage(14 , blunt) | thrust_damage(34 , pierce),imodbits_polearm,
[], briton_factions],
["longspeart3_alt",   "Long Spear", [("02spjotkesja",0)], itp_spearalt, itc_staff, 180 , weight(2.55)|abundance(60)|difficulty(8)|spd_rtng(90) | weapon_length(230)|swing_damage(16 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
# #saxon 2 h spear, lanza a dos manos
["twohand_speart3",   "Saxon Two-Handed Blade Spear", [("saxon2hspear",0)], itp_bladespear, itc_bladespear, 600 , weight(3)|difficulty(11)|spd_rtng(88) | weapon_length(139)|swing_damage(23 , cut) | thrust_damage(25 , pierce),imodbits_polearm,
[], saxon_factions + jute_factions + engle_factions],
#spear 2 h cstadi con hoja larga como cuchilla
["twohand_speart3_alt",   "Two-Handed Spear", [("saxon2hspear",0)], itp_spearalt, itc_staff, 400 , weight(4)|difficulty(0)|spd_rtng(85) | weapon_length(199)|swing_damage(21 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["saxon_medium_speart2", "Saxon Spear", [("saxon_spear",0)], itp_spear, itc_spear, 480, weight(2)|difficulty(8)|spd_rtng(89)|weapon_length(140)|swing_damage(15,blunt)|thrust_damage(30,pierce), imodbits_polearm,
[], saxon_factions + jute_factions + engle_factions],
["saxon_medium_speart2_alt", "Saxon Spear", [("saxon_spear",0)], itp_spearalt, itc_staff, 480, weight(2)|difficulty(8)|spd_rtng(90)|weapon_length(140)|swing_damage(16,blunt)|thrust_damage(9,pierce), imodbits_polearm ],
 #1 manoasdfasdf
["germanshortspeart2",   "German Short Spear", [("atgeirr1",0)], itp_spear, itc_spear, 480 , weight(0.69)|abundance(60)|difficulty(7)|spd_rtng(118) | weapon_length(116)|swing_damage(12 , blunt) | thrust_damage(31 , pierce),imodbits_polearm,
[], saxon_factions + jute_factions + engle_factions],
["germanshortspeart2_alt",   "German Short Spear", [("atgeirr1",0)], itp_spearalt, itc_staff, 360 , weight(0.69)|abundance(60)|difficulty(0)|spd_rtng(107) | weapon_length(114)|swing_damage(13 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["engle_speart2",   "Saxon Spear", [("saxon_spear",0)], itp_spear, itc_spear, 510 , weight(2)|difficulty(10)|spd_rtng(88) | weapon_length(149)|swing_damage(15 , blunt) | thrust_damage(32 , pierce),imodbits_polearm,
[], saxon_factions + jute_factions + engle_factions],
["engle_speart2_alt",   "Saxon Spear", [("saxon_spear",0)], itp_spearalt, itc_staff, 440 , weight(2)|difficulty(10)|spd_rtng(88) | weapon_length(149)|swing_damage(16 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["germanlongspeart2",   "Saxon Long Spear", [("langr_svia",0)],itp_spear, itc_spear, 590 , weight(3)|difficulty(10)|spd_rtng(89) | weapon_length(220)|swing_damage(15 , blunt) | thrust_damage(30 , pierce),imodbits_polearm,
[], saxon_factions + jute_factions + engle_factions],
["germanlongspeart2_alt",   "Saxon Long Spear", [("langr_svia",0)],itp_spearalt, itc_staff, 500 , weight(3.25)|difficulty(8)|spd_rtng(95) | weapon_length(235)|swing_damage(17 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
# Goedendag Irish y pictos
["hunting_spear", "Hunting Spear", [("04hoggkesja",0)], itp_spear, itc_spear, 160 , weight(1.7)|abundance(60)|difficulty(6)|spd_rtng(97) | weapon_length(125)|swing_damage(14 , blunt) | thrust_damage(26 , pierce),imodbits_polearm,
[], pict_factions + irish_factions],
["hunting_spear_alt", "Hunting Spear", [("04hoggkesja",0)], itp_spearalt, itc_staff, 160 , weight(1.7)|abundance(60)|difficulty(7)|spd_rtng(97) | weapon_length(157)|swing_damage(15 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["medium_speaript3",   "Elite Gael Med Spear", [("02bryntvari",0)], itp_spear, itc_spear, 580 , weight(2.25)|difficulty(9)|abundance(20)|spd_rtng(93) | weapon_length(140)|swing_damage(16 , blunt) | thrust_damage(32 , pierce),imodbits_polearm,
[], pict_factions + irish_factions],
["medium_speaript3_alt",   "Medium Spear", [("02bryntvari",0)], itp_spearalt, itc_staff,580 , weight(2.25)|difficulty(6)|spd_rtng(93) | weapon_length(140)|swing_damage(17 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["pictish_boar_speart2",   "Pictish Boar Spear", [("02svia2",0)], itp_spear, itc_spear,425 , weight(3)|abundance(50)|difficulty(8)|spd_rtng(88) | weapon_length(135)|swing_damage(18 , blunt) | thrust_damage(27 , pierce),imodbits_polearm,
[], pict_factions + irish_factions],
["pictish_boar_speart2_alt",   "Pictish Boar Spear", [("02svia2",0)], itp_spearalt, itc_staff,425 , weight(3)|abundance(60)|difficulty(6)|spd_rtng(88) | weapon_length(145)|swing_damage(19 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["warspear_godelict3",   "Godelic Elite Spear", [("03bryntvari",0)], itp_spearunique, itc_spear,580 , weight(2.9)|difficulty(6)|spd_rtng(95) | weapon_length(152)|swing_damage(16 , blunt) | thrust_damage(32 , pierce),imodbits_polearm,
[], pict_factions + irish_factions],
["warspear_godelict3_alt",   "Godelic Elite Spear", [("03bryntvari",0)], itp_spearalt, itc_staff, 180 , weight(2.25)|difficulty(6)|spd_rtng(95) | weapon_length(152)|swing_damage(17 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["spear_lightgael",   "Godelic Light Spear", [("05hoggkesja",0)], itp_spear, itc_spear,160 , weight(1.7)|abundance(60)|difficulty(6)|spd_rtng(115) | weapon_length(117)|swing_damage(12 , blunt) | thrust_damage(28 , pierce),imodbits_polearm,
[], pict_factions + irish_factions],
["spear_lightgael_alt",   "Godelic Light Spear", [("05hoggkesja",0)], itp_spearalt, itc_staff,160 , weight(1.7)|abundance(60)|difficulty(7)|spd_rtng(97) | weapon_length(157)|swing_damage(13 , blunt) | thrust_damage(9 , pierce),imodbits_polearm],
["long_speaript2",   "Godelic Pike", [("fjadraspjot",0)], itp_pike, itc_spear, 440 , weight(4)|abundance(60)|difficulty(9)|spd_rtng(92) | weapon_length(225)|swing_damage(15 , blunt) | thrust_damage(30 , pierce),imodbits_polearm,
[], pict_factions + irish_factions],
["long_speaript2_alt",   "Godelic Long Spear", [("fjadraspjot",0)], itp_spearalt, itc_staff, 420 , weight(4)|abundance(60)|difficulty(9)|spd_rtng(97) | weapon_length(225)|swing_damage(16 , blunt) | thrust_damage(8 , pierce),imodbits_polearm],
["spearslot1",   "Third testSpear", [("spjot",0)], itp_test1hspear, itc_spear, 460 , weight(2.25)|abundance(0)|difficulty(6)|spd_rtng(90) | weapon_length(144)|swing_damage(13 , blunt) | thrust_damage(28 , pierce),imodbits_polearm ],
["spearslot1_alt",   "Fourthtest Spear", [("hoggkesja",0)], itp_test1hspear, itc_spear,  460 , weight(2.25)|abundance(0)|difficulty(6)|spd_rtng(90) | weapon_length(144)|swing_damage(20 , blunt) | thrust_damage(20 , pierce),imodbits_polearm ],
["spearslot2", "Fifth testspear", [("02svia2",0)],itp_spearalt, itc_spear, 199, weight(2.25)|abundance(0)|difficulty(6)|spd_rtng(90) | weapon_length(144)|swing_damage(13 , blunt) | thrust_damage(30 , pierce), imodbits_polearm ],
["spearslot2_alt", "Sixth testspear2h", [("04hoggkesja",0)], itp_spearalt, itc_staff, 199, weight(2.25)|abundance(0)|difficulty(6)|spd_rtng(90) | weapon_length(144)|swing_damage(14 , blunt) | thrust_damage(31 , pierce),imodbits_polearm ],
#long meshes: saxon2hspear saxon_spear  01langr_bryntvari  hasta  spjotkesja-longspear
["spear_cavalrylance1",   "Dawn Ray Cav", [("krokaspjott1",0)], itp_spear, itc_spear, 580, weight(2.55)|abundance(20)|spd_rtng(96) | weapon_length(185)|swing_damage(13 , blunt) | thrust_damage(32 , pierce),imodbit_balanced ],
["spear_cavalrylance1_alt",   "Dawn Ray Cav", [("krokaspjott1",0)], itp_spearalt, itc_staff, 260 , weight(2.55)|abundance(20)|spd_rtng(96) | weapon_length(185)|swing_damage(14 , blunt) | thrust_damage(13 , pierce),imodbit_balanced ],
#lanzas magicas especiales reyes y nobles  #short meshes: 02svia2  05bryntvari2  svia2 04hoggkesja-  01krokaspjott2
["spear_elitequest1",   "rHope LongWarrior", [("02krokaspjott1",0)], itp_spearalt, itc_spear, 360 , weight(2.55)|difficulty(5)|spd_rtng(90) | weapon_length(185)|swing_damage(13 , blunt) | thrust_damage(30 , pierce),imodbit_balanced ],
["spear_elitequest1_alt",   "rHopelong3", [("ped_heavy_spear_long",0)], itp_spearalt, itc_staff, 360 , weight(2.55)|difficulty(8)|spd_rtng(90) | weapon_length(185)|swing_damage(17 , blunt) | thrust_damage(31 , pierce),imodbit_balanced ],
["spear_elitequest2",   "s7britonwarsp", [("01langr_bryntvari",0)], itp_spearalt, itc_spear, 360 , weight(2.55)|difficulty(6)|spd_rtng(90) | weapon_length(200)|swing_damage(15 , blunt) | thrust_damage(33 , pierce),imodbit_balanced ],
["spear_elitequest2_alt",   "s8reBreath of Dragon", [("05bryntvari2",0)], itp_spearalt, itc_staff, 360 , weight(2.55)|difficulty(6)|spd_rtng(90) | weapon_length(200)|swing_damage(15 , blunt) | thrust_damage(34 , pierce),imodbit_balanced ],
#05bryntvari2 was breathfjadraspjot01langr_bryntvari
["spear_elitequest3",   "s9rRaven", [("fjadraspjot",0)], itp_test2hspear, itc_spear, 360 , weight(2.55)|difficulty(6)|spd_rtng(115) | weapon_length(144)|swing_damage(22 , blunt) | thrust_damage(18 , pierce),imodbit_balanced ],
["spear_elitequest3_alt",   "s10roman", [("roman_spear_2",0)], itp_spearalt, itc_staff, 360 , weight(2.55)|difficulty(6)|spd_rtng(115) | weapon_length(144)|swing_damage(20 , blunt) | thrust_damage(25 , pierce),imodbit_balanced ],
#lanzas especiales chief
["spear_elitequest4","Neko's Spear", [("krokaspjott1",0)] , itp_spearunique, itc_spear, 1060,weight(2.55)|difficulty(6)|spd_rtng(90) | weapon_length(180)|swing_damage(14 , blunt) | thrust_damage(32 , pierce),imodbit_balanced ],
["spear_elitequest4_alt","Neko's Spear", [("krokaspjott1",0)] , itp_spearalt, itc_staff, 1060,weight(2.55)|difficulty(6)|spd_rtng(90) | weapon_length(180)|swing_damage(14 , blunt) | thrust_damage(32 , pierce),imodbit_balanced ],
#####estandartes finales chief####
 #############################
#sajon, anglo y juto banner
["wessexbanner1",   "Banner", [("wessexbanner1",0)],itp_banner, itc_banner, 550 , weight(4)|difficulty(8)|spd_rtng(70) | weapon_length(148)|swing_damage(28 , blunt) | thrust_damage(10 , blunt),imodbits_polearm ],
["cavalrybannert2",   "Cavalry Banner", [("wessexbanner2",0)], itp_spear, itc_spear, 730 , weight(4)|difficulty(2)|spd_rtng(81) | weapon_length(135)|swing_damage(13 , blunt) | thrust_damage(30 , pierce),imodbits_polearm ],
["cavalrybannert2_alt",   "Cavalry Banner", [("wessexbanner2",0)], itp_spearalt, itc_staff, 780 , weight(2)|difficulty(8)|spd_rtng(80) | weapon_length(135)|swing_damage(14 , blunt) | thrust_damage(9 , blunt),imodbits_polearm ],

["spearbannert2",   "Fighting Banner", [("wessexbanner3",0)], itp_banner, itc_spear, 690 , weight(2)|difficulty(8)|spd_rtng(79) | weapon_length(139)|swing_damage(18 , blunt) | thrust_damage(25 , pierce),imodbits_polearm ],
["spearbannert2_alt",   "Fighting Banner", [("wessexbanner3",0)], itp_spearalt, itc_staff, 780 , weight(2)|difficulty(8)|spd_rtng(79) | weapon_length(139)|swing_damage(19 , blunt) | thrust_damage(9 , blunt),imodbits_polearm ],

["spearbanner4",   "Banner", [("wessexbanner4",0)],itp_banner, itc_spear, 640 , weight(5)|difficulty(8)|spd_rtng(70) | weapon_length(148)|swing_damage(18 , blunt) | thrust_damage(6 , pierce),imodbits_polearm ],
["spearbanner4_alt",   "Banner", [("wessexbanner4",0)],itp_spearalt, itc_staff, 650 , weight(5)|difficulty(8)|spd_rtng(70) | weapon_length(149)|swing_damage(18 , blunt) | thrust_damage(6 , blunt),imodbits_polearm ],
["spearbanner5",   "Banner", [("wessexbanner5",0)], itp_banner, itc_spear, 648 , weight(5)|difficulty(8)|spd_rtng(75) | weapon_length(149)|swing_damage(18 , blunt) | thrust_damage(6 , pierce),imodbits_polearm ],
["spearbanner5_alt",   "Banner", [("wessexbanner5",0)], itp_spearalt, itc_staff, 638 , weight(5)|difficulty(8)|spd_rtng(75) | weapon_length(149)|swing_damage(18 , blunt) | thrust_damage(6 , blunt),imodbits_polearm ],
["wessexbanner6",   "Banner", [("wessexbanner6",0)], itp_banner, itc_banner, 550 , weight(5)|difficulty(8)|spd_rtng(70) | weapon_length(149)|swing_damage(18 , blunt) | thrust_damage(6 , pierce),imodbits_polearm ],
["wessexbanner7",   "Banner", [("wessexbanner7",0)],  itp_banner, itc_banner, 550 , weight(5)|difficulty(8)|spd_rtng(70) | weapon_length(149)|swing_damage(18 , blunt) | thrust_damage(6, pierce),imodbits_polearm ],
["wessexbanner8",   "Banner", [("wessexbanner8",0)],  itp_banner, itc_banner, 550 , weight(5)|difficulty(8)|spd_rtng(70) | weapon_length(149)|swing_damage(18 , blunt) | thrust_damage(6 , pierce),imodbits_polearm ],
["heraldicbannert3",   "Heraldic Banner", [("personalbanner",0)],itp_spear, itc_spear, 820 , weight(5)|difficulty(8)|spd_rtng(85) | weapon_length(135)|swing_damage(22 , blunt) | thrust_damage(26 , pierce),imodbits_polearm, 
[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],
["heraldicbannert3_alt",   "Heraldic Banner", [("personalbanner",0)], itp_spearalt, itc_staff, 780 , weight(2)|difficulty(8)|spd_rtng(85) | weapon_length(135)|swing_damage(24 , blunt) | thrust_damage(12 , blunt),imodbits_polearm, ],
["wessexbanner9",   "Banner", [("wessexbanner9",0)],  itp_banner, itc_staff, 550 , weight(4)|difficulty(5)|spd_rtng(70) | weapon_length(149)|swing_damage(18 , blunt) | thrust_damage(9, pierce),imodbits_none ],
#todo correcto pero problemas para ajustar textura, pasable por ahora

#####estandartes finales acaba####
 ##############################
###############lanzas chief acaba #######################################
###########################################################################
]

######################### Shields #########################
###########################################################

items += module_items_shields.items

items += [
################## Ranged items ##################

["darts", "darts", [("dart_b",0),("dart_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 85 , weight(2)|difficulty(1)|spd_rtng(90) | shoot_speed(30) | thrust_damage(23 , pierce)|max_ammo(7)|weapon_length(32)|accuracy(80),imodbits_thrown,missile_distance_trigger ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(6, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown,missile_distance_trigger ],
["throwing_daggers_alt", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(6, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown,missile_distance_trigger ],

["javelins", "Javelins", [("atgeirr1",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
200, weight(2)|difficulty(1)|spd_rtng(75) | shoot_speed(28) | thrust_damage(31 , cut)|max_ammo(4)|weapon_length(65)|accuracy(99),imodbits_thrown,missile_distance_trigger ],
["javelins_melee", "Javelin", [("atgeirr1",0)], itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
200, weight(2)|difficulty(0)|spd_rtng(82) |swing_damage(9, cut)| thrust_damage(25, cut)|weapon_length(65),imodbits_polearm ],

["wooden_javelins", "Wooden Javelins", [("kijek",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_next_item_as_melee ,itcf_throw_javelin,
190, weight(2)|difficulty(0)|spd_rtng(85) | shoot_speed(33) | thrust_damage(27 , cut)|max_ammo(4)|weapon_length(60)|accuracy(90),imodbits_thrown,missile_distance_trigger ],
["wooden_javelinsmelee", "Wooden Javelin", [("kijek",0)], itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
200, weight(2)|difficulty(0)|spd_rtng(88) |swing_damage(9, cut)| thrust_damage(20, cut)|weapon_length(65),imodbits_polearm ],

["cavaljavelins", "Horsemen Javelins", [("02atgeirr1",0),("javelins_quiver_new", ixmesh_carry)], itp_merchandise|itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
300, weight(4)|difficulty(2)|spd_rtng(75) | shoot_speed(28) | thrust_damage(31 , cut)|max_ammo(6)|weapon_length(65)|accuracy(95),imodbits_thrown,missile_distance_trigger ],
["cavaljavelins_melee", "Horseman Javelin", [("02atgeirr1",0)], itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
300, weight(4)|difficulty(0)|spd_rtng(82) |swing_damage(9, cut)| thrust_damage(25, cut)|weapon_length(65),imodbits_polearm ],

["throwing_spear", "Throwing Spears", [("kastad_krokaspjott",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
425, weight(2)|difficulty(1)|spd_rtng(65) | shoot_speed(17) | thrust_damage(41 , pierce)|max_ammo(1)|weapon_length(100)|accuracy(85),imodbits_thrown,missile_distance_trigger ],
["throwing_spear_melee", "Throwing Spear", [("kastad_krokaspjott",0)],itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
425, weight(2)|difficulty(2)|spd_rtng(80) | swing_damage(10, cut) | thrust_damage(31 , pierce)|weapon_length(100),imodbits_thrown ],

["angons", "Angons", [("angon1",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
425, weight(2)|difficulty(2)|spd_rtng(65) | shoot_speed(17) | thrust_damage(41 , pierce)|max_ammo(1)|weapon_length(100)|accuracy(85),imodbits_thrown,missile_distance_trigger ],
["angons_melee", "Angon", [("angon1",0)],itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
425, weight(2)|difficulty(2)|spd_rtng(80) | swing_damage(10, cut) | thrust_damage(31 , pierce)|weapon_length(100),imodbits_thrown ],

["angonst2", "Angons", [("05kastad_krokaspjott",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
415, weight(2)|difficulty(2)|spd_rtng(75) | shoot_speed(19) | thrust_damage(37 , pierce)|max_ammo(1)|weapon_length(100)|accuracy(85),imodbits_thrown,missile_distance_trigger ],
["angonst2_melee", "Angon", [("05kastad_krokaspjott",0)],itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
415, weight(2)|difficulty(2)|spd_rtng(80) | swing_damage(10, cut) | thrust_damage(31 , pierce)|weapon_length(100),imodbits_thrown ],

["angonst3", "Angons", [("kastspjottmidtaggir",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
435, weight(2)|difficulty(2)|spd_rtng(60) | shoot_speed(15) | thrust_damage(44 , pierce)|max_ammo(1)|weapon_length(100)|accuracy(85),imodbits_thrown,missile_distance_trigger ],
["angonst3_melee", "Angon", [("kastspjottmidtaggir",0)],itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
435, weight(2)|difficulty(2)|spd_rtng(80) | swing_damage(10, cut) | thrust_damage(31 , pierce)|weapon_length(100),imodbits_thrown ],

["gaebolgajavel", "Gae Bolga", [("01kastad_krokaspjott",0)], itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
2225, weight(3)|difficulty(3)|spd_rtng(75) | shoot_speed(25) | thrust_damage(60 , pierce)|max_ammo(1)|weapon_length(105)|accuracy(85),imodbit_balanced ,missile_distance_trigger],
["gaebolgajavel_melee", "Gae Bolga", [("01kastad_krokaspjott",0)],itp_type_polearm|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry , itc_staff,
2225, weight(3)|difficulty(2)|spd_rtng(80) | swing_damage(7, cut) | thrust_damage(33 , pierce)|weapon_length(105),imodbit_balanced ],

["slotjavelins", "future weapon", [("atgeirr1",0)], itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
200, weight(2)|difficulty(1)|spd_rtng(75) | shoot_speed(28) | thrust_damage(31 , cut)|max_ammo(4)|weapon_length(65)|accuracy(99),imodbits_thrown,missile_distance_trigger ],
["slotjavelins_melee", "future weapon", [("atgeirr1",0)], itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
200, weight(2)|difficulty(0)|spd_rtng(82) |swing_damage(9, cut)| thrust_damage(25, cut)|weapon_length(65),imodbits_polearm ],

["slot2javelins", "future weapon", [("atgeirr1",0)], itp_type_thrown |itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee ,itcf_throw_javelin,
200, weight(2)|difficulty(1)|spd_rtng(75) | shoot_speed(28) | thrust_damage(31 , cut)|max_ammo(4)|weapon_length(65)|accuracy(99),imodbits_thrown,missile_distance_trigger ],
["slot2javelins_melee", "future weapon", [("atgeirr1",0)], itp_type_polearm|itp_primary|itp_secondary|itp_wooden_parry , itc_staff,
200, weight(2)|difficulty(0)|spd_rtng(82) |swing_damage(9, cut)| thrust_damage(25, cut)|weapon_length(65),imodbits_polearm ],

#todo: Heavy throwing Spear

["stones1", "Throwing Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary ,itcf_throw_stone, 1 , weight(1)|difficulty(0)|spd_rtng(95) | shoot_speed(20) | thrust_damage(17 , blunt)|max_ammo(6)|weapon_length(8),imodbit_large_bag,missile_distance_trigger ],
["stones2", "Throwing Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary ,itcf_throw_stone, 1 , weight(1)|difficulty(0)|spd_rtng(95) | shoot_speed(20) | thrust_damage(17 , blunt)|max_ammo(6)|weapon_length(8),imodbit_large_bag,missile_distance_trigger ],

#todo: Light Trowing axe, Heavy Throwing Axe
["throwing_axes", "Francisca", [("francisca",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee,itcf_throw_axe,
380, weight(3)|difficulty(4)|spd_rtng(65) | shoot_speed(15) | thrust_damage(42,cut)|max_ammo(1)|weapon_length(59),imodbits_thrown_minus_heavy,missile_distance_trigger],
["throwing_axes_melee", "Francisca", [("francisca",0)], itp_type_one_handed_wpn |itp_primary|itp_secondary|itp_bonus_against_shield,itc_axe1h,
380, weight(3)|difficulty(4)|spd_rtng(75)|weapon_length(53)| swing_damage(35,cut),imodbits_thrown_minus_heavy],
["light_throwing_axes", "Light Francisca", [("francisca_afilada",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_next_item_as_melee,itcf_throw_axe,
360, weight(2)|difficulty(2)|spd_rtng(69) | shoot_speed(18) | thrust_damage(39,cut)|max_ammo(2)|weapon_length(53),imodbits_thrown_minus_heavy,missile_distance_trigger],
["light_throwing_axes_melee", "Light Francisca", [("francisca_afilada",0)], itp_type_one_handed_wpn |itp_primary|itp_secondary|itp_bonus_against_shield,itc_axe1h,
380, weight(2)|difficulty(2)|spd_rtng(75)|weapon_length(53)| swing_damage(35,cut),imodbits_thrown_minus_heavy, [], jute_factions],

#########FELCHAS CHIEF empieza finales #########################
 #######################see practice arrows for multiple quantities
["arrows1","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 200,weight(3)|abundance(60)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(40),imodbits_missile,missile_distance_trigger],
["byzantine_arrows","Byzantine Arrows", [("arrow_b",0),("flying_arrow_b",ixmesh_flying_ammo),("spak_ar_bag", ixmesh_carry)], itp_type_arrows|itp_unique, itcf_carry_quiver_back_right, 410,weight(3.5)|abundance(60)|weapon_length(95)|thrust_damage(3,pierce)|max_ammo(30),imodbits_missile,missile_distance_trigger],
["barbed_arrows","Fire Arrow", [("arrow",0),("flying_missile_fire",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 200,weight(3)|abundance(60)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(40),imodbits_missile,missile_distance_trigger],
["siegebag_arrows","62 Arrows", [("arrow",0),("flying_missile_fire",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 200,weight(3)|abundance(60)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(65),imodbits_missile,missile_distance_trigger],
["arrows2","arrowslot", [("arrow",0),("flying_missile_fire",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_quiver_back, 200,weight(3)|abundance(60)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(40),imodbits_missile,missile_distance_trigger],
["bolts","Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 164,weight(1)|abundance(60)|weapon_length(63)|thrust_damage(1,pierce)|max_ammo(20),imodbits_missile, [], jute_factions + pict_factions],
##################chief finales arcos empieza##############################################
 ###########################################################################################
["huntingbow",   "Hunting Bow", [("hunting_bow1",0),("hunting_bow_carry1",ixmesh_carry)],itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 267 , weight(1)|difficulty(1)|spd_rtng(70) | shoot_speed(47) | thrust_damage(18 , pierce)|accuracy(85),imodbits_bow],
#  [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]],
["shortbow",   "Short Bow", [("short_bow1",0),("short_bow_carry1",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 368 , weight(1)|difficulty(1)|spd_rtng(67) | shoot_speed(44) | thrust_damage(20 , pierce )|accuracy(90),imodbits_bow,
  [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]],
["nomad_bowreserv",   "rComposite Bow", [("nomad_bow1",0),("nomad_bow_case1", ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 690 , weight(1.25)|difficulty(2)|spd_rtng(64) | shoot_speed(55) | thrust_damage(24 , pierce)|accuracy(95),imodbits_bow,
  [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]], #arco poco usado, no en mercaders pero podemos anadirlo a unidades determinadas chief
["longbow",   "Long Bow", [("long_bow1",0),("long_bow_carry1",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 630 , weight(1.75)|difficulty(2)|spd_rtng(60) | shoot_speed(50) | thrust_damage(22 , pierce)|accuracy(99),imodbits_bow,
  [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])],
 briton_factions],
["slotforbow1",   "unused Bow", [("short_bow1",0),("short_bow_carry1",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 368 , weight(1)|difficulty(1)|spd_rtng(67) | shoot_speed(44) | thrust_damage(20 , pierce )|accuracy(90),imodbits_bow,
  [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]],
["slotforbow2",   "unused Bow", [("short_bow1",0),("short_bow_carry1",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 368 , weight(1)|difficulty(1)|spd_rtng(67) | shoot_speed(44) | thrust_damage(20 , pierce )|accuracy(90),imodbits_bow,
  [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]],

##arco para incendiar
["khergit_bowreserv",   "rFire Bow", [("khergit_bow",0),("khergit_bow_case", ixmesh_carry)], itp_type_bow |itp_unique|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 368 , weight(1)|difficulty(2)|spd_rtng(67) | shoot_speed(44) | thrust_damage(20 , pierce )|accuracy(90),imodbits_bow,
  [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]],

###ARCOS ESPECIALES heroes
["longbowbandit",   "Dark Hunter", [("war_bow1",0),("war_bow_carry1", ixmesh_carry)], itp_type_bow |itp_primary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 830 , weight(1.75)|difficulty(1)|spd_rtng(60) | shoot_speed(50) | thrust_damage(22 , pierce)|accuracy(99),imodbits_sword_high,
  [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]],
["cavbowbandit",   "Eye-popping", [("strong_bow1",0),("strong_bow_case1",ixmesh_carry)],itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 890 , weight(1.25)|difficulty(1)|spd_rtng(64) | shoot_speed(55) | thrust_damage(24 , pierce)|accuracy(95),imodbits_sword_high,
  [(ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 48, pos1)])]],


["pict_crossbow", "Pictish Crossbow", [("xenoargh_arbalest",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_cant_use_on_horseback|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
250 , weight(2.25)|difficulty(1)|spd_rtng(40) | shoot_speed(45) | thrust_damage(20 , pierce)|max_ammo(1)|accuracy(85),imodbits_crossbow, [], pict_factions],
["frankish_crossbow", "Frankish Crossbow", [("xenoargh_arbalest",0)], itp_merchandise|itp_type_crossbow |itp_no_pick_up_from_ground|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
67 , weight(2.5)|difficulty(8)|spd_rtng(45) | shoot_speed(59) | thrust_damage(44 , pierce)|max_ammo(1),imodbits_crossbow, [], strange_combination],
["byzantine_crossbow", "Frankish Crossbow", [("xenoargh_arbalest",0)], itp_merchandise|itp_type_crossbow |itp_no_pick_up_from_ground|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
67 , weight(2.5)|difficulty(8)|spd_rtng(45) | shoot_speed(59) | thrust_damage(44 , pierce)|max_ammo(1),imodbits_crossbow, [], strange_combination],
 
#sling sot chief
["slingrocks", "Sling Rocks", [("throwing_stone",0),("throwing_stone",ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)],
 itp_type_bullets|itp_merchandise, 0, 15,weight(0.5)|abundance(60)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile],
["slingrockst2", "Sling Lead", [("throwing_stone",0),("throwing_stone",ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)],
 itp_type_bullets|itp_merchandise, 0, 350,weight(0.7)|abundance(60)|weapon_length(3)|thrust_damage(6,pierce)|max_ammo(30),imodbits_missile],
#sling sot chief
["basic_sling", "Sling", [("Sling",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_cant_use_on_horseback ,itcf_throw_stone, 30, weight(0.5)|difficulty(0)|spd_rtng(60) | shoot_speed(50) | thrust_damage(19 ,blunt)|max_ammo(1)|accuracy(90),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],
["slingtier2", "Military Sling", [("Slingmilitargrande",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_cant_use_on_horseback ,itcf_throw_stone, 90, weight(0.5)|difficulty(0)|spd_rtng(65) | shoot_speed(55) | thrust_damage(23 ,blunt)|max_ammo(1)|accuracy(93),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],
["fustibalus", "Fustibalus", [("Staf_Sling_fustibalus",0)],
 itp_type_pistol |itp_merchandise|itp_primary|itp_cant_use_on_horseback ,itcf_throw_stone, 110, weight(1)|difficulty(0)|spd_rtng(70) | shoot_speed(75) | thrust_damage(23 ,blunt)|max_ammo(1)|accuracy(90),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_stone")])]],

# itp_type_crossbow |itp_merchandise|itp_primary ,itcf_throw_stone|itcf_carry_dagger_front_right|itcf_reload_pistol, 22 , weight(0.5)|difficulty(0)|spd_rtng(147) | shoot_speed(40) | thrust_damage(15 , blunt)|max_ammo(1),imodbits_crossbow ],
##
["torch",   "Torches", [("torch_h",0)], itp_type_thrown|itp_merchandise |itp_primary ,itcf_throw_axe, 41 , weight(5)|difficulty(1)|spd_rtng(99) | shoot_speed(20) | thrust_damage(15,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),]),
 (ti_on_weapon_attack, [(call_script, "script_cf_set_fire_arrow", 20, pos1)])]], ###chief fire arrow cambia para asedios

###########################proyectiles acaba chief####################################
 ####################################################################################


["lyre", "Lyre", [("lyre",0)], itp_merchandise|itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back, 220 , weight(2.5)|hit_points(80)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute", "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back, 218 , weight(2.5)|hit_points(80)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["slotinstrument1", "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back, 218 , weight(2.5)|hit_points(80)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["instruments_end", "Instruments End", [("leathershield_small_b",0)], 0, 0, 1, 0, 0],

#bebe, hijo de player
["baby",   "Baby", [("baby",0)], itp_always_loot|itp_type_goods, 0, 255,weight(50)|abundance(60),imodbits_none],

#chief unique
##["short_sword", "Short Sword",
## [("sword_norman",0),("sword_norman_scabbard", ixmesh_carry),("sword_norman_rusty",imodbit_rusty),("sword_norman_rusty_scabbard", ixmesh_carry|imodbit_rusty)],
## itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(75)|swing_damage(25 , cut) | thrust_damage(19 , pierce),imodbits_sword ],

##["strange_armor", "native", [("samurai_armor",0)], itp_type_body_armor |itp_covers_legs ,0, 1259 , weight(18)|abundance(60)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(7) ,imodbits_armor ],
##["strange_boots", "native", [("samurai_boots",0)], itp_type_foot_armor | itp_attach_armature,0, 465 , weight(1)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
##["strange_helmet", "native", [("samurai_helmet",0)], itp_type_head_armor  ,0, 824 , weight(2)|abundance(60)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
##["strange_sword", "native", [("katana",0),("katana_scabbard",ixmesh_carry)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 679 , weight(2.0)|difficulty(9)|spd_rtng(89) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(12 , pierce),imodbits_sword ],
##["strange_great_sword", "native", [("no_dachi",0),("no_dachi_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 920 , weight(3.5)|difficulty(11)|spd_rtng(92) | weapon_length(125)|swing_damage(33 , cut) | thrust_damage(0 , pierce),imodbits_axe ],
##["strange_short_sword", "native", [("wakizashi",0),("wakizashi_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 321 , weight(1.25)|difficulty(0)|spd_rtng(108) | weapon_length(65)|swing_damage(15 , cut) | thrust_damage(24 , pierce),imodbits_sword ],
["court_dress", "Court Dress", [("court_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian  ,0, 348 , weight(4)|abundance(60)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
#chief unique acaba

#################especiales chief#############################################
#piedra para asedio chief Siege warfare
["stones_siege",   "Siege Stones", [("siegestone",0)], itp_type_thrown |itp_no_pick_up_from_ground|itp_primary|itp_secondary ,itcf_throw_stone, 10 , weight(4)|difficulty(4)|spd_rtng(60) | shoot_speed(8) | thrust_damage(25 , blunt)|max_ammo(3)|weapon_length(14),imodbits_none,
[
  (ti_on_missile_hit,
 [
	 (try_begin),
		#Solid Round Script
  #pos1 - Missile hit position
  #param_1 - Shooter agent
		(this_or_next|multiplayer_is_server),
		(neg|game_in_multiplayer_mode),		
		(store_trigger_param_1,":shooter"),
		(copy_position, pos63, pos1),
		(particle_system_burst,"psys_piedra_dust",pos1,1),
		(try_for_agents,":agent"),
			(agent_get_position,pos62,":agent"),
			(get_distance_between_positions,":dist",pos63,pos62),
			(try_begin),
				(lt,":dist",100),#1-meter radius,otherwise doesn't register enough
				(neg|agent_is_ally,":agent"),
				(agent_is_active,":agent"),
				(agent_is_alive,":agent"),
				(neq,":agent",":shooter"),				  
#				(agent_set_hit_points,":agent",0,1),#insta-death
				(agent_deliver_damage_to_agent,":shooter",":agent"),
			(play_sound,"snd_shield_broken"),
  (try_end),
		(try_end),
		(try_end),
]),
]],
["boiling_water",   "Boiling Water", [("boiling_water",0)], itp_type_thrown|itp_can_penetrate_shield|itp_no_pick_up_from_ground |itp_no_pick_up_from_ground|itp_primary|itp_secondary ,itcf_throw_stone, 10 , weight(5)|difficulty(5)|spd_rtng(60) | shoot_speed(6) | thrust_damage(35 , blunt)|max_ammo(3)|weapon_length(14),imodbits_none,
[
 (ti_on_missile_hit,
 [
   #pos1 - Missile hit position
   #param_1 - Shooter agent
   (try_begin),
		 (this_or_next|multiplayer_is_server),
		 (neg|game_in_multiplayer_mode),
			 
			(store_trigger_param_1,":shooter"),
			(copy_position, pos63, pos1),				 
			# (particle_system_burst,"psys_agua_hirviendo",pos63,1),
			# (particle_system_burst,"psys_agua_hirviendo",pos63,3),
			# (particle_system_burst,"psys_agua_hirviendo",pos63,10),
 (particle_system_burst,"psys_boiling_water",pos63,1),
 (particle_system_burst,"psys_boiling_water",pos63,3),
 (particle_system_burst,"psys_boiling_water",pos63,10),
(play_sound, "snd_dummy_destroyed"),
   			(spawn_scene_prop,"spr_dungeon_water_drops",63),
			(store_random_in_range,":random_no",10,45),
			(assign,reg0,":random_no"),				 
   (try_for_agents,":agent"),
    (agent_get_position,pos62,":agent"),
    (get_distance_between_positions,":dist",pos63,pos62),
    (try_begin),
				  (lt,":dist",245),
					(neg|agent_is_ally,":agent"),
					(agent_is_active,":agent"),
					(agent_is_alive,":agent"),
					(neq,":agent",":shooter"),				  
				  (store_agent_hit_points,":hp",":agent",1), 
				  (val_sub,":hp",":random_no"),    
					(try_begin),
						(lt,":hp",1),
						(agent_deliver_damage_to_agent,":shooter",":agent"),
					(else_try),
						(agent_set_hit_points,":agent",":hp",1),
					(try_end),
    (try_end),
   (try_end),
   (try_end),
]),
]],
 
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting chief Mod begin#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
["deer","Deer", [("deer",0)], itp_unique|itp_type_horse, 0, 1411,abundance(60)|hit_points(30)|body_armor(5)|difficulty(11)|horse_speed(50)|horse_maneuver(32)|horse_charge(20),imodbits_horse_basic],
["boar","Boar", [("boar",0)], itp_unique|itp_type_horse, 0, 1411,abundance(60)|hit_points(80)|body_armor(15)|difficulty(11)|horse_speed(25)|horse_maneuver(20)|horse_charge(200)|horse_scale(55),imodbits_horse_basic],
["wolf","Wolf", [("warg",0)], itp_unique|itp_type_horse, 0, 1411,abundance(60)|hit_points(80)|body_armor(10)|difficulty(11)|horse_speed(30)|horse_maneuver(40)|horse_charge(100)|horse_scale(55),imodbits_horse_basic],
["goata","Wild Goat", [("goat_c",0)], itp_unique|itp_type_horse, 0, 1411,abundance(60)|hit_points(20)|body_armor(8)|difficulty(11)|horse_speed(35)|horse_maneuver(30)|horse_charge(20)|horse_scale(55),imodbits_horse_basic],
["goatb","Angry Sheep", [("goat",0)], itp_unique|itp_type_horse, 0, 1411,abundance(60)|hit_points(20)|body_armor(8)|difficulty(11)|horse_speed(35)|horse_maneuver(30)|horse_charge(20)|horse_scale(55),imodbits_horse_basic],
["wilddonkey","Wild Donkey", [("wild_donkey",0)], itp_unique|itp_type_horse, 0, 1411,abundance(60)|hit_points(40)|body_armor(10)|difficulty(11)|horse_speed(25)|horse_maneuver(20)|horse_charge(50)|horse_scale(65),imodbits_horse_basic],
["dangerousanimal","Vorpal Bunnies", [("wild_donkey",0)], itp_unique|itp_type_horse, 0, 1411,abundance(60)|hit_points(40)|body_armor(10)|difficulty(11)|horse_speed(25)|horse_maneuver(20)|horse_charge(50)|horse_scale(65),imodbits_horse_basic],
["cow1","Vorpal Bunnies", [("wild_donkey",0)], itp_unique|itp_type_horse, 0, 1411,abundance(60)|hit_points(40)|body_armor(10)|difficulty(11)|horse_speed(25)|horse_maneuver(20)|horse_charge(50)|horse_scale(65),imodbits_horse_basic],
["otheranimal","Vorpal Bunnies", [("wild_donkey",0)], itp_unique|itp_type_horse, 0, 1411,abundance(60)|hit_points(40)|body_armor(10)|difficulty(11)|horse_speed(25)|horse_maneuver(20)|horse_charge(50)|horse_scale(65),imodbits_horse_basic],

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting chief Mod end#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


####trofeos de batalla chief
["trophy_a","Battle Trophy", [("horn",0)], itp_type_goods|itp_always_loot, 0, 210,weight(3)|abundance(60),imodbits_none],
["trophy_b","War Trophy", [("wessexbanner8",0)], itp_type_goods|itp_always_loot, 0, 410,weight(7)|abundance(60),imodbits_none],
["trophy_c","Epic King Trophy", [("chest_c",0)], itp_type_goods|itp_always_loot, 0, 610,weight(10)|abundance(60),imodbits_none],
#chief begin
["dplmc_coat_of_plates_red_constable", "Constable Mail", [("byrnie16",0)], itp_type_body_armor |itp_covers_legs |itp_civilian,0,
 3828 , weight(25)|abundance(60)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(0) ,imodbits_armor ],
["iniauhorn",   "Iniau Horn", [("horn",0)], itp_type_goods, 0, 255,weight(50)|abundance(60),imodbits_none],
## gdw 
#Otros, cuerno####
 ###########
["horn_of_arthur", "horn_of_arthur", [("horn",0),], itp_type_thrown |itp_primary|itp_no_pick_up_from_ground, itcf_throw_knife, 145 , weight(1.5)|difficulty(0)|spd_rtng(50) | shoot_speed(54) | thrust_damage(3 , cut)|max_ammo(5)|weapon_length(0),imodbits_thrown,
   [(ti_on_weapon_attack, [
       (play_sound,"snd_horn"),(try_for_agents,":agent"),
                              (agent_is_alive,":agent"),
                              (agent_is_human,":agent"),
                              (agent_is_ally,":agent"),
       (store_agent_hit_points,":life",":agent",0),
##       (try_begin),
##       (agent_set_animation, ":troop", "anim_horn_blow"),
###                           (agent_set_animation, ":agent", "anim_cheer"),
##       (try_end),
       (val_add,":life",14),
       (agent_set_hit_points,":agent",":life",0),     
       (agent_play_sound, ":agent", "snd_man_victory"),
       (try_end),          
       (store_add,":recovery", 14),
       (assign,reg1,":recovery"),
       (display_message,"@Horn rally men! (wounded troops recover 13 hitpoints)",0x6495ed),     
                              ],)]],
   ##need to find new mesh for 2nd horn
["horn_multiplayer", "Horn", [("horn",0),], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword, 145 , weight(1.5)|difficulty(0)|spd_rtng(50) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(4 , pierce),imodbits_none,
[(ti_on_weapon_attack, [

       (play_sound,"snd_horn2"),(try_for_agents,":agent"),
                              (agent_is_alive,":agent"),
                              (agent_is_human,":agent"),
                              (agent_is_ally,":agent"),
       (store_agent_hit_points,":life",":agent",0),
##       (try_begin),
##       (agent_set_animation, ":troop", "anim_horn_blow"),
###                           (agent_set_animation, ":agent", "anim_cheer"),
##       (try_end),
       (val_add,":life",5),
       (agent_set_hit_points,":agent",":life",0),      
       (agent_play_sound, ":agent", "snd_man_victory"),
       (try_end),           
       (store_add,":recovery",5),
       (assign,reg1,":recovery"),
     #  (display_message,"@Horn rally men! (wounded troops recover 5 hitpoints)",0x6495ed),      
                              ],)]],
   
["horn1", "BattleHorn", [("horn",0)], itp_no_pick_up_from_ground| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_none, 
   [(ti_on_weapon_attack, [

       (play_sound,"snd_horn2"),(try_for_agents,":agent"),
                              (agent_is_alive,":agent"),
                              (agent_is_human,":agent"),
                              (agent_is_ally,":agent"),
       (store_agent_hit_points,":life",":agent",0),
##       (try_begin),
##       (agent_set_animation, ":troop", "anim_horn_blow"),
###                           (agent_set_animation, ":agent", "anim_cheer"),
##       (try_end),
       (val_add,":life",5),
       (agent_set_hit_points,":agent",":life",0),      
       (agent_play_sound, ":agent", "snd_man_victory"),
       (try_end),           
       (store_add,":recovery",5),
       (assign,reg1,":recovery"),
     #  (display_message,"@Horn rally men! (wounded troops recover 5 hitpoints)",0x6495ed),      
                              ],)]],    
############3
 ##################
 
##diplomacy chief end 
#################especiales chief acaba ################################

####OTROS chief ##################################
["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a_bry",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 80 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(3)|leg_armor(1), imodbits_cloth ],
["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_axe1h,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ], 
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(60)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)], itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(60)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

#cuerno multiplayer chief

["siege_stones",   "Siege Stones", [("siegestone",0)], itp_type_thrown |itp_primary|itp_secondary ,itcf_throw_stone, 10 , weight(4)|difficulty(0)|spd_rtng(60) | shoot_speed(8) | thrust_damage(25 , blunt)|max_ammo(3)|weapon_length(14),imodbits_none,
[#??multiplayer gdw
(ti_on_missile_hit,
 [
 (try_begin),
  #Solid Round Script
  #pos1 - Missile hit position
  #param_1 - Shooter agent
  # (multiplayer_is_server),
  #(neg|game_in_multiplayer_mode),    
  (store_trigger_param_1,":shooter"),
  (copy_position, pos63, pos1),
  (particle_system_burst,"psys_piedra_dust",pos1,1),
  (try_for_agents,":agent"),
    (agent_get_position,pos62,":agent"),
    (get_distance_between_positions,":dist",pos63,pos62),
    (try_begin),
      (lt,":dist",100),#1-meter radius,otherwise doesn't register enough
      (neg|agent_is_ally,":agent"),
      (agent_is_active,":agent"),
      (agent_is_alive,":agent"),
      (neq,":agent",":shooter"),          
#       (agent_set_hit_points,":agent",0,1),#insta-death
      (agent_deliver_damage_to_agent,":shooter",":agent"),
     #(multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_shield_broken"),
    (play_sound,"snd_shield_broken"),
    (try_end),
  (try_end),
  (try_end),
]), 
 ]],


["boiling_watermultip",   "Boiling Water", [("boiling_water",0)], itp_type_thrown|itp_can_penetrate_shield|itp_no_pick_up_from_ground|itp_primary|itp_secondary ,itcf_throw_stone, 10 , weight(5)|difficulty(0)|spd_rtng(60) | shoot_speed(6) | thrust_damage(35 , blunt)|max_ammo(2)|weapon_length(14),imodbits_none,
[(ti_on_missile_hit,
[
  (store_trigger_param_1, ":agent_no"),
  (call_script, "script_explosion_at_pos1", 500, 50, ":agent_no"),
])],
],
#chief unique acaba
#################basicas chief acaba NATIVE
#chief unique
##########nativos#########################
#chief unique
#######nativos############
########nativoskeep slots for new mod weapons replace these as they have no function
["slottwo_handed_cleaver", "slotforfutureitem", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["slotshortened_voulge_alt",   "slotforfutureitem", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["slot9bardiche",   "slotforfutureitem", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["slot9voulge",   "slotforfutureitem", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["slot9long_bardiche",   "slotforfutureitem", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["slot9flail_blunt",   "slotforfutureitem", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["slot9flail_blunt_alt",   "slotforfutureitem", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
["slot9fighting_pick", "slotforfutureitem", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 , pierce),imodbits_sword,
[], pict_factions + irish_factions],
# ["slotmilitary_pick", "slotforfutureitem", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 , pierce),imodbits_sword,
# [], pict_factions + irish_factions],
# ["slotmorningstar_alt",   "slotforfutureitem", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 , pierce),imodbits_sword,
# [], pict_factions + irish_factions],
# ["slotcleaver",   "slotforfutureitem", [("Pictish_Longsword",0),("Scab_Pictish_Longsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 960 , weight(1.3)|difficulty(8)|spd_rtng(82) | weapon_length(99)|swing_damage(36 , cut) | thrust_damage(12 , pierce),imodbits_sword,
# [], pict_factions + irish_factions],

#chief unique acaba
#["scaleorangeblkbands", "native", [("shirt_a_bry",0)], itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 400 , weight(0.5)|abundance(60)|head_armor(0)|body_armor(15)|leg_armor(2), imodbits_cloth],
# #chief unique acaba ############3otros #############################
["items_end", "Items End", [("leathershield_small_b",0)], 0, 0, 1, 0, 0],
]

# #mace_1 replaced ["mail_boots_for_tableau", "native", [("ankle_boots_a_new_bry",0)], itp_type_foot_armor | itp_attach_armature ,0, 1, weight(3)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
# #MOTO generate no-swing versions of weapons
# from copy import deepcopy

# def modmerge(var_set):
# 	try:
# 		var_name_1 = "items"
# 		orig_items = var_set[var_name_1]
		
# 		add_item = deepcopy(orig_items)
# 		for i_item in range(1,len(orig_items)):
# 			type = add_item[i_item][3] & 0x000000ff
# 			# if itp_type_one_handed_wpn <= type <= itp_type_polearm and add_item[i_item-1][3] & itp_next_item_as_melee == 0 and (get_thrust_damage(add_item[i_item][6]) % 256) > 0 and "tutorial" not in add_item[i_item][0] and "arena" not in add_item[i_item][0] and "practice" not in add_item[i_item][0] and "tpe" not in add_item[i_item][0]:nd "tpe" not in add_item[i_item][0]
# 			if itp_type_one_handed_wpn <= type <= itp_type_polearm and (get_thrust_damage(add_item[i_item][6])&0xff) > 5 and "tutorial" not in add_item[i_item][0] and "practice" not in add_item[i_item][0] and "alt" not in add_item[i_item][0]  and "hammer" not in add_item[i_item][0] and "blunt" not in add_item[i_item][0] and "kni" not in add_item[i_item][0] and "slot9" not in add_item[i_item][0] and "javel" not  in add_item[i_item][0]:
# 				# and "ax" not  in add_item[i_item][0] this will clip off 11 items gdw71115
#         #Above checks that it is a weapon with thrust damage; also checks that it isn't a tournament-type weapon by checking the item ID (just to prevent not-used items)
# 				add_item[i_item][0] = 'noswing_'+add_item[i_item][0]   #add noswing_ to the item's name
# 				add_item[i_item][6] = add_item[i_item][6] & ~(ibf_damage_mask << iwf_swing_damage_bits) #should set new item's swing damage to 0
# 				add_item[i_item][4] = add_item[i_item][4] & ~itcf_overswing_polearm #remove itcf_ capabilties to prevent swinging without damage 
# 				add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashright_polearm     
# 				add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashleft_polearm
# 				#add_item[i_item][4] = add_item[i_item][4] & ~itcf_overswing_onehanded  
# 				add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashright_onehanded     
# 				add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashleft_onehanded
# 				#add_item[i_item][4] = add_item[i_item][4] & ~itcf_overswing_twohanded
# 				add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashright_twohanded     
# 				add_item[i_item][4] = add_item[i_item][4] & ~itcf_slashleft_twohanded
# 				if type == itp_type_polearm and add_item[i_item][3] & itp_two_handed == 0:
# 					add_item[i_item][4] = add_item[i_item][4] | itcf_thrust_onehanded #so that the polearms use 'bent elbow' with shields, but normal without
# 				add_item[i_item][3] = add_item[i_item][3] & ~itp_merchandise
# 				# orig_items.insert((len(orig_items)-1), add_item[i_item])  #add right above itm_items_end
# 				orig_items.append(add_item[i_item])
		
# 	except KeyError:
# 		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
# 		raise ValueError(errstring)
# modmerger_start version=201 type=2
