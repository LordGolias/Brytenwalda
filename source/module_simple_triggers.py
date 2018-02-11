from .header_operations import *
from .header_common import *

from .header_triggers import *
from .header_parties import *
from .header_music import mtf_sit_travel
from .header_items import ek_item_0
from .header_item_modifiers import imod_rotten, imod_fresh
from .header_skills import skl_trainer, skl_foraging
from .header_troops import ca_intelligence, ca_charisma
from .header_terrain_types import rt_water, rt_river, rt_bridge, dplmc_terrain_code_siege

from .module_constants import *

from . import economy, loans, companions, caravans, villages, patrols, constable
####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked. gdwThis is in hours and it doesn't appear to allow a delay to be set
##gdw the game starts at 6 am I'm told
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################



simple_triggers = [

# This trigger is deprecated. Use "script_game_event_party_encounter" in module_scripts.py instead  
  (ti_on_party_encounter,
   [
    ]),


# This trigger is deprecated. Use "script_game_event_simulate_battle" in module_scripts.py instead 
  (ti_simulate_battle,
   [
    ]),


  (0.5,##Don't understand the purpose of this as it makes resetting parties complicated. Changed interval check from 1-3 hours
   [
     # (try_begin),
     #    (eq, "$training_ground_position_changed", 0),
     #    (assign, "$training_ground_position_changed", 1),
		   #  (set_fixed_point_multiplier, 100),
     #    (position_set_x, pos0, 7050),
     #    (position_set_y, pos0, 7200),
     #    (party_set_position, "p_training_ground_3", pos0),
     #  (try_end),
	 # (try_begin),#changefromTMLpergdw per=>
  # #  ("celidon_forest","Ancient_Stones",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.0,-52.0),[]),  #orig at 13.88,79.56)26.53,-57.13
  # # ("hidden_valley","Rare_Ruins",icon_town_snow|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.598,47.851),[]),  #tmlpgdw-59.91,47.69#TML78.56^^
  # # ("iniau_hideout","Sacred_Grove",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(93.052,90.85),[]),  #tml91.28,89.86##93.052,90.85krag
  # # ("quarry1","Quarry",icon_town_snow|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(86.11,67.17),[]),
  # # ("hadrian_wall","Hadrian Wall",icon_town_snow|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.83,1.26),[]),
  # # ("odin_cave","Cave",icon_castle_snow_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.013,-123.055),[]),
  #     (neq, "$tml_version", 120),
  #     (assign, "$tml_version", 120),
  #     (set_fixed_point_multiplier, 100),
  #     (position_set_x, pos0, -1224),
  #     (position_set_y, pos0, 338),
  #     (party_set_position, "p_town_7", pos0),
  #     (position_set_x, pos0, -5904),
  #     (position_set_y, pos0, -4742),
  #     (party_set_position, "p_town_27", pos0),
  #     (position_set_x, pos0, 5049),
  #     (position_set_y, pos0, 2548),
  #     (party_set_position, "p_town_32", pos0),
  #     (position_set_x, pos0, 8234),
  #     (position_set_y, pos0, -1891),
  #     (party_set_position, "p_town_33", pos0),
  #     (position_set_x, pos0, -5234),
  #     (position_set_y, pos0, -13013),
  #     (party_set_position, "p_town_37", pos0),
  #     (position_set_x, pos0, -7649),
  #     (position_set_y, pos0, 12352),
  #     (party_set_position, "p_castle_19", pos0),
  #     (position_set_x, pos0, -8828),
  #     (position_set_y, pos0, 12660),
  #     (party_set_position, "p_village_49", pos0),
  #     (position_set_x, pos0, 2500),  ##1388  2
  #     (position_set_y, pos0, -5200),   ##7976
  #     (party_set_position, "p_celidon_forest", pos0),
  #     (position_set_x, pos0, -6060),
  #     (position_set_y, pos0, 4785),
  #     (party_set_position, "p_hidden_valley", pos0),
  #     (position_set_x, pos0, 9305),
  #     (position_set_y, pos0, 9085),
  #     (party_set_position, "p_iniau_hideout", pos0),
  #     (position_set_x, pos0, 1501),
  #     (position_set_y, pos0, -12305),
  #     (party_set_position, "p_odin_cave", pos0),
  #     (position_set_x, pos0, 1225),
  #     (position_set_y, pos0, 549),
  #     (party_set_position, "p_monasterio1", pos0),
  #     (position_set_x, pos0, -7320),
  #     (position_set_y, pos0, 3302),
  #     (party_set_position, "p_bridge_1", pos0),
  #     (position_set_x, pos0, -5903),
  #     (position_set_y, pos0, -1036),
  #     (party_set_position, "p_bridge_2", pos0),
  #     (position_set_x, pos0, -7831),
  #     (position_set_y, pos0, 7870),
  #     (party_set_position, "p_bridge_3", pos0),
  #     (position_set_x, pos0, -1903),
  #     (position_set_y, pos0, 10656),
  #     (party_set_position, "p_bridge_4", pos0),
  #     (position_set_x, pos0, -8837),
  #     (position_set_y, pos0, 13087),
  #     (party_set_position, "p_bridge_5", pos0),
  #     (position_set_x, pos0, -5010),
  #     (position_set_y, pos0, 12552),
  #     (party_set_position, "p_bridge_6", pos0),
  #     (position_set_x, pos0, -1972),
  #     (position_set_y, pos0, 9466),
  #     (party_set_position, "p_bridge_7", pos0),
  #     (position_set_x, pos0, 3100),
  #     (position_set_y, pos0, -5927),
  #     (party_set_position, "p_bridge_8", pos0),
  #     (position_set_x, pos0, 10106),
  #     (position_set_y, pos0, 7006),
  #     (party_set_position, "p_bridge_9", pos0),
  #     (position_set_x, pos0, 823),
  #     (position_set_y, pos0, -6391),
  #     (party_set_position, "p_bridge_10", pos0),
  #     (position_set_x, pos0, -5932),
  #     (position_set_y, pos0, 702),
  #     (party_set_position, "p_bridge_11", pos0),
  #     (position_set_x, pos0, -7448),
  #     (position_set_y, pos0, 4441),
  #     (party_set_position, "p_bridge_12", pos0),
  #     (position_set_x, pos0, -3787),
  #     (position_set_y, pos0, 11490),
  #     (party_set_position, "p_bridge_13", pos0),
  #     (position_set_x, pos0, -403),
  #     (position_set_y, pos0, 8336),
  #     (party_set_position, "p_bridge_15", pos0),
  #     (position_set_x, pos0, 8831),
  #     (position_set_y, pos0, 4445),
  #     (party_set_position, "p_bridge_16", pos0),
  #     (position_set_x, pos0, -3304),
  #     (position_set_y, pos0, 15350),
  #     (party_set_position, "p_bridge_17", pos0),
  #     (position_set_x, pos0, 7366),
  #     (position_set_y, pos0, 9129),
  #     (party_set_position, "p_bridge_18", pos0),
  #     (position_set_x, pos0, 8605),
  #     (position_set_y, pos0, 9431),
  #     (party_set_position, "p_bridge_19", pos0),
  #     (str_store_string, s0, "@looking for victims"),
  #     (party_set_name, "p_sea_raider_spawn_point_1", s0),
  #     (party_set_name, "p_sea_raider_spawn_point_2", s0),
  #     (party_set_name, "p_sea_raider_spawn_point_3", s0),
  #   (try_end),
	##gdw see game menus build_ladders_cont
#      (gt,"$auto_siege_town",0), #siege warfare chief
#      (gt,"$auto_siege_port",0), #siege warfare chief

###anadido sieges menu por caba'drin chief
      (gt,"$auto_besiege_town",0),#gdw town is being besieged
      (gt,"$g_player_besiege_town", 0),#gdw town is being besieged by player
      (ge, "$g_siege_method", 1),
      
      (store_distance_to_party_from_party, ":distance", "$g_player_besiege_town", "p_main_party"),
      (try_begin),
        (gt, ":distance", raid_distance / 2),
        (str_store_party_name_link, s1, "$g_player_besiege_town"),
        (display_message, "@You have broken off your siege of {s1}."),
        (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
        (assign, "$g_player_besiege_town", -1),

        (assign, "$g_raid_distance_warned", 0),
##trigger combined from 4 strigs below gdw
      (else_try),
        (ge, ":distance", raid_distance / 3),

        (neq, "$g_raid_distance_warned", 1),

        (str_store_party_name_link, s1, "$g_player_besiege_town"),
        (display_message, "@You cannot maintain your siege of {s1} from this distance. You risk your lines breaking."),

        (assign, "$g_raid_distance_warned", 1),
      (else_try),
        (assign, "$g_raid_distance_warned", 0),
        (store_current_hours, ":cur_hours"),
      (eq, "$g_siege_force_wait", 0), #chief cambia para reparar bug de esperar
      (ge, ":cur_hours", "$g_siege_method_finish_hours"), #chief cambia para reparar bug de esperar
      (ge, ":cur_hours", "$g_siegewarfare_metodo"), #siege warfare #chief cambia para reparar bug de esperar

        (neg|is_currently_night),
        (rest_for_hours, 0, 0, 0), #stop resting, if resting
        (start_encounter, "$auto_besiege_town"),###this line is add-on
      (try_end),



##gdw snip below was alone in this position. Trying to combine
      # (store_current_hours, ":cur_hours"),
      # (eq, "$g_siege_force_wait", 0),
      # (ge, ":cur_hours", "$g_siege_method_finish_hours"),
      # (ge, ":cur_hours", "$g_siegewarfare_metodo"), #siege warfare
      # (neg|is_currently_night),
      # (rest_for_hours, 0, 0, 0), #stop resting
    ]),

  (0,
   [
      (try_begin),
        (eq, "$bug_fix_version", 0),     
      
        #fix for hiding test_scene in older savegames
        (disable_party, "p_test_scene"),
        #fix for correcting town_1 siege type
        (party_set_slot, "p_town_1", "slot_center_siege_with_belfry", 0),
        #fix for hiding player_faction notes
        (faction_set_note_available, "fac_player_faction", 0),
        #fix for hiding faction 0 notes
        (faction_set_note_available, "fac_no_faction", 0),
        #fix for removing kidnapped girl from party
        (try_begin),
          (neg|check_quest_active, "qst_kidnapped_girl"),
          (party_remove_members, "p_main_party", "trp_kidnapped_girl", 1),
        (try_end),
        #fix for not occupied but belong to a faction lords
        (try_for_range, ":cur_troop", lords_begin, lords_end),
          (try_begin),                
            (troop_slot_eq, ":cur_troop", "slot_troop_occupation", slto_inactive),
            (store_troop_faction, ":cur_troop_faction", ":cur_troop"),
            (is_between, ":cur_troop_faction", "fac_kingdom_1", kingdoms_end),          
            (troop_set_slot, ":cur_troop", "slot_troop_occupation", slto_kingdom_hero),
          (try_end),
        (try_end),  
        #fix for an error in 1.105, also fills new slot values
        (call_script, "script_initialize_item_info"),  
        
        (assign, "$bug_fix_version", 1),     
      (try_end),  

      (eq,"$g_player_is_captive",1),
      (gt, "$capturer_party", 0),
      (party_is_active, "$capturer_party"),
      (party_relocate_near_party, "p_main_party", "$capturer_party", 0),
    ]),


#Auto-menu
  (0,
   [          
     (try_begin),
       (gt, "$g_last_rest_center", 0),
       (party_get_battle_opponent, ":besieger_party", "$g_last_rest_center"),
       (gt, ":besieger_party", 0),
       (store_faction_of_party, ":encountered_faction", "$g_last_rest_center"),
       (store_relation, ":faction_relation", ":encountered_faction", "fac_player_supporters_faction"),
       (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
       (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_supporters_faction"),
       (ge, ":faction_relation", 0),
       (lt, ":besieger_party_relation", 0),
       (start_encounter, "$g_last_rest_center"),
       (rest_for_hours, 0, 0, 0), #stop resting
     (else_try),
       (store_current_hours, ":cur_hours"),
       (assign, ":check", 0),
       (try_begin),
         (neq, "$g_check_autos_at_hour", 0),
         (ge, ":cur_hours", "$g_check_autos_at_hour"),
         (assign, ":check", 1),
         (assign, "$g_check_autos_at_hour", 0),
       (try_end),
       (this_or_next|eq, ":check", 1),
       (map_free),
       (try_begin),
         (ge,"$auto_menu",1),
         (jump_to_menu,"$auto_menu"),
         (assign,"$auto_menu",-1),
       (else_try),
         (ge,"$auto_enter_town",1),
         (start_encounter, "$auto_enter_town"),
		 (try_begin), #rigale chief empieza
			 (eq,"$begging_action_started",1),
			 (assign,"$begging_action_started",0), #abort begging to avoid conflicts 
		(try_end), #rigale chief acaba
       (else_try), #chief permite a player acceder a inventario en sieges, mas en tigger por clave: acceder inventario en sieges
         (ge,"$auto_besiege_town",1),
         (start_encounter, "$auto_besiege_town"),
       (else_try),
         (ge,"$g_camp_mode", 1),
         (assign, "$g_camp_mode", 0),
         (assign, "$g_infinite_camping", 0),
         
#motomataru fix camping on water
         # (assign, "$g_player_icon_state", pis_normal),
         (party_get_current_terrain,":terrain","p_main_party"),
		 (try_begin),
           (neq, ":terrain", 0),	#not rt_water
           (neq, ":terrain", 7),	#not rt_river used as water terrain
           (neq, ":terrain", 8),	#not rt_bridge used as water terrain
           (assign, "$g_player_icon_state", pis_normal),
		 (else_try),
           (assign, "$g_player_icon_state", pis_ship),
 		 (try_end),
#end motomataru fix camping on water
     (rest_for_hours, 0, 0, 0), #stop camping
                  
         (display_message, "@Breaking camp..."),
###rigale chief 
	   (else_try), #rigale ambush end by moving
			(eq, "$ambush_set_by_player", 1),
			(assign,"$ambush_set_by_player", 0),
			(display_message, "@AMBUSH CANCELLED, DON'T MOVE WHILE AMBUSHING.",0xFF3300),
			(rest_for_hours, 0, 0, 0), #stop ambushing
#rigale chief acaba			
						
       (try_end),
     (try_end),
     ]),
###anadido sieges menu por caba'drin chief
(#0.25,##gdw m oved to top of s triggers partly because it isn't working and we need to try something different
   ti_on_party_encounter,
  [
    ]),

      # (gt,"$auto_besiege_town",0),

      # (ge,"$g_player_besiege_town", 0),
      # (ge, "$g_siege_method", 1),
      
      # (store_distance_to_party_from_party, ":distance", "$g_player_besiege_town", "p_main_party"),
      # (try_begin),
      #   (gt, ":distance", raid_distance / 2),
      #   (str_store_party_name_link, s1, "$g_player_besiege_town"),
      #   (display_message, "@You have broken off your siege of {s1}."),
      #   (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
      #   (assign, "$g_player_besiege_town", -1),

      #   (assign, "$g_raid_distance_warned", 0),

      # (else_try),
      #   (ge, ":distance", raid_distance / 3),

      #   (neq, "$g_raid_distance_warned", 1),

      #   (str_store_party_name_link, s1, "$g_player_besiege_town"),
      #   (display_message, "@You cannot maintain your siege of {s1} from this distance. You risk your lines breaking."),

      #   (assign, "$g_raid_distance_warned", 1),
      # (else_try),
      #   (assign, "$g_raid_distance_warned", 0),
      #   (store_current_hours, ":cur_hours"),
      # (eq, "$g_siege_force_wait", 0), #chief cambia para reparar bug de esperar
      # (ge, ":cur_hours", "$g_siege_method_finish_hours"), #chief cambia para reparar bug de esperar
      # (ge, ":cur_hours", "$g_siegewarfare_metodo"), #siege warfare #chief cambia para reparar bug de esperar

      #   (neg|is_currently_night),
      #   (rest_for_hours, 0, 0, 0), #stop resting, if resting
      #   (start_encounter, "$auto_besiege_town"),
      # (try_end),
    # ]),


  ###acaba sieges menu chief
#Notification menus
  (0,
   [
     (troop_slot_ge, "trp_notification_menu_types", 0, 1),
     (troop_get_slot, ":menu_type", "trp_notification_menu_types", 0),
     (troop_get_slot, "$g_notification_menu_var1", "trp_notification_menu_var1", 0),
     (troop_get_slot, "$g_notification_menu_var2", "trp_notification_menu_var2", 0),
     (jump_to_menu, ":menu_type"),
     (assign, ":end_cond", 2),
     (try_for_range, ":cur_slot", 1, ":end_cond"),
       (try_begin),
         (troop_slot_ge, "trp_notification_menu_types", ":cur_slot", 1),
         (val_add, ":end_cond", 1),
       (try_end),
       (store_sub, ":cur_slot_minus_one", ":cur_slot", 1),
       (troop_get_slot, ":local_temp", "trp_notification_menu_types", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_types", ":cur_slot_minus_one", ":local_temp"),
       (troop_get_slot, ":local_temp", "trp_notification_menu_var1", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_var1", ":cur_slot_minus_one", ":local_temp"),
       (troop_get_slot, ":local_temp", "trp_notification_menu_var2", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_var2", ":cur_slot_minus_one", ":local_temp"),
     (try_end),
    ]),

  #Music,
  (1,
   [
       (map_free),
       (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
	    ]),	

  (0,
	[
      # reset mission participation
      (try_begin),
        (gt, "$g_reset_mission_participation", 1),
        
        (try_for_range, ":troop", active_npcs_begin, kingdom_ladies_end),
          (troop_set_slot, ":troop", "slot_troop_mission_participation", 0),
        (try_end),
      (try_end),
	]),
	
(24,
[
    (try_for_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
      (faction_get_slot, ":faction_morale", ":kingdom_no",  "slot_faction_morale_of_player_troops"),

	  (store_sub, ":divisor", 140, "$player_right_to_rule"),
	  (val_div, ":divisor", 14),
	  (val_max, ":divisor", 1),
	  
      (store_div, ":faction_morale_div_10", ":faction_morale", ":divisor"), #10 is the base, down to 2 for 100 rtr     
      (val_sub, ":faction_morale", ":faction_morale_div_10"),           

      (faction_set_slot, ":kingdom_no",  "slot_faction_morale_of_player_troops", ":faction_morale"),
    (try_end),
]),

	
 (4, #Locate kingdom ladies
    [
      #change location for all ladies
      (try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
        (neg|troop_slot_ge, ":troop_id", "slot_troop_prisoner_of_party", 0),
        (call_script, "script_get_kingdom_lady_social_determinants", ":troop_id"),
        (assign, ":location", reg1),
        (troop_set_slot, ":troop_id", "slot_troop_cur_center", ":location"),
      (try_end),	
	]),

	
 (80, #Error check for multiple parties on the map
	[
	(eq, "$cheat_mode", 1),
	(assign, ":debug_menu_noted", 0),
	(try_for_parties, ":party_no"),
		(gt, ":party_no", "p_spawn_points_end"),
		(party_stack_get_troop_id, ":commander", ":party_no", 0),
		##diplomacy start+ chief
		(is_between, ":commander", heroes_begin, heroes_end),
		(this_or_next|troop_slot_eq, ":commander", "slot_troop_occupation", slto_kingdom_hero),
		##diplomacy end+
		(is_between, ":commander", active_npcs_begin, active_npcs_end),
		(troop_get_slot, ":commander_party", ":commander", "slot_troop_leaded_party"),
		(neq, ":party_no", ":commander_party"),
		(assign, reg4, ":party_no"),
		(assign, reg5, ":commander_party"),
		
		(str_store_troop_name, s3, ":commander"),
		(display_message, "@{!}{s3} commander of party #{reg4} which is not his troop_leaded party {reg5}"), 
		##diplomacy start+ Make it clear what the error was chief
		(try_begin),
			(gt, reg4, 0),
			(gt, reg5, 0),
			(str_store_party_name, s3, reg4),
			(str_store_party_name, s65, reg5),
			(display_message, "@{!} Commanded party #{reg4} is {s3}, troop_leaded party #{reg5} is {s65}"),
			(str_store_troop_name, s3, ":commander"),
		(try_end),
		##diplomacy end+
		(str_store_string, s65, "str_party_with_commander_mismatch__check_log_for_details_"),

		(try_begin),
			(eq, ":debug_menu_noted", 0),
			(call_script, "script_add_notification_menu", "mnu_debug_alert_from_s65", 0, 0),
			(assign, ":debug_menu_noted", 1),
		(try_end),
	(try_end),
	]),	
	
   
 (24, #Kingdom ladies send messages
 [ 
	(try_begin),
		(neg|check_quest_active, "qst_visit_lady"),
		(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 1),
		(neg|troop_slot_ge, "trp_player", "slot_troop_spouse", active_npcs_begin),
		
		(assign, ":lady_not_visited_longest_time", -1),
		(assign, ":longest_time_without_visit", 120), #five days
		
		(try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
            ##diplomacy start+ not dead, exiled, etc. chief
			(neg|troop_slot_ge, ":troop_id", "slot_troop_occupation", slto_retirement),
			##diplomacy end+
		
			#set up message for ladies the player is courting
			(troop_slot_ge, ":troop_id", "slot_troop_met", 2),
			(neg|troop_slot_eq, ":troop_id", "slot_troop_met", 4),
			
			(troop_slot_eq, ":troop_id", "slot_lady_no_messages", 0),
			(troop_slot_eq, ":troop_id", "slot_troop_spouse", -1),
			
			(troop_get_slot, ":location", ":troop_id", "slot_troop_cur_center"),
			(is_between, ":location", walled_centers_begin, walled_centers_end),
			(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_id"),
			(gt, reg0, 1),
			
			(store_current_hours, ":hours_since_last_visit"),
			(troop_get_slot, ":last_visit_hour", ":troop_id", "slot_troop_last_talk_time"),
			(val_sub, ":hours_since_last_visit", ":last_visit_hour"),
			
			(gt, ":hours_since_last_visit", ":longest_time_without_visit"),
			(assign, ":longest_time_without_visit", ":hours_since_last_visit"),
			(assign, ":lady_not_visited_longest_time", ":troop_id"),
			(assign, ":visit_lady_location", ":location"),
		
		(try_end),
		
		(try_begin),
			(gt, ":lady_not_visited_longest_time", 0),
			(call_script, "script_add_notification_menu", "mnu_notification_lady_requests_visit", ":lady_not_visited_longest_time", ":visit_lady_location"),
		(try_end),
		
	(try_end),	
	]),
   
##################grueso tempered chief################gdw removed this because felt prisoner management skills was valuable investment of time and supplies. Also, agility removed as attribute
###chief asigna lvl de skill segun numero de tropas, para prisioneros#gdw new script added to increase prisoners with party size. This striggers prevents PM from ever increasing over 2 in first 20-30 hours of game
     (1 , #chief
   [
 #     (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
 #   (assign, ":num_men", 0),
 #   (try_for_range, ":i_stack", 0, ":num_stacks"),
 #     (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
 #     (val_add, ":num_men", ":stack_size"),
  #  (try_end),
 #     (try_begin),
 #      (lt, ":num_men", 50),
 #               (call_script, "script_troop_set_skill_level", "skl_prisoner_management", 1),
 #     (else_try),
 #      (gt, ":num_men", 49),
 #      (lt, ":num_men", 100),
#                (call_script, "script_troop_set_skill_level", "skl_prisoner_management", 2),
 #     (else_try),
 #      (gt, ":num_men", 99),
 #      (lt, ":num_men", 150),
 #               (call_script, "script_troop_set_skill_level", "skl_prisoner_management", 3),
 #     (else_try),
#       (gt, ":num_men", 149),
 #      (lt, ":num_men", 200),
 #               (call_script, "script_troop_set_skill_level", "skl_prisoner_management", 4),
#      (else_try),
  #     (gt, ":num_men", 179),
  #     (lt, ":num_men", 220),
  #              (call_script, "script_troop_set_skill_level", "skl_prisoner_management", 11),
  #    (else_try),
   #    (gt, ":num_men", 219),
  #     (lt, ":num_men", 280),
  #              (call_script, "script_troop_set_skill_level", "skl_prisoner_management", 12),
  #    (else_try),
  #     (gt, ":num_men", 279),#gdw
  #     (lt, ":num_men", 355),
  #              (call_script, "script_troop_set_skill_level", "skl_prisoner_management", 13),
   #   (else_try),
   #    (gt, ":num_men", 450),#gdw65
    #   (lt, ":num_men", 490),
    #            (call_script, "script_troop_set_skill_level", "skl_prisoner_management", 14),
   #   (else_try),
    #   (gt, ":num_men", 489),#gdw
   #    (call_script, "script_troop_set_skill_level", "skl_prisoner_management", 15),
     # (else_try),
      #          (call_script, "script_troop_set_skill_level", "skl_prisoner_management", 10),
     # (try_end),
    ]),
######prisioneros acaba
#####Ikaguia chief bardo entretenimiento acaba
   #entertainment party morale bonus
     (24, [
       (assign, ":entertain_bonus", 0),
       #companions
       (store_party_size_wo_prisoners, reg0, "p_main_party"),
       (try_begin),
           (gt, reg0, 1),
           (try_for_range, ":hero", companions_begin, companions_end),
               (main_party_has_troop,":hero"),
               (store_skill_level,":skill","skl_entertain",":hero"),
               (store_mul, reg0, ":skill", ":skill"),     #higher skill has bigger effect
               (val_add, ":entertain_bonus", reg0),
           (try_end),
           #player troop
           (store_skill_level,":skill","skl_entertain","trp_player"),
           (store_mul, reg0, ":skill", ":skill"),     #higher skill has bigger effect
           (val_add, ":entertain_bonus", reg0),
           #now get the bonus
           (assign, reg0, ":entertain_bonus"),
           (convert_to_fixed_point, reg0),
           (store_sqrt, ":entertain_bonus", reg0),
           (convert_from_fixed_point, ":entertain_bonus"),
           (val_mul, ":entertain_bonus", "$entertainement_on"), #normal kind is 1 but if it is an aewsome entertainement it will get a bonus (like playing lordly/royal musics)
           (val_div, ":entertain_bonus", 2),     #every x2  skill level gives a morale point (normally)
           #and apply it
           (try_begin),
               (gt, ":entertain_bonus", 0),
               (display_message, "@Your troops enjoy the entertainment you and your companions give them."),
               (call_script, "script_change_player_party_morale", ":entertain_bonus"),
           (else_try),
               (display_message, "@Your troops wish you and your companions would provide more entertainment."),
               (lt, "$entertainement_on", 1),
              # (call_script, "script_change_player_party_morale", -1), #Moto, if a player wantnt be bard, should we do him have entertain skill?
           (try_end),
       (try_end),    #party size > 1
       (assign, "$entertainement_on", 0),    #init for new day
   ]),
  
	#bardic reputation bonus
   #bardic reputation bonus
   # (48,[#(store_div, ":reputation", "$bardic_reputation", 1000),    MOTO tweak entertainment -- renown bump done in script_entertain_income now
        # (val_min, ":reputation", 1),
        # (val_add, ":reputation", 1),
        # (troop_get_slot, ":old_reputation", "trp_player", "slot_troop_renown"),
        # (store_mul, ":new_reputation", ":old_reputation", ":reputation"),    #MOTO: multiply? $bardic_reputation will have an EXPONENTIAL effect...
        # (troop_set_slot, "trp_player", "slot_troop_renown", ":new_reputation"),
        # (store_sub, reg12, ":new_reputation", ":old_reputation"),
        # (try_begin),
           # (gt, reg12, 0),
           # (display_message, "@You gained {reg12} renown over the last two days from your bardic reputation.", 0x33ff33),
        # (else_try),
           # (lt, reg12, 0),
           # (val_mul, reg12, -1),
           # (display_message, "@You lost {reg12} renown over the last two days from your bardic reputation.", 0xff3333),
        # (try_end),
        # ]),
  
	#entertainment effects other than party morale NOW a script called from menu
	# (12,	[(ge, "$entertainement_on", 1),
		 # (assign, ":income_rate", "$entertain_income_rate"),
		 # (assign, ":income_type", "$entertain_income_type"),
		 # (assign, ":income_type2", "$entertain_income_type2"),
		 
		 # (store_mul, ":max", ":income_rate", 1),
		 # (store_skill_level,":skill_lvl","skl_entertain","trp_player"),
		 # (val_add, ":max", ":skill_lvl"),
		 # (val_mul, ":max", "$entertainement_on"),
		 
		 # (store_mul, ":min", ":income_rate", -1),
		 # (val_div, ":min", 2),
		 # (val_div, ":min", "$entertainement_on"),
		 
		 # (store_random_in_range, ":income", ":min", ":max"),
		 # (store_div, ":reputation", "$bardic_reputation", 400),
		 # (val_min, ":reputation", 1),
		 # (val_add, ":reputation", 1),
		 # (val_mul, ":income", ":reputation"),
		 # (val_sub, ":income", ":reputation"),
		 # (call_script, "script_entertain_income", ":income", ":income_type"),
		 # (call_script, "script_entertain_income", ":income", ":income_type2"),
		 # ]),
###skill de entretenimiento acaba bardo
###rigale chief
     (4 , #rigale begging
   [
   (troop_get_slot, ":player_renown","trp_player", "slot_troop_renown"),
   
   (str_store_string,s2,"@0",),
   (str_store_string,s3,"@0",),
   
   (try_begin),
	   (eq,"$begging_action_started",1),
	   (store_random_in_range,":honor_loss",1,6),
	   (try_begin),
		   (eq,":honor_loss",1),
		   (val_sub,"$player_honor",1),
		   (str_store_string,s2,"@1",),		   
	   (try_end),
   
	   (store_random_in_range,":renown_loss",1,6),
	   (try_begin),
		   (eq,":renown_loss",1),
		   (val_sub,":player_renown",1),
		   (str_store_string,s3,"@1",),		   
			(troop_set_slot, "trp_player", "slot_troop_renown", ":player_renown"),
		(try_end),
		
	  (store_random_in_range,reg0,0,11), #gold gain
		(display_message,"@You gain {reg0} scillingas from begging. You lose {s2} reputation and {s3} renown"),	  
		(troop_add_gold,"trp_player",reg0),

   (try_end),
   ]),


   ( 1, #rigale ambush notices
  [
	(try_begin),
		(eq, "$ambush_set_by_player", 1),
		
		(try_begin),
		(eq, "$type_of_ambushing_success", 1),		
		 (store_random_in_range,":show_message",1,16),
			(try_begin),
				(lt,":show_message",2),
				(display_message,"@You have very bad feelings about this ambush...",0xFF0000),
			 (else_try),
				(is_between,":show_message",2,6),
				(display_message,"@You have bad feelings about this ambush.",0xFF9999),				
			 (else_try),
				(is_between,":show_message",6,13),
				(display_message,"@You have good feelings about this ambush.",0xCCFF33),		 
			 (else_try),
				(gt,":show_message",13),
				(display_message,"@You have very good feelings about this ambush.",0x66FF33),		 
			(try_end),		 
		(else_try),
		(eq, "$type_of_ambushing_success", 2),		
		 (store_random_in_range,":show_message",1,16),
			(try_begin),
				(lt,":show_message",2),
				(display_message,"@You have very bad feelings about this ambush...",0xFF0000),
			 (else_try),
				(is_between,":show_message",2,7),
				(display_message,"@You have bad feelings about this ambush.",0xFF9999),				
			 (else_try),
				(is_between,":show_message",7,14),
				(display_message,"@You have good feelings about this ambush.",0xCCFF33),		 
			 (else_try),
				(gt,":show_message",14),
				(display_message,"@You have very good feelings about this ambush.",0x66FF33),		 
			(try_end),		 
		(else_try),
		(eq, "$type_of_ambushing_success", 3),		
		 (store_random_in_range,":show_message",1,16),
			(try_begin),
				(lt,":show_message",2),
				(display_message,"@You have very bad feelings about this ambush...",0xFF0000),
			 (else_try),
				(is_between,":show_message",2,9),
				(display_message,"@You have bad feelings about this ambush.",0xFF9999),				
			 (else_try),
				(is_between,":show_message",9,14),
				(display_message,"@You have good feelings about this ambush.",0xCCFF33),		 
			 (else_try),
				(gt,":show_message",14),
				(display_message,"@You have very good feelings about this ambush.",0x66FF33),		 
			(try_end),		 
		(else_try),
		(eq, "$type_of_ambushing_success", 4),		
		 (store_random_in_range,":show_message",1,16),
			(try_begin),
				(lt,":show_message",4),
				(display_message,"@You have very bad feelings about this ambush...",0xFF0000),
			 (else_try),
				(is_between,":show_message",4,10),
				(display_message,"@You have bad feelings about this ambush.",0xFF9999),				
			 (else_try),
				(is_between,":show_message",10,14),
				(display_message,"@You have good feelings about this ambush.",0xCCFF33),		 
			 (else_try),
				(gt,":show_message",14),
				(display_message,"@You have very good feelings about this ambush.",0x66FF33),		 
			(try_end),		 
		 (try_end),
		 
		 
		 (rest_for_hours_interactive,2,1,1),
	(try_end),
	]
  ), 

  
  ( 1, #rigale sneaking notices
  [
	(try_begin),
		(eq, "$sneaking_set_by_player", 1),
		
		(try_begin),
		(eq, "$type_of_sneaking_success", 1),		
		 (store_random_in_range,":show_message",1,16),
			(try_begin),
				(lt,":show_message",2),
				(display_message,"@You have very bad feelings about this sneaking...",0xFF0000),
			 (else_try),
				(is_between,":show_message",2,6),
				(display_message,"@You have bad feelings about this sneaking.",0xFF9999),				
			 (else_try),
				(is_between,":show_message",6,13),
				(display_message,"@You have good feelings about this sneaking.",0xCCFF33),		 
			 (else_try),
				(gt,":show_message",13),
				(display_message,"@You have very good feelings about this sneaking.",0x66FF33),		 
			(try_end),		 
		(else_try),
		(eq, "$type_of_sneaking_success", 2),		
		 (store_random_in_range,":show_message",1,16),
			(try_begin),
				(lt,":show_message",2),
				(display_message,"@You have very bad feelings about this sneaking...",0xFF0000),
			 (else_try),
				(is_between,":show_message",2,7),
				(display_message,"@You have bad feelings about this sneaking.",0xFF9999),				
			 (else_try),
				(is_between,":show_message",7,14),
				(display_message,"@You have good feelings about this sneaking.",0xCCFF33),		 
			 (else_try),
				(gt,":show_message",14),
				(display_message,"@You have very good feelings about this sneaking.",0x66FF33),		 
			(try_end),		 
		(else_try),
		(eq, "$type_of_sneaking_success", 3),		
		 (store_random_in_range,":show_message",1,16),
			(try_begin),
				(lt,":show_message",2),
				(display_message,"@You have very bad feelings about this sneaking...",0xFF0000),
			 (else_try),
				(is_between,":show_message",2,9),
				(display_message,"@You have bad feelings about this sneaking.",0xFF9999),				
			 (else_try),
				(is_between,":show_message",9,14),
				(display_message,"@You have good feelings about this sneaking.",0xCCFF33),		 
			 (else_try),
				(gt,":show_message",14),
				(display_message,"@You have very good feelings about this sneaking.",0x66FF33),		 
			(try_end),		 
		(else_try),
		(eq, "$type_of_sneaking_success", 4),		
		 (store_random_in_range,":show_message",1,16),
			(try_begin),
				(lt,":show_message",4),
				(display_message,"@You have very bad feelings about this sneaking...",0xFF0000),
			 (else_try),
				(is_between,":show_message",4,10),
				(display_message,"@You have bad feelings about this sneaking.",0xFF9999),				
			 (else_try),
				(is_between,":show_message",10,14),
				(display_message,"@You have good feelings about this sneaking.",0xCCFF33),		 
			 (else_try),
				(gt,":show_message",14),
				(display_message,"@You have very good feelings about this sneaking.",0x66FF33),		 
			(try_end),		 
		 (try_end),
	(try_end),	 

	
	]
  ),

      ( 1, #rigale peasantry timelapse
  [

  
  
  
  (try_begin),
        (this_or_next|eq, "$g_player_is_captive", 1),
        (this_or_next|party_slot_eq, "$current_town", "slot_village_state", svs_being_raided),
        (party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),

        # (gt,"$g_work_for_village_ongoing",1),        
               (gt,"$g_work_for_village_ongoing",0),    #MOTO chief avoid      successful conclusion
  (assign,"$g_work_for_village_ongoing", 0),
		(rest_for_hours,0,0,0),
     	(jump_to_menu,"mnu_village_basic_work"),
  (else_try),
		 (gt,"$g_work_for_village_ongoing",1),
		 (val_sub, "$g_work_for_village_ongoing", 1),
		 (store_random_in_range,":show_overrall_message",1,5),
		 (try_begin),		 
			 (eq,":show_overrall_message",1),
			(display_message,"@You keep working hard for this village...",0x66CC33),		 
		 (try_end),
		 		 (rest_for_hours,2,5,0),
	(else_try), 
		 (eq,"$g_work_for_village_ongoing",1),
		 (display_message,"@Your strenuous village work ends.",),
		 (rest_for_hours,0,0,0),
		 (val_sub, "$g_work_for_village_ongoing", 1),
		(jump_to_menu,"mnu_village_basic_work"),
	 (try_end),	
	]
  ),
###chief acaba rigale

  #TEMPERED        chief ###################  CHANGE CONTEXT MENU FOR PARTY PICKING  ##############################

  (0, [	(map_free),
		(eq,"$pick_party",1),
		(assign,"$pick_party",0),
		(assign,"$party_picker_active",1),
		(dialog_box,"str_party_picker_attack","str_party_picker_title"),
		(disable_party,"p_main_party"),
       ]),	
	   
  (0, [	(map_free),
		(eq,"$party_picker_active",1),
		(gt,"$message_party_target",0),
		(assign,"$party_picker_active",0),
		(enable_party,"p_main_party"),
		(start_presentation,"prsnt_view_message"),
       ]),

#TEMPERED    chief      ############################  SPEND TIME AFTER BATTLE BURYING THE DEAD AND LOOTING #####################################
	   
  (0, [	(map_free),
		(this_or_next|eq,"$bury_dead",1),
		(eq,"$loot_dead",1),
		(party_get_battle_opponent, ":in_battle", "p_main_party"),
		(le,":in_battle",0),
		(assign,":start_bonfire",0),
		(try_begin),
			(eq,"$bury_dead",1),
			(eq,"$loot_dead",1),
			(assign,":time_after_battle",3),
			(display_message,"@                                Looting and burying the dead."),
			(assign,":start_bonfire",1),
			(gt,"$wagon_attached",0),
			(call_script,"script_add_wagon_inventory"),
		(else_try),
			(eq,"$bury_dead",1),
			(eq,"$loot_dead",0),
			(assign,":time_after_battle",2),
			(assign,":start_bonfire",1),
			(display_message,"@                                      Burying the dead."),
		(else_try),
			(eq,"$bury_dead",0),
			(eq,"$loot_dead",1),
			(assign,":time_after_battle",1),
			(display_message,"@                                       Looting the dead."),
			(gt,"$wagon_attached",0),
			(call_script,"script_add_wagon_inventory"),
		(try_end),
		(assign, "$g_player_icon_state", pis_camping),
		(party_set_slot,"p_main_party","slot_party_entrenched",0),
		(assign,"$g_camp_mode", 1),
		(rest_for_hours,":time_after_battle",0,1),
		(assign,"$bury_dead",0),
		(assign,"$loot_dead",0),
		(try_begin),
			(eq,":start_bonfire",1),
			(set_spawn_radius, 1),
			(spawn_around_party, "p_main_party", "pt_funeral_pyre"),
			(assign, ":funeral_pyre", reg0),
			(store_current_hours,":cur_hour"),
			(val_add,":cur_hour",8),
			(party_set_slot, ":funeral_pyre", "slot_village_smoke_added", ":cur_hour"),
			(party_add_particle_system, ":funeral_pyre", "psys_map_village_fire"),
			(party_add_particle_system, ":funeral_pyre", "psys_map_village_fire_smoke"),
		(try_end),
       ]),  
 
#TEMPERED  CLEAN UP FUNERAL PYRES
  (3, [	(store_random_party_of_template,":party_no","pt_funeral_pyre"),
		(gt,":party_no",0),
		(store_current_hours,":cur_hour"),
		(party_get_slot,":end_hour",":party_no","slot_village_smoke_added"),
		(gt,":cur_hour",":end_hour"),
		(party_clear_particle_systems, ":party_no"),
		(party_clear,":party_no"),
		(remove_party,":party_no"),
       ]),

	
#TEMPERED       chief  #########################  CHECK FOR ENTRENCHMENT FINISHED  ##############################

  (0, [	(party_get_slot,":entrenched","p_main_party","slot_party_entrenched"),
		(eq,"$g_camp_mode", 1),
		(eq,":entrenched",-1),
		(store_current_hours,":cur_hour"),
		(try_begin),
			(ge,":cur_hour","$entrench_time"),
			(set_spawn_radius,0),
			(spawn_around_party,"p_main_party","pt_entrench"),
			(assign,"$current_camp_party",reg0),
			(party_set_slot,"$current_camp_party","slot_village_state",1),
			(party_set_slot,"$current_camp_party","slot_party_type",spt_entrenchment),
			(party_set_slot,"p_main_party","slot_party_entrenched",1),
			(display_message,"@_Camp defenses have been completed."),
			(assign,"$entrench_time",0),
			(jump_to_menu,"mnu_camp"),
		(try_end),
       ]),
#TEMPERED                     ########################      CHECK FOR SIEGE CAMP COMPLETE  OR OUT OF RANGE   ##################################
	(0,	[	(party_slot_eq,"p_main_party","slot_party_siege_camp",-1),
			(store_current_hours,":cur_hour"),
			(try_begin),
				(lt, "$g_player_besiege_town", 1),
				(party_set_slot,"p_main_party","slot_party_siege_camp",0),
				(assign,"$entrench_time",0),
			(else_try),				
				(gt, "$g_player_besiege_town", 0),
				(store_distance_to_party_from_party, ":distance", "$g_player_besiege_town", "p_main_party"),
				(try_begin),
					(le,":distance",3),
					(ge,":cur_hour","$entrench_time"),
					(party_set_slot,"p_main_party","slot_party_siege_camp",1),
					(assign,"$entrench_time",0),
				(else_try),
					(gt,":distance",3),
					(party_set_slot,"p_main_party","slot_party_siege_camp",0),
					(display_message,"@ Your siege camp was destroyed while you were away!"),
					(assign,"$entrench_time",0),
				(try_end),
			(try_end),
		]),
#TEMPERED CHECK FOR SIEGE CAMP OUT OF RANGE OR ABANDONED		
	(1,	[	(party_slot_eq,"p_main_party","slot_party_siege_camp",1),
			(try_begin),
				(lt, "$g_player_besiege_town", 1),
				(party_set_slot,"p_main_party","slot_party_siege_camp",0),
			(else_try),				
				(gt, "$g_player_besiege_town", 0),
				(store_distance_to_party_from_party, ":distance", "$g_player_besiege_town", "p_main_party"),
				(gt,":distance",3),
				(party_set_slot,"p_main_party","slot_party_siege_camp",0),
				(display_message,"@ Your siege camp was destroyed while you were away!"),
			(try_end),
		]),

#TEMPERED                    ##########################           CHECK FOR NO LONGER ENTRENCHED    ##########################

  (0, [ (eq,"$g_player_icon_state",pis_normal),
		(eq, "$g_camp_mode", 0),#not camping
		(try_begin),
			(party_slot_eq,"p_main_party","slot_party_entrenched",1), #entrenched			
			(party_set_slot,"p_main_party","slot_party_entrenched",0), #not entrenched
			#try_begin),#gdw trying to solve compilation error 1 try_end missing"
				#(party_slot_eq,"$current_camp_party","slot_village_state",1),#Tempered check to see if player just left entrenchment
				(party_set_slot,"$current_camp_party","slot_village_state",2),
				(store_current_hours,":cur_hour"),
				(val_add,":cur_hour",72),
				(party_set_slot,"$current_camp_party","slot_village_smoke_added",":cur_hour"),
				(party_add_particle_system, "$current_camp_party", "psys_map_village_fire_smoke"),
			#try_end),
		(else_try),
			(party_slot_eq,"p_main_party","slot_party_entrenched",-1), #working on entrenchment
			(party_set_slot,"p_main_party","slot_party_entrenched",0), #not entrenched
		(try_end),	
		(assign,"$current_camp_party",-1),
       ]),
#TEMPERED                    ##########################         Deteriorate abandoned entrenchments    ##########################

  (3, [ (try_for_parties,":current_party"),
			(party_slot_eq,":current_party","slot_party_type",spt_entrenchment),
			(party_slot_eq,":current_party","slot_village_state",2),
			(party_get_slot,":end_hour",":current_party","slot_village_smoke_added"),
			(store_current_hours,":cur_hour"),
			(gt,":cur_hour",":end_hour"),
			(party_clear_particle_systems, ":current_party"),
			(remove_party,":current_party"),
		(try_end),
		#(party_set_flags, ":new_camp", pf_icon_mask, 1),
       ]),   

#TEMPERED chief  QUESTION BOX FOR ATTACK PARTY BRIBERY
   
(ti_question_answered, 
	[	(store_trigger_param_1,":answer"),
		(try_begin),
			(eq,":answer",0),
			(gt,"$attack_party_question",0),
			(assign,":party_no","$attack_party_question"),
			(store_troop_gold,":cur_wealth","trp_player"),
			(party_get_slot,":target_party",":party_no","slot_message_target"),
			(party_get_slot,":target_party_2",":party_no","slot_message_target_2"),
			(party_get_slot, ":party_type",":target_party_2","slot_party_type"),
			(party_stack_get_troop_id, ":leader",":target_party",0),
			(assign,":ai_state",spai_engaging_army),
			(assign,"$attack_party_answer",5),
			(try_begin),
				(eq,":party_type",spt_village),
				(assign,":ai_state",spai_raiding_around_center),
				(assign,"$attack_party_answer",2),
			(else_try),
				(eq,":party_type",spt_town),
				(assign,":ai_state",spai_besieging_center),
				(assign,"$attack_party_answer",3),
			(else_try),
				(eq,":party_type",spt_castle),
				(assign,":ai_state",spai_besieging_center),
				(assign,"$attack_party_answer",4),
			(try_end),	
			(try_begin),							
				(ge,":cur_wealth","$bribe_amount"),
				(troop_remove_gold,"trp_player","$bribe_amount"),
				(troop_add_gold,":leader","$bribe_amount"),
				(party_set_slot,  ":target_party", "slot_party_commander_party",-1),
				(call_script,"script_party_set_ai_state",":target_party",":ai_state",":target_party_2"),
				(party_set_slot, ":target_party", "slot_party_follow_me", 0),
				(party_set_flags, ":target_party", pf_default_behavior, 1),
				(store_current_hours,":cur_hour"),
				(store_add,":end_time",":cur_hour",24),				
				(party_set_slot,":target_party","slot_party_hired",":end_time"),				
			(else_try),
				(lt,":cur_wealth","$bribe_amount"),			
				(party_stack_get_troop_id, ":leader", ":target_party", 0),
				(assign,"$unable_to_pay",1),
				(assign,"$attack_party_answer",-1),
				(call_script, "script_change_player_relation_with_troop", ":leader", -1),
			(try_end),			
		(else_try),
			(eq,":answer",1),
			(gt,"$attack_party_question",0),
			(assign,"$attack_party_answer",1),
		(try_end),
		(assign,"$attack_party_question",-1),
	]),
				
#TEMPERED  chief  #########################        CHECK FOR MESSENGER ARRIVAL        #########################

  (0,  
   [ 	(store_random_party_of_template,":party_no","pt_personal_messenger"),
		(assign,":continue",0),
		(try_begin),
			(party_is_active,":party_no"),
			(party_is_in_any_town,":party_no"),			
			(party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
			(party_set_ai_object,":party_no","p_main_party"),
			(assign,":continue",1),
		(try_end),
		(eq,":continue",1),
		(call_script,"script_personal_messenger",":party_no"),
    ]),  

#TEMPERED   chief          CHECK BUILDING WAGON PROGRESS
  (1, [	
		(eq,"$g_camp_mode", 1),
		(ge,"$building_wagon",1),
		(val_add,"$building_wagon",1),
		(try_begin),
			(ge,"$building_wagon",5),
			(assign,"$building_wagon",0),
			(assign,"$wagon_attached",1),
			(assign,"$owns_wagon",1),
			(display_message,"@_Your troops have finished building a new supply wagon."),
		(try_end),
       ]),
	   
#TEMPERED   chief    ##########################    CHECK FOR LOOT WAGON TOWN ARRIVAL          ###############################

  (3,  
   [ 	(le,"$wagon_attached",0),
		(party_get_slot,":party_no","p_main_party","slot_party_loot_wagon"),
		(party_get_slot,":town_no","p_main_party","slot_loot_wagon_target"),
		(try_begin),
			(party_is_active,":party_no"),
			(party_is_in_town,":party_no",":town_no"),
			(party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
			(party_set_ai_object,":party_no","p_main_party"),
			(party_set_bandit_attraction, ":party_no",60),
			(call_script,"script_loot_wagon_trade",":party_no"),			
		(try_end),		
    ]), 
	
#Tempered     chief      ####################################### CHECK FOR SPY ENTERING TOWN ###############################################

 
  (1.5,  
   [ 	(store_random_party_of_template,":spy_party_id","pt_spy_party"),
		(party_get_slot,":cur_center",":spy_party_id","slot_spy_target_town"),
		(gt,":cur_center",0),
		(try_begin),
			(party_is_in_town,":spy_party_id",":cur_center"),
			(str_store_party_name,s5,":cur_center"),
			(store_current_hours,":cur_hour"),
			(party_set_slot,":cur_center","slot_spy_in_town",":cur_hour"),
			(remove_party,":spy_party_id"),
			(add_party_note_from_sreg,":cur_center",2,"str_spy_infiltrating",0),
			(display_message,"str_spy_infiltrating"),
		(try_end),
		(str_clear,s5),
    ]),

#Tempered     chief  ##############   CHECK FOR HIRED PARTIES CONTRACT END AND DUEL EXPIRATION  ##########################

 
  (2,  
   [ 	(store_current_hours,":cur_hour"),
		(try_begin),
			(gt,":cur_hour",18),
			(try_for_parties,":party_no"),
				(neq,":party_no","p_main_party"),
				(party_get_slot,":hire_time_end",":party_no","slot_party_hired"),
				(try_begin),
					(party_slot_eq,":party_no","slot_party_type",spt_kingdom_hero_party),
					(party_stack_get_troop_id, ":leader", ":party_no", 0),					
					(troop_get_slot,":duel_challenger_expire",":leader","slot_troop_duel_challenger"),
					(troop_get_slot,":duel_challenged_expire",":leader","slot_troop_duel_challenged"),
					(party_get_battle_opponent,":in_battle",":party_no"),
					(get_party_ai_current_behavior,":cur_behavior",":party_no"),
					(party_is_active,":party_no"),
					(try_begin),
						(troop_slot_ge,":leader","slot_troop_duel_challenger",1),
						(try_begin),
							(gt,":duel_challenger_expire",":cur_hour"),
							(party_get_attached_to, ":attached_to_party", ":party_no"),
							(try_begin),
								(is_between, ":attached_to_party", centers_begin, centers_end),
								(party_detach, ":party_no"),
							(try_end),
							(party_get_slot,":duel_location",":party_no","slot_message_target_2"),
							(party_get_position,pos1,":duel_location"),
							(map_get_land_position_around_position,pos2,pos1,1),
							(party_set_ai_behavior,":party_no",ai_bhvr_travel_to_point), 
							(party_set_ai_target_position,":party_no",pos2),
						(else_try),
							(lt,":duel_challenger_expire",":cur_hour"),
							(this_or_next|eq,":cur_behavior",ai_bhvr_travel_to_party),
							(eq,":cur_behavior",ai_bhvr_attack_party),
							(troop_set_slot,":leader","slot_troop_duel_challenger",-1),
							(party_set_slot,":party_no","slot_message_target_2",-1),
							(str_store_troop_name,s1,":leader"),
							(display_message,"@ Your duel with {s1} was canceled due to unforseen circumstances."),
						(else_try),
							(lt,":duel_challenger_expire",":cur_hour"),
							(gt,":in_battle",0),
							(troop_set_slot,":leader","slot_troop_duel_challenger",-1),
							(party_set_slot,":party_no","slot_message_target_2",-1),
							(str_store_troop_name,s1,":leader"),
							(display_message,"@ Your duel with {s1} was canceled due to unforseen circumstances."),
						(else_try),
							(lt,":duel_challenger_expire",":cur_hour"),
							(call_script,"script_change_troop_renown","trp_player",-5),
							(call_script,"script_change_troop_renown",":leader",5),
							(call_script,"script_change_player_relation_with_troop",":leader",-1),
							(call_script,"script_change_player_honor",-2),
							(store_faction_of_party,":faction_no",":party_no"),
							(call_script,"script_get_closest_walled_center_of_faction",":party_no",":faction_no"),
							(assign,":ai_object",reg0),
							(call_script,"script_party_set_ai_state",":party_no",spai_retreating_to_center,":ai_object"),
							(troop_set_slot, ":leader", "slot_troop_duel_challenger", -1),
							(party_set_slot,":party_no","slot_message_target_2",-1),
							(str_store_troop_name,s1,":leader"),
							(dialog_box,"str_missed_duel"),
							(call_script, "script_objectionable_action", tmt_aristocratic, "str_missed_duel_npc"),
						(try_end),
					(else_try),
						(troop_slot_ge,":leader","slot_troop_duel_challenged",1),
						(try_begin),
							(gt,":duel_challenged_expire",":cur_hour"),
							(party_get_slot,":duel_location",":party_no","slot_message_target_2"),
							(party_get_position,pos1,":duel_location"),
							(map_get_land_position_around_position,pos2,pos1,1),
							(party_set_ai_behavior,":party_no",ai_bhvr_travel_to_point), 
							(party_set_ai_target_position,":party_no",pos2),
						(else_try),
							(lt,":duel_challenged_expire",":cur_hour"),
							(this_or_next|eq,":cur_behavior",ai_bhvr_travel_to_party),
							(eq,":cur_behavior",ai_bhvr_attack_party),
							(troop_set_slot,":leader","slot_troop_duel_challenged",-1),
							(party_set_slot,":party_no","slot_message_target_2",-1),
							(str_store_troop_name,s1,":leader"),
							(display_message,"@ Your duel with {s1} was canceled due to unforseen circumstances."),
						(else_try),
							(lt,":duel_challenged_expire",":cur_hour"),
							(gt,":in_battle",0),
							(troop_set_slot,":leader","slot_troop_duel_challenged",-1),
							(party_set_slot,":party_no","slot_message_target_2",-1),
							(str_store_troop_name,s1,":leader"),
							(display_message,"@ Your duel with {s1} was canceled due to unforseen circumstances."),
						(else_try),
							(lt,":duel_challenged_expire",":cur_hour"),
							(call_script,"script_change_troop_renown","trp_player",-5),
							(call_script,"script_change_troop_renown",":leader",5),
							(call_script,"script_change_player_relation_with_troop",":leader",-1),
							(call_script,"script_change_player_honor",-2),
							(store_faction_of_party,":faction_no",":party_no"),
							(call_script,"script_get_closest_walled_center_of_faction",":party_no",":faction_no"),
							(assign,":ai_object",reg0),
							(call_script,"script_party_set_ai_state",":party_no",spai_retreating_to_center,":ai_object"),
							(troop_set_slot, ":leader", "slot_troop_duel_challenged", -1),
							(party_set_slot,":party_no","slot_message_target_2",-1),
							(str_store_troop_name,s1,":leader"),
							(dialog_box,"str_missed_duel"),
							(call_script, "script_objectionable_action", tmt_aristocratic, "str_missed_duel_npc"),
						(try_end),
					(try_end),
				(try_end),
				(gt,":hire_time_end",16),
				(try_begin),
					(gt,":cur_hour",":hire_time_end"),
					(store_faction_of_party,":faction_no",":party_no"),
					(call_script,"script_get_closest_walled_center_of_faction",":party_no",":faction_no"),
					(assign,":ai_object",reg0),
					(call_script,"script_party_set_ai_state",":party_no",spai_retreating_to_center,":ai_object"),
					(str_store_party_name,s1,":party_no"),
					(display_message,"@ Your contract with {s1} has expired."),
					(party_set_slot,":party_no","slot_party_hired",-1),
				(try_end),
			(try_end),
			(str_clear,s1),
		(try_end),
			
    ]),	

		
#Tempered  chief      #######################################  SPY UPDATES EVERY 12 HOURS ################################################
	(12,
		[
			(try_for_range,":cur_center",centers_begin,centers_end),
				
				(str_clear,s5),				
				(store_current_hours,":cur_hour"),
				(party_get_slot,":spy_days",":cur_center","slot_spy_in_town"),
				(store_faction_of_party,":cur_center_fac",":cur_center"),
				(store_sub,":total_time",":cur_hour",":spy_days"),
				(try_begin),
					(eq,":total_time",":cur_hour"),
					(assign,":total_time",0),
				(try_end),
				(store_div,":days",":total_time",24),
				(assign,reg5,":days"),
				(party_get_slot,":spy_mission",":cur_center","slot_spy_sabotage"),
				(party_get_slot,":poison_count",":cur_center","slot_well_poisoned"),
				(party_get_slot,":spies_deployed","p_main_party","slot_spies_deployed"),
				(assign,":kill_modified",0),
				(assign,":total_relation",0),
					(try_begin),
						(ge,":poison_count",1),
						(call_script,"script_poison_well",":cur_center"),
						(party_set_slot,":cur_center","slot_well_poisoned",0),
					(try_end),
					(try_begin),
						(ge,":spy_days",1),
						#(assign,reg5,":days"),
						(str_store_party_name,s5,":cur_center"),
						(party_get_slot,":p_type",":cur_center","slot_party_type"),
						(store_relation,":cur_relation","fac_player_faction",":cur_center_fac"),						
						(party_get_slot,":center_relation",":cur_center","slot_center_player_relation"),
						(store_random_in_range,":kill_chance",5,300),
						(store_add,":total_relation",":center_relation",":cur_relation"),
							(try_begin),
								(eq,":p_type",2),
								(val_sub,":kill_chance",20),
							(else_try),
								(ge,":p_type",3),
								(val_add,":kill_chance",30),
							(try_end),
							(try_begin),
								(ge,":spy_mission",1),
								(val_sub,":kill_chance",30),
							(try_end),
							(try_begin),
								(eq,":spy_mission",4),
								(val_sub,":kill_chance",20),
							(try_end),
						(store_add,":kill_modified",":kill_chance",":total_relation"),
							(try_begin),
								(le,":kill_modified",15),
								(party_set_slot,":cur_center","slot_spy_in_town",0),
								(party_set_slot,":cur_center","slot_spy_sabotage",0),
								(val_sub,":spies_deployed",1),
								(party_set_slot,"p_main_party","slot_spies_deployed",":spies_deployed"),
								(party_get_slot, ":lord_troop_id", ":cur_center", "slot_town_lord"),
								(call_script, "script_change_player_relation_with_troop", ":lord_troop_id", -3),
								(call_script, "script_change_player_relation_with_center", ":cur_center", -5),
								(dialog_box,"str_spy_captured"),
							(else_try),
								(ge,":kill_modified",16),
									#(display_message,"@Your spy has been in {s5} for {reg5} days."),
									(try_begin),
										(is_between,":p_type",3,5),
										(le,":center_relation",20),
										(ge,":days",2),
										(call_script, "script_change_player_relation_with_center", ":cur_center",1),
									(try_end),
									(try_begin), #Tempered begin check for sabotage missions
										(ge,":spy_mission",1),
											(try_begin),
												(eq,":spy_mission",1), #Tempered poison well
												(call_script,"script_poison_well",":cur_center"),
												(party_set_slot,":cur_center","slot_spy_sabotage",0),
												(party_set_slot,":cur_center","slot_well_poisoned",1),
												(display_message,"@Your spy in {s5} has successfully poisoned the well."),
											(else_try),
												(eq,":spy_mission",2), #Tempered poison food
												(call_script,"script_poison_food",":cur_center"),
												(party_set_slot,":cur_center","slot_spy_sabotage",0),
													(try_begin),
														(le,":p_type",3),
														(display_message,"@Rats have infested the food stocks in {s5}."),
													(else_try),
														(eq,":p_type",4),
														(display_message,"@A pox has inflicted the cattle herds of {s5}."),
													(try_end),
											(else_try),
												(eq,":spy_mission",3), #Tempered cause unrest
												(call_script,"script_unrest_sabotage",":cur_center"),
												(party_set_slot,":cur_center","slot_spy_sabotage",0),
													(try_begin),
														(eq,":p_type",3),
														(display_message,"@Civil unrest in {s5} is having an adverse effect on the town economy."),
													(else_try),
														(eq,":p_type",4),
														(display_message,"@Farmers in {s5} are rioting."),
													(try_end),
											(else_try),
												(eq,":spy_mission",4), #Tempered RESCUE PRISONER SPY MISSION
												(party_set_slot,":cur_center","slot_spy_sabotage",0),
											(try_end),
									(try_end),
								
							(try_end),
						(call_script, "script_update_center_recon_notes", ":cur_center"),
					(try_end),
			(try_end),
			(str_clear,s5),
		]
	),
	
#####TEMPERED ADJUST COMMONER TRUST EVERY 7 DAYS 
  (24 * 7,
   [	(set_show_messages,0),
		(try_begin),
			(is_between,"$commoner_trust",10,100),
			(val_sub,"$commoner_trust",1),
##		(else_try),
##			(is_between,"$commoner_trust",-79,-30),
##			(val_add,"$commoner_trust",1),
		(try_end),
		(try_for_range,":cur_village",villages_begin,villages_end),
			(try_begin),
				(gt,"$commoner_trust",40),
				(call_script, "script_change_player_relation_with_center", ":cur_village",1),
##			(else_try),
##				(lt,"$commoner_trust",-40),
##				(call_script, "script_change_player_relation_with_center", ":cur_village",-1),
			(try_end),
		(try_end),
		(set_show_messages,1),
    ]),   
#tempered chief  acaba   ##########
#################grueso tempered chief acaba#################

 #Pay day.
 (24 * 7,
  [
    ##diplomacy chief begin
    (store_current_hours, "$g_next_pay_time"),
    (val_add, "$g_next_pay_time", 24 * 7),
    ##diplomacy end
    (assign, "$g_presentation_lines_to_display_begin", 0),
    (assign, "$g_presentation_lines_to_display_end", 15),
    (assign, "$g_apply_budget_report_to_gold", 1),
    # (try_begin),
  #  (this_or_next|eq, "$freelancer_state", 1), # Freelancer - Allow normal budget presentation to fire chief
     (eq, "$g_infinite_camping", 0),
      (start_presentation, "prsnt_budget_report"),
    # (try_end),
    # (try_begin), #bas chief anade
       # (gt, "$g_player_debt_to_party_members", 0),    MOTO presentation doesn't start until AFTER this trigger (so do there) chief
       # (display_message, "@Your troops are unpaid!  Morale has dropped.",0xFFFFAAAA),
       # (call_script, "script_change_player_party_morale", -25),
   # (try_end), #bas chief acaba
   # (assign, "$g_cur_week_half_daily_wage_payments", 0),    MOTO done in presentation #Reseting the weekly half wage payments
   ]),
  # Oath fulfilled -- ie, mercenary contract expired?
  
  (24,
   [
      (le, "$auto_menu", 0),
      (gt, "$players_kingdom", 0),
      (neq, "$players_kingdom", "fac_player_supporters_faction"),
      (eq, "$player_has_homage", 0),
	  
	  (troop_get_slot, ":player_spouse", "trp_player", "slot_troop_spouse"),
	  
	  #A player bound to a kingdom by marriage will not have the contract expire. This should no longer be the case, as I've counted wives as having homage, but is in here as a fallback
	  (assign, ":player_has_marriage_in_faction", 0),
	  (try_begin),
		(is_between, ":player_spouse", active_npcs_begin, active_npcs_end),
		(store_faction_of_troop, ":spouse_faction", ":player_spouse"),
		(eq, ":spouse_faction", "$players_kingdom"),
	    (assign, ":player_has_marriage_in_faction", 1),
	  (try_end),
	  (eq, ":player_has_marriage_in_faction", 0),
	  
      (store_current_day, ":cur_day"),
      (gt, ":cur_day", "$mercenary_service_next_renew_day"),
      (jump_to_menu, "mnu_oath_fulfilled"),
    ]),

  # Reducing luck by 1 in every 180 hours
  (180,
   [
     (val_sub, "$g_player_luck", 1),
     (val_max, "$g_player_luck", 0),
    ]),

	#courtship reset
  (72,
   [
     (assign, "$lady_flirtation_location", 0),
    ]),

	#reset time to spare
  (4,
   [
     (assign, "$g_time_to_spare", 1),

    (try_begin),
		(troop_slot_ge, "trp_player", "slot_troop_spouse", active_npcs_begin),
		(assign, "$g_player_banner_granted", 1),
	(try_end),

	 ]),

	
  # Banner selection menu
  (24,
   [
    (eq, "$g_player_banner_granted", 1),
    (troop_slot_eq, "trp_player", "slot_troop_banner_scene_prop", 0),
    (le,"$auto_menu",0),
#normal_banner_begin
    (start_presentation, "prsnt_banner_selection"),
#custom_banner_begin
#    (start_presentation, "prsnt_custom_banner"),
    ]),

  # Party Morale: Move morale towards target value.
  (24,
   [
      (call_script, "script_get_player_party_morale_values"),
      (assign, ":target_morale", reg0),
      (party_get_morale, ":cur_morale", "p_main_party"),
      (store_sub, ":dif", ":target_morale", ":cur_morale"),
      (store_div, ":dif_to_add", ":dif", 5),
      (store_mul, ":dif_to_add_correction", ":dif_to_add", 5),
      (try_begin),#finding ceiling of the value
        (neq, ":dif_to_add_correction", ":dif"),
        (try_begin),
          (gt, ":dif", 0),
          (val_add, ":dif_to_add", 1),
        (else_try),
          (val_sub, ":dif_to_add", 1),
        (try_end),
      (try_end),
      (val_add, ":cur_morale", ":dif_to_add"),
      (party_set_morale, "p_main_party", ":cur_morale"),      
    ]),
  

#Party AI: pruning some of the prisoners in each center (once a week)
  (24*7,
   [
       (try_for_range, ":center_no", centers_begin, centers_end),
         (party_get_num_prisoner_stacks, ":num_prisoner_stacks",":center_no"),
         (try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
           (party_prisoner_stack_get_troop_id, ":stack_troop",":center_no",":stack_no"),
           (neg|troop_is_hero, ":stack_troop"),
           (party_prisoner_stack_get_size, ":stack_size",":center_no",":stack_no"),
           (store_random_in_range, ":rand_no", 0, 40),
           (val_mul, ":stack_size", ":rand_no"),
           (val_div, ":stack_size", 100),
#TEMPERED chief ADD WEALTH FOR SALE OF PRISONERS, 20GP PER PRISONER
			(party_get_slot, ":cur_wealth", ":center_no", "slot_town_wealth"),
			(store_mul,":prisoner_sales",":stack_size",20),
			(val_add,":cur_wealth",":prisoner_sales"),
			(party_set_slot, ":center_no", "slot_town_wealth", ":cur_wealth"),
#TEMPERED CHANGES END
           (party_remove_prisoners, ":center_no", ":stack_troop", ":stack_size"),
         (try_end),
       (try_end),
    ]),

  #Adding net incomes to heroes (once a week)
  #Increasing debts to heroes by 1% (once a week)
  #Adding net incomes to centers (once a week)
  (24*7,
   [
       (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
         (troop_get_slot, ":cur_debt", ":troop_no", "slot_troop_player_debt"),#Increasing debt
         (val_mul, ":cur_debt", 101),
         (val_div, ":cur_debt", 100),
         (troop_set_slot, ":troop_no", "slot_troop_player_debt", ":cur_debt"),
         (call_script, "script_calculate_hero_weekly_net_income_and_add_to_wealth", ":troop_no"),#Adding net income
       (try_end),
	   
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         #If non-player center, adding income to wealth
         (neg|party_slot_eq, ":center_no", "slot_town_lord", "trp_player"), #center does not belong to player.
         (party_slot_ge, ":center_no", "slot_town_lord", 1), #center belongs to someone.
         (party_get_slot, ":cur_wealth", ":center_no", "slot_town_wealth"),
         (party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),
         (store_mul, ":added_wealth", ":prosperity", 20), #chief cambia
         (val_add, ":added_wealth", 2000), #chief cambia
         (try_begin),
           (party_slot_eq, ":center_no", "slot_party_type", spt_town),
           (val_mul, ":added_wealth", 3),
           (val_div, ":added_wealth", 2),
         (try_end),
         (val_add, ":cur_wealth", ":added_wealth"),
         (call_script, "script_calculate_weekly_party_wage", ":center_no"),
         (val_sub, ":cur_wealth", reg0),
         (val_max, ":cur_wealth", 0),
         (party_set_slot, ":center_no", "slot_town_wealth", ":cur_wealth"),
       (try_end),
    ]),

  #Hiring men with hero wealths (once a day)
  #Hiring men with center wealths (once a day)
  (24,
   [
     (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
       (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
       (troop_get_slot, ":party_no", ":troop_no", "slot_troop_leaded_party"),
       (ge, ":party_no", 1),
       (party_is_active, ":party_no"),
       (party_get_attached_to, ":cur_attached_party", ":party_no"),
       (is_between, ":cur_attached_party", centers_begin, centers_end),
#siege warfare chief cambia

       (assign, ":doit", 1),
       (try_begin),
         (this_or_next | party_slot_eq, ":cur_attached_party", "slot_center_blockaded", 1),    #center blockaded (by player) OR
         (party_slot_ge, ":cur_attached_party", "slot_center_is_besieged_by", 1), #center besieged by someone else
         (assign, ":doit", 0),
       (try_end),
       (eq, ":doit", 1),
#siege warfare         
                       
       (store_faction_of_party, ":party_faction", ":party_no"),
       (try_begin),
         (this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
         (eq, ":party_faction", "$players_kingdom"),        
         (assign, ":num_hiring_rounds", 1), 
         (store_random_in_range, ":random_value", 0, 2),         
         (val_add, ":num_hiring_rounds", ":random_value"),
       (else_try),
         (options_get_campaign_ai, ":reduce_campaign_ai"),
         (try_begin),
           (eq, ":reduce_campaign_ai", 0), #hard (2x reinforcing)
           (assign, ":num_hiring_rounds", 2),
         (else_try),
           (eq, ":reduce_campaign_ai", 1), #medium (1x or 2x reinforcing)
           (assign, ":num_hiring_rounds", 1), 
           (store_random_in_range, ":random_value", 0, 2),         
           (val_add, ":num_hiring_rounds", ":random_value"),
         (else_try),
           (eq, ":reduce_campaign_ai", 2), #easy (1x reinforcing)
           (assign, ":num_hiring_rounds", 1),          
         (try_end),                
       (try_end), 
       
       (try_begin),
         (faction_slot_eq,  ":party_faction", "slot_faction_marshall", ":troop_no"),
         (val_add, ":num_hiring_rounds", 1),
       (try_end),
                
       (try_for_range, ":unused", 0, ":num_hiring_rounds"),         
         (call_script, "script_hire_men_to_kingdom_hero_party", ":troop_no"), #Hiring men with current wealth        
       (try_end),  
     (try_end),
       
     (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
       (neg|party_slot_eq, ":center_no", "slot_town_lord", "trp_player"), #center does not belong to player.
       (party_slot_ge, ":center_no", "slot_town_lord", 1), #center belongs to someone.       
#siege warfare chief cambia
       (assign, ":doit", 1),
       (try_begin),
         (this_or_next | party_slot_eq, ":center_no", "slot_center_blockaded", 1),    #center blockaded (by player) OR
         (party_slot_ge, ":center_no", "slot_center_is_besieged_by", 1), #center besieged by someone else
         (assign, ":doit", 0),
       (try_end),
       (eq, ":doit", 1),
#siege warfare         
       (store_faction_of_party, ":center_faction", ":center_no"),
       (try_begin),
         (this_or_next|eq, ":center_faction", "fac_player_supporters_faction"),
         (eq, ":center_faction", "$players_kingdom"),        
         (assign, ":reinforcement_cost", reinforcement_cost_moderate),
       (else_try),
         (options_get_campaign_ai, ":reduce_campaign_ai"),
         (assign, ":reinforcement_cost", reinforcement_cost_moderate),
         (try_begin), 
           (eq, ":reduce_campaign_ai", 0), #hard (1x or 2x reinforcing)
           (assign, ":reinforcement_cost", reinforcement_cost_hard),
           (store_random_in_range, ":num_hiring_rounds", 0, 2),
           (val_add, ":num_hiring_rounds", 1),
         (else_try), 
           (eq, ":reduce_campaign_ai", 1), #moderate (1x reinforcing)
           (assign, ":reinforcement_cost", reinforcement_cost_moderate),
           (assign, ":num_hiring_rounds", 1),
         (else_try), 
           (eq, ":reduce_campaign_ai", 2), #easy (none or 1x reinforcing)
           (assign, ":reinforcement_cost", reinforcement_cost_easy),
           (store_random_in_range, ":num_hiring_rounds", 0, 2),
         (try_end),           
       (try_end),
       
       (try_for_range, ":unused", 0, ":num_hiring_rounds"),          
         (party_get_slot, ":cur_wealth", ":center_no", "slot_town_wealth"),
         (assign, ":hiring_budget", ":cur_wealth"),
         (val_div, ":hiring_budget", 2),
         (gt, ":hiring_budget", ":reinforcement_cost"),       
         (call_script, "script_cf_reinforce_party", ":center_no"),       
         (val_sub, ":cur_wealth", ":reinforcement_cost"),
         (party_set_slot, ":center_no", "slot_town_wealth", ":cur_wealth"),
       (try_end),  
     (try_end),

     #this is moved up from below , from a 24 x 15 slot to a 24 slot
     (try_for_range, ":center_no", centers_begin, centers_end),
       #(neg|is_between, ":center_no", castles_begin, castles_end),

	   (store_random_in_range, ":random", 0, 30),
	   (le, ":random", 10),
	   
       (call_script, "script_get_center_ideal_prosperity", ":center_no"),
       (assign, ":ideal_prosperity", reg0),
       (party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),       
       (try_begin),
	     (eq, ":random", 0), #with 3% probability it will gain +10/-10 prosperity even it has higher prosperity than its ideal prosperity.
         (try_begin),
           (store_random_in_range, ":random", 0, 2),
           (try_begin),
             (eq, ":random", 0),
             (neg|is_between, ":center_no", castles_begin, castles_end), #castles always gain positive prosperity from surprise income to balance their prosperity.
             (call_script, "script_change_center_prosperity", ":center_no", -10),
             (val_add, "$newglob_total_prosperity_from_convergence", -10),
           (else_try),     
             (call_script, "script_change_center_prosperity", ":center_no", 10),
             (val_add, "$newglob_total_prosperity_from_convergence", 10),
           (try_end),
         (try_end),
	   (else_try),
         (gt, ":prosperity", ":ideal_prosperity"),		 
         (call_script, "script_change_center_prosperity", ":center_no", -1),
         (val_add, "$newglob_total_prosperity_from_convergence", -1),
       (else_try),
         (lt, ":prosperity", ":ideal_prosperity"),		 
         (call_script, "script_change_center_prosperity", ":center_no", 1),
         (val_add, "$newglob_total_prosperity_from_convergence", 1),
	   (try_end),
     (try_end),	   	   	   
    ]),

  #Converging center prosperity to ideal prosperity once in every 15 days
  # (24*15,
   # [#(try_for_range, ":center_no", centers_begin, centers_end),
    #  (call_script, "script_get_center_ideal_prosperity", ":center_no"),
    #  (assign, ":ideal_prosperity", reg0),
    #  (party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),
    #  (try_begin),
    #    (gt, ":prosperity", ":ideal_prosperity"),
    #    (call_script, "script_change_center_prosperity", ":center_no", -1),
    #  (else_try),
    #    (lt, ":prosperity", ":ideal_prosperity"),
    #    (call_script, "script_change_center_prosperity", ":center_no", 1),
    #  (try_end),
    #(try_end),
    # ]),

  #Checking if the troops are resting at a half payment point
  (6,
   [(store_current_day, ":cur_day"),
    (try_begin),
      (neq, ":cur_day", "$g_last_half_payment_check_day"),
      (assign, "$g_last_half_payment_check_day", ":cur_day"),
      (try_begin),
        (eq, "$g_half_payment_checkpoint", 1),
        (val_add, "$g_cur_week_half_daily_wage_payments", 1), #half payment for yesterday
      (try_end),
      (assign, "$g_half_payment_checkpoint", 1),
    (try_end),
    (assign, ":resting_at_manor_or_walled_center", 0),
    (try_begin),
      (neg|map_free),
      (ge, "$g_last_rest_center", 0),
      (this_or_next|party_slot_eq, "$g_last_rest_center", "slot_center_has_manor", 1),
      (is_between, "$g_last_rest_center", walled_centers_begin, walled_centers_end),
      (assign, ":resting_at_manor_or_walled_center", 1),
    (try_end),
    (eq, ":resting_at_manor_or_walled_center", 0),
    (assign, "$g_half_payment_checkpoint", 0),
    ]),

#diplomatic indices
  (36,###gdw was 24
   [
#    (store_time_of_day, ":cur_hour"),
#    (store_current_hours, reg9),
#    (try_begin),
#     (this_or_next|ge, ":cur_hour", 20),
#     (le, ":cur_hour", 4),
#     (assign, reg10,":cur_hour"),

#     (set_show_messages, 1),
    
# 	  (call_script, "script_find_neighbors"),	#MOTO chief
# 	  (call_script, "script_randomly_start_war_peace_new", 1),
#     #(display_message, "@{!}DEBUG calling random political triggers script at {reg10} and {reg9}",0xFF0000),##reg1 interacts with one of the scripts just called gdw
#     (display_message, "@{!}DEBUG calling startwarpeacenew at {reg10}and {reg9}",0xFF0000),
#     (display_message, "@{!}DEBUG -- Doing randomly_start_war at {reg10}and {reg9}",0xFF0000),
#     (try_begin),
# 	      (ge, "$cheat_mode", 0),
# 		    # (store_time_of_day, ":cur_hour"),
#       #     (assign, ":cur_hour", reg9),
#           #(str_store_troop_name, s9, ":troop_no"),
#           (display_message, "@{!}DEBUG calling startwarpeacenew at {reg10}and {reg9}",0xFF0000),
#           (display_message, "@{!}DEBUG -- Doing randomly_start_war at {reg10}and {reg9}",0xFF0000),
#     (try_end),
# 	# #MOTO ramp up border incidents MOVE TO HOURLY TRIGGER
# 	# (try_for_range, ":acting_village", villages_begin, villages_end),
# 	# # (try_begin),
# 		# # (store_random_in_range, ":acting_village", villages_begin, villages_end),
# 	# #MOTO ramp up border incidents end
# 		# (store_random_in_range, ":target_village", villages_begin, villages_end),
# 		# (store_faction_of_party, ":acting_faction", ":acting_village"),
# 		# (store_faction_of_party, ":target_faction", ":target_village"), #target faction receives the provocation
# 		# (neq, ":acting_village", ":target_village"),
# 		# (neq, ":acting_faction", ":target_faction"),
		
# 		# (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":target_faction", ":acting_faction"),
# 		# (eq, reg0, 0),

# 		# (try_begin),
# 			# (party_slot_eq, ":acting_village", "slot_center_original_faction", ":target_faction"),
			
# 			# (call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", -1),
# 		# (else_try),
# 			# (party_slot_eq, ":acting_village", "slot_center_ex_faction", ":target_faction"),
			
# 			# (call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", -1),
			
# 		# (else_try),
# 			# (set_fixed_point_multiplier, 1),
# 			# (store_distance_to_party_from_party, ":distance", ":acting_village", ":target_village"),
# 			# (lt, ":distance", 25),
			
# 			# (call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", ":target_village"),
# 		# (try_end),
# 	# (try_end),
	
# 	(try_for_range, ":faction_1", kingdoms_begin, kingdoms_end),
# 		(faction_slot_eq, ":faction_1", "slot_faction_state", sfs_active),
# 		(try_for_range, ":faction_2", kingdoms_begin, kingdoms_end),
# 			(neq, ":faction_1", ":faction_2"),
# 			(faction_slot_eq, ":faction_2", "slot_faction_state", sfs_active),
			
# 			#remove provocations
# 			(store_add, ":slot_truce_days", ":faction_2", "slot_faction_truce_days_with_factions_begin"),
# 			(val_sub, ":slot_truce_days", kingdoms_begin),
# 			(faction_get_slot, ":truce_days", ":faction_1", ":slot_truce_days"),
# 			(try_begin),
# 				(ge, ":truce_days", 1),
# 				(try_begin),
# 					(eq, ":truce_days", 1),
# 					(call_script, "script_update_faction_notes", ":faction_1"),
# 					(lt, ":faction_1", ":faction_2"),
# 			##		(call_script, "script_add_notification_menu", "mnu_notification_truce_expired", ":faction_1", ":faction_2"), #chief puesto off para evitar saturacion de avisos
# 				##diplomacy chief begin
# 		##nested diplomacy start+ Replace "magic numbers" with named constants
#         (else_try),
#           (eq, ":truce_days", dplmc_treaty_alliance_days_expire + 1),#replaced 61
#           (call_script, "script_update_faction_notes", ":faction_1"),
#           (lt, ":faction_1", ":faction_2"),       
# #          (call_script, "script_add_notification_menu", "mnu_dplmc_notification_alliance_expired", ":faction_1", ":faction_2"), #chief puesto off
#         (else_try),
#          (eq, ":truce_days",dplmc_treaty_defense_days_expire + 1),#replaced 41
#           (call_script, "script_update_faction_notes", ":faction_1"),
#           (lt, ":faction_1", ":faction_2"),       
# #          (call_script, "script_add_notification_menu", "mnu_dplmc_notification_defensive_expired", ":faction_1", ":faction_2"), #chief puesto off
#         (else_try),
#           (eq, ":truce_days", dplmc_treaty_trade_days_expire + 1),#replaced 21
#           (call_script, "script_update_faction_notes", ":faction_1"),
#           (lt, ":faction_1", ":faction_2"),       
# #          (call_script, "script_add_notification_menu", "mnu_dplmc_notification_trade_expired", ":faction_1", ":faction_2"), #chief puesto off
#   	    ##nested diplomacy end+
#         ##diplomacy chief end
#         ##diplomacy chief end
# 				(try_end),
# 				(val_sub, ":truce_days", 1),
# 				(faction_set_slot, ":faction_1", ":slot_truce_days", ":truce_days"),
# 			(try_end),
		
# 			(store_add, ":slot_provocation_days", ":faction_2", "slot_faction_provocation_days_with_factions_begin"),
# 			(val_sub, ":slot_provocation_days", kingdoms_begin),
# 			(faction_get_slot, ":provocation_days", ":faction_1", ":slot_provocation_days"),
# 			(try_begin),
# 				(ge, ":provocation_days", 1),
# 				(try_begin),#factions already at war
# 					(store_relation, ":relation", ":faction_1", ":faction_2"),
# 					(lt, ":relation", 0),
# 					(faction_set_slot, ":faction_1", ":slot_provocation_days", 0),
# 				(else_try), #Provocation expires
# 					(eq, ":provocation_days", 1),
# 					(call_script, "script_add_notification_menu", "mnu_notification_casus_belli_expired", ":faction_1", ":faction_2"), #puesto off chief para que no aparezca el menu Fails to respond
# ##chief anadido
# ##      (str_store_faction_name, s1, "$g_notification_menu_var1"),
# ##      (str_store_faction_name, s2, "$g_notification_menu_var2"),
# ##	  (faction_get_slot, ":faction_leader", "$g_notification_menu_var1", "slot_faction_leader"),
# ##      (str_store_troop_name, s3, ":faction_leader"),
# ##	  (troop_get_type, reg4, ":faction_leader"),
# ##
# ##	   (call_script, "script_faction_follows_controversial_policy", "$g_notification_menu_var1", logent_policy_ruler_ignores_provocation), #chief puesto para fails
# ##chief anadido acaba
# 					(faction_set_slot, ":faction_1", ":slot_provocation_days", 0),
# 				(else_try),
# 					(val_sub, ":provocation_days", 1), 
# 					(faction_set_slot, ":faction_1", ":slot_provocation_days", ":provocation_days"),
# 				(try_end),
# 			(try_end),

# 			(try_begin), #at war
# 				(store_relation, ":relation", ":faction_1", ":faction_2"),
# 				(lt, ":relation", 0),
# 				(store_add, ":slot_war_damage", ":faction_2", "slot_faction_war_damage_inflicted_on_factions_begin"),
# 				(val_sub, ":slot_war_damage", kingdoms_begin),
# 				(faction_get_slot, ":war_damage", ":faction_1", ":slot_war_damage"),
# 				(val_add, ":war_damage", 1),
# 				(faction_set_slot, ":faction_1", ":slot_war_damage", ":war_damage"),
# 			(try_end),	
			
# 		(try_end),
# 		(call_script, "script_update_faction_notes", ":faction_1"),
# 	(try_end),
# (try_end),
    ]),
		
  # Give some xp to hero parties #chief cambia de 48 a 24 para que la IA tenga mas nivel de tropas
   (48,
   [      
       (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
         (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
	              
         (troop_get_slot, ":hero_party", ":troop_no", "slot_troop_leaded_party"),
         (gt, ":hero_party", centers_end),
         (party_is_active, ":hero_party"),
         
         (store_skill_level, ":trainer_level", skl_trainer, ":troop_no"),                  
         (val_add, ":trainer_level", 5), #average trainer level is 3 for npc lords, worst : 0, best : 6
         (store_mul, ":xp_gain", ":trainer_level", 2050), #xp gain in two days of period for each lord, average : 8000.#gdw       1000^
         ##gdw this was 1100 xp on a 24 hr cycle
         (assign, ":max_accepted_random_value", 30),
         (try_begin),               
           (store_troop_faction, ":cur_troop_faction", ":troop_no"),
           (neq, ":cur_troop_faction", "$players_kingdom"),#doesn'tapplytoplayer
           
           (options_get_campaign_ai, ":reduce_campaign_ai"),
           (try_begin),
             (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
             (assign, ":max_accepted_random_value", 35),
             (val_mul, ":xp_gain", 3),#multiplyxpgainX1.5
             (val_div, ":xp_gain", 2),
           (else_try),
             (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
             (assign, ":max_accepted_random_value", 25),#tmlWAS22
             (val_div, ":xp_gain", 2),#tml-1
           (try_end),
         (try_end),
         
         (store_random_in_range, ":rand", 0, 100),
         (le, ":rand", ":max_accepted_random_value"),

         (party_upgrade_with_xp, ":hero_party", ":xp_gain"),
       (try_end),
       
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),         
         (party_get_slot, ":center_lord", ":center_no", "slot_town_lord"),
         (neq, ":center_lord", "trp_player"),#notforplayer
         
         (assign, ":xp_gain", 4100), #xp gain in two days of period for each center, average : 3000.
         ##gdw this was at3000 for the 24 trigger
         (assign, ":max_accepted_random_value", 30),
         (try_begin),            
           (assign, ":cur_center_lord_faction", -1),
           (try_begin),
             (ge, ":center_lord", 0),
             (store_troop_faction, ":cur_center_lord_faction", ":center_lord"),
           (try_end),             
           (neq, ":cur_center_lord_faction", "$players_kingdom"),
           
           (options_get_campaign_ai, ":reduce_campaign_ai"),
           (try_begin),
             (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
             (assign, ":max_accepted_random_value", 35),
             (val_mul, ":xp_gain", 3),
             (val_div, ":xp_gain", 2),
           (else_try),
             (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
             (assign, ":max_accepted_random_value", 25),
             (val_div, ":xp_gain", 2),
           (try_end),
         (try_end),

         (store_random_in_range, ":rand", 0, 100),
         (le, ":rand", ":max_accepted_random_value"),
         
         (party_upgrade_with_xp, ":center_no", ":xp_gain"),
       (try_end),
    ]),

  # Process sieges
   (24,
   [
       (call_script, "script_process_sieges"),
    ]),

  # Decide vassal ai
   (7,
    [
      (call_script, "script_init_ai_calculation"),
      #(call_script, "script_decide_kingdom_party_ais"),
      (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
        (call_script, "script_calculate_troop_ai", ":troop_no"),
      (try_end),
      ]),

  # Hold regular marshall elections for players_kingdom
   # (24, #Disabled in favor of new system
    # [
    #  (val_add, "$g_election_date", 1),
    #  (ge, "$g_election_date", 90), #elections holds once in every 90 days.
    #  (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
    #  (neq, "$players_kingdom", "fac_player_supporters_faction"),
    #  (assign, "$g_presentation_input", -1),
    #  (assign, "$g_presentation_marshall_selection_1_vote", 0),
    #  (assign, "$g_presentation_marshall_selection_2_vote", 0),

    #  (assign, "$g_presentation_marshall_selection_max_renown_1", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_2", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_3", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_1_troop", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_2_troop", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_3_troop", -10000),
    #  (assign, ":num_men", 0),
    #  (try_for_range, ":loop_var", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
    #    (assign, ":cur_troop", ":loop_var"),
    #    (assign, ":continue", 0),
    #    (try_begin),
    #      (eq, ":loop_var", "trp_kingdom_heroes_including_player_begin"),
    #      (assign, ":cur_troop", "trp_player"),
    #      (try_begin),
    #        (eq, "$g_player_is_captive", 0),
    #        (assign, ":continue", 1),
    #      (try_end),
    #    (else_try),
#		  (troop_slot_eq, ":cur_troop", "slot_troop_occupation", slto_kingdom_hero),
 #         (store_troop_faction, ":cur_troop_faction", ":cur_troop"),
 #         (eq, "$players_kingdom", ":cur_troop_faction"),
  #        #(troop_slot_eq, ":cur_troop", "slot_troop_is_prisoner", 0),
  #        (neg|troop_slot_ge, ":cur_troop", "slot_troop_prisoner_of_party", 0),
   #       (troop_slot_ge, ":cur_troop", "slot_troop_leaded_party", 1),
    #      (troop_slot_eq, ":cur_troop", "slot_troop_occupation", slto_kingdom_hero),
    #      (neg|faction_slot_eq, ":cur_troop_faction", "slot_faction_leader", ":cur_troop"),
    #      (troop_get_slot, ":cur_party", ":cur_troop", "slot_troop_leaded_party"),
    #      (gt, ":cur_party", 0),
    #      (party_is_active, ":cur_party"),
    #      (call_script, "script_party_count_fit_for_battle", ":cur_party"),
    #      (assign, ":party_fit_for_battle", reg0),
    #      (call_script, "script_party_get_ideal_size", ":cur_party"),
    #      (assign, ":ideal_size", reg0),
    #      (store_mul, ":relative_strength", ":party_fit_for_battle", 100),
    #      (val_div, ":relative_strength", ":ideal_size"),
    #      (ge, ":relative_strength", 25),
    #      (assign, ":continue", 1),
    #    (try_end),
    #    (eq, ":continue", 1),
    #    (val_add, ":num_men", 1),
    #    (troop_get_slot, ":renown", ":cur_troop", "slot_troop_renown"),
    #    (try_begin),
    #      (gt, ":renown", "$g_presentation_marshall_selection_max_renown_1"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3", "$g_presentation_marshall_selection_max_renown_2"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_1"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_1", ":renown"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_1_troop"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_1_troop", ":cur_troop"),
    #    (else_try),
    #      (gt, ":renown", "$g_presentation_marshall_selection_max_renown_2"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3", "$g_presentation_marshall_selection_max_renown_2"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_2", ":renown"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_2_troop", ":cur_troop"),
    #    (else_try),
    #      (gt, ":renown", "$g_presentation_marshall_selection_max_renown_3"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3", ":renown"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", ":cur_troop"),
    #    (try_end),
    #  (try_end),
    #  (ge, "$g_presentation_marshall_selection_max_renown_1_troop", 0),
    #  (ge, "$g_presentation_marshall_selection_max_renown_2_troop", 0),
    #  (ge, "$g_presentation_marshall_selection_max_renown_3_troop", 0),
    #  (gt, ":num_men", 2), #at least 1 voter
    #  (assign, "$g_election_date", 0),
    #  (assign, "$g_presentation_marshall_selection_ended", 0),
    #  (try_begin),
    #    (neq, "$g_presentation_marshall_selection_max_renown_1_troop", "trp_player"),
    #    (neq, "$g_presentation_marshall_selection_max_renown_2_troop", "trp_player"),
    #    (start_presentation, "prsnt_marshall_selection"),
    #  (else_try),
    #    (jump_to_menu, "mnu_marshall_selection_candidate_ask"),
    #  (try_end),
      # ]),#

   (24,
    [	  
	(try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
		(troop_get_slot, ":impatience", ":kingdom_hero", "slot_troop_intrigue_impatience"),
		(val_sub, ":impatience", 5),
		(val_max, ":impatience", 0),
		(troop_set_slot, ":kingdom_hero", "slot_troop_intrigue_impatience", ":impatience"),
	(try_end),
	
	(store_random_in_range, ":controversy_deduction", 1, 3),
	(val_min, ":controversy_deduction", 2),
#	(assign, ":controversy_deduction", 1),
	
	#This reduces controversy by one each round
	(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
		(troop_get_slot, ":controversy", ":active_npc", "slot_troop_controversy"),
		(ge, ":controversy", 1),
		(val_sub, ":controversy", ":controversy_deduction"),
		(val_max, ":controversy", 0),
		(troop_set_slot, ":active_npc", "slot_troop_controversy", ":controversy"),
	(try_end),
	
	(troop_get_slot, ":controversy", "trp_player", "slot_troop_controversy"),
	(val_sub, ":controversy", ":controversy_deduction"),
	(val_max, ":controversy", 0),
	(troop_set_slot, "trp_player", "slot_troop_controversy", ":controversy"),
	
	]),
		
    #POLITICAL TRIGGERS
	#POLITICAL TRIGGER #1`
   # (8, #increased from 12
   (6, #increased from 12##gdw was at 4 for BW 1.41
    [	  
    (store_time_of_day, ":cur_hour"),
    (this_or_next|ge, ":cur_hour", 21),
    (le, ":cur_hour", 4),
	   (call_script, "script_cf_random_political_event"),
    (assign, reg1, ":cur_hour",),

	#Added Nov 2010 begins - do this twice
	# #(call_script, "script_cf_random_political_event"),	MOTO nah, just double trigger
	#Added Nov 2010 ends	
	
	#This generates quarrels and occasional reconciliations and interventions	
	    ]),
	
    #Individual lord political calculations
    #Check for lords without fiefs, auto-defections, etc
    (0.5,	
     [
        (val_add, "$g_lord_long_term_count", 1),
        (try_begin),
          (neg|is_between, "$g_lord_long_term_count", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
          (assign, "$g_lord_long_term_count", "trp_kingdom_heroes_including_player_begin"),
		(try_end),

        (assign, ":troop_no", "$g_lord_long_term_count"),
	
        (try_begin),
          (eq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),	
          (assign, ":troop_no", "trp_player"),
		(try_end),
		
	    (try_begin),
	      (eq, "$cheat_mode", 1),
		  (store_time_of_day, ":cur_hour"),
          (assign, reg9, ":cur_hour"),
          (str_store_troop_name, s9, ":troop_no"),
          (display_message, "@{!}DEBUG -- Doing political calculations for {s9} at {reg9}",0xFF0000),
        (try_end),
	
        #Penalty for no fief
        (try_begin),
          (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
          (neq, ":troop_no", "trp_player"),
		  
			 ##diplomacy start+ chief
			 ##Replace the loop with something quicker (if try_for_range works like I believe it does)
			 ##OLD:
          #(assign, ":fief_found", -1),
          #(try_for_range, ":center", centers_begin, centers_end),
          #  (party_slot_eq, ":center", "slot_town_lord", ":troop_no"),
          #  (assign, ":fief_found", ":center"),
          #(try_end),
			 ##NEW:
          (assign, ":fief_found", centers_end),
          (try_for_range, ":center", centers_begin, ":fief_found"),
            (party_slot_eq, ":center", "slot_town_lord", ":troop_no"),
            (assign, ":fief_found", ":center"),#<- should break the loop
          (try_end),
			 (try_begin),
			   #Do this so I don't have to change the code below that checks for -1
			   (eq, ":fief_found", centers_end),
				(assign, ":fief_found", -1),
			 (try_end),
			 ##diplomacy end+ chief
		
          (try_begin),
            (eq, ":fief_found", -1),
                        			
            (store_faction_of_troop, ":original_faction", ":troop_no"),
            (faction_get_slot, ":faction_leader", ":original_faction", "slot_faction_leader"),
            (troop_get_slot, ":troop_reputation", ":troop_no", "slot_lord_reputation_type"),
			
			(try_begin),
              (neq, ":faction_leader", ":troop_no"),
       			



	  ##diplomacy start+
				  #Ensure the faction leader is valid
				  (gt, ":faction_leader", -1),
				  ##diplomacy end+
            (try_begin),
                (this_or_next|eq, ":troop_reputation", lrep_quarrelsome),
                (this_or_next|eq, ":troop_reputation", lrep_selfrighteous),
                (this_or_next|eq, ":troop_reputation", lrep_cunning),
                (eq, ":troop_reputation", lrep_debauched),
                (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_leader", -2), #chief cambiado
				(val_add, "$total_no_fief_changes", -2), #chief cambiado#tml-3
             (display_message, "@{!}DEBUG -- Relation of {s9} with liege drops 2 fief assigned"),
              (else_try),
                (eq, ":troop_reputation", lrep_martial),
                (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_leader", -1), #chief cambiado
				(val_add, "$total_no_fief_changes", -1), #chief cambiado#tml-2
        (display_message, "@{!}DEBUG -- Relation of {s9} with liege drops 1 fief assigned"),
              (try_end),
            (try_end),
          (try_end),
        (try_end),
	
		
        #Auto-indictment or defection
        (try_begin),
			(this_or_next|troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
				(eq, ":troop_no", "trp_player"),		
		
			(try_begin),
				(eq, ":troop_no", "trp_player"),
				(assign, ":faction", "$players_kingdom"),
			(else_try),
				(store_faction_of_troop, ":faction", ":troop_no"),
			(try_end),
		
			(faction_get_slot, ":faction_leader", ":faction", "slot_faction_leader"),
			(neq, ":troop_no", ":faction_leader"),
			
			#I don't know why these are necessary, but they appear to be
			(neg|is_between, ":troop_no", "trp_kingdom_1_lord", "trp_knight_1_1"),
			(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
			
		  (assign, ":num_centers", 0),		  
		  (try_for_range,":cur_center", walled_centers_begin, walled_centers_end),		    
		    (store_faction_of_party, ":faction_of_center", ":cur_center"),
			(eq, ":faction_of_center", ":faction"),			
			(val_add, ":num_centers", 1),
		  (try_end),

		  #we are counting num_centers to allow defection although there is high relation between faction leader and troop. 
		  #but this rule should not applied for player's faction and player_supporters_faction so thats why here 1 is added to num_centers in that case.
		  (try_begin), 
		    (this_or_next|eq, ":faction", "$players_kingdom"),
			(eq, ":faction", "fac_player_supporters_faction"),
			(val_add, ":num_centers", 1),
		  (try_end),
			###if these two conditions apply, can intrigute
          (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
          (this_or_next|le, reg0, -99), #chief cambiado a -90 la mala relacion del lord con el rey para irse#gdw90
		      (eq, ":num_centers", 0), #if there is no walled centers that faction has defection happens 100%.			
			

			(call_script, "script_cf_troop_can_intrigue", ":troop_no", 0), #Should include battle, prisoner, in a castle with others 
		  
			(store_random_in_range, ":who_moves_first", 0, 2),
			
			(try_begin),
        (this_or_next|eq, ":num_centers", 0), #Thanks Caba`drin & Osviux
				(neq, ":who_moves_first", 0),
				(neq, ":troop_no", "trp_player"),
				
            #do a defection
                        (try_begin), 
                          (neq, ":num_centers", 0), 
                          (assign, "$g_give_advantage_to_original_faction", 1), 
                        (try_end),
			#(assign, "$g_give_advantage_to_original_faction", 1),

			(store_faction_of_troop, ":orig_faction", ":troop_no"),
			(call_script, "script_lord_find_alternative_faction", ":troop_no"),
			(assign, ":new_faction", reg0),			
			(assign, "$g_give_advantage_to_original_faction", 0),
			(try_begin),
			  (neq, ":new_faction", ":orig_faction"),			  
            
              (is_between, ":new_faction", kingdoms_begin, kingdoms_end),
              (str_store_troop_name_link, s1, ":troop_no"),
              (str_store_faction_name_link, s2, ":new_faction"),	
              (str_store_faction_name_link, s3, ":faction"),
              (call_script, "script_change_troop_faction", ":troop_no", ":new_faction"),
              (try_begin),
                (ge, "$cheat_mode", 1),
                (str_store_troop_name, s4, ":troop_no"),
                (display_message, "@{!}DEBUG - {s4} faction changed in defection",0xFF0000), 
              (try_end),	
              (troop_get_type, reg4, ":troop_no"),
              (val_mod, reg4, 2),    #gender fix chief moto
              (str_store_string, s4, "str_lord_defects_ordinary"),
              (display_log_message, "@{!}{s4}"),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (this_or_next|eq, ":new_faction", "$players_kingdom"),
                (eq, ":faction", "$players_kingdom"),
                (call_script, "script_add_notification_menu", "mnu_notification_lord_defects", ":troop_no", ":faction"),
              (try_end),				
			(try_end),
          (else_try),	
            (neq, ":faction_leader", "trp_player"),
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
			(le, reg0, -99), #chief cambia para que sea mas dificil cambiar de reino a los lords##gdw was -98
            (call_script, "script_indict_lord_for_treason", ":troop_no", ":faction"),
          (try_end),		  
        (else_try),  #Take a stand on an issue
          (neq, ":troop_no", "trp_player"),
          (store_faction_of_troop, ":faction", ":troop_no"),
          (faction_slot_ge, ":faction", "slot_faction_political_issue", 1),
          #This bit of complication is needed for savegame compatibility -- if zero is in the slot, they'll choose anyway			
          (neg|troop_slot_ge, ":troop_no", "slot_troop_stance_on_faction_issue", 1),
          (this_or_next|troop_slot_eq, ":troop_no", "slot_troop_stance_on_faction_issue", -1),
          (neq, "$players_kingdom", ":faction"),
          (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
          (call_script, "script_npc_decision_checklist_take_stand_on_issue", ":troop_no"),
          (troop_set_slot, ":troop_no", "slot_troop_stance_on_faction_issue", reg0),
        (try_end),

        (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
          (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":active_npc"),
          (lt, reg0, 0),
          (assign, ":relation", reg0),
          (store_sub, ":chance_of_convergence", 0, ":relation"),
          (store_random_in_range, ":random", 0, 300),
          (lt, ":random", ":chance_of_convergence"),
          (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":active_npc", 1),
          (val_add, "$total_relation_changes_through_convergence", 1),
        (try_end),				
        ]),
	
#TEMPORARILY DISABLED, AS READINESS IS NOW A PRODUCT OF NPC_DECISION_CHECKLIST	
  # Changing readiness to join army
#   (10,
 #   [
 #     (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
#		(eq, 1, 0),
#	    (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
#        (assign, ":modifier", 1),
#        (troop_get_slot, ":party_no", ":troop_no", "slot_troop_leaded_party"),
#        (try_begin),
#          (gt, ":party_no", 0),
#          (party_get_slot, ":commander_party", ":party_no", "slot_party_commander_party"),
#          (ge, ":commander_party", 0),
#          (store_faction_of_party, ":faction_no", ":party_no"),
#          (faction_get_slot, ":faction_marshall", ":faction_no", "slot_faction_marshall"),
#          (ge, ":faction_marshall", 0),
#          (troop_get_slot, ":marshall_party", ":faction_marshall", "slot_troop_leaded_party"),
#          (eq, ":commander_party", ":marshall_party"),
#          (assign, ":modifier", -1),
#        (try_end),
#        (troop_get_slot, ":readiness", ":troop_no", "slot_troop_readiness_to_join_army"),
#        (val_add, ":readiness", ":modifier"),
#        (val_clamp, ":readiness", 0, 100),
#        (troop_set_slot, ":troop_no", "slot_troop_readiness_to_join_army", ":readiness"),
#        (assign, ":modifier", 1),
#        (try_begin),
#          (gt, ":party_no", 0),
#          (store_troop_faction, ":troop_faction", ":troop_no"),
#          (eq, ":troop_faction", "fac_player_supporters_faction"),
#          (neg|troop_slot_eq, ":troop_no", "slot_troop_player_order_state", spai_undefined),
#          (party_get_slot, ":party_ai_state", ":party_no", "slot_party_ai_state"),
#          (party_get_slot, ":party_ai_object", ":party_no", "slot_party_ai_object"),
#          #Check if party is following player orders
#          (try_begin),
#            (troop_slot_eq, ":troop_no", "slot_troop_player_order_state", ":party_ai_state"),
#            (troop_slot_eq, ":troop_no", "slot_troop_player_order_object", ":party_ai_object"),
#            (assign, ":modifier", -1),
#          (else_try),
#            #Leaving following player orders if the current party order is not the same.
#            (troop_set_slot, ":troop_no", "slot_troop_player_order_state", spai_undefined),
#            (troop_set_slot, ":troop_no", "slot_troop_player_order_object", -1),
#          (try_end),
#        (try_end),
#        (troop_get_slot, ":readiness", ":troop_no", "slot_troop_readiness_to_follow_orders"),
#        (val_add, ":readiness", ":modifier"),
#        (val_clamp, ":readiness", 0, 100),
#        (troop_set_slot, ":troop_no", "slot_troop_readiness_to_follow_orders", ":readiness"),
#        (try_begin),
#          (lt, ":readiness", 10),
#          (troop_set_slot, ":troop_no", "slot_troop_player_order_state", spai_undefined),
#          (troop_set_slot, ":troop_no", "slot_troop_player_order_object", -1),
#        (try_end),
#      (try_end),
 #     ]),
  
  # Process vassal ai
   # (2,
   # [
     #(call_script, "script_process_kingdom_parties_ai"), #moved to below trigger (per 1 hour) in order to allow it processed more frequent.
   # ]),

  # Process alarms - perhaps break this down into several groups, with a modula
   (1, #this now calls 1/3 of all centers each time, thus hopefully lightening the CPU load
   [
     (call_script, "script_process_alarms"),

    # (call_script, "script_allow_vassals_to_join_indoor_battle"), #moto chief pone off
     
     (call_script, "script_process_kingdom_parties_ai"),
   ]),

  # Process siege ai
   (3,
   [
       ##diplomacy start+ chief
	  (assign, ":save_reg0", reg0),#Save registers
	  (assign, ":save_reg1", reg1),
	  ##diplomacy end+
     (store_current_hours, ":cur_hours"),
      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
        (party_get_slot, ":besieger_party", ":center_no", "slot_center_is_besieged_by"),
        (gt, ":besieger_party", 0),
        (party_is_active, ":besieger_party"),
        (store_faction_of_party, ":besieger_faction", ":besieger_party"),
        (party_slot_ge, ":center_no", "slot_center_is_besieged_by", 1),
        (party_get_slot, ":siege_begin_hours", ":center_no", "slot_center_siege_begin_hours"),
        (store_sub, ":siege_begin_hours", ":cur_hours", ":siege_begin_hours"),
        (assign, ":launch_attack", 0),
        (assign, ":call_attack_back", 0),
        (assign, ":attacker_strength", 0),
        (assign, ":marshall_attacking", 0),
        (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
          (neg|troop_slot_ge, ":troop_no", "slot_troop_prisoner_of_party", 0),
          (troop_get_slot, ":party_no", ":troop_no", "slot_troop_leaded_party"),
          (gt, ":party_no", 0),
          (party_is_active, ":party_no"),
		  
          (store_troop_faction, ":troop_faction_no", ":troop_no"),
          (eq, ":troop_faction_no", ":besieger_faction"),
          (assign, ":continue", 0),
          (try_begin),
            (party_slot_eq, ":party_no", "slot_party_ai_state", spai_besieging_center),
            (party_slot_eq, ":party_no", "slot_party_ai_object", ":center_no"),
            (assign, ":continue", 1),
          (else_try),
            (party_slot_eq, ":party_no", "slot_party_ai_state", spai_accompanying_army),
            (party_get_slot, ":commander_party", ":party_no", "slot_party_ai_object"),
            (gt, ":commander_party", 0),
            (party_is_active, ":commander_party"),
            (party_slot_eq, ":commander_party", "slot_party_ai_state", spai_besieging_center),
            (party_slot_eq, ":commander_party", "slot_party_ai_object", ":center_no"),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (party_get_battle_opponent, ":opponent", ":party_no"),
          (this_or_next|lt, ":opponent", 0),
          (eq, ":opponent", ":center_no"),
          (try_begin),
            (faction_slot_eq, ":besieger_faction", "slot_faction_marshall", ":troop_no"),
            (assign, ":marshall_attacking", 1),
          (try_end),
          (call_script, "script_party_calculate_regular_strength", ":party_no"),
          (call_script, "script_party_calculate_regular_strength", ":party_no"),
		  ##diplomacy start+ terrain advantage chief
		  (try_begin),
			(ge, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
			(call_script, "script_dplmc_party_calculate_strength_in_terrain", ":party_no", dplmc_terrain_code_siege, 0, 0),
          (try_end),
		  ##diplomacy end+
          (val_add, ":attacker_strength", reg0),
        (try_end),
        (try_begin),
          (gt, ":attacker_strength", 0),
          (party_collect_attachments_to_party, ":center_no", "p_collective_enemy"),
          (call_script, "script_party_calculate_regular_strength", "p_collective_enemy"),
 		  ##diplomacy start+ terrain advantage chief
		  (try_begin),
			(ge, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
			(call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_enemy", dplmc_terrain_code_siege, 0, 0),
          (try_end),
		  ##diplomacy end+
         (assign, ":defender_strength", reg0),
          (try_begin),
            (eq, "$auto_enter_town", ":center_no"),
            (eq, "$g_player_is_captive", 0),
            (call_script, "script_party_calculate_regular_strength", "p_main_party"),
 			##diplomacy start+ terrain advantage chief
			(try_begin),
				(ge, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
				(call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_enemy", dplmc_terrain_code_siege, 0, 0),
			(try_end),
			##diplomacy end+
           (val_add, ":defender_strength", reg0),
            (val_mul, ":attacker_strength", 2), #double the power of attackers if the player is in the campaign
          (try_end),
          (party_get_slot, ":siege_hardness", ":center_no", "slot_center_siege_hardness"),
          (val_add, ":siege_hardness", 100),
          (val_mul, ":defender_strength", ":siege_hardness"),
          (val_div, ":defender_strength", 100),
          (val_max, ":defender_strength", 1),
          (try_begin),
            (eq, ":marshall_attacking", 1),
            (eq, ":besieger_faction", "$players_kingdom"),
            (check_quest_active, "qst_follow_army"),
            (val_mul, ":attacker_strength", 2), #double the power of attackers if the player is in the campaign
          (try_end),
          (store_mul, ":strength_ratio", ":attacker_strength", 100),
          (val_div, ":strength_ratio", ":defender_strength"),
          (store_sub, ":random_up_limit", ":strength_ratio", 250), #was 300 (1.126)
                    
          (try_begin),
            (gt, ":random_up_limit", -100), #never attack if the strength ratio is less than 150%
            (store_div, ":siege_begin_hours_effect", ":siege_begin_hours", 2), #was 3 (1.126)
            (val_add, ":random_up_limit", ":siege_begin_hours_effect"),
          (try_end),

          (val_div, ":random_up_limit", 5),
          (val_max, ":random_up_limit", 0),
          (store_sub, ":random_down_limit", 175, ":strength_ratio"), #was 200 (1.126)
          (val_max, ":random_down_limit", 0),
          (try_begin),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", ":random_up_limit"),
            (gt, ":siege_begin_hours", 24),#initial preparation
            (assign, ":launch_attack", 1),
          (else_try),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", ":random_down_limit"),            
            (assign, ":call_attack_back", 1),
          (try_end),
        (else_try),
          (assign, ":call_attack_back", 1),
        (try_end),

        #Assault the fortress
        (try_begin),
          (eq, ":launch_attack", 1),
          (call_script, "script_begin_assault_on_center", ":center_no"),
        (else_try),
          (eq, ":call_attack_back", 1),
          (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
            (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
            (neg|troop_slot_ge, ":troop_no", "slot_troop_prisoner_of_party", 0),
            (troop_get_slot, ":party_no", ":troop_no", "slot_troop_leaded_party"),
            (gt, ":party_no", 0),
            (party_is_active, ":party_no"),
			
            (party_slot_eq, ":party_no", "slot_party_ai_state", spai_besieging_center),
            (party_slot_eq, ":party_no", "slot_party_ai_object", ":center_no"),
            (party_slot_eq, ":party_no", "slot_party_ai_substate", 1),
            (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
            (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, ":center_no"),
            #resetting siege begin time if at least 1 party retreats
            (party_set_slot, ":center_no", "slot_center_siege_begin_hours", ":cur_hours"),
          (try_end),
        (try_end),
      (try_end),
	  ##diplomacy start+ chief
	  #Revert registers
	  (assign, reg0, ":save_reg0"),
	  (assign, reg1, ":save_reg1"),
	  ##diplomacy end+
    ]),

    # Decide faction ais
    (6, #it was 23
    [
      (assign, "$g_recalculate_ais", 1),
    ]),
	
    
  # Decide faction ai flag check
   (0,
   [
   

    (try_begin),
		(ge, "$cheat_mode", 1),
	
		(try_for_range, ":king", "trp_kingdom_1_lord", "trp_knight_1_1"),		
			(store_add, ":proper_faction", ":king", "fac_kingdom_1"),
			(val_sub, ":proper_faction", "trp_kingdom_1_lord"),
			(store_faction_of_troop, ":actual_faction", ":king"),
			
			(neq, ":proper_faction", ":actual_faction"),
			(neq, ":actual_faction", "fac_commoners"),
			(ge, "$cheat_mode", 2),
			(neq, ":king", "trp_kingdom_2_lord"),
			
			(str_store_troop_name, s4, ":king"),
			(str_store_faction_name, s5, ":actual_faction"),
			(str_store_faction_name, s6, ":proper_faction"),
			(str_store_string, s65, "@{!}DEBUG - {s4} is in {s5}, should be in {s6}, disabling political cheat mode"),
#			(display_message, "@{s65}"),
			(rest_for_hours, 0, 0, 0),
			
			#(assign, "$cheat_mode", 1),
			(jump_to_menu, "mnu_debug_alert_from_s65"),
		(try_end),
	
	
	(try_end),
   
     (eq, "$g_recalculate_ais", 1),
     (assign, "$g_recalculate_ais", 0),
     (call_script, "script_recalculate_ais"),
   ]),
	
    # Count faction armies
    (24,
    [
       (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
         (call_script, "script_faction_recalculate_strength", ":faction_no"),
       (try_end),
	   
	   (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
		(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
		(neg|faction_slot_eq, ":active_npc_faction", "slot_faction_ai_state", sfai_default),
		(neg|faction_slot_eq, ":active_npc_faction", "slot_faction_ai_state", sfai_feast),
		(neg|faction_slot_eq, ":active_npc_faction", "slot_faction_ai_state", sfai_gathering_army),
		
		(troop_get_slot, ":active_npc_party", ":active_npc", "slot_troop_leaded_party"),
		(party_is_active, ":active_npc_party"),
		
		(val_add, "$total_vassal_days_on_campaign", 1),
		
	    (party_slot_eq, ":active_npc_party", "slot_party_ai_state", spai_accompanying_army),
		(val_add, "$total_vassal_days_responding_to_campaign", 1),
		
	   
	   (try_end),
	   
    ]),

  # Reset hero quest status
  # Change hero relation
   (36,
   [
     (try_for_range, ":troop_no", heroes_begin, heroes_end),
       (troop_set_slot, ":troop_no", "slot_troop_does_not_give_quest", 0),
     (try_end),
     
     (try_for_range, ":troop_no", village_elders_begin, village_elders_end),
       (troop_set_slot, ":troop_no", "slot_troop_does_not_give_quest", 0),
     (try_end),
    ]),

  #Refreshing village defenders
  #Clearing "slot_village_player_can_not_steal_cattle" flags
   (48,
   [
      (try_for_range, ":village_no", villages_begin, villages_end),
        (call_script, "script_refresh_village_defenders", ":village_no"),
        (party_set_slot, ":village_no", "slot_village_player_can_not_steal_cattle", 0),
      (try_end),
    ]),

  # Refresh number of cattle in villages
  (24 * 7,
   [
       (try_for_range, ":village_no", centers_begin, centers_end),
	  (neg|is_between, ":village_no", castles_begin, castles_end),
      (party_get_slot, ":num_cattle", ":village_no", "slot_center_head_cattle"),
      (party_get_slot, ":num_sheep", ":village_no", "slot_center_head_sheep"),
      (party_get_slot, ":num_acres", ":village_no", "slot_center_acres_pasture"),
	  (val_max, ":num_acres", 1),
	  
	  (store_mul, ":grazing_capacity", ":num_cattle", 400),
	  (store_mul, ":sheep_addition", ":num_sheep", 200),
	  (val_add, ":grazing_capacity", ":sheep_addition"),
	  (val_div, ":grazing_capacity", ":num_acres"),
	  
	  
      (store_random_in_range, ":random_no", 0, 100),
      (try_begin), #Disaster
        (eq, ":random_no", 0),#1% chance of epidemic - should happen once every two years
        (val_min, ":num_cattle", 10),
		
            ##diplomacy start+ Add display message for the player's own fiefs chief
        (try_begin),
		   #(store_distance_to_party_from_party, ":dist", "p_main_party", ":village_no"),
		   #(this_or_next|lt, ":dist", 30),
	          (gt, "$g_player_chamberlain", 0),
		   (party_slot_eq, ":village_no", "slot_town_lord", "trp_player"),
		   (party_get_slot, reg4, ":village_no", "slot_center_head_cattle"),
		   (val_sub, reg4, ":num_cattle"),
		   (gt, reg4, 0),
		   (str_store_party_name_link, s4, ":village_no"),
		   (display_log_message, "@A livestock epidemic has killed {reg4} cattle in {s4}."),
       (try_end),
		   ##diplomacy end+
		
      (else_try), #Overgrazing
	    (gt, ":grazing_capacity", 100),
		
		(val_mul, ":num_sheep", 90),
		(val_div, ":num_sheep", 100),

		(val_mul, ":num_cattle", 90),
		(val_div, ":num_cattle", 100),
       (else_try), #superb grazing
         (lt, ":grazing_capacity", 30),

         (val_mul, ":num_cattle", 120), #20% increase at number of cattles
         (val_div, ":num_cattle", 100),
         (val_add, ":num_cattle", 1),
		
         (val_mul, ":num_sheep", 120), #20% increase at number of sheeps
         (val_div, ":num_sheep", 100),
         (val_add, ":num_sheep", 1),
		
       (else_try), #very good grazing
         (lt, ":grazing_capacity", 60),

         (val_mul, ":num_cattle", 110), #10% increase at number of cattles
         (val_div, ":num_cattle", 100),
         (val_add, ":num_cattle", 1),
		
         (val_mul, ":num_sheep", 110), #10% increase at number of sheeps
         (val_div, ":num_sheep", 100),
         (val_add, ":num_sheep", 1),

       (else_try), #good grazing
         (lt, ":grazing_capacity", 100),
         (lt, ":random_no", 50),

         (val_mul, ":num_cattle", 105), #5% increase at number of cattles
         (val_div, ":num_cattle", 100),
         (try_begin), #if very low number of cattles and there is good grazing then increase number of cattles also by one
           (le, ":num_cattle", 20),
           (val_add, ":num_cattle", 1),
         (try_end),
		
         (val_mul, ":num_sheep", 105), #5% increase at number of sheeps
         (val_div, ":num_sheep", 100),
         (try_begin), #if very low number of sheeps and there is good grazing then increase number of sheeps also by one
           (le, ":num_sheep", 20),
           (val_add, ":num_sheep", 1),
         (try_end),		
       (try_end),

       (party_set_slot, ":village_no", "slot_center_head_cattle", ":num_cattle"),
       (party_set_slot, ":village_no", "slot_center_head_sheep", ":num_sheep"),	  	  	  
     (try_end),
    ]),

   #Accumulate taxes
   (24 * 7,
   [
      #Adding earnings to town lords' wealths.
      #Moved to troop does business
      #(try_for_range, ":center_no", centers_begin, centers_end),
      #  (party_get_slot, ":town_lord", ":center_no", "slot_town_lord"),
      #  (neq, ":town_lord", "trp_player"),
      #  (is_between, ":town_lord", active_npcs_begin, active_npcs_end),
      #  (party_get_slot, ":accumulated_rents", ":center_no", "slot_center_accumulated_rents"),
      #  (party_get_slot, ":accumulated_tariffs", ":center_no", "slot_center_accumulated_tariffs"),
      #  (troop_get_slot, ":troop_wealth", ":town_lord", "slot_troop_wealth"),
      #  (val_add, ":troop_wealth", ":accumulated_rents"),
      #  (val_add, ":troop_wealth", ":accumulated_tariffs"),
      #  (troop_set_slot, ":town_lord", "slot_troop_wealth", ":troop_wealth"),
      #  (party_set_slot, ":center_no", "slot_center_accumulated_rents", 0),
      #  (party_set_slot, ":center_no", "slot_center_accumulated_tariffs", 0),
      #  (try_begin),
      #    (eq, "$cheat_mode", 1),
      #    (assign, reg1, ":troop_wealth"),
      #    (add_troop_note_from_sreg, ":town_lord", 1, "str_current_wealth_reg1", 0),
      #  (try_end),
      #(try_end),
      
	  #Collect taxes for another week
      (try_for_range, ":center_no", centers_begin, centers_end),
        (try_begin),
          (party_slot_ge, ":center_no", "slot_town_lord", 0), #unassigned centers do not accumulate rents	  
        
          (party_get_slot, ":accumulated_rents", ":center_no", "slot_center_accumulated_rents"),		  
		
          (assign, ":cur_rents", 0),
          (try_begin),
            (party_slot_eq, ":center_no", "slot_party_type", spt_village),
            (try_begin),
              (party_slot_eq, ":center_no", "slot_village_state", svs_normal),
              (assign, ":cur_rents", 1200),
            (try_end),
          (else_try),
            (party_slot_eq, ":center_no", "slot_party_type", spt_castle),
            (assign, ":cur_rents", 1200),
          (else_try),  
            (party_slot_eq, ":center_no", "slot_party_type", spt_town),
            (assign, ":cur_rents", 2400),
          (try_end),
		
          (party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"), #prosperty changes between 0..100     
          (store_add, ":multiplier", 20, ":prosperity"), #multiplier changes between 20..120
#TAXES begin chief SoD
		(try_begin),
			(party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
			(val_add, ":multiplier", "$g_sod_tax"),
			(try_begin),
							 (this_or_next|eq, "$g_sod_faith", 4),
							 (eq, "$g_pueblos_religion", 4),
			(lt, ":multiplier", 0),
			(assign, ":multiplier", 0),
			(party_get_slot, ":faith", ":center_no", "slot_center_sod_local_faith"),
			(val_div, ":faith", 10),
			(val_add, ":multiplier", ":faith"),
			(else_try),
							 (this_or_next|eq, "$g_sod_faith", 3),
							 (party_slot_eq, ":center_no", "slot_center_religion_pagan", 1),
			(lt, ":multiplier", 0),
			(assign, ":multiplier", 0),
			(party_get_slot, ":faith", ":center_no", "slot_center_sod_local_faith"),
			(val_mul, ":faith", -1),
			(val_div, ":faith", 10),
			(val_add, ":multiplier", ":faith"),
			(try_end),
		(try_end),
#TAXES end
          (val_mul, ":cur_rents", ":multiplier"), 
          (val_div, ":cur_rents", 127),#Prosperity of 100 gives the default values
#sod chief empieza rentas con black smith#gdwmarker at Simpletrigger71was120
			(try_begin),
				(lt, ":cur_rents", 0),
				(assign, ":cur_rents", 0),
			(try_end),
		(try_begin),
			(party_slot_eq, ":center_no", "slot_party_type", spt_castle),
			(val_sub, ":cur_rents", -260),# Removed to make castle income better TML. F123 - Submod -> 1.41 was at +250?gdwfrom-250Why not just add this?gdwval_add
#SoD Buildings Begin
			(try_begin),
				(party_slot_eq, ":center_no", "slot_center_has_blacksmith", 1),
				(val_add, ":cur_rents", 150),# Increased blacksmith bonus to 100 TML. up from 50 F123 - Submod -> 1.41#gdw120 for quikr invest recovery
			(try_end),
#SDO BUILDINGS END
		(try_end),
#sod chief acaba rentas          
          (try_begin),
            (party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
            
            (options_get_campaign_ai, ":reduce_campaign_ai"),
            (try_begin),
              (eq, ":reduce_campaign_ai", 0), #hard (less money from rents)
              (val_mul, ":cur_rents", 3),
              (val_div, ":cur_rents", 4),
            (else_try),
              (eq, ":reduce_campaign_ai", 1), #medium (normal money from rents)
              #same
            (else_try),
              (eq, ":reduce_campaign_ai", 2), #easy (more money from rents)
              (val_mul, ":cur_rents", 4),
              (val_div, ":cur_rents", 3),
            (try_end),                
          (try_end),  
                    
          (val_add, ":accumulated_rents", ":cur_rents"), #cur rents changes between 23..1000
        ##diplomacy chief begin
          (try_begin),    
            (str_store_party_name, s6, ":center_no"),
             
            (party_get_slot, ":tax_rate", ":center_no", "slot_center_taxation"),
            (neq, ":tax_rate", 0),
            (store_div, ":rent_change", ":accumulated_rents", 100),
            (val_mul, ":rent_change", ":tax_rate"),
   
            (try_begin), #debug
              (eq, "$cheat_mode", 1),
              (assign, reg0, ":tax_rate"),
              (display_message, "@{!}DEBUG : tax rate in {s6}: {reg0}"),
              (assign, reg0, ":accumulated_rents"),
              (display_message, "@{!}DEBUG : accumulated_rents  in {s6}: {reg0}"),
              (assign, reg0, ":rent_change"),
              (display_message, "@{!}DEBUG : rent_change in {s6}: {reg0}  in {s6}"),
            (try_end),          
  
            (val_add, ":accumulated_rents", ":rent_change"),
            
            (val_div, ":tax_rate", -25),
            
            (call_script, "script_change_center_prosperity", ":center_no", ":tax_rate"),
  
            (try_begin),
              (lt, ":tax_rate", 0), #double negative values
              (val_mul, ":tax_rate", 2),
              
              (try_begin), #debug
                (eq, "$cheat_mode", 1),
                (assign, reg0, ":tax_rate"),
                (display_message, "@{!}DEBUG : tax rate after modi in {s6}: {reg0}"),
              (try_end),
  
              (try_begin),
                (this_or_next|is_between, ":center_no", villages_begin, villages_end),
                (is_between, ":center_no", towns_begin, towns_end),
                (party_get_slot, ":center_relation", ":center_no", "slot_center_player_relation"),
  
                (try_begin), #debug
                  (eq, "$cheat_mode", 1),
                  (assign, reg0, ":center_relation"),
                  (display_message, "@{!}DEBUG : center relation: {reg0}"),
                (try_end),
              
                (le, ":center_relation", -5),
                (store_random_in_range, ":random",-100, 0),
                (gt, ":random", ":center_relation"),           
                
                (neg|party_slot_eq, ":center_no", "slot_village_infested_by_bandits", "trp_peasant_woman"),
                (display_message, "@Riot in {s6}!"),
                (party_set_slot, ":center_no", "slot_village_infested_by_bandits", "trp_peasant_woman"), #trp_peasant_woman used to simulate riot
                (call_script, "script_change_center_prosperity", ":center_no", -1),     
                (call_script, "script_add_notification_menu", "mnu_dplmc_notification_riot", ":center_no", 0),         
  
                #add additional troops
                (store_character_level, ":player_level", "trp_player"),
                (store_div, ":player_leveld2", ":player_level", 2),
                (store_mul, ":player_levelx2", ":player_level", 2),
                (try_begin), 
                  (is_between, ":center_no", villages_begin, villages_end),       
                  (store_random_in_range, ":random",0, ":player_level"),
                  (party_add_members, ":center_no", "trp_merc_infantryt4", ":random"),
                  (store_random_in_range, ":random", 0, ":player_leveld2"),
                  (party_add_members, ":center_no", "trp_merc_infantryt5", ":random"),
                (else_try),
                  (party_set_banner_icon, ":center_no", 0),   
                  (party_get_num_companion_stacks, ":num_stacks",":center_no"),
                  (try_for_range, ":i_stack", 0, ":num_stacks"),
                    (party_stack_get_size, ":stack_size",":center_no",":i_stack"),                             
                    (val_div, ":stack_size", 2),
                    (party_stack_get_troop_id, ":troop_id", ":center_no", ":i_stack"),
                    (party_remove_members, ":center_no", ":troop_id", ":stack_size"),
                  (try_end),
                  (store_random_in_range, ":random",":player_leveld2", ":player_levelx2"),
                  (party_add_members, ":center_no", "trp_townsman", ":random"),
                  (store_random_in_range, ":random",0, ":player_level"),
                  (party_add_members, ":center_no", "trp_merc_infantryt2", ":random"),
                (try_end),
              (end_try),     
            (try_end),
            (call_script, "script_change_player_relation_with_center", ":center_no", ":tax_rate"),
          (try_end),
          
          (try_begin), #no taxes for infested villages and towns 
            (party_slot_ge, ":center_no", "slot_village_infested_by_bandits", 1),
            (assign,":accumulated_rents", 0),
          (try_end),
        ##diplomacy chief end

          (party_set_slot, ":center_no", "slot_center_accumulated_rents", ":accumulated_rents"),
#TAXES begin
		(try_begin),
		(party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
		(party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),
		(party_get_slot, ":cur_relation", ":center_no", "slot_center_player_relation"),
		(try_begin),
			(eq, "$g_sod_tax", -80),
			(val_add, ":prosperity", 3),
			(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),
			(val_add, ":cur_relation", 3),
			(party_set_slot, ":center_no", "slot_center_player_relation", ":cur_relation"),
		(else_try),
			(eq, "$g_sod_tax", -30),
			(val_add, ":prosperity", 2),
			(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),
			(val_add, ":cur_relation", 2),
			(party_set_slot, ":center_no", "slot_center_player_relation", ":cur_relation"),
		(else_try),
		(eq, "$g_sod_tax", -50),
			(val_add, ":prosperity", 1),
			(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),
			(val_add, ":cur_relation", 1),
			(party_set_slot, ":center_no", "slot_center_player_relation", ":cur_relation"),
		(else_try),
		(eq, "$g_sod_tax", -50),
			(val_add, ":prosperity", 0),
			(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),
			(val_add, ":cur_relation", 0),
			(party_set_slot, ":center_no", "slot_center_player_relation", ":cur_relation"),
		(else_try),
		(eq, "$g_sod_tax", -50),
			(val_add, ":prosperity", -1),
			(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),
			(val_add, ":cur_relation", -1),
			(party_set_slot, ":center_no", "slot_center_player_relation", ":cur_relation"),
		(else_try),
		(eq, "$g_sod_tax", 30),
			(val_add, ":prosperity", -2),
			(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),
			(val_add, ":cur_relation", -2),
			(party_set_slot, ":center_no", "slot_center_player_relation", ":cur_relation"),
		(else_try),
		(eq, "$g_sod_tax", 80),
			(val_add, ":prosperity", -5),
			(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),
			(val_add, ":cur_relation", -5),
			(party_set_slot, ":center_no", "slot_center_player_relation", ":cur_relation"),
		(try_end),
		(try_end),
		
#TAXES end
      (try_end),
        
		(try_begin),
		  (is_between, ":center_no", villages_begin, villages_end),
		  (party_get_slot, ":bound_castle", ":center_no", "slot_village_bound_center"),
		  (party_slot_ge, ":bound_castle", "slot_town_lord", 0), #unassigned centers do not accumulate rents	  
		  (is_between, ":bound_castle", castles_begin, castles_end),
		  (party_get_slot, ":accumulated_rents", ":bound_castle", "slot_center_accumulated_rents"), #castle's accumulated rents
		  (val_add, ":accumulated_rents", ":cur_rents"), #add village's rent to castle rents
		  (party_set_slot, ":bound_castle", "slot_center_accumulated_rents", ":accumulated_rents"),
		(try_end),		
      (try_end),
    ]),

#chief prisioneros en las minas
  # Pay slave labor earnings
   (24 * 7,
   [
    (try_begin),
	  (gt, "$g_num_prisoners", 0),
	  (assign, "$g_earnings", 0),
	  (assign, "$g_num_escapees", 0),
    #  (try_for_range, ":center_no", "p_salt_mine", "p_test_scene"),#gdwpertml
#	    (party_get_num_companions,"$g_num_guards",":center_no"),#gdwpertml
	    (party_get_num_prisoners, "$g_num_prisoners", "p_salt_mine"), #TML Rewrote slave labor code. F123 - Submod -> 1.41

    (party_get_num_companion_stacks, ":num_stacks","p_salt_mine"),
    (assign, ":guard_strength", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (store_character_level, ":troop_level", ":i_stack"),
      (try_begin),
        (is_between, ":troop_level", 0, 16), 
        (assign, ":strength", 200),
      (else_try),  
        (is_between, ":troop_level", 16, 20),
        (assign, ":strength", 300),
      (else_try),  
        (is_between, ":troop_level", 20, 24),
        (assign, ":strength", 400),
      (else_try),  
        (is_between, ":troop_level", 24, 28),
        (assign, ":strength", 500),
      (else_try),  
        (is_between, ":troop_level", 28, 30),
        (assign, ":strength", 600),
      (else_try),  
        (is_between, ":troop_level", 30, 34),
        (assign, ":strength", 800),
      (else_try),
        (assign, ":strength", 1000),
      (try_end),
      (party_stack_get_size, ":stack_size","p_salt_mine",":i_stack"),
      (val_mul, ":strength", ":stack_size"),
      (val_add, ":guard_strength", ":strength"),
    (try_end),
    (store_div, ":ratio", ":guard_strength", "$g_num_prisoners"),
    (assign, ":escape_chance", 0),
    (try_begin),
      (ge, ":ratio", 200),
    (else_try),
      (is_between, ":ratio", 99, 200),
      (assign, ":escape_chance", 1),
    (else_try),
      (store_sub, ":escape_chance", 100, ":ratio"),
    (try_end),
      #(try_begin),
        #(gt, ":difference", 0),
        #(store_random_in_range, ":random", 0, ":difference"),
        #(try_begin),
        #  (gt, ":random", 5),
        #  (store_random_in_range, ":escapees", 0, ":difference"),
        #  (try_begin),
        #    (eq, ":escapees", 0),
        #    (assign, ":escapees", 1),
        #  (try_end),
        #  (assign, "$g_num_escapees", ":escapees"),
        #  (party_get_num_prisoner_stacks, ":num_stacks", ":center_no"),
        #  (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
        #  (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":center_no", ":troop_iterator"),
        #  (party_prisoner_stack_get_size, ":stack_size", ":center_no", ":troop_iterator"),
        #  (try_begin),
        #    (gt, ":escapees", 0),
        #    (try_begin),
        #      (gt, ":stack_size", ":escapees"),
        #      (store_sub, ":stack_sub", ":stack_size", ":escapees"),
        #      (val_sub, ":escapees", ":stack_sub"),
        #      (party_remove_prisoners, ":center_no", ":cur_troop_id", ":stack_sub"),
        #    (try_end),
        #  (try_end),
        #(try_end),
#escapan mas prisioneros chief
    (party_get_num_prisoner_stacks, ":num_stacks", "p_salt_mine"), # TML Changed salt mine code. F123 - Submod -> 1.41
    (try_begin),
      (gt, ":escape_chance", 0),
      (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
        (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_salt_mine", ":cur_stack"),
        (party_prisoner_stack_get_size, ":stack_size","p_salt_mine",":cur_stack"),
        (try_for_range_backwards, ":unused", 0, ":stack_size"),
          (store_random_in_range,":random_no",0,100),
          (lt,":random_no",":escape_chance"),
          (party_remove_prisoners,"p_salt_mine",":cur_troop_id",1),
          (val_add, ":escape_chance", 1),
          (val_add, "$g_num_escapees", 1),
        (try_end),
      (try_end),
    (try_end),
    (assign, reg0, "$g_num_escapees"),
    (try_begin),
      (gt, reg0, 0),
      (display_message, "@{reg0} of your prisoners escaped of Salt Mine!", color_terrible_news),
    (try_end),
###chief acaba
    #(try_end),
		#(try_end),
    (call_script, "script_change_player_honor", -2),
		(party_get_num_prisoners, "$g_num_prisoners", "p_salt_mine"),
		(store_mul, ":earnings", 14, "$g_num_prisoners"), #anadido coste de los guardias chief#gdw 10 to 14. earnings still too low to be comparable to selling outright
		#(store_mul, ":earnings2", 10, "$g_num_guards"), #anadido coste de los guardias chief
    #(store_sub, ":earnings", ":earnings1", ":earnings2"), #anadido coste de los guardias chief
    (val_add, "$g_earnings", ":earnings"),
		(jump_to_menu,"mnu_slave_labor"),
  (try_end),
    #(try_end),#endTMLchanges
    ]),


#chief prisioneros en las minas acaba
##  # Pay slave labor earnings para iron mine
##   (24 * 7,
##   [
##    (try_begin),
##	  (gt, "$g_num_prisoners2", 0),
##	  (assign, "$g_earnings", 0),
##	  (assign, "$g_num_escapees", 0),
##      (try_for_range, ":center_no", "p_iron_mine", "p_test_scene"),
##	    (party_get_num_companions,"$g_num_guards2",":center_no"),
##	    (party_get_num_prisoners, "$g_num_prisoners2", ":center_no"),
##        (store_sub, ":difference", "$g_num_prisoners2", "$g_num_guards2"),
##		(try_begin),
##		  (gt, ":difference", 0),
##		  (store_random_in_range, ":random", 0, ":difference"),
##		  (try_begin),
##		    (gt, ":random", 5),
##			(store_random_in_range, ":escapees", 0, ":difference"),
##			(try_begin),
##			  (eq, ":escapees", 0),
##			  (assign, ":escapees", 1),
##			(try_end),
##			(assign, "$g_num_escapees", ":escapees"),
##            (party_get_num_prisoner_stacks, ":num_stacks", ":center_no"),
##            (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
##              (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":center_no", ":troop_iterator"),
##              (party_prisoner_stack_get_size, ":stack_size", ":center_no", ":troop_iterator"),
##			  (try_begin),
##			    (gt, ":escapees", 0),
##			    (try_begin),
##			      (gt, ":stack_size", ":escapees"),
##                  (store_sub, ":stack_sub", ":stack_size", ":escapees"),
##				  (val_sub, ":escapees", ":stack_sub"),
##				  (party_remove_prisoners, ":center_no", ":cur_troop_id", ":stack_sub"),
##				(try_end),
##			  (try_end),
##            (try_end),
##		  (try_end),
##		(try_end),
##		(party_get_num_prisoners, "$g_num_prisoners2", ":center_no"),
##		(store_mul, ":earnings", 10, "$g_num_prisoners2"),
##        (val_add, "$g_earnings", ":earnings"),
##		(jump_to_menu,"mnu_slave_labor2"),
##      (try_end),
##    (try_end),
##    ]),
###chief prisioneros en las minas acaba

#   (7 * 24,
#   [
##       (call_script, "script_get_number_of_unclaimed_centers_by_player"),
##       (assign, ":unclaimed_centers", reg0),
##       (gt, ":unclaimed_centers", 0),
# You are holding an estate without a lord.        
#       (try_for_range, ":troop_no", heroes_begin, heroes_end),
#         (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
#         (troop_get_slot, ":relation", ":troop_no", "slot_troop_player_relation"),
#         (val_sub, ":relation", 1),
#         (val_max, ":relation", -100),
#         (troop_set_slot, ":troop_no", "slot_troop_player_relation", ":relation"),
#       (try_end),
# You relation with all kingdoms other than your own has decreased by 1.     
#       (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
#         (neq, ":faction_no", "$players_kingdom"),
#         (store_relation,":faction_relation",":faction_no","fac_player_supporters_faction"),
#         (val_sub, ":faction_relation", 1),
#         (val_max, ":faction_relation", -100),
#		  WARNING: Never use set_relation!
#         (set_relation, ":faction_no", "fac_player_supporters_faction", ":faction_relation"),
#       (try_end),
#    ]),

  
  # Offer player to join faction
  # Only if the player is male -- female characters will be told that they should seek out a faction through NPCs, possibly
   (32,
   [
     (eq, "$freelancer_state", 0),	#Caba chief freelancer fixes - Added to prevent vassalage while enlisted and becoming stuck in a lord's army.  - Windy
     (eq, "$players_kingdom", 0),
     (le, "$g_invite_faction", 0),
     (eq, "$g_player_is_captive", 0),
	 (troop_get_type, ":type", "trp_player"),
    (val_mod, ":type", 2),    #gender fix chief
     (try_begin),
		(eq, ":type", 1),
		(eq, "$npc_with_sisterly_advice", 0),
		(try_for_range, ":npc", companions_begin, companions_end),
			(main_party_has_troop, ":npc"),
			(troop_get_type, ":npc_type", ":npc"),
###gender fix chief
       (this_or_next|eq, ":npc_type", 1), #male
       (this_or_next|eq, ":npc_type", 3), #male
       (this_or_next|eq, ":npc_type", 5), #male
       (eq, ":npc_type", 7), #male
#gender fix chief acaba
			(troop_slot_ge, "trp_player", "slot_troop_renown", 150),
			(troop_slot_ge, ":npc", "slot_troop_woman_to_woman_string", 1),
			(assign, "$npc_with_sisterly_advice", ":npc"),
		(try_end),
	 (else_try),
	     (store_random_in_range, ":kingdom_no", npc_kingdoms_begin, npc_kingdoms_end),
	     (assign, ":min_distance", 999999),
	     (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
	       (store_faction_of_party, ":center_faction", ":center_no"),
	       (eq, ":center_faction", ":kingdom_no"),
	       (store_distance_to_party_from_party, ":cur_distance", "p_main_party", ":center_no"),
	       (val_min, ":min_distance", ":cur_distance"),
	     (try_end),
	     (lt, ":min_distance", 30),
	     (store_relation, ":kingdom_relation", ":kingdom_no", "fac_player_supporters_faction"),
	     (faction_get_slot, ":kingdom_lord", ":kingdom_no", "slot_faction_leader"),
	     (call_script, "script_troop_get_player_relation", ":kingdom_lord"),
	     (assign, ":lord_relation", reg0),
	     #(troop_get_slot, ":lord_relation", ":kingdom_lord", "slot_troop_player_relation"),
	     (call_script, "script_get_number_of_hero_centers", "trp_player"),
	     (assign, ":num_centers_owned", reg0),
	     (eq, "$g_infinite_camping", 0),
	     	     
	     (assign, ":player_party_size", 0),	     
	     (try_begin),
	       (ge, "p_main_party", 0),
	       (store_party_size_wo_prisoners, ":player_party_size", "p_main_party"),	     
	     (try_end),  
	     
	     (try_begin),	       
	       (eq, ":num_centers_owned", 0),
	       (troop_get_slot, ":player_renown", "trp_player", "slot_troop_renown"),
	       (ge, ":player_renown", 160),
	       (ge, ":kingdom_relation", 0),
	       (ge, ":lord_relation", 0),
	       (ge, ":player_party_size", 45),
	       (store_random_in_range, ":rand", 0, 100),
	       (lt, ":rand", 50),
	       (call_script, "script_get_poorest_village_of_faction", ":kingdom_no"),
	       (assign, "$g_invite_offered_center", reg0),
	       (ge, "$g_invite_offered_center", 0),
	       (assign, "$g_invite_faction", ":kingdom_no"),
	       (jump_to_menu, "mnu_invite_player_to_faction"),
	     (else_try),
	       (gt, ":num_centers_owned", 0),
	       (neq, "$players_oath_renounced_against_kingdom", ":kingdom_no"),
	       (ge, ":kingdom_relation", -40),
	       (ge, ":lord_relation", -20),
	       (ge, ":player_party_size", 30),
	       (store_random_in_range, ":rand", 0, 100),
	       (lt, ":rand", 20),
	       (assign, "$g_invite_faction", ":kingdom_no"),
	       (assign, "$g_invite_offered_center", -1),
	       (jump_to_menu, "mnu_invite_player_to_faction_without_center"),
	     (try_end),
	 (try_end), 
    ]),

    #recalculate lord random decision seeds once in every week
	(24 * 7, 
	[
      (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
        (store_random_in_range, ":random", 0, 9999),
        (troop_set_slot, ":troop_no", "slot_troop_temp_decision_seed", ":random"),
      (try_end),   		
	
	#npcs will only change their minds on issues at least 24 hours after speaking to the player
    #(store_current_hours, ":hours"),
    #(try_begin),
    #  (eq, 1, 0), #disabled
    #  (try_for_range, ":npc", active_npcs_begin, active_npcs_end),
    #    (troop_get_slot, ":last_talk", ":npc", "slot_troop_last_talk_time"),
    #    (val_sub, ":hours", ":last_talk"),
    #    (ge, ":hours", 24),
    #    (store_random_in_range, ":random", 0, 9999),
    #    (troop_set_slot, ":npc", "slot_troop_temp_decision_seed", ":random"),
    #  (try_end),
    #(try_end),
	]),
		
  # During rebellion, removing troops from player faction randomly because of low relation points
  # Deprecated -- should be part of regular political events


  # Reset kingdom lady current centers
##   (28,
##   [
##       (try_for_range, ":troop_no", heroes_begin, heroes_end),
##         (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_lady),
##
##         # Find the active quest ladies
##         (assign, ":not_ok", 0),
##         (try_for_range, ":quest_no", lord_quests_begin, lord_quests_end),
##           (eq, ":not_ok", 0),
##           (check_quest_active, ":quest_no"),
##           (quest_slot_eq, ":quest_no", "slot_quest_object_troop", ":troop_no"),
##           (assign, ":not_ok", 1),
##         (try_end),
##         (eq, ":not_ok", 0),
##
##         (troop_get_slot, ":troop_center", ":troop_no", "slot_troop_cur_center"),
##         (assign, ":is_under_siege", 0),
##         (try_begin),
##           (is_between, ":troop_center", walled_centers_begin, walled_centers_end),
##           (party_get_battle_opponent, ":besieger_party", ":troop_center"),
##           (gt, ":besieger_party", 0),
##           (assign, ":is_under_siege", 1),
##         (try_end),
##
##         (eq, ":is_under_siege", 0),# Omit ladies in centers under siege
##
##         (try_begin),
##           (store_random_in_range, ":random_num",0, 100),
##           (lt, ":random_num", 20),
##           (store_troop_faction, ":cur_faction", ":troop_no"),
##           (call_script, "script_cf_select_random_town_with_faction", ":cur_faction"),#Can fail
##           (troop_set_slot, ":troop_no", "slot_troop_cur_center", reg0),
##         (try_end),
##       
##         (store_random_in_range, ":random_num",0, 100),
##         (lt, ":random_num", 50),
##         (troop_get_slot, ":lord_no", ":troop_no", "slot_troop_father"),
##         (try_begin),
##           (eq, ":lord_no", 0),
##           (troop_get_slot, ":lord_no", ":troop_no", "slot_troop_spouse"),
##         (try_end),
##         (gt, ":lord_no", 0),
##         (troop_get_slot, ":cur_party", ":lord_no", "slot_troop_leaded_party"),
##         (gt, ":cur_party", 0),
##         (party_get_attached_to, ":cur_center", ":cur_party"),
##         (gt, ":cur_center", 0),
##
##         (troop_set_slot, ":troop_no", "slot_troop_cur_center", ":cur_center"),
##       (try_end),
##    ]),


  # Attach Lord Parties to the town they are in
  (0.1,
   [
       (try_for_range, ":troop_no", heroes_begin, heroes_end),
         (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
         (troop_get_slot, ":troop_party_no", ":troop_no", "slot_troop_leaded_party"),
         (ge, ":troop_party_no", 1),
		 (party_is_active, ":troop_party_no"),
		 
         (party_get_attached_to, ":cur_attached_town", ":troop_party_no"),
         (lt, ":cur_attached_town", 1),
         (party_get_cur_town, ":destination", ":troop_party_no"),
         (is_between, ":destination", centers_begin, centers_end),
         (call_script, "script_get_relation_between_parties", ":destination", ":troop_party_no"),
         (try_begin),
           (ge, reg0, 0),
           (party_attach_to_party, ":troop_party_no", ":destination"),
         (else_try),
           (party_set_ai_behavior, ":troop_party_no", ai_bhvr_hold),
         (try_end),
         
         (try_begin),
           (this_or_next|party_slot_eq, ":destination", "slot_party_type", spt_town),
           (party_slot_eq, ":destination", "slot_party_type", spt_castle),
           (store_faction_of_party, ":troop_faction_no", ":troop_party_no"),
           (store_faction_of_party, ":destination_faction_no", ":destination"),
           (eq, ":troop_faction_no", ":destination_faction_no"),
           (party_get_num_prisoner_stacks, ":num_stacks", ":troop_party_no"),
           (gt, ":num_stacks", 0),
           (assign, "$g_move_heroes", 1),
           (call_script, "script_party_prisoners_add_party_prisoners", ":destination", ":troop_party_no"),#Moving prisoners to the center
           (assign, "$g_move_heroes", 1),
           (call_script, "script_party_remove_all_prisoners", ":troop_party_no"),
         (try_end),
       (try_end),
	   	   
	   (try_for_parties, ":bandit_camp"),
	 	 (gt, ":bandit_camp", "p_spawn_points_end"),
		 #Can't have party is active here, because it will fail for inactive parties
		 (party_get_template_id, ":template", ":bandit_camp"),
#		 (ge, ":template", "pt_steppe_bandit_lair"), ## CC fix, Floris: disabled
		 (is_between, ":template", "pt_steppe_bandit_lair", "pt_bandit_lair_templates_end"), ##CC fix - Caba Fix chief
		
		 (store_distance_to_party_from_party, ":distance", "p_main_party", ":bandit_camp"),
	     (lt, ":distance", 3), 
	     (party_set_flags, ":bandit_camp", pf_disabled, 0),
	     (party_set_flags, ":bandit_camp", pf_always_visible, 1),	   
	   (try_end),
    ]),

  # Check escape chances of hero prisoners.
  #AJM chief CHECK ONCE A WEEK
  #AJM PRETTY SHARPLY REDUCED ESCAPE CHANCES SO FACTION WARS ACTUALLY RESLOVE INSTEAD OF SEE-SAWING AD NAUSEUM
  (24 * 7,
   [
       (assign, ":troop_no", "trp_player"),
       (store_skill_level, ":skill", "skl_prisoner_management", ":troop_no"),
       (store_mul, ":escape_chance_reduction", ":skill", 2), #ajm 2% reduction of escape chance per rank
       (assign, ":escape_chance", 37),#gdw w PM actual skill30
       (val_sub, ":escape_chance", ":escape_chance_reduction"),

       (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "p_main_party", ":escape_chance"),
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
##         (party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
         (assign, ":escape_chance", 15),
         (val_sub, ":escape_chance", ":escape_chance_reduction"),
         (try_begin),
           (party_slot_eq, ":center_no", "slot_center_has_prisoner_tower", 1),
           (assign, ":escape_chance", 5),
           (val_sub, ":escape_chance", ":escape_chance_reduction"),
         (try_end),
         (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", ":center_no", ":escape_chance"),
       (try_end),
    ]),
####chief acaba#######

  # Asking the ownership of captured centers to the player
#  (3,
#   [
#    (assign, "$g_center_taken_by_player_faction", -1),
#    (try_for_range, ":center_no", centers_begin, centers_end),
#      (eq, "$g_center_taken_by_player_faction", -1),
#      (store_faction_of_party, ":center_faction", ":center_no"),
#      (eq, ":center_faction", "fac_player_supporters_faction"),
#      (this_or_next|party_slot_eq, ":center_no", "slot_town_lord", stl_reserved_for_player),
#      (this_or_next|party_slot_eq, ":center_no", "slot_town_lord", stl_unassigned),
#      (party_slot_eq, ":center_no", "slot_town_lord", stl_rejected_by_player),
#      (assign, "$g_center_taken_by_player_faction", ":center_no"),
#    (try_end),
#    (faction_get_slot, ":leader", "fac_player_supporters_faction", "slot_faction_leader"),

#	(try_begin),
#		(ge, "$g_center_taken_by_player_faction", 0),
		
#		(eq, "$cheat_mode", 1),
#		(str_store_party_name, s14, "$g_center_taken_by_player_faction"),
#		(display_message, "@{!}{s14} should be assigned to lord"),
#	(try_end),
	
#    ]),


  # Respawn hero party after kingdom hero is released from captivity or when lord goes missing after battlegdw
  (48, 
   [
       (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
         (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
         (str_store_troop_name, s1, ":troop_no"),
         (neg|troop_slot_ge, ":troop_no", "slot_troop_prisoner_of_party", 0),
         (neg|troop_slot_ge, ":troop_no", "slot_troop_leaded_party", 1),

         (store_troop_faction, ":cur_faction", ":troop_no"),
         (try_begin),
           (eq, ":cur_faction", "fac_outlaws"), #Do nothing
         (else_try),         
           (try_begin),
             (eq, "$cheat_mode", 2),
             (str_store_troop_name, s4, ":troop_no"),
             (display_message, "str_debug__attempting_to_spawn_s4"),
           (try_end),
           
           (call_script, "script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege", ":cur_faction", ":troop_no"),#Can fail
           (assign, ":center_no", reg0),

           (try_begin),
             (eq, "$cheat_mode", 2),
             (assign, reg7, ":center_no"),
             (str_store_party_name, s7, ":center_no"),
			 (str_store_troop_name, s0, ":troop_no"),
             (display_message, "str_debug__s0_is_spawning_around_party__s7"),
           (try_end),
       
           (call_script, "script_create_kingdom_hero_party", ":troop_no", ":center_no"),
		   (try_begin),
		     (eq, "$g_there_is_no_avaliable_centers", 0),
             (party_attach_to_party, "$pout_party", ":center_no"),
           (try_end),
           
           #new
           #(troop_get_slot, ":party_no", ":troop_no", "slot_troop_leaded_party"),
		   #(call_script, "script_npc_decision_checklist_party_ai", ":troop_no"), #This handles AI for both marshal and other parties		
		   #(call_script, "script_party_set_ai_state", ":party_no", reg0, reg1),
		   #new end

           (troop_get_slot, ":party_no", ":troop_no", "slot_troop_leaded_party"),
           (call_script, "script_party_set_ai_state", ":party_no", spai_holding_center, ":center_no"),           
           
         (else_try),
           (neg|faction_slot_eq, ":cur_faction", "slot_faction_state", sfs_active),
           (try_begin),
             (is_between, ":troop_no", kings_begin, kings_end),
             (troop_set_slot, ":troop_no", "slot_troop_change_to_faction", "fac_commoners"),
           (else_try),
             (store_random_in_range, ":random_no", 0, 100),
             (lt, ":random_no", 10),
             (call_script, "script_cf_get_random_active_faction_except_player_faction_and_faction", ":cur_faction"),
             (troop_set_slot, ":troop_no", "slot_troop_change_to_faction", reg0),
           (try_end),
         (try_end),
       (try_end),
    ]),

 #Increase castle food stores #TEMPERED chief CHANGED FROM 2 HOURS TO 24 HOURS
  (24,
   [
    ##diplomacy start+ Change to vary with village prosperity chief
   (try_begin),
       (lt, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
       ##OLD:
       #unaltered block begin
       (try_for_range, ":center_no", castles_begin, castles_end),
#siege warfare chief cambia
         (party_slot_eq, ":center_no", "slot_center_blockaded", 0),    #center not blockaded (by player) AND
         (neg|party_slot_ge, ":center_no", "slot_center_is_besieged_by", 1), #center not besieged by someone else
#siege warfare		 
         (party_get_slot, ":center_food_store", ":center_no", "slot_party_food_store"),
         (val_add, ":center_food_store", 100),
         (call_script, "script_center_get_food_store_limit", ":center_no"),
         (assign, ":food_store_limit", reg0),
         (val_min, ":center_food_store", ":food_store_limit"),
         (party_set_slot, ":center_no", "slot_party_food_store", ":center_food_store"),
       (try_end),
       #unaltered block end
   (else_try),
       ##NEW: chief
       (try_for_range, ":village_no", villages_begin, villages_end),
          (neg|party_slot_ge, ":village_no", "slot_center_is_besieged_by", 0),
          (party_slot_eq, ":village_no", "slot_village_state", svs_normal),
          (party_get_slot, ":center_no", ":village_no", "slot_village_bound_center"),
          (is_between, ":center_no", castles_begin, castles_end),
          (neg|party_slot_ge, ":center_no", "slot_center_is_besieged_by", 0),
          (party_get_slot, ":center_food_store", ":center_no", "slot_party_food_store"),
          (party_get_slot, reg0, ":village_no", "slot_town_prosperity"),
          (val_add, reg0, 75),
          (val_mul, reg0, 100),#base addition is 100
          (val_add, reg0, 62),
          (val_div, reg0, 125),#plus or minus 40%
          (val_add, ":center_food_store", reg0),
          (call_script, "script_center_get_food_store_limit", ":center_no"),
          (assign, ":food_store_limit", reg0),
          (val_min, ":center_food_store", ":food_store_limit"),
          (party_set_slot, ":center_no", "slot_party_food_store", ":center_food_store"),
       (try_end),
   (try_end),
#chief acaba
    ]),

 #Comida extra para ciudades y castillos con puerto chief Siege Warfare
 (24,
  [
  (party_is_active, "$g_encountered_party"),
  (party_slot_eq,"$g_encountered_party","slot_town_port", 1),
  (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
#siege warfare chief cambia
         (party_slot_eq, ":center_no", "slot_center_blockaded", 0),    #center not blockaded (by player) AND
         (neg|party_slot_ge, ":center_no", "slot_center_is_besieged_by", 1), #center not besieged by someone else
#siege warfare		 
         (party_get_slot, ":center_food_store", ":center_no", "slot_party_food_store"),
         (val_add, ":center_food_store", 100),
         (call_script, "script_center_get_food_store_limit", ":center_no"),
         (assign, ":food_store_limit", reg0),
         (val_min, ":center_food_store", ":food_store_limit"),
         (party_set_slot, ":center_no", "slot_party_food_store", ":center_food_store"),
       (try_end),
    ]),



 #cache party strengths (to avoid re-calculating)
##  (2,
##   [
##       (try_for_range, ":cur_troop", heroes_begin, heroes_end),
##         (troop_slot_eq, ":cur_troop", "slot_troop_occupation", slto_kingdom_hero),
##         (troop_get_slot, ":cur_party", ":cur_troop", "slot_troop_leaded_party"),
##         (ge, ":cur_party", 0),
##         (call_script, "script_party_calculate_strength", ":cur_party", 0), #will update "slot_party_cached_strength"
##       (try_end),
##    ]),
##  
##  (6,
##   [
##       (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
##         (call_script, "script_party_calculate_strength", ":cur_center", 0), #will update "slot_party_cached_strength"
##       (try_end),
##    ]),

##  (1,
##   [
##       (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
##         (store_random_in_range, ":rand", 0, 100),
##         (lt, ":rand", 10),
##         (store_faction_of_party, ":center_faction", ":cur_center"),
##         (assign, ":friend_strength", 0),
##         (try_for_range, ":cur_troop", heroes_begin, heroes_end),
##           (troop_slot_eq, ":cur_troop", "slot_troop_occupation", slto_kingdom_hero),
##           (troop_get_slot, ":cur_troop_party", ":cur_troop", "slot_troop_leaded_party"),
##           (gt, ":cur_troop_party", 0),
##           (store_distance_to_party_from_party, ":distance", ":cur_troop_party", ":cur_center"),
##           (lt, ":distance", 10),
##           (store_troop_faction, ":army_faction", ":cur_troop"),
##           (store_relation, ":rel", ":army_faction", ":center_faction"),
##           (try_begin),
##             (gt, ":rel", 10),
##             (party_get_slot, ":str", ":cur_troop_party", "slot_party_cached_strength"),
##             (val_add, ":friend_strength", ":str"),
##           (try_end),
##         (try_end),
##         (party_set_slot, ":cur_center", "slot_party_nearby_friend_strength", ":friend_strength"),
##       (try_end),
##    ]),

  # Make heroes running away from someone retreat to friendly centers
  (0.5,
   [
       (try_for_range, ":cur_troop", heroes_begin, heroes_end),
         (troop_slot_eq, ":cur_troop", "slot_troop_occupation", slto_kingdom_hero),
         (troop_get_slot, ":cur_party", ":cur_troop", "slot_troop_leaded_party"),
         (gt, ":cur_party", 0),
         (try_begin),
           (party_is_active, ":cur_party"),
           (try_begin),
             (get_party_ai_current_behavior, ":ai_bhvr", ":cur_party"),
             (eq, ":ai_bhvr", ai_bhvr_avoid_party),
			 
			 #Certain lord personalities will not abandon a battlefield to flee to a fortress
			 (assign, ":continue", 1),
			 (try_begin),
				(this_or_next|troop_slot_eq, ":cur_troop", "slot_lord_reputation_type", lrep_upstanding),
					(troop_slot_eq, ":cur_troop", "slot_lord_reputation_type", lrep_martial),
				(get_party_ai_current_object, ":ai_object", ":cur_party"),
				(party_is_active, ":ai_object"),
				(party_get_battle_opponent, ":battle_opponent", ":ai_object"),
				(party_is_active, ":battle_opponent"),
				(assign, ":continue", 0),
			 (try_end),
			 (eq, ":continue", 1),
			 
			 
             (store_faction_of_party, ":party_faction", ":cur_party"),
             (party_get_slot, ":commander_party", ":cur_party", "slot_party_commander_party"),
             (faction_get_slot, ":faction_marshall", ":party_faction", "slot_faction_marshall"),
             (neq, ":faction_marshall", ":cur_troop"),
             (assign, ":continue", 1),
             (try_begin),
               (ge, ":faction_marshall", 0),
               (troop_get_slot, ":faction_marshall_party", ":faction_marshall", "slot_troop_leaded_party"),
               (party_is_active, ":faction_marshall_party", 0),
               (eq, ":commander_party", ":faction_marshall_party"),
               (assign, ":continue", 0),
             (try_end),
             (eq, ":continue", 1),
             (assign, ":done", 0),
             (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
               (eq, ":done", 0),
               (party_slot_eq, ":cur_center", "slot_center_is_besieged_by", -1),
               (store_faction_of_party, ":center_faction", ":cur_center"),
               (store_relation, ":cur_relation", ":center_faction", ":party_faction"),
               (gt, ":cur_relation", 0),
               (store_distance_to_party_from_party, ":cur_distance", ":cur_party", ":cur_center"),
               (lt, ":cur_distance", 20),
               (party_get_position, pos1, ":cur_party"),
               (party_get_position, pos2, ":cur_center"),
               (neg|position_is_behind_position, pos2, pos1),
               (call_script, "script_party_set_ai_state", ":cur_party", spai_retreating_to_center, ":cur_center"),
               (assign, ":done", 1),
             (try_end),
           (try_end),
         (else_try),
           (troop_set_slot, ":cur_troop", "slot_troop_leaded_party", -1),
         (try_end),
       (try_end),
    ]),

  # Centers give alarm if the player is around
  (0.5,
   [
     (store_current_hours, ":cur_hours"),
     (store_mod, ":cur_hours_mod", ":cur_hours", 11),
     (store_sub, ":hour_limit", ":cur_hours", 5),
     (party_get_num_companions, ":num_men", "p_main_party"),
     (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
     (val_add, ":num_men", ":num_prisoners"),
     (convert_to_fixed_point, ":num_men"),
     (store_sqrt, ":num_men_effect", ":num_men"),
     (convert_from_fixed_point, ":num_men_effect"),
     (try_begin),
       (eq, ":cur_hours_mod", 0),
       #Reduce alarm by 2 in every 11 hours.
       (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
         (faction_get_slot, ":player_alarm", ":cur_faction", "slot_faction_player_alarm"),
         (val_sub, ":player_alarm", 1),
         (val_max, ":player_alarm", 0),
         (faction_set_slot, ":cur_faction", "slot_faction_player_alarm", ":player_alarm"),
       (try_end),
     (try_end),
     (eq, "$g_player_is_captive", 0),
     (try_for_range, ":cur_center", centers_begin, centers_end),
       (store_faction_of_party, ":cur_faction", ":cur_center"),
       (store_relation, ":reln", ":cur_faction", "fac_player_supporters_faction"),
       (lt, ":reln", 0),
       (store_distance_to_party_from_party, ":dist", "p_main_party", ":cur_center"),
       (lt, ":dist", 5),
       (store_mul, ":dist_sqr", ":dist", ":dist"),
       (store_sub, ":dist_effect", 20, ":dist_sqr"),
       (store_sub, ":reln_effect", 20, ":reln"),
       (store_mul, ":total_effect", ":dist_effect", ":reln_effect"),
       (val_mul, ":total_effect", ":num_men_effect"),
       (store_div, ":spot_chance", ":total_effect", 10),
       (store_random_in_range, ":random_spot", 0, 1000),
       (lt, ":random_spot", ":spot_chance"),
       (faction_get_slot, ":player_alarm", ":cur_faction", "slot_faction_player_alarm"),
       (val_add, ":player_alarm", 1),
       (val_min, ":player_alarm", 100),
       (faction_set_slot, ":cur_faction", "slot_faction_player_alarm", ":player_alarm"),
       (try_begin),
         (neg|party_slot_ge, ":cur_center", "slot_center_last_player_alarm_hour", ":hour_limit"),
         (str_store_party_name_link, s1, ":cur_center"),
         (display_message, "@Your party is spotted by {s1}."),
         (party_set_slot, ":cur_center", "slot_center_last_player_alarm_hour", ":cur_hours"),
       (try_end),
     (try_end),
    ]),
  
  # Consuming food at every 14 hours
  #AJM chief THIS IS MOUNT & BLADE, NOT FOOD MANAGEMENT AND ENTERPRISE
  #AJM chief EAT 1X A DAY, EACH UNIT EATS 1 FOOD UNIT
  #AJM chief RELEVANT: I TRIPLED THE FOOD QUANTITY OF ALL FOOD ITEMS W/O CHANGING WEIGHT OR PRICE
  #AJM chief ALL THIS REALLY DOES IS MAKE EASIER TO EYE-BALL HOW MUCH FOOD YOU GOT LEFT. 1 UNIT OF FOOD = 1 GUY FED PER DAY.
  (24,
   [#(store_sub, ":num_food", food_end, food_begin),
    (eq, "$g_player_is_captive", 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
      (val_add, ":num_men", ":stack_size"),
    (try_end),
    #AJM WAS DIVIDED BY 3, CHANGED TO 1 SO 1 GUY = 1 FOOD UNIT EATEN
    (val_div, ":num_men", 1),
    (try_begin),
      (eq, ":num_men", 0),
      (val_add, ":num_men", 1),
    (try_end),
#original    
    (try_begin),
      (assign, ":number_of_foods_player_has", 0),
      (try_for_range, ":cur_edible", food_begin, food_end),      
        (call_script, "script_cf_player_has_item_without_modifier", ":cur_edible", imod_rotten),
        (val_add, ":number_of_foods_player_has", 1),
      (try_end),
      (try_begin),
        (ge, ":number_of_foods_player_has", 6),
        (unlock_achievement, ACHIEVEMENT_ABUNDANT_FEAST),        
      (try_end),
    (try_end),
#original acaba
    ## Jrider chief
    (call_script, "script_forage_for_food"),

    # backup original number for message display
    (assign, ":orig_men", ":num_men"),
    (try_begin),
      # set min consumption to 1 unit of food in inventory
      (ge, reg4, ":num_men"),
      (assign, ":num_men", 1),
    (else_try),
      # else deduct foraged amount from consumed from party size
      (val_sub, ":num_men", reg4),
    (try_end),
    ## Jrider chief -

    
    (assign, ":consumption_amount", ":num_men"),
    (assign, ":no_food_displayed", 0),
    (try_for_range, ":unused", 0, ":consumption_amount"),
      (assign, ":available_food", 0),
      (try_for_range, ":cur_food", food_begin, food_end),
        (item_set_slot, ":cur_food", "slot_item_is_checked", 0),
        (call_script, "script_cf_player_has_item_without_modifier", ":cur_food", imod_rotten),
        (val_add, ":available_food", 1),
      (try_end),
      (try_begin),
        (gt, ":available_food", 0),
        (store_random_in_range, ":selected_food", 0, ":available_food"),
        (call_script, "script_consume_food", ":selected_food"),
      (else_try),
        (eq, ":no_food_displayed", 0),
        (display_message, "@Your men have nothing to eat!", 0xFF0000),
        (call_script, "script_change_player_party_morale", -3),
        (assign, ":no_food_displayed", 1),
#NPC companion changes begin
        (try_begin),
            (call_script, "script_party_count_fit_regulars", "p_main_party"),
            (gt, reg0, 0),
            (call_script, "script_objectionable_action", tmt_egalitarian, "str_men_hungry"),
        (try_end),
#NPC companion changes end
      (try_end),
    (try_end),
    ## Jrider chief
    (call_script, "script_food_consumption_display_message", ":orig_men"),
    ## Jrider - chief
    ]),

  # Setting item modifiers for food
  (24,
   [
     (troop_get_inventory_capacity, ":inv_size", "trp_player"),
     (try_for_range, ":i_slot", 0, ":inv_size"),
       (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
       (this_or_next|eq, ":item_id", "itm_cattle_meat"),
       (this_or_next|eq, ":item_id", "itm_boar_meat"), 
		   (this_or_next|eq, ":item_id", "itm_pork"),#gdwfixforfreshmeat
            (this_or_next|eq, ":item_id", "itm_deer_meat"),
            (this_or_next|eq, ":item_id", "itm_boar_meat"),
            (this_or_next|eq, ":item_id", "itm_wolf_meat"),
            (this_or_next|eq, ":item_id", "itm_goat_meat"),
            (this_or_next|eq, ":item_id", "itm_goatb_meat"),
            (this_or_next|eq, ":item_id", "itm_wilddonkey_meat"),
				(eq, ":item_id", "itm_chicken"),
       (troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":i_slot"),
       (try_begin),
         (ge, ":modifier", imod_fresh),
         (lt, ":modifier", imod_rotten),
         (val_add, ":modifier", 1),
         (troop_set_inventory_slot_modifier, "trp_player", ":i_slot", ":modifier"),
       (else_try),
         (lt, ":modifier", imod_fresh),
         (troop_set_inventory_slot_modifier, "trp_player", ":i_slot", imod_fresh),
       (try_end),
     (try_end),
    ]),

  # Assigning lords to centers with no leaders
  # (72,
   # [
   #(call_script, "script_assign_lords_to_empty_centers"),
    # ]),
  
  # Updating player icon in every frame
  (0,
   [(troop_get_inventory_slot, ":cur_horse", "trp_player", 8), #horse slot
    (assign, ":new_icon", -1),
    (try_begin),
      (eq, "$g_player_icon_state", pis_normal),
      (try_begin),
        (ge, ":cur_horse", 0),
        (assign, ":new_icon", "icon_player_horseman"),
      (else_try),
        (assign, ":new_icon", "icon_player"),
      (try_end),
    (else_try),
      (eq, "$g_player_icon_state", pis_camping),
#motomataru fix camping on water chief
      # (assign, ":new_icon", "icon_camp_plain"), #tempered chief cambiado
      (party_get_current_terrain,":terrain","p_main_party"),
      (try_begin),
        (neq, ":terrain", 0),	#not rt_water
        (neq, ":terrain", 7),	#not rt_bridge used as water terrain
        (neq, ":terrain", 8),	#not rt_bridge used as water terrain
        (assign, ":new_icon", "icon_camp_plain"),
      (else_try),
        (assign, ":new_icon", "icon_ship_on_land"),
      (try_end),
#end motomataru fix camping on water
    (else_try),
      (eq, "$g_player_icon_state", pis_ship),
      (assign, ":new_icon", "icon_ship"),
    (try_end),
    (neq, ":new_icon", "$g_player_party_icon"),
    (assign, "$g_player_party_icon", ":new_icon"),
    (party_set_icon, "p_main_party", ":new_icon"),
    ]),
  
 #Update how good a target player is for bandits bandidos atacan a player con mucho dinero chief
  (2,
   [
       (store_troop_gold, ":total_value", "trp_player"),
       (store_div, ":bandit_attraction", ":total_value", (200000/100)), #20000 gold = excellent_target chief anade un 0

       (troop_get_inventory_capacity, ":inv_size", "trp_player"),
       (try_for_range, ":i_slot", 0, ":inv_size"),
         (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
         (ge, ":item_id", 0),
         (try_begin),
           (is_between, ":item_id", trade_goods_begin, trade_goods_end),
           (store_item_value, ":item_value", ":item_id"),
           (val_add, ":total_value", ":item_value"),
         (try_end),
       (try_end),
       (val_clamp, ":bandit_attraction", 0, 100),
       (party_set_bandit_attraction, "p_main_party", ":bandit_attraction"),
    ]),


	#This is a backup script to activate the player faction if it doesn't happen automatically, for whatever reason
  (3,
	[
	(try_for_range, ":center", walled_centers_begin, walled_centers_end),
		(faction_slot_eq, "fac_player_supporters_faction", "slot_faction_state", sfs_inactive),
		(store_faction_of_party, ":center_faction", ":center"),
		(eq, ":center_faction", "fac_player_supporters_faction"),
		(call_script, "script_activate_player_faction", "trp_player"),
	(try_end),
	]),
	
  # Checking escape chances of prisoners that joined the party recently.
  (6,
   [(gt, "$g_prisoner_recruit_troop_id", 0),
    (gt, "$g_prisoner_recruit_size", 0),
    (gt, "$g_prisoner_recruit_last_time", 0),
    (is_currently_night),
    (try_begin),
      (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
      (val_mul, ":leadership", 5),
      (store_sub, ":chance", 66, ":leadership"),
      (gt, ":chance", 0),
      (assign, ":num_escaped", 0),
      (try_for_range, ":unused", 0, "$g_prisoner_recruit_size"),
        (store_random_in_range, ":random_no", 0, 100),
        (lt, ":random_no", ":chance"),
        (val_add, ":num_escaped", 1),
      (try_end),
      (party_remove_members, "p_main_party", "$g_prisoner_recruit_troop_id", ":num_escaped"),
      (assign, ":num_escaped", reg0),
      (gt, ":num_escaped", 0),
      (try_begin),
        (gt, ":num_escaped", 1),
        (assign, reg2, 1),
      (else_try),
        (assign, reg2, 0),
      (try_end),
      (assign, reg1, ":num_escaped"),
      (str_store_troop_name_by_count, s1, "$g_prisoner_recruit_troop_id", ":num_escaped"),
      (display_log_message, "@{reg1} {s1} {reg2?have:has} escaped from your party during the night.", color_bad_news),
    (try_end),
    (assign, "$g_prisoner_recruit_troop_id", 0),
    (assign, "$g_prisoner_recruit_size", 0),
    ]),

  # Offering ransom fees for player's prisoner heroes
  (24,
   [(neq, "$g_ransom_offer_rejected", 1),
    (call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", "p_main_party"),
    (eq, reg0, 0),#no prisoners offered
    (assign, ":end_cond", walled_centers_end),
    (try_for_range, ":center_no", walled_centers_begin, ":end_cond"),
      (party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
      (call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", ":center_no"),
      (eq, reg0, 1),#a prisoner is offered
      (assign, ":end_cond", 0),#break
    (try_end),
    ]), 

  # Exchanging hero prisoners between factions and clearing old ransom offers
  (72,
   [(assign, "$g_ransom_offer_rejected", 0),
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
      (party_get_slot, ":town_lord", ":center_no", "slot_town_lord"),
      (gt, ":town_lord", 0),
      (party_get_num_prisoner_stacks, ":num_stacks", ":center_no"),
      (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
        (party_prisoner_stack_get_troop_id, ":stack_troop", ":center_no", ":i_stack"),
        (troop_is_hero, ":stack_troop"),
        (troop_slot_eq, ":stack_troop", "slot_troop_occupation", slto_kingdom_hero),
        (store_random_in_range, ":random_no", 0, 100),
        (try_begin),
          (le, ":random_no", 10),
          (call_script, "script_calculate_ransom_amount_for_troop", ":stack_troop"),
          (assign, ":ransom_amount", reg0),
          (troop_get_slot, ":wealth", ":town_lord", "slot_troop_wealth"),
          (val_add, ":wealth", ":ransom_amount"),
          (troop_set_slot, ":town_lord", "slot_troop_wealth", ":wealth"),
          (party_remove_prisoners, ":center_no", ":stack_troop", 1),
          (call_script, "script_remove_troop_from_prison", ":stack_troop"),
          (store_troop_faction, ":faction_no", ":town_lord"),
          (store_troop_faction, ":troop_faction", ":stack_troop"),
          (str_store_troop_name, s1, ":stack_troop"),
          (str_store_faction_name, s2, ":faction_no"),
          (str_store_faction_name, s3, ":troop_faction"),
          ## CC chief
          (faction_get_color, ":faction_color", ":troop_faction"),
          (display_log_message, "@{s1} of {s3} has been released from captivity.", ":faction_color"),
          ## CC
#          (display_log_message, "@{s1} of {s3} has been released from captivity."),
        (try_end),
      (try_end),
    (try_end),
    ]),
  
  # Adding mercenary troops to the towns
  (72,
   [
     (call_script, "script_update_mercenary_units_of_towns"),
     #NPC changes begin
     # removes   (call_script, "script_update_companion_candidates_in_taverns"),
     #NPC changes end
     (call_script, "script_update_ransom_brokers"),
     (call_script, "script_update_tavern_travellers"),
     (call_script, "script_update_tavern_minstrels"),
     (call_script, "script_update_booksellers"),
    ]),

#reclutar en ciudades chief
  (72,
   [
       (try_for_range, ":town_no", towns_begin, towns_end),
       (call_script, "script_update_volunteer_troops_in_village", ":town_no"),
       (call_script, "script_update_npc_volunteer_troops_in_village", ":town_no"),
     (try_end),
    ]),
#reclutar en ciudades acaba

  (24,
   [	
    (call_script, "script_update_other_taverngoers"),
	]),
	
  # Setting random walker types
  (36,
   [(try_for_range, ":center_no", centers_begin, centers_end),
#      (this_or_next|party_slot_eq, ":center_no", "slot_party_type", spt_town),
#      (             party_slot_eq, ":center_no", "slot_party_type", spt_village),
      (call_script, "script_center_remove_walker_type_from_walkers", ":center_no", walkert_needs_money),
      (call_script, "script_center_remove_walker_type_from_walkers", ":center_no", walkert_needs_money_helped),
      (store_random_in_range, ":rand", 0, 100),
      (try_begin),
        (lt, ":rand", 70),
        (neg|party_slot_ge, ":center_no", "slot_town_prosperity", 60),
        (call_script, "script_cf_center_get_free_walker", ":center_no"),
        (call_script, "script_center_set_walker_to_type", ":center_no", reg0, walkert_needs_money),
      (try_end),
    (try_end),
    ]),

  # Checking center upgrades
  (12,#"mill"
   [(try_for_range, ":center_no", centers_begin, centers_end),
      (party_get_slot, ":cur_improvement", ":center_no", "slot_center_current_improvement"),
      (gt, ":cur_improvement", 0),
      (party_get_slot, ":cur_improvement_end_time", ":center_no", "slot_center_improvement_end_hour"),
      (store_current_hours, ":cur_hours"),
      (ge, ":cur_hours", ":cur_improvement_end_time"),
      (party_set_slot, ":center_no", ":cur_improvement", 1),
      (party_set_slot, ":center_no", "slot_center_current_improvement", 0),
      (call_script, "script_get_improvement_details", ":cur_improvement"),
      (try_begin),
        (party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
        (str_store_party_name, s4, ":center_no"),
        (display_log_message, "@Building of {s0} in {s4} has been completed.", color_quest_and_faction_news),
      (try_end),
      (try_begin),
        (is_between, ":center_no", villages_begin, villages_end),
        (eq, ":cur_improvement", "slot_center_has_fish_pond"),
       (call_script, "script_change_center_prosperity", ":center_no", 5),
      (try_end),
    (try_end),
    ]),

  # Adding bandits to towns and villages
  (24, [
    (try_for_range, ":center_no", centers_begin, centers_end),
      (this_or_next|party_slot_eq, ":center_no", "slot_party_type", spt_town),
      (party_slot_eq, ":center_no", "slot_party_type", spt_village),
      (party_get_slot, ":has_bandits", ":center_no", "slot_center_has_bandits"),
      (try_begin),
        (le, ":has_bandits", 0),
        (assign, ":continue", 0),
        (try_begin),
          (check_quest_active, "qst_deal_with_night_bandits"),
          (quest_slot_eq, "qst_deal_with_night_bandits", "slot_quest_target_center", ":center_no"),
          (neg|check_quest_succeeded, "qst_deal_with_night_bandits"),
          (assign, ":continue", 1),
        (else_try),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", 3),
          (assign, ":continue", 1),
        (try_end),
        (try_begin),
          (eq, ":continue", 1),
          (store_random_in_range, ":random_no", 0, 3),
          (try_begin),
            (eq, ":random_no", 0),
            (assign, ":bandit_troop", "trp_bandit"),
          (else_try),
            (eq, ":random_no", 1),
            (assign, ":bandit_troop", "trp_mountain_bandit"),
          (else_try),
            (assign, ":bandit_troop", "trp_forest_bandit"),
          (try_end),
          (party_set_slot, ":center_no", "slot_center_has_bandits", ":bandit_troop"),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s1, ":center_no"),
            (display_message, "@{!}{s1} is infested by bandits (at night)."),
          (try_end),
        (try_end),
      (else_try),
        (try_begin),
          (assign, ":random_chance", 40),
          (try_begin),
            (party_slot_eq, ":center_no", "slot_party_type", spt_town),
            (assign, ":random_chance", 20),
          (try_end),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", ":random_chance"),
          (party_set_slot, ":center_no", "slot_center_has_bandits", 0),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s1, ":center_no"),
            (display_message, "@{s1} is no longer infested by bandits (at night)."),
          (try_end),
        (try_end),
      (try_end),
    (try_end),
    ]),

#(0.1,

#	[
#	(try_begin),
#		(troop_slot_ge, "trp_player", "slot_troop_spouse", active_npcs_begin),
#		(troop_get_slot, ":spouse", "trp_player", "slot_troop_spouse"),
#		(store_faction_of_troop, ":spouse_faction", ":spouse"),
#		(neq, ":spouse_faction", "$players_kingdom"),
#		(display_message, "@{!}ERROR! Player and spouse are separate factions"),
#	(try_end),
#	]
#),
	
  # Asking to give center to player
  # (8,
   # [
#    (assign, ":done", 0),
#    (try_for_range, ":center_no", centers_begin, centers_end),
#      (eq, ":done", 0),
#      (party_slot_eq, ":center_no", "slot_town_lord", stl_reserved_for_player),
#      (assign, "$g_center_to_give_to_player", ":center_no"),
 #     (try_begin),
  #      (eq, "$g_center_to_give_to_player", "$g_castle_requested_by_player"),
   #     (assign, "$g_castle_requested_by_player", 0),
	#	(try_begin),
	#		(eq, "$g_castle_requested_for_troop", "trp_player"),
	#		(jump_to_menu, "mnu_requested_castle_granted_to_player"),
	#	(else_try),
	#		(jump_to_menu, "mnu_requested_castle_granted_to_player_husband"),
	#	(try_end),	
    #  (else_try),
    #    (jump_to_menu, "mnu_give_center_to_player"),
    # (try_end),
    #  (assign, ":done", 1),
    #(else_try),
    #  (eq, ":center_no", "$g_castle_requested_by_player"),
    #  (party_slot_ge, ":center_no", "slot_town_lord", active_npcs_begin),
    #  (assign, "$g_castle_requested_by_player", 0),
    #  (store_faction_of_party, ":faction", ":center_no"),
    #  (eq, ":faction", "$players_kingdom"),
    #  (assign, "$g_center_to_give_to_player", ":center_no"),
	#  (try_begin),
#		(eq, "$player_has_homage", 1),
#		(jump_to_menu, "mnu_requested_castle_granted_to_another"),
#	  (else_try),	
#		(jump_to_menu, "mnu_requested_castle_granted_to_another_female"),
#	  (try_end),	
 #     (assign, ":done", 1),
  #  (try_end),
    # ]),
   
  # Taking denars from player while resting in not owned centers
  (1,
   [(neg|map_free),
    (is_currently_night),
#    (ge, "$g_last_rest_center", 0),
    (is_between, "$g_last_rest_center", centers_begin, centers_end),
    (neg|party_slot_eq, "$g_last_rest_center", "slot_town_lord", "trp_player"),

##diplomacy chief begin
    (party_get_slot, ":town_lord", "$g_last_rest_center", "slot_town_lord"),
    (assign, reg0, 0),
    (try_begin),
      (is_between, ":town_lord", lords_begin, kingdom_ladies_end),
      (call_script, "script_dplmc_is_affiliated_family_member", ":town_lord"),
      (try_begin),
        (neq, reg0, 0),
        (display_message, "@You are within the walls of an affiliated family member and don't have to pay for accommodation."),
      (try_end),
    (try_end),
    (eq, reg0, 0),
##diplomacy end

    (store_faction_of_party, ":last_rest_center_faction", "$g_last_rest_center"),
    (neq, ":last_rest_center_faction", "fac_player_supporters_faction"),
    (store_current_hours, ":cur_hours"),
    (ge, ":cur_hours", "$g_last_rest_payment_until"),
    (store_add, "$g_last_rest_payment_until", ":cur_hours", 24),
    (store_troop_gold, ":gold", "trp_player"),
    (party_get_num_companions, ":num_men", "p_main_party"),
    (store_div, ":total_cost", ":num_men", 4),
    (val_add, ":total_cost", 1),
    (try_begin),
      (ge, ":gold", ":total_cost"),
      (display_message, "@You pay for accommodation."),
      (troop_remove_gold, "trp_player", ":total_cost"),
    (else_try),
      (gt, ":gold", 0),
      (troop_remove_gold, "trp_player", ":gold"),
    (try_end),
    ]),
    
  # Spawn some bandits. Chief cambia el tiempo de spwan de bandidos
  (72,
   [
       (call_script, "script_spawn_bandits"),
    ]),

  # Make parties larger as game progresses.
  (24,
   [
       (call_script, "script_update_party_creation_random_limits"),
    ]),
  
  # Check if a faction is defeated every day
  (24,
   [
    (assign, ":num_active_factions", 0),
    (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_set_slot, ":cur_kingdom", "slot_faction_number_of_parties", 0),
    (try_end),
    (try_for_parties, ":cur_party"),
      (store_faction_of_party, ":party_faction", ":cur_party"),
      (is_between, ":party_faction", kingdoms_begin, kingdoms_end),
      (this_or_next|is_between, ":cur_party", centers_begin, centers_end),
		(party_slot_eq, ":cur_party", "slot_party_type", spt_kingdom_hero_party),
      (faction_get_slot, ":kingdom_num_parties", ":party_faction", "slot_faction_number_of_parties"),
      (val_add, ":kingdom_num_parties", 1),
      (faction_set_slot, ":party_faction", "slot_faction_number_of_parties", ":kingdom_num_parties"),
    (try_end),
    (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
##      (try_begin),
##        (eq, "$cheat_mode", 1),
##        (str_store_faction_name, s1, ":cur_kingdom"),
##        (faction_get_slot, reg1, ":cur_kingdom", "slot_faction_number_of_parties"),
##        (display_message, "@{!}Number of parties belonging to {s1}: {reg1}"),
##      (try_end),
      (faction_slot_eq, ":cur_kingdom", "slot_faction_state", sfs_active),
      (val_add, ":num_active_factions", 1),
      (faction_slot_eq, ":cur_kingdom", "slot_faction_number_of_parties", 0),
      (assign, ":faction_removed", 0),
      (try_begin),
        (eq, ":cur_kingdom", "fac_player_supporters_faction"),
        (try_begin),
          (le, "$supported_pretender", 0),
          (faction_set_slot, ":cur_kingdom", "slot_faction_state", sfs_inactive),
          (assign, ":faction_removed", 1),
        (try_end),
      (else_try),
        (neq, "$players_kingdom", ":cur_kingdom"),
        (faction_set_slot, ":cur_kingdom", "slot_faction_state", sfs_defeated),
        (try_for_parties, ":cur_party"),
          (store_faction_of_party, ":party_faction", ":cur_party"),
          (eq, ":party_faction", ":cur_kingdom"),
          (party_get_slot, ":home_center", ":cur_party", "slot_party_home_center"),
          (store_faction_of_party, ":home_center_faction", ":home_center"),
          (party_set_faction, ":cur_party", ":home_center_faction"),
        (try_end),
        (assign, ":kingdom_pretender", -1),
        (try_for_range, ":cur_pretender", pretenders_begin, pretenders_end),
          (troop_slot_eq, ":cur_pretender", "slot_troop_original_faction", ":cur_kingdom"),
          (assign, ":kingdom_pretender", ":cur_pretender"),
        (try_end),
        (try_begin),
          (is_between, ":kingdom_pretender", pretenders_begin, pretenders_end),
          (neq, ":kingdom_pretender", "$supported_pretender"),
          (troop_set_slot, ":kingdom_pretender", "slot_troop_cur_center", 0), #remove pretender from the world
        (try_end),
        (assign, ":faction_removed", 1),
        (try_begin),
          (eq, "$players_oath_renounced_against_kingdom", ":cur_kingdom"),
          (assign, "$players_oath_renounced_against_kingdom", 0),
          (assign, "$players_oath_renounced_given_center", 0),
          (assign, "$players_oath_renounced_begin_time", 0),
          (call_script, "script_add_notification_menu", "mnu_notification_oath_renounced_faction_defeated", ":cur_kingdom", 0),
        (try_end),
        #This menu must be at the end because faction banner will change after this menu if the player's supported pretender's original faction is cur_kingdom
        (call_script, "script_add_notification_menu", "mnu_notification_faction_defeated", ":cur_kingdom", 0),
        ## start peace CC chief
        (try_for_range, ":other_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
          (neq, ":other_kingdom", ":cur_kingdom"),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", ":cur_kingdom", ":other_kingdom", 0),
        (try_end),
##CC chief acaba
      (try_end),
      (try_begin),
        (eq, ":faction_removed", 1),
        (val_sub, ":num_active_factions", 1),
        #(call_script, "script_store_average_center_value_per_faction"),
      (try_end),
      (try_for_range, ":cur_kingdom_2", kingdoms_begin, kingdoms_end),
        (call_script, "script_update_faction_notes", ":cur_kingdom_2"),
      (try_end),
    (try_end),
    (try_begin),
      (eq, ":num_active_factions", 1),
      (eq, "$g_one_faction_left_notification_shown", 0),
      (assign, "$g_one_faction_left_notification_shown", 1),
      (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":cur_kingdom", "slot_faction_state", sfs_active),
        (call_script, "script_add_notification_menu", "mnu_notification_one_faction_left", ":cur_kingdom", 0),
      (try_end),
    (try_end),
    ]),

  (3, #check to see if player's court has been captured
   [
     (try_begin), #The old court has been lost
     ##diplomacy chief begin
       (is_between, "$g_player_court", centers_begin, centers_end),
       (party_slot_eq, "$g_player_court", "slot_village_infested_by_bandits", "trp_peasant_woman"),
       (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
     (else_try),
     ##diplomacy chief end
       (is_between, "$g_player_court", centers_begin, centers_end),
       (store_faction_of_party, ":court_faction", "$g_player_court"),
       (neq, ":court_faction", "fac_player_supporters_faction"),
       (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
     (else_try),	#At least one new court has been found
       (lt, "$g_player_court", centers_begin),
       #Will by definition not active until a center is taken by the player faction
       #Player minister must have been appointed at some point
       (this_or_next|faction_slot_eq, "fac_player_supporters_faction", "slot_faction_leader", "trp_player"),
		(gt, "$g_player_minister", 0),
		
       (assign, ":center_found", 0),
       (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
         (eq, ":center_found", 0),
         (store_faction_of_party, ":court_faction", ":walled_center"),
         (eq, ":court_faction", "fac_player_supporters_faction"),
         (assign, ":center_found", ":walled_center"),
       (try_end),
       (ge, ":center_found", 1),
       (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
     (try_end),
     #Also, piggy-backing on this -- having bandits go to lairs and back
     (try_for_parties, ":bandit_party"),
       (gt, ":bandit_party", "p_spawn_points_end"),
       (party_get_template_id, ":bandit_party_template", ":bandit_party"),
       (is_between, ":bandit_party_template", "pt_steppe_bandits", "pt_deserters"),
       (party_template_get_slot, ":bandit_lair", ":bandit_party_template", "slot_party_template_lair_party"),
       (try_begin),#If party is active and bandit is far away, then move to location
         (gt, ":bandit_lair", "p_spawn_points_end"),
         (store_distance_to_party_from_party, ":distance", ":bandit_party", ":bandit_lair"), #this is the cause of the error
         (gt, ":distance", 30),
         #All this needs checking
         (party_set_ai_behavior, ":bandit_party", ai_bhvr_travel_to_point),
         (party_get_position, pos5, ":bandit_lair"),
         (party_set_ai_target_position, ":bandit_party", pos5),
       (else_try), #Otherwise, act freely
         (get_party_ai_behavior, ":behavior", ":bandit_party"),
         (eq, ":behavior", ai_bhvr_travel_to_point),
         (try_begin),
           (gt, ":bandit_lair", "p_spawn_points_end"),
           (store_distance_to_party_from_party, ":distance", ":bandit_party", ":bandit_lair"),
           (lt, ":distance", 3),
           (party_set_ai_behavior, ":bandit_party", ai_bhvr_patrol_party),
           (party_template_get_slot, ":spawnpoint", ":bandit_party_template", "slot_party_template_lair_spawnpoint"),
           (party_set_ai_object, ":bandit_party", ":spawnpoint"),
           (party_set_ai_patrol_radius, ":bandit_party", 45),
         (else_try),
           (lt, ":bandit_lair", "p_spawn_points_end"),
           (party_set_ai_behavior, ":bandit_party", ai_bhvr_patrol_party),
           (party_template_get_slot, ":spawnpoint", ":bandit_party_template", "slot_party_template_lair_spawnpoint"),
           (party_set_ai_object, ":bandit_party", ":spawnpoint"),
           (party_set_ai_patrol_radius, ":bandit_party", 45),
         (try_end),
       (try_end),
     (try_end),
     #Piggybacking on trigger:
     (try_begin),
       (troop_get_slot, ":betrothed", "trp_player", "slot_troop_betrothed"),
       (gt, ":betrothed", 0),
       (neg|check_quest_active, "qst_wed_betrothed"),
       (neg|check_quest_active, "qst_wed_betrothed_female"),
       (str_store_troop_name, s5, ":betrothed"),
       (display_message, "@Betrothal to {s5} expires"),
       (troop_set_slot, "trp_player", "slot_troop_betrothed", -1),
       (troop_set_slot, ":betrothed", "slot_troop_betrothed", -1),
     (try_end),
     ]),
		
  # Reduce renown slightly by 0.5% every week
  (7 * 24,
   [
       (troop_get_slot, ":player_renown", "trp_player", "slot_troop_renown"),
       (store_div, ":renown_decrease", ":player_renown", 200),
       (val_sub, ":player_renown", ":renown_decrease"),
       (troop_set_slot, "trp_player", "slot_troop_renown", ":player_renown"),
    ]),
# ["book_tactics","History of the Peloponnesian War (tactics)", [("book_a",0)], itp_type_book, 0, 4500,weight(2)|abundance(60),imodbits_none],
# ["book_persuasion","Rhetorica ad Herennium (persuasion)", [("book_b",0)], itp_type_book, 0, 4600,weight(2)|abundance(60),imodbits_none],
# ["book_leadership","The Life of Alexander the Great (leadership)", [("book_d",0)], itp_type_book, 0, 3780,weight(2)|abundance(60),imodbits_none], #cambiar chief
# ["book_intelligence","Paedeia (intelligence)", [("book_e",0)], itp_type_book, 0, 4500,weight(2)|abundance(60),imodbits_none],
# ["book_pathfinding","Guiding Pilgrim Travellers (pathfinding)", [("book_f",0)], itp_type_book, 0, 3600,weight(2)|abundance(60),imodbits_none],
# ["book_weapon_mastery", "Polity of the Lacedaemonians, of Xenofonte (weaponsmaster)", [("book_d",0)], itp_type_book, 0, 4500,weight(2)|abundance(60),imodbits_none],
# ["book_engineering","De architectura, of Vitrivius (engineering)", [("book_open",0)], itp_type_book, 0, 4500,weight(2)|abundance(60),imodbits_none],
# ["book_charisma","Motivational Daily Readings (charimsa)", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(60),imodbits_none],
# ["book_surgery","Synopsis of Aelius Galenus (surgery)", [("book_c",0)], itp_type_book, 0, 3600,weight(2)|abundance(60),imodbits_none],
# ["book_training","Epitoma Rei Militaris (training)", [("book_open",0)], itp_type_book, 0, 3600,weight(2)|abundance(60),imodbits_none],
# #Reference books
# #This book must be at the beginning of reference books
# ["book_wound_treatment_reference","De Materia Medica, of Dioscorides", [("book_c",0)], itp_type_book, 0, 3600,weight(2)|abundance(60),imodbits_none],
# ["book_looting_reference","Swords of King Arthur's Court", [("book_c",0)], itp_type_book, 0, 3600,weight(2)|abundance(60),imodbits_none],
# ["book_firstaid_reference","Convalescence shortened", [("book_c",0)], itp_type_book, 0, 3600,weight(2)|abundance(60),imodbits_none],
# ["book_trade_reference","Merchant's Ledger", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(60),imodbits_none],
  # Read books if player is resting.
  (1, [(neg|map_free),
       (gt, "$g_player_reading_book", 0),
       (player_has_item, "$g_player_reading_book"),
       (store_attribute_level, ":int", "trp_player", ca_intelligence),
       (item_get_slot, ":int_req", "$g_player_reading_book", "slot_item_intelligence_requirement"),
       (le, ":int_req", ":int"),
       (item_get_slot, ":book_reading_progress", "$g_player_reading_book", "slot_item_book_reading_progress"),
       (item_get_slot, ":book_read", "$g_player_reading_book", "slot_item_book_read"),
       (eq, ":book_read", 0),
       (val_add, ":book_reading_progress", 5),#gdw7
       (item_set_slot, "$g_player_reading_book", "slot_item_book_reading_progress", ":book_reading_progress"),
       (ge, ":book_reading_progress", 1000),
       (item_set_slot, "$g_player_reading_book", "slot_item_book_read", 1),
       (str_store_item_name, s1, "$g_player_reading_book"),
       (str_clear, s2),
       (try_begin),
         (eq, "$g_player_reading_book", "itm_book_tactics"),
         (troop_raise_skill, "trp_player", "skl_tactics", 2),#gdw1
         (str_store_string, s2, "@ Your tactics skill has increased by 2."),#gdw1
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_persuasion"),
         (troop_raise_skill, "trp_player", "skl_persuasion", 2),#gdw1
         (str_store_string, s2, "@ Your persuasion skill has increased by 2."),#gdw1
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_leadership"),
         (troop_raise_skill, "trp_player", "skl_leadership", 2),#gdw1
         (str_store_string, s2, "@ Your leadership skill has increased by 2."),#gdw1
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_intelligence"),
         (troop_raise_attribute, "trp_player", ca_intelligence, 2),#gdw1
         (str_store_string, s2, "@ Your intelligence has increased by 2."),#gdw1
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_charisma"),
         (troop_raise_attribute, "trp_player", ca_charisma, 2),#gdw1
         (str_store_string, s2, "@ Your intelligence has increased by 2."),#gdw1
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_pathfinding"),
         (troop_raise_skill, "trp_player", "skl_trade", 2),#gdw1
         (str_store_string, s2, "@ Your trade skill has increased by 2."),#gdw1
         (else_try),
       (eq, "$g_player_reading_book", "itm_book_surgery"),
         (troop_raise_skill, "trp_player", "skl_trade", 2),#gdw1
         (str_store_string, s2, "@ Your trade skill has increased by 2."),#gdw1
         (else_try),
         (eq, "$g_player_reading_book", "itm_book_training"),
         (troop_raise_skill, "trp_player", "skl_trade", 2),#gdw1
         (str_store_string, s2, "@ Your trade skill has increased by 2."),#gdw1
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_weapon_mastery"),
         (troop_raise_skill, "trp_player", "skl_weapon_master", 2),#gdw1
         (str_store_string, s2, "@ Your weapon master skill has increased by 2."),#g
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_engineering"),
         (troop_raise_skill, "trp_player", "skl_engineer", 2),#gdw1
         (str_store_string, s2, "@ Your engineer skill has increased by 2."),#gdw1
       (try_end),
       (unlock_achievement, ACHIEVEMENT_BOOK_WORM),

       (try_begin),
         (eq, "$g_infinite_camping", 0),
         (dialog_box, "@You have finished reading {s1}.{s2}", "@Book Read"),
       (try_end),  
              
       (assign, "$g_player_reading_book", 0),	   	   
       ]),

# Removing cattle herds if they are way out of range
  (24, [(try_for_parties, ":cur_party"), ##gdw12
          (party_slot_eq, ":cur_party", "slot_party_type", spt_cattle_herd1),
          (store_distance_to_party_from_party, ":dist",":cur_party", "p_main_party"),
          (try_begin),
            (gt, ":dist", 30),
            (remove_party, ":cur_party"),
            (try_begin),
              #Fail quest if the party is the quest party
              (check_quest_active, "qst_move_cattle_herd1"),
              (neg|check_quest_concluded, "qst_move_cattle_herd1"),
              (quest_slot_eq, "qst_move_cattle_herd1", "slot_quest_target_party", ":cur_party"),
              (call_script, "script_fail_quest", "qst_move_cattle_herd1"),
            (end_try),
          (else_try),
            (gt, ":dist", 10),
            (party_set_slot, ":cur_party", "slot_cattle_driven_by_player", 0),
            (party_set_ai_behavior, ":cur_party", ai_bhvr_hold),
          (try_end),
        (try_end),
    ]),

  
#####!!!!!

# Village upgrade triggers

# School chief cambia a 7x24
  (7 * 24,
   [(try_for_range, ":cur_village", villages_begin, villages_end),
      (party_slot_eq, ":cur_village", "slot_town_lord", "trp_player"),
      (party_slot_eq, ":cur_village", "slot_center_has_school", 1),
      (party_get_slot, ":cur_relation", ":cur_village", "slot_center_player_relation"),
      (val_add, ":cur_relation", 1),
      (val_min, ":cur_relation", 100),
      (party_set_slot, ":cur_village", "slot_center_player_relation", ":cur_relation"),
    (try_end),
    ]),

# Quest triggers:

# Remaining days text update
  (24, [(try_for_range, ":cur_quest", all_quests_begin, all_quests_end),
          (try_begin),
            (check_quest_active, ":cur_quest"),
            (try_begin),
              (neg|check_quest_concluded, ":cur_quest"),
              (quest_slot_ge, ":cur_quest", "slot_quest_expiration_days", 1),
              (quest_get_slot, ":exp_days", ":cur_quest", "slot_quest_expiration_days"),
              (val_sub, ":exp_days", 1),
              (try_begin),
                (eq, ":exp_days", 0),
                (call_script, "script_abort_quest", ":cur_quest", 1),
              (else_try),
                (quest_set_slot, ":cur_quest", "slot_quest_expiration_days", ":exp_days"),
                (assign, reg0, ":exp_days"),
                (add_quest_note_from_sreg, ":cur_quest", 7, "@You have {reg0} days to finish this quest.", 0),
              (try_end),
            (try_end),
          (else_try),
            (quest_slot_ge, ":cur_quest", "slot_quest_dont_give_again_remaining_days", 1),
            (quest_get_slot, ":value", ":cur_quest", "slot_quest_dont_give_again_remaining_days"),
            (val_sub, ":value", 1),
            (quest_set_slot, ":cur_quest", "slot_quest_dont_give_again_remaining_days", ":value"),
          (try_end),
        (try_end),
    ]),

# Report to army quest ##gdw this was at 2
  (3,   
   [
     (eq, "$g_infinite_camping", 0),
     (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
     (eq, "$g_player_is_captive", 0),
     	 
	 (try_begin),
		(check_quest_active, "qst_report_to_army"),
		(faction_slot_eq, "$players_kingdom", "slot_faction_marshall", -1),
		(call_script, "script_abort_quest", "qst_report_to_army", 0),
	 (try_end),
	 
	 (faction_get_slot, ":faction_object", "$players_kingdom", "slot_faction_ai_object"),
	 
     (neg|faction_slot_eq, "$players_kingdom", "slot_faction_ai_state", sfai_default),
     (neg|faction_slot_eq, "$players_kingdom", "slot_faction_ai_state", sfai_feast),
          
     (assign, ":continue", 1),
     (try_begin),     
       (this_or_next|faction_slot_eq, "$players_kingdom", "slot_faction_ai_state", sfai_attacking_enemies_around_center),
       (this_or_next|faction_slot_eq, "$players_kingdom", "slot_faction_ai_state", sfai_attacking_center),
       (faction_slot_eq, "$players_kingdom", "slot_faction_ai_state", sfai_raiding_village),
       (neg|is_between, ":faction_object", walled_centers_begin, walled_centers_end),
       (assign, ":continue", 0),
     (try_end),       
     (eq, ":continue", 1),
                            	 
	 (assign, ":kingdom_is_at_war", 0),
	 (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
		(neq, ":faction", "$players_kingdom"),
		(store_relation, ":relation", ":faction", "$players_kingdom"),
		(lt, ":relation", 0),
		(assign, ":kingdom_is_at_war", 1),
	 (try_end),
	 (eq, ":kingdom_is_at_war", 1),
	 	 
     (neg|check_quest_active, "qst_report_to_army"),
     (neg|check_quest_active, "qst_follow_army"),
     
     (neg|quest_slot_ge, "qst_report_to_army", "slot_quest_dont_give_again_remaining_days", 1),
     (faction_get_slot, ":faction_marshall", "$players_kingdom", "slot_faction_marshall"),
     (gt, ":faction_marshall", 0),
     (troop_get_slot, ":faction_marshall_party", ":faction_marshall", "slot_troop_leaded_party"),
     (gt, ":faction_marshall_party", 0),
     (party_is_active, ":faction_marshall_party"),
     
     (store_distance_to_party_from_party, ":distance_to_marshal", ":faction_marshall_party", "p_main_party"),
     (le, ":distance_to_marshal", 96),
     
     (assign, ":has_no_quests", 1),     
     (try_for_range, ":cur_quest", lord_quests_begin, lord_quests_end),
       (check_quest_active, ":cur_quest"),
       (quest_slot_eq, ":cur_quest", "slot_quest_giver_troop", ":faction_marshall"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),
     
     (try_for_range, ":cur_quest", lord_quests_begin_2, lord_quests_end_2),
       (check_quest_active, ":cur_quest"),
       (quest_slot_eq, ":cur_quest", "slot_quest_giver_troop", ":faction_marshall"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),
     
     (try_for_range, ":cur_quest", army_quests_begin, army_quests_end),
       (check_quest_active, ":cur_quest"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),
     
     (store_character_level, ":level", "trp_player"),
     (ge, ":level", 8),
     (assign, ":cur_target_amount", 2),
     (try_for_range, ":cur_center", centers_begin, centers_end),
       (party_slot_eq, ":cur_center", "slot_town_lord", "trp_player"),
       (try_begin),
         (party_slot_eq, ":cur_center", "slot_party_type", spt_town),
         (val_add, ":cur_target_amount", 3),
       (else_try),
         (party_slot_eq, ":cur_center", "slot_party_type", spt_castle),
         (val_add, ":cur_target_amount", 1),
       (else_try),
         (val_add, ":cur_target_amount", 1),
       (try_end),
     (try_end),
     
     (val_mul, ":cur_target_amount", 4),
     (val_min, ":cur_target_amount", 60),
     (quest_set_slot, "qst_report_to_army", "slot_quest_giver_troop", ":faction_marshall"),
     (quest_set_slot, "qst_report_to_army", "slot_quest_target_troop", ":faction_marshall"),
     (quest_set_slot, "qst_report_to_army", "slot_quest_target_amount", ":cur_target_amount"),
     (quest_set_slot, "qst_report_to_army", "slot_quest_expiration_days", 4),
     (quest_set_slot, "qst_report_to_army", "slot_quest_dont_give_again_period", 22),
     (jump_to_menu, "mnu_kingdom_army_quest_report_to_army"),
   ]),

# Army quest initializer
  (3,
   [
     (assign, "$g_random_army_quest", -1),
     (check_quest_active, "qst_follow_army", 1),
     (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
#Rebellion changes begin
#     (neg|is_between, "$players_kingdom", rebel_factions_begin, rebel_factions_end),
#Rebellion changes end
     (neg|faction_slot_eq, "$players_kingdom", "slot_faction_ai_state", sfai_default),
     (faction_get_slot, ":faction_marshall", "$players_kingdom", "slot_faction_marshall"),
     (neq, ":faction_marshall", "trp_player"),
     (gt, ":faction_marshall", 0),
     (troop_get_slot, ":faction_marshall_party", ":faction_marshall", "slot_troop_leaded_party"),
     (gt, ":faction_marshall_party", 0),
     (party_is_active, ":faction_marshall_party"),
     (store_distance_to_party_from_party, ":dist", ":faction_marshall_party", "p_main_party"),
     (try_begin),
       (lt, ":dist", 15),
       (assign, "$g_player_follow_army_warnings", 0),
       (store_current_hours, ":cur_hours"),
       (faction_get_slot, ":last_offensive_time", "$players_kingdom", "slot_faction_last_offensive_concluded"),
       (store_sub, ":passed_time", ":cur_hours", ":last_offensive_time"),

       (assign, ":result", -1),
       (try_begin),
         (store_random_in_range, ":random_no", 0, 100),
         (lt, ":random_no", 30),
         (troop_slot_eq, ":faction_marshall", "slot_troop_does_not_give_quest", 0),
         (try_for_range, ":unused", 0, 20), #Repeat trial twenty times
           (eq, ":result", -1),
           (store_random_in_range, ":quest_no", army_quests_begin, army_quests_end),
           (neg|quest_slot_ge, ":quest_no", "slot_quest_dont_give_again_remaining_days", 1),
           (try_begin),
             (eq, ":quest_no", "qst_deliver_cattle_to_army"),
			# (eq, 1, 0), #disables temporarily			 
             (try_begin),
               (faction_slot_eq, "$players_kingdom", "slot_faction_ai_state", sfai_attacking_center),
               (gt, ":passed_time", 120),#5 days
               (store_random_in_range, ":quest_target_amount", 5, 10),
               (assign, ":result","qst_deliver_cattle_to_army"),
               (quest_set_slot, ":result", "slot_quest_target_amount", ":quest_target_amount"),
               (quest_set_slot, ":result", "slot_quest_expiration_days", 10),
               (quest_set_slot, ":result", "slot_quest_dont_give_again_period", 30),
             (try_end),
           (else_try),
             (eq, ":quest_no", "qst_join_siege_with_army"),
			 (eq, 1, 0),
             (try_begin),
               (faction_slot_eq, "$players_kingdom", "slot_faction_ai_state", sfai_attacking_center),
               (faction_get_slot, ":ai_object", "$players_kingdom", "slot_faction_ai_object"),
               (is_between, ":ai_object", walled_centers_begin, walled_centers_end),
               (party_get_battle_opponent, ":besieged_center", ":faction_marshall_party"),
               (eq, ":besieged_center", ":ai_object"),
               #army is assaulting the center
               (assign, ":result", ":quest_no"),
               (quest_set_slot, ":result", "slot_quest_target_center", ":ai_object"),
               (quest_set_slot, ":result", "slot_quest_expiration_days", 2),
               (quest_set_slot, ":result", "slot_quest_dont_give_again_period", 15),
             (try_end),
           (else_try),
             (eq, ":quest_no", "qst_scout_waypoints"),
             (try_begin),
               (assign, ":end_cond", 100),
               (assign, "$qst_scout_waypoints_wp_1", -1),
               (assign, "$qst_scout_waypoints_wp_2", -1),
               (assign, "$qst_scout_waypoints_wp_3", -1),
               (assign, ":continue", 0),
               (try_for_range, ":unused", 0, ":end_cond"),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_1", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (assign, "$qst_scout_waypoints_wp_1", reg0),
                 (try_end),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_2", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (neq, "$qst_scout_waypoints_wp_1", reg0),
                   (assign, "$qst_scout_waypoints_wp_2", reg0),
                 (try_end),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_3", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (neq, "$qst_scout_waypoints_wp_1", reg0),
                   (neq, "$qst_scout_waypoints_wp_2", reg0),
                   (assign, "$qst_scout_waypoints_wp_3", reg0),
                 (try_end),
                 (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                 (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                 (neq, "$qst_scout_waypoints_wp_2", "$qst_scout_waypoints_wp_3"),
                 (ge, "$qst_scout_waypoints_wp_1", 0),
                 (ge, "$qst_scout_waypoints_wp_2", 0),
                 (ge, "$qst_scout_waypoints_wp_3", 0),
                 (assign, ":end_cond", 0),
                 (assign, ":continue", 1),
               (try_end),
               (eq, ":continue", 1),
               (assign, "$qst_scout_waypoints_wp_1_visited", 0),
               (assign, "$qst_scout_waypoints_wp_2_visited", 0),
               (assign, "$qst_scout_waypoints_wp_3_visited", 0),
               (assign, ":result", "qst_scout_waypoints"),
               (quest_set_slot, ":result", "slot_quest_expiration_days", 7),
               (quest_set_slot, ":result", "slot_quest_dont_give_again_period", 25),
             (try_end),
           (try_end),
         (try_end),
		 
         (try_begin),
           (neq, ":result", -1),
           (quest_set_slot, ":result", "slot_quest_current_state", 0),
           (quest_set_slot, ":result", "slot_quest_giver_troop", ":faction_marshall"),
           (try_begin),
             (eq, ":result", "qst_join_siege_with_army"),
             (jump_to_menu, "mnu_kingdom_army_quest_join_siege_order"),
           (else_try),
             (assign, "$g_random_army_quest", ":result"),
             (quest_set_slot, "$g_random_army_quest", "slot_quest_giver_troop", ":faction_marshall"),
             (jump_to_menu, "mnu_kingdom_army_quest_messenger"),
           (try_end),
         (try_end),
       (try_end),
     (else_try),
       (val_add, "$g_player_follow_army_warnings", 1),
       (try_begin),
         (lt, "$g_player_follow_army_warnings", 15),
         (try_begin),
           (store_mod, ":follow_mod", "$g_player_follow_army_warnings", 3),
           (eq, ":follow_mod", 0),
           (str_store_troop_name_link, s1, ":faction_marshall"),
           (try_begin),
             (lt, "$g_player_follow_army_warnings", 8),
#             (display_message, "str_marshal_warning"),
           (else_try),
             (display_message, "str_marshal_warning"),
           (try_end),
         (try_end),
       (else_try),
         (jump_to_menu, "mnu_kingdom_army_follow_failed"),
       (try_end),
     (try_end),
    ]),

# Move cattle herd
  (0.5, [(check_quest_active,"qst_move_cattle_herd1"),
         (neg|check_quest_concluded,"qst_move_cattle_herd1"),
         (quest_get_slot, ":target_party", "qst_move_cattle_herd1", "slot_quest_target_party"),
         (quest_get_slot, ":target_center", "qst_move_cattle_herd1", "slot_quest_target_center"),
         (store_distance_to_party_from_party, ":dist",":target_party", ":target_center"),
         (lt, ":dist", 3),
         (remove_party, ":target_party"),
         (call_script, "script_succeed_quest", "qst_move_cattle_herd1"),
    ]),

  (2, [
       (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
		 (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
		 (troop_get_slot, ":party_no", ":troop_no", "slot_troop_leaded_party"),
         (ge, ":party_no", 1),
		 (party_is_active, ":party_no"),
         (party_slot_eq, ":party_no", "slot_party_following_player", 1),
         (store_current_hours, ":cur_time"),
         (neg|party_slot_ge, ":party_no", "slot_party_follow_player_until_time", ":cur_time"),
         (party_set_slot, ":party_no", "slot_party_commander_party", -1),
         (party_set_slot, ":party_no", "slot_party_following_player", 0),
         (assign,  ":dont_follow_period", 200),
         (store_add, ":dont_follow_time", ":cur_time", ":dont_follow_period"),
         (party_set_slot, ":party_no", "slot_party_dont_follow_player_until_time",  ":dont_follow_time"),
       (try_end),
    ]),

# Deliver cattle and deliver cattle to army
  (0.5,
   [
     (try_begin),
       (check_quest_active,"qst_deliver_cattle"),
       (neg|check_quest_succeeded, "qst_deliver_cattle"),
       (quest_get_slot, ":target_center", "qst_deliver_cattle", "slot_quest_target_center"),
       (quest_get_slot, ":target_amount", "qst_deliver_cattle", "slot_quest_target_amount"),
       (quest_get_slot, ":cur_amount", "qst_deliver_cattle", "slot_quest_current_state"),
       (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
       (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_center", ":left_amount"),
       (val_add, ":cur_amount", reg0),
       (quest_set_slot, "qst_deliver_cattle", "slot_quest_current_state", ":cur_amount"),
       (le, ":target_amount", ":cur_amount"),
       (call_script, "script_succeed_quest", "qst_deliver_cattle"),
     (try_end),
     (try_begin),
       (check_quest_active, "qst_deliver_cattle_to_army"),
       (neg|check_quest_succeeded, "qst_deliver_cattle_to_army"),
       (quest_get_slot, ":giver_troop", "qst_deliver_cattle_to_army", "slot_quest_giver_troop"),
       (troop_get_slot, ":target_party", ":giver_troop", "slot_troop_leaded_party"),
       (try_begin),
         (gt, ":target_party", 0),
         (quest_get_slot, ":target_amount", "qst_deliver_cattle_to_army", "slot_quest_target_amount"),
         (quest_get_slot, ":cur_amount", "qst_deliver_cattle_to_army", "slot_quest_current_state"),
         (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
         (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_party", ":left_amount"),
         (val_add, ":cur_amount", reg0),
         (quest_set_slot, "qst_deliver_cattle_to_army", "slot_quest_current_state", ":cur_amount"),
         (try_begin),
           (le, ":target_amount", ":cur_amount"),
           (call_script, "script_succeed_quest", "qst_deliver_cattle_to_army"),
         (try_end),
       (else_try),
         (call_script, "script_abort_quest", "qst_deliver_cattle_to_army", 0),
       (try_end),
     (try_end),
     ]),

# Train peasants against bandits
  (1,
   [
     (neg|map_free),
     (check_quest_active, "qst_train_peasants_against_bandits"),
     (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
     (eq, "$qst_train_peasants_against_bandits_currently_training", 1),
     (val_add, "$qst_train_peasants_against_bandits_num_hours_trained", 1),
     (call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
     (assign, ":trainer_skill", reg0),
     (store_sub, ":needed_hours", 16, ":trainer_skill"),#gdw20
     (val_mul, ":needed_hours", 3),#tml
     (val_div, ":needed_hours", 5),
     (ge, "$qst_train_peasants_against_bandits_num_hours_trained", ":needed_hours"),
     (assign, "$qst_train_peasants_against_bandits_num_hours_trained", 0),
     (rest_for_hours, 0, 0, 0), #stop resting
     (jump_to_menu, "mnu_train_peasants_against_bandits_ready"),
     ]),

# Scout waypoints
  (1,
   [
     (check_quest_active,"qst_scout_waypoints"),
     (neg|check_quest_succeeded, "qst_scout_waypoints"),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_1_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_1", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_1_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_1"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_2_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_2", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_2_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_2"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_3_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_3", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_3_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_3"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (eq, "$qst_scout_waypoints_wp_1_visited", 1),
     (eq, "$qst_scout_waypoints_wp_2_visited", 1),
     (eq, "$qst_scout_waypoints_wp_3_visited", 1),
     (call_script, "script_succeed_quest", "qst_scout_waypoints"),
     ]),
  
# Kill local merchant
  
  (3, [(neg|map_free),
       (check_quest_active, "qst_kill_local_merchant"),
       (quest_slot_eq, "qst_kill_local_merchant", "slot_quest_current_state", 0),
       (quest_set_slot, "qst_kill_local_merchant", "slot_quest_current_state", 1),
       (rest_for_hours, 0, 0, 0), #stop resting
       (assign, "$auto_enter_town", "$qst_kill_local_merchant_center"),
       (assign, "$quest_auto_menu", "mnu_kill_local_merchant_begin"),
       ]),

# Collect taxes
  (1, [(neg|map_free),
       (check_quest_active, "qst_collect_taxes"),
       (eq, "$g_player_is_captive", 0),
       (eq, "$qst_collect_taxes_currently_collecting", 1),
       (quest_get_slot, ":quest_current_state", "qst_collect_taxes", "slot_quest_current_state"),
       (this_or_next|eq, ":quest_current_state", 1),
       (this_or_next|eq, ":quest_current_state", 2),
       (eq, ":quest_current_state", 3),
       (quest_get_slot, ":left_hours", "qst_collect_taxes", "slot_quest_target_amount"),
       (val_sub, ":left_hours", 1),
       (quest_set_slot, "qst_collect_taxes", "slot_quest_target_amount", ":left_hours"),
       (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
       
       (try_begin),
         (lt, ":left_hours", 0),
         (assign, ":quest_current_state", 4),
         (quest_set_slot, "qst_collect_taxes", "slot_quest_current_state", 4),
         (rest_for_hours, 0, 0, 0), #stop resting
         (jump_to_menu, "mnu_collect_taxes_complete"),
       (else_try),
         #Continue collecting taxes
         (assign, ":max_collected_tax", "$qst_collect_taxes_hourly_income"),
         (party_get_slot, ":prosperity", "$g_encountered_party", "slot_town_prosperity"),
         (store_add, ":multiplier", 30, ":prosperity"),
         (val_mul, ":max_collected_tax", ":multiplier"),
         (val_div, ":max_collected_tax", 80),#Prosperity of 50 gives the default values
       
         (try_begin),
           (eq, "$qst_collect_taxes_halve_taxes", 1),
           (val_div, ":max_collected_tax", 2),
         (try_end),
         (val_max, ":max_collected_tax", 2),
         (store_random_in_range, ":collected_tax", 1, ":max_collected_tax"),
         (quest_get_slot, ":cur_collected", "qst_collect_taxes", "slot_quest_gold_reward"),
         (val_add, ":cur_collected", ":collected_tax"),
         (quest_set_slot, "qst_collect_taxes", "slot_quest_gold_reward", ":cur_collected"),
         (call_script, "script_troop_add_gold", "trp_player", ":collected_tax"),
       (try_end),
       (try_begin),
         (eq, ":quest_current_state", 1),
         (val_sub, "$qst_collect_taxes_menu_counter", 1),
         (le, "$qst_collect_taxes_menu_counter", 0),
         (quest_set_slot, "qst_collect_taxes", "slot_quest_current_state", 2),
         (jump_to_menu, "mnu_collect_taxes_revolt_warning"),
       (else_try), #Chance of revolt against player
         (eq, ":quest_current_state", 2),
         (val_sub, "$qst_collect_taxes_unrest_counter", 1),
         (le, "$qst_collect_taxes_unrest_counter", 0),
         (eq, "$qst_collect_taxes_halve_taxes", 0),
         (quest_set_slot, "qst_collect_taxes", "slot_quest_current_state", 3),

         (store_div, ":unrest_chance", 10000, "$qst_collect_taxes_total_hours"),
         (val_add, ":unrest_chance",30),
       
         (store_random_in_range, ":unrest_roll", 0, 1000),
         (try_begin),
           (lt, ":unrest_roll", ":unrest_chance"),
           (jump_to_menu, "mnu_collect_taxes_revolt"),
         (try_end),
       (try_end),
       ]),

#persuade_lords_to_make_peace begin
  (72, [(gt, "$g_force_peace_faction_1", 0),
        (gt, "$g_force_peace_faction_2", 0),
        (try_begin),
          (store_relation, ":relation", "$g_force_peace_faction_1", "$g_force_peace_faction_2"),
          (lt, ":relation", 0),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_force_peace_faction_1", "$g_force_peace_faction_2", 1),
        (try_end),
        (assign, "$g_force_peace_faction_1", 0),
        (assign, "$g_force_peace_faction_2", 0),
       ]),  

#NPC changes begin
#Resolve one issue each hour
(1, 
   [
		#add pretender to party if not active		
		(try_begin),
			(check_quest_active, "qst_rebel_against_kingdom"),
			(is_between, "$supported_pretender", pretenders_begin, pretenders_end),
			(neg|main_party_has_troop, "$supported_pretender"),
			(neg|troop_slot_eq, "$supported_pretender", "slot_troop_occupation", slto_kingdom_hero),
			(party_add_members, "p_main_party", "$supported_pretender", 1),
		(try_end),
		#make player marshal of rebel faction
		(try_begin),
			(check_quest_active, "qst_rebel_against_kingdom"),
			(is_between, "$supported_pretender", pretenders_begin, pretenders_end),
			(main_party_has_troop, "$supported_pretender"),
			(neg|faction_slot_eq, "fac_player_supporters_faction", "slot_faction_marshall", "trp_player"),
			(call_script, "script_appoint_faction_marshall", "fac_player_supporters_faction", "trp_player"),
		(try_end),

]),
#NPC changes end
#chief cambia a cada 180 dias horas el tiempo en deserciones de senores lores
#(998, 
(24*180, 
   [(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
      (troop_slot_ge, ":troop_no", "slot_troop_change_to_faction", 1),
      (store_troop_faction, ":faction_no", ":troop_no"),
      (troop_get_slot, ":new_faction_no", ":troop_no", "slot_troop_change_to_faction"),
      (troop_get_slot, ":party_no", ":troop_no", "slot_troop_leaded_party"),
      (assign, ":continue", 0),
      (try_begin),
        (le, ":party_no", 0),
        #(troop_slot_eq, ":troop_no", "slot_troop_is_prisoner", 0),
        (neg|troop_slot_ge, ":troop_no", "slot_troop_prisoner_of_party", 0),
        (assign, ":continue", 1),
      (else_try),
        (gt, ":party_no", 0),

        #checking if the party is outside the centers
        (party_get_attached_to, ":cur_center_no", ":party_no"),
        (try_begin),
          (lt, ":cur_center_no", 0),
          (party_get_cur_town, ":cur_center_no", ":party_no"),
        (try_end),
        (this_or_next|neg|is_between, ":cur_center_no", centers_begin, centers_end),
        (party_slot_eq, ":cur_center_no", "slot_town_lord", ":troop_no"),
    
        #checking if the party is away from his original faction parties
        (assign, ":end_cond", active_npcs_end),
        (try_for_range, ":enemy_troop_no", active_npcs_begin, ":end_cond"),
    (troop_slot_eq, ":enemy_troop_no", "slot_troop_occupation", slto_kingdom_hero),
        ## bugfix - must not include himself chief
          (neq, ":enemy_troop_no", ":troop_no"),
          ## bugfix
          (troop_get_slot, ":enemy_party_no", ":enemy_troop_no", "slot_troop_leaded_party"),
          (party_is_active, ":enemy_party_no"),
          (store_faction_of_party, ":enemy_faction_no", ":enemy_party_no"),
          (eq, ":enemy_faction_no", ":faction_no"),
          (store_distance_to_party_from_party, ":dist", ":party_no", ":enemy_party_no"),
          (lt, ":dist", 4),
          (assign, ":end_cond", 0),
        (try_end),
        (neq, ":end_cond", 0),
        (assign, ":continue", 1),
      (try_end),
      (eq, ":continue", 1),
	  
		(try_begin),
			(ge, "$cheat_mode", 1),
			(str_store_troop_name, s4, ":troop_no"),
			(display_message, "@{!}DEBUG - {s4} faction changed simple trigger ln5721 from 'slot_troop_change_to_faction'"),
		(try_end),	  
		
      (call_script, "script_change_troop_faction", ":troop_no", ":new_faction_no"),
      (troop_set_slot, ":troop_no", "slot_troop_change_to_faction", 0),
      (try_begin),
        (is_between, ":new_faction_no", kingdoms_begin, kingdoms_end),
        (str_store_troop_name_link, s1, ":troop_no"),
        (str_store_faction_name_link, s2, ":faction_no"),
        (str_store_faction_name_link, s3, ":new_faction_no"),
        (display_message, "@{s1} has switched from {s2} to {s3}."),
        (try_begin),
          (eq, ":faction_no", "$players_kingdom"),
          (call_script, "script_add_notification_menu", "mnu_notification_troop_left_players_faction", ":troop_no", ":new_faction_no"),
        (else_try),
          (eq, ":new_faction_no", "$players_kingdom"),
          (call_script, "script_add_notification_menu", "mnu_notification_troop_joined_players_faction", ":troop_no", ":faction_no"),
        (try_end),
      (try_end),
    (try_end),
    ]),


(2,#gdw1
   [
     (eq, "$cheat_mode", 1),
     (try_for_range, ":center_no", centers_begin, centers_end),
       (party_get_battle_opponent, ":besieger_party", ":center_no"),
       (try_begin),
         (gt, ":besieger_party", 0),
         (str_store_party_name, s2, ":center_no"),
         (str_store_party_name, s3, ":besieger_party"),
         (display_message, "@{!}DEBUG : {s2} is besieging by {s3}"),
       (try_end),
     (try_end),    
     ]),

(2, #gdw1
   [
     (store_current_day, ":cur_day"),
     (gt, ":cur_day", "$g_last_report_control_day"),
     (store_time_of_day, ":cur_hour"),
     (ge, ":cur_hour", 18),

     (store_random_in_range, ":rand_no", 0, 4),
     (this_or_next|ge, ":cur_hour", 22),
     (eq, ":rand_no", 0),
     
     (assign, "$g_last_report_control_day", ":cur_day"),
     
     (store_troop_gold, ":gold", "trp_player"),
     
     (try_begin),
       (lt, ":gold", 0),
       (store_sub, ":gold_difference", 0, ":gold"),
       (troop_add_gold, "trp_player", ":gold_difference"),
     (try_end),

     (party_get_morale, ":main_party_morale", "p_main_party"),     
     
     #(assign, ":swadian_soldiers_are_upset_message_showed", 0),
     #(assign, ":vaegir_soldiers_are_upset_message_showed", 0),
     #(assign, ":khergit_soldiers_are_upset_message_showed", 0),
     #(assign, ":nord_soldiers_are_upset_message_showed", 0),
     #(assign, ":rhodok_soldiers_are_upset_message_showed", 0),
    
     (try_begin),
       (str_store_string, s1, "str_party_morale_is_low"),            
       (str_clear, s2),

       (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
       (assign, ":num_deserters_total", 0),
       (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
         (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
         (neg|troop_is_hero, ":stack_troop"),
         (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
         
         (store_troop_faction, ":faction_no", ":stack_troop"),
      
         (assign, ":troop_morale", ":main_party_morale"),         
         (try_begin),
           (ge, ":faction_no", npc_kingdoms_begin),
           (lt, ":faction_no", npc_kingdoms_end),
        
           (faction_get_slot, ":troop_morale_addition", ":faction_no",  "slot_faction_morale_of_player_troops"),
           (val_div, ":troop_morale_addition", 100),
           (val_add, ":troop_morale", ":troop_morale_addition"),
         (try_end),

         (lt, ":troop_morale", 32),
         (store_sub, ":desert_prob", 36, ":troop_morale"),
         (val_div, ":desert_prob", 4),

         (assign, ":num_deserters_from_that_troop", 0),
         (try_for_range, ":unused", 0, ":stack_size"),
           (store_random_in_range, ":rand_no", 0, 100),
           (lt, ":rand_no", ":desert_prob"),
           (val_add, ":num_deserters_from_that_troop", 1),
           #p.remove_members_from_stack(i_stack,cur_deserters, &main_party_instances);
           (remove_member_from_party, ":stack_troop", "p_main_party"),
         (try_end),
         (try_begin),
           (ge, ":num_deserters_from_that_troop", 1),           
           (str_store_troop_name, s2, ":stack_troop"),
           (assign, reg0, ":num_deserters_from_that_troop"),
           
#           (try_begin),           
#             (lt, ":troop_morale_addition", -2),
#             (ge, ":main_party_morale", 28),
#             (try_begin),
#               (eq, ":faction_no", "fac_kingdom_1"),  
#               (eq, ":swadian_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_swadian_soldiers_are_upset"),
#               (assign, ":swadian_soldiers_are_upset_message_showed", 1),
#             (else_try),
#               (eq, ":faction_no", "fac_kingdom_2"),  
#               (eq, ":vaegir_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_vaegir_soldiers_are_upset"),
#               (assign, ":vaegir_soldiers_are_upset_message_showed", 1),
#             (else_try),
#               (eq, ":faction_no", "fac_kingdom_3"),  
#               (eq, ":khergit_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_khergit_soldiers_are_upset"),
#               (assign, ":khergit_soldiers_are_upset_message_showed", 1),
#             (else_try),
#               (eq, ":faction_no", "fac_kingdom_4"),  
#               (eq, ":nord_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_nord_soldiers_are_upset"),
#               (assign, ":nord_soldiers_are_upset_message_showed", 1),
#             (else_try),
#               (eq, ":faction_no", "fac_kingdom_5"),  
#               (eq, ":rhodok_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_rhodok_soldiers_are_upset"),
#               (assign, ":rhodok_soldiers_are_upset_message_showed", 1),
#             (try_end),
#             (str_store_string, s1, "@{!}{s1} {s3}"),
#           (try_end),
           
           (try_begin),
             (ge, ":num_deserters_total", 1),
             (str_store_string, s1, "str_s1_reg0_s2"),
           (else_try),
             (str_store_string, s3, s1),
             (str_store_string, s1, "str_s3_reg0_s2"),
           (try_end),
           (val_add, ":num_deserters_total", ":num_deserters_from_that_troop"),
         (try_end),
       (try_end),

       (try_begin),
         (ge, ":num_deserters_total", 1),
  
         (try_begin),
           (ge, ":num_deserters_total", 2),
           (str_store_string, s2, "str_have_deserted_the_party"),
         (else_try),
           (str_store_string, s2, "str_has_deserted_the_party"),
         (try_end),          

         (str_store_string, s1, "str_s1_s2"),

         (eq, "$g_infinite_camping", 0),
         
         (tutorial_box, s1, "str_weekly_report"),
       (try_end), 
     (try_end),
 ]),
 # reserved for future use. For backward compatibility, we need to use these triggers instead of creating new ones.
  
  (4,
   [
     (call_script, "script_calculate_castle_prosperities_by_using_its_villages"),

     (store_add, ":fac_kingdom_6_plus_one", "fac_kingdom_6", 1),

     (try_for_range, ":faction_1", "fac_kingdom_1", ":fac_kingdom_6_plus_one"),
       (try_for_range, ":faction_2", "fac_kingdom_1", ":fac_kingdom_6_plus_one"),
         (store_relation, ":faction_relation", ":faction_1", ":faction_2"),
         (str_store_faction_name, s7, ":faction_1"),
         (str_store_faction_name, s8, ":faction_2"),
         (neq, ":faction_1", ":faction_2"),
         (assign, reg1, ":faction_relation"),
         #(display_message, "@{s7}-{s8}, relation is {reg1}"),
       (try_end),
     (try_end),          
   ]),
   
  (1,
   [   
     (try_begin),
       (eq, "$g_player_is_captive", 1),
       (neg|party_is_active, "$capturer_party"),
       (rest_for_hours, 0, 0, 0),
     (try_end),            
     
    ##diplomacy chief begin
      #seems to be a native bug
     (is_between, "$next_center_will_be_fired", villages_begin, villages_end),
     ##diplomacy end
     (assign, ":village_no", "$next_center_will_be_fired"),
     (party_get_slot, ":is_there_already_fire", ":village_no", "slot_village_smoke_added"),
     (eq, ":is_there_already_fire", 0),
	 
	 
     (try_begin),
       (party_get_slot, ":bound_center", ":village_no", "slot_village_bound_center"),  
       (party_get_slot, ":last_nearby_fire_time", ":bound_center", "slot_town_last_nearby_fire_time"),
       (store_current_hours, ":cur_hours"),
	   
	   (try_begin),
		(eq, "$cheat_mode", 1),
		(is_between, ":village_no", centers_begin, centers_end),
		(is_between, ":bound_center", centers_begin, centers_end),
		(str_store_party_name, s4, ":village_no"),
		(str_store_party_name, s5, ":bound_center"),
		(store_current_hours, reg3),
        (party_get_slot, reg4, ":bound_center", "slot_town_last_nearby_fire_time"),
		(display_message, "@{!}DEBUG - Checking fire at {s4} for {s5} - current time {reg3}, last nearby fire {reg4}"),
	   (try_end),
	   
	   
       (eq, ":cur_hours", ":last_nearby_fire_time"),
       (party_add_particle_system, ":village_no", "psys_map_village_fire"),
       (party_add_particle_system, ":village_no", "psys_map_village_fire_smoke"),       
     (else_try),  
       (store_add, ":last_nearby_fire_finish_time", ":last_nearby_fire_time", fire_duration),
       (eq, ":last_nearby_fire_finish_time", ":cur_hours"),
       (party_clear_particle_systems, ":village_no"),
     (try_end),  
     

   ]),
#chief quita viejo   
  (24,
   [
   (val_sub, "$g_dont_give_fief_to_player_days", 1),
   (val_max, "$g_dont_give_fief_to_player_days", -1),
   (val_sub, "$g_dont_give_marshalship_to_player_days", 1),
   (val_max, "$g_dont_give_marshalship_to_player_days", -1),

##   #this to correct string errors in games started in 1.104 or before
##   (party_set_name, "p_steppe_bandit_spawn_point", "str_the_steppes"),
##   (party_set_name, "p_taiga_bandit_spawn_point", "str_the_tundra"),
##   (party_set_name, "p_forest_bandit_spawn_point", "str_the_forests"),
##   (party_set_name, "p_mountain_bandit_spawn_point", "str_the_highlands"),
##   (party_set_name, "p_sea_raider_spawn_point_1", "str_the_coast"),
##   (party_set_name, "p_sea_raider_spawn_point_2", "str_the_coast"),
##   (party_set_name, "p_desert_bandit_spawn_point", "str_the_deserts"),

   
   #This to correct inappropriate home strings - Katrin to Uxkhal, Matheld to Fearichen
##   (troop_set_slot, "trp_npclady2", "slot_troop_home", "p_town_7"),
##   (troop_set_slot, "trp_npc8", "slot_troop_home", "p_village_35"),
##   
##   (troop_set_slot, "trp_npcengineer", "slot_troop_town_with_contacts", "p_town_20"), #durquba
   
   #this to correct linen production at villages of durquba 
   (party_set_slot, "p_village_93", "slot_center_linen_looms", 0), #mazigh
   (party_set_slot, "p_village_94", "slot_center_linen_looms", 0), #sekhtem
   (party_set_slot, "p_village_95", "slot_center_linen_looms", 0), #qalyut
   (party_set_slot, "p_village_96", "slot_center_linen_looms", 0), #tilimsal
   (party_set_slot, "p_village_97", "slot_center_linen_looms", 0), #shibal zumr
   (party_set_slot, "p_village_102", "slot_center_linen_looms", 0), #tamnuh
   (party_set_slot, "p_village_109", "slot_center_linen_looms", 0), #habba

   (party_set_slot, "p_village_67", "slot_center_fishing_fleet", 0), #Tebandra
   (party_set_slot, "p_village_5", "slot_center_fishing_fleet", 15), #Kulum
   
   
   #The following scripts are to end quests which should have cancelled, but did not because of a bug
   (try_begin),
	(check_quest_active, "qst_formal_marriage_proposal"),
	(check_quest_failed, "qst_formal_marriage_proposal"),
    (call_script, "script_end_quest", "qst_formal_marriage_proposal"),
   (try_end),
   
   (try_begin),
	(check_quest_active, "qst_lend_companion"),
	(quest_get_slot, ":giver_troop", "qst_lend_companion", "slot_quest_giver_troop"),
	(store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
    (store_relation, ":faction_relation", ":giver_troop_faction", "$players_kingdom"),
    (this_or_next|lt, ":faction_relation", 0),
	(neg|is_between, ":giver_troop_faction", kingdoms_begin, kingdoms_end),
    (call_script, "script_abort_quest", "qst_lend_companion", 0),
   (try_end),
   
   
   
   (try_begin),
	(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
	(neq, "$players_kingdom", "fac_player_supporters_faction"),
    (faction_slot_eq, "$players_kingdom", "slot_faction_marshall", "trp_player"),
    (val_add, "$g_player_days_as_marshal", 1),
   (else_try),
    (assign, "$g_player_days_as_marshal", 0),
   (try_end),
    ]),
###chief esposas de soldados en numero de 30 dan moral cada 48 horas
  (48,
   [
            (party_get_num_companion_stacks, ":num", "p_main_party"),
            (try_for_range, ":stack_no", 0, ":num"),
               (party_stack_get_troop_id, ":party_troop", "p_main_party", ":stack_no"),
               (eq, ":party_troop", "trp_fighter_woman"),
               (assign, ":num", 0), #loop breaker
               (party_stack_get_size, ":size", "p_main_party", ":stack_no"),
               (party_stack_get_num_wounded, ":wounded", "p_main_party", ":stack_no"),
               (val_sub, ":size", ":wounded"),
               (ge, ":size", 30),
#               (val_add, ":modifier_value", 2),
	   (call_script, "script_change_player_party_morale", 1),
#	   (display_message, "@."),
            (try_end),
       ]),

  (48,
   [
           (party_get_num_companion_stacks, ":num", "p_main_party"),
            (try_for_range, ":stack_no", 0, ":num"),
               (party_stack_get_troop_id, ":party_troop", "p_main_party", ":stack_no"),
               (eq, ":party_troop", "trp_sword_sister"),
               (assign, ":num", 0), #loop breaker
               (party_stack_get_size, ":size", "p_main_party", ":stack_no"),
               (party_stack_get_num_wounded, ":wounded", "p_main_party", ":stack_no"),
               (val_sub, ":size", ":wounded"),
               (ge, ":size", 30),
#               (val_add, ":modifier_value", 2),
	   (call_script, "script_change_player_party_morale", 1),
#	   (display_message, "@."),
            (try_end),
       ]),
####chief esposas moral acaba
  #siege warfare chief. A los 7 dias la AI recupera la entrada de comida y tropas. Repara el problema de los lords que no reclutan tropas.
  # (24*7,
   # [
##       (party_set_slot,"$g_encountered_party",centro_bloqueado, 0),               
##       (party_set_slot,"$g_encountered_party",centro_port_blockaded, 0),
# ]),
  # (24,
   # []),
  # (24,
   # []),
  # (24,
   # []),
  # (24,
   # []),
  # (24,
   # []),
  # (24,
   # []),
#####################grueso chief empieza#########################
##refuerzos ciudades chief zaitenko
##  (0.2, #Every 0.2 game hours will the game check if there are any reinforcements in the centers.
##[
##(try_for_parties, ":party_no"), 
##(party_slot_eq, ":party_no", "slot_party_type", spt_reinforcement_party), #Find parties of the type spt_reinforcement_party
##(party_is_in_any_town, ":party_no"), # Is the party in any town?
##(party_get_cur_town, ":cur_center", ":party_no"), #What town are they in?
###(call_script, "script_party_add_party_companions", ":cur_center", ":party_no"), #Add the party to the center, which is infact a party ;)
###(party_clear, ":party_no"), #Not sure if this cleaning up is necessary, but it's a precaution so we don't have a bundle of templates lying around.
##(remove_party, ":party_no"),    #MOTO avoid having game swamped by parties
##(try_end), 
##]),
  #refuerzos acaba chief
  
  #freelancer chief
##  (24,
##   [(call_script, "script_dplmc_init_item_difficulties"),]),

#+freelancer start
  #  WEEKLY PAY AND CHECKS FOR UPGRADE

    (24 * 7, [
        (eq, "$freelancer_state", 1),
		(store_current_hours, "$freelancer_next_pay_time"),#TML
        (val_add, "$freelancer_next_pay_time", 24 * 7), #TML New pay time variable to make sure it's correct. Was often incorrect going by the other one. F123 - Submod -> 1.41
        (troop_get_slot, ":service_xp_start", "trp_player", "slot_troop_freelancer_start_xp"),
        (troop_get_xp, ":player_xp_cur", "trp_player"),
        (store_sub, ":service_xp_cur", ":player_xp_cur", ":service_xp_start"),

        #ranks for pay levels and to upgrade player equipment based on upgrade troop level times 1000
        # (try_begin),
           # (troop_get_upgrade_troop, ":upgrade_troop", "$player_cur_troop", 0),
           # (gt, ":upgrade_troop", 1), #make sure troop is valid and not player troop
           # (store_character_level, ":level", ":upgrade_troop"),
           # (store_pow, ":required_xp", ":level", 2), #square the level and
           # (val_mul, ":required_xp", 100),           #multiply by 100 to get xp
           # (ge, ":service_xp_cur", ":level"),
           # (jump_to_menu, "mnu_upgrade_path"),
        # (try_end),
		(try_begin),
           (troop_get_upgrade_troop, ":upgrade_troop", "$player_cur_troop", 0),
           (gt, ":upgrade_troop", 1), #make sure troop is valid and not player troop
           
		   (call_script, "script_game_get_upgrade_xp_freelancer", "$player_cur_troop"), #chief cambia script para anadir subidas mas dificil
		   (assign, ":required_xp", reg0),		   
		   ##THIS  BLOCK IS ALMOST DEFINITELY BE BETTER than the above two lines which could be commented out in exchange for them.
		   # (store_character_level, ":cur_level", "$player_cur_troop"),
           # (val_sub, ":cur_level", 1),
           # (get_level_boundary, ":cur_level", ":cur_level"),
		   # (store_character_level, ":required_xp", ":upgrade_troop"),
		   # (val_sub, ":required_xp", 1),
		   # (get_level_boundary, ":required_xp", ":required_xp"),
		   # (val_sub, ":required_xp", ":cur_level"),		   
		   ##
		   		   
           (ge, ":service_xp_cur", ":required_xp"),
		   (try_begin),
		   		(call_script, "script_cf_freelancer_player_can_upgrade", ":upgrade_troop"),
				(troop_set_slot, "trp_player", "slot_troop_freelancer_start_xp", ":player_xp_cur"),
				(jump_to_menu, "mnu_upgrade_path"),
		   (else_try),
				(assign, ":reason", reg0), #from cf_freelancer_player_can_upgrade
				(try_begin),
					(eq, ":reason", 0), #not enough strength, for melee weapons
					(display_message, "@You are not strong enough to lift a weapon fit for your promotion!"),
				(else_try),
					(eq, ":reason", 1), #not enough strength, for armor
					(display_message, "@You are not strong enough to hold all that weight required with promotion!."),
				(else_try),
					(eq, ":reason", 2), #not enough power draw/throw/strength for bow/crossbow/throwing
					(display_message, "@Your arms are to weak to advance in the artillary at this moment."),
				(else_try),
					(eq, ":reason", 3), #not enough riding skill for horse
					(display_message, "@You require more horse riding skills to fit your next poisition!"),
				(try_end),				
		   (try_end),			
        (try_end),
		

		#(store_current_hours, "$g_next_pay_time"),
		#(val_add, "$g_next_pay_time", 24 * 7),		
        (store_character_level, ":level", "$player_cur_troop"),
        #pays player 10 times the troop level
        (store_mul, ":weekly_pay", 10, ":level"),
        (troop_add_gold, "trp_player", ":weekly_pay"),
        (add_xp_to_troop, 70, "trp_player"),
        (play_sound, "snd_money_received", 0),
    ]),

#  HOURLY CHECKS

    (1,[
        (eq, "$freelancer_state", 1),
        #so that sight and camera follows near commander's party
        (set_camera_follow_party, "$enlisted_party"),
        (party_relocate_near_party, "p_main_party", "$enlisted_party", 1), 

        (assign, ":num_food", 0),
        (troop_get_inventory_capacity, ":max_inv_slot", "trp_player"),
        (try_for_range, ":cur_inv_slot", ek_item_0, ":max_inv_slot"),
           (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_inv_slot"),
           (ge, ":cur_item", 0),
           (is_between, ":cur_item", food_begin, food_end),
           (val_add, ":num_food", 1),
        (try_end),
        (try_begin),
           (lt, ":num_food", 2),
           (troop_add_item, "trp_player", "itm_bread"),
        (try_end),
    ]),
	
  #+freelancer end chief acaba
#LAZERAS chief MODIFIED  {Top Tier Troops Recruit} (Need to know how to not allow recruiting of prisoners)
  (24,
   [
      #################################################################
      ## LEVEL CHECK BEGIN 
      ## Comment to disable LEVEL CHECK 
      (store_character_level, ":level", "trp_player"),   
      (ge, ":level", 82),
      ## LEVEL CHECK END
      #################################################################
      
	  (store_current_hours,":now"),
      (ge, ":now", "$g_upgrade_time"),
      (store_random_in_range, ":rand", 14, 22),         ## Next Call 14 - 21 days ahead    
      (val_mul, ":rand", 24),
      (val_add, ":rand", ":now"),
      (assign, "$g_upgrade_time"),
	  (assign, ":found", 0),
      (store_random_in_range, ":rand_check", 1, 30),
      (store_random_in_range, ":rand_chance", 1, 100), 
	  (try_begin),
	  (gt, ":rand_check", ":rand_chance"),
         (try_for_range, ":hero_id", additional_heroes_begin, additional_heroes_end),
		  (party_get_num_companion_stacks, ":stack_num", "p_main_party"),
		  (assign, ":result", 0),
		  (try_for_range, ":stack_no", 0, ":stack_num"),
			 (eq, ":result", 0),
			 (party_stack_get_troop_id, ":current_troop", "p_main_party", ":stack_no"),
			 (party_stack_get_size, ":result", "p_main_party", ":stack_no"),
		  (try_end),
			(eq, ":current_troop", ":hero_id"),		  
            (troop_get_slot, ":hero_ocu", ":hero_id", "slot_troop_occupation"),
            (gt, ":hero_ocu", 0),
            (neq, ":hero_ocu",slto_kingdom_hero),
            (neq, ":hero_ocu",slto_player_companion),
            (main_party_has_troop, ":hero_ocu"),
            (assign, ":found", 1),
            (assign, reg11, ":hero_id"),
         (try_end),
         (eq, ":found", 1),
         (jump_to_menu, "mnu_upgrade_to_hero"),
	   (try_end),
    ]),   
#LAZERAS MODIFIED  {Top Tier Troops Recruit}



#saqueo chief
  (0,
   [
			(eq, "$g_center_saqueo", 1),
			(jump_to_menu, "mnu_saquear_centro"),
    ]),

#  Prisioneros a escapar chief garnier
  	  #Check for prisoners to escape
  (1,
   [
      (store_mul,":hours",24,prisoners_escape_chance_modifier),
	  (val_div,":hours",100),
	  (store_random_in_range, ":random",0,":hours"),
	  (try_begin),
		(eq, ":random", 0),
		(call_script, "script_prisoners_escape_from_party"),
		#(call_script, "script_troops_leave_party"), Disabled as it didn't appear to work properly
	  (try_end),
    ]),
#chequeos escaramuzas chief
  (3,
   [
        (assign, "$g_escaramuza_accion", 0),
        (assign, "$g_reclutar_p_puede", 0),
    ]),

#chequeos bounty chief
  (90,
   [
         (assign, "$g_bounty_activo", 0),
         (assign, "$g_rezar_monasterio", 0),
           (assign,"$emboscada_time", 0), #antes de 90 horas no puede haber otra emboscada ambush chief
    ]),

   #reclutar cantabros chief
  (240,
   [
         (assign, "$reclutar_cantabros", 0),
    ]),
    
#chequeo somebody reclutar chief
  	  #Set max warriors available
  (24,
   [
         (assign, "$g_empieza_campeon", 0),
         (assign, "$g_empieza_discurso", 0),
           (assign, "$reclutar_puede", 0),
           (assign, "$reclutar_puede_refuges", 0),
##	  (faction_set_slot, "fac_kingdom_1","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_2","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_3","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_4","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_5","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_6","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_7","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_8","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_9","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_10","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_11","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_12","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_13","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_14","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_15","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_16","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_17","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_18","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_19","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_20","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_21","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_22","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_23","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_24","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_25","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_26","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_27","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_28","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_29","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_30","slot_faction_num_troops",1),
##	  (faction_set_slot, "fac_kingdom_31","slot_faction_num_troops",1),
##
##	  (faction_set_slot, "fac_kingdom_1","slot_faction_town_troop_1","trp_jute_infantryt3"),
##	  (faction_set_slot, "fac_kingdom_2","slot_faction_town_troop_1","trp_saxon_infantryt3"),
##	  (faction_set_slot, "fac_kingdom_3","slot_faction_town_troop_1","trp_saxon_infantryt3"),
##	  (faction_set_slot, "fac_kingdom_4","slot_faction_town_troop_1","trp_engle_infantryt3"),
##	  (faction_set_slot, "fac_kingdom_5","slot_faction_town_troop_1","trp_saxon_infantryt3"),
##	  (faction_set_slot, "fac_kingdom_6","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_7","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_8","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_9","slot_faction_town_troop_1","trp_engle_infantryt3"),
##	  (faction_set_slot, "fac_kingdom_10","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_11","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_12","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_13","slot_faction_town_troop_1","trp_engle_infantryt3"),
##	  (faction_set_slot, "fac_kingdom_14","slot_faction_town_troop_1","trp_engle_infantryt3"),
##	  (faction_set_slot, "fac_kingdom_15","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_16","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_17","slot_faction_town_troop_1","trp_irish_skirmishert3"),
##	  (faction_set_slot, "fac_kingdom_18","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_19","slot_faction_town_troop_1","trp_irish_skirmishert3"),
##	  (faction_set_slot, "fac_kingdom_20","slot_faction_town_troop_1","trp_pict_horsesquiret3"),
##	  (faction_set_slot, "fac_kingdom_21","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_22","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_23","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_24","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_25","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_26","slot_faction_town_troop_1","trp_briton_skirmt3"),
##	  (faction_set_slot, "fac_kingdom_27","slot_faction_town_troop_1","trp_irish_skirmishert3"),
##	  (faction_set_slot, "fac_kingdom_28","slot_faction_town_troop_1","trp_irish_skirmishert3"),
##	  (faction_set_slot, "fac_kingdom_29","slot_faction_town_troop_1","trp_irish_skirmishert3"),
##	  (faction_set_slot, "fac_kingdom_30","slot_faction_town_troop_1","trp_irish_skirmishert3"),
##	  (faction_set_slot, "fac_kingdom_31","slot_faction_town_troop_1","trp_irish_skirmishert3"),
##
##	  (troop_set_slot, "trp_jute_infantryt3","slot_troop_recruit_price",290),
##	  (troop_set_slot, "trp_saxon_infantryt3","slot_troop_recruit_price",290),
##	  (troop_set_slot, "trp_engle_infantryt3","slot_troop_recruit_price",290),
##	  (troop_set_slot, "trp_briton_skirmt3","slot_troop_recruit_price",290),
##	  (troop_set_slot, "trp_irish_skirmishert3","slot_troop_recruit_price",290),
##	  (troop_set_slot, "trp_pict_horsesquiret3","slot_troop_recruit_price",290),
##
##    (call_script,"script_set_max_troops"),
##	(call_script,"script_set_available_troops"),
    ]),
#chief somebody acaba
  ##diplomacy chief begin##############
  #Troop AI Spouse: Spouse thinking
  (3,
   [
    (try_for_parties, ":spouse_party"),  
      (party_slot_eq, ":spouse_party", "slot_party_type", dplmc_spt_spouse),
      
      (troop_get_slot, ":player_spouse", "trp_player", "slot_troop_spouse"),
      (party_get_slot, ":spouse_target", ":spouse_party", "slot_party_orders_object"),
      (party_get_slot, ":home_center", ":spouse_party", "slot_party_home_center"),
      (store_distance_to_party_from_party, ":distance", ":spouse_party", ":spouse_target"),

      #Moving spouse to home village
      (try_begin),
        (le, ":distance", 1),
        (try_begin),
          (this_or_next|eq, ":spouse_target", "$g_player_court"), 
		      (eq, ":spouse_target", ":home_center"), 
          (remove_party, ":spouse_party"),
          (troop_set_slot, ":player_spouse", "slot_troop_cur_center", ":spouse_target"),
        (else_try),
          (try_begin),
            (is_between, ":spouse_target", villages_begin, villages_end),
            (party_get_slot,":cur_merchant",":spouse_target", "slot_town_elder"),
          (else_try), 
            (party_get_slot,":cur_merchant",":spouse_target", "slot_town_merchant"), 
          (try_end),
          (troop_get_slot, ":amount", ":player_spouse", "slot_troop_mission_diplomacy"),
          (troop_remove_items, ":cur_merchant", "itm_bread", ":amount"),        
          (party_set_ai_behavior, ":spouse_party", ai_bhvr_travel_to_party),
          (try_begin),
            (gt, "$g_player_court", 0),
            (party_set_slot, ":spouse_party", "slot_party_ai_object", "$g_player_court"),
            (party_set_ai_object, ":spouse_party", "$g_player_court"), 
          (else_try),
            (party_set_slot, ":spouse_party", "slot_party_ai_object", ":home_center"),
            (party_set_ai_object, ":spouse_party", ":home_center"), 
          (try_end),
            
          (troop_add_items, "trp_household_possessions", "itm_bread", ":amount"), 
        (try_end),
      (try_end),
    (try_end),
    ]),

 #process gift_carvans
 (0.5,
 [
  (eq, "$g_player_chancellor", "trp_dplmc_chancellor"),
  ##nested diplomacy start+ chief
  #These gifts are far too efficient.  To be balanced with Native, they
  #should not (at the best case) exceed an efficiency of 1000 gold per point.
  (assign, ":save_reg0", reg0),
  (assign, ":save_reg1", reg1),
  (options_get_campaign_ai, ":reduce_campaign_ai"),#store for use below
  ##nested diplomacy end+
  (try_for_parties, ":party_no"),
    (party_slot_eq,":party_no", "slot_party_type", dplmc_spt_gift_caravan),
    (party_is_active, ":party_no"),
    (party_get_slot, ":target_party", ":party_no", "slot_party_ai_object"),
    (party_get_slot, ":target_troop", ":party_no", "slot_party_orders_object"),
     
    (try_begin),
      (party_is_active, ":target_party"),
  
      (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),  
      (str_store_party_name, s14, ":party_no"),
      (str_store_party_name, s15,":target_party"),
      
      (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (assign, reg0, ":distance_to_target"),
        (display_message, "@Distance between {s14} and {s15}: {reg0}"),
      (try_end),
  
      (try_begin),
        (le, ":distance_to_target", 1),
  
        (party_get_slot, ":gift", ":party_no", "slot_party_mission_diplomacy"),
        (str_store_item_name, s12, ":gift"),
        
        (try_begin),
          (gt, ":target_troop", 0),
          (str_store_troop_name, s13, ":target_troop"),  
        (else_try),
          (str_store_party_name, s13, ":target_party"),
        (end_try),
        (display_log_message, "@Your caravan has brought {s12} to {s13}.", 0x00FF00),
        (display_message, "@Your caravan has brought {s12} to {s13}.", 0x00FF00),
        
        (assign, ":relation_boost", 0),
        (store_faction_of_party, ":target_faction", ":target_party"),
        
        (try_begin),
          (gt, ":target_troop", 0),
          (faction_slot_eq,":target_faction","slot_faction_leader",":target_troop"),
          (try_begin),
            (eq, ":gift", "itm_wine"),
            (assign, ":relation_boost", 1),
          (else_try),
            (eq, ":gift", "itm_oil"),
            (assign, ":relation_boost", 2),
          (try_end),  
        (else_try),
          (store_random_in_range, ":random", 1, 3),
          (try_begin),
            (eq, ":gift", "itm_ale"),
            (val_add, ":relation_boost", ":random"),
          (else_try),
            (eq, ":gift", "itm_wine"),
            (store_add, ":relation_boost", 1, ":random"),
          (else_try),
            (eq, ":gift", "itm_oil"),
            (store_add, ":relation_boost", 2, ":random"),
          (else_try),
            (eq, ":gift", "itm_raw_dyes"),
            (val_add, ":relation_boost", 1), 
          (else_try),
            (eq, ":gift", "itm_rare_fabric"),
            (val_add, ":relation_boost", 2),    
          (else_try),
            (eq, ":gift", "itm_velvet"),
            (val_add, ":relation_boost", 4),   
          (else_try),
            (eq, ":gift", "itm_smoked_fish"),
            (try_begin),
              (party_slot_eq, ":target_party", "slot_party_type", spt_village),
              (val_add, ":relation_boost", 1),
            (try_end),
          (else_try),
            (eq, ":gift", "itm_cheese"),
            (val_add, ":relation_boost", 1),
            (try_begin),
              (party_slot_eq, ":target_party", "slot_party_type", spt_village),
              (val_add, ":relation_boost", 1),
            (try_end),    
          (else_try),
            (eq, ":gift", "itm_honey"),
            (val_add, ":relation_boost", 2),    
            (try_begin),
              (party_slot_eq, ":target_party", "slot_party_type", spt_village),
              (val_add, ":relation_boost", 2),
            (try_end),                      
          (try_end),  
        (try_end), 
        
        (try_begin),
          (this_or_next|eq, ":target_faction", "fac_player_supporters_faction"),
          (eq, ":target_faction", "$players_kingdom"),
          (val_add, ":relation_boost", 1),    
        (try_end),
        
		##nested diplomacy start+
		#Determine the gold cost of the gifts.
		(store_item_value, ":gift_value", ":gift"),
		#Determine how many copies of the gift are used
		(party_get_slot, ":gift_value_factor", ":party_no", "slot_party_mission_parameter_1"),
		(try_begin),
			#This should only fail if the game was saved using an old version while
			#a caravan was en route.
			(gt, ":gift_value_factor", 0),
			(val_mul, ":gift_value", ":gift_value_factor"),
		(else_try),
			#Gifts to ladies had no multiplier.
			#Also, don't do anything for non-trade-goods.
			(this_or_next|is_between, ":target_troop", kingdom_ladies_begin, kingdom_ladies_end),
			(neg|is_between, ":gift", trade_goods_begin, trade_goods_end),
		(else_try),
			 #Gifts to lords used 150 copies of an item
			(is_between, ":target_troop", active_npcs_begin, active_npcs_end),
			(val_mul, ":gift_value", 150),
		(else_try),
			#Gifts to centers used 300 copies of an item
			(is_between, ":target_party", centers_begin, centers_end),
			(val_mul, ":gift_value", 300),
		(try_end),
		(assign, ":gift_value_factor", 100),

		#(store_sub, ":gift_slot_no", ":gift", trade_goods_begin),
		#(val_add, ":gift_slot_no", "slot_town_trade_good_prices_begin"),

		(try_begin),
			#Gift isn't a trade good: this should never happen
			(neg|is_between, ":gift", trade_goods_begin, trade_goods_end),
			(try_begin),
				(this_or_next|gt, ":target_troop", 0),
					(party_slot_eq, ":target_party", "slot_party_type", spt_town),
				(assign, ":gift_value_factor", 115),
			(else_try),
				(assign, ":gift_value_factor", 130),
			(try_end),
		(else_try),
			#Given to a lord.
			(gt, ":target_troop", 0),

			(assign, ":global_price_factor", 0),
			(assign, ":faction_price_factor", 0),
			(assign, ":faction_markets", 0),
			(assign, ":personal_price_factor", 0),
			(assign, ":personal_markets", 0),

			(try_for_range, ":center_no", towns_begin, towns_end),
				(call_script, "script_dplmc_get_item_buy_price_factor", ":gift", ":center_no", -2, -2),
				(val_add, ":global_price_factor", reg0),

				(store_faction_of_party, ":center_faction", ":center_no"),
				(eq, ":center_faction", ":target_faction"),
				(val_add, ":faction_price_factor", reg0),
				(val_add, ":faction_markets", 1),

				(party_slot_eq, ":center_no", "slot_town_lord", ":target_troop"),
				(val_add, ":personal_price_factor", reg0),
				(val_add, ":personal_markets", 1),
			(try_end),

			(try_begin),
				(eq, ":personal_markets", 0),
				(try_for_range, ":center_no", villages_begin, villages_end),
					(try_begin),
						(party_slot_eq, ":center_no", "slot_town_lord", ":target_troop"),
						(call_script, "script_dplmc_get_item_buy_price_factor", ":gift", ":center_no", -2, -2),
						(val_add, ":faction_markets", reg0),
						(val_add, ":personal_markets", 1),
					(try_end),
					#Check for castles (deliberately allow multiple-counting)
					(try_begin),
						(party_get_slot, reg1, ":center_no", "slot_village_bound_center"),
						(gt, reg1, 0),
						(party_slot_eq, reg1, "slot_party_type", spt_castle),
						(party_slot_eq, reg1, "slot_town_lord", ":target_troop"),
						(call_script, "script_dplmc_get_item_buy_price_factor", ":gift", ":center_no", -2, -2),
						(val_add, ":faction_markets", reg0),
						(val_add, ":personal_markets", 1),
					(try_end),
				(try_end),
			(try_end),

			(try_begin),
				#First use any markets at or near the target's fiefs
				(gt, ":personal_markets", 0),
				(store_div, ":gift_value_factor", ":personal_price_factor", ":personal_markets"),
			(else_try),
				#Alternately use any faction markets
				(gt, ":faction_markets", 0),
				(val_mul, ":faction_price_factor", 130),#Convert trade penalty from 115% to 130%
				(val_div, ":faction_price_factor", 115),
				(store_div, ":gift_value_factor", ":faction_price_factor", ":faction_markets"),
			(else_try),
				#As a final option use the global average price
				(gt, towns_end, towns_begin),#should always be true (if not, then the gift price factor stays average)
				(store_sub, reg1, towns_end, towns_begin),
				(val_mul, ":global_price_factor", 130),#Convert trade penalty from 115% to 130%
				(val_div, ":global_price_factor", 115),
				(store_div, ":gift_value_factor", ":global_price_factor", reg1),
			(try_end),
		(else_try),
			#Given to a town or village
			(gt, ":target_party", 0),
			(call_script, "script_dplmc_get_item_buy_price_factor", ":gift", ":center_no", -2, -2),
			(assign, ":gift_value_factor", reg0),
		(else_try),
			#This should never happen
			(assign, ":gift_value_factor", 115),
		(try_end),

		(try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg0, ":gift_value_factor"),
			(store_mul, reg1, ":gift_value", ":gift_value_factor"),
			(val_add, reg1, 50),
			(val_div, reg1, 100),
			(val_add, reg1, 50),
			(display_message, "@{!} Gift price factor {reg0}/100, effective value {reg1}"),
		(try_end),

		(val_mul, ":gift_value", ":gift_value_factor"),
		(val_add, ":gift_value", 50),
		(val_div, ":gift_value", 100),

		(val_add, ":gift_value", 50),#the cost of the messenger
	    (store_random_in_range, ":random", 0, 1000),#randomly round up or down later, when dividing by 1000
		(assign, reg0, ":gift_value"),#<-- see (1) below, store gold value of gift
		(val_add, ":gift_value", ":random"),
		(val_div, ":gift_value", 1000),

		(try_begin),
		   (eq, ":reduce_campaign_ai", 0), #hard: do not exceed 1/1000 efficiency
		   (val_min, ":relation_boost", ":gift_value"),
		   (try_begin),
			  (eq, ":relation_boost", 0),
			  (store_random_in_range, ":random", 0, 1000),
			  (lt, ":random", reg0),#<-- (1) see above, has gold value of gift
			  (assign, ":relation_boost", 1),
		   (try_end),
		(else_try),
		   (eq, ":reduce_campaign_ai", 1), #medium: use a blend of the two
		   (lt, ":gift_value", ":relation_boost"),
		   (val_add, ":relation_boost", ":gift_value"),
		   (val_add, ":relation_boost", 1),
		   (val_div, ":relation_boost", 2),
	    (else_try),
		   (eq, ":reduce_campaign_ai", 2), #easy: do not use
		(try_end),

		(val_max, ":gift_value", 1),
		(val_min, ":relation_boost", ":gift_value"),
		##nested diplomacy end+

        (try_begin),
		##nested diplomacy start+
		#Write a message so the player doesn't think the lack of relation gain is an error.
			(lt, ":relation_boost", 1),
			(try_begin),
				(gt, ":target_troop", 0),
				(display_message, "@{s13} is unimpressed by your paltry gift."),
			(else_try),
				(display_message, "@The people of {s13} are unimpressed by your paltry gift."),
			(try_end),
		(else_try),
		##nested diplomacy+
          (gt, ":target_troop", 0),
		  (call_script, "script_change_player_relation_with_troop", ":target_troop", ":relation_boost"),
        (else_try),
          (call_script, "script_change_player_relation_with_center", ":target_party", ":relation_boost"),
        (try_end),
        (remove_party, ":party_no"),
      (try_end),
    (else_try),
      (display_log_message, "@Your caravan has lost it's way and gave up your mission!", 0xFF0000),
      (remove_party, ":party_no"),
    (try_end),
  (try_end),
  ##nested diplomacy start+
  (assign, reg0, ":save_reg0"),
  (assign, reg1, ":save_reg1"),
  ##nested diplomacy start+
 ]),
 
 #process messengers
 (0.5,
 [
  (try_for_parties, ":party_no"),
    (party_slot_eq,":party_no", "slot_party_type", spt_messenger),

    (party_get_slot, ":target_party", ":party_no", "slot_party_ai_object"),
    (party_get_slot, ":orders_object", ":party_no", "slot_party_orders_object"),
    
    (try_begin),
      (party_is_active, ":target_party"),
      (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),  
      (str_store_party_name, s14, ":party_no"),
      (str_store_party_name, s15,":target_party"),
      
      (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (assign, reg0, ":distance_to_target"),
        (display_message, "@Distance between {s14} and {s15}: {reg0}"),
      (try_end),
  
      (try_begin),
        (le, ":distance_to_target", 1),
    
        (try_begin), # returning to p_main_party
          (eq, ":target_party", "p_main_party"),
          (party_get_slot, ":party_leader", ":party_no", "slot_party_orders_object"), 
          (party_get_slot, ":success", ":party_no", "slot_party_mission_diplomacy"),
          (call_script, "script_add_notification_menu", "mnu_dplmc_messenger", ":party_leader", ":success"),   
          (remove_party, ":party_no"),
        (else_try), # patrols
          (party_slot_eq, ":target_party", "slot_party_type", spt_patrol),
          (party_get_slot, ":message", ":party_no", "slot_party_mission_diplomacy"),

          (try_begin),
            (eq, ":message", spai_undefined),
            (remove_party, ":target_party"),
          (else_try),
            (eq, ":message", spai_retreating_to_center),
            (str_store_party_name, s6, ":orders_object"),           
            (party_set_name, ":target_party", "@Transfer to {s6}"),
            (party_set_ai_behavior, ":target_party", ai_bhvr_travel_to_party), 
            (party_set_ai_object, ":target_party", ":orders_object"),
            (party_set_slot, ":target_party", "slot_party_ai_object", ":orders_object"),
            (party_set_slot, ":target_party", "slot_party_ai_state", spai_retreating_to_center),                       
            (party_set_aggressiveness, ":target_party", 0),
            (party_set_courage, ":target_party", 3),
            (party_set_ai_initiative, ":target_party", 100),
          (else_try),
            (str_store_party_name, s6, ":orders_object"),           
            (party_set_name, ":target_party", "@{s6} patrol"),
            (party_set_ai_behavior, ":target_party", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":target_party", ":orders_object"),
            (party_set_slot, ":target_party", "slot_party_ai_object", ":orders_object"),
            (party_set_slot, ":target_party", "slot_party_orders_type", ":message"),
          (try_end),

          (remove_party, ":party_no"),
        (else_try), # reached any other target
          (party_stack_get_troop_id, ":party_leader", ":target_party", 0),
          (str_store_troop_name, s13, ":party_leader"), 
    
          (try_begin), #debug
            (eq, "$cheat_mode", 1),
            (display_log_message, "@Your messenger reached {s13}.", 0x00FF00),
            (assign, "$g_talk_troop", ":party_leader"), #debug
          (try_end),
          
          (party_get_slot, ":message", ":party_no", "slot_party_mission_diplomacy"),
          (assign, ":success", 0),
          (try_begin),
            (party_set_slot, ":target_party", "slot_party_commander_party", "p_main_party"),
          	(store_current_hours, ":hours"),
          	(party_set_slot, ":target_party", "slot_party_following_orders_of_troop", "trp_kingdom_heroes_including_player_begin"),
          	(party_set_slot, ":target_party", "slot_party_orders_object", ":orders_object"),
          	(party_set_slot, ":target_party", "slot_party_orders_type", ":message"),
          	
          	(party_set_slot, ":target_party", "slot_party_orders_time", ":hours"),
            (call_script, "script_npc_decision_checklist_party_ai", ":party_leader"), #This handles AI for both marshal and other parties		
  
  
            (try_begin), #debug
              (eq, "$cheat_mode", 1),
              (display_message, "@{s14}"), #debug
            (try_end),
  
            (try_begin),
              (eq, reg0, ":message"),
              (eq, reg1, ":orders_object"),
              (assign, ":success", 1),
            (try_end),
            (call_script, "script_party_set_ai_state", ":target_party", reg0, reg1),
          (try_end),
          
          (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party), 
          (party_set_ai_object, ":party_no", "p_main_party"),  
          (party_set_slot, ":party_no", "slot_party_ai_object", "p_main_party"),
          (party_set_slot, ":party_no", "slot_party_orders_object", ":party_leader"), 
          (party_set_slot, ":party_no", "slot_party_mission_diplomacy", ":success"),
        (try_end),
      (try_end),
    (else_try),
      (display_log_message, "@Your messenger has lost it's way and gave up your mission!", 0xFF0000),
      (remove_party, ":party_no"),
    (try_end),
  (try_end),
 ]),

      # Policy
   (30 * 24,
   [  
  (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),    
    (faction_slot_eq, ":kingdom", "slot_faction_state", sfs_active),
    
    (faction_get_slot, ":centralization", ":kingdom", "slot_faction_centralization"),
    (faction_get_slot, ":aristocracy", ":kingdom", "slot_faction_aristocracy"),
    (faction_get_slot, ":quality", ":kingdom", "slot_faction_quality"),
    (faction_get_slot, ":serfdom", ":kingdom", "slot_faction_serfdom"),
  	 ##nested diplomacy start+
    (faction_get_slot, ":mercantilism", ":kingdom", "slot_faction_mercantilism"),
	 ##nested diplomacy end+
  
    (try_begin),
      (eq, "$cheat_mode", 1),
      (str_store_faction_name, s9, ":kingdom"),
      (assign, reg1, ":centralization"),
      (display_message, "@{!}DEBUG - centralization {reg1}"),
      (assign, reg1, ":aristocracy"),
      (display_message, "@{!}DEBUG - aristocracy {reg1}"),
      (assign, reg1, ":quality"),
      (display_message, "@{!}DEBUG - quality {reg1}"),
      (assign, reg1, ":serfdom"),
      (display_message, "@{!}DEBUG - serfdom {reg1}"),
		##nested diplomacy start+
      (assign, reg1, ":mercantilism"),
      (display_message, "@{!}DEBUG - mercantilism {reg1}"),
		##nested diplomacy end+
    (try_end),

    (try_begin),
      (is_between, ":kingdom", npc_kingdoms_begin, npc_kingdoms_end),
      
       ##nested diplomacy start+
	  (store_random_in_range, ":random", 0, 10),
      ##nested diplomacy end+
      
      (try_begin),
		  ##nested diplomacy start+
        #(is_between, ":random", 1, 5),
		  (is_between, ":random", 1, 6),
		  ##nested diplomacy end+
        (store_random_in_range, ":change", -1, 2),
      
        (try_begin),
          (eq, "$cheat_mode", 1),
          (str_store_faction_name, s12, ":kingdom"),
          (assign, reg1, ":change"),
          (assign, reg2, ":random"),
          (display_message, "@{!}DEBUG - changing {reg1} of {reg2} for {s12}"),
        (try_end),
        
        (try_begin),
          (eq, ":random", 1),
          (val_add, ":centralization", ":change"),
          (val_max, ":centralization", -3),
          (val_min, ":centralization", 3),
          (faction_set_slot, ":kingdom", "slot_faction_centralization", ":centralization"),
        (else_try),
          (eq, ":random", 2),
          (val_add, ":aristocracy", ":change"),
          (val_max, ":aristocracy", -3),
          (val_min, ":aristocracy", 3),
          (faction_set_slot, ":kingdom", "slot_faction_aristocracy", ":aristocracy"),
        (else_try),
          (eq, ":random", 3),
          (val_add, ":quality", ":change"),
          (val_max, ":quality", -3),
          (val_min, ":quality", 3),
          (faction_set_slot, ":kingdom", "slot_faction_quality", ":quality"),
        (else_try),
          (eq, ":random", 4),
          (val_add, ":serfdom", ":change"),
          (val_max, ":serfdom", -3),
          (val_min, ":serfdom", 3),
          (faction_set_slot, ":kingdom", "slot_faction_serfdom", ":serfdom"),
  		  ##nested diplomacy start+
          (eq, ":random", 5),
          (val_add, ":mercantilism", ":change"),
			 (val_clamp, ":mercantilism", -3, 4),#-3 min, +3 max
          (faction_set_slot, ":kingdom", "slot_faction_mercantilism", ":mercantilism"),
		  ##nested diplomacy end+
      (try_end),
      (try_end),
    
    (else_try),
      #only player faction is affected by relation hits      
      ##nested diplomacy start+
      ##Don't alter the values of centralization and aristocracy, since that's confusing.
      #(store_mul, ":centralization", ":centralization", -1),
      #(store_mul, ":aristocracy", ":aristocracy", 1),
      #(store_add, ":relation_change", ":centralization", ":aristocracy"),

		(store_sub, ":relation_change", ":aristocracy", ":centralization"),
      ##custodian (merchant) lords like plutocracy, unlike ordinary lords
      (store_mul, ":custodian_change", ":aristocracy", -1),
		(val_sub, ":custodian_change", ":centralization"),
      #benefactor lords like freedom and dislike serfdom
		(store_mul, ":benefactor_change", ":serfdom", -1),
		(val_sub, ":custodian_change", ":centralization"),
      ##nested diplomacy end+           
      (try_begin),
        ##nested diplomacy start+
        (this_or_next|neq, ":benefactor_change", 0),
        (this_or_next|neq, ":custodian_change", 0),
        ##nested diplomacy end+
        (neq, ":relation_change", 0),
      
        (try_begin),
          (eq, "$cheat_mode", 1),
          (str_store_faction_name, s9, ":kingdom"),
          (assign, reg1, ":relation_change"),
          (display_message, "@{!}DEBUG - relation_change =  {reg1} for {s9}"),
  (try_end),
        
        (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
          (store_troop_faction, ":faction_no", ":troop_no"),
          (eq, ":kingdom", ":faction_no"),
          (faction_get_slot, ":faction_leader", ":kingdom", "slot_faction_leader"),
          (call_script, "script_troop_change_relation_with_troop", ":faction_leader", ":troop_no", ":relation_change"),
          ##diplomacy start+
          (neq, ":troop_no", ":faction_leader"),
          (assign, ":change_for_troop", ":relation_change"),
          (try_begin),
             (troop_slot_eq, ":troop_no", "slot_lord_reputation_type", lrep_custodian),
             (assign, ":change_for_troop", ":custodian_change"),
          (else_try),
             (troop_slot_eq, ":troop_no", "slot_lord_reputation_type", lrep_benefactor),
             (assign, ":change_for_troop", ":benefactor_change"),
        (try_end),   
          ##Extra penalty for going back on a promise, extra bonus for keeping it
          (assign, ":promise_mod", 0),
          (try_begin),
             ##Following are only relevant for companions
				 (is_between, ":troop_no", companions_begin, companions_end),
             (troop_slot_eq, ":troop_no", "slot_troop_kingsupport_state", 1),
             (try_begin),
                #Argument: Lords
                (troop_slot_eq, ":troop_no", "slot_troop_kingsupport_argument", argument_lords),
                (try_begin),
                  #If more than slightly centralized, or more than slightly balanced against aristocrats  
                  (this_or_next|neg|faction_slot_ge, ":faction_no", "slot_faction_aristocracy", -1),
                     (faction_slot_ge, ":faction_no", "slot_faction_centralization", 2),
                  (val_sub, ":promise_mod", 1),
                (else_try),
                  #If more than slightly decentralized or more than slightly balanced in favor of aristocrats
                  (this_or_next|faction_slot_ge, ":faction_no", "slot_faction_aristocracy", 2),
                  (neg|faction_slot_ge, ":faction_no", "slot_faction_centralization", -2),
                  (faction_slot_ge, ":faction_no", "slot_faction_aristocracy", -1),#redundant
                  (val_add, ":promise_mod", 1),
                (try_end),
             (else_try),
                  #Argument: Commons
                  (troop_slot_eq, ":troop_no", "slot_troop_kingsupport_argument", argument_commons),
                  (try_begin),
                    (faction_slot_ge, ":faction_no", "slot_faction_serfdom", 2),
                    (val_sub, ":promise_mod", 1),
                  (else_try),
                    (neg|faction_slot_ge, ":faction_no", "slot_faction_serfdom", 0),
                    (store_add, ":local_temp", ":serfdom", ":aristocracy"),
                    (lt, ":local_temp", 0),
                    (val_add, ":promise_mod", 1),
                  (try_end),
             (try_end),
         (try_end),
         #Check other broken promises
         (try_begin),
             (troop_slot_eq, ":troop_no", "slot_lord_recruitment_argument", argument_lords),
             (this_or_next|neg|faction_slot_ge, ":faction_no", "slot_faction_aristocracy", -1),
                (faction_slot_ge, ":faction_no", "slot_faction_centralization", 2),
             #Lord must actually have cared about argument
             (neg|troop_slot_eq, ":troop_no", "slot_lord_reputation_type", lrep_debauched),
             (neg|troop_slot_eq, ":troop_no", "slot_lord_reputation_type", lrep_upstanding),
             (val_sub, ":promise_mod", 1),
         (else_try),
             (troop_slot_eq, ":troop_no", "slot_lord_recruitment_argument", argument_commons),
             (faction_slot_ge, ":faction_no", "slot_faction_serfdom", 2),
             #Lord must actually have cared about argument
             (neg|troop_slot_eq, ":troop_no", "slot_lord_reputation_type", lrep_quarrelsome),
             (neg|troop_slot_eq, ":troop_no", "slot_lord_reputation_type", lrep_selfrighteous),
             (neg|troop_slot_eq, ":troop_no", "slot_lord_reputation_type", lrep_debauched),
             (val_sub, ":promise_mod", 1),
         (try_end),
         (val_clamp, ":promise_mod", -1, 2),#-1, 0, or 1
         (val_add, ":change_for_troop", ":promise_mod"),
         
		 (neq, ":change_for_troop", 0),
		 (call_script, "script_change_player_relation_with_troop", ":troop_no", ":change_for_troop"),
        ##diplomacy end+
        (try_end),   
      (try_end),
    (try_end),
  (try_end),
  ]),

  # affilated family ai
   (24 * 7,
   [         
    (is_between, "$g_player_affiliated_troop", lords_begin, kingdom_ladies_end),
    
    (assign, ":bad_relation", 0),
    (try_for_range, ":family_member", lords_begin, kingdom_ladies_end),
      (call_script, "script_dplmc_is_affiliated_family_member", ":family_member"),
      (gt, reg0, 0),
      (call_script, "script_troop_get_player_relation", ":family_member"),
      (le, reg0, -20),
      (assign, ":bad_relation", ":family_member"),
    (try_end), 
    
    (try_begin),
      (eq, ":bad_relation", 0),

      (try_for_range, ":family_member", lords_begin, kingdom_ladies_end),
        (call_script, "script_dplmc_is_affiliated_family_member", ":family_member"),
        (gt, reg0, 0),
        (try_begin),
           (troop_slot_ge, ":family_member", "slot_troop_prisoner_of_party", 0),
           (call_script, "script_change_player_relation_with_troop", ":family_member", -1),
        (else_try),
          (call_script, "script_change_player_relation_with_troop", ":family_member", 1),
        (try_end),
      (try_end),   
    (else_try),
      (call_script, "script_add_notification_menu", "mnu_dplmc_affiliate_end", ":bad_relation", 0),
      (call_script, "script_dplmc_affiliate_end", 1),
    (try_end),
    ]),
    
   (2,
   [
    (assign, ":has_walled_center", 0),
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", centers_begin, centers_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", "slot_town_lord"),
      (eq, ":lord_troop_id", "trp_player"),    
      (try_begin),
        (is_between, ":center_no", walled_centers_begin, walled_centers_end),
        (assign, ":has_walled_center", 1),
      (try_end),
      (assign, ":has_fief", 1),
    (try_end),
    
    (try_begin),
      (eq, ":has_walled_center", 0),
      (neq, "$g_player_chancellor", 0),
      (assign, "$g_player_chancellor", 0),
    (try_end),
    
    (try_begin),
      (eq, ":has_fief", 0),
      (neq, "$g_player_chamberlain", 0),
      (assign, "$g_player_chamberlain", 0),
      
      (store_troop_gold, ":cur_gold", "trp_household_possessions"),
      (try_begin),
        (gt, ":cur_gold", 0),
        (call_script, "script_dplmc_withdraw_from_treasury", ":cur_gold"),
        (val_div, ":cur_gold", 3),
        (call_script, "script_troop_add_gold", "trp_player", ":cur_gold"),
        (display_message, "@Your last fief was captured and you lost 2/3 of your treasury"),      
      (try_end),
    (try_end),
    ]),
    
   (1,	#MOTO recycle trigger (to 1 from 24) from another 24-hour trigger
   [
	(store_time_of_day, ":oclock"),
	(store_current_day, ":day_mod"),
	(val_mod, ":day_mod", 8),	#eighth the rate of incidents moto chief
	
	(store_sub, ":num_villages", villages_end, villages_begin),
	(val_div, ":num_villages", 23),
	(store_mul, ":start_village", ":oclock", ":num_villages"),
	(val_add, ":start_village", villages_begin),
	(store_add, ":end_village", ":start_village", ":num_villages"),
	(val_min, ":end_village", villages_end),
	
	#MOTO ramp up border incidents
	(try_for_range, ":acting_village", ":start_village", ":end_village"),
		(store_mod, reg0, ":acting_village", 8),	#eighth the rate of incidents moto chief
		(eq, reg0, ":day_mod"),
	# (try_begin),
		# (store_random_in_range, ":acting_village", villages_begin, villages_end),
	#MOTO ramp up border incidents end
		(store_random_in_range, ":target_village", villages_begin, villages_end),
		(store_faction_of_party, ":acting_faction", ":acting_village"),
		(store_faction_of_party, ":target_faction", ":target_village"), #target faction receives the provocation
		(neq, ":acting_village", ":target_village"),
		(neq, ":acting_faction", ":target_faction"),
		
		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":target_faction", ":acting_faction"),
		(eq, reg0, 0),

		(try_begin),
			(party_slot_eq, ":acting_village", "slot_center_original_faction", ":target_faction"),
			
			(call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", -1),
		(else_try),
			(party_slot_eq, ":acting_village", "slot_center_ex_faction", ":target_faction"),
			
			(call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", -1),
			
		(else_try),
			(set_fixed_point_multiplier, 1),
			(store_distance_to_party_from_party, ":distance", ":acting_village", ":target_village"),
			(lt, ":distance", 25),
			
			(call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", ":target_village"),
		(try_end),
	(try_end),
      # (try_for_range, ":faction1", npc_kingdoms_begin, npc_kingdoms_end),	MOTO duplicates script_npc_decision_checklist_peace_or_war (besides neither being correct nor complete)
        # (assign, ":attitude_change", 2), #positive means good attitude
        # (try_for_range, ":faction2", kingdoms_begin, kingdoms_end),
          # (neq, ":faction1", ":faction2"),
          # # (try_for_parties, ":party"),	MOTO ay Dios mio
            # # (is_between, ":party", centers_begin, centers_end),
            # # (store_faction_of_party, ":party_faction", ":party"),
            # # (eq, ":party_faction", ":faction2"),
            # # (party_slot_eq, ":faction1", ":party", "slot_center_original_faction"),
          # (try_for_range, ":center", centers_begin, centers_end),	#lose attitude for each center faction2 has taken from faction1
            # (store_faction_of_party, ":center_faction", ":center"),
            # (eq, ":center_faction", ":faction2"),
            # (party_slot_eq, ":center", "slot_center_original_faction", ":faction1"),
			# #MOTO ay Dios mio end
            # (val_sub, ":attitude_change", 1), #less attitude
          # (try_end),

          # (try_for_range, ":faction3", kingdoms_begin, kingdoms_end),
            # (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":faction2", ":faction3"),
            # (eq, reg0, -2), #war between 2 and 3
            # (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":faction1", ":faction3"),
            # (eq, reg0, -2), #war between 1 and 3
            # (val_add, ":attitude_change", 1), #higher attitude
          # (try_end),
        # (try_end),  
        
        # (store_add, ":faction1_to_faction2_slot", ":faction2", "slot_faction_attitude_begin"),
        # # (party_set_slot, ":faction1", ":faction1_to_faction2_slot", ":attitude_change"),	MOTO ay Dios mio
        # (val_sub, ":faction1_to_faction2_slot", kingdoms_begin),
        # (faction_set_slot, ":faction1", ":faction1_to_faction2_slot", ":attitude_change"),
		# #MOTO ay Dios mio end
      # (try_end),
    ]),

  ##diplomacy chief end
##############SOD CHIEF EMPIEZA
  #TEMPLE AND CHAPEL
(24 * 7,
	[
	(try_for_range, ":center_no", centers_begin, centers_end),
		(party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
		(this_or_next|party_slot_eq, ":center_no", "slot_center_has_temple1", 1),
		(this_or_next|party_slot_eq, ":center_no", "slot_center_has_temple2", 1),
		(this_or_next|party_slot_eq, ":center_no", "slot_center_has_temple3", 1),
		(this_or_next|party_slot_eq, ":center_no", "slot_center_has_temple5", 1),
		(party_slot_eq, ":center_no", "slot_center_has_chapel5", 1),
		(party_get_slot, ":faith", ":center_no", "slot_center_sod_local_faith"),
    (try_begin),
		(eq, "$g_sod_faith", 4),                                                        
		(val_add, ":faith", 7),#gdw was5
    (else_try),
                   (this_or_next|eq, "$g_sod_faith", 2),
			(eq, "$g_sod_faith", 3),
		(val_add, ":faith", -7),#gdw was5
    (assign,reg1,":faith"),
	(try_end),

    		(party_set_slot, ":center_no", "slot_center_sod_local_faith", ":faith"),
		(val_add, "$g_sod_global_faith", 5),
			(party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
			(party_get_slot, ":cur_relation", ":center_no", "slot_center_player_relation"),
			(val_add, ":cur_relation", 1),
			(party_set_slot, ":center_no", "slot_center_player_relation", ":cur_relation"),
		# DEBUG REMOVE ME
(display_message, "@Faith change of {reg1}"),#gdwaddedbackin due to bugs
	(try_end),
]),

#SHRINE
(24 * 7,
	[
	
	(try_for_range, ":center_no", centers_begin, centers_end),
		(party_slot_eq, ":center_no", "slot_center_has_shrine5", 1),
		(party_get_slot, ":faith", ":center_no", "slot_center_sod_local_faith"),
    (try_begin),
		(eq, "$g_sod_faith", 4),                                                        
		(val_add, ":faith", 7),#gdw was5
    (else_try),
      (this_or_next|eq, "$g_sod_faith", 2),
			(eq, "$g_sod_faith", 3),
		(val_add, ":faith", -7),#gdw was5
	(try_end),
		(party_set_slot, ":center_no", "slot_center_sod_local_faith", ":faith"),
		(val_add, "$g_sod_global_faith", 3),
			(party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
			(party_get_slot, ":cur_relation", ":center_no", "slot_center_player_relation"),
			(val_add, ":cur_relation", 1),
			(party_set_slot, ":center_no", "slot_center_player_relation", ":cur_relation"),
		# DEBUG REMOVE ME
(display_message, "@New cult place is working"),#addedbackin due to report bug gdw
	(try_end),
	]),

#MONASTERY
(24 * 7,
	[
	
	(try_for_range, ":center_no", centers_begin, centers_end),		
		(this_or_next|party_slot_eq, ":center_no", "slot_center_has_monastery1", 1),
		(this_or_next|party_slot_eq, ":center_no", "slot_center_has_monastery2", 1),
		(party_slot_eq, ":center_no", "slot_center_has_monastery3", 1),
		(party_get_slot, ":faith", ":center_no", "slot_center_sod_local_faith"),
    (try_begin),
		(eq, "$g_sod_faith", 4),                                                        
		(val_add, ":faith", 7),#gdw was5
    (else_try),
                   (this_or_next|eq, "$g_sod_faith", 2),
			(eq, "$g_sod_faith", 3),
		(val_add, ":faith", -7),#gdw was5
	(try_end),
		(party_set_slot, ":center_no", "slot_center_sod_local_faith", ":faith"),
		(val_add, "$g_sod_global_faith", 2),
		(party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),
		(val_add, ":prosperity", 3),
		(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),	
			(party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
			(party_get_slot, ":cur_relation", ":center_no", "slot_center_player_relation"),
			(val_add, ":cur_relation", 1),
			(party_set_slot, ":center_no", "slot_center_player_relation", ":cur_relation"),
			# DEBUG REMOVE ME
		(display_message, "@New cult place is working."),#addedbackin due to report bug gdw
	(try_end),
	]),

#UNIVERSITY
(24 * 7,
	[
	#(try_for_range, ":cur_village", villages_begin, villages_end),
   #   (party_slot_eq, ":cur_village", "slot_town_lord", "trp_player"),
   #   (party_slot_eq, ":cur_village", "slot_center_has_school", 1),
   #   (party_get_slot, ":cur_relation", ":cur_village", "slot_center_player_relation"),
   #   (val_add, ":cur_relation", 1),
   #   (val_min, ":cur_relation", 100),
   ##   (party_set_slot, ":cur_village", "slot_center_player_relation", ":cur_relation"),
    #(try_end),
    #]),
	(try_for_range, ":center_no", centers_begin, centers_end),		
		(party_slot_eq, ":center_no", "slot_center_has_university", 1),
    (party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),
    (val_add, ":prosperity", 2),#gdw5
    (party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),  
#		(party_get_slot, ":center_lord", ":center_no", "slot_town_lord"),
	#	(party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
		(call_script, "script_change_troop_renown", "trp_player", 10),
			# DEBUG REMOVE ME#gdw10
		(display_message, "@Library improved your renown."),
    (display_message, "@Library added 2 prosperity to your town/s."),
	(try_end),
	]),

#GUILD
(24 * 7,
	[
	
	(try_for_range, ":center_no", centers_begin, centers_end),		

		(party_slot_eq, ":center_no", "slot_center_has_guild", 1),
		(party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),
		(val_add, ":prosperity", 7),#gdw5
		(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),	
		# DEBUG REMOVE ME
		(display_message, "@Merchants guild add prosperity to your town/s."),
	(try_end),
	]),

#edificios religiosos generan prosperidad
(24 * 7,
	[
	
	(try_for_range, ":center_no", centers_begin, centers_end),		

		(party_slot_eq, ":center_no", "slot_center_has_temple1", 1),
		(party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),
		(val_add, ":prosperity", 3),#gdw2
		(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),	
		# DEBUG REMOVE ME
		(display_message, "@Monasteries add prosperity to your town/s."),
	(try_end),
	]),

(24 * 7,
	[
	
	(try_for_range, ":center_no", centers_begin, centers_end),		

		(party_slot_eq, ":center_no", "slot_center_has_temple2", 1),
		(party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),
		(val_add, ":prosperity", 3),#gdw2
		(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),	
		# DEBUG REMOVE ME
		(display_message, "@Sacred Forest add prosperity to your town/s."),
	(try_end),
	]),

(24 * 7,
	[
	
	(try_for_range, ":center_no", centers_begin, centers_end),		

		(party_slot_eq, ":center_no", "slot_center_has_temple3", 1),
		(party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),
		(val_add, ":prosperity", 3),#gdw2
		(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),	
		# DEBUG REMOVE ME
		(display_message, "@Woden's temple add prosperity to your town/s."),
	(try_end),
	]),

(24 * 7,
	[
	
	(try_for_range, ":center_no", centers_begin, centers_end),		

		(party_slot_eq, ":center_no", "slot_center_has_temple5", 1),
		(party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),
		(val_add, ":prosperity", 3),#gdw2
		(party_set_slot, ":center_no", "slot_town_prosperity", ":prosperity"),	
		# DEBUG REMOVE ME
		(display_message, "@Monasteries add prosperity to your town/s."),
	(try_end),
	]),
#prosperidad acaba chief
  #Change relation due to faith
(24 * 7,
	[
	(try_for_range, ":center_no", centers_begin, centers_end),
			(party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
			(party_get_slot, ":cur_relation", ":center_no", "slot_center_player_relation"),
			(party_get_slot, ":cur_faith", ":center_no", "slot_center_sod_local_faith"),

    (try_begin),
		 (this_or_next|eq, "$g_sod_faith", 1),##if player christian, divide faith level by 30. If they're pagain, this will give a # between -1.5 to -4.5
      (eq, "$g_sod_faith", 4),                                                       
			(val_div, ":cur_faith", 30),##gdw was 20
       (this_or_next|eq, "$g_sod_faith", 1),
                (eq, "$g_sod_faith", 4),
    (else_try),
      (this_or_next|eq, "$g_sod_faith", 2),
			(eq, "$g_sod_faith", 3),
			(val_mul, ":cur_faith", -1),
			(val_div, ":cur_faith", 30),##gdw was 20
	(try_end),
			(val_add, ":cur_relation", ":cur_faith"),
			(party_set_slot, ":center_no", "slot_center_player_relation", ":cur_relation"),
		# DEBUG REMOVE ME
	(display_message, "@FAITH RELATION: Your faith change your relation with centers."),
	(try_end),
	]),


#para saqueo
(90,
	[
	(try_for_range, ":center_no", centers_begin, centers_end),
        (party_slot_eq, ":center_no", "slot_town_sacked", 1),
		(party_set_slot, ":center_no", "slot_town_sacked", 0),
	(try_end),
]),  




#Activamos -religion-, ram para savegames
(1,
	[
     
          (eq, "$g_savegames_necesario", 0),    
      (party_set_slot,"p_castle_23", "slot_center_siege_with_ram",      0),
      (party_set_slot,"p_castle_38", "slot_center_siege_with_ram",      0),
      (party_set_slot,"p_castle_42", "slot_center_siege_with_ram",      1),
      (party_set_slot,"p_town_30", "slot_center_siege_with_ram",      0),
      (party_set_slot,"p_town_36", "slot_center_siege_with_ram",      0),
      (party_set_slot,"p_town_40", "slot_center_siege_with_ram",      0),
      (party_set_slot,"p_town_32", "slot_center_siege_with_belfry", 0),
      (party_set_slot,"p_town_27", "slot_center_siege_with_belfry", 0),
      (party_set_slot,"p_town_13", "slot_center_siege_with_belfry", 0),

          (assign, "$g_savegames_necesario", 1),    


		#(eq, "$g_sod_faith", 0),                                                        
##   (try_begin),
##(assign, "$g_sod_faith", 1),           
##(assign, "$g_pueblos_religion", 0),
##(assign, "$g_sod_global_faith", 0),
##      (party_set_slot,"p_town_8","slot_center_religion_pagan", 1),                 ##Set grantebrydge como pagana
##      (party_set_slot,"p_town_11","slot_center_religion_pagan", 1),                 ##Set Aegelesburh como pagana
##      (party_set_slot,"p_town_18","slot_center_religion_pagan", 1),                 ##Set Searoburh como pagana
##      (party_set_slot,"p_town_23","slot_center_religion_pagan", 1),                 ##Set Licidfelth como pagana
##      (party_set_slot,"p_town_24","slot_center_religion_pagan", 1),                 ##Set Linnuis como pagana
##
##      (party_set_slot,"p_village_1","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_2","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_4","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_8","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_10","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_14","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_74","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_51","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_16","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_41","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_49","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_12","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_21","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_76","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_87","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_75","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_38","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_88","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_89","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_44","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_93","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_52","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_98","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_17","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_48","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_36","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_67","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_103","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_129","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_122","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_55","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_54","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_124","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_42","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_90","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_91","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_151","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_95","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_99","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_20","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_3","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_28","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_47","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##      (party_set_slot,"p_village_46","slot_center_religion_pagan", 1),                 ##Set aldea como pagana
##
##
####	(try_for_range, ":center_no", centers_begin, centers_end),
####		(neg|party_slot_eq, ":center_no", "slot_party_type", spt_castle),
####		(store_random_in_range, ":rand", -50, 50),	
####		(party_set_slot, ":center_no", "slot_center_sod_local_faith", ":rand"),
####	(try_end),
###gente cristiana
##	(try_for_range, ":center_no", centers_begin, centers_end),
##        (neg|party_slot_ge, ":center_no", "slot_center_religion_pagan", 1), #skip villages which are pagan.
##		(neg|party_slot_eq, ":center_no", "slot_party_type", spt_castle),
##		(assign, "$g_pueblos_religion", 4),	
##		(store_random_in_range, ":rand", 30, 90),	
##		(party_set_slot, ":center_no", "slot_center_sod_local_faith", ":rand"),
##	(try_end),
##	(try_for_range, ":center_no", centers_begin, centers_end),
##		(neg|party_slot_eq, ":center_no", "slot_party_type", spt_castle),
##        (party_slot_eq, ":center_no", "slot_center_religion_pagan", 1), #anade fe a paganos
##		(store_random_in_range, ":rand", -90, -30),	
##		(party_set_slot, ":center_no", "slot_center_sod_local_faith", ":rand"),
##	(try_end),
##	(try_end),
#chief acaba sod
	]),  
###Local Faith decreases slowly when not maintained
##(24 * 7,
##	[
##	
##	(try_for_range, ":center_no", centers_begin, centers_end),
##		(party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
##		(party_get_slot, ":cur_faith", ":center_no", "slot_center_sod_local_faith"),
##		(val_sub, ":cur_faith", 2),
##			(try_begin),
##				(gt, ":cur_faith", 100),
##				(assign, ":cur_faith", 100),
##			(else_try),
##				(lt, ":cur_faith", -100),
##				(assign, ":cur_faith", -100),
##			(try_end),
##		(party_set_slot, ":center_no", "slot_center_sod_local_faith", ":cur_faith"),
##		# DEBUG REMOVE ME
##		(display_message, "@FAITH RELATION: if a center have diferent religion to you, you lose relation."),
##	(try_end),	
##	]),  
#invierno baja moral y otras cosas chief
(24 * 7,
	[
          (this_or_next|eq, "$g_cur_month", 12),
          (this_or_next|eq, "$g_cur_month", 1),
          (eq, "$g_cur_month", 2),
	    (neq, "$freelancer_state", 1),	#+freelancer chief

		(call_script, "script_change_troop_renown", "trp_player", -3),
         	   (call_script, "script_change_player_party_morale", -5),
		(display_message, "@Winter is the worst time for war. It's cold, it rains too much and food is scarce. In winter, men would rather be sheltered from the fire that campaign. Watch your moral and your food stocks."),
	]),  
#invierno penaltie chief


  #ramdon events chief
  ## Abhuva Random Events
   #---BEGIN LYX RANDOM EVENTS---
(24 * 7,[   # interval currently set to 6 hours for testing  - should be 14 * 24 for normal play, 1 * 6 for testing

   # Init
   # ---------------------------------------------------------------------------
#   (eq,"$random_events",1), ## abhuva, 1 = use random events, 0 = dont use them
   ##   (display_message, "@_Random Events Trigger fired.", 0xFF8000),  ## for bugfix
(neq,"$g_camp_mode", 1),
(neq, "$g_empieza_asedio", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_icon_state", pis_ship),
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief

            (neq, "$g_player_is_captive", 1),
       (assign, ":total_events", 11),   # update this when adding/removing events!
   (val_add, ":total_events", 1),   # MnB has weird ideas of ranges
   (store_random_in_range, ":curr_event", 0, ":total_events"),
   (neq, ":curr_event", "$g_lyx_last_random_event"),   # ignore event if same as last
   (assign, "$g_lyx_last_random_event", ":curr_event"),
   (assign, ":pos", 0),
   (try_begin), (eq,1,2),   # dummy


   # Events
   # ---------------------------------------------------------------------------

   # --- PLAYER INJURED --- 15
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
#      (call_script, "script_get_troop_health", "trp_player"), (ge,reg0,60),   # abort if player is already weak
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@During today's training, you were accidently injured. While the wounds aren't severe, it may take some time for them to heal."),
      (else_try),
           (dialog_box, "@During today's training, you were accidently injured. While the wounds aren't severe, it may take some time for them to heal.", "@Training accident:"),
     (try_end),
     (call_script, "script_change_troop_health", "trp_player", -20),
  
   # --- PLAYER INJURED --- 16
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
#      (call_script, "script_get_troop_health", "trp_player"), (ge,reg0,60),   # abort if player is already weak
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@Today, you awoke with a horrible toothache and now you can no longer hide the pain."),
      (else_try),
           (dialog_box, "@Today, you awoke with a horrible toothache and now you can no longer hide the pain.", "@Toothache:"),
     (try_end),
     (call_script, "script_change_troop_health", "trp_player", -5),

  # --- PLAYER INJURED --- 17
  (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
#      (call_script, "script_get_troop_health", "trp_player"), (ge,reg0,60),   # abort if player is already weak
     (try_begin),
#       (eq,"$random_events_box",0),
      (display_message, "@You slipped on wet ground, and you were injured."),
     (else_try),
          (dialog_box, "@You slipped on wet ground, and you were injured.", "@Injured."),
    (try_end),
    (call_script, "script_change_troop_health", "trp_player", -5),

   # --- PLAYER INJURED --- 18
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
#      (call_script, "script_get_troop_health", "trp_player"), (ge,reg0,60),   # abort if player is already weak
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@(While traveling) You happen to find an abandoned house. You found some loot."),
      (else_try),
           (dialog_box, "@(While traveling) You happen to find an abandoned house. You found some loot.", "@Abandoned house."),
     (try_end),
     (troop_add_gold, "trp_player", 50),
	(troop_add_item, "trp_player", "itm_spear_hvy", 0), #chief cambiado premio por eliminar al borracho
	(troop_add_item, "trp_player", "itm_smoked_fish", 0), #chief cambiado premio por eliminar al borracho


   # --- PLAYER strong ---19
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
#      (call_script, "script_get_troop_health", "trp_player"), (ge,reg0,60),   # abort if player is already weak
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@The adventure, life in the field, the constant training makes you feel strong and well, you are ready to face any challenge."),
      (else_try),
      (dialog_box, "@The adventure, life in the field, the constant training makes you feel strong and well, you are ready to face any challenge.", "@Heal improved:"),
     (try_end),
      (call_script, "script_change_troop_health", "trp_player", 40),

   # --- GOLD FOUND --- 20
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@Today you got lucky and found a small bag hidden behind a bush. Inside the bag was 300 scillingas."),
      (else_try),
          (dialog_box, "@Today you got lucky and found a small bag hidden behind a bush. Inside the bag was 300 scillingas.", "@Found Gold bag:"),
     (try_end),
     (troop_add_gold, "trp_player", 300),

  # --- WORTHLESS METAL FOUND --- 21
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@During a small rest you noticed a shiney object in the ground caught your eye. You tooked a closer look, thinking it may be some scillingas. Unfortunately it was only a small piece of rusted metal lying on the ground, totally worthless."),
       (else_try),
           (dialog_box, "@During a small rest you noticed a shiney object in the ground caught your eye. You tooked a closer look, thinking it may be some scillingas. Unfortunately it was only a small piece of rusted metal lying on the ground, totally worthless.", "@Found some crap:"),
      (try_end),

  # --- Reservas de agua contaminadas --- 22
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@The water reserves have been contaminated and it must be rationed until you reach the next town."),
       (else_try),
           (dialog_box, "@The water reserves have been contaminated and it must be rationed until you reach the next town.", "@Water Reserves contaminated."),
      (try_end),
     (call_script, "script_change_troop_health", "trp_player", -15),
     (call_script, "script_change_player_party_morale", -15),
   
  # --- Encuentra cargamento de hidromiel --- 23
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@You and your party have come across an abandoned wagon of full of mead, and you gift it to your men."),
       (else_try),
           (dialog_box, "@You and your party have come across an abandoned wagon of full of mead, and you gift it to your men.", "@Wagon of Mead."),
      (try_end),
     (call_script, "script_change_player_party_morale", 10),
      
  # --- leales regalan a la party del heroe --- 24
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@Loyalist supporters from a nearby village have gathered a bounty of food for your troops."),
       (else_try),
           (dialog_box, "@Loyalist supporters from a nearby village have gathered a bounty of food for your troops.", "@Bounty of food."),
      (try_end),
     (call_script, "script_change_player_party_morale", 10),

## # --- PLAYER INJURED/GOLD LOSS --- 25  needs editing
##   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
##      (call_script, "script_get_troop_health", "trp_player"), (ge,reg0,40),   # abort if player is already weak
##      #(call_script, "script_get_player_gold", "trp_player"), (ge, reg0, 120), # abort if too less money left on player
##      (try_begin),
##       (eq,"$random_events_box",0),
##       (display_message, "@Today you were injured by stumbling across a hidden stone. Your wounds are minor but later you discovered that you have lossed a bag of denar during the incident. DEBUG MESSAGE: Needs editing"),
##      (else_try),
##             (dialog_box, "@Today you were injured by stumbling across a hidden stone. Your wounds are minor but later you discovered that you have lossed a bag of denar during the incident.", "@Minor accident:"),
##     (try_end),
##     (call_script, "script_change_troop_health", "trp_player", -25),
##     #(troop_add_gold, "trp_player", -120),

#Griggs additional events
  # --- BATTLE LEFTOVERS --- 25  
   (else_try),   (val_add,":pos",1), (eq,":pos",":curr_event"),   # this first line is same for all events
      (try_begin),
#       (eq,"$random_events_box",0),
       (display_message, "@You have found leftovers of a recent battle. Searching the bodies, you managed to find 200 scillingas."),
      (else_try),
             (dialog_box, "@You have found leftovers of a recent battle. Searching the bodies, you managed to find 200 scillingas.", "@Minor accident:"),
     (try_end),
     (troop_add_gold, "trp_player", 200),
#Griggs additional events end
     # Closing
   # --------------------------------------
   ## ideas for future events: morale of troops +/-, adding inventory items (food, maybe armour etc with smaller chance)
   (try_end),
] ),
#---END LYX RANDOM EVENTS---
## Abhuva Random Events ends chief acaba
      #x############################################
# EVENTS WITHOUT PREQUISITES ARE SPAWNED BY THIS TRIGGER 
#x############################################

(194,
	[
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_empieza_asedio", 1),
(neq, "$g_player_icon_state", pis_ship),
(neq, "$g_player_is_captive", 1),
(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
        (troop_get_slot, ":player_renown", "trp_player", "slot_troop_renown"),
        (gt, ":player_renown", 270),
          (store_random_in_range, ":rand", 0, 13),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_01"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_23"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_24"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_26"),
                                          (else_try),
                                            (eq, ":rand", 4),
                        (jump_to_menu,"mnu_event_02"),
                                           (else_try),
                                            (eq, ":rand", 5),
                        (jump_to_menu,"mnu_event_03"),
                                          (else_try),
                                            (eq, ":rand", 6),
                        (jump_to_menu,"mnu_event_05"),
                                          (else_try),
                                            (eq, ":rand", 7),
                        (jump_to_menu,"mnu_event_07"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

(310,
	[
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_empieza_asedio", 1),
(neq, "$g_player_icon_state", pis_ship),
(neq, "$g_player_is_captive", 1),
(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
        (troop_get_slot, ":player_renown", "trp_player", "slot_troop_renown"),
        (gt, ":player_renown", 140),
          (store_random_in_range, ":rand", 0, 15),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_04"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_11"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_27"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_28"),
                                          (else_try),
                                            (eq, ":rand", 4),
                        (jump_to_menu,"mnu_event_12"),
                                           (else_try),
                                            (eq, ":rand", 5),
                        (jump_to_menu,"mnu_event_13"),
                                          (else_try),
                                            (eq, ":rand", 6),
                        (jump_to_menu,"mnu_event_14"),
                                          (else_try),
                                            (eq, ":rand", 7),
                        (jump_to_menu,"mnu_event_101"),
                                          (else_try),
                                            (eq, ":rand", 8),
                        (jump_to_menu,"mnu_event_102"),
                                          (else_try),
                                            (eq, ":rand", 9),
                        (jump_to_menu,"mnu_event_103"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

(284,
	[
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_is_captive", 1),
(neq, "$g_empieza_asedio", 1),
(neq, "$g_player_icon_state", pis_ship),
(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
        (troop_get_slot, ":player_renown", "trp_player", "slot_troop_renown"),
        (gt, ":player_renown", 300),
          (store_random_in_range, ":rand", 0, 12),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_29"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_30"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_31"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_36"),
                                          (else_try),
                                            (eq, ":rand", 4),
			(jump_to_menu,"mnu_event_37"),
                                           (else_try),
                                            (eq, ":rand", 5),
			(jump_to_menu,"mnu_event_32"),
                                          (else_try),
                                            (eq, ":rand", 6),
			(jump_to_menu,"mnu_event_33"),
                                          (else_try),
                                            (eq, ":rand", 7),
			(jump_to_menu,"mnu_event_34"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

    (260,
	[

         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
   (assign, ":has_fief1", 0),
    (try_for_range, ":center_no", centers_begin, centers_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", "slot_town_lord"),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief1", 1),
    (try_end),
    (eq, ":has_fief1", 1),

(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_is_captive", 1),
(neq, "$g_empieza_asedio", 1),
(neq, "$g_player_icon_state", pis_ship),
	(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
        (troop_get_slot, ":player_renown", "trp_player", "slot_troop_renown"),
        (gt, ":player_renown", 140),
          (store_random_in_range, ":rand", 0, 10),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_06"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_08"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_18"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_19"),
                                          (else_try),
                                            (eq, ":rand", 4),
			(jump_to_menu,"mnu_event_22"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

(224,
	[
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_is_captive", 1),
(neq, "$g_empieza_asedio", 1),
(neq, "$g_player_icon_state", pis_ship),
(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
        (troop_get_slot, ":player_renown", "trp_player", "slot_troop_renown"),
        (gt, ":player_renown", 220),
          (store_random_in_range, ":rand", 0, 12),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_35"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_37"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_38"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_39"),
                                          (else_try),
                                            (eq, ":rand", 4),
			(jump_to_menu,"mnu_event_40"),
                                           (else_try),
                                            (eq, ":rand", 5),
			(jump_to_menu,"mnu_event_42"),
                                          (else_try),
                                            (eq, ":rand", 6),
			(jump_to_menu,"mnu_event_41"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

  (170,
	[
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_player_is_captive", 1),
(neq, "$g_empieza_asedio", 1),
(neq, "$g_player_icon_state", pis_ship),
	(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
          (store_random_in_range, ":rand", 0, 13),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_10"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_09"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_25"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_15"),
                                          (else_try),
                                            (eq, ":rand", 4),
			(jump_to_menu,"mnu_event_16"),
                                           (else_try),
                                            (eq, ":rand", 5),
			(jump_to_menu,"mnu_event_20"),
                                          (else_try),
                                            (eq, ":rand", 6),
			(jump_to_menu,"mnu_event_21"),
                                          (else_try),
                                            (eq, ":rand", 7),
			(jump_to_menu,"mnu_event_17"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

  #chief eventos de king rey
  (315,
	[
   (assign, ":has_fief1", 0),
    (try_for_range, ":center_no", towns_begin, towns_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", "slot_town_lord"),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief1", 1),
    (try_end),
    (eq, ":has_fief1", 1),
(neq,"$g_camp_mode", 1),
(neq, "$g_town_visit_after_rest", 1),
(neq, "$g_empieza_asedio", 1),
(neq, "$g_player_icon_state", pis_ship),
(neq, "$g_player_is_captive", 1),
(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
        (troop_get_slot, ":player_renown", "trp_player", "slot_troop_renown"),
        (gt, ":player_renown", 180),
                                          (try_begin),
                                            (eq, "$g_juicio", 0), 
			(jump_to_menu,"mnu_event_01_juicio"),
                                            (assign, "$g_juicio", 1), 
                                          (else_try),
                                            (eq, "$g_juicio", 1), 
			(jump_to_menu,"mnu_event_02_juicio"),
                                            (assign, "$g_juicio", 2), 
                                          (else_try),
                                            (eq, "$g_juicio", 2), 
			(jump_to_menu,"mnu_event_03_juicio"),
                                            (assign, "$g_juicio", 3), 
                                          (else_try),
                                            (eq, "$g_juicio", 3), 
			(jump_to_menu,"mnu_event_04_juicio"),
                                            (assign, "$g_juicio", 4), 
                                          (else_try),
                                            (eq, "$g_juicio", 4), 
			(jump_to_menu,"mnu_event_06_juicio"),
                                            (assign, "$g_juicio", 5), 
                                           (else_try),
                                            (eq, "$g_juicio", 5), 
			(jump_to_menu,"mnu_event_07_juicio"),
                                            (assign, "$g_juicio", 6), 
                                          (else_try),
                                            (eq, "$g_juicio", 6), 
			(jump_to_menu,"mnu_event_08_juicio"),
                                            (assign, "$g_juicio", 7), 
                                          (else_try),
                                            (eq, "$g_juicio", 7), 
			(jump_to_menu,"mnu_event_09_juicio"),
                                            (assign, "$g_juicio", 8), 
                                          (else_try),
                                            (eq, "$g_juicio", 8), 
			(jump_to_menu,"mnu_event_11_juicio"),
                                            (assign, "$g_juicio", 9), 
                                          (else_try),
                                            (eq, "$g_juicio", 9), 
			(jump_to_menu,"mnu_event_12_juicio"),
                                            (assign, "$g_juicio", 10), 
                                          (else_try),
                                            (eq, "$g_juicio", 10), 
			(jump_to_menu,"mnu_event_13_juicio"),
                                            (assign, "$g_juicio", 11), 
                                          (else_try),
                                            (eq, "$g_juicio", 11), 
			(jump_to_menu,"mnu_event_14_juicio"),
                                            (assign, "$g_juicio", 12), 
                                           (else_try),
                                            (eq, "$g_juicio", 12), 
			(jump_to_menu,"mnu_event_15_juicio"),
                                            (assign, "$g_juicio", 13), 
                                          (else_try),
                                            (eq, "$g_juicio", 13), 
			(jump_to_menu,"mnu_event_16_juicio"),
                                            (assign, "$g_juicio", 14), 
                                          (else_try),
                                            (eq, "$g_juicio", 14), 
			(jump_to_menu,"mnu_event_17_juicio"),
                                            (assign, "$g_juicio", 15), 
                                          (else_try),
                                            (eq, "$g_juicio", 15), 
			(jump_to_menu,"mnu_event_18_juicio"),
                                            (assign, "$g_juicio", 16), 
                                          (else_try),
                                            (eq, "$g_juicio", 16), 
			(jump_to_menu,"mnu_event_19_juicio"),
                                            (assign, "$g_juicio", 17), 
                                          (else_try),
                                            (eq, "$g_juicio", 17), 
			(jump_to_menu,"mnu_event_20_juicio"),
                                            (assign, "$g_juicio", 18), 
                                          (else_try),
                                            (eq, "$g_juicio", 18), 
			(jump_to_menu,"mnu_event_21_juicio"),
                                            (assign, "$g_juicio", 19), 
                                           (else_try),
                                            (eq, "$g_juicio", 19), 
			(jump_to_menu,"mnu_event_22_juicio"),
                                            (assign, "$g_juicio", 20), 
                                          (else_try),
                                            (eq, "$g_juicio", 20), 
			(jump_to_menu,"mnu_event_23_juicio"),
                                            (assign, "$g_juicio", 21), 
                                          (else_try),
                                            (eq, "$g_juicio", 21), 
			(jump_to_menu,"mnu_event_24_juicio"),
                                            (assign, "$g_juicio", 22), 
                                          (else_try),
                                            (eq, "$g_juicio", 22), 
			(jump_to_menu,"mnu_event_05_juicio"),
                                            (assign, "$g_juicio", 23), 
                                          (else_try),
                                            (eq, "$g_juicio", 23), 
			(jump_to_menu,"mnu_event_10_juicio"),
                                            (assign, "$g_juicio", 24), 
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

  
###chief finalizado#####
#script of moral motomataru chief
 (2, [    #morale impact of resting/not resting by motomataru
         (neq, "$freelancer_state", 1), #+freelancer chief #brytenwalda chief
 (neq, "$g_morale_rest", 0),

 (store_party_size_wo_prisoners, reg0, "p_main_party"),
 (try_begin),
     (lt, reg0, 2),
     (party_set_slot, "p_main_party", "slot_party_unrested_morale_penalty", 0),
 (else_try),
     (is_currently_night),
     (try_begin),
         (eq, "$g_last_rest_center", "$current_town"),
         (assign, "$rest_up", 1),##jump to elsetry
     (else_try),
         (neq, "$g_player_icon_state", pis_camping),
         (neq, "$g_player_icon_state", pis_ship),
         (neq, "$g_player_besiege_town", "$g_encountered_party"),
         (neq, "$g_player_is_captive", 1),
         (party_get_slot, reg0, "p_main_party", "slot_party_unrested_morale_penalty"),##get last morale penalty
         (val_add, reg0, 3),##gdw was 1
         (party_set_slot, "p_main_party", "slot_party_unrested_morale_penalty", reg0),
         (display_message, "@Your troops lose 3 morale from no night rest. morale_modifier_weariness={reg0}."),
         #(assign, ":lose_morale", reg0),
         #(call_script, "script_change_player_party_morale", -3),
     (try_end),
 (else_try),
     (neq, "$rest_up", 0),##means rested in town
     (party_get_slot, reg0, "p_main_party", "slot_party_unrested_morale_penalty"),
     
     #(try_begin),##if 4 and up, don't assign further penalty gdw
     (assign, reg1, 6),
     (try_begin),##does this apply only to state where in town or in camp
       (ge, "$g_last_rest_center", 0),
       (party_slot_eq, "$g_last_rest_center", "slot_party_type", spt_town),
       (val_add, reg1, 2),##gdw this was 1
     (try_end),
     (val_sub, reg0, reg1),
     (party_set_slot, "p_main_party", "slot_party_unrested_morale_penalty", reg0),
     #(call_script, "script_change_player_party_morale", reg1),
     #(try_end),
     (display_message, "@Your troops feel refreshed from the center rest 8. morale_modifier_weariness={reg0}"),
     (assign, "$rest_up", 0),
  (else_try),##camping?
     (is_currently_night),
     (party_get_slot, reg0, "p_main_party", "slot_party_unrested_morale_penalty"),
     (val_sub, reg0, 4),#camp less restful
     # (val_max, reg0,0),
     (party_set_slot, "p_main_party", "slot_party_unrested_morale_penalty", reg0),
     #(call_script, "script_change_player_party_morale", 4),
     (display_message, "@Your troops troops gain morale from night rest. morale_modifier_weariness={reg0}."),
  (else_try),##day resting
     (eq, "$g_player_icon_state", pis_camping),
     (party_get_slot, reg0, "p_main_party", "slot_party_unrested_morale_penalty"),
     #(val_max, reg0,0),##test gdw delte this
     (val_sub, reg0, 2),#camp less restful
     # (val_max, reg0,0),
     (party_set_slot, "p_main_party", "slot_party_unrested_morale_penalty", reg0),
     (display_message, "@Your troops troops gain morale from day rest. morale_modifier_weariness={reg0}."),
     #(call_script, "script_change_player_party_morale", 2),
  (else_try),
      (eq, "$g_battle_weary",1),
      (party_get_slot, reg0, "p_main_party", "slot_party_unrested_morale_penalty"),
     #(val_max, reg0,0),##test gdw delte this
      (val_sub, reg0, 9),#camp less restful
     # (val_max, reg0,0),
      (party_set_slot, "p_main_party", "slot_party_unrested_morale_penalty", reg0),
      (assign, "$g_battle_weary",0),
  (else_try),
      (party_get_slot, reg0, "p_main_party", "slot_party_unrested_morale_penalty"),
      (try_begin),
      (eq, "$cheat_mode", 1),
      (display_message, "@end of script morale_modifier_weariness={reg0}"),
      (try_end),
  (try_end),

 (try_begin),##gdw new script
    (party_get_slot, reg0, "p_main_party", "slot_party_unrested_morale_penalty"),
    (gt, reg0,46),
    (assign, "$g_encumbrance_penalty", 3),
    (display_message, "@encumbrancelevel 3 fromnorest."),
 (else_try),
    (party_get_slot, reg0, "p_main_party", "slot_party_unrested_morale_penalty"),
    (le, reg0,46),
    (gt, reg0,20),
    (assign, "$g_encumbrance_penalty", 2),
    (try_begin),
    (eq, "$cheat_mode", 1),
    (display_message, "@encumbrancelevel 2 fromlittlerest."),
    (try_end),
 (else_try),

    (party_get_slot, reg0, "p_main_party", "slot_party_unrested_morale_penalty"),
    (le, reg0,20),
    #(le, reg0,18),
    (assign, "$g_encumbrance_penalty", 1),
    (try_begin),
    (eq, "$cheat_mode", 1),
    (display_message, "@encumbrancelevel 1 fromOKrest."),
    (try_end),
    (try_end),
 ]),
 

  
##mejor IA chief para seguir al marshal o player y que los lores no se largen a la primera de Rubik
    (1,
    [
      (try_for_parties, ":party_no"),
        (party_slot_eq, ":party_no", "slot_party_type", spt_kingdom_hero_party),
        (store_faction_of_party, ":party_faction", ":party_no"),
        (try_begin), ## follow
          (party_slot_eq, ":party_no", "slot_party_ai_state", spai_accompanying_army),
          (party_get_slot, ":dest_ai_party", ":party_no", "slot_party_ai_object"),
          (gt, ":dest_ai_party", -1),
          (party_is_active, ":dest_ai_party"),
          (try_begin), # skip player's party
            (eq, ":dest_ai_party", "p_main_party"),
          (else_try),
            (party_set_slot, ":party_no", "slot_party_blind_to_other_parties", 1),
            (try_begin),
              (party_get_battle_opponent, ":opponent_party", ":dest_ai_party"),
              (store_distance_to_party_from_party, ":dist", ":party_no", ":dest_ai_party"),
              (gt, ":opponent_party", -1),
              (le, ":dist", 5),
              (party_set_slot, ":party_no", "slot_party_blind_to_other_parties", 0),
            (try_end),
          (try_end),
        (else_try), ## besiege
          (party_slot_eq, ":party_no", "slot_party_ai_state", spai_besieging_center),
          (party_get_slot, ":ai_object", ":party_no", "slot_party_ai_object"),
          (gt, ":ai_object", -1),
          (party_set_slot, ":party_no", "slot_party_blind_to_other_parties", 1),
          (try_for_parties, ":party_no_2"),
            (neq, ":party_no_2", ":party_no"),
            (store_distance_to_party_from_party, ":dist_2", ":party_no", ":party_no_2"),
            (le, ":dist_2", 5),
            (party_slot_eq, ":party_no_2", "slot_party_type", spt_kingdom_hero_party),
            (store_faction_of_party, ":party_faction_2", ":party_no_2"),
            (eq, ":party_faction_2", ":party_faction"),
            (party_get_battle_opponent, ":opponent_party_2", ":party_no_2"),
            (gt, ":opponent_party_2", -1),
            (party_set_slot, ":party_no", "slot_party_blind_to_other_parties", 0),
          (try_end),
        (else_try),
          (party_set_slot, ":party_no", "slot_party_blind_to_other_parties", 0),
        (try_end),
      (try_end),
    ]),

    # todo: This block was missing a "try_end" and therefore is probably incorrect.
    # script to start a rebelion
    # On average, over 100 days, every defeated faction considers rebellion once.
    (24*3, [
        (store_skill_level, ":skill", "skl_leadership", "trp_player"),
        (store_attribute_level, ":charisma", "trp_player", ca_charisma),
        (try_begin),
            (this_or_next|ge, ":skill", 6),
            (ge, ":charisma", 18),
            (display_message, "@ The defeated kingdoms seem calm, and your "
                              "reports confirm that there are no rebellion "
                              "plots.", 0xFF0000),
        (else_try),

            (ge, ":skill", 1),
            (ge, ":charisma", 1),
            (try_for_range, ":cur_troop", kingdom_heroes_begin2, kingdom_heroes_end2),
                (troop_slot_eq, ":cur_troop", "slot_troop_occupation", slto_kingdom_hero),
                (troop_get_slot, ":original_faction", ":cur_troop", "slot_troop_original_faction"),
                (neg|faction_slot_eq, ":original_faction", "slot_faction_state", sfs_active),
                (store_relation, ":rebelde_reln", ":original_faction", "fac_player_supporters_faction"),

                (store_troop_faction, ":faction_no", ":cur_troop"),
                (neq, ":faction_no", ":original_faction"),

                # check if it has a walled center
                (assign, ":num_walled_centers", 0),
                (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
                    (party_slot_eq, ":walled_center", "slot_town_lord", ":cur_troop"),
                    (val_add, ":num_walled_centers", 1),
                (try_end),
                (gt, ":num_walled_centers", 0),

                (store_sub, ":original_king", ":original_faction", "fac_kingdom_1"),
                (val_add, ":original_king", "trp_kingdom_1_lord"),
                (faction_set_slot, ":original_faction", "slot_faction_leader", ":original_king"),

                (str_store_troop_name, s14, ":original_king"),
                (store_random_in_range, ":rand", 0, 33*5),

                (try_begin),
                    (eq, ":rand", 0),
                    (display_message, "@(Possible Rebellion) Rumors say that {s14} is still alive.", 0xFF0000),
                (else_try),
                    (eq, ":rand", 1),
                    (display_message, "@(Possible Rebellion) Rumors say that {s14} meets in secret with his faithful.", 0xFF0000),
                (else_try),
                    (eq, ":rand", 2),
                    (display_message, "@(Possible Rebellion) Rumors say that people favor the restoration of {s14}.", 0xFF0000),
                (else_try),
                    (eq, ":rand", 3),
                    (display_message, "@(Possible Rebellion) Rumors say that {s14} is gathering an army to regain his throne.", 0xFF0000),
                (else_try),
                    (eq, ":rand", 4),
                    (try_begin),
                        (lt, ":rebelde_reln", 10),

                        (call_script, "script_change_troop_faction", ":cur_troop", ":original_faction"),
                        (try_for_range, ":cur_troop_2", kingdom_heroes_begin2, kingdom_heroes_end2),
                            (troop_slot_eq, ":cur_troop_2", "slot_troop_occupation", slto_kingdom_hero),
                            (neg|is_between, ":cur_troop_2", pretenders_begin, pretenders_end),
                            (neq, ":cur_troop_2", ":cur_troop"),
                            (troop_get_slot, ":original_faction_2", ":cur_troop_2", "slot_troop_original_faction"),
                            (store_troop_faction, ":faction_no_2", ":cur_troop_2"),
                            (eq, ":original_faction_2", ":original_faction"),
                            (neq, ":faction_no_2", ":original_faction"),
                            (troop_set_slot, ":cur_troop_2", "slot_troop_change_to_faction", ":original_faction"),
                        (try_end),
                        (call_script, "script_add_notification_menu", "mnu_notification_kingdom_restoration", ":cur_troop", ":faction_no"),
                    (else_try),
                        (display_message, "@(Possible Rebellion) Rumors say that {s14} is stockpiling weapons and is seeking support among the Franks.", 0xFF0000),
                    (try_end),
                (try_end),
            (try_end),
        (try_end),
       ]),

  #algo del tema de vender prisioneros por ciudades chief commander CC
  ####siege warfare, player pierde dinero durante un asedio por gastos varios y diariamente. Los asedios eran muy caros.
    (24,
   [
(eq, "$g_empieza_asedio", 1),
       (store_troop_gold,":money","trp_player"),
      (try_begin),
        (gt,":money",99),
       (troop_remove_gold, "trp_player", 100),
      (call_script, "script_change_player_party_morale", -1),
        (display_message,"@(Expenditure siege) Each day of the siege you need to cover a number of expenses: as rewards for people or digging latrines, cleaning stables, buying and bringing water and food, cooking, entertaining the troops...", 0xFF0000),
      (else_try),
      (call_script, "script_change_player_party_morale", -5),
        (display_message,"@ You do not have money to cover the basic expenses of the siege. This greatly undermines morale.", 0xFF0000),
      (try_end),
   ]),
  
###random events siege
#raciones#Trigger-line154?
  (60,
	[
(eq, "$g_empieza_asedio", 1),
           (neq, "$g_siege_saneamiento", 1),
(neq, "$g_player_is_captive", 1),
(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
      (val_add, ":num_men", ":stack_size"),
    (try_end),
	(gt, ":num_men", 19),
          (store_random_in_range, ":rand", 0, 12),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_siege_01"),
                                          (else_try),
                                            (eq, ":rand", 1),
			(jump_to_menu,"mnu_event_siege_02"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_siege_03"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

#eventos de guerrilla e infiltracion
    (68,
	[
(eq, "$g_empieza_asedio", 1),
(neq, "$g_player_is_captive", 1),
(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
      (val_add, ":num_men", ":stack_size"),
    (try_end),
	(gt, ":num_men", 10),
          (store_random_in_range, ":rand", 0, 15),
                                          (try_begin),
                                            (eq, ":rand", 0), 
                                (eq, "$g_enemigo_quema_comida", 0),
                           (neq, "$g_siege_circunvalation", 2),
			(jump_to_menu,"mnu_event_siege_04"),
                                          (else_try),
                                            (eq, ":rand", 1),
                      (eq, "$g_siege_circunvalation", 2),
                       (jump_to_menu,"mnu_event_siege_05"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_siege_06"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_siege_07"),
                                          (else_try),
                                            (eq, ":rand", 4),
			(jump_to_menu,"mnu_event_siege_08"),
                                          (else_try),
                                            (eq, ":rand", 5),
			(jump_to_menu,"mnu_event_siege_09"),
                                          (else_try),
                                            (eq, ":rand", 6),
			(jump_to_menu,"mnu_event_siege_10"),
                                          (else_try),
                                            (eq, ":rand", 7),
			(jump_to_menu,"mnu_event_siege_12"),
                                          (else_try),
                                            (eq, ":rand", 8),
			(jump_to_menu,"mnu_event_siege_18"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),
#invierno
    (24,
	[
(eq, "$g_empieza_asedio", 1),
(neq, "$g_player_is_captive", 1),
          (this_or_next|eq, "$g_cur_month", 12),
          (this_or_next|eq, "$g_cur_month", 1),
          (eq, "$g_cur_month", 2),
(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
      (val_add, ":num_men", ":stack_size"),
    (try_end),
	(gt, ":num_men", 10),
          (store_random_in_range, ":rand", 0, 1),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_siege_11"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),
#salidas, asaltos y respuestas
    (96,
	[
(eq, "$g_empieza_asedio", 1),
(neq, "$g_player_is_captive", 1),
(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
      (val_add, ":num_men", ":stack_size"),
    (try_end),
	(gt, ":num_men", 20),
          (store_random_in_range, ":rand", 0, 6),
                                          (try_begin),
                                            (eq, ":rand", 0), 
                           (neq, "$g_siege_circunvalation", 2),
			(jump_to_menu,"mnu_event_siege_13"),
                                          (else_try),
                                            (eq, ":rand", 1),
                           (neq, "$g_siege_circunvalation", 2),
                       (jump_to_menu,"mnu_event_siege_14"),
                                          (else_try),
                                            (eq, ":rand", 2),
                           (neq, "$g_siege_circunvalation", 2),
			(jump_to_menu,"mnu_event_siege_15"),
                                          (else_try),
                                            (eq, ":rand", 3),
                           (neq, "$g_siege_circunvalation", 2),
			(jump_to_menu,"mnu_event_siege_16"),
                                          (else_try),
                                            (eq, ":rand", 4),
                           (neq, "$g_siege_circunvalation", 2),
			(jump_to_menu,"mnu_event_siege_17"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),
#atacando defensores circunvallation and equipamiento de asalto
    (96,
	[
(eq, "$g_empieza_asedio", 1),
(neq, "$g_player_is_captive", 1),
(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
      (val_add, ":num_men", ":stack_size"),
    (try_end),
	(gt, ":num_men", 10),
          (store_random_in_range, ":rand", 0, 2),
                                          (try_begin),
                                            (eq, ":rand", 0), 
         (neq, "$g_siege_circunvalation", 0),
			(jump_to_menu,"mnu_event_siege_19"),
                                          (else_try),
                                            (eq, ":rand", 1), 
         (neq, "$g_siege_method", 0),
			(jump_to_menu,"mnu_event_siege_20"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

  #sucesos duante circunvallation
      (104,
	[
(eq, "$g_empieza_asedio", 1),
 (eq, "$g_siege_circunvalation", 2),
(neq, "$g_player_is_captive", 1),
(neg|troop_slot_ge, "trp_player", "slot_troop_prisoner_of_party", 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
      (val_add, ":num_men", ":stack_size"),
    (try_end),
	(gt, ":num_men", 150),
          (store_random_in_range, ":rand", 0, 10),
                                          (try_begin),
                                            (eq, ":rand", 0), 
			(jump_to_menu,"mnu_event_siege_21"),
                                          (else_try),
                                            (eq, ":rand", 1),
                       (jump_to_menu,"mnu_event_siege_22"),
                                          (else_try),
                                            (eq, ":rand", 2),
			(jump_to_menu,"mnu_event_siege_23"),
                                          (else_try),
                                            (eq, ":rand", 3),
			(jump_to_menu,"mnu_event_siege_24"),
                                          (else_try),
                                            (eq, ":rand", 4),
			(jump_to_menu,"mnu_event_siege_25"),
                                          (else_try),
                                            (eq, ":rand", 5),
			(jump_to_menu,"mnu_event_siege_26"),
                                          (else_try),
                                            (eq, ":rand", 6),
			(jump_to_menu,"mnu_event_siege_27"),
                                          (else_try),
                                            (eq, ":rand", 7),
			(jump_to_menu,"mnu_event_siege_28"),
                                          (else_try),
                                            (eq, ":rand", 8),
			(jump_to_menu,"mnu_event_siege_29"),
                                          (else_try),
        (display_message,"@ "),
          (try_end),
	]),

#SEA BATTLES chief
#SEA BATTLES chief
(.2, [    #trigger rewritten by motomataru
   (party_get_current_terrain, ":terrain", "p_main_party"),
   (store_party_size_wo_prisoners, ":party_size", "p_main_party"),

   #player icon state and other considerations...
   (try_begin),
       (neq, ":terrain", rt_water),
       (neq, ":terrain", rt_river),
       (neq, ":terrain", rt_bridge),    #not rt_bridge used as water terrain
       (try_begin),
           (neq, "$sea_clock", 0),
           (assign, "$g_player_icon_state", pis_normal),
           (try_begin),
               (gt, ":party_size", 1),
               (display_message, "@Back on solid ground, out of reach of swells and sea monsters, your men seem more relaxed."),
               (call_script, "script_change_player_party_morale", "$sea_morale_penalty"),
           (else_try),
               (set_show_messages, 0),
               (call_script, "script_change_player_party_morale", "$sea_morale_penalty"),
               (set_show_messages, 1),
           (try_end),
           (assign, "$sea_morale_penalty", 0),
           (assign, "$ship_rented", 0),
           (assign, "$sea_clock", 0),
       (try_end),

   (else_try),    #water terrain
       (neq, "$g_player_is_captive", 1),
          (neq, "$freelancer_state", 1), #si esta en freelancer no paga chief
   (store_troop_gold, ":money", "trp_player"),
       (try_begin),
           (eq, "$g_player_icon_state", pis_normal),
           (assign, "$g_player_icon_state", pis_ship),
           (gt, ":money", 9),
           (display_message, "@You hire a nearby boat for the trip."),
           (assign, "$ship_rented", 1),
       (try_end),

       (try_begin),
           (eq, "$sea_clock", 0),
           (gt, ":party_size", 1),
           (display_message, "@Your men are uneasy about crossing the ocean and start losing heart."),
       (try_end),

       (store_mod, ":sea_tick", "$sea_clock", 5),
       (try_begin),
           (eq, ":sea_tick", 0),    #once per second...
           (try_begin),
               (gt, ":party_size", 1),
               (call_script, "script_change_player_party_morale", -1),
               (val_add, "$sea_morale_penalty", 1),
           (try_end),

           #ship rental
           (eq, "$ship_rented", 1),
           (try_begin),
               (store_party_size, ":rental_rate",      "p_main_party"),
                     (ge, ":money", ":rental_rate"),
                     (troop_remove_gold, "trp_player", ":rental_rate"),
##               (gt, ":money", 59),
##               (troop_remove_gold, "trp_player", 60),
               (call_script, "script_change_player_party_morale", -1),
           (else_try),
               (try_begin),
                   (eq, "$sea_clock", 0),
                   (display_message, "@Lacking money, you commandeer a nearby boat."),
               (else_try),
                   (display_message, "@Running out of money, you force the boat to continue your voyage."),
               (try_end),
               (call_script, "script_change_player_honor", -2),
               (call_script, "script_change_player_party_morale", -2),
               (assign, "$ship_rented", 0),
           (try_end),
       (try_end),

       (val_add, "$sea_clock", 1),
   (try_end),

   #other party icons
   (try_for_parties, ":cur_party"),
		(neq, ":cur_party", "p_main_party"),
		(party_get_template_id, ":cur_template", ":cur_party"),
		(party_get_icon, ":cur_icon", ":cur_party"),
		(party_get_current_terrain, ":terrain", ":cur_party"),
		(try_begin),
			(this_or_next|eq, ":terrain", rt_water),
			(this_or_next|eq, ":terrain", rt_river),
			(eq, ":terrain", rt_bridge),	#rt_bridge used as water terrain
			(try_begin),
				(neq, ":cur_icon", "icon_ship"),
				(neq, ":cur_icon", "icon_castle_snow_a"),
				(party_set_slot, ":cur_party", "slot_party_save_icon", ":cur_icon"),
				(try_begin),
					(neq, ":cur_template", "pt_deer_herd"),
					(neq, ":cur_template", "pt_boar_herd"),
					(neq, ":cur_template", "pt_wolf_herd"),
					(neq, ":cur_template", "pt_coat_herd"),
					(neq, ":cur_template", "pt_coatb_herd"),
					(neq, ":cur_template", "pt_wilddonkey_herd"),
					(party_set_icon, ":cur_party", "icon_ship"),
				(else_try),	#exception for wild animals
					(party_set_icon, ":cur_party", "icon_castle_snow_a"),	#???
				(try_end),
				
				(this_or_next|eq, ":cur_template", "pt_sea_raiders_ships"),	#in case ships had "leaked" onto land
				(this_or_next|eq, ":cur_template", "pt_sea_raiders_ships2"),
				(this_or_next|eq, ":cur_template", "pt_sea_raiders_ships3"),
				(eq, ":cur_template", "pt_sea_traders"),
				(party_set_flags, ":cur_party", pf_is_ship, 1),
			(try_end),

		#not water terrain
		(else_try),
			(neq, ":cur_template", "pt_sea_raiders_ships"),	#hope these guys get in the water! Problem is they spawn on land...
			(neq, ":cur_template", "pt_sea_raiders_ships2"),
			(neq, ":cur_template", "pt_sea_raiders_ships3"),

			(this_or_next|eq, ":cur_icon", "icon_castle_snow_a"),	#exception for wild animals
			(eq, ":cur_icon", "icon_ship"),
			(try_begin),
				(eq, ":cur_template", "pt_sea_traders"),
				(party_set_icon, ":cur_party", "icon_gray_knight"),
				(party_set_flags, ":cur_party", pf_is_ship, 0),
			(else_try),
				(party_get_slot, ":new_icon", ":cur_party", "slot_party_save_icon"),
				(party_set_icon, ":cur_party", ":new_icon"),
			(try_end),
		# (else_try),
# (this_or_next|eq, ":cur_template", "pt_sea_raiders_ships"),
# (this_or_next|eq, ":cur_template", "pt_sea_raiders_ships2"),
# (eq, ":cur_template", "pt_sea_raiders_ships3"),
# (eq, ":cur_icon", "icon_ship"),
# (assign, reg0, ":cur_party"),
# (assign, reg1, ":cur_template"),
# (display_message, "@Party {reg0} type {reg1} sailing on land!"),
			# (try_begin),
				# (eq, ":cur_template", "pt_kingdom_hero_party"),
				# (party_set_icon,":cur_party","icon_flagbearer_a"),
			# (else_try),
				# (this_or_next|eq, ":cur_template", "pt_dplmc_gift_caravan"),
				# (this_or_next|eq, ":cur_template", "pt_player_loot_wagon"),
				# (eq, ":cur_template", "pt_kingdom_caravan_party"),
				# (party_set_icon,":cur_party","icon_mule"),
			# (else_try),
				# (this_or_next|eq, ":cur_template", "pt_dplmc_recruiter"),
				# (this_or_next|eq, ":cur_template", "pt_personal_messenger"),
				# (eq, ":cur_template", "pt_merchant_caravan"),
				# (party_set_icon,":cur_party","icon_gray_knight"),
			# (else_try),
				# (eq, ":cur_template", "pt_skirmish_party"),
				# (party_set_icon,":cur_party","icon_khergit"),
			# (else_try),
				# (this_or_next|eq, ":cur_template", "pt_sacerdotes_party"),
				# (this_or_next|eq, ":cur_template", "pt_paganos_party"),
				# (eq, ":cur_template", "pt_village_farmers"),
				# (party_set_icon,":cur_party","icon_peasant"),
			# (else_try),
				# (this_or_next|eq, ":cur_template", "pt_reinforcements"),
				# (this_or_next|eq, ":cur_template", "pt_manhunters"),
				# (this_or_next|eq, ":cur_template", "pt_neko"),
				# (this_or_next|eq, ":cur_template", "pt_cado_template"),
				# (this_or_next|eq, ":cur_template", "pt_arrians"),
				# (this_or_next|eq, ":cur_template", "pt_eadfrith"),
				# (this_or_next|eq, ":cur_template", "pt_center_reinforcements"),
				# (this_or_next|eq, ":cur_template", "pt_looters"),
				# (this_or_next|eq, ":cur_template", "pt_forest_bandits"),
				# (this_or_next|eq, ":cur_template", "pt_steppe_bandits"),
				# (this_or_next|eq, ":cur_template", "pt_mountain_bandits"),
				# (this_or_next|eq, ":cur_template", "pt_sea_raiders2"),
				# (this_or_next|eq, ":cur_template", "pt_taiga_bandits"),
				# (this_or_next|eq, ":cur_template", "pt_deserters"),
				# #cambio parties navales
				# # (eq, ":cur_template", "pt_sea_raiders"),
				# (this_or_next|eq, ":cur_template", "pt_sea_raiders"),
				# (this_or_next|eq, ":cur_template", "pt_sea_raiders_ships"),
				# (this_or_next|eq, ":cur_template", "pt_sea_raiders_ships2"),
				# (eq, ":cur_template", "pt_sea_raiders_ships3"),
				# (party_set_icon,":cur_party","icon_axeman"),
			# (else_try),
				# (eq, ":cur_template", "pt_cattle_herd1"),
				# (party_set_icon,":cur_party","icon_cattle"),
			# (try_end),
		(try_end),
	(try_end),	#try_for_parties
 ]),
#### SEA BATTLES END chief#### SEA BATTLES END chief
  #seafare de duh chief
  	(24, #Floris Seafaring Wilderness Check
	[
		(try_for_parties, ":party_no"),
		    (party_slot_eq, ":party_no", "slot_party_type", spt_ship),
			(party_slot_eq, ":party_no", "slot_ship_center", ship_wild_no_guard),
			(party_get_slot, ":timer", ":party_no", "slot_ship_time"),
			(store_current_hours, ":cur_time"),
			(ge, ":cur_time", ":timer"),
			(store_random_in_range, ":luck", 0, 10),
			(ge, ":luck", 8),
			(str_store_party_name, s1, ":party_no"),
			(display_message, "@You have a bad feeling about your ship {s1}."),
			(display_message, "@You have a bad feeling about your ship {s1}."),
			(display_message, "@Ship {s1} isnt yet. Oh, damn!"), #chief
			(remove_party, ":party_no"),			
		(try_end),
		]),

	(1, #Floris fishing
	[	
		(try_begin),
			(party_get_current_terrain, ":terrain", "p_main_party"),
         (this_or_next|eq,":terrain",0), #chief
         (this_or_next|eq,":terrain",7), #chief
          (eq,":terrain",8), #chief
			(neq, "$g_player_icon_state", pis_ship),
			(assign, "$g_player_icon_state", pis_ship),
		(try_end),
 
		(try_begin),
			(party_get_slot, ":timer", "p_main_party", "slot_ship_time"),
			(gt, ":timer", 0),
			(store_current_hours, ":cur_time"),			
			(ge, ":cur_time", ":timer"),
			(try_begin),
				(party_get_current_terrain, ":terrain", "p_main_party"),
				(eq, ":terrain", 0),
				(store_skill_level, ":skill", skl_foraging,"trp_player"),
				(val_mul, ":skill", 10),
				(store_random_in_range, ":luck", 0, 100),
				(ge, ":skill", ":luck"),
				(store_free_inventory_capacity, ":i_space", "trp_player"),
				(try_begin),
					(ge, ":i_space", 1),
					(display_message, "@You caught some fish."),
					(troop_add_item, "trp_player", "itm_smoked_fish"),
					#(troop_add_merchandise, "trp_player", "itm_smoked_fish", 1),
				(else_try),
					(display_message, "@Due to insufficient space, you had to throw the fish back into the ocean"),
				(try_end),				
				(assign,"$g_camp_mode", 0),
				(rest_for_hours_interactive, 0, 5, 1),
				(party_set_slot, "p_main_party", "slot_ship_time", 0),
			(else_try),
				(display_message, "@All you caught were some seaweeds."),
				(assign,"$g_camp_mode", 0),
				(rest_for_hours_interactive, 0, 5, 1),
				(party_set_slot, "p_main_party", "slot_ship_time", -1),
			(try_end),
		(try_end),



	]),
  #chief acaba duh
  ##CC
  # Moving prisoners to the center when a lord in a center
  (3,
   [
       (try_for_range, ":troop_no", heroes_begin, heroes_end),
         (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
         (troop_get_slot, ":troop_party_no", ":troop_no", "slot_troop_leaded_party"),
         (ge, ":troop_party_no", 1),
         (party_is_active, ":troop_party_no"),

         (party_get_attached_to, ":cur_attached_town", ":troop_party_no"),
         (ge, ":cur_attached_town", 1),
         (party_get_cur_town, ":destination", ":troop_party_no"),
         (is_between, ":destination", centers_begin, centers_end),
         
         (this_or_next|party_slot_eq, ":destination", "slot_party_type", spt_town),
         (party_slot_eq, ":destination", "slot_party_type", spt_castle),
         (store_faction_of_party, ":troop_faction_no", ":troop_party_no"),
         (store_faction_of_party, ":destination_faction_no", ":destination"),
         (eq, ":troop_faction_no", ":destination_faction_no"),
         (party_get_num_prisoner_stacks, ":num_stacks", ":troop_party_no"),
         (gt, ":num_stacks", 0),
         (assign, "$g_move_heroes", 1),
         (call_script, "script_party_prisoners_add_party_prisoners", ":destination", ":troop_party_no"),
         (assign, "$g_move_heroes", 1),
         (call_script, "script_party_remove_all_prisoners", ":troop_party_no"),
       (try_end),
    ]),

  (24,  # mercenarios se les escapan prisioneros
   [
    (try_for_parties, ":party_no"),
          (party_slot_eq, ":party_no","slot_party_type", spt_companion_raider),
            (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
            (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
              (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
              (party_prisoner_stack_get_size, ":stack_size", ":party_no", ":troop_iterator"),
          (party_remove_prisoners, ":party_no", ":cur_troop_id", ":stack_size"),
#         (display_message, "@Oops: your mercenary captain kills his prisoners to he can move faster."),
          (try_end),
         (display_message, "@Oops: your mercenary captain kills his prisoners to he can move faster."),
     (try_end),
   ]),

##  (120,  # walled centers sell prisoners CC
##   [
##      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
##        (party_get_slot, ":town_lord", ":center_no", "slot_town_lord"),
##        (gt, ":town_lord", "trp_player"), #center does not belong to player.
##        (neg|is_between, ":town_lord", companions_begin, companions_end), # not companions
##        # processing ransom
##        (party_clear, "p_temp_party"),
##        (party_get_num_prisoner_stacks, ":prisoner_stacks", ":center_no"),
##        (try_for_range_backwards, ":prisoner_stack_no", 0, ":prisoner_stacks"),
##          (party_prisoner_stack_get_troop_id, ":prisoner_troop_no", ":center_no", ":prisoner_stack_no"),
##          (neg|troop_is_hero, ":prisoner_troop_no"),
##          (store_troop_faction, ":prisoner_faction", ":prisoner_troop_no"),
##          (neq, ":prisoner_faction", "fac_outlaws"),
##          (party_prisoner_stack_get_size, ":prisoner_stack_size", ":center_no", ":prisoner_stack_no"),
##          (party_remove_prisoners, ":center_no", ":prisoner_troop_no", ":prisoner_stack_size"),
##          (party_add_members, "p_temp_party", ":prisoner_troop_no", ":prisoner_stack_size"),
##        (try_end),
##        (call_script, "script_calculate_ransom_for_party", "p_temp_party"),
##        (assign, ":total_ransom_cost", reg0),
##        (party_get_slot, ":cur_wealth", ":center_no", "slot_town_wealth"),
##        (val_add, ":cur_wealth", ":total_ransom_cost"),
##        (party_set_slot, ":center_no", "slot_town_wealth", ":cur_wealth"),
##        ## upgrade after processing ransom
##        (store_mul, ":xp_gain", ":total_ransom_cost", 5),
##        #(party_upgrade_with_xp, ":center_no", ":xp_gain"),
##        (call_script, "script_upgrade_hero_party", ":center_no", ":xp_gain"),
##      (try_end),
##   ]),

####################grueso chief acaba######LINE190 intext
    (24,
   [
	  # Setting food bonuses - these have been changed to incentivize using historical rations. Bread is the most cost-efficient#gdwthisoverlaps w scripts whowin?
	  #Staples
      (item_set_slot, "itm_bread", "slot_item_food_bonus", 6), #brought up from 4
      (item_set_slot, "itm_grain", "slot_item_food_bonus", 3), #new - can be boiled as porridge
	  
	  #Fat sources - preserved
      (item_set_slot, "itm_smoked_fish", "slot_item_food_bonus", 5),#gdwdrdsltfishawful
      (item_set_slot, "itm_dried_meat", "slot_item_food_bonus", 8),
      (item_set_slot, "itm_cheese", "slot_item_food_bonus", 6),#gdwnewprices
      (item_set_slot, "itm_sausages", "slot_item_food_bonus", 5),#gdwnewprices
      (item_set_slot, "itm_butter", "slot_item_food_bonus", 7), #brought down from 8

	  #Fat sources - perishable
      (item_set_slot, "itm_chicken", "slot_item_food_bonus", 8), #brought up from 7
      (item_set_slot, "itm_cattle_meat", "slot_item_food_bonus", 11), #gdwnewprices
      (item_set_slot, "itm_pork", "slot_item_food_bonus", 9), #gdwnewprices
	  
	  #Produce
      (item_set_slot, "itm_raw_olives", "slot_item_food_bonus", 10),#gdwnewprices
      (item_set_slot, "itm_cabbages", "slot_item_food_bonus", 4),#gdwnewprices
      (item_set_slot, "itm_raw_grapes", "slot_item_food_bonus", 8),
      (item_set_slot, "itm_apples", "slot_item_food_bonus", 5), #gdwnewprices

	  #Sweet items
      (item_set_slot, "itm_mead", "slot_item_food_bonus", 16), #brought down from 8
      (item_set_slot, "itm_honey", "slot_item_food_bonus", 10), ##gdwnewprices6
      
      (item_set_slot, "itm_wine", "slot_item_food_bonus", 12),#gdwnewprices
      (item_set_slot, "itm_ale", "slot_item_food_bonus", 14),

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting chief Mod begin#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
      (item_set_slot, "itm_deer_meat", "slot_item_food_bonus", 11),#gdwnewprices
      (item_set_slot, "itm_boar_meat", "slot_item_food_bonus", 13),#gdwnewprices
      (item_set_slot, "itm_wolf_meat", "slot_item_food_bonus", 8),#gdwnon-perishable
      (item_set_slot, "itm_goat_meat", "slot_item_food_bonus", 12),#gdwrare
      (item_set_slot, "itm_goatb_meat", "slot_item_food_bonus", 9),#gdwmorecomon
      (item_set_slot, "itm_wilddonkey_meat", "slot_item_food_bonus", 11),#gdwnewprices
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#Hunting chief Mod end#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#Estandartes bonus de moral chief
      (item_set_slot, "itm_wessexbanner1", "slot_item_food_bonus", 15),#gdwunchanged
      (item_set_slot, "itm_cavalrybannert2", "slot_item_food_bonus", 17),#gdw16inscripts
      (item_set_slot, "itm_spearbannert2", "slot_item_food_bonus", 15),
      (item_set_slot, "itm_spearbanner4", "slot_item_food_bonus", 15),
      (item_set_slot, "itm_spearbanner5", "slot_item_food_bonus", 15),
      (item_set_slot, "itm_wessexbanner6", "slot_item_food_bonus", 15),
      (item_set_slot, "itm_wessexbanner7", "slot_item_food_bonus", 15),
      (item_set_slot, "itm_wessexbanner8", "slot_item_food_bonus", 15),
      (item_set_slot, "itm_wessexbanner9", "slot_item_food_bonus", 15),
      (item_set_slot, "itm_heraldicbannert3", "slot_item_food_bonus", 18),#gdwtest15
   ]),

# Check escape hero prisoners in lairs. No lords in lair
          (2,
           [
               (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "p_fort", 990),
            ]),


] \
+ economy.simple_triggers \
+ loans.simple_triggers \
+ companions.simple_triggers \
+ caravans.simple_triggers \
+ villages.simple_triggers \
+ patrols.simple_triggers \
+ constable.simple_triggers \
