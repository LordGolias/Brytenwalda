from .header_parties import *

from .lazy_flag import LazyFlag

from . import constable

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",LazyFlag("icon_gray_knight"),0,"fac_commoners",merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",LazyFlag("icon_gray_knight"),0,"fac_commoners",merchant_personality,[]),
  ("enemy","Enemy",LazyFlag("icon_gray_knight"),0,"fac_undeads",merchant_personality,[]),
  ("hero_party","Hero Party",LazyFlag("icon_gray_knight"),0,"fac_commoners",merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",LazyFlag("icon_saxon_skirmishert5"),0,"fac_neutral",merchant_personality,[]),
  ("village_defenders","Village Defenders",LazyFlag("icon_peasant"),0,"fac_commoners",merchant_personality,[("trp_farmer",10,20),("trp_peasant_woman",0,8)]),

  ("cattle_herd1","Cattle Herd",LazyFlag("icon_cattle")|carries_goods(10),0,"fac_neutral",merchant_personality,[("trp_cattle",80,120)]),
  ("cattle_herd2","Cattle Herd",LazyFlag("icon_cattle")|carries_goods(10),0,"fac_neutral",merchant_personality,[("trp_cattle",80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",LazyFlag("icon_saxon_skirmishert5")|carries_goods(10)|pf_quest_party,0,"fac_commoners",merchant_personality,[("trp_nobleman",1,1),("trp_saxon_skirmishert5",2,6),("trp_saxon_horseman1",4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",LazyFlag("icon_gray_knight")|carries_goods(10)|pf_quest_party,0,"fac_commoners",merchant_personality,[("trp_nobleman",1,1),("trp_briton_cavalry",2,6),("trp_briton_horseman",4,12)]),
# Ryan BEGIN
  ("looters","Bandits",LazyFlag("icon_axeman")|carries_goods(8),0,"fac_outlaws",bandit_personality,[("trp_looter",3,60)]), #chief cambiado
# Ryan END
  ("manhunters","Young Warriors",LazyFlag("icon_axeman"),0,"fac_manhunters",soldier_personality,[("trp_manhunter",12,70)]), #chief cambiado
##  ("peasant","Peasant",LazyFlag("icon_peasant"),0,"fac_commoners",merchant_personality,[("trp_farmer",1,6),("trp_peasant_woman",0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",LazyFlag("icon_pict_footmant2_b")|carries_goods(2),0,"fac_black_khergits",bandit_personality,[("trp_black_khergit_guard",1,10),("trp_pict_footmant2",5,5)]),
  ("steppe_bandits","Scoti Raiders",LazyFlag("icon_axeman")|carries_goods(2),0,"fac_mountain_bandits",bandit_personality,[("trp_looter_leader2",1,2),("trp_steppe_bandit",8,58)]),
  ("taiga_bandits","Outlaw Warriors",LazyFlag("icon_axeman")|carries_goods(2),0,"fac_outlaws",bandit_personality,[("trp_looter_leader2",1,2),("trp_taiga_bandit",8,58)]),
  ("desert_bandits","Bandits Gang",LazyFlag("icon_axeman")|carries_goods(2),0,"fac_outlaws",bandit_personality,[("trp_looter_leader2",1,2),("trp_desert_bandit",8,58)]),
  ("forest_bandits","Unrights Gang",LazyFlag("icon_axeman")|carries_goods(2),0,"fac_forest_bandits",bandit_personality,[("trp_looter_leader2",1,2),("trp_forest_bandit",4,52),("trp_brigand",8,40)]),
  ("mountain_bandits","Band of Thieves and Murderers",LazyFlag("icon_axeman")|carries_goods(2),0,"fac_outlaws",bandit_personality,[("trp_looter_leader2",1,2),("trp_mountain_bandit",4,60)]),
  ("sea_raiders","Frankish Raiders",LazyFlag("icon_axeman")|carries_goods(2),0,"fac_mountain_bandits",bandit_personality,[("trp_sea_raider_leader2",1,2),("trp_sea_raider",15,70)]),
  ("sea_raiders2","Dena Raiders",LazyFlag("icon_axeman")|carries_goods(2),0,"fac_mountain_bandits",bandit_personality,[("trp_sea_raider_leader2",1,2),("trp_dena_pirate",14,70)]),
#new party chief
  ("sea_band","Warrior Band",LazyFlag("icon_axeman")|carries_goods(2),0,"fac_mountain_bandits",bandit_personality,[("trp_looter_leader2",1,2),("trp_sea_raider",8,40),("trp_looter",8,40),("trp_mountain_bandit",5,30)]),
#chief acaba
  ("deserters","Masterless Men",LazyFlag("icon_axeman")|carries_goods(3),0,"fac_deserters",bandit_personality,[]),
  
  ("merchant_caravan","Merchant Caravan",LazyFlag("icon_gray_knight")|carries_goods(40)|pf_auto_remove_in_town|pf_quest_party,0,"fac_commoners",escorted_merchant_personality,[("trp_caravan_master",1,1),("trp_merc_infantryt3",5,25)]),
  ("troublesome_bandits","Troublesome Bandits",LazyFlag("icon_axeman")|carries_goods(9)|pf_quest_party,0,"fac_outlaws",bandit_personality,[("trp_bandit",14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",LazyFlag("icon_axeman")|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,"fac_neutral",bandit_personality,[("trp_bandit",24,58),("trp_kidnapped_girl",1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",LazyFlag("icon_woman")|pf_quest_party,0,"fac_neutral",merchant_personality,[("trp_kidnapped_girl",1,1)]),

  ("village_farmers","Village Farmers",LazyFlag("icon_peasant")|pf_civilian,0,"fac_innocents",merchant_personality,[("trp_farmer",5,10),("trp_peasant_woman",3,8)]),
#nuevo template chief de neko y relic quest
  ("neko","Neko party",LazyFlag("icon_axeman")|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,"fac_neko",merchant_personality,[("trp_npcneko",1,1),("trp_cantaber_iuventus",20,27)]),
  ("cado_template","Cado party",LazyFlag("icon_axeman")|carries_goods(9)|pf_quest_party,0,"fac_neko",soldier_personality,[("trp_cado",1,1),("trp_cantaber_iuventus",388,400)]),
  ("arrians","Arrians",LazyFlag("icon_axeman")|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,"fac_neutral",merchant_personality,[("trp_thyr",1,1),("trp_guardianarian",20,30)]),
  ("eadfrith","Eadfrith's Warband",LazyFlag("icon_axeman")|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,"fac_eadfrith",merchant_personality,[("trp_especiales_3",1,1),("trp_engle_skirmishert4",30,40)]),#gdw soldier personality

  ("spy_partners", "Unremarkable Travellers", LazyFlag("icon_gray_knight")|carries_goods(10)|pf_default_behavior|pf_quest_party,0,"fac_neutral",merchant_personality,[("trp_spy_partner",1,1),("trp_merc_infantryt3",5,11)]),
  ("runaway_serfs","Runaway Serfs",LazyFlag("icon_peasant")|carries_goods(8)|pf_default_behavior|pf_quest_party,0,"fac_neutral",merchant_personality,[("trp_farmer",6,7), ("trp_peasant_woman",3,3)]),
  ("spy", "Ordinary Townsman", LazyFlag("icon_gray_knight")|carries_goods(4)|pf_default_behavior|pf_quest_party,0,"fac_neutral",merchant_personality,[("trp_spyenemy",1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", LazyFlag("icon_gray_knight")|carries_goods(3)|pf_default_behavior|pf_quest_party,0,"fac_neutral",merchant_personality,[]),
##  ("conspirator", "Conspirators", LazyFlag("icon_gray_knight")|carries_goods(8)|pf_default_behavior|pf_quest_party,0,"fac_neutral",merchant_personality,[("trp_conspirator",3,4)]),
##  ("conspirator_leader", "Conspirator Leader", LazyFlag("icon_gray_knight")|carries_goods(8)|pf_default_behavior|pf_quest_party,0,"fac_neutral",merchant_personality,[("trp_conspirator_leader",1,1)]),
##  ("peasant_rebels", "Peasant Rebels", LazyFlag("icon_peasant"),0,"fac_peasant_rebels",bandit_personality,[("trp_peasant_rebel",33,97)]),
##  ("noble_refugees", "Noble Refugees", LazyFlag("icon_gray_knight")|carries_goods(12)|pf_quest_party,0,"fac_noble_refugees",merchant_personality,[("trp_noble_refugee",3,5),("trp_noble_refugee_woman",5,7)]),

  ("forager_party","Foraging Party",LazyFlag("icon_gray_knight")|carries_goods(5)|pf_show_faction,0,"fac_commoners",merchant_personality,[]),
  ##  NEW PATROLS somebody chief patrullas
  ("patrol_party","Patrol",LazyFlag("icon_gray_knight")|carries_goods(2)|pf_show_faction,0,"fac_commoners",soldier_personality,[]),
  ("patrols_end","Patrol",LazyFlag("icon_gray_knight"),0,"fac_player_faction",aggressiveness_0|courage_15,[]),
  ##  NEW PATROLS somebody chief patrullas
#  ("war_party", "War Party",LazyFlag("icon_gray_knight")|carries_goods(3),0,"fac_commoners",soldier_personality,[]),
  ("messenger_party","Messenger",LazyFlag("icon_gray_knight")|pf_show_faction,0,"fac_commoners",merchant_personality,[]),
  ("raider_party","Raiders",LazyFlag("icon_gray_knight")|carries_goods(16)|pf_quest_party,0,"fac_outlaws",bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,"fac_commoners",0,[("trp_peasant_woman",6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",LazyFlag("icon_mule")|carries_goods(45)|pf_show_faction,0,"fac_commoners",merchant_personality,[("trp_caravan_master",1,1),("trp_merc_infantryt3",12,40)]),
  ("prisoner_train_party","Prisoner Train",LazyFlag("icon_gray_knight")|carries_goods(5)|pf_show_faction,0,"fac_commoners",merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,"fac_commoners",0,[("trp_bandit",5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",LazyFlag("icon_saxon_skirmishert5"),0,"fac_commoners",soldier_personality,[]),



#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting chief Mod begin#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

  ("deer_herd","Deer Herd",LazyFlag("icon_flagbearer_b")|carries_goods(10),0,"fac_wild_animals",merchant_personality,[("trp_deer",16,40)]),
  ("boar_herd","Boar Herd",LazyFlag("icon_flagbearer_b")|carries_goods(10),0,"fac_wild_animals",merchant_personality,[("trp_boar",3,12)]),
  ("wolf_herd","Wolf Pack",LazyFlag("icon_flagbearer_b")|carries_goods(10),0,"fac_wild_animals",merchant_personality,[("trp_wolf",4,18)]),
  ("coat_herd","Goat Herd",LazyFlag("icon_flagbearer_b")|carries_goods(10),0,"fac_wild_animals",merchant_personality,[("trp_coat",4,28)]),
  ("coatb_herd","Goat Herd",LazyFlag("icon_flagbearer_b")|carries_goods(10),0,"fac_wild_animals",merchant_personality,[("trp_coat_b",4,28)]),
  ("wilddonkey_herd","Wild Donkey Herd",LazyFlag("icon_flagbearer_b")|carries_goods(10),0,"fac_wild_animals",merchant_personality,[("trp_wilddonkey",6,18)]),
  ("wildanimalslot1","slot Donkey Herd",LazyFlag("icon_flagbearer_b")|carries_goods(10),0,"fac_wild_animals",merchant_personality,[("trp_wilddonkey",6,18)]),
  ("wildanimalslot2","slot Donkey Herd",LazyFlag("icon_flagbearer_b")|carries_goods(10),0,"fac_wild_animals",merchant_personality,[("trp_wilddonkey",6,18)]),
#  ("village_hunters","Village Hunters",LazyFlag("icon_peasant"),0,"fac_innocents",soldier_personality,[("trp_hunter",8,16)]),

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting chief Mod end#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Caravans
  ("center_reinforcements","Reinforcements",LazyFlag("icon_axeman")|carries_goods(16),0,"fac_commoners",soldier_personality,[("trp_townsman",5,30),("trp_merc_infantryt2",4,20)]),
  
  ("kingdom_hero_party","War Party",LazyFlag("icon_flagbearer_a")|pf_show_faction|pf_default_behavior,0,"fac_commoners",soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_jute_recruit",2,4),("trp_jute_footmant2",2,5),("trp_jute_archert1",1,3)]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_jute_skirmishert3",6,12),("trp_jute_infantryt3",6,12),("trp_jute_skirmishert4",3,6)]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_jute_infantryt4",4,10),("trp_jute_portaestandarte",0,1),("trp_jute_cleric",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_saxon_recruit",2,4),("trp_saxon_footmant2",2,5),("trp_saxon_archer",1,3)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_saxon_skirmishert3",6,12),("trp_saxon_infantryt3",6,12),("trp_saxon_skirmishert4",3,6)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_saxon_infantryt4",4,10),("trp_saxon_bannerman",0,1),("trp_saxon_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_saxon_recruit",2,4),("trp_saxon_footmant2",2,5),("trp_saxon_archer",1,3)]),
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_saxon_skirmishert3",6,12),("trp_saxon_infantryt3",6,12),("trp_saxon_skirmishert4",3,6)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_saxon_infantryt4",4,10),("trp_saxon_bannerman",0,1),("trp_pagan_priest",0,1),("trp_saxon_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_engle_recruit",2,4),("trp_engle_footmant2",2,5),("trp_engle_archer",1,3)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_engle_skirmishert3",6,12),("trp_engle_infantryt3",6,12),("trp_engle_skirmishert4",3,6)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_engle_infantryt4",4,10),("trp_engle_bannerman",0,1),("trp_engle_rxpriest",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_saxon_recruit",2,3),("trp_fresna_recruit",0,1),("trp_saxon_footmant2",2,5),("trp_saxon_archer",1,3)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_saxon_skirmishert3",6,12),("trp_saxon_infantryt3",6,12),("trp_saxon_skirmishert4",3,6)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_saxon_infantryt4",4,10),("trp_saxon_bannerman",0,1),("trp_pagan_priest",0,1),("trp_saxon_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,5),("trp_briton_archer",2,4)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_saxon_skirmishert3",6,12),("trp_saxon_infantryt3",6,12),("trp_saxon_skirmishert4",3,6)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_saxon_infantryt4",4,10),("trp_saxon_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),
  
  ("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_engle_recruit",2,4),("trp_engle_footmant2",2,5),("trp_engle_archer",1,3)]),
  ("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_engle_skirmishert3",6,12),("trp_engle_infantryt3",6,12),("trp_engle_skirmishert4",3,6)]),
  ("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_engle_infantryt4",4,10),("trp_engle_bannerman",0,1),("trp_pagan_priest",0,1),("trp_todos_cuerno",0,1)]),
  
  ("kingdom_10_reinforcements_a", "{!}kingdom_10_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_10_reinforcements_b", "{!}kingdom_10_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_10_reinforcements_c", "{!}kingdom_10_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_11_reinforcements_a", "{!}kingdom_11_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_11_reinforcements_b", "{!}kingdom_11_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_11_reinforcements_c", "{!}kingdom_11_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_12_reinforcements_a", "{!}kingdom_12_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_12_reinforcements_b", "{!}kingdom_12_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_12_reinforcements_c", "{!}kingdom_12_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",1,2),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_13_reinforcements_a", "{!}kingdom_13_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_engle_recruit",2,4),("trp_engle_footmant2",2,5),("trp_engle_archer",1,3)]),
  ("kingdom_13_reinforcements_b", "{!}kingdom_13_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_engle_skirmishert3",6,12),("trp_engle_infantryt3",6,12),("trp_engle_skirmishert4",3,6)]),
  ("kingdom_13_reinforcements_c", "{!}kingdom_13_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_engle_infantryt4",4,10),("trp_engle_bannerman",0,1),("trp_engle_rxpriest",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_14_reinforcements_a", "{!}kingdom_14_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_engle_recruit",2,4),("trp_engle_footmant2",2,5),("trp_engle_archer",1,3)]),
  ("kingdom_14_reinforcements_b", "{!}kingdom_14_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_engle_skirmishert3",6,12),("trp_engle_infantryt3",6,12),("trp_engle_skirmishert4",3,6)]),
  ("kingdom_14_reinforcements_c", "{!}kingdom_14_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_engle_infantryt4",4,10),("trp_engle_bannerman",0,1),("trp_pagan_priest",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_15_reinforcements_a", "{!}kingdom_15_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_15_reinforcements_b", "{!}kingdom_15_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_15_reinforcements_c", "{!}kingdom_15_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_16_reinforcements_a", "{!}kingdom_16_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_16_reinforcements_b", "{!}kingdom_16_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_16_reinforcements_c", "{!}kingdom_16_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_17_reinforcements_a", "{!}kingdom_17_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_irish_recruit",2,5),("trp_irish_footmant2",2,4),("trp_irish_archer",2,3)]),
  ("kingdom_17_reinforcements_b", "{!}kingdom_17_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_irish_infantryt3",4,11),("trp_irish_skirmishert3",4,10),("trp_irish_horseman",4,9)]),
  ("kingdom_17_reinforcements_c", "{!}kingdom_17_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_irish_skirmishert4",4,10),("trp_irish_bannerman",0,1),("trp_irish_priest",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_18_reinforcements_a", "{!}kingdom_18_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_18_reinforcements_b", "{!}kingdom_18_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_18_reinforcements_c", "{!}kingdom_18_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_19_reinforcements_a", "{!}kingdom_19_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_irish_recruit",2,5),("trp_irish_footmant2",2,4),("trp_irish_archer",2,3)]),
  ("kingdom_19_reinforcements_b", "{!}kingdom_19_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_irish_infantryt3",4,11),("trp_irish_skirmishert3",4,10),("trp_irish_horseman",4,9)]),
  ("kingdom_19_reinforcements_c", "{!}kingdom_19_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_irish_skirmishert4",4,10),("trp_irish_bannerman",0,1),("trp_irish_priest",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_20_reinforcements_a", "{!}kingdom_20_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_pict_recruit",2,3),("trp_pict_woman",1,2),("trp_pict_footmant2",2,4),("trp_pict_archer",2,3)]),
  ("kingdom_20_reinforcements_b", "{!}kingdom_20_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_pict_skirmishert3",5,11),("trp_pict_horsesquiret3",5,11),("trp_pict_horseman",4,8)]),
  ("kingdom_20_reinforcements_c", "{!}kingdom_20_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_pict_skirmishert4",4,10),("trp_picto_portaestandarte",0,1),("trp_picto_sacerdote",0,1),("trp_picto_cuerno",0,1)]),

  ("kingdom_21_reinforcements_a", "{!}kingdom_21_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_21_reinforcements_b", "{!}kingdom_21_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_21_reinforcements_c", "{!}kingdom_21_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_22_reinforcements_a", "{!}kingdom_22_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_22_reinforcements_b", "{!}kingdom_22_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_22_reinforcements_c", "{!}kingdom_22_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_23_reinforcements_a", "{!}kingdom_23_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_23_reinforcements_b", "{!}kingdom_23_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_23_reinforcements_c", "{!}kingdom_23_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_24_reinforcements_a", "{!}kingdom_24_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_24_reinforcements_b", "{!}kingdom_24_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_24_reinforcements_c", "{!}kingdom_24_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_25_reinforcements_a", "{!}kingdom_25_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_25_reinforcements_b", "{!}kingdom_25_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_25_reinforcements_c", "{!}kingdom_25_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_26_reinforcements_a", "{!}kingdom_26_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_recruit",2,4),("trp_briton_footmant2",2,4),("trp_briton_archer",2,4)]),
  ("kingdom_26_reinforcements_b", "{!}kingdom_26_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",5,11),("trp_briton_skirmt3",5,11),("trp_briton_horseman",4,8)]),
  ("kingdom_26_reinforcements_c", "{!}kingdom_26_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_skirmishert4",4,10),("trp_briton_bannerman",0,1),("trp_briton_sacerdote",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_27_reinforcements_a", "{!}kingdom_27_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_irish_recruit",2,5),("trp_irish_footmant2",2,4),("trp_irish_archer",2,3)]),
  ("kingdom_27_reinforcements_b", "{!}kingdom_27_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_irish_infantryt3",4,11),("trp_irish_skirmishert3",4,10),("trp_irish_horseman",4,9)]),
  ("kingdom_27_reinforcements_c", "{!}kingdom_27_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_irish_skirmishert4",4,10),("trp_irish_bannerman",0,1),("trp_irish_priest",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_28_reinforcements_a", "{!}kingdom_28_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_irish_recruit",2,5),("trp_irish_footmant2",2,4),("trp_irish_archer",2,3)]),
  ("kingdom_28_reinforcements_b", "{!}kingdom_28_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_irish_infantryt3",4,11),("trp_irish_skirmishert3",4,10),("trp_irish_horseman",4,9)]),
  ("kingdom_28_reinforcements_c", "{!}kingdom_28_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_irish_skirmishert4",4,10),("trp_irish_bannerman",0,1),("trp_irish_priest",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_29_reinforcements_a", "{!}kingdom_29_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_irish_recruit",2,5),("trp_irish_footmant2",2,4),("trp_irish_archer",2,3)]),
  ("kingdom_29_reinforcements_b", "{!}kingdom_29_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_irish_infantryt3",4,11),("trp_irish_skirmishert3",4,10),("trp_irish_horseman",4,9)]),
  ("kingdom_29_reinforcements_c", "{!}kingdom_29_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_irish_skirmishert4",4,10),("trp_irish_bannerman",0,1),("trp_irish_priest",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_30_reinforcements_a", "{!}kingdom_30_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_irish_recruit",2,5),("trp_irish_footmant2",2,4),("trp_irish_archer",2,3)]),
  ("kingdom_30_reinforcements_b", "{!}kingdom_30_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_irish_infantryt3",4,11),("trp_irish_skirmishert3",4,10),("trp_irish_horseman",4,9)]),
  ("kingdom_30_reinforcements_c", "{!}kingdom_30_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_irish_skirmishert4",4,10),("trp_irish_bannerman",0,1),("trp_irish_priest",0,1),("trp_todos_cuerno",0,1)]),

  ("kingdom_31_reinforcements_a", "{!}kingdom_31_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_irish_recruit",2,5),("trp_irish_footmant2",2,4),("trp_irish_archer",2,3)]),
  ("kingdom_31_reinforcements_b", "{!}kingdom_31_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_irish_infantryt3",4,11),("trp_irish_skirmishert3",4,10),("trp_irish_horseman",4,9)]),
  ("kingdom_31_reinforcements_c", "{!}kingdom_31_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_irish_skirmishert4",4,10),("trp_irish_bannerman",0,1),("trp_irish_priest",0,1),("trp_todos_cuerno",0,1)]),

