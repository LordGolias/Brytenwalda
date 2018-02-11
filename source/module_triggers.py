from .header_operations import *
from .header_common import *

from .header_triggers import ti_once, key_left_mouse_button
from .header_parties import ai_bhvr_attack_party, ai_bhvr_travel_to_party, \
    pf_default_behavior, ai_bhvr_escort_party, ai_bhvr_hold

from .module_constants import *

from . import companions, caravans, constable

####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################


triggers = [
(0.1, 0, ti_once, [(map_free,0)], [(dialog_box,"str_tutorial_map1")]),

(5.0, 0, 20.0,
[
   (store_time_of_day, ":cur_hour"),
   (this_or_next|ge, ":cur_hour", 20),
     (le, ":cur_hour", 1),
  ],
  [
    (call_script, "script_find_neighbors"),
    (call_script, "script_randomly_start_war_peace_new"),

    (try_for_range, ":faction_1", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":faction_1", "slot_faction_state", sfs_active),

      (try_for_range, ":faction_2", ":faction_1", kingdoms_end),
        (faction_slot_eq, ":faction_2", "slot_faction_state", sfs_active),
        (lt, ":faction_1", ":faction_2"),

        # update truce days
        (store_add, ":slot_truce_days", ":faction_2", "slot_faction_truce_days_with_factions_begin"),
        (val_sub, ":slot_truce_days", kingdoms_begin),
        (faction_get_slot, ":truce_days", ":faction_1", ":slot_truce_days"),
        (try_begin),
          (ge, ":truce_days", 1),
          (val_sub, ":truce_days", 1),
          (faction_set_slot, ":faction_1", ":slot_truce_days", ":truce_days"),
        (try_end),

        # update provocations
        (store_add, ":slot_provocation_days", ":faction_2", "slot_faction_provocation_days_with_factions_begin"),
        (val_sub, ":slot_provocation_days", kingdoms_begin),
        (faction_get_slot, ":provocation_days", ":faction_1", ":slot_provocation_days"),
        (try_begin),
          (ge, ":provocation_days", 1),
          (val_sub, ":provocation_days", 1),
          (try_begin),
            # factions already at war
            # todo: put provocation to 0 when factions declares war.
            (store_relation, ":relation", ":faction_1", ":faction_2"),
            (lt, ":relation", 0),
            (assign, ":provocation_days", 0),
          (try_end),
          (faction_set_slot, ":faction_1", ":slot_provocation_days", ":provocation_days"),
        (try_end),

        # update war dammage
        (try_begin),
          (store_relation, ":relation", ":faction_1", ":faction_2"),
          (lt, ":relation", 0),
          (store_add, ":slot_war_damage", ":faction_2", "slot_faction_war_damage_inflicted_on_factions_begin"),
          (val_sub, ":slot_war_damage", kingdoms_begin),
          (faction_get_slot, ":war_damage", ":faction_1", ":slot_war_damage"),
          (val_add, ":war_damage", 1),
          (faction_set_slot, ":faction_1", ":slot_war_damage", ":war_damage"),
        (try_end),

      (try_end), # try_for_range, ":faction_2"

      (call_script, "script_update_faction_notes", ":faction_1"),
    (try_end), # try_for_range, ":faction_1"
  ]),

#  (1.0, 0, ti_once, [(map_free,0)], [(start_map_conversation, "trp_guide1", -1)]),
#(0.1, 0.5, 0, [(map_free,0),(eq,"$g_move_fast", 1)], [((assign, "$g_move_slow", 1),)]),
##cc chief
  (4, 0, 1, [(map_free),], 
    [
      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
        (store_faction_of_party, ":center_faction", ":center_no"),
        (store_relation, ":cur_relation", "fac_player_supporters_faction", ":center_faction"),
        (lt, ":cur_relation",-1),
        (store_distance_to_party_from_party, ":dist", "p_main_party", ":center_no"),
        (assign, ":center_no", reg2),
        (lt, ":dist", 5),
        (display_message, "@You are near to the enemy's realm, and stop to hide from what you think is an enemy patrol", 0xff3333),
        #(rest_for_hours, 1, 1, 0),
        (assign, "$g_move_slow", 1),
        (try_begin),
          (gt, "$cheat_mode", 0),
          (display_message, "@{!}DEBUG -- slowing in enemy territory at {reg2}"),
        (try_end),
      (try_end),
    ]),
## From floris see scripts
#  (0.1, 0.5, 0, [(map_free,0),(eq,"$g_move_fast", 1)], [(assign,"$g_move_fast", 0)]),

#############
#TEMPERED  chief skirmisher TRIGGER
	
  (0.0,2,0,
	[		(party_is_active,"$skirmish_party_no"),
			(party_is_in_any_town,"$skirmish_party_no"),			

	],
	[		(party_set_ai_behavior, "$skirmish_party_no", ai_bhvr_attack_party),
			(party_set_ai_object,"$skirmish_party_no","p_main_party"),
	]),
###TEMPERED chief Patron saint of peasants 
##  (120,0,12,
##	[		(ge,"$commoner_trust",100),			
##			(eq, "$players_kingdom", "fac_player_supporters_faction"),
##			(faction_slot_eq, "fac_player_supporters_faction", "slot_faction_state", sfs_active),
##	],
##	[	
##		(assign, ":closest_dist", 100000),
##		(try_for_range,":cur_village", villages_begin, villages_end),
##			(store_distance_to_party_from_party, ":dist", ":cur_village", "p_main_party"),
##			(store_faction_of_party, ":cur_village_faction", ":cur_village"),
##			(neq,":cur_village_faction","fac_player_supporters_faction"),
##			(lt, ":dist", ":closest_dist"),
##			(assign, ":closest_dist", ":dist"),
##			(assign,":rebel_village",":cur_village"),
##		(try_end),
##		(call_script,"script_give_center_to_lord",":rebel_village","trp_player",0),
##		(display_message,"@ A village has rebeled against their lord and now supports your cause."),			
##	]),
###TEMEPRED chief PEASANT REVOLT puesto off chief por si es el problema de aldeas sin asignacion	
##  (120,0,12,
##	[		(lt,"$commoner_trust",-70),			
##			(gt, "$players_kingdom",0),
##
##
##	],
##	[	
##		(store_random_in_range,":revolt_chance","$commoner_trust",20),
##		(try_for_range,":player_village", villages_begin, villages_end),
##			(store_faction_of_party, ":cur_village_faction", ":player_village"),
##			(eq,":cur_village_faction","$players_kingdom"),
##			(assign,":rebel_village",":player_village"),
##		(try_end),
##		(gt,":rebel_village",0),
##		(lt,":revolt_chance",0),
##		(party_set_faction, ":rebel_village", "fac_peasant_rebels"),
##		(party_set_slot, ":rebel_village", "slot_town_lord", stl_unassigned),
##		(display_message,"@ A village has rebeled against your rule."),			
##	]),
	
#Tempered chief dialog trigger trusted friend of peasants
	
  (3,1,ti_once,
	[		(map_free),			
			(gt,"$commoner_trust",40),
	],
	[	
		(dialog_box,"str_peasant_trusted_friend"),
	]),
	
#Tempered  chief dialog trigger patron saint of peasants
	
  (3,1,ti_once,
	[		(map_free),			
			(ge,"$commoner_trust",100),
	],
	[	
		(dialog_box,"str_peasant_patron_saint"),
	]),
#tempered chief acaba

#Captivity:

#  (1.0, 0, 0.0, [],
#   [
#       (ge,"$captivity_mode",1),
#       (store_current_hours,reg(1)),
#       (val_sub,reg(1),"$captivity_end_time"),
#       (ge,reg(1),0),
#       (display_message,"str_nobleman_reached_destination"),
#       (jump_to_menu,"$captivity_end_menu"),
#    ]),


  (5.7, 0, 0.0, 
  [
    (store_num_parties_of_template, reg2, "pt_manhunters"),    
    (lt, reg2, 4)
  ],
  [
    (set_spawn_radius, 1),
    (store_add, ":p_town_22_plus_one", "p_town_42", 1), #chief cambia, en Brytenwalda hay 42 ciudades
    (store_random_in_range, ":selected_town", "p_town_1", ":p_town_22_plus_one"),
    (spawn_around_party, ":selected_town", "pt_manhunters"),
  ]),



  (1.0, 0.0, 0.0, [
  (check_quest_active, "qst_track_down_bandits"),
  (neg|check_quest_failed, "qst_track_down_bandits"),
  (neg|check_quest_succeeded, "qst_track_down_bandits"),
  
  ],
   [
    (quest_get_slot, ":bandit_party", "qst_track_down_bandits", "slot_quest_target_party"),
	(try_begin),
		(party_is_active, ":bandit_party"),
		(store_faction_of_party, ":bandit_party_faction", ":bandit_party"),
		(neg|is_between, ":bandit_party_faction", kingdoms_begin, kingdoms_end), #ie, the party has not respawned as a non-bandit
		
		
		(assign, ":spot_range", 8),
		(try_begin),
			(is_currently_night),
			(assign, ":spot_range", 5),
		(try_end),
		
		(try_for_parties, ":party"),
			(gt, ":party", "p_spawn_points_end"),
			
			(store_faction_of_party, ":faction", ":party"),
			(is_between, ":faction", kingdoms_begin, kingdoms_end),
			
			
			(store_distance_to_party_from_party, ":distance", ":party", ":bandit_party"),
			(lt, ":distance", ":spot_range"),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_party_name, s4, ":party"),
				(display_message, "@{!}DEBUG -- Wanted bandits spotted by {s4}"),
			(try_end),
			
			(call_script, "script_get_closest_center", ":bandit_party"),
			(assign, ":nearest_center", reg0),
#			(try_begin),
#				(get_party_ai_current_behavior, ":behavior", ":party"),
#				(eq, ":behavior", ai_bhvr_attack_party),
#				(call_script, "script_add_log_entry",  logent_party_chases_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
#				(eq, ":behavior", ai_bhvr_avoid_party),
#				(call_script, "script_add_log_entry",  logent_party_runs_from_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
			(call_script, "script_add_log_entry",  logent_party_spots_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(try_end),
		(try_end),
	(else_try), #Party not found
		(display_message, "str_bandits_eliminated_by_another"),
        (call_script, "script_abort_quest", "qst_track_down_bandits", 0),
	(try_end),
   ]),


#Tax Collectors
# Prisoner Trains
#  (4.1, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_prisoner_train"),
#                         (assign, "$pin_limit", peak_prisoner_trains),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),
#
#  (4.1, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_prisoner_train"),
#                         (assign, "$pin_limit", peak_prisoner_trains),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_prisoner_train_party"),
               (party_is_in_any_town,reg(2)),
               ],
              [(store_faction_of_party, ":faction_no", reg(2)),
               (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
               (party_set_ai_object,reg(2),reg0),
               (party_set_flags, reg(2), pf_default_behavior, 0),
            ]),

