from header_triggers import key_z, key_t, key_o, key_f7, key_n

##############################################################
# These constants are used in various files.
# If you need to define a value that will be used in those files,
# just define it here rather than copying it across each file, so
# that it will be easy to change it if you need to.

###################### Agent constants ######################
#############################################################

# order types and respective keys
ranged = 0
onehand = 1
bothhands = 2
shield = 3
clear = -1

key_for_onehand = key_z
key_for_bothhands = key_t
key_for_ranged = key_n
key_for_shield = key_o

# Bleeding
blood_per_hp = 600
dmg_threshold = 3
dmg_low_range = 6
dmg_hi_range = 12

# bard
instruments_begin = "itm_lyre"
instruments_end = "itm_instruments_end"
income_denars = 1
income_honor = 2
income_reputation = 3
income_right_to_rule = 4
income_bard_reputation = 5
entertainment_simple = 0
entertainment_medium = 1
entertainment_complex = 2
entertainment_lordly = 3
entertainment_royal = 4
entertainment_speech = 5

##################### Faction constants #####################
#############################################################

# "slot_faction_state" values
sfs_active = 0
sfs_defeated = 1
sfs_inactive = 2
# sfs_inactive_rebellion         = 3
# sfs_beginning_rebellion        = 4


# "slot_faction_ai_state" values
sfai_default = 0  # also defending
sfai_gathering_army = 1
sfai_attacking_center = 2
sfai_raiding_village = 3
sfai_attacking_enemy_army = 4
sfai_attacking_enemies_around_center = 5
sfai_feast = 6  # can be feast, wedding, or major tournament

# Social events are a generic aristocratic gathering. Tournaments take place if they are in a town,
# and hunts take place if they are at a castle.
# Weddings will take place at social events between betrothed couples if they have been engaged
# for at least a month, if the lady's guardian is the town lord, and if both bride and groom are present

# revolts -- notes for self
# type 1 -- minor revolt, aimed at negotiating change without changing the ruler
# type 2 -- alternate ruler revolt (ie, pretender, chinese dynastic revolt -- keep the same polity but switch the ruler)
# subtype -- pretender (keeps the same dynasty)
# "mandate of heaven" -- same basic rules, but a different dynasty
# alternate/religious
# alternate/political
# type 3 -- separatist revolt
# reGonalist/dynastic (based around an alternate ruling house
# regionalist/republican
# messianic (ie, Canudos)

# Treaty lengths.  Use these constants instead of "magic numbers" to make it
# obvious what code is supposed to do, and also make it easy to change the
# lengths without having to go through the entire mod.

# Truces (as exist in Native)
dplmc_treaty_truce_days_initial = 20
dplmc_treaty_truce_days_expire = 0

# Trade treaties convert to truces after 20 days.
dplmc_treaty_trade_days_initial = 40
dplmc_treaty_trade_days_expire = dplmc_treaty_truce_days_initial

# Defensive alliances convert to trade treaties after 20 days.
dplmc_treaty_defense_days_initial = 60
dplmc_treaty_defense_days_expire = dplmc_treaty_trade_days_initial

# Alliances convert to defensive alliances after 20 days.
dplmc_treaty_alliance_days_initial = 80
dplmc_treaty_alliance_days_expire = dplmc_treaty_defense_days_initial

# Define these by name to make them more clear in the source code.
# They should not be altered from their definitions.
dplmc_treaty_truce_days_half_done = (dplmc_treaty_truce_days_initial + dplmc_treaty_truce_days_expire) // 2
dplmc_treaty_trade_days_half_done = (dplmc_treaty_trade_days_initial + dplmc_treaty_trade_days_expire) // 2
dplmc_treaty_defense_days_half_done = (dplmc_treaty_defense_days_initial + dplmc_treaty_defense_days_expire) // 2
# dplmc_treaty_alliance_days_half_done = (dplmc_treaty_alliance_days_initial + dplmc_treaty_alliance_days_expire) // 2


###################### Party constants ######################
#############################################################

# "slot_lord_recruitement_argument"
argument_claim = 1
# todo: remove one of the two following arguments
argument_ruler = 2  # deprecate for commons
argument_commons = 2
argument_benefit = 3
argument_victory = 4
argument_lords = 5

# slot_party_type values
spt_castle = 2
spt_town = 3
spt_village = 4
spt_merchant_caravan = 5  # sea trader
spt_patrol = 7
spt_messenger = 8
spt_companion_raider = 9
spt_scout = 10
spt_kingdom_caravan = 11
dplmc_spt_recruiter = 12
spt_kingdom_hero_party = 13
spt_village_farmer = 15
spt_ship = 16
spt_cattle_herd1 = 17
spt_bandit_lair = 18
dplmc_spt_spouse = 19
spt_entrenchment = 23
dplmc_spt_gift_caravan = 116
spt_player_loot_wagon = 210

# "slot_party_ai_state"
spai_undefined = -1
spai_besieging_center = 1
spai_patrolling_around_center = 4
spai_raiding_around_center = 5
spai_holding_center = 7
spai_engaging_army = 10
spai_accompanying_army = 11
spai_screening_army = 12
spai_trading_with_town = 13
spai_retreating_to_center = 14
spai_visiting_village = 16

# "slot_village_state"
svs_normal = 0
svs_being_raided = 1
svs_looted = 2
svs_deserted = 4
svs_under_siege = 5

# "$g_player_icon_state"
pis_normal = 0
pis_camping = 1
pis_ship = 2

num_party_loot_slots = 5

# initial position of the ram
pos_ram_begin = 35

# "slot_ship_center"
ship_wild_no_guard = 100
ship_wild_guarded = 150
ship_player_sailing = 200

###################### Troop constants ######################
#############################################################

# "slot_troop_morality_state"
# "slot_troop_2ary_morality_state"
tms_no_problem = 0
tms_acknowledged = 1
tms_dismissed = 2

# "slot_troop_morality_type"
# "slot_troop_2ary_morality_type"
tmt_aristocratic = 1
tmt_egalitarian = 2
tmt_humanitarian = 3
tmt_honest = 4
tmt_pious = 5

# "slot_troop_personalityclash_state"
pclash_penalty_to_self = 1
pclash_penalty_to_other = 2
pclash_penalty_to_both = 3

# "slot_troop_playerparty_history"
pp_history_scattered = 1
pp_history_dismissed = 2
pp_history_quit = 3
pp_history_indeterminate = 4

# "slot_troop_mission_object"
npc_mission_kingsupport = 1
npc_mission_gather_intel = 2
npc_mission_peace_request = 3
npc_mission_pledge_vassal = 4
npc_mission_seek_recognition = 5
npc_mission_test_waters = 6
npc_mission_non_aggression = 7
npc_mission_rejoin_when_possible = 8
npc_mission_on_patrol = 20