##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_briton_infantryt3",3,7),("trp_briton_archer",5,10),("trp_briton_footmant2",11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_briton_horseman",5,10),("trp_briton_skirmt3",5,10),("trp_briton_infantryt4",3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_briton_cavalry",2,6),("trp_briton_skirmishert4",2,5),("trp_briton_longbowman",2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_saxon_skirmishert3",3,7),("trp_saxon_archer",5,10),("trp_saxon_footmant2",11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_saxon_horseman1",4,9),("trp_saxon_infantryt3",5,10),("trp_saxon_infantryt4",3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_saxon_skirmishert5",3,7),("trp_saxon_skirmishert4",2,5),("trp_saxon_infantryt5",2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_pict_footmant2",3,7),("trp_pict_archer",5,10),("trp_pict_recruit",11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_pict_horsesquiret3",4,9),("trp_pict_skirmishert3",5,10),("trp_pict_footmant2",3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_pict_skirmishert4",3,7),("trp_pict_horsesquiret3",2,5),("trp_pict_skirmishert3",2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_engle_skirmishert3",3,7),("trp_engle_footmant2",5,10),("trp_engle_recruit",11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_engle_skirmishert4",4,9),("trp_engle_infantryt3",5,10),("trp_engle_footmant2",3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_engle_horseman",1,3),("trp_engle_skirmishert4",2,5),("trp_engle_infantryt3",2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, "fac_commoners", 0, [("trp_irish_footmant2",3,7),("trp_irish_archer",5,10),("trp_irish_recruit",11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, "fac_commoners", 0, [("trp_irish_infantryt3",4,9),("trp_irish_footmant2",5,10),("trp_irish_archer",3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, "fac_commoners", 0, [("trp_irish_infantryt5",3,7),("trp_irish_skirmishert3",2,5),("trp_irish_horseman",2,5)]),



  ("steppe_bandit_lair" ,"Scoti Lair",LazyFlag("icon_camp")|carries_goods(2)|pf_is_static|pf_hide_defenders,0,"fac_neutral",bandit_personality,[("trp_steppe_bandit",15,58)]),#chief cambiado icono
  ("taiga_bandit_lair","Outlaw Bandit Lair",LazyFlag("icon_camp")|carries_goods(2)|pf_is_static|pf_hide_defenders,0,"fac_neutral",bandit_personality,[("trp_taiga_bandit",15,58)]),#chief cambiado icono
  ("desert_bandit_lair" ,"Bandit Lair",LazyFlag("icon_camp")|carries_goods(2)|pf_is_static|pf_hide_defenders,0,"fac_neutral",bandit_personality,[("trp_desert_bandit",15,58)]),#chief cambiado icono
  ("forest_bandit_lair" ,"Unrights Bandit Camp",LazyFlag("icon_camp")|carries_goods(2)|pf_is_static|pf_hide_defenders,0,"fac_neutral",bandit_personality,[("trp_forest_bandit",15,58)]),#chief cambiado icono
  ("mountain_bandit_lair" ,"Morths Bandit Hideout",LazyFlag("icon_camp")|carries_goods(2)|pf_is_static|pf_hide_defenders,0,"fac_neutral",bandit_personality,[("trp_mountain_bandit",15,58)]),#chief cambiado icono
  ("sea_raider_lair","Frankish Landing",LazyFlag("icon_ship_on_land")|carries_goods(2)|pf_is_static|pf_hide_defenders,0,"fac_neutral",bandit_personality,[("trp_sea_raider",15,50)]), #chief cambiado icono
  ("sea_raider_lair2","Dena Landing",LazyFlag("icon_ship_on_land")|carries_goods(2)|pf_is_static|pf_hide_defenders,0,"fac_neutral",bandit_personality,[("trp_dena_pirate",15,50)]), #chief cambiado icono
  ("looter_lair","Kidnappers' Hideout",LazyFlag("icon_camp")|carries_goods(2)|pf_is_static|pf_hide_defenders,0,"fac_neutral",bandit_personality,[("trp_looter",15,25)]),#chief cambiado icono
  #gdw ("bandits_awaiting_ransom","Bandits Awaiting Ransom",LazyFlag("icon_axeman")|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,"fac_neutral",bandit_personality,[("trp_bandit",24,58),("trp_kidnapped_girl",1,1,pmf_is_prisoner)]),
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",LazyFlag("icon_axeman")|carries_goods(2)|pf_is_static,0,"fac_outlaws",bandit_personality,[("trp_sea_raider",15,50)]),

  ("leaded_looters","Band of Robbers",LazyFlag("icon_axeman")|carries_goods(8)|pf_quest_party,0,"fac_neutral",bandit_personality,[("trp_looter_leader",1,1),("trp_looter",3,3)]),

   ##diplomacy chief begin
  ("dplmc_spouse","Your spouse",LazyFlag("icon_woman")|pf_civilian|pf_show_faction,0,"fac_neutral",merchant_personality,[]),

  ("dplmc_gift_caravan","Your Caravan",LazyFlag("icon_mule")|carries_goods(45)|pf_show_faction,0,"fac_commoners",escorted_merchant_personality,[("trp_caravan_master",1,1),("trp_merc_infantryt3",5,25)]),
   ##diplomacy chief  end