##Caravans
#  (4.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_caravan"),
#                         (assign, "$pin_limit", peak_kingdom_caravans),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

#  (4.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_caravan"),
#                         (assign, "$pin_limit", peak_kingdom_caravans),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

##  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_kingdom_caravan_party"),
##               (party_is_in_any_town,reg(2)),
##               ],
##              [(store_faction_of_party, ":faction_no", reg(2)),
##               (call_script,"script_cf_select_random_town_with_faction", ":faction_no"),
##               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
##               (party_set_ai_object,reg(2),reg0),
##               (party_set_flags, reg(2), pf_default_behavior, 0),
##            ]),

#Messengers
#  (4.2, 0, 0.0, [],
#   [(assign, "$pin_faction", "fac_swadians"),
#    (assign, "$pin_party_template", "pt_briton_messenger"),
#    (assign, "$pin_limit", peak_kingdom_messengers),
#    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#    (party_set_ai_object,"$pout_party","$pout_town"),
#    ]),

#  (4.2, 0, 0.0, [],
#   [(assign, "$pin_faction", "fac_vaegirs"),
#    (assign, "$pin_party_template", "pt_saxon_messenger"),
#    (assign, "$pin_limit", peak_kingdom_caravans),
#    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#    (party_set_ai_object,"$pout_party","$pout_town"),
#    ]),

  (1.5, 0, 0, [(store_random_party_of_template, reg(2), "pt_messenger_party"),
               (party_is_in_any_town,reg(2)),
               ],
   [(store_faction_of_party, ":faction_no", reg(2)),
    (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
    (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
    (party_set_ai_object,reg(2),reg0),
    (party_set_flags, reg(2), pf_default_behavior, 0),
    ]),
  
  

#Deserters

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_briton_deserters"),
#                         (assign, "$pin_limit", 4),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),
  
#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_saxon_deserters"),
#                         (assign, "$pin_limit", 4),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#Kingdom Parties
  (1.0, 0, 0.0, [],
   [(try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":cur_kingdom", "slot_faction_state", sfs_active),
###chief SoT activo
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_forager),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (eq, ":cur_kingdom", fac_kingdom_20),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_scouts),
##      (try_end),
#chief Sot activo acaba
##      (neq, ":cur_kingdom", "fac_player_supporters_faction"),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_forager),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_scout),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_patrol),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_messenger),
##      (try_end),
      (try_begin),
        (store_random_in_range, ":random_no", 0, 100),
        (lt, ":random_no", 10),
        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_kingdom_caravan),
      (try_end),
     (try_begin),                        #SEATRADE chief
        (store_random_in_range, ":random_no", 0, 100),       #Disable these for faster testing
        (lt, ":random_no", 10),                              #Disable these for faster testing 
        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_merchant_caravan),
      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_prisoner_train),
##      (try_end),
    (try_end),
    ]),


#Swadians
###chief SoT parties
##  (0.0, 0.0, ti_once, [], [(assign,"$peak_rheged_foragers",4)]),
##  (0.0, 0.0, ti_once, [], [(assign,"$peak_dalriadan_foragers",4)]),
##  (0.0, 0.0, ti_once, [], [(assign,"$peak_gododdin_foragers",4)]),
##  (0.0, 0.0, ti_once, [], [(assign,"$peak_bernician_foragers",4)]),
##  (0.0, 0.0, ti_once, [], [(assign,"$peak_pictish_foragers",4)]),
##  (0.0, 0.0, ti_once, [], [(assign,"$peak_alcluyd_foragers",4)]),
##  (0.0, 0.0, ti_once, [], [(assign,"$peak_scouts",4)]),
###  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_harassers",3)]),
###  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_war_parties",2)]),
##
##
##  (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_1"),
##                         (assign, "$pin_party_template", "pt_rheged_foragers"),
##                         (assign, "$pin_limit", "$peak_rheged_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##  (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_2"),
##                         (assign, "$pin_party_template", "pt_dalriadan_foragers"),
##                         (assign, "$pin_limit", "$peak_dalriadan_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##  (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_3"),
##                         (assign, "$pin_party_template", "pt_dalriadan_foragers"),
##                         (assign, "$pin_limit", "$peak_dalriadan_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_4"),
##                         (assign, "$pin_party_template", "pt_bernician_foragers"),
##                         (assign, "$pin_limit", "$peak_bernician_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##
##  (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_5"),
##                         (assign, "$pin_party_template", "pt_dalriadan_foragers"),
##                         (assign, "$pin_limit", "$peak_dalriadan_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_6"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_7"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_8"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_9"),
##                         (assign, "$pin_party_template", "pt_bernician_foragers"),
##                         (assign, "$pin_limit", "$peak_bernician_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_10"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_11"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_12"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_13"),
##                         (assign, "$pin_party_template", "pt_bernician_foragers"),
##                         (assign, "$pin_limit", "$peak_bernician_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_14"),
##                         (assign, "$pin_party_template", "pt_bernician_foragers"),
##                         (assign, "$pin_limit", "$peak_bernician_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_15"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_16"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##    (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_17"),
##                         (assign, "$pin_party_template", "pt_alcluyd_foragers"),
##                         (assign, "$pin_limit", "$peak_alcluyd_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]), 
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_18"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##    (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_19"),
##                         (assign, "$pin_party_template", "pt_alcluyd_foragers"),
##                         (assign, "$pin_limit", "$peak_alcluyd_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]), 
##    (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_20"),
##                         (assign, "$pin_party_template", "pt_pictish_foragers"),
##                         (assign, "$pin_limit", "$peak_pictish_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_21"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_22"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_23"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_24"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_25"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##   (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_26"),
##                         (assign, "$pin_party_template", "pt_gododdin_foragers"),
##                         (assign, "$pin_limit", "$peak_gododdin_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),
##
##    (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_27"),
##                         (assign, "$pin_party_template", "pt_alcluyd_foragers"),
##                         (assign, "$pin_limit", "$peak_alcluyd_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]), 
##    (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_28"),
##                         (assign, "$pin_party_template", "pt_alcluyd_foragers"),
##                         (assign, "$pin_limit", "$peak_alcluyd_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]), 
##    (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_29"),
##                         (assign, "$pin_party_template", "pt_alcluyd_foragers"),
##                         (assign, "$pin_limit", "$peak_alcluyd_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]), 
##    (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_30"),
##                         (assign, "$pin_party_template", "pt_alcluyd_foragers"),
##                         (assign, "$pin_limit", "$peak_alcluyd_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]), 
##    (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_31"),
##                         (assign, "$pin_party_template", "pt_alcluyd_foragers"),
##                         (assign, "$pin_limit", "$peak_alcluyd_foragers"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]), 
##  (10.2, 0, 0.0, [],
##                     [
##                         (assign, "$pin_faction", "fac_kingdom_20"),
##                         (assign, "$pin_party_template", "pt_scouts"),
##                         (assign, "$pin_limit", "$peak_scouts"),
##                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
##                    ]),

#chief Sot Acaba
  
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_foragers",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_scouts",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_harassers",3)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_war_parties",2)]),


#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_foragers"),
#                         (assign, "$pin_limit", "$peak_swadian_foragers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_scouts"),
#                         (assign, "$pin_limit", "$peak_swadian_scouts"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_patrol"),
#                         (assign, "$pin_limit", "$peak_swadian_harassers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_war_party"),
#                         (assign, "$pin_limit", "$peak_swadian_war_parties"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),
#Vaegirs
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_foragers",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_scouts",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_harassers",3)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_war_parties",2)]),
  

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_foragers"),
#                         (assign, "$pin_limit", "$peak_vaegir_foragers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_scouts"),
#                         (assign, "$pin_limit", "$peak_vaegir_scouts"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_patrol"),
#                         (assign, "$pin_limit", "$peak_vaegir_harassers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_war_party"),
#                         (assign, "$pin_limit", "$peak_vaegir_war_parties"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#Villains etc.
#  (14.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_sea_raiders"),
#                         (assign, "$pin_party_template", "pt_sea_raiders"),
#                         (assign, "$pin_limit", 5),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),