# "slot_troop_mission_participation"
mp_stay_out = 1
mp_prison_break_fight = 2
mp_prison_break_stand_back = 3
mp_prison_break_escaped = 4
mp_prison_break_caught = 5

# duel constants
king_renown_for_duel = 350  # Minimum renown needed to challenge a king to a friendly duel
lord_renown_for_duel = 50  # Minimum renown needed to challenge a king to a friendly duel

# "slot_lord_reputation_type"
lrep_none = 0
lrep_martial = 1  # chivalrous but not terribly empathetic or introspective, - eg Richard Lionheart, your average 14th century French baron
lrep_quarrelsome = 2  # spiteful, cynical, a bit paranoid, possibly hotheaded - eg Robert Graves' Tiberius, some of Charles VI's uncles
lrep_selfrighteous = 3  # coldblooded, moralizing, often cruel - eg William the Conqueror, Timur, Octavian, Aurangzeb (although he is arguably upstanding instead, particularly after his accession)
lrep_cunning = 4  # coldblooded, pragmatic, amoral - eg Louis XI, Guiscard, Akbar Khan, Abd al-Aziz Ibn Saud
lrep_debauched = 5  # spiteful, amoral, sadistic - eg Caligula, Tuchman's Charles of Navarre
lrep_goodnatured = 6  # chivalrous, benevolent, perhaps a little too decent to be a good warlord - eg Hussein ibn Ali. Few well-known historical examples maybe. because many lack the drive to rise to faction leadership. Ranjit Singh has aspects
lrep_upstanding = 7  # moralizing, benevolent, pragmatic, - eg Bernard Cornwell's Alfred, Charlemagne, Salah al-Din, Sher Shah Suri

lrep_roguish = 8  # used for commons, specifically ex-companions. Tries to live life as a lord to the full
lrep_benefactor = 9  # used for commons, specifically ex-companions. Tries to improve lot of folks on land
lrep_custodian = 10  # used for commons, specifically ex-companions. Tries to maximize fief's earning potential

lrep_conventional = 21  # Charlotte York in SATC seasons 1-2, probably most medieval aristocrats
lrep_adventurous = 22  # Tomboyish. However, this basically means that she likes to travel and hunt, and perhaps yearn for wider adventures. However, medieval noblewomen who fight are rare, and those that attempt to live independently of a man are rarer still, and best represented by pre-scripted individuals like companions
lrep_otherworldly = 23  # Prone to mysticism, romantic.
lrep_ambitious = 24  # Lady Macbeth
lrep_moralist = 25  # Equivalent of upstanding or benefactor -- takes nobless oblige, and her traditional role as repository of morality, very seriously. Based loosely on Christine de Pisa

# "slot_troop_occupation"
slto_inactive = 0  # for companions at the beginning of the game
slto_kingdom_hero = 2
slto_player_companion = 5  # This is specifically for companions in the employ of the player -- ie, in the party, or on a mission
slto_kingdom_lady = 6  # Usually inactive (Calradia is a traditional place). However, can be made potentially active if active_npcs are expanded to include ladies
slto_kingdom_seneschal = 7
slto_inactive_pretender = 9
slto_retirement = 11
dplmc_slto_exile = 14  # Set for newly exiled lords.  In saved games, this is retroactively applied (once only).
slto_dead = 86

# "slot_town_lord"
stl_unassigned = -1
stl_reserved_for_player = -2
stl_rejected_by_player = -3

# "slot_troop_current_mission"
plyr_mission_vacation = 1
dplmc_npc_mission_war_request = 9
dplmc_npc_mission_alliance_request = 10
dplmc_npc_mission_spy_request = 11
dplmc_npc_mission_gift_fief_request = 12
dplmc_npc_mission_gift_horses_request = 13
dplmc_npc_mission_threaten_request = 14
dplmc_npc_mission_prisoner_exchange = 15
dplmc_npc_mission_defensive_request = 16
dplmc_npc_mission_trade_request = 17
dplmc_npc_mission_nonaggression_request = 18
dplmc_npc_mission_persuasion = 19

####################### Team contexts #######################
#############################################################

# "slot_team_d0_formation"
formation_none = 0
formation_default = 1
formation_ranks = 2
formation_shield = 3
formation_wedge = 4
formation_square = 5

# Formation tweaks
formation_minimum_spacing = 42  # chief cambiado # TML less spacing (down to 30 from 47). I assume this variable is used, didn't check but it sounds good and between it and the one below they're closer together now so I'm happy. F123 - Submod -> 1.41
# gdw I disagree with this issue but will comp halfway. Too easy to flank naro form
formation_minimum_spacing_horse_length = 300
formation_minimum_spacing_horse_width = 200
formation_start_spread_out = 1
formation_min_foot_troops = 9
formation_min_cavalry_troops = 4
formation_native_ai_use_formation = 1
formation_reequip = 1  # TO DO: One-time-on-form option when formation slots integrated
formation_reform_interval = 2  # seconds
formation_rethink_for_formations_only = 0

# Other constants (not tweaks)
Third_Max_Weapon_Length = 250 / 3
Km_Per_Hour_To_Cm = formation_reform_interval * 100000 / 3600
Reform_Trigger_Modulus = formation_reform_interval * 2  # trigger is half-second
Top_Speed = 13
Far_Away = 1000000

# positions used through formations and AI triggers
Current_Pos = 34  # pos34
Speed_Pos = 36  # pos36
Target_Pos = 37  # pos37
Enemy_Team_Pos = 38  # pos38
Temp_Pos = 39  # pos39

scratch_team = 7

# "slot_team_d0_type"
sdt_infantry = 0
sdt_archer = 1
sdt_cavalry = 2
sdt_polearm = 3
sdt_skirmisher = 4
sdt_harcher = 5
sdt_support = 6
sdt_bodyguard = 7
sdt_unknown = -1

####################### Talk contexts #######################
#############################################################

tc_town_talk = 0
tc_court_talk = 1
tc_party_encounter = 2
tc_castle_gate = 3
tc_siege_commander = 4
tc_join_battle_ally = 5
tc_join_battle_enemy = 6
tc_castle_commander = 7
tc_hero_freed = 8
tc_hero_defeated = 9
tc_entering_center_quest_talk = 10
tc_back_alley = 11
tc_siege_won_seneschal = 12
tc_ally_thanks = 13
tc_tavern_talk = 14
tc_rebel_thanks = 15
tc_garden = 16
tc_courtship = 16
tc_after_duel = 17
tc_prison_break = 18
tc_escape = 19
tc_give_center_to_fief = 20
tc_merchants_house = 21
tc_roman_dungeon = 23
tc_odin_cave = 24

###################### Encounter types ######################
#############################################################

enctype_fighting_against_village_raid = 1
enctype_catched_during_village_raid = 2


###################### Log entry types ######################
#############################################################

logent_village_raided = 1
logent_village_extorted = 2
logent_caravan_accosted = 3  # in caravan accosted, center and troop object are -1, and the defender's faction is the object
logent_traveller_attacked = 3  # in traveller attacked, origin and destination are center and troop object, and the attacker's faction is the object