#tempered chief
  ("skirmish_party","Skirmishers",LazyFlag("icon_khergit")|carries_goods(1)|pf_always_visible|pf_limit_members,0,"fac_commoners",aggressiveness_0 | courage_15,[]), #Tempered chief skirmish party
  ("spy_party","Cautious Traveler",LazyFlag("icon_gray_knight")|carries_goods(1)|pf_always_visible|pf_limit_members,0,"fac_commoners",aggressiveness_0 | courage_15,[("trp_merc_spy",1,1)]), #Tempered chief spy party 
  ("player_loot_wagon","Supply Wagon",LazyFlag("icon_mule")|pf_show_faction|pf_quest_party,0,"fac_commoners",escorted_merchant_personality,[]), #Tempered chief added player loot wagon
  ("escaped_companion","Exhausted Companion",LazyFlag("icon_gray_knight")|pf_show_faction,0,"fac_commoners",escorted_merchant_personality,[]), #Tempered chief added for defeated player companions
  ("funeral_pyre","Funeral Pyre",LazyFlag("icon_funeral_pyre")|pf_is_static|pf_hide_defenders|pf_always_visible|pf_no_label ,0,"fac_neutral",escorted_merchant_personality,[]), #tempered chief funeral pyre
  ("personal_messenger","Messenger",LazyFlag("icon_gray_knight")|pf_always_visible|pf_limit_members,0,"fac_commoners",aggressiveness_0 | courage_15,[("trp_merc_spy",1,1)]), #Tempered chief messenger
  ("entrench","Entrenchment",LazyFlag("icon_last_entrench")|pf_is_static|pf_always_visible|pf_no_label,0, "fac_neutral",bandit_personality,[]),  