#
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_refugees"),
##                         (assign, "$pin_limit", 5),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),
##
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_farmers"),
##                         (assign, "$pin_limit", 6),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),

#  [1.0, 96.0, ti_once, [], [[assign,"$peak_dark_hunters",3]]],
  
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_dark_hunters"),
##                         (assign, "$pin_limit", "$peak_dark_hunters"),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),

#Companion quests

##  (0, 0, ti_once,
##   [
##       (entering_town,"p_town_1"),
##       (main_party_has_troop,"trp_borcha"),
##       (eq,"$borcha_freed",0)
##    ],
##   
##   [
##       (assign,"$borcha_arrive_sargoth_as_prisoner", 1),
##       (start_map_conversation, "trp_borcha", -1)
##    ]
##   ),
##
##  (1, 0, ti_once,
##   [
##      (map_free,0),
##      (eq,"$borcha_asked_for_freedom",0),
##      (main_party_has_troop,"trp_borcha")
##    ],
##   [
##       (start_map_conversation, "trp_borcha", -1)
##    ]
##   ),
##  
##  (2, 0, ti_once,
##   [
##      (map_free, 0),
##      (neq,"$borcha_asked_for_freedom",0),
##      (eq,"$borcha_freed",0),
##      (main_party_has_troop,"trp_borcha")
##    ],
##   [
##       (start_map_conversation, "trp_borcha", -1),
##    ]
##   ),
########Sistema de heridas chel comienza chief################
         (0.0,
		0,
		24.0,
		[
			(store_current_day,":currentday"),
			(eq,":currentday","$heal_day")
		],
		[
       (call_script, "script_heal_long_term_wounds"),
			# 	(try_begin),
			# 		(eq,"$wound_type",1), #Slight - Cut Arm
			# 		(display_message,"@Your cut arm finally heals."),
			# 		(troop_raise_attribute,"trp_player",ca_strength,1),
			# 	(else_try),
			# 		(eq,"$wound_type",2), #Slight - Cut Torso
			# 		(display_message,"@The cut on your torso finally heals."),
			# 		(troop_raise_attribute,"trp_player",ca_strength,1),
			# 		(troop_raise_attribute,"trp_player",ca_agility,1),
			# 	(else_try),
			# 		(eq,"$wound_type",3), #Slight - Blow to Head
			# 		(display_message,"@Your thoughts clear."),
			# 		(troop_raise_attribute,"trp_player",ca_intelligence,1),
			# 	(else_try),
			# 		(eq,"$wound_type",4), #Slight - Blow to Leg
			# 		(display_message,"@Your leg finally heals."),
			# 		(troop_raise_attribute,"trp_player",ca_agility,1),
			# 	(else_try),
			# 		(eq,"$wound_type",5), #Severe - Broken Arm
			# 		(display_message,"@Your broken arm finally heals."),
			# 		(troop_raise_attribute,"trp_player",ca_strength,3),
			# 		(troop_raise_skill, "trp_player",skl_power_strike,1),
			# 		(troop_raise_skill, "trp_player",skl_power_draw,1),
			# 	(else_try),
			# 		(eq,"$wound_type",6), #Severe - Broken Rib
			# 		(display_message,"@Your broken rib finally heals."),
			# 		(troop_raise_attribute,"trp_player",ca_strength,2),
			# 		(troop_raise_attribute,"trp_player",ca_agility,2),
			# 		(troop_raise_skill, "trp_player",skl_ironflesh,1),
			# 	(else_try),
			# 		(eq,"$wound_type",7), #Severe - Heavy Blow to Head
			# 		(display_message,"@Your headache is finally gone."),
			# 		(troop_raise_attribute,"trp_player",ca_intelligence,2),
			# 		(troop_raise_skill, "trp_player",skl_leadership,1),
			# 		(troop_raise_skill, "trp_player",skl_tactics,1),
			# 	(else_try),
			# 		(eq,"$wound_type",8), #Severe - Broken Leg
			# 		(display_message,"@Your broken leg finally heals."),
			# 		(troop_raise_attribute,"trp_player",ca_agility,3),
			# 		(troop_raise_skill, "trp_player",skl_riding,1),
			# 		(troop_raise_skill, "trp_player",skl_athletics,1),
			# 	(try_end),
			# (assign,"$wound_type",0),
			# (assign,"$heal_day",0)
		]
	),
######sistema de heridas end chief###############

##### TODO: QUESTS COMMENT OUT BEGIN

###########################################################################
### Random Governer Quest triggers
###########################################################################