logent_helped_peasants = 4

logent_party_traded = 5

logent_castle_captured_by_player = 10
logent_lord_defeated_by_player = 11
logent_lord_captured_by_player = 12
logent_lord_defeated_but_let_go_by_player = 13
logent_player_defeated_by_lord = 14
logent_player_retreated_from_lord = 15
logent_player_retreated_from_lord_cowardly = 16
logent_lord_helped_by_player = 17
logent_player_participated_in_siege = 18
logent_player_participated_in_major_battle = 19
logent_castle_given_to_lord_by_player = 20

logent_pledged_allegiance = 21
logent_liege_grants_fief_to_vassal = 22

logent_renounced_allegiance = 23

logent_player_claims_throne_1 = 24
logent_player_claims_throne_2 = 25

logent_troop_feels_cheated_by_troop_over_land = 26
logent_ruler_intervenes_in_quarrel = 27
logent_lords_quarrel_over_woman = 31

logent_lord_protests_marshall_appointment = 32
logent_lord_blames_defeat = 33

logent_player_suggestion_succeeded = 35
logent_player_suggestion_failed = 36

logent_liege_promises_fief_to_vassal = 37

logent_game_start = 45

logent_lady_favors_suitor = 51  # basically for gossip
logent_lady_betrothed_to_suitor_by_choice = 52
logent_lady_betrothed_to_suitor_by_family = 53
logent_lady_rejects_suitor = 54
logent_lady_father_rejects_suitor = 55
logent_lady_marries_lord = 56
logent_lady_elopes_with_lord = 57
logent_lady_rejected_by_suitor = 58
logent_lady_betrothed_to_suitor_by_pressure = 59  # mostly for gossip

logent_lady_marries_suitor = 61

logent_player_stole_cattles_from_village = 66

logent_party_spots_wanted_bandits = 70

logent_border_incident_cattle_stolen = 72  # possibly add this to rumors for non-player faction
logent_border_incident_bride_abducted = 73  # possibly add this to rumors for non-player faction
logent_border_incident_villagers_killed = 74  # possibly add this to rumors for non-player faction
logent_border_incident_subjects_mistreated = 75  # possibly add this to rumors for non-player faction

# These supplement caravans accosted and villages burnt, in that they create a provocation.
# So far, they only refer to the player
logent_border_incident_troop_attacks_neutral = 76
logent_border_incident_troop_breaks_truce = 77
logent_border_incident_troop_suborns_lord = 78

logent_policy_ruler_attacks_without_provocation = 80
logent_policy_ruler_ignores_provocation = 81  # possibly add this to rumors for non-player factions
logent_policy_ruler_makes_peace_too_soon = 82
logent_policy_ruler_declares_war_with_justification = 83
logent_policy_ruler_breaks_truce = 84

logent_player_faction_declares_war = 90  # this doubles for declare war to extend power
logent_faction_declares_war_out_of_personal_enmity = 91
logent_faction_declares_war_to_regain_territory = 92
logent_faction_declares_war_to_curb_power = 93
logent_faction_declares_war_to_respond_to_provocation = 94
logent_faction_declares_war_to_fulfil_pact = 95
logent_war_declaration_types_end = 96


###################### Other constants ######################
#############################################################

# Rebellion changes end
# character backgrounds
cb_noble = 1
cb_merchant = 2
cb_guard = 3
cb_forester = 4
cb_nomad = 5
cb_thief = 6

cb2_page = 0
cb2_apprentice = 1
cb2_urchin = 2
cb2_steppe_child = 3
cb2_merchants_helper = 4

cb3_poacher = 3
cb3_craftsman = 4
cb3_peddler = 5
cb3_troubadour = 7
cb3_squire = 8
cb3_lady_in_waiting = 9
cb3_student = 10

cb4_revenge = 1
cb4_loss = 2
cb4_wanderlust = 3
cb4_disown = 5
cb4_greed = 6

# different poems
courtship_poem_tragic = 1  # Emphasizes longing, Laila and Majnoon
courtship_poem_heroic = 2  # Norse sagas with female heroines
courtship_poem_comic = 3  # Emphasis on witty repartee -- Contrasto (Sicilian school satire)
courtship_poem_mystic = 4  # Sufi poetry. Song of Songs
courtship_poem_allegoric = 5  # Idealizes woman as a civilizing force -- the Romance of the Rose, Siege of the Castle of Love

# Troop Commentaries end

tutorial_fighters_begin = "trp_tutorial_fighter_1"
tutorial_fighters_end = "trp_tutorial_archer_1"

# Walker types:
walkert_default = 0
walkert_needs_money = 1
walkert_needs_money_helped = 2
walkert_spy = 3
num_town_walkers = 8
town_walker_entries_start = 32

reinforcement_cost_easy = 600
reinforcement_cost_moderate = 450
reinforcement_cost_hard = 300

merchant_toll_duration = 72  # Tolls are valid for 72 hours

hero_escape_after_defeat_chance = 39

raid_distance = 4

surnames_begin = "str_surname_1"
surnames_end = "str_surnames_end"
names_begin = "str_name_1"
names_end = surnames_begin
countersigns_begin = "str_countersign_1"

secret_signs_begin = "str_secret_sign_1"
secret_signs_end = countersigns_begin

kingdom_titles_male_begin = "str_faction_title_male_player"
kingdom_titles_female_begin = "str_faction_title_female_player"

kingdoms_begin = "fac_player_supporters_faction"
kingdoms_end = "fac_kingdoms_end"

npc_kingdoms_begin = "fac_kingdom_1"
npc_kingdoms_end = kingdoms_end

bandits_begin = "trp_looter"
bandits_end = "trp_manhunter"

kingdom_ladies_begin = "trp_knight_1_1_wife"
kingdom_ladies_end = "trp_heroes_end"

# active NPCs in order: companions, kings, lords, pretenders

pretenders_begin = "trp_kingdom_1_pretender"
pretenders_end = kingdom_ladies_begin

lords_begin = "trp_knight_1_1"
lords_end = pretenders_begin

kings_begin = "trp_kingdom_1_lord"
kings_end = lords_begin

companions_begin = "trp_npc1"
companions_end = "trp_companions_end"

active_npcs_begin = "trp_especiales_1"
active_npcs_end = kingdom_ladies_begin
# "active_npcs_begin replaces kingdom_heroes_begin to allow for companions to become lords. Includes anyone who may at some point lead their own party: the original kingdom heroes, companions who may become kingdom heroes, and pretenders. (slto_kingdom_hero as an occupation means that you lead a party on the map. Pretenders have the occupation "slto_inactive_pretender", even if they are part of a player's party, until they have their own independent party)
# If you're a modder and you don't want to go through and switch every kingdom_heroes to active_npcs, simply define a constant: kingdom_heroes_begin = active_npcs_begin., and kingdom_heroes_end = active_npcs_end. I haven't tested for that, but I think it should work.