#tempered chief acaba
#chief sacerdotes party
  ("sacerdotes_party","Christian Clergy",LazyFlag("icon_peasant")|carries_goods(2),0,"fac_christians",merchant_personality,[("trp_picto_sacerdote",3,9), ("trp_peasant_woman",4,15)]),
  ("paganos_party","Pagan Priests",LazyFlag("icon_peasant")|carries_goods(2),0,"fac_pagans",merchant_personality,[("trp_pagan_priest",3,9), ("trp_farmer",4,15)]),

  # Script de refuerzos y reclutas a ciudades chief
  #("reinforcements","Reinforcements",LazyFlag("icon_axeman")|pf_show_faction,0,"fac_commoners",soldier_personality,[]),
#mas chief
#wulf
  ("sea_raiders_ships","Frankish Pirates",LazyFlag("icon_ship")|pf_is_ship|carries_goods(2),0,"fac_outlaws",bandit_personality,[("trp_sea_raider",20,40)]),
  ("sea_raiders_ships2","Dena Pirates",LazyFlag("icon_ship")|pf_is_ship|carries_goods(2),0,"fac_outlaws",bandit_personality,[("trp_dena_pirate",20,40)]),
  ("sea_raiders_ships3","Scoti Pirates",LazyFlag("icon_ship")|pf_is_ship|carries_goods(2),0,"fac_outlaws",bandit_personality,[("trp_steppe_bandit",20,40)]),