# Incriminate Loyal Advisor quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_incriminate_loyal_commander"),
       (neg|check_quest_concluded, "qst_incriminate_loyal_commander"),
       (quest_slot_eq, "qst_incriminate_loyal_commander", "slot_quest_current_state", 2),
       (quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", "slot_quest_target_center"),
       (quest_get_slot, ":quest_target_party", "qst_incriminate_loyal_commander", "slot_quest_target_party"),
       (try_begin),
         (neg|party_is_active, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", "slot_quest_current_state", 3),
         (call_script, "script_fail_quest", "qst_incriminate_loyal_commander"),
       (else_try),
         (party_is_in_town, ":quest_target_party", ":quest_target_center"),
         (remove_party, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", "slot_quest_current_state", 3),
         (quest_get_slot, ":quest_object_troop", "qst_incriminate_loyal_commander", "slot_quest_object_troop"),
         (assign, ":num_available_factions", 0),
         (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
           (faction_slot_eq, ":faction_no", "slot_faction_state", sfs_active),
           (neq, ":faction_no", "fac_player_supporters_faction"),
           (neg|quest_slot_eq, "qst_incriminate_loyal_commander", "slot_quest_target_faction", ":faction_no"),
           (val_add, ":num_available_factions", 1),
         (try_end),
         (try_begin),
           (gt, ":num_available_factions", 0),
           (store_random_in_range, ":random_faction", 0, ":num_available_factions"),
           (assign, ":target_faction", -1),
           (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
             (eq, ":target_faction", -1),
             (faction_slot_eq, ":faction_no", "slot_faction_state", sfs_active),
             (neq, ":faction_no", "fac_player_supporters_faction"),
             (neg|quest_slot_eq, "qst_incriminate_loyal_commander", "slot_quest_target_faction", ":faction_no"),
             (val_sub, ":random_faction", 1),
             (lt, ":random_faction", 0),
             (assign, ":target_faction", ":faction_no"),
           (try_end),
         (try_end),
         (try_begin),
           (gt, ":target_faction", 0),
           (call_script, "script_change_troop_faction", ":quest_object_troop", ":target_faction"),
         (else_try),
           (call_script, "script_change_troop_faction", ":quest_object_troop", "fac_robber_knights"),
         (try_end),
         (call_script, "script_succeed_quest", "qst_incriminate_loyal_commander"),
       (try_end),
    ],
   []
   ),
# Runaway Peasants quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_bring_back_runaway_serfs"),
       (neg|check_quest_concluded, "qst_bring_back_runaway_serfs"),
       (quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", "slot_quest_object_center"),
       (quest_get_slot, ":quest_target_center", "qst_bring_back_runaway_serfs", "slot_quest_target_center"),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_1"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_1"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_2"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_2"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_3"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_3"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
         (try_end),
       (try_end),
       (assign, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_returned"),
       (val_add, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_fleed"),
       (ge, ":sum_removed", 3),
       (try_begin),
         (ge, "$qst_bring_back_runaway_serfs_num_parties_returned", 3),
         (call_script, "script_succeed_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (eq, "$qst_bring_back_runaway_serfs_num_parties_returned", 0),
         (call_script, "script_fail_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (call_script, "script_conclude_quest", "qst_bring_back_runaway_serfs"),
       (try_end),
    ],
   []
   ),
### Defend Nobles Against Peasants quest
##  (0.2, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_defend_nobles_against_peasants"),
##       (neg|check_quest_succeeded, "qst_defend_nobles_against_peasants"),
##       (neg|check_quest_failed, "qst_defend_nobles_against_peasants"),
##       (quest_get_slot, ":quest_target_center", "qst_defend_nobles_against_peasants", "slot_quest_target_center"),
##       (assign, ":num_active_parties", 0),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_1", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_1", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_2", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_2", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_3", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_3", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_4", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_4", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_5", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_5", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_6", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_6", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_7", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_7", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_8", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_8", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (eq, ":num_active_parties", 0),
##       (try_begin),
##         (store_div, ":limit", "$qst_defend_nobles_against_peasants_num_nobles_to_save", 2),
##         (ge, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":limit"),
##         (call_script, "script_succeed_quest", "qst_defend_nobles_against_peasants"),
##       (else_try),
##         (call_script, "script_fail_quest", "qst_defend_nobles_against_peasants"),
##       (try_end),
##    ],
##   []
##   ),
### Capture Conspirators quest
##  (0.15, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_capture_conspirators"),
##       (neg|check_quest_succeeded, "qst_capture_conspirators"),
##       (neg|check_quest_failed, "qst_capture_conspirators"),
##       (quest_get_slot, ":quest_target_center", "qst_capture_conspirators", "slot_quest_target_center"),
##       (quest_get_slot, ":faction_no", "qst_capture_conspirators", "slot_quest_target_faction"),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_num_parties_to_spawn", "$qst_capture_conspirators_num_parties_spawned"),
##         (store_random_in_range, ":random_no", 0, 100),
##         (lt, ":random_no", 20),
##         (set_spawn_radius, 3),
##         (spawn_around_party,":quest_target_center","pt_conspirator"),
##         (val_add, "$qst_capture_conspirators_num_parties_spawned", 1),
##         (party_get_num_companions, ":num_companions", reg0),
##         (val_add, "$qst_capture_conspirators_num_troops_to_capture", ":num_companions"),
##         (party_set_ai_behavior, reg0, ai_bhvr_travel_to_party),
##         (party_set_ai_object, reg0, "$qst_capture_conspirators_party_1"),
##         (party_set_flags, reg0, pf_default_behavior, 0),
##         (try_begin),
##           (le, "$qst_capture_conspirators_party_2", 0),
##           (assign, "$qst_capture_conspirators_party_2", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_3", 0),
##           (assign, "$qst_capture_conspirators_party_3", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_4", 0),
##           (assign, "$qst_capture_conspirators_party_4", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_5", 0),
##           (assign, "$qst_capture_conspirators_party_5", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_6", 0),
##           (assign, "$qst_capture_conspirators_party_6", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_7", 0),
##           (assign, "$qst_capture_conspirators_party_7", reg0),
##         (try_end),
##       (try_end),
##
##       (assign, ":num_active_parties", 0),
##
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_1", 0),
##         (party_is_active, "$qst_capture_conspirators_party_1"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_1"),
##           (remove_party, "$qst_capture_conspirators_party_1"),
##         (else_try),
##           (party_get_num_attached_parties, ":num_attachments", "$qst_capture_conspirators_party_1"),
##           (gt, ":num_attachments", 0),
##           (assign, ":leave_meeting", 0),
##           (try_begin),
##             (store_sub, ":required_attachments", "$qst_capture_conspirators_num_parties_to_spawn", 1),
##             (eq, ":num_attachments", ":required_attachments"),
##             (val_add, "$qst_capture_conspirators_leave_meeting_counter", 1),
##             (ge, "$qst_capture_conspirators_leave_meeting_counter", 15),
##             (assign, ":leave_meeting", 1),
##           (try_end),
##           (try_begin),
##             (eq, "$qst_capture_conspirators_num_parties_to_spawn", "$qst_capture_conspirators_num_parties_spawned"),
##             (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_capture_conspirators_party_1"),
##             (assign, ":min_distance", 3),
##             (try_begin),
##               (is_currently_night),
##               (assign, ":min_distance", 2),
##             (try_end),
##             (lt, ":cur_distance", ":min_distance"),
##             (assign, "$qst_capture_conspirators_leave_meeting_counter", 15),
##             (assign, ":leave_meeting", 1),
##           (try_end),
##           (eq, ":leave_meeting", 1),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_1", ai_bhvr_travel_to_point),
##           (party_set_flags, "$qst_capture_conspirators_party_1", pf_default_behavior, 0),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_1"),
##           (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##           (party_set_ai_target_position, "$qst_capture_conspirators_party_1", pos2),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_2", 0),
##             (party_detach, "$qst_capture_conspirators_party_2"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_2", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_3", 0),
##             (party_detach, "$qst_capture_conspirators_party_3"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_3", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_4", 0),
##             (party_detach, "$qst_capture_conspirators_party_4"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_4", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_5", 0),
##             (party_detach, "$qst_capture_conspirators_party_5"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_5", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_6", 0),
##             (party_detach, "$qst_capture_conspirators_party_6"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_6", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_7", 0),
##             (party_detach, "$qst_capture_conspirators_party_7"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_7", pos2),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_1"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_1"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_1"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_1", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_1", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_1", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_1", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_2", 0),
##         (party_is_active, "$qst_capture_conspirators_party_2"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_2"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_2", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_2"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_2"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_hold),
##             (party_attach_to_party, "$qst_capture_conspirators_party_2", "$qst_capture_conspirators_party_1"),
##             (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_2"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_2"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_2"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_2", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_2", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_3", 0),
##         (party_is_active, "$qst_capture_conspirators_party_3"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_3"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_3", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_3"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_3"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_hold),
##             (party_attach_to_party, "$qst_capture_conspirators_party_3", "$qst_capture_conspirators_party_1"),
##             (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_3"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_3"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_3"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_3", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_3", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_4", 0),
##         (party_is_active, "$qst_capture_conspirators_party_4"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_4"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_4", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_4"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_4"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_4", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_4"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_4"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_4"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_4", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_4", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_5", 0),
##         (party_is_active, "$qst_capture_conspirators_party_5"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_5"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_5", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_5"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_5"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_5", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_5"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_5"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_5"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_5", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_5", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_6", 0),
##         (party_is_active, "$qst_capture_conspirators_party_6"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_6"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_6", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_6"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_6"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_6", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_6"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_6"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_6"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_6", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_6", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_7", 0),
##         (party_is_active, "$qst_capture_conspirators_party_7"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_7"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_7", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_7"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_7"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_7", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_7"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_7"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_7"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_7", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_7", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##
##       (eq, ":num_active_parties", 0),
##       (party_count_prisoners_of_type, ":count_captured_conspirators", "p_main_party", "trp_conspirator"),
##       (party_count_prisoners_of_type, ":count_captured_conspirator_leaders", "p_main_party", "trp_conspirator_leader"),
##       (val_add, ":count_captured_conspirators", ":count_captured_conspirator_leaders"),
##       (try_begin),
##         (store_div, ":limit", "$qst_capture_conspirators_num_troops_to_capture", 2),
##         (gt, ":count_captured_conspirators", ":limit"),
##         (call_script, "script_succeed_quest", "qst_capture_conspirators"),
##       (else_try),
##         (call_script, "script_fail_quest", "qst_capture_conspirators"),
##       (try_end),
##    ],
##   []
##   ),
# Follow Spy quest
  (0.5, 0.0, 0.0,
   [
       (check_quest_active, "qst_follow_spy"),
       (eq, "$qst_follow_spy_no_active_parties", 0),
       (quest_get_slot, ":quest_giver_center", "qst_follow_spy", "slot_quest_giver_center"),
       (quest_get_slot, ":quest_object_center", "qst_follow_spy", "slot_quest_object_center"),
       (assign, ":abort_meeting", 0),
       (try_begin),
         (this_or_next|ge, "$qst_follow_spy_run_away", 2),
         (this_or_next|neg|party_is_active, "$qst_follow_spy_spy_party"),
         (neg|party_is_active, "$qst_follow_spy_spy_partners_party"),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 0),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_party"),
         (try_begin),
           (assign, ":min_distance", 3),
           (try_begin),
             (is_currently_night),
             (assign, ":min_distance", 1),
           (try_end),
           (le, ":cur_distance", ":min_distance"),
           (store_distance_to_party_from_party, ":player_distance_to_quest_giver_center", "p_main_party", ":quest_giver_center"),
           (gt, ":player_distance_to_quest_giver_center", 1),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
           (assign, ":abort_meeting", 1),
           (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "$qst_follow_spy_spy_partners_party", "$qst_follow_spy_spy_party"),
           (le, ":cur_distance", 1),
           (party_attach_to_party, "$qst_follow_spy_spy_party", "$qst_follow_spy_spy_partners_party"),
           (assign, "$qst_follow_spy_meeting_state", 1),
           (assign, "$qst_follow_spy_meeting_counter", 0),
         (try_end),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 1),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_partners_party"),
         (try_begin),
           (le, ":cur_distance", 1),
           (party_detach, "$qst_follow_spy_spy_party"),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
           (assign, ":abort_meeting", 1),
           (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (val_add, "$qst_follow_spy_meeting_counter", 1),
           (gt, "$qst_follow_spy_meeting_counter", 4),
           (party_detach, "$qst_follow_spy_spy_party"),
           (assign, ":abort_meeting", 1),
           (assign, "$qst_follow_spy_meeting_state", 2),
         (try_end),
       (try_end),
       (try_begin),
         (eq, ":abort_meeting", 1),
         (party_set_ai_object, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         
         (party_set_ai_object, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         
         (party_set_ai_behavior, "$qst_follow_spy_spy_party", ai_bhvr_travel_to_party),
         (party_set_ai_behavior, "$qst_follow_spy_spy_partners_party", ai_bhvr_travel_to_party),
         (party_set_flags, "$qst_follow_spy_spy_party", pf_default_behavior, 0),
         (party_set_flags, "$qst_follow_spy_spy_partners_party", pf_default_behavior, 0),
       (try_end),
       (assign, ":num_active", 0),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         (remove_party, "$qst_follow_spy_spy_party"),
         (assign, "$qst_follow_spy_spy_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_partners_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         (remove_party, "$qst_follow_spy_spy_partners_party"),
         (assign, "$qst_follow_spy_partner_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (eq, "$qst_follow_spy_partner_back_in_town",1),
         (eq, "$qst_follow_spy_spy_back_in_town",1),
         (call_script, "script_fail_quest", "qst_follow_spy"),
       (try_end),
       (try_begin),
         (eq, ":num_active", 0),
         (assign, "$qst_follow_spy_no_active_parties", 1),
         (party_count_prisoners_of_type, ":num_spies", "p_main_party", "trp_spyenemy"),
         (party_count_prisoners_of_type, ":num_spy_partners", "p_main_party", "trp_spy_partner"),
         (gt, ":num_spies", 0),
         (gt, ":num_spy_partners", 0),
         (call_script, "script_succeed_quest", "qst_follow_spy"),
       (try_end),
    ],
   []
   ),
### Raiders quest
##  (0.95, 0.0, 0.2,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##    ],
##   [
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", "slot_quest_target_party"),
##       (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
##    ]
##   ),
##
##  (0.7, 0, 0.2,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##    ],
##   [
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", "slot_quest_target_party"),
##       (party_set_ai_behavior,":quest_target_party",ai_bhvr_travel_to_party),
##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
##    ]
##   ),
##  
##  (0.1, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", "slot_quest_target_party"),
##       (neg|party_is_active, ":quest_target_party")
##    ],
##   [
##       (call_script, "script_succeed_quest", "qst_hunt_down_raiders"),
##    ]
##   ),
##  
##  (1.3, 0, 0.0,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", "slot_quest_target_party"),
##       (quest_get_slot, ":quest_target_center", "qst_hunt_down_raiders", "slot_quest_target_center"),
##       (party_is_in_town,":quest_target_party",":quest_target_center")
##    ],
##   [
##       (call_script, "script_fail_quest", "qst_hunt_down_raiders"),
##       (display_message, "str_raiders_reached_base"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", "slot_quest_target_party"),
##       (remove_party, ":quest_target_party"),
##    ]
##   ),

##### TODO: QUESTS COMMENT OUT END

#########################################################################
# Random MERCHANT quest triggers
####################################  
 # Apply interest to merchants guild debt  1% per week
  (24.0 * 7, 0.0, 0.0,
   [],
   [
       (val_mul,"$debt_to_merchants_guild",101),
       (val_div,"$debt_to_merchants_guild",100)
    ]
   ),
# Escort merchant caravan:
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
                   (eq, "$escort_merchant_caravan_mode", 1)
                   ],
                  [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", "slot_quest_target_party"),
                   (try_begin),
                     (party_is_active, ":quest_target_party"),
                     (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
                     (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                   (try_end),
                   ]),
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
                    (eq, "$escort_merchant_caravan_mode", 0),
                    ],
                   [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", "slot_quest_target_party"),
                    (try_begin),
                      (party_is_active, ":quest_target_party"),
                      (party_set_ai_behavior, ":quest_target_party", ai_bhvr_escort_party),
                      (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                      (party_set_ai_object, ":quest_target_party", "p_main_party"),
                    (try_end),
                    ]),

  (0.1, 0, 0.0, [(check_quest_active, "qst_escort_merchant_caravan"),
                 (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", "slot_quest_target_party"),
                 (neg|party_is_active,":quest_target_party"),
                 ],
                [(call_script, "script_abort_quest", "qst_escort_merchant_caravan", 2),
                 ]),
  # Escort bishop: SoT chief
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_bishop"),
                   (eq, "$escort_merchant_caravan_mode", 1)
                   ],
                  [(quest_get_slot, ":quest_target_party", "qst_escort_bishop", "slot_quest_target_party"),
                   (try_begin),
                     (party_is_active, ":quest_target_party"),
                     (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
                     (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                   (try_end),
                   ]),
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_bishop"),
                    (eq, "$escort_merchant_caravan_mode", 0),
                    ],
                   [(quest_get_slot, ":quest_target_party", "qst_escort_bishop", "slot_quest_target_party"),
                    (try_begin),
                      (party_is_active, ":quest_target_party"),
                      (party_set_ai_behavior, ":quest_target_party", ai_bhvr_escort_party),
                      (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                      (party_set_ai_object, ":quest_target_party", "p_main_party"),
                    (try_end),
                    ]),

  (0.1, 0, 0.0, [(check_quest_active, "qst_escort_bishop"),
                 (quest_get_slot, ":quest_target_party", "qst_escort_bishop", "slot_quest_target_party"),
                 (neg|party_is_active,":quest_target_party"),
                 ],
                [(call_script, "script_abort_quest", "qst_escort_bishop", 2),
                 ]),

#escoltar obispo acaba chief

# Troublesome bandits
  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_failed, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (eq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(display_message, "str_bandits_eliminated_by_another"),
                   (call_script, "script_abort_quest", "qst_troublesome_bandits", 0),
                   ]),

  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_succeeded, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (neq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(call_script, "script_succeed_quest", "qst_troublesome_bandits"),]),
				  
# Kidnapped girl:
   (1, 0, 0,
   [(check_quest_active, "qst_kidnapped_girl"),
    (quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", "slot_quest_target_party"),
    (party_is_active, ":quest_target_party"),
    (party_is_in_any_town, ":quest_target_party"),
    (remove_party, ":quest_target_party"),
    ],
   []
   ),


#Rebellion changes begin
#move 

  (0, 0, 24 * 14,
   [
        (try_for_range, ":pretender", pretenders_begin, pretenders_end),
          (troop_set_slot, ":pretender", "slot_troop_cur_center", 0),
          (neq, ":pretender", "$supported_pretender"),
          (troop_get_slot, ":target_faction", ":pretender", "slot_troop_original_faction"),
          (faction_slot_eq, ":target_faction", "slot_faction_state", sfs_active),
          (faction_slot_eq, ":target_faction", "slot_faction_has_rebellion_chance", 1),
          (neg|troop_slot_eq, ":pretender", "slot_troop_occupation", slto_kingdom_hero),

          (try_for_range, ":unused", 0, 30),
            (troop_slot_eq, ":pretender", "slot_troop_cur_center", 0),
            (store_random_in_range, ":town", towns_begin, towns_end),
            (store_faction_of_party, ":town_faction", ":town"),
            (store_relation, ":relation", ":town_faction", ":target_faction"),
            (le, ":relation", 0), #fail if nothing qualifies
           
            (troop_set_slot, ":pretender", "slot_troop_cur_center", ":town"),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, 4, ":pretender"),
              (str_store_party_name, 5, ":town"),
              (display_message, "@{!}{s4} is in {s5}"),
            (try_end),
          (try_end),

#        (try_for_range, ":rebel_faction", rebel_factions_begin, rebel_factions_end),
#            (faction_get_slot, ":rebellion_status", ":rebel_faction", "slot_faction_state"),
#            (eq, ":rebellion_status", sfs_inactive_rebellion),
#            (faction_get_slot, ":pretender", ":rebel_faction", "slot_faction_leader"),
#            (faction_get_slot, ":target_faction", ":rebel_faction", "slot_faction_rebellion_target"),#

#            (store_random_in_range, ":town", towns_begin, towns_end),
#            (store_faction_of_party, ":town_faction", ":town"),
#            (store_relation, ":relation", ":town_faction", ":target_faction"),
#            (le, ":relation", 0), #fail if nothing qualifies

 #           (faction_set_slot, ":rebel_faction", "slot_faction_inactive_leader_location", ":town"),
        (try_end), 
       ],
[]
),
#Rebellion changes end

# Lady of the lake achievement
# Lady of the lake achievement
   (1, 0, 0,
   [
     (troop_get_type, ":is_female", "trp_player"),
       (val_mod, ":is_female", 2),    #gender fix chief moto
     (eq, ":is_female", 1),       
     (try_for_range, ":companion", companions_begin, companions_end),
       (troop_slot_eq, ":companion", "slot_troop_occupation", slto_player_companion),

       (troop_get_inventory_capacity, ":inv_cap", ":companion"),
       (try_for_range, ":i_slot", 0, ":inv_cap"),
         (troop_get_inventory_slot, ":item_id", ":companion", ":i_slot"),

		 (ge, ":item_id", 0),

	 	 (this_or_next|eq, ":item_id", "itm_angleswordt2"),
	 	 (this_or_next|eq, ":item_id", "itm_britonswordt2"),
		 (eq, ":item_id", "itm_espada_banditking"),
		 		 
		 (unlock_achievement, ACHIEVEMENT_LADY_OF_THE_LAKE),
		 (assign, ":inv_cap", 0),
	   (try_end),
	 (try_end),
    ],
   []
   ),
#########################################grueso chief final###########################################
#chief freelancer
#+freelancer start

#  CHECKS IF "$enlisted_party" IS DEFEATED

    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
        (gt, "$enlisted_party", 0),
        (neg|party_is_active, "$enlisted_party"),
    ],
    [
        (assign, "$freelancer_state", 0),
        (call_script, "script_freelancer_detach_party"),

        		#to prevent companions from being lost forever
		(call_script, "script_party_restore"), 
		(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":return_troop", "p_main_party", ":cur_stack"),
			(neg|troop_is_hero, ":return_troop"),
			(party_stack_get_size, ":stack_size", "p_main_party", ":cur_stack"),
			(party_remove_members, "p_main_party", ":return_troop", ":stack_size"),
		(try_end),

        #removes faction relation given at enlist
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
            (neq, ":commander_faction", ":cur_faction"),
			(faction_slot_eq, ":cur_faction", "slot_faction_state", sfs_active),
            (call_script, "script_set_player_relation_with_faction", ":cur_faction", 0),
        (try_end),

		(assign, "$g_encountered_party", "$g_enemy_party"),
		(jump_to_menu, "mnu_captivity_start_wilderness"),

    ]),

 #  CHECKS IF "$enlisted_party" HAS JOINED BATTLE

    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
		#collected nearby enemies->detach (post-battle)
		(try_begin), 
			(party_slot_ge, "p_freelancer_party_backup", "slot_party_last_in_combat", 1),
			(map_free),
			(party_set_slot, "p_freelancer_party_backup", "slot_party_last_in_combat", 0),
			(party_get_num_attached_parties, ":num_attached", "p_main_party"),
			(try_for_range_backwards, ":i", 0, ":num_attached"),
				(party_get_attached_party_with_rank, ":party", "p_main_party", ":i"),
				(party_detach, ":party"),
			(try_end),
		(try_end),
		
		#Is currently in battle

        (party_get_battle_opponent, ":commander_enemy", "$enlisted_party"),
        (gt, ":commander_enemy", 0),
        (store_troop_health, ":player_health", "trp_player"),
        #checks that the player's health is high enough to join battle
        (ge, ":player_health", 50),
    ],
    [
        (jump_to_menu, "mnu_world_map_soldier"),
    ]),

#  CHECKS IF PLAYER WON THE REVOLT

    (1.0, 0, 0, [
        (eq, "$freelancer_state", 0),
        (gt, "$enlisted_party", 0),
        (neg|party_is_active, "$enlisted_party"),

		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
        (store_relation, ":relation", "fac_player_supporters_faction", ":commander_faction"),
        (lt, ":relation", 0),

        (party_get_attached_party_with_rank, ":attached_party", "p_main_party", 0),
        (eq, "p_temp_party_2", ":attached_party"),
    ],
    [
        (assign, "$enlisted_party", -1),
        (party_detach, "p_temp_party_2"),
        (store_skill_level, ":cur_leadership", "skl_leadership", "trp_player"),
        (store_skill_level, ":cur_persuasion", "skl_persuasion", "trp_player"),
        (store_add, ":chance", ":cur_persuasion", ":cur_leadership"),
        (val_add, ":chance", 10),
        (store_random_in_range, ":prisoner_state", 0, ":chance"),

        (try_begin),
            (is_between, ":prisoner_state", 0, 5),
            (call_script, "script_party_calculate_strength", "p_main_party", 0),
            (assign, ":main_strength", reg0),
            (call_script, "script_party_calculate_strength", "p_temp_party_2", 0),
            (assign, ":temp_strength", reg0),
            (ge, ":temp_strength", ":main_strength"),

            (party_get_num_prisoner_stacks, ":num_stacks", "p_temp_party_2"),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_prisoner_stack_get_troop_id, ":cur_troops", "p_temp_party_2", ":cur_stack"),
                (party_prisoner_stack_get_size, ":cur_size", "p_temp_party_2", ":cur_stack"),
                (party_remove_prisoners, "p_temp_party_2", ":cur_troops", ":cur_size"),
            (try_end),

            (tutorial_box, "@The released prisoners were not be trusted and they are preparing to attack you!", "@Warning!"),
            (start_encounter, "p_temp_party_2"),
            (change_screen_map),
        (else_try),
            (is_between, ":prisoner_state", 5, 10),
            (tutorial_box, "@The released prisoners scattered as soon as the battle finished. You will not be seeing them again.", "@Notice!"),
            (party_clear, "p_temp_party_2"),
        (else_try),
            (tutorial_box, "@The released prisoners have remained loyal and will join your party", "@Notice!"),
            (party_get_num_companion_stacks, ":num_stacks", "p_temp_party_2"),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":cur_troops", "p_temp_party_2", ":cur_stack"),
                (party_stack_get_size, ":cur_size", "p_temp_party_2", ":cur_stack"),
                (party_add_members, "p_main_party", ":cur_troops", ":cur_size"),
            (try_end),
            (party_clear, "p_temp_party_2"),
        (try_end),
    ]),