kingdom_heroes_begin = active_npcs_begin  # puesto chief
kingdom_heroes_end = active_npcs_end  # puesto chief

active_npcs_including_player_begin = "trp_kingdom_heroes_including_player_begin"
original_kingdom_heroes_begin = "trp_kingdom_1_lord"

heroes_begin = active_npcs_begin
heroes_end = kingdom_ladies_end

soldiers_begin = "trp_farmer"
soldiers_end = "trp_town_walker_1"

kingdom_heroes_begin2 = "trp_kingdom_1_lord"
kingdom_heroes_end2 = kingdom_ladies_begin

outlaws_troops_begin = "trp_looter"
outlaws_troops_end = "trp_caravan_master"

bardo_begin = "trp_bardo_1"
bardo_end = "trp_sacerdote_1"

sacerdote_begin = "trp_sacerdote_1"
sacerdote_end = "trp_quastuosa_1"

quastuosa_begin = "trp_quastuosa_1"
quastuosa_end = "trp_especiales_1"

tavern_minstrels_begin = "trp_tavern_minstrel_1"
tavern_minstrels_end = bardo_begin

tavern_booksellers_begin = "trp_tavern_bookseller_1"
tavern_booksellers_end = tavern_minstrels_begin

tavern_travelers_begin = "trp_tavern_traveler_1"
tavern_travelers_end = tavern_booksellers_begin

ransom_brokers_begin = "trp_ransom_broker_1"
ransom_brokers_end = tavern_travelers_begin

mercenary_troops_begin = "trp_merc_infantryt2"
mercenary_troops_end = "trp_mercenaries_end"

multiplayer_troops_begin = "trp_multiplayer_empieza"
multiplayer_troops_end = "trp_multiplayer_end"

multiplayer_lordscapitan_begin = "trp_capitan1"
multiplayer_lordscapitan_end = "trp_tropa32"

multiplayer_ai_troops_begin = "trp_jute_infantryt3_multiplayer_ai"
multiplayer_ai_troops_end = "trp_multiplayer_empieza"

multiplayer_scenes_begin = "scn_multi_scene_1"
multiplayer_scenes_end = "scn_multiplayer_maps_end"

multiplayer_scene_names_begin = "str_multi_scene_1"
# multiplayer_scene_names_end = "str_multi_scene_end"

multiplayer_flag_projections_begin = "mesh_flag_project_sw"
# multiplayer_flag_projections_end = "mesh_flag_projects_end"

multiplayer_flag_taken_projections_begin = "mesh_flag_project_sw_miss"
# multiplayer_flag_taken_projections_end = "mesh_flag_project_misses_end"

multiplayer_game_type_names_begin = "str_multi_game_type_1"
# multiplayer_game_type_names_end = "str_multi_game_types_end"

quick_battle_troops_begin = "trp_quick_battle_troop_1"
quick_battle_troops_end = "trp_quick_battle_troops_end"

quick_battle_troop_texts_begin = "str_quick_battle_troop_1"
# quick_battle_troop_texts_end = "str_quick_battle_troops_end"

quick_battle_scenes_begin = "scn_quick_battle_scene_1"
quick_battle_scenes_end = "scn_quick_battle_maps_end"

quick_battle_scene_images_begin = "mesh_cb_ui_maps_scene_01"

quick_battle_battle_scenes_begin = quick_battle_scenes_begin
quick_battle_battle_scenes_end = "scn_quick_battle_scene_4"

quick_battle_siege_scenes_begin = quick_battle_battle_scenes_end
quick_battle_siege_scenes_end = quick_battle_scenes_end

quick_battle_scene_names_begin = "str_quick_battle_scene_1"

lord_quests_begin = "qst_deliver_message"
lord_quests_end = "qst_follow_army"

lord_quests_begin_2 = "qst_destroy_bandit_lair"
lord_quests_end_2 = "qst_blank_quest_2"

enemy_lord_quests_begin = "qst_lend_surgeon"
enemy_lord_quests_end = lord_quests_end

village_elder_quests_begin = "qst_deliver_grain"
village_elder_quests_end = "qst_eliminate_bandits_infesting_village"

village_elder_quests_begin_2 = "qst_blank_quest_6"
village_elder_quests_end_2 = "qst_blank_quest_6"

mayor_quests_begin = "qst_move_cattle_herd1"
mayor_quests_end = village_elder_quests_begin

mayor_quests_begin_2 = "qst_blank_quest_11"
mayor_quests_end_2 = "qst_blank_quest_11"

lady_quests_begin = "qst_rescue_lord_by_replace"
lady_quests_end = mayor_quests_begin

lady_quests_begin_2 = "qst_blank_quest_16"
lady_quests_end_2 = "qst_blank_quest_16"

army_quests_begin = "qst_deliver_cattle_to_army"
army_quests_end = lady_quests_begin

# bounty quest chief
outlaws_begin = "trp_bounty5"
outlaws_end = "trp_bounty6"

rogues_begin = "trp_bounty4"
rogues_end = "trp_bounty5"

goblin_outlaws_begin = "trp_bounty1"
goblin_outlaws_end = "trp_bounty4"

orc_outlaws_begin = "trp_bounty6"
orc_outlaws_end = "trp_bounty7"

elf_outlaws_begin = "trp_bounty8"
elf_outlaws_end = "trp_bounty9"

darkelf_outlaws_begin = "trp_bounty10"
darkelf_outlaws_end = "trp_bounty11"

saracen_outlaws_begin = "trp_bounty12"
saracen_outlaws_end = "trp_bounty1"

fugitives_begin = "trp_fugitive"
fugitives_end = "trp_fugitive2"

bounties_begin = "qst_bounty_1"
bounties_end = "qst_kill_local_merchant"

bandit_party_template_begin = "pt_steppe_bandits"
bandit_party_template_end = "pt_deserters"

all_items_begin = 0
all_items_end = "itm_items_end"

all_quests_begin = 0
all_quests_end = "qst_quests_end"

towns_begin = "p_town_1"
castles_begin = "p_castle_1"
villages_begin = "p_village_1"

towns_end = castles_begin
castles_end = villages_begin
villages_end = "p_salt_mine"

walled_centers_begin = towns_begin
walled_centers_end = castles_end

centers_begin = towns_begin
centers_end = villages_end

training_grounds_begin = "p_training_ground_1"
training_grounds_end = "p_monasterio1"

spawn_points_begin = "p_zendar"
spawn_points_end = "p_spawn_points_end"

regular_troops_begin = "trp_novice_fighter"
regular_troops_end = "trp_tournament_master"

arena_masters_begin = "trp_town_1_arena_master"
arena_masters_end = "trp_town_1_armorer"

training_gound_trainers_begin = "trp_trainer_1"
training_gound_trainers_end = "trp_ransom_broker_1"