#wulf end   ("sea_pierats","Sea Pirates",LazyFlag("icon_ship")|pf_is_ship|carries_goods(2),0,"fac_outlaws",bandit_personality,[("trp_sea_raider",20,40)]),
#otras chief
  ("bishop_party","Bishop",LazyFlag("icon_gray_knight")|carries_goods(5)|pf_auto_remove_in_town|pf_quest_party,0,"fac_commoners",escorted_merchant_personality,[("trp_bishop",1,1),("trp_picto_sacerdote",4,10)]),
#  ("scouts","Pictish Scouts",LazyFlag("icon_gray_knight")|carries_goods(1)|pf_show_faction,0,"fac_kingdom_20",bandit_personality,[("trp_pict_archer",10,20),("trp_pict_woman",1,1)]),
#  ("watchtower_scouts","Scouts",LazyFlag("icon_gray_knight")|carries_goods(1)|pf_show_faction,0,"fac_kingdom_20",bandit_personality,[("trp_mercenary_horseman",5,7)]),
("iniau","Iniau Scouts",LazyFlag("icon_saxon_skirmishert5")|carries_goods(1)|pf_auto_remove_in_town|pf_quest_party,0,"fac_neutral",bandit_personality,[("trp_iniau",1,1),("trp_briton_skirmishert4",43,65)]),#gdw
#chief followers seguidores
##Floris addon seatrade chief
  ("sea_traders","Sea Traders",LazyFlag("icon_ship")|pf_is_ship|carries_goods(50)|pf_show_faction,0,"fac_commoners",merchant_personality,[("trp_caravan_master",1,1),("trp_merc_infantryt3",20,40),("trp_merc_archer",10,25)]),