# IF LEFT MOUSE CLICK GO TO SOLDIER'S MENU

    (0.0, 0, 0, [
        (eq, "$freelancer_state", 1),
        (key_clicked, key_left_mouse_button),

        (set_fixed_point_multiplier, 1000),
        (mouse_get_position, pos0),
        (position_get_y, ":y", pos0),
        (gt, ":y", 50), #allows the camp, reports, quests, etc. buttons to be clicked
    ],
    [
        (jump_to_menu, "mnu_world_map_soldier"),
        (rest_for_hours_interactive, 9999, 4, 0),
    ]),

(24.0, 0, 0, [
        (eq, "$freelancer_state", 2),
    ],
    [
		(troop_get_slot, ":days_left", "trp_player", "slot_troop_days_on_mission"),
		(try_begin),
		  (gt, ":days_left", 5),
		  (val_sub, ":days_left", 1),
		  (troop_set_slot, "trp_player", "slot_troop_days_on_mission", ":days_left"),
		(else_try),		  
		  (is_between, ":days_left", 1, 5),
		  (assign, reg0, ":days_left"),
		  (display_message, "@You have {reg0} days left till you are declared as a deserter!"),
		  (val_sub, ":days_left", 1),
		  (troop_set_slot, "trp_player", "slot_troop_days_on_mission", ":days_left"),
		(else_try), #declare deserter
		  (eq, ":days_left", 0),
		  (call_script, "script_event_player_deserts"),
          (display_message, "@You have now been declared as a deserter!"),
		(try_end),  
    ]),