town_walkers_begin = "trp_town_walker_1"
# town_walkers_end = "trp_village_walker_1"

# spy_walkers_begin = "trp_spy_walker_1"
spy_walkers_end = "trp_tournament_master"

walkers_begin = town_walkers_begin
walkers_end = spy_walkers_end

armor_merchants_begin = "trp_town_1_armorer"
armor_merchants_end = "trp_town_1_weaponsmith"

weapon_merchants_begin = "trp_town_1_weaponsmith"
weapon_merchants_end = "trp_specialmerch1"

special_merchants_begin = "trp_specialmerch1"
special_merchants_end = "trp_town_1_tavernkeeper"

tavernkeepers_begin = "trp_town_1_tavernkeeper"
tavernkeepers_end = "trp_town_1_merchant"

goods_merchants_begin = "trp_town_1_merchant"
goods_merchants_end = "trp_town_1_horse_merchant"

horse_merchants_begin = "trp_town_1_horse_merchant"
horse_merchants_end = "trp_town_1_mayor"

mayors_begin = "trp_town_1_mayor"
mayors_end = "trp_village_1_elder"

village_elders_begin = "trp_village_1_elder"
village_elders_end = "trp_merchants_end"

average_price_factor = 1000
minimum_price_factor = 100
maximum_price_factor = 10000

trade_goods_begin = "itm_spice"
trade_goods_end = "itm_siege_supply"

food_begin = "itm_smoked_fish"
food_end = "itm_siege_supply"

bebidas_begin = "itm_wine"
bebidas_end = "itm_smoked_fish"

reference_books_begin = "itm_book_wound_treatment_reference"
reference_books_end = "itm_relic1"

readable_books_begin = "itm_book_tactics"
readable_books_end = reference_books_begin

books_begin = readable_books_begin
books_end = reference_books_end

horses_begin = "itm_pony_horse"
horses_end = "itm_pilgrim_disguise"

weapons_begin = "itm_club_stick"
weapons_end = "itm_cheap_buckler"

ranged_weapons_begin = "itm_darts"
ranged_weapons_end = "itm_torch"

armors_begin = "itm_leather_gloves1"
armors_end = "itm_club_stick"

shields_begin = "itm_cheap_buckler"
shields_end = ranged_weapons_begin

estandartes_begin = "itm_wessexbanner1"
estandartes_end = "itm_cheap_buckler"

banner_meshes_begin = "mesh_banner_a01"
banner_meshes_end_minus_one = "mesh_banner_k21"

arms_meshes_begin = "mesh_arms_a01"
# arms_meshes_end_minus_one = "mesh_arms_k21"

custom_banner_charges_begin = "mesh_custom_banner_charge_01"
custom_banner_charges_end = "mesh_tableau_mesh_custom_banner"

custom_banner_backgrounds_begin = "mesh_custom_banner_bg"
custom_banner_backgrounds_end = custom_banner_charges_begin

custom_banner_flag_types_begin = "mesh_custom_banner_01"
custom_banner_flag_types_end = custom_banner_backgrounds_begin

custom_banner_flag_map_types_begin = "mesh_custom_map_banner_01"
custom_banner_flag_map_types_end = custom_banner_flag_types_begin

custom_banner_map_icons_begin = "icon_custom_banner_01"
# custom_banner_map_icons_end = "icon_banner_01"

banner_map_icons_begin = "icon_banner_01"
banner_map_icons_end_minus_one = "icon_banner_198"

banner_scene_props_begin = "spr_banner_a"
banner_scene_props_end_minus_one = "spr_banner_k21"

companion_banner_begin = "spr_banner_a"

# Some constants for merchant inventories
merchant_inventory_space = 30
num_merchandise_goods = 40

num_forest_bandit_spawn_points = 4
num_mountain_bandit_spawn_points = 6
num_steppe_bandit_spawn_points = 1
num_taiga_bandit_spawn_points = 1
num_desert_bandit_spawn_points = 1
num_sea_raider_spawn_points = 3
num_new_sp = 4
num_sea_pirate_spawn_points = 3

# battle tactics
btactic_hold = 1
btactic_follow_leader = 2
# btactic_charge = 3
# btactic_stand_ground = 4

# default right mouse menu orders
cmenu_move = -7
cmenu_follow = -6

# "$g_mt_mode"
# Town center modes - resets in game menus during the options
tcm_default = 0
tcm_disguised = 1
# tcm_prison_break 	= 2
tcm_escape = 3

# Arena battle modes
abm_training = 1
abm_visit = 2
abm_tournament = 3

# Camp training modes
ctm_melee = 1
ctm_ranged = 2
ctm_mounted = 3

# For $g_dplmc_terrain_advantage
# DPLMC_TERRAIN_ADVANTAGE_DISABLE     =  -1
DPLMC_TERRAIN_ADVANTAGE_ENABLE = 0  # So I don't have to keep track of whether it is enabled or disabled by default
# For $g_dplmc_ai_changes
# DPLMC_AI_CHANGES_DISABLE        =  -1
# DPLMC_AI_CHANGES_LOW            =   0
# DPLMC_AI_CHANGES_MEDIUM         =   1
# DPLMC_AI_CHANGES_HIGH           =   2
# Low:
#  - Center points for fief allocation are calculated (villages 1 / castles 2 / towns 3)
#    instead of (villages 1 / castles 1 / towns 2).
#  - For qst_rescue_prisoner and qst_offer_gift, the relatives that can be a target of the
#    quest have been extended to include uncles and aunts and in-laws.
#  - Alterations to script_calculate_troop_score_for_center (these changes currently are
#    only relevant during claimant quests).
#  - When picking a new faction, lords are more likely to return to their original faction
#    (except when that's the faction they're being exiled from), if the ordinary conditions
#    for rejoining are met.  A lord's decision may also be influenced by his relations with
#    other lords in the various factions, instead of just his relations with the faction
#    leaders.
# Medium:
#  - Some changes for lord relation gains/losses when fiefs are allocated.
#  - Kings overrule lords slightly less frequently on faction issues.
#  - In deciding who to support for a fief, minor parameter changes for certain personalities.
#    Some lords will still give priority to fiefless lords or to the lord who conquered the
#    center if they have a slightly negative relation (normally the cutoff is 0 for all
#    personalities).
#  - When a lord can't find any good candidates for a fief under the normal rules,
#    instead of automatically supporting himself he uses a weighted scoring scheme.
#  - In various places where "average renown * 3/2" appears, an alternate calculation is
#    sometimes used.
# High:
#  - The "renown factor" when an NPC lord or the player courts and NPC lady is adjusted by
#    the prestige of the lady's guardian.