##Floris addon seatrade end
 #rigale chief
("ambushers","Ambushers",LazyFlag("icon_axeman")|carries_goods(2),0,"fac_forest_bandits",aggressiveness_15 | courage_15,[("trp_forest_bandit",5,80)]),
  ("zamoshie_bandits", "North Bandits",LazyFlag("icon_peasant")|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,"fac_neutral",bandit_personality,[("trp_forest_bandit",27,49),("trp_looter_theow_leader",3,4)] ),

	("ship"	,"Ship",LazyFlag("icon_ship")|pf_is_ship|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction,0,"fac_commoners",merchant_personality,[("trp_mercenary_leader",1,1)]),
  ("ambushers1","slotAmbushers",LazyFlag("icon_axeman")|carries_goods(2),0,"fac_forest_bandits",aggressiveness_15 | courage_15,[("trp_forest_bandit",5,80)]),
  ("ambushers2","slotAmbushers",LazyFlag("icon_axeman")|carries_goods(2),0,"fac_forest_bandits",aggressiveness_15 | courage_15,[("trp_forest_bandit",5,80)]),
  ("ambushers3","slotAmbushers",LazyFlag("icon_axeman")|carries_goods(2),0,"fac_forest_bandits",aggressiveness_15 | courage_15,[("trp_forest_bandit",5,80)]),
  

  ##  ("followers","Camp Followers",LazyFlag("icon_mule")|carries_goods(25)|pf_show_faction,0,"fac_commoners",merchant_personality,[("trp_caravan_master",1,3),("trp_merc_infantryt3",4,6),("trp_farmer",3,14),("trp_follower_woman",15,60),("trp_fighter_woman",12,40)]),