#+freelancer end chief
#############script refuerzos ciudades chief#############
##(72, 0, 0.0, [], [  ## establece el spawn de refuerzos cada 72 horas, cambiar a nuestro gusto
##                     (try_for_range, ":center", walled_centers_begin, walled_centers_end),
##                     (party_get_slot, ":besieged", ":center", "slot_center_is_besieged_by"),
##                         (neg|ge, ":besieged", 0), #Town/castle is under siege jump out
##                         (store_faction_of_party, ":faction", ":center"),
##                         (party_get_num_companions, ":garrison", ":center"),
##                         (faction_get_slot, ":party_template_a", ":faction", "slot_faction_reinforcements_a"),
##                         (faction_get_slot, ":party_template_b", ":faction", "slot_faction_reinforcements_b"),
##                         (faction_get_slot, ":party_template_c", ":faction", "slot_faction_reinforcements_c"),
##                         (assign, ":party_template", 0),
##                         (try_begin),
##                             (party_slot_eq, ":center", "slot_party_type", spt_town),
##                             (lt, ":garrison", 170),            ## cuando la guarnicion sea menor, vendran refuerzos a la ciudad
##                             (assign, ":party_template", "pt_reinforcements"),
##                         (else_try),
##                             (party_slot_eq, ":center", "slot_party_type", spt_castle),
##                             (lt, ":garrison", 80),            ## cuando la guarnicion sea menor, vendran refuerzos al castillo
##                             (assign, ":party_template", "pt_reinforcements"),
##                         (try_end),
##                         (try_begin),
##                             (gt, ":party_template", 0),
##                             (try_for_range, ":village_reinforcements", villages_begin, villages_end),
##                                 (try_begin),
##                                     (party_slot_eq, ":center", "slot_party_type", spt_castle),  ## para castillos
##                                     (party_slot_eq, ":village_reinforcements", "slot_village_bound_center", ":center"),
##                                     (party_slot_eq, ":village_reinforcements", "slot_village_state", svs_normal), ## si la villa es atacada no genera refuerzos
##                                     (neg|party_slot_eq, ":center", "slot_town_lord", "trp_player"),  ## si no pertenece al jugador
##                                     (spawn_around_party, ":village_reinforcements", ":party_template"),
##                                     (assign, ":result", reg0),
##                                     (store_random_in_range, ":rand", 0, 100),
##                                     (try_begin),
##                                         (is_between, ":rand", 0, 45),  ## Selecciona el template mas debil
##                                         (party_add_template, ":result", ":party_template_a"),
##                                     (else_try),
##                                         (is_between, ":rand", 45, 85), ## Selecciona el template mas fuerte
##                                         (party_add_template, ":result", ":party_template_b"),
##                                     (else_try),
##                                         (ge, ":rand", 85), ## Get strongest template
##                                         (party_add_template, ":result", ":party_template_c"),
##                                     (try_end),
##                                     (party_set_faction, ":result", ":faction"),
##                                     (party_set_slot, ":result", "slot_party_type", spt_reinforcement_party),
##                                     (party_set_slot, ":result", "slot_party_ai_object", ":center"),
##                                     (str_store_party_name, s14, ":village_reinforcements"),
##                                     (party_set_name, ":result", "@Reinforcements from {s14}"),
##                                     (party_set_ai_behavior,":result",ai_bhvr_travel_to_party),
##                                     (party_set_ai_object,":result", ":center"),
##                                     (party_set_flags, ":result", pf_default_behavior, 1),
##                                 (else_try),        
##                                     (party_slot_eq, ":center", "slot_party_type", spt_town), ## para ciudades
##                                     (party_slot_eq, ":village_reinforcements", "slot_village_bound_center", ":center"),
##                                     (party_slot_eq, ":village_reinforcements", "slot_village_state", svs_normal), ## si la villa es atacada no genera refuerzos
##                                     (neg|party_slot_eq, ":center", "slot_town_lord", "trp_player"), ## si no pertenece al jugador
##                                     (spawn_around_party, ":village_reinforcements", ":party_template"),
##                                     (assign, ":result", reg0),
##                                     (store_random_in_range, ":rand", 0, 100),
##                                     (try_begin),
##                                         (is_between, ":rand", 0, 45),  ## Selecciona el template mas debil
##                                         (party_add_template, ":result", ":party_template_a"),
##                                     (else_try),
##                                         (is_between, ":rand", 40, 85), ## Selecciona el template mas fuerte
##                                         (party_add_template, ":result", ":party_template_b"),
##                                     (else_try),
##                                         (ge, ":rand", 85), ## Get strongest template
##                                         (party_add_template, ":result", ":party_template_c"),
##                                     (try_end),
##                                     (party_set_faction, ":result", ":faction"),
##                                     (party_set_slot, ":result", "slot_party_type", spt_reinforcement_party),
##                                     (party_set_slot, ":result", "slot_party_ai_object", ":center"),
##                                     (str_store_party_name, s14, ":village_reinforcements"),
##                                     (party_set_name, ":result", "@Reinforcements of {s14}"),
##                                     (party_set_ai_behavior,":result",ai_bhvr_travel_to_party),
##                                     (party_set_ai_object,":result", ":center"),
##                                     (party_set_flags, ":result", pf_default_behavior, 1),
##                                 (try_end),
##                             (try_end),
##                         (try_end),
##                     (try_end)]),
##########chief acaba###########
  ##diplomacy chief start
  # Appoint chamberlain
   (24 , 0, 24 * 12, 
   [],
   [
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", centers_begin, centers_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", "slot_town_lord"),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),
    
    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, "$g_player_chamberlain"),
      (display_message, "@{!}DEBUG : chamberlain: {reg0}"),
    (try_end),

    (assign, ":notification", 0),
    (try_begin),
      (eq, "$g_player_chamberlain", 0),
      (assign, ":notification", 1),
    (else_try),
      (neq, "$g_player_chamberlain", -1),
      (neq, "$g_player_chamberlain", "trp_dplmc_chamberlain"),
      (assign, ":notification", 1),
    (try_end),
    
    (try_begin),
      (eq, ":notification", 1),
      (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_chamberlain", 0, 0),
    (try_end),]
   ),

  # Appoint chancellor
   (24 , 0, 24 * 14, 
   [],
   [
   (assign, ":has_fief", 0),
    (try_for_range, ":center_no", towns_begin, towns_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", "slot_town_lord"),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),
    
    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, "$g_player_chancellor"),
      (display_message, "@{!}DEBUG : chancellor: {reg0}"),
    (try_end),

    (assign, ":notification", 0),
    (try_begin),
      (eq, "$g_player_chancellor", 0),
      (assign, ":notification", 1),
    (else_try),
      (neq, "$g_player_chancellor", -1),
      (neq, "$g_player_chancellor", "trp_dplmc_chancellor"),
      (assign, ":notification", 1),
    (try_end),
    
    (try_begin),
      (eq, ":notification", 1),
      (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_chancellor", 0, 0),
    (try_end),
    ]
   ),
##diplomacy chief end
###SEA BATTLES chief
##(0.5, 0, 0, [(neq, "$g_player_icon_state", pis_ship),
##            (neq, "$g_player_is_captive", 1),
##             (party_get_current_terrain,":terrain","p_main_party"),
##    (assign,reg1,":terrain"),
##], # rt_steppe is an example for the name of your new water terrain
##   [(try_begin),
##       (troop_get_inventory_slot, ":cur_horse", "trp_player", 8), #horse slot
##    (assign, ":new_icon", -1),
##    (try_begin),
##      (eq,reg1,7), #terreno
##      (assign, ":new_icon", "icon_ship"),
##           (store_troop_gold,":money","trp_player"),
##      (try_begin),
##        (gt,":money",9),
##       (troop_remove_gold, "trp_player", 10),
##     (display_message,"@You hire a boat for the trip."),
##        (display_message,"@Your men are concerned about the ocean."),
##      (call_script, "script_change_player_party_morale", -1),
##    (else_try),
##        (display_message,"@You do not have money, but forced some fishermen to take their boats."),
##        (call_script, "script_change_player_honor", -1),
##        (display_message,"@Your men are concerned about the ocean."),
##      (call_script, "script_change_player_party_morale", -1),
##      (try_end),
###     (display_message,"@water"),
##     (else_try),
##      (eq, "$g_player_icon_state", pis_normal),
##      (try_begin),
##        (ge, ":cur_horse", 0),
##        (assign, ":new_icon", "icon_player_horseman"),
###        (display_message,"@Back on the ground. Gone are the dizzy, rocking and sea monsters. Your men seem more relaxed."),
###      (call_script, "script_change_player_party_morale", 5),
##      (else_try),
##        (assign, ":new_icon", "icon_player"),
###        (display_message,"@Back on the ground. Gone are the dizzy, rocking and sea monsters. Your men seem more relaxed."),
###      (call_script, "script_change_player_party_morale", 5),
##      (try_end),
##    (else_try),
##      (eq, "$g_player_icon_state", pis_camping), # All of this is thanks to Lumos bein' generous, and not being as much of a lazy arse as I am
##      (assign, ":new_icon", "icon_camp"),
##    (try_end),
##    (party_set_icon,"p_main_party", ":new_icon"),
##]),

#esta sobre oceano despues de batalla
##  #SEA BATTLES chief
##(0.1, 0, 0, [
##   (neq, "$g_player_icon_state", pis_ship),
##             (party_get_current_terrain,":terrain","p_main_party"),
##    (assign,reg1,":terrain"),
####            (neq, "$g_player_is_captive", 1),
##], # rt_steppe is an example for the name of your new water terrain
##   [(try_begin),
##       (troop_get_inventory_slot, ":cur_horse", "trp_player", 8), #horse slot
##    (assign, ":new_icon", -1),
##    (try_begin),
##(neq,reg1,7), #terreno
##(this_or_next|eq,reg1,0), #terreno
##(eq,reg1,8), #terreno
##      (assign, ":new_icon", "icon_ship"),
##     (else_try),
##      (eq, "$g_player_icon_state", pis_normal),
##      (try_begin),
##        (ge, ":cur_horse", 0),
##        (assign, ":new_icon", "icon_player_horseman"),
##      (else_try),
##        (assign, ":new_icon", "icon_player"),
##      (try_end),
##    (else_try),
##      (eq, "$g_player_icon_state", pis_camping), # All of this is thanks to Lumos bein' generous, and not being as much of a lazy arse as I am
##      (assign, ":new_icon", "icon_camp"),
##    (try_end),
##    (party_set_icon,"p_main_party", ":new_icon"),
##]),
##
##
##
##   (0.1, 0, 0.0, [],
##[(try_for_parties, ":cur_party"),
##   (party_get_current_terrain, ":terrain", ":cur_party"),
##   (eq, ":terrain", 7), #terreno
##  (party_get_template_id, ":cur_template", ":cur_party"),
## (this_or_next|eq, ":cur_template", "pt_kingdom_hero_party"),
## (this_or_next|eq, ":cur_template", "pt_kingdom_caravan_party"),
## (this_or_next|eq, ":cur_template", "pt_manhunters"),
## (this_or_next|eq, ":cur_template", "pt_village_farmers"),
## (this_or_next|eq, ":cur_template", "pt_merchant_caravan"),
## (this_or_next|eq, ":cur_template", "pt_neko"),
## (this_or_next|eq, ":cur_template", "pt_cado_template"),
## (this_or_next|eq, ":cur_template", "pt_arrians"),
## (this_or_next|eq, ":cur_template", "pt_eadfrith"),
## (this_or_next|eq, ":cur_template", "pt_center_reinforcements"),
## (this_or_next|eq, ":cur_template", "pt_skirmish_party"),
## (this_or_next|eq, ":cur_template", "pt_player_loot_wagon"),
## (this_or_next|eq, ":cur_template", "pt_personal_messenger"),
## (this_or_next|eq, ":cur_template", "pt_sacerdotes_party"),
## (this_or_next|eq, ":cur_template", "pt_paganos_party"),
## (this_or_next|eq, ":cur_template", "pt_reinforcements"),
## (this_or_next|eq, ":cur_template", "pt_dplmc_gift_caravan"),
## (this_or_next|eq, ":cur_template", "pt_dplmc_recruiter"),
## (this_or_next|eq, ":cur_template", "pt_deserters"),
## (this_or_next|eq, ":cur_template", "pt_looters"),
## (this_or_next|eq, ":cur_template", "pt_forest_bandits"),
## (this_or_next|eq, ":cur_template", "pt_steppe_bandits"),
## (this_or_next|eq, ":cur_template", "pt_mountain_bandits"),
## (this_or_next|eq, ":cur_template", "pt_taiga_bandits"),
## (this_or_next|eq, ":cur_template", "pt_sea_raiders2"),
## (eq, ":cur_template", "pt_sea_raiders"),
##   (party_set_icon, ":cur_party", "icon_ship"),
## (else_try),
##   (neq,":terrain",7), #terreno
##   (party_get_template_id, ":cur_template", ":cur_party"),
##   (eq, ":cur_template", "pt_kingdom_hero_party"),
## (party_set_icon,":cur_party","icon_flagbearer_a"),
## (else_try),
## (this_or_next|eq, ":cur_template", "pt_dplmc_gift_caravan"),
## (this_or_next|eq, ":cur_template", "pt_player_loot_wagon"),
## (eq, ":cur_template", "pt_kingdom_caravan_party"),
## (party_set_icon,":cur_party","icon_mule"),
## (else_try),
## (this_or_next|eq, ":cur_template", "pt_dplmc_recruiter"),
## (this_or_next|eq, ":cur_template", "pt_personal_messenger"),
## (eq, ":cur_template", "pt_merchant_caravan"),
## (party_set_icon,":cur_party","icon_gray_knight"),
## (else_try),
## (eq, ":cur_template", "pt_skirmish_party"),
## (party_set_icon,":cur_party","icon_khergit"),
## (else_try),
## (this_or_next|eq, ":cur_template", "pt_sacerdotes_party"),
## (this_or_next|eq, ":cur_template", "pt_paganos_party"),
##  (eq, ":cur_template", "pt_village_farmers"),
## (party_set_icon,":cur_party","icon_peasant"),
## (else_try),
## (this_or_next|eq, ":cur_template", "pt_reinforcements"),
## (this_or_next|eq, ":cur_template", "pt_manhunters"),
## (this_or_next|eq, ":cur_template", "pt_neko"),
## (this_or_next|eq, ":cur_template", "pt_cado_template"),
## (this_or_next|eq, ":cur_template", "pt_arrians"),
## (this_or_next|eq, ":cur_template", "pt_eadfrith"),
## (this_or_next|eq, ":cur_template", "pt_center_reinforcements"),
##  (this_or_next|eq, ":cur_template", "pt_looters"),
## (this_or_next|eq, ":cur_template", "pt_forest_bandits"),
## (this_or_next|eq, ":cur_template", "pt_steppe_bandits"),
## (this_or_next|eq, ":cur_template", "pt_mountain_bandits"),
## (this_or_next|eq, ":cur_template", "pt_sea_raiders2"),
## (this_or_next|eq, ":cur_template", "pt_taiga_bandits"),
## (this_or_next|eq, ":cur_template", "pt_deserters"),
## (eq, ":cur_template", "pt_sea_raiders"),
## (party_set_icon,":cur_party","icon_axeman"),
## (else_try),
## (eq, ":cur_template", "pt_cattle_herd1"),
## (party_set_icon,":cur_party","icon_cattle"),
## (try_end),]),
##
###cambio parties navales
##     (0.1, 0, 0.0, [],
##[(try_for_parties, ":cur_party"),
##   (party_get_current_terrain, ":terrain", ":cur_party"),
##   (this_or_next|eq,":terrain",2), #terreno
##   (this_or_next|eq,":terrain",3), #terreno
##   (eq,":terrain",4), #terreno
##   (party_get_template_id, ":cur_template", ":cur_party"),
## (this_or_next|eq, ":cur_template", "pt_sea_raiders_ships"),
## (this_or_next|eq, ":cur_template", "pt_sea_raiders_ships2"),
## (eq, ":cur_template", "pt_sea_raiders_ships3"),
## (party_set_icon,":cur_party","icon_axeman"),
## (else_try),
##   (this_or_next|neq,":terrain",2), #terreno
##   (this_or_next|neq,":terrain",3), #terreno
##   (neq,":terrain",4), #terreno
##   (party_get_template_id, ":cur_template", ":cur_party"),
## (this_or_next|eq, ":cur_template", "pt_sea_raiders_ships"),
## (this_or_next|eq, ":cur_template", "pt_sea_raiders_ships2"),
## (eq, ":cur_template", "pt_sea_raiders_ships3"),
## (party_set_icon,":cur_party","icon_ship"),
## (try_end),]),
##
##
##  #para animales chief
##
##     (0.1, 0, 0.0, [],
##[(try_for_parties, ":cur_party"),
##   (party_get_current_terrain, ":terrain", ":cur_party"),
##   (eq,":terrain",7), #terreno
##  (party_get_template_id, ":cur_template", ":cur_party"),
## (this_or_next|eq, ":cur_template", "pt_deer_herd"),
## (eq, ":cur_template", "pt_boar_herd"),
##   (party_set_icon, ":cur_party", "icon_castle_snow_a"),
## (else_try),
##   (neq,":terrain",7), #terreno
##   (party_get_template_id, ":cur_template", ":cur_party"),
## (this_or_next|eq, ":cur_template", "pt_deer_herd"),
##   (eq, ":cur_template", "pt_boar_herd"),
## (party_set_icon,":cur_party","icon_cattle"),
## (try_end),]),
###chief acaba
#### SEA BATTLES END chief
###parties de seguidores followers chief
##     (0.8, 0, 0.0, [    (call_script, "script_party_count_members_with_full_health", "p_main_party"),
##    (ge, reg0, 300),
##],
##[
##      (store_script_param_1, ":faction_no"),
##      (str_store_faction_name, s7, ":faction_no"),
##    (try_for_parties, ":cur_party"),
##    (party_get_current_terrain, ":terrain", ":cur_party"),
##   (this_or_next|eq,":terrain",2), #terreno
##   (this_or_next|eq,":terrain",3), #terreno
##   (eq,":terrain",4), #terreno
##  (party_get_template_id, ":cur_template", ":cur_party"),
##         (assign, ":cur_template", reg0),
##        (is_between, ":cur_template", active_npcs_begin, active_npcs_end),
## (eq, ":cur_template", "pt_kingdom_hero_party"),
##(spawn_around_party,":cur_template","pt_followers"),
##        (assign, ":result", reg0),
##        (party_set_faction, ":result", ":faction_no"),
###    (party_set_ai_behavior, "pt_followers", ai_bhvr_travel_to_party),
##    (party_set_ai_behavior, "pt_followers", ai_bhvr_track_party),
##    (party_set_flags, "pt_followers", pf_default_behavior, 0),
##            (store_distance_to_party_from_party, reg(4),":cur_template", "pt_followers"),
##            (lt, reg(4), 0),
####         (try_begin),
####        (try_end),
##    (else_try),
##   (this_or_next|neq,":terrain",2), #terreno
##   (this_or_next|neq,":terrain",3), #terreno
##   (neq,":terrain",4), #terreno
###   (eq, ":cur_template", "pt_kingdom_hero_party"),
##    (remove_party, "pt_followers"),
## (try_end),]),
#chief seguidores acaba

#paso del dia aviso chief
    #change to night routine
     (1, 0, 0, [[eq,"$daytime",1],[store_time_of_day,reg(0)],[gt,reg(0), 18]],
                [[display_message, "str_the_sun_sets",0xFFDFE65B], [assign,"$daytime",0],
                 (store_random, reg(1), 10),
                 (try_begin, 0),(lt, reg(1), 7),
                   (play_sound,"snd_wolf_short"),  
                 (else_try, 0),(ge, reg(1), 7),
                   (play_sound,"snd_wolf_short"),
                 (try_end, 0)]),                 


#change to day routine
     (1, 0, 0, [[eq,"$daytime",0],[store_time_of_day,reg(0)],[ge,reg(0), 5],[le,reg(0), 18]],
                [[display_message, "str_the_sun_rises",0xFFDFE65B],[assign,"$daytime",1],
                 (store_random, reg(1), 10),
                 (try_begin, 0),(lt, reg(1), 7),
                   (play_sound,"snd_morning_birds"),  
                 (else_try, 0),(ge, reg(1), 7),
                   (play_sound,"snd_morning_birds"),
                 (try_end, 0)
                 ]), 

###midday and midnight routine
     (0, 6, 12, [],
                [[try_begin],
##				 [eq,"$daytime",0],
##				 [display_message, "str_it_is_midnight",0xFFDFE65B],
##				 [else_try],
##				 [eq,"$daytime",1],
##				 [display_message, "str_it_is_noon",0xFFDFE65B],
                                 (play_sound,"snd_bells"),
				 [end_try],				
                 ]),

  #tener hijo
  (24, 270, ti_once,
[
      (eq,"$g_spouse_embarazada",1),         
],
[
      (assign,"$g_spouse_embarazada2",1),         
]),
#tener hijo chief acaba
#################################grueso chief final acaba#########################################
# slot
#   (0.0, 0, 968.0, [],
# [
#   (call_script, "script_refresh_special_merchants8"),
# ]),

# # slot
#   (0.0, 0, 968.0, [],
# [
#   (call_script, "script_refresh_special_merchants0"),
# ]),

# # slot
#   (0.0, 0, 968.0, [],
# [
#   (call_script, "script_refresh_special_merchants10"),
# ]),
] \
+ companions.triggers \
+ caravans.triggers \
    + constable.triggers \