# For $g_dplmc_gold_changes
# DPLMC_GOLD_CHANGES_DISABLE = -1
DPLMC_GOLD_CHANGES_LOW = 0
# DPLMC_GOLD_CHANGES_MEDIUM  =  1
# DPLMC_GOLD_CHANGES_HIGH    =  2
#
# Mercantilism
# - Your caravans generate more revenue for your towns, but your benefit
#   from the caravans of other kingdoms is diminished.
# - Trade within the kingdom is made more efficient, while imports are
#   discouraged.
#
# Low:
# - Caravan trade benefits both the source and the destination
# - When the player surrenders, there is a chance his personal equipment
#   will not be looted, based on who accepted the surrender and the difficulty
#   setting.  (This is meant to address a gameplay issue.  In the first 700
#   days or so, there is no possible benefit to surrendering rather than
#   fighting to the last man.)  Also, a bug that made it possible for
#   books etc. to be looted was corrected.
# - AI caravans take into consideration distance when choosing their next
#   destination and will be slightly more like to visit their own faction.
#   This strategy is mixed with the Native one, so the trade pattern will
#   differ but not wildly.
# - Scale town merchant gold by prosperity (up to a maximum 40% change).
# - Food prices increase in towns that have been under siege for at least
#   48 hours.
# - In towns the trade penalty script has been tweaked to make it more
#   efficient to sell goods to merchants specializing in them.
#
# Medium:
# - Food consumption increases in towns as prosperity increases.
#   Consumption also increases with garrison sizes.
# - Lords' looting skill affects how much gold they take from the player
#   when they defeat him.
# - Lords' leadership skill modifies their troop wage costs the same way
#   it does for the player.
# - The player can lose gold when his fiefs are looted, like lords.
# - The same way that lord party sizes increase as the player progresses,
#   mercenary party sizes also increase to maintain their relevance.
#   (The rate is the same as for lords: a 1.25% increase per level.)
# - If the player has a kingdom of his own, his spouse will receive
#   part of the bonus that ordinarily would be due a liege.  The extent
#   of this bonus depends on the number of fiefs the players holds.
#   This bonus is non-cumulative with the marshall bonus.
# - Attrition is inflicted on NPC-owned centers if they can't pay wages,
#   but only above a certain threshold.
# - Strangers cannot acquire enterprises (enforced at 1 instead of at 0,
#   so you have to do something).
#
# High:
# - The total amount of weekly bonus gold awarded to kings in Calradia
#   remains constant: as kings go into exile, their bonuses are divided
#   among the remaining kings.
# - If lord's run a personal gold surplus after party wages, the extra is
#   divided among the lord and his garrisons budgets (each castle and town
#   has its own pool of funds to pay for soldiers) on the basis of whether
#   the lord is low on gold or any of his fortresses are.  (If none are low
#   on gold, the lord takes everything, like before.)
# - The honor loss from an offense depends in part on the player's honor
#   at the time.  The purer the reputation, the greater the effect of a single
#   disagrace.
# - Raiding change: village gold lost is removed from uncollected taxes before
#   the balance (if any) is removed from the lord.
# - Csah for prisoners

# For relatives: a standard way of generating IDs for "relatives" that are not
# implemented in the game as troops, but nevertheless should be taken into
# account for the purpose of script_troop_get_family_relation_to_troop
DPLMC_VIRTUAL_RELATIVE_MULTIPLIER = -4
DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET = -1  # e.g. father for x = (DPLMC_VIRTUAL_RELATIVE_MULTIPLIER * x) + DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET
# DPLMC_VIRTUAL_RELATIVE_MOTHER_OFFSET = -2
# DPLMC_VIRTUAL_RELATIVE_SPOUSE_OFFSET = -3

# Village bandits attack modes
vba_normal = 1
vba_after_training = 2

arena_tier1_opponents_to_beat = 3
arena_tier1_prize = 15
arena_tier2_opponents_to_beat = 6
arena_tier2_prize = 35
arena_tier3_opponents_to_beat = 10
arena_tier3_prize = 90
arena_tier4_opponents_to_beat = 20
arena_tier4_prize = 250
arena_grand_prize = 700

fire_duration = 4  # fires takes 4 hours

# NORMAL ACHIEVEMENTS
ACHIEVEMENT_NONE_SHALL_PASS = 1,
# ACHIEVEMENT_MAN_EATER = 2,
# ACHIEVEMENT_THE_HOLY_HAND_GRENADE = 3,
ACHIEVEMENT_LOOK_AT_THE_BONES = 4,
# ACHIEVEMENT_KHAAAN = 5,
ACHIEVEMENT_GET_UP_STAND_UP = 6,
ACHIEVEMENT_BARON_GOT_BACK = 7,
ACHIEVEMENT_BEST_SERVED_COLD = 8,
# ACHIEVEMENT_TRICK_SHOT = 9,
# ACHIEVEMENT_GAMBIT = 10,
# ACHIEVEMENT_OLD_SCHOOL_SNIPER = 11,
# ACHIEVEMENT_CALRADIAN_ARMY_KNIFE = 12,
ACHIEVEMENT_MOUNTAIN_BLADE = 13,
# ACHIEVEMENT_HOLY_DIVER = 14,
# ACHIEVEMENT_FORCE_OF_NATURE = 15,

# SKILL RELATED ACHIEVEMENTS:
# ACHIEVEMENT_BRING_OUT_YOUR_DEAD = 16,
# ACHIEVEMENT_MIGHT_MAKES_RIGHT = 17,
# ACHIEVEMENT_COMMUNITY_SERVICE = 18,
# ACHIEVEMENT_AGILE_WARRIOR = 19,
# ACHIEVEMENT_MELEE_MASTER = 20,
# ACHIEVEMENT_DEXTEROUS_DASTARD = 21,
# ACHIEVEMENT_MIND_ON_THE_MONEY = 22,
# ACHIEVEMENT_ART_OF_WAR = 23,
# ACHIEVEMENT_THE_RANGER = 24,
# ACHIEVEMENT_TROJAN_BUNNY_MAKER = 25,

# MAP RELATED ACHIEVEMENTS:
ACHIEVEMENT_MIGRATING_COCONUTS = 26,
ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED = 27,
ACHIEVEMENT_SARRANIDIAN_NIGHTS = 28,
ACHIEVEMENT_OLD_DIRTY_SCOUNDREL = 29,
ACHIEVEMENT_THE_BANDIT = 30,
ACHIEVEMENT_GOT_MILK = 31,
# ACHIEVEMENT_SOLD_INTO_SLAVERY = 32,
ACHIEVEMENT_MEDIEVAL_TIMES = 33,
ACHIEVEMENT_GOOD_SAMARITAN = 34,
# ACHIEVEMENT_MORALE_LEADER = 35,
ACHIEVEMENT_ABUNDANT_FEAST = 36,
ACHIEVEMENT_BOOK_WORM = 37,
ACHIEVEMENT_ROMANTIC_WARRIOR = 38,