##  ("followersplayer","Camp Followers",LazyFlag("icon_mule")|carries_goods(25)|pf_show_faction,0,"fac_commoners",merchant_personality,[("trp_caravan_master",1,3),("trp_merc_infantryt3",4,6),("trp_farmer",3,14),("trp_follower_woman",15,60),("trp_fighter_woman",12,40)]),
# Foragers SoT chief
###anglos
##  ("bernician_foragers","Acerweras",LazyFlag("icon_gray_knight")|carries_goods(5),0,"fac_kingdom_4",merchant_personality,[("trp_engle_footmant2",5,10),("trp_engle_archer",2,4),("trp_engle_infantryt3",2,4)]),
###jutos
##  ("rheged_foragers","Foragers",LazyFlag("icon_saxon_skirmishert5")|carries_goods(5),0,"fac_kingdom_1",merchant_personality,[("trp_jute_footmant2",5,10),("trp_jute_archert1",2,4),("trp_jute_infantryt3",2,4)]),
###britons
##  ("gododdin_foragers","Foragers",LazyFlag("icon_saxon_skirmishert5")|carries_goods(5),0,"fac_kingdom_3",merchant_personality,[("trp_briton_footmant2",3,7),("trp_briton_infantryt3",3,5),("trp_briton_archer",2,6)]),
###sajones
##  ("dalriadan_foragers","Foragers",LazyFlag("icon_saxon_skirmishert5")|carries_goods(5),0,"fac_kingdom_2",merchant_personality,[("trp_saxon_footmant2",5,10),("trp_saxon_archer",2,4),("trp_saxon_infantryt3",2,4)]),
###irish
##  ("alcluyd_foragers","Foragers",LazyFlag("icon_saxon_skirmishert5")|carries_goods(5),0,"fac_kingdom_7",merchant_personality,[("trp_irish_footmant2",5,10),("trp_irish_archer",2,4),("trp_irish_skirmishert3",2,4)]),
###pictos
##  ("pictish_foragers","Pictish Foragers",LazyFlag("icon_saxon_skirmishert5")|carries_goods(5),0,"fac_kingdom_5",merchant_personality,[("trp_pict_archer",6,12),("trp_pict_horseman",3,5),("trp_pict_woman",1,3)]),

] \
    + constable.party_templates