# POLITICALLY ORIENTED ACHIEVEMENTS:
ACHIEVEMENT_HAPPILY_EVER_AFTER = 39,
ACHIEVEMENT_HEART_BREAKER = 40,
ACHIEVEMENT_AUTONOMOUS_COLLECTIVE = 41,
ACHIEVEMENT_I_DUB_THEE = 42,
ACHIEVEMENT_SASSY = 43,
ACHIEVEMENT_THE_GOLDEN_THRONE = 44,
ACHIEVEMENT_KNIGHTS_OF_THE_ROUND = 45,
ACHIEVEMENT_TALKING_HELPS = 46,
ACHIEVEMENT_KINGMAKER = 47,
ACHIEVEMENT_PUGNACIOUS_D = 48,
# ACHIEVEMENT_GOLD_FARMER = 49,
ACHIEVEMENT_ROYALITY_PAYMENT = 50,
ACHIEVEMENT_MEDIEVAL_EMLAK = 51,
ACHIEVEMENT_CALRADIAN_TEA_PARTY = 52,
ACHIEVEMENT_MANIFEST_DESTINY = 53,
ACHIEVEMENT_CONCILIO_CALRADI = 54,
ACHIEVEMENT_VICTUM_SEQUENS = 55,

# MULTIPLAYER ACHIEVEMENTS:
ACHIEVEMENT_THIS_IS_OUR_LAND = 56,
ACHIEVEMENT_SPOIL_THE_CHARGE = 57,
ACHIEVEMENT_HARASSING_HORSEMAN = 58,
ACHIEVEMENT_THROWING_STAR = 59,
ACHIEVEMENT_SHISH_KEBAB = 60,
ACHIEVEMENT_RUIN_THE_RAID = 61,
ACHIEVEMENT_LAST_MAN_STANDING = 62,
ACHIEVEMENT_EVERY_BREATH_YOU_TAKE = 63,
ACHIEVEMENT_CHOPPY_CHOP_CHOP = 64,
ACHIEVEMENT_MACE_IN_YER_FACE = 65,
ACHIEVEMENT_THE_HUSCARL = 66,
ACHIEVEMENT_GLORIOUS_MOTHER_FACTION = 67,
ACHIEVEMENT_ELITE_WARRIOR = 68,

# COMBINED ACHIEVEMENTS
# ACHIEVEMENT_SON_OF_ODIN = 69,
# ACHIEVEMENT_KING_ARTHUR = 70,
# ACHIEVEMENT_KASSAI_MASTER = 71,
# ACHIEVEMENT_IRON_BEAR = 72,
# ACHIEVEMENT_LEGENDARY_RASTAM = 73,
# ACHIEVEMENT_SVAROG_THE_MIGHTY = 74,

ACHIEVEMENT_MAN_HANDLER = 75,  # F123 - 1.41 -> Submod (gdwnochangethough?
ACHIEVEMENT_GIRL_POWER = 76,
ACHIEVEMENT_QUEEN = 77,
ACHIEVEMENT_EMPRESS = 78,
ACHIEVEMENT_TALK_OF_THE_TOWN = 79,
ACHIEVEMENT_LADY_OF_THE_LAKE = 80,

# COOP  chief CONSTANTS ########################################################################
coop_temp_party_enemy_heroes = "p_temp_casualties_2"
coop_temp_party_ally_heroes = "p_temp_casualties_3"

coop_temp_party_enemy_begin = 20  # = zendar
coop_temp_casualties_enemy_begin = coop_temp_party_enemy_begin + 40  # 4x this number = 160 total temp parties reserved in MP
coop_temp_party_ally_begin = coop_temp_casualties_enemy_begin + 40
coop_temp_casualties_ally_begin = coop_temp_party_ally_begin + 40

# round for siege battles
coop_round_battle = 1
coop_round_stop_reinforcing_wall = 2
coop_round_town_street = 3
coop_round_stop_reinforcing_street = 4
coop_round_castle_hall = 5

# type of mission
coop_battle_type_field_battle = 1
coop_battle_type_siege_player_attack = 2
coop_battle_type_siege_player_defend = 3
coop_battle_type_village_player_attack = 4
coop_battle_type_village_player_defend = 5
coop_battle_type_bandit_lair = 6

coop_battle_state_none = 0
coop_battle_state_setup_sp = 1
coop_battle_state_setup_mp = 2
coop_battle_state_started = 3
coop_battle_state_end_mp = 4
# coop_battle_state_end_sp               = 5




# multiplayer message subtypes
# multiplayer_event_coop_send_to_server
coop_event_start_map = 1
coop_event_battle_size = 2
coop_event_spawn_formation = 3
coop_event_skip_admin_panel = 4
coop_event_player_open_inventory_before_spawn = 5
coop_event_player_get_selected_item_types = 6
coop_event_player_ask_for_selected_item = 7
coop_event_player_remove_selected_item = 8
coop_event_setup_battle = 9
coop_event_start_battle = 10
coop_event_open_admin_panel = 11
coop_event_open_game_rules = 12
coop_event_end_battle = 13
coop_event_disable_inventory = 14
coop_event_reduce_damage = 15

# multiplayer_event_coop_send_to_player
coop_event_store_hero_troops = 20
coop_event_round = 21
coop_event_troop_banner = 22
coop_event_troop_raise_attribute = 23
coop_event_troop_raise_skill = 24
coop_event_troop_raise_proficiency_linear = 25
coop_event_troop_set_slot = 26
coop_event_player_set_slot = 27
coop_event_send_inventory = 28
coop_event_prsnt_coop_item_select = 29
coop_event_inv_troop_set_slot = 30
coop_event_set_scene_1 = 31
coop_event_set_scene_2 = 32
coop_event_set_scene_3 = 33
coop_event_set_scene_4 = 34
coop_event_set_scene_5 = 35
coop_event_return_team_faction = 36
coop_event_return_spawn_formation = 37
coop_event_return_battle_size = 38
coop_event_return_game_type = 39
coop_event_return_castle_party = 40
coop_event_return_battle_scene = 41
coop_event_return_skip_menu = 42
coop_event_return_open_game_rules = 43
coop_event_receive_next_string = 44
coop_event_return_num_reserves = 45
coop_event_return_battle_state = 46
coop_event_result_saved = 47
coop_event_return_disable_inventory = 48
coop_event_return_reduce_damage = 49
############################################################### COOP acaba chief

# motomataru chief IA Improved
# AI variables
AI_long_range = 8000  # do not put over 130m if you want archers to always fire
AI_firing_distance = AI_long_range / 2
AI_charge_distance = 2000
AI_for_kingdoms_only = 0
# Percentage_Cav_For_New_Dest	= 40
Hold_Point = 100  # archer hold if outnumbered
Advance_More_Point = 100 - Hold_Point * 100 / (Hold_Point + 100)  # advance 'cause expect other side is holding
AI_Max_Reinforcements = 1000000  # maximum number of reinforcement stages in a battle
AI_Replace_Dead_Player = 1
AI_Poor_Troop_Level = 24  # average level of troops under      which a division may lose discipline    MOTO chief
# AI_Max_Size_Oblong_Formations    = 48    #size above which AI will      make a (more maneuverable) square (typical Roman lines 40 w x 7.5      d; here 16 w x 3 d)

# Battle Phases
BP_Setup = 1
BP_Jockey = 2
BP_Fight = 3

# positions used in a script, named for convenience
Nearest_Enemy_Troop_Pos = 48  # pos48	used only by infantry AI
Nearest_Enemy_Battlegroup_Pos = 50  # pos50	used only by ranged AI
Nearest_Threat_Pos = Nearest_Enemy_Troop_Pos  # used only by cavalry AI
Nearest_Target_Pos = Nearest_Enemy_Battlegroup_Pos  # used only by cavalry AI
Infantry_Pos = 51  # pos51
Archers_Pos = 53  # pos53
Cavalry_Pos = 54  # pos54
Team_Starting_Point = 55  # pos55

# positions used through battle
Team0_Cavalry_Destination = 56  # pos56
Team1_Cavalry_Destination = 57  # pos57
Team2_Cavalry_Destination = 58  # pos58
Team3_Cavalry_Destination = 59  # pos59
# Ia improved chief acaba motomataru

# para negativos equipamiento chief habilidades
desnudos_begin = "itm_war_paintbody_two"
desnudos_end = "itm_celtcloakedbody01"
armadura_pesada_begin = "itm_noblearmor3res"
armadura_pesada_end = "itm_noblemanshirt1"
armadura_pesada2_begin = "itm_longmail_coat_king2"
armadura_pesada2_end = "itm_mail_goatist"
armadura_pesada3_begin = "itm_mail_goatist"
armadura_pesada3_end = "itm_lamellaraqua"  # Shifted this up from cuir_bouilli so viking lamellars were no longer in heavy. TML. F123 - Submod -> 1.41 (All item changes)
armadura_pesada4_begin = "itm_mail_goatist"  # Changed this from cuir_bouilli because otherwise it was generating a nonsense check of is_between big number through small number. Does that hurt anything? Probably not, but it didn't do anything either. The whole code for these requiring 4 variables when they're all in one long list confuses me, but I didn't want to mess with it too much. TML
armadura_pesada4_end = "itm_lamellaraqua"
armadura_media_begin = "itm_lamellaraqua"  # This was actually already set to this, #which is what made me think they may have been intended to be medium. TML
armadura_media_end = "itm_mailcuir_bouilli"
armadura_media2_begin = "itm_mailcuir_bouilli"  # I notice that these are actually heavy armor #ingame because the heavy list overwrites it just like it did for viking armor #before, but didn't feel the need to change it. TML
# gdw acceptedTML-all thought don't understand #calc. Leave Byrnies in heavy as are very heavy mail for torso. Lamellar works as #med.reduceheavy penalty,add lammel to merchan

armadura_media2_end = "itm_jack_armorpaddedyelo"
yelmos_pesados_begin = "itm_helm_leathert2"
yelmos_pesados_end = "itm_helmet_stripedt3"
yelmos_pesados2_begin = "itm_helmet_stripedt3"
yelmos_pesados2_end = "itm_noheadhelm"
calzado_pesados_begin = "itm_greaves1"
calzado_pesados_end = "itm_cavalry_greaves"
escudos_pesados_begin = "itm_gaelic_shielda"
escudos_pesados_end = "itm_shield_roundengle1"
escudos_pesados2_begin = "itm_shield_roundengle1"
escudos_pesados2_end = "itm_banner_reinforced_shield"
burro_begin = "itm_donkey_horse1"
burro_end = "itm_pilgrim_disguise"
coronas_begin = "itm_crown_lombardy"
coronas_end = "itm_leathercap1"
mercaderes_begin = "itm_richlong_tunic1"
mercaderes_end = "itm_leather_aprontunic"
# nobleclothes1_begin = "itm_noblemanshirt1"
# nobleclothes1_end = "itm_noblemanshirt4"#it doesn't include this last itemgdw
nobleclothes1_begin = "itm_noblemanshirt3"
nobleclothes1_end = "itm_mailtunic_blkcheap"  # it doesn't include this last itemgdw
nobleclothes2_begin = "itm_noblearmor1res"
nobleclothes2_end = "itm_noblemanshirt3"
# specials_begin = "military_cleaver_b"
# specials_end = "itm_sarranid_boots_b"

# caba'drin order skirmish chief
skirmish_min_distance = 1500  # Min distance you wish maintained, in cm. Where agent will retreat
skirmish_max_distance = 2500  # Max distance to maintain, in cm. Where agent will stop retreating

key_for_skirmish = key_f7
# chief skirmish order acaba

# COLORS
color_good_news = 0xCCFFCC
color_terrible_news = 0xFFCCCC
color_bad_news = 0xff3333
# color_neutral_news = 0xFFFFFF
color_quest_and_faction_news = 0xCCCCFF
color_hero_news = 0xFFFF99

#  Percent modifier of days between prisoner escapes (bigger number = less likely escapes)
prisoners_escape_chance_modifier = 50

# dungeon chief
dungeon_prisoners_begin = "trp_refugeeromanruins"
dungeon_prisoners_end = "trp_refugeedruid"
stone_refugee_begin = "trp_refugeedruid"
stone_refugee_end = "trp_prisonerdruid"

rumor_found_chance = 70

# these are only changed to `trp_global_values`
# todo: why aren't these global variables?
slot_gloval_show_fire_arrow_particle = 1
slot_gloval_fire_arrow_key = 2
slot_gloval_max_fire_arrow = 3
slot_gloval_max_flame_slot = 4

additional_heroes_begin = "trp_hero1"
additional_heroes_end = "trp_town_1_seneschal"

freelancer_can_use_item = "script_dplmc_troop_can_use_item"

mount_patrol_max_speed = 15
mount_patrol_min_speed = 5
mount_patrol_closing_dist = 6000

# Health regeneration
# Rates listed below are per kill, not based on duration.  They are also % of health, not exact values.
wp_hr_player_rate = 1
wp_hr_strength_factor = 4  # This is the value STR is divided by.  So 4 = .25% per point of Strength.
wp_hr_leadership_factor = 2  # This is the value Leadership is divided by.  Only non-heroes gain this.
wp_hr_lord_rate = 20
wp_hr_companion_rate = 2
wp_hr_king_rate = 30
wp_hr_common_rate = 5
# wp_hr_elite_rate                   = 15  # Currently unused.
wp_hr_factor_difficulty = 1  # This turns ON (1) or OFF (0) any code changes based on difficulty.
wp_hr_diff_enemy_bonus = 4  # Amount the health regeneration of enemies is boosted by per difficulty rank.
wp_hr_diff_ally_penalty = -3  # Amount the health regeneration of allies is reduced by per difficulty rank.
wp_hr_debug = 0  # This turns ON (1) or OFF (0) all of the debug messages.
