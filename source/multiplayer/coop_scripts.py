from source.header_operations import *
from source.header_common import *
from source.header_presentations import *
from source.header_skills import *
from source.header_mission_templates import *
from source.header_terrain_types import *
from source.header_items import *
from source.header_item_modifiers import *
from source.header_troops import *

from source.module_constants import *

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

coop_scripts = [

   ("coop_troop_can_use_item",
   [
    (try_begin), 
      (neg|is_vanilla_warband),
      (store_script_param, ":troop", 1),
      (store_script_param, ":item", 2),
      (store_script_param, ":item_modifier", 3),

      (item_get_difficulty, ":difficulty", ":item"),
      (item_get_type, ":type", ":item"),

      (try_begin),
        (eq, ":difficulty", 0), # don't apply imod modifiers if item has no requirement
      (else_try),
        (eq, ":item_modifier", imod_stubborn),
        (val_add, ":difficulty", 1),
      (else_try),
        (eq, ":item_modifier", imod_timid),
        (val_sub, ":difficulty", 1),
      (else_try),
        (eq, ":item_modifier", imod_heavy),
        (neq, ":type", itp_type_horse),
        (val_add, ":difficulty", 1),	  
      (else_try),
        (eq, ":item_modifier", imod_strong),
        (val_add, ":difficulty", 2),	  
      (else_try),
        (eq, ":item_modifier", imod_masterwork),
        (val_add, ":difficulty", 4),	  
      (try_end),
	  	  
      (try_begin),
        (eq, ":type", itp_type_horse),
        (store_skill_level, ":skill", skl_riding, ":troop"),
      (else_try),
        (eq, ":type", itp_type_shield),
        (store_skill_level, ":skill", skl_shield, ":troop"),
      (else_try),
        (eq, ":type", itp_type_bow),
        (store_skill_level, ":skill", skl_power_draw, ":troop"),
      (else_try),
        (eq, ":type", itp_type_thrown),
        (store_skill_level, ":skill", skl_power_throw, ":troop"),
      (else_try),
        (store_attribute_level, ":skill", ":troop", ca_strength),
      (try_end),
      
      (try_begin),
        (lt, ":skill", ":difficulty"),
        (assign, reg0, 0),
      (else_try),
        (assign, reg0, 1),
      (try_end),

    (try_end),
   ]),


 #
 # script_coop_on_admin_panel_load
  ("coop_on_admin_panel_load",
    [
      (try_begin), 
        (neg|is_vanilla_warband),
        (dict_create, "$coop_dict"),
        (dict_load_file, "$coop_dict", "@coop_battle", 2),

        (dict_get_int, "$coop_battle_state", "$coop_dict", "@battle_state"), # 0 = no battle 1 = is setup 2 = is done
        (eq, "$coop_battle_state", coop_battle_state_setup_sp),
        (dict_set_int, "$coop_dict", "@battle_state", coop_battle_state_setup_mp), # disable starting twice
        (assign, "$coop_battle_state", coop_battle_state_setup_mp),
        (dict_save, "$coop_dict", "@coop_battle"),

#PREPARE TO CREATE PARTIES
        #assigning constants before copy reg to parties
        (assign, "$coop_cur_temp_party_enemy", coop_temp_party_enemy_begin), #store current spawn party
        (assign, "$coop_cur_temp_party_ally", coop_temp_party_ally_begin), #store current spawn party
        (assign, "$coop_main_party_spawn", coop_temp_party_ally_begin), #main party spawn party

        (call_script, "script_coop_copy_file_to_parties_mp"),	#also copies admin settings to variables

#CHANGE ADMIN PANEL

        (dict_get_int, ":garrison_commander_party", "$coop_dict", "@p_castle_lord"),
        (dict_get_int, ":garrison_party", "$coop_dict", "@p_garrison"),
        (dict_get_int, "$coop_castle_banner", "$coop_dict", "@p_garrison_banner"),
        (dict_get_int, "$coop_battle_type", "$coop_dict", "@map_type"),

        (try_begin),
          (eq, "$coop_battle_type", coop_battle_type_field_battle), #field battle
          (assign, ":coop_game_type", multiplayer_game_type_coop_battle),
        (else_try),
          (eq, "$coop_battle_type", coop_battle_type_village_player_attack), #village battle
          (assign, ":coop_game_type", multiplayer_game_type_coop_battle),
          (store_add, "$coop_garrison_commander_party", coop_temp_party_enemy_begin, ":garrison_commander_party"), 
          (store_add, "$coop_garrison_party", coop_temp_party_enemy_begin, ":garrison_party"), #garrison is first enemy party
        (else_try),
          (eq, "$coop_battle_type", coop_battle_type_village_player_defend), #village battle
          (assign, ":coop_game_type", multiplayer_game_type_coop_battle),
          (store_add, "$coop_garrison_commander_party", coop_temp_party_ally_begin, ":garrison_commander_party"), 
          (store_add, "$coop_garrison_party", coop_temp_party_ally_begin, ":garrison_party"), #garrison is first ally party
        (else_try),
          (eq, "$coop_battle_type", coop_battle_type_siege_player_attack),#player attacking siege
          (assign, ":coop_game_type", multiplayer_game_type_coop_siege),
          (assign, "$defender_team", 0),
          (assign, "$attacker_team", 1),
          (store_add, "$coop_garrison_commander_party", coop_temp_party_enemy_begin, ":garrison_commander_party"), 
          (store_add, "$coop_garrison_party", coop_temp_party_enemy_begin, ":garrison_party"), #garrison is first enemy party
        (else_try),
          (eq, "$coop_battle_type", coop_battle_type_siege_player_defend), #player defending siege
          (assign, ":coop_game_type", multiplayer_game_type_coop_siege), 
          (assign, "$attacker_team", 0),
          (assign, "$defender_team", 1),
          (store_add, "$coop_garrison_commander_party", coop_temp_party_ally_begin, ":garrison_commander_party"), 
          (store_add, "$coop_garrison_party", coop_temp_party_ally_begin, ":garrison_party"), #garrison is first ally party
        (else_try),
          (eq, "$coop_battle_type", coop_battle_type_bandit_lair), #bandit lair battle
          (assign, ":coop_game_type", multiplayer_game_type_coop_battle),
          # (mission_tpl_entry_set_override_flags, "mt_coop_battle", 0, af_override_horse), #NEW
        (else_try),
          (assign, ":coop_game_type", multiplayer_game_type_deathmatch), #cant find type
        (try_end),
        (assign, "$g_multiplayer_game_type", ":coop_game_type"),

        (assign, "$coop_round", coop_round_battle),

        (assign, "$g_multiplayer_selected_map", "scn_random_multi_plain_medium"),
        (dict_get_int, "$coop_battle_scene", "$coop_dict", "@map_scn"),
        (dict_get_int, "$coop_castle_scene", "$coop_dict", "@map_castle"),
        (dict_get_int, "$coop_street_scene", "$coop_dict", "@map_street"),
        (dict_get_int, "$coop_map_party", "$coop_dict", "@map_party_id"),
      #set weather
        (dict_get_int, "$coop_time_of_day", "$coop_dict", "@map_time"),
        (dict_get_int, "$coop_cloud", "$coop_dict", "@map_cloud"),
        (dict_get_int, "$coop_haze", "$coop_dict", "@map_haze"),
        (dict_get_int, "$coop_rain", "$coop_dict", "@map_rain"),#0=none 1=rain 2=snow

        (assign, "$g_multiplayer_ready_for_spawning_agent", 0), #dont start battle yet
        #set team ratios
        (assign, ":num_bots_team_1", "$coop_num_bots_team_1"),
        (assign, ":num_bots_team_2", "$coop_num_bots_team_2"),
        (val_max, ":num_bots_team_1", 1),


        (dict_get_int, ":battle_advantage", "$coop_dict", "@battle_adv"),#clamp(((15.0f + advantage) / 15.0f), 0.2f, 2.5f) * number of allies

        (val_mul, ":battle_advantage", 1000),
        (val_add, ":battle_advantage", 15000),
        (val_div, ":battle_advantage", 15),
        (val_clamp, ":battle_advantage", 200, 2500),
        # (val_clamp, ":battle_advantage", 700, 1500),

        (try_begin),
          (eq, "$coop_battle_type", coop_battle_type_bandit_lair), #ignore advantage for bandit lair battle
          (assign, ":battle_advantage", 200),
        (try_end),
        (val_mul, ":num_bots_team_2", ":battle_advantage"),
        (store_div, "$coop_team_ratio", ":num_bots_team_2", ":num_bots_team_1"), #(ratio / 1000) * team 1 = team 2
        (val_clamp, "$coop_team_ratio", 500, 2000), #clamp to 0.5 ~ 2.0 (this ends up reducing the effect of battle advantage)

        (dict_get_str, s0, "$coop_dict", "@tm1_name"),
        (faction_set_name, "fac_player_supporters_faction", s0),
        (dict_get_int, "$coop_team_1_faction", "$coop_dict", "@tm0_fac"),
        (dict_get_int, "$coop_team_2_faction", "$coop_dict", "@tm1_fac"),

        #battle size limit
        (try_begin),
          (lt, "$coop_battle_size", 20), #min setting
          (assign, "$coop_battle_size",  100), #default battle size
        (try_end),
        # (assign, "$g_multiplayer_max_num_bots", 10001), #limit


      (try_for_range, reg1, 0, 9),
        (dict_get_str, s1, "$coop_dict", "@cls{reg1}_name"),
        (class_set_name, reg1, s1),
      (try_end),

        (assign, "$g_multiplayer_respawn_period", 0), 
        (assign, "$g_multiplayer_factions_voteable", 0), #dont allow these
        (assign, "$g_multiplayer_maps_voteable", 0),    #dont allow these
        (assign, "$g_multiplayer_auto_team_balance_limit", 1000), #set for some scripts but dont show in admin panel
        (assign, "$g_multiplayer_num_bots_voteable", -1), 

        (multiplayer_send_int_to_server, multiplayer_event_admin_set_add_to_servers_list, "$coop_set_add_to_servers_list"),
        # (multiplayer_send_int_to_server, multiplayer_event_admin_set_anti_cheat, "$coop_set_anti_cheat"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_max_num_players, "$coop_set_max_num_players"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_melee_friendly_fire, "$coop_set_melee_friendly_fire"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_friendly_fire, "$coop_set_friendly_fire"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_friendly_fire_damage_self_ratio, "$coop_set_friendly_fire_damage_self_ratio"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_friendly_fire_damage_friend_ratio, "$coop_set_friendly_fire_damage_friend_ratio"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_ghost_mode, "$coop_set_ghost_mode"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_control_block_dir, "$coop_set_control_block_dir"),
        (multiplayer_send_int_to_server, multiplayer_event_admin_set_combat_speed, "$coop_set_combat_speed"),

        #these are only set in script_coop_copy_reg_to_settings
        # (assign, "$g_multiplayer_kick_voteable", 1),
        # (assign, "$g_multiplayer_ban_voteable", 1),
        # (assign, "$g_multiplayer_valid_vote_ratio", 51), #more than 50 percent
        # (assign, "$g_multiplayer_player_respawn_as_bot", 0),
      (dict_save, "$coop_dict", "@coop_battle"),
      (dict_free, "$coop_dict"),

        (display_message, "@Admin panel set."),

      (try_end),
     ]),	
  

  # script_coop_copy_settings_to_file
  ("coop_copy_settings_to_file",
   [
#SP: setup battle
#MP: at battle end
    (try_begin), 
      (neg|is_vanilla_warband),
      (try_begin),
        (game_in_multiplayer_mode),#copy setting at end of battle (only ones that use native variables that may be changed in other modes)
        (server_get_add_to_game_servers_list, "$coop_set_add_to_servers_list"),
        # (server_get_anti_cheat, "$coop_set_anti_cheat"),
        (server_get_max_num_players, "$coop_set_max_num_players"),
        (server_get_friendly_fire, "$coop_set_friendly_fire"),
        (server_get_melee_friendly_fire, "$coop_set_melee_friendly_fire"),
        (server_get_friendly_fire_damage_self_ratio, "$coop_set_friendly_fire_damage_self_ratio"),
        (server_get_friendly_fire_damage_friend_ratio, "$coop_set_friendly_fire_damage_friend_ratio"),
        (server_get_ghost_mode, "$coop_set_ghost_mode"),
        (server_get_control_block_dir, "$coop_set_control_block_dir"),
        (server_get_combat_speed, "$coop_set_combat_speed"),
      (try_end),

      (dict_set_int, "$coop_dict", "@srvr_set0", "$coop_set_add_to_servers_list"),
      # (dict_set_int, "$coop_dict", "@srvr_set1", "$coop_set_anti_cheat"),
      (dict_set_int, "$coop_dict", "@srvr_set2", "$coop_set_max_num_players"),
      (dict_set_int, "$coop_dict", "@srvr_set3", "$coop_battle_size"),
      (dict_set_int, "$coop_dict", "@srvr_set4", "$coop_set_melee_friendly_fire"),
      (dict_set_int, "$coop_dict", "@srvr_set5", "$coop_set_friendly_fire"),
      (dict_set_int, "$coop_dict", "@srvr_set6", "$coop_set_friendly_fire_damage_self_ratio"),
      (dict_set_int, "$coop_dict", "@srvr_set7", "$coop_set_friendly_fire_damage_friend_ratio"),
      (dict_set_int, "$coop_dict", "@srvr_set8", "$coop_set_ghost_mode"),
      (dict_set_int, "$coop_dict", "@srvr_set9", "$coop_set_control_block_dir"),
      (dict_set_int, "$coop_dict", "@srvr_set10", "$coop_set_combat_speed"),
      (dict_set_int, "$coop_dict", "@srvr_set11", "$coop_battle_spawn_formation"),
      (dict_set_int, "$coop_dict", "@srvr_set12", "$g_multiplayer_kick_voteable"),
      (dict_set_int, "$coop_dict", "@srvr_set13", "$g_multiplayer_ban_voteable"),
      (dict_set_int, "$coop_dict", "@srvr_set14", "$g_multiplayer_valid_vote_ratio"),
      (dict_set_int, "$coop_dict", "@srvr_set15", "$g_multiplayer_player_respawn_as_bot"),
      (dict_set_int, "$coop_dict", "@srvr_set16", "$coop_skip_menu"),
      (dict_set_int, "$coop_dict", "@srvr_set17", "$coop_disable_inventory"),
      (dict_set_int, "$coop_dict", "@srvr_set18", "$coop_reduce_damage"),
    (try_end),
     ]),	


  # script_coop_copy_file_to_settings
  ("coop_copy_file_to_settings",
   [
#MP: before admin panel
#SP: when use results
    (try_begin), 
      (neg|is_vanilla_warband),
      (dict_get_int, "$coop_set_add_to_servers_list", "$coop_dict", "@srvr_set0"),
      # (dict_get_int, "$coop_set_anti_cheat", "$coop_dict", "@srvr_set1"),
      (dict_get_int, "$coop_set_max_num_players", "$coop_dict", "@srvr_set2"),
      (dict_get_int, "$coop_battle_size", "$coop_dict", "@srvr_set3"),
      (dict_get_int, "$coop_set_melee_friendly_fire", "$coop_dict", "@srvr_set4"),
      (dict_get_int, "$coop_set_friendly_fire", "$coop_dict", "@srvr_set5"),
      (dict_get_int, "$coop_set_friendly_fire_damage_self_ratio", "$coop_dict", "@srvr_set6"),
      (dict_get_int, "$coop_set_friendly_fire_damage_friend_ratio", "$coop_dict", "@srvr_set7"),
      (dict_get_int, "$coop_set_ghost_mode", "$coop_dict", "@srvr_set8"),
      (dict_get_int, "$coop_set_control_block_dir", "$coop_dict", "@srvr_set9"),
      (dict_get_int, "$coop_set_combat_speed", "$coop_dict", "@srvr_set10"),
      (dict_get_int, "$coop_battle_spawn_formation", "$coop_dict", "@srvr_set11"),
      (dict_get_int, "$g_multiplayer_kick_voteable", "$coop_dict", "@srvr_set12"),
      (dict_get_int, "$g_multiplayer_ban_voteable", "$coop_dict", "@srvr_set13"),
      (dict_get_int, "$g_multiplayer_valid_vote_ratio", "$coop_dict", "@srvr_set14"),
      (dict_get_int, "$g_multiplayer_player_respawn_as_bot", "$coop_dict", "@srvr_set15"),
      (dict_get_int, "$coop_skip_menu", "$coop_dict", "@srvr_set16"),
      (dict_get_int, "$coop_disable_inventory", "$coop_dict", "@srvr_set17"),
      (dict_get_int, "$coop_reduce_damage", "$coop_dict", "@srvr_set18"),
    (try_end),

     ]),	



  # script_coop_set_default_admin_settings
  ("coop_set_default_admin_settings",
   [
    #this should be set to run once at game_start
     (try_begin),    #set this first as default, then use saved setting
      (assign, "$coop_set_add_to_servers_list", 1),
      # (assign, "$coop_set_anti_cheat", 0),
      (assign, "$coop_set_max_num_players", 20),
      (assign, "$coop_battle_size", 100), 

      (assign, "$coop_set_melee_friendly_fire", 0),
      (assign, "$coop_set_friendly_fire", 1),
      (assign, "$coop_set_friendly_fire_damage_self_ratio", 0),
      (assign, "$coop_set_friendly_fire_damage_friend_ratio", 20),
      (assign, "$coop_set_ghost_mode", 0),
      (assign, "$coop_set_control_block_dir", 1),
      (assign, "$coop_set_combat_speed", 0),
      (assign, "$coop_battle_spawn_formation", 0),
      (assign, "$coop_skip_menu", 0),
      (assign, "$coop_disable_inventory", 0),
      (assign, "$coop_reduce_damage", 0),

      (assign, "$g_multiplayer_kick_voteable", 1),
      (assign, "$g_multiplayer_ban_voteable", 1),
      (assign, "$g_multiplayer_valid_vote_ratio", 50),#more than 50 percent
      (assign, "$g_multiplayer_player_respawn_as_bot", 1),
    (try_end),
     ]),	



  # script_coop_get_battle_state
  ("coop_get_battle_state",
   [
    (store_script_param, ":option", 1),
    (try_begin),
      (neg|is_vanilla_warband),
      (dict_create, ":dict"),
      (dict_load_file, ":dict", "@coop_battle", 2),
      (try_begin), 
        (eq, ":option", 1),
        (dict_get_int, "$coop_battle_state", ":dict", "@battle_state"), # 0 = no battle 1 = is setup 2 = is done
      (else_try),
        (eq, ":option", 2),
        # (dict_set_int, ":dict", "@battle_state",coop_battle_state_none),
        # (dict_save, ":dict", "@coop_battle"),
        (dict_delete_file, "@coop_battle"),
      (else_try),
        (eq, ":option", 3),
        (dict_set_int, ":dict", "@battle_state",coop_battle_state_started),
        (dict_save, ":dict", "@coop_battle"),

      (try_end),
      (dict_free, ":dict"),
    (else_try),
#      (display_message, "@Remember: Warband Script Enhancer 'WSE' is needed in order to play single player battles in multiplayer."), #chief cambia
      (display_message, "@ "), #chief cambia
    (try_end),
     ]),	



  # script_coop_init_mission_variables
  # This is called EVERY ROUND on ti_before_mission_start
  ("coop_init_mission_variables",
   [
    (assign, "$coop_string_received", 0), #init this global before we get names
    (assign, "$coop_class_string_received", 0), #init this global before we get class names

    (get_max_players, ":num_players"),
    (try_for_range, ":all_player_no", 0, ":num_players"),
      (player_is_active, ":all_player_no"),
      (player_set_slot, ":all_player_no", "slot_player_coop_selected_troop", 0), #clear these slots every round
    (try_end),
    (try_begin),
      (neg|multiplayer_is_server),
      # (try_for_range, ":slot", 100, 200),
        # (troop_set_slot, "trp_temp_array_a", ":slot", -1),
        # (troop_set_slot, "trp_temp_array_b", ":slot", -1),
      # (try_end),

        (party_clear, coop_temp_party_enemy_heroes),
        (party_clear, coop_temp_party_ally_heroes),

      (try_for_range, ":slot", 0, 250),
        (troop_set_slot, "trp_temp_troop", ":slot", -1),
      (try_end),
    (try_end),

     ]),	


	#script_coop_get_scene_name
  # INPUT: arg1 = option_index, arg2 = option_value
  ("coop_get_scene_name",
    [
     (store_script_param, ":scene_no", 1),

      (str_store_string, s0, "@Unknown"),
      (try_begin),
        (gt, "$coop_map_party", 0), #if we know the party use it first
        (str_store_party_name, s0,  "$coop_map_party"),
      (else_try),
        (assign, ":scene_party", 0),
        (try_begin),
          (assign, ":end", castles_end),
          (try_for_range, ":castle_no", castles_begin, ":end"),
            (store_sub, ":offset", ":castle_no", castles_begin),
            (val_mul, ":offset", 3),
            (store_add, ":exterior_scene_no", "scn_castle_1_exterior", ":offset"),
            (store_add, ":interior_scene_no", "scn_castle_1_interior", ":offset"),
            (this_or_next|eq, ":scene_no", ":exterior_scene_no"),
            (eq, ":scene_no", ":interior_scene_no"),
            (assign, ":scene_party", ":castle_no"),
            (assign, ":end", 0),
          (try_end),

          (gt, ":end", 0),
          (assign, ":end", towns_end),
          (try_for_range, ":town_no", towns_begin, ":end"),
            (store_sub, ":offset", ":town_no", towns_begin),
            (store_add, ":town_center", "scn_town_1_center", ":offset"),
            (store_add, ":town_castle", "scn_town_1_castle", ":offset"),
            (store_add, ":town_walls", "scn_town_1_walls", ":offset"),
            (store_add, ":town_arena", "scn_town_1_arena", ":offset"),

            (this_or_next|eq, ":scene_no", ":town_arena"),
            (this_or_next|eq, ":scene_no", ":town_walls"),
            (this_or_next|eq, ":scene_no", ":town_castle"),
            (eq, ":scene_no", ":town_center"),
            (assign, ":scene_party", ":town_no"),
            (assign, ":end", 0),
          (try_end),
            
          (gt, ":end", 0),
          (assign, ":end", villages_end),
          (try_for_range, ":village_no", villages_begin, ":end"),
            (store_sub, ":offset", ":village_no", villages_begin),
            (store_add, ":village_scene_no", "scn_village_1", ":offset"),
            (eq, ":village_scene_no", ":scene_no"),
            (assign, ":scene_party", ":village_no"),
            (assign, ":end", 0),
          (try_end),
        (try_end),

        (try_begin),
          (eq, ":end", 0), #if center was found
          (str_store_party_name, s0,  ":scene_party"),
        (else_try),
          (try_begin),
            (eq, ":scene_no", "scn_lair_steppe_bandits"),
            (str_store_string, s0, "@Steppe Bandit Lair"),
          (else_try),
            (eq, ":scene_no", "scn_lair_taiga_bandits"),
            (str_store_string, s0, "@Tundra Bandit Lair"),
          (else_try),
            (eq, ":scene_no", "scn_lair_desert_bandits"),
            (str_store_string, s0, "@Desert Bandit Lair"),
          (else_try),
            (eq, ":scene_no", "scn_lair_forest_bandits"),
            (str_store_string, s0, "@Forest Bandit Camp"),
          (else_try),
            (eq, ":scene_no", "scn_lair_mountain_bandits"),
            (str_store_string, s0, "@Mountain Bandit Hideout"),
          (else_try),
            (eq, ":scene_no", "scn_lair_sea_raiders"),
            (str_store_string, s0, "@Sea Raider Landing"),
          (else_try), #chief anade
            (str_store_string, s0, "@Landing"),
          (try_end),
        (try_end),

      (try_end),  

   ]),	


######## 
 #set_trigger_result tells game to add one to option_index and call script again
	#script_coop_server_send_data_before_join
  # INPUT: arg1 = option_index
  ("coop_server_send_data_before_join",
    [
     (store_script_param, ":option_index", 1),
    
     (try_begin),
       (eq, ":option_index", 0),
       (assign, reg0, "$coop_team_1_faction"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 1),
       (assign, reg0, "$coop_team_2_faction"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 2),
       (assign, reg0, "$coop_num_bots_team_1"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 3),
       (assign, reg0, "$coop_num_bots_team_2"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 4),
       (server_get_friendly_fire, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 5),
       (server_get_melee_friendly_fire, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 6),
       (server_get_friendly_fire_damage_self_ratio, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 7),
       (server_get_friendly_fire_damage_friend_ratio, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 8),
       (server_get_ghost_mode, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 9),
       (server_get_control_block_dir, reg0),       
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 10),
       (server_get_combat_speed, reg0),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 11),
       (assign, reg0, "$g_multiplayer_player_respawn_as_bot"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 12),
       (assign, reg0, "$coop_time_of_day"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 13),
       (assign, reg0, "$coop_rain"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 14),
       (assign, reg0, "$coop_cloud"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 15),
       (assign, reg0, "$coop_haze"),
       (set_trigger_result, 1),
     (else_try),
       (eq, ":option_index", 16),
       (assign, reg0, "$coop_castle_banner"),
       (set_trigger_result, 1),
     (try_end),     
       # (assign, reg1, ":option_index"),
       # (display_message, "@server send {reg1} {reg0}"),

   ]),	

	#script_coop_client_receive_data_before_join
  # INPUT: arg1 = option_index, arg2 = option_value
  ("coop_client_receive_data_before_join",
    [
     (store_script_param, ":option_index", 1),
     (store_script_param, ":option_value", 2),

       # (assign, reg1, ":option_index"),
       # (assign, reg2, ":option_value"),
       # (display_message, "@client get {reg1} {reg2}"),
     (try_begin),
       (eq, ":option_index", 0),
       (assign, reg1, 1),
       (str_store_string, s0, "str_team_reg1_faction"),
       (str_store_faction_name, s1, ":option_value"),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 1),
       (assign, reg1, 2),
       (str_store_string, s0, "str_team_reg1_faction"),
       (str_store_faction_name, s1, ":option_value"),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 2),
       (assign, reg1, 1),
       (str_store_string, s0, "@Number of troops on team {reg1}:"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 3),
       (assign, reg1, 2),
       (str_store_string, s0, "@Number of troops on team {reg1}:"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 4),
       (str_store_string, s0, "str_allow_friendly_fire"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_no_wo_dot"),
       (else_try),
         (str_store_string, s1, "str_yes_wo_dot"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 5),
       (str_store_string, s0, "str_allow_melee_friendly_fire"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_no_wo_dot"),
       (else_try),
         (str_store_string, s1, "str_yes_wo_dot"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 6),
       (str_store_string, s0, "str_friendly_fire_damage_self_ratio"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 7),
       (str_store_string, s0, "str_friendly_fire_damage_friend_ratio"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 8),
       (str_store_string, s0, "str_spectator_camera"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_free"),
       (else_try),
         (eq, ":option_value", 1),
         (str_store_string, s1, "str_stick_to_any_player"),
       (else_try),
         (eq, ":option_value", 2),
         (str_store_string, s1, "str_stick_to_team_members"),
       (else_try),
         (str_store_string, s1, "str_stick_to_team_members_view"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 9),
       (str_store_string, s0, "str_control_block_direction"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_automatic"),
       (else_try),
         (str_store_string, s1, "str_by_mouse_movement"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 10),
       (str_store_string, s0, "str_combat_speed"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_combat_speed_0"),
       (else_try),
         (eq, ":option_value", 1),
         (str_store_string, s1, "str_combat_speed_1"),
       (else_try),
         (eq, ":option_value", 2),
         (str_store_string, s1, "str_combat_speed_2"),
       (else_try),
         (eq, ":option_value", 3),
         (str_store_string, s1, "str_combat_speed_3"),
       (else_try),
         (str_store_string, s1, "str_combat_speed_4"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 11),
       (str_store_string, s0, "str_players_take_control_of_a_bot_after_death"),
       (try_begin),
         (eq, ":option_value", 0),
         (str_store_string, s1, "str_no_wo_dot"),
       (else_try),
         (str_store_string, s1, "str_yes_wo_dot"),
       (try_end),
       (str_store_string, s0, "str_s0_s1"),
     (else_try),
       (eq, ":option_index", 12),
       (assign, "$coop_time_of_day", ":option_value"),
       (str_store_string, s0, "@Time of day:"),
       (assign, reg0, ":option_value"),
       (str_store_string, s0, "str_s0_reg0"),
     (else_try),
       (eq, ":option_index", 13),
       (assign, "$coop_rain", ":option_value"),
     (else_try),
       (eq, ":option_index", 14),
       (assign, "$coop_cloud", ":option_value"),
     (else_try),
       (eq, ":option_index", 15),
       (assign, "$coop_haze", ":option_value"),
     (else_try),
       (eq, ":option_index", 16),
       (assign, "$coop_castle_banner", ":option_value"),
       (display_message, "@Recieved Scene Data."),
     (try_end),  

   ]),	


######## 
	
  # script_coop_server_player_joined_common
  # Input: arg1 
  # Output: none
  ("coop_server_player_joined_common",
   [
    (store_script_param, ":player_no", 1),

    (try_begin),
      (gt, ":player_no", 0), #dont send stats to server

      (str_store_faction_name, s0, "fac_player_supporters_faction"),
      (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),

      #send names of main party troop classes
      (try_for_range, ":class", 0, 9),
        (str_store_class_name, s0, ":class"), 
        (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
      (try_end),

      (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_castle_party, "$coop_map_party"),
      (get_max_players, ":num_players"),
      (try_for_range, ":all_player_no", 0, ":num_players"),
        (player_is_active, ":all_player_no"),
        (player_get_slot, ":other_player_selected_troop", ":all_player_no", "slot_player_coop_selected_troop"),
        (gt, ":other_player_selected_troop", 0),
        (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_player_set_slot, ":other_player_selected_troop", ":all_player_no", "slot_player_coop_selected_troop"),
      (try_end),

      #send list of heroes in battle (since client cannot upgrade character, only send fighting skills)
      (party_get_num_companion_stacks, ":num_heroes", coop_temp_party_enemy_heroes),
      (try_for_range, ":stack", 0, ":num_heroes"),
        (party_stack_get_troop_id, ":hero_troop", coop_temp_party_enemy_heroes, ":stack"),	
        (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_store_hero_troops, ":hero_troop", coop_temp_party_enemy_heroes),
#NEW
        (try_begin),
          # (neg|is_between, ":hero_troop", kings_begin, pretenders_end),
          (str_store_troop_name, s0, ":hero_troop"),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),

          (troop_get_face_keys, reg1, ":hero_troop"),
          (str_store_face_keys, s0, reg1),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
        (try_end),

        (try_for_range, ":attribut", ca_strength, ca_intelligence),#0,1
          (store_attribute_level,":value",":hero_troop",":attribut"),
          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_attribute, ":value",":hero_troop",":attribut"),
        (try_end),
        (try_for_range, ":skill", skl_horse_archery, skl_reserved_14),
          (neg|is_between, ":skill", "skl_reserved_9", "skl_power_draw"), #skip these skills
          (store_skill_level,":value",":skill",":hero_troop"),
          (gt,":value",0),
          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_skill, ":value",":hero_troop",":skill"),
        (try_end),
        (try_for_range, ":wprof", wpt_one_handed_weapon, 7),
          (store_proficiency_level,":value",":hero_troop",":wprof"),
          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_proficiency_linear, ":value",":hero_troop",":wprof"),
        (try_end),
      (try_end),

      (party_get_num_companion_stacks, ":num_heroes", coop_temp_party_ally_heroes),
      (try_for_range, ":stack", 0, ":num_heroes"),
        (party_stack_get_troop_id, ":hero_troop", coop_temp_party_ally_heroes, ":stack"),	
        (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_store_hero_troops, ":hero_troop", coop_temp_party_ally_heroes),
#NEW
        (try_begin),
          # (neg|is_between, ":hero_troop", kings_begin, pretenders_end),
          (str_store_troop_name, s0, ":hero_troop"),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),

          (troop_get_face_keys, reg1, ":hero_troop"),
          (str_store_face_keys, s0, reg1),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
        (try_end),

        (try_for_range, ":attribut", ca_strength, ca_intelligence),#0,1
          (store_attribute_level,":value",":hero_troop",":attribut"),
          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_attribute, ":value",":hero_troop",":attribut"),
        (try_end),
        (try_for_range, ":skill", skl_horse_archery, skl_reserved_14),
          (neg|is_between, ":skill", "skl_reserved_9", "skl_power_draw"), #skip these skills
          (store_skill_level,":value",":skill",":hero_troop"),
          (gt,":value",0),
          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_skill, ":value",":hero_troop",":skill"),
        (try_end),
        (try_for_range, ":wprof", wpt_one_handed_weapon, 7),
          (store_proficiency_level,":value",":hero_troop",":wprof"),
          (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_raise_proficiency_linear, ":value",":hero_troop",":wprof"),
        (try_end),
      (try_end),

    (try_end),
    #do send this to server
    (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_round, "$coop_round", "$coop_battle_started"), #start welcome message after getting team data
   ]),	


######## 
	#script_coop_receive_network_message
  # This script is called from the game engine when a new network message is received.
  # INPUT: arg1 = player_no, arg2 = event_type, arg3 = value, arg4 = value_2, arg5 = value_3, arg6 = value_4
  ("coop_receive_network_message",
    [
      (store_script_param, ":player_no", 1),
      (store_script_param, ":event_type", 2),

    (try_begin),
      #(multiplayer_is_server),
      (try_begin),
        #SERVER EVENTS#
        (eq, ":event_type", multiplayer_event_change_troop_id), #receive player chosen troop
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_battle),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_siege),
        (store_script_param, ":troop", 3),
        (try_begin),
          (gt, ":troop", 0),
          (player_get_agent_id, ":player_agent", ":player_no"),
          (this_or_next|eq, ":player_agent", -1),#if spectator
          (neg|agent_is_alive, ":player_agent"), #if dead

          #only continue if hero is not dead yet
          (player_get_team_no, ":player_team", ":player_no"),
          (assign, ":num", 0),
          (try_begin),
            (eq, ":player_team", 0),
            (party_count_members_of_type, ":num", coop_temp_party_enemy_heroes, ":troop"),
          (else_try),
            (eq, ":player_team", 1),
            (party_count_members_of_type, ":num", coop_temp_party_ally_heroes, ":troop"),
          (try_end),
          (eq, ":num", 1),

          (try_begin),
            (eq, "$coop_battle_started", 1),
            (assign, ":end_cond", 0),
            (try_for_agents, ":cur_agent"),
              (eq, ":end_cond", 0),
              (agent_is_alive, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_is_non_player, ":cur_agent"),
              (agent_get_troop_id,":troop_no", ":cur_agent"),
              (eq, ":troop", ":troop_no"),
              #(troop_is_hero, ":troop_no"),
              (player_set_troop_id, ":player_no", ":troop_no"),#NEW
              (player_control_agent, ":player_no", ":cur_agent"),

              (assign, ":end_cond", 1), #break
            (try_end),
          (else_try),
            #only tell other players before spawn, after spawn other players check agents if troop is in use
            (get_max_players, ":num_players"),
            (try_for_range, ":all_player_no", 0, ":num_players"), 
              (player_is_active, ":all_player_no"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_player_set_slot, ":troop", ":player_no", "slot_player_coop_selected_troop"),
            (try_end),
          (try_end),
          (player_set_slot, ":player_no", "slot_player_coop_selected_troop", ":troop"), #server always save to player slot

        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_change_team_no),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_battle),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_siege),
        (store_script_param, ":team", 3),
        (try_begin),
          (eq, ":team", multi_team_spectator),
          (try_begin),
            (eq, "$coop_battle_started", 0), #only send to players before spawn if already picked
            (player_get_slot,  ":player_troop", ":player_no", "slot_player_coop_selected_troop"),
            (gt, ":player_troop", 0),
            (get_max_players, ":num_players"),
            (try_for_range, ":all_player_no", 0, ":num_players"), 
              (player_is_active, ":all_player_no"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_player_set_slot, 0, ":player_no", "slot_player_coop_selected_troop"),
            (try_end),
          (try_end),
          (player_set_slot, ":player_no", "slot_player_coop_selected_troop", 0),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_set_bot_selection), #also called from native script for "slot_player_bot_type_1_wanted", "slot_player_bot_type_4_wanted"
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_battle),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_siege),
        (store_script_param, ":slot_no", 3),
        (store_script_param, ":value", 4),
        (try_begin),
          (is_between, ":slot_no", "slot_player_coop_class_wanted_begin", "slot_player_coop_class_wanted_end"), # coop only slots
          (is_between, ":value", 0, 2),
          (player_set_slot, ":player_no", ":slot_no", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_open_admin_panel), 
        (try_begin),
          (call_script, "script_coop_get_battle_state", 1), #sets coop_battle_state
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_battle_state, "$coop_battle_state"),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_battle),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_siege),
          (call_script, "script_game_quick_start"), #add this to native event when switching back to native game type
        (try_end),


      # COOP EVENTS#
      (else_try),
        (eq, ":event_type", multiplayer_event_coop_send_to_server),
        (store_script_param, ":event_subtype", 3),

        (try_begin),
          (eq, ":event_subtype", coop_event_start_map),
          (try_begin),
            (player_is_admin, ":player_no"),
            (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_battle),
            (eq, "$g_multiplayer_game_type", multiplayer_game_type_coop_siege),
            (get_max_players, ":num_players"),
            (try_for_range, ":all_player_no", 0, ":num_players"), 
              (player_is_active, ":all_player_no"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_set_scene_1, "$coop_time_of_day"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_set_scene_2, "$coop_rain"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_set_scene_3, "$coop_cloud"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_set_scene_4, "$coop_haze"),
              (multiplayer_send_4_int_to_player, ":all_player_no", multiplayer_event_coop_send_to_player, coop_event_set_scene_5, "$coop_castle_banner"),
            (try_end),
            (call_script, "script_coop_get_battle_state", 3), #sets state to started
            (team_set_faction, 0, "$coop_team_1_faction"),
            (team_set_faction, 1, "$coop_team_2_faction"),
            (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
            (start_multiplayer_mission, reg0, "$coop_battle_scene", 1),
          (try_end),

        (else_try),
          (eq, ":event_subtype", coop_event_setup_battle), #have server load saved battle
          (try_begin),
            (player_is_admin, ":player_no"),
            (call_script, "script_coop_on_admin_panel_load"),
            (eq, "$coop_battle_state", coop_battle_state_setup_mp),#only if coop battle is setup
            (call_script, "script_coop_server_send_admin_setttings_to_player", ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_receive_next_string, 3),
            (str_store_server_password, s0),
            (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),
            (call_script, "script_coop_get_battle_state", 1), #sets coop_battle_state
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_battle_state, "$coop_battle_state"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_skip_menu, "$coop_skip_menu"),
          (try_end),
        (else_try),
          (eq, ":event_subtype", coop_event_start_battle), 
          (try_begin),
            (eq, "$coop_battle_started", 0),
            (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
            (reset_mission_timer_a),
          (try_end),
        (else_try),
          (eq, ":event_subtype", coop_event_end_battle),
          (try_begin),
            (eq, "$coop_battle_started", 1),
            (call_script, "script_coop_copy_parties_to_file_mp"),
          (try_end),
          (try_begin),
            (neg|multiplayer_is_dedicated_server),
            (finish_mission,0), #alway end
          (try_end),
        (else_try),
          (eq, ":event_subtype", coop_event_open_admin_panel),
          (try_begin),
            (player_is_admin, ":player_no"),
            (call_script, "script_coop_server_send_admin_setttings_to_player", ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_receive_next_string, 3),
            (str_store_server_password, s0),
            (multiplayer_send_string_to_player, ":player_no", multiplayer_event_coop_send_to_player_string, s0),

            (call_script, "script_coop_get_battle_state", 1), #sets coop_battle_state
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_battle_state, "$coop_battle_state"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_skip_menu, "$coop_skip_menu"),
          (try_end),
        (else_try),
          (eq, ":event_subtype", coop_event_open_game_rules),
          (call_script, "script_coop_server_send_admin_setttings_to_player", ":player_no"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_open_game_rules),
        (else_try),
          (eq, ":event_subtype", coop_event_battle_size),
          (store_script_param, ":value", 4),
          (try_begin),
            (ge, ":value", 20),
            (assign, "$coop_battle_size", ":value"), #store current battle size setting
          (try_end),
        (else_try),
          (eq, ":event_subtype", coop_event_spawn_formation),
          (store_script_param, ":value", 4),
          (assign, "$coop_battle_spawn_formation", ":value"),
        (else_try),
          (eq, ":event_subtype", coop_event_skip_admin_panel),
          (store_script_param, ":value", 4),
          (assign, "$coop_skip_menu", ":value"),
        (else_try),
          (eq, ":event_subtype", coop_event_disable_inventory),
          (store_script_param, ":value", 4),
          (assign, "$coop_disable_inventory", ":value"),
        (else_try),
          (eq, ":event_subtype", coop_event_reduce_damage),
          (store_script_param, ":value", 4),
          (assign, "$coop_reduce_damage", ":value"),
        (else_try),
          (eq, ":event_subtype", coop_event_player_open_inventory_before_spawn),
          (try_begin),
            (eq, "$coop_disable_inventory", 0),#inventory access is optional
            (player_get_slot,  ":player_troop", ":player_no", "slot_player_coop_selected_troop"),
            (gt, ":player_troop", 0),
            (party_count_members_of_type,":num","$coop_main_party_spawn",":player_troop"),
            (eq,":num",1),
            (try_for_range, ":slot", 0, 9),
              (troop_get_inventory_slot, ":player_cur_item", ":player_troop", ":slot"),
              (troop_get_inventory_slot_modifier, ":player_cur_imod", ":player_troop", ":slot"),
              (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_inv_troop_set_slot, ":slot", ":player_cur_item", ":player_cur_imod"),
            (try_end),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_prsnt_coop_item_select), #done
          (try_end),

        (else_try),
          (eq, ":event_subtype", coop_event_player_get_selected_item_types),
          (store_script_param, ":itm_type_1", 4),
          (store_script_param, ":itm_type_2", 5),

          (player_get_slot,  ":player_troop", ":player_no", "slot_player_coop_selected_troop"),
          (try_begin),
            (player_get_agent_id, ":player_agent", ":player_no"),
            (ge, ":player_agent", 0),
            (agent_get_troop_id, ":player_troop", ":player_agent"),
          (try_end),     
          (troop_is_hero, ":player_troop"),

          (troop_get_inventory_capacity, ":end", "trp_temp_troop"),
          (val_add,":end", 1), 
          (try_for_range, ":slot", 10, ":end"),
            (troop_get_inventory_slot, ":item", "trp_temp_troop", ":slot"), #inventory troop
            (troop_get_inventory_slot_modifier, ":imod", "trp_temp_troop", ":slot"),
            #  (troop_inventory_slot_get_item_amount, ":item_quant", ":cur_troop", ":slot"),
            (gt, ":item", 0),
            (item_get_type, ":item_class", ":item"),

            (assign, ":continue_2", 0),
            (try_begin),
              (eq, ":itm_type_1", itp_type_one_handed_wpn),
              (is_between, ":item_class", itp_type_pistol, itp_type_animal), #add firearms here
              (assign, ":continue_2", 1),
            (else_try),
              (is_between, ":item_class", ":itm_type_1", ":itm_type_2"),
              (assign, ":continue_2", 1),
            (try_end),
            (eq, ":continue_2", 1),
            (call_script, "script_coop_troop_can_use_item",":player_troop", ":item", ":imod"),
            (eq, reg0, 1),
            (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_send_inventory, ":slot", ":item", ":imod"),
          # (assign, reg1, ":slot"), 
          # (str_store_item_name, s40, ":item"),
          # (display_message, "@sending inv slot {reg1}  = {reg0} {s40} "),
          (try_end),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_prsnt_coop_item_select), #done

        (else_try),
          (eq, ":event_subtype", coop_event_player_ask_for_selected_item),
          (store_script_param, ":equip_slot", 4),
          (store_script_param, ":item_id", 5),
          (store_script_param, ":party_inv_slot", 6),
          (player_get_slot,  ":player_troop", ":player_no", "slot_player_coop_selected_troop"),
          (try_begin),
            (player_get_agent_id, ":player_agent", ":player_no"),
            (ge, ":player_agent", 0),
            (agent_get_troop_id, ":player_troop", ":player_agent"),
          (try_end),     
          (troop_is_hero, ":player_troop"),

          (try_begin),
            (gt, ":item_id", 0),
            (ge, ":party_inv_slot", 10),

            (troop_get_inventory_slot, ":cur_item", ":player_troop", ":equip_slot"),
            (troop_get_inventory_slot_modifier, ":cur_imod", ":player_troop", ":equip_slot"),
            (troop_get_inventory_slot, ":new_item", "trp_temp_troop", ":party_inv_slot"),
            (troop_get_inventory_slot_modifier, ":new_imod", "trp_temp_troop", ":party_inv_slot"),

            (try_begin),
              (eq, ":item_id", ":new_item"),
              (call_script, "script_coop_troop_can_use_item",":player_troop", ":new_item", ":new_imod"),
              (eq, reg0, 1),
              (troop_set_inventory_slot, ":player_troop", ":equip_slot", ":new_item"),
              (troop_set_inventory_slot_modifier, ":player_troop", ":equip_slot", ":new_imod"),
              (troop_set_inventory_slot, "trp_temp_troop", ":party_inv_slot", ":cur_item"),
              (troop_set_inventory_slot_modifier, "trp_temp_troop", ":party_inv_slot", ":cur_imod"),

              #remove item from agent
              (try_begin),
                (player_get_agent_id, ":player_agent", ":player_no"),
                (ge, ":player_agent", 0),
                (lt, ":equip_slot", 4),
                (neg|is_vanilla_warband),
                (agent_set_item_slot, ":player_agent", ":equip_slot", ":new_item", ":new_imod"),#NEW
              (try_end),

            (else_try),
              (display_message, "@Trade failed."),
            (try_end),
            #after trade refresh that equip slot
            (troop_get_inventory_slot, ":player_cur_item", ":player_troop", ":equip_slot"),
            (troop_get_inventory_slot_modifier, ":player_cur_imod", ":player_troop", ":equip_slot"),
            (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_inv_troop_set_slot, ":equip_slot", ":player_cur_item", ":player_cur_imod"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_prsnt_coop_item_select), #done


            (try_begin), 
              (gt, ":new_item", 0),
              (str_store_item_name, s40, ":new_item"),
            (else_try),
              (str_store_string, s40, "@none"),
            (try_end),
            (try_begin), 
              (gt, ":cur_item", 0),
              (str_store_item_name, s42, ":cur_item"),
            (else_try),
              (str_store_string, s42, "@none"),
            (try_end),
            (str_store_troop_name, s41, ":player_troop"),
            (display_message, "@{s41} traded {s42} for {s40}."),

          (try_end),

        (else_try),
          (eq, ":event_subtype", coop_event_player_remove_selected_item),
          (store_script_param, ":equip_slot", 4),
          (store_script_param, ":item_remove", 5),
          (player_get_slot,  ":player_troop", ":player_no", "slot_player_coop_selected_troop"),
          (try_begin), #if agent has spawned already
            (player_get_agent_id, ":player_agent", ":player_no"),
            (ge, ":player_agent", 0),
            (agent_get_troop_id, ":player_troop", ":player_agent"),
          (try_end),     
          (troop_is_hero, ":player_troop"),

          (try_begin),
            (gt, ":item_remove", 0),
            (troop_get_inventory_slot, ":cur_item", ":player_troop", ":equip_slot"),
            (troop_get_inventory_slot_modifier, ":cur_imod", ":player_troop", ":equip_slot"),
            (eq, ":item_remove", ":cur_item"),

            (troop_get_inventory_capacity, ":end", "trp_temp_troop"),
            (val_add,":end", 1), 
            (try_for_range, ":party_inv_slot", 10, ":end"),
              (troop_get_inventory_slot, ":party_inv_item", "trp_temp_troop", ":party_inv_slot"),
              (lt, ":party_inv_item", 1),
              (troop_set_inventory_slot, ":player_troop", ":equip_slot", -1),
              (troop_set_inventory_slot_modifier, ":player_troop", ":equip_slot", -1),
              (troop_set_inventory_slot, "trp_temp_troop", ":party_inv_slot", ":cur_item"),
              (troop_set_inventory_slot_modifier, "trp_temp_troop", ":party_inv_slot", ":cur_imod"),

              (try_begin),
                (lt, ":equip_slot", 4),
                (player_get_agent_id, ":player_agent", ":player_no"),
                (ge, ":player_agent", 0),
                (agent_unequip_item, ":player_agent", ":cur_item", ":equip_slot"), #(agent_unequip_item, <agent_id>, <item_id>, [weapon_slot_no]),
              (try_end),
              (assign, ":end", 0),
            (try_end),
          (try_end),

        (try_end),


      (try_end),
    (try_end),


## CLIENT EVENTS ##
  (try_begin),
    (neg|multiplayer_is_dedicated_server),
    (try_begin),
      (eq, ":event_type", multiplayer_event_coop_send_to_player_string),

      (try_begin),
        (eq, "$coop_string_received", 0), 
        (faction_set_name, "fac_player_supporters_faction", s0),
        (assign, "$coop_string_received", 1), 
      (else_try),
        (eq, "$coop_string_received", 1), 
        (class_set_name, "$coop_class_string_received", s0), #store 8 strings for troop class names
        (val_add, "$coop_class_string_received", 1),

        (try_begin),
          (eq, "$coop_class_string_received", 9), # 8 strings, add one after each = 9
          (assign, "$coop_string_received", 2), 
        (try_end),
      (else_try),
#NEW
        (eq, "$coop_string_received", 2), 
        (troop_set_name, "$coop_last_hero_received", s0),
        (assign, "$coop_string_received", 3), 
      (else_try),
        (eq, "$coop_string_received", 3), 
        (try_begin),
          (neg|is_vanilla_warband),
          (face_keys_store_string, reg1, s0),
          (troop_set_face_keys, "$coop_last_hero_received", reg1),
        (try_end),
        (assign, "$coop_string_received", 2), 

      (else_try),
        (eq, "$coop_string_received", 4), #set by coop_event_round
        (server_set_password, s0),
      (try_end),

    (else_try),
      (eq, ":event_type", multiplayer_event_coop_send_to_player), 
      (store_script_param, ":event_subtype", 3),

      (try_begin),
        (eq, ":event_subtype", coop_event_store_hero_troops), 
        (store_script_param, ":hero_troop", 4),
        (store_script_param, ":party_no", 5),
        (try_begin),
          (neg|multiplayer_is_server), #server already added heroes to this party
          (party_add_members, ":party_no", ":hero_troop", 1),
        (try_end),
        (assign, "$coop_last_hero_received", ":hero_troop"), #remember troop to receive name
      (else_try),
        (eq, ":event_subtype", coop_event_round), 
        (store_script_param, ":value", 4),
        (store_script_param, ":value2", 5),
        (assign, "$coop_battle_started", ":value2"),
        (assign, "$coop_round", ":value"), #assign siege round
#NEW
        (assign, "$coop_string_received", 4), #set this after client has received all data
        (neq, "$coop_battle_started", -1),
          # player remembers troop selections, send to server when player joins (player id will change between rounds)
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_bot_type_1_wanted", "$g_multiplayer_bot_type_1_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_bot_type_2_wanted", "$g_multiplayer_bot_type_2_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_bot_type_3_wanted", "$g_multiplayer_bot_type_3_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_bot_type_4_wanted", "$g_multiplayer_bot_type_4_wanted"),

          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_coop_class_0_wanted", "$coop_class_0_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_coop_class_1_wanted", "$coop_class_1_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_coop_class_2_wanted", "$coop_class_2_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_coop_class_3_wanted", "$coop_class_3_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_coop_class_4_wanted", "$coop_class_4_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_coop_class_5_wanted", "$coop_class_5_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_coop_class_6_wanted", "$coop_class_6_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_coop_class_7_wanted", "$coop_class_7_wanted"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_bot_selection, "slot_player_coop_class_8_wanted", "$coop_class_8_wanted"),

        (try_begin), 
          (eq, "$coop_round", coop_round_battle),
          (assign, "$coop_my_team", multi_team_unassigned),  
          (start_presentation, "prsnt_coop_welcome_message"), #start welcome message after getting team data
        (else_try),
          (multiplayer_get_my_player, ":my_player_no"), #change my team in later rounds
          (ge, ":my_player_no", 0),
          (player_set_team_no, ":my_player_no", "$coop_my_team"),
          (multiplayer_send_int_to_server, multiplayer_event_change_team_no, "$coop_my_team"),
          (multiplayer_send_int_to_server, multiplayer_event_change_troop_id, "$coop_my_troop_no"),
        (try_end),
      (else_try),
        (eq, ":event_subtype", coop_event_troop_banner), 
        (store_script_param, ":value", 4),
        (assign, "$coop_agent_banner", ":value"), #assign spawning troops banner
      (else_try),
        (eq, ":event_subtype", coop_event_troop_raise_attribute),
        (store_script_param, ":value", 4),
        (store_script_param, ":selected_troop", 5),
        (store_script_param, ":attribut", 6),
        (troop_raise_attribute, ":selected_troop", ":attribut", -1000),
        (troop_raise_attribute, ":selected_troop", ":attribut", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_troop_raise_skill),
        (store_script_param, ":value", 4),
        (store_script_param, ":selected_troop", 5),
        (store_script_param, ":skill", 6),
        (troop_raise_skill, ":selected_troop", ":skill", -1000),
        (troop_raise_skill, ":selected_troop", ":skill", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_troop_raise_proficiency_linear),
        (store_script_param, ":value", 4),
        (store_script_param, ":selected_troop", 5),
        (store_script_param, ":prof", 6),
        (troop_raise_proficiency_linear, ":selected_troop", ":prof", -1000),
        (troop_raise_proficiency_linear, ":selected_troop", ":prof", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_troop_set_slot),
        (store_script_param, ":value", 4),
        (store_script_param, ":selected_troop", 5),
        (store_script_param, ":slot", 6),
        (troop_set_slot, ":selected_troop", ":slot", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_player_set_slot),
        (store_script_param, ":value", 4),
        (store_script_param, ":selected_player", 5),
        (store_script_param, ":slot", 6),
        (player_set_slot, ":selected_player", ":slot", ":value"),
        (try_begin), #if receiving other player spawn choice, refresh presentation
          (eq, ":slot", "slot_player_coop_selected_troop"),
          (assign, "$coop_refresh_troop_select_presentation", 1),

          (try_begin),
            (gt, ":value", 0),
            (str_store_player_username, s40, ":selected_player"),
            (str_store_troop_name, s41, ":value"),
            (display_message, "@{s40} has picked {s41}. "), #tell server when player picks troop
          (try_end), 
        (try_end), 
      (else_try),
        (eq, ":event_subtype", coop_event_inv_troop_set_slot),
        (store_script_param, ":slot", 4),
        (store_script_param, ":item", 5),
        (store_script_param, ":imod", 6),
        (troop_set_slot, "trp_temp_troop", ":slot", ":item"), #item slot 0..8
        (val_add, ":slot", 10),
        (troop_set_slot, "trp_temp_troop", ":slot", ":imod"),#imod slot 10..18


      (else_try),
        (eq, ":event_subtype", coop_event_send_inventory), #receive items of type for equipment slot
        (store_script_param, ":inv_slot", 4),
        (store_script_param, ":item", 5),
        (store_script_param, ":imod", 6),
        #  (store_script_param, ":item_quant", 6), #would need its own message type
        (store_add, ":cur_slot_index", "$coop_num_available_items", multi_data_item_button_indices_begin),
        (store_add, ":cur_imod_index",":cur_slot_index",100),
        (troop_set_slot, "trp_multiplayer_data", ":cur_slot_index", ":item"),
        (troop_set_slot, "trp_temp_troop", ":cur_slot_index", ":inv_slot"), #slot matching multi_data_item_button_indices_begin stores which inventory slot this item is from
        (troop_set_slot, "trp_temp_troop", ":cur_imod_index", ":imod"),
        (val_add, "$coop_num_available_items", 1),
      (else_try),
        (eq, ":event_subtype", coop_event_prsnt_coop_item_select),
        (start_presentation, "prsnt_coop_item_select"), #start presentation after we recieve all inventory
      (else_try),
        (eq, ":event_subtype", coop_event_set_scene_1),
        (store_script_param, ":value", 4),
        (assign, "$coop_time_of_day", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_set_scene_2),
        (store_script_param, ":value", 4),
        (assign, "$coop_rain", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_set_scene_3),
        (store_script_param, ":value", 4),
        (assign, "$coop_cloud", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_set_scene_4),
        (store_script_param, ":value", 4),
        (assign, "$coop_haze", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_set_scene_5),
        (store_script_param, ":value", 4),
        (assign, "$coop_castle_banner", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_return_team_faction),
        (store_script_param, ":team", 4),
        (store_script_param, ":value", 5),
        (try_begin), 
          (eq, ":team", 1),
          (assign, "$coop_team_1_faction", ":value"),
        (else_try),
          (eq, ":team", 2),
          (assign, "$coop_team_2_faction", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_subtype", coop_event_return_spawn_formation),
        (store_script_param, ":value", 4),
        (assign, "$coop_battle_spawn_formation", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_return_battle_size),
        (store_script_param, ":value", 4),
        (assign, "$coop_battle_size", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_return_game_type),
        (store_script_param, ":value", 4),
        (assign, "$g_multiplayer_game_type", ":value"),
     (else_try),
        (eq, ":event_subtype", coop_event_return_castle_party),
        (store_script_param, ":value", 4),
        (assign, "$coop_map_party", ":value"),
     (else_try),
        (eq, ":event_subtype", coop_event_return_battle_scene),
        (store_script_param, ":value", 4),
        (assign, "$coop_battle_scene", ":value"),
     (else_try),
        (eq, ":event_subtype", coop_event_return_disable_inventory),
        (store_script_param, ":value", 4),
        (assign, "$coop_disable_inventory", ":value"),
     (else_try),
        (eq, ":event_subtype", coop_event_return_reduce_damage),
        (store_script_param, ":value", 4),
        (assign, "$coop_reduce_damage", ":value"),
      (else_try),
        (eq, ":event_subtype", coop_event_return_skip_menu),
        (store_script_param, ":value", 4),
        (assign, "$coop_skip_menu", ":value"),
        (start_presentation, "prsnt_coop_admin_panel"),#this is the last option in admin panel, so start the presentation
      (else_try),
        (eq, ":event_subtype", coop_event_return_open_game_rules),
        #this is the last message for open rules
        (assign, "$g_multiplayer_show_server_rules", 1),
        (start_presentation, "prsnt_coop_welcome_message"),
      (else_try),
        (eq, ":event_subtype", coop_event_receive_next_string),
        (store_script_param, ":value", 4),
        (assign, "$coop_string_received", ":value"), 
      (else_try),
        (eq, ":event_subtype", coop_event_return_num_reserves),
        (store_script_param, ":team", 4),
        (store_script_param, ":value", 5),
        (try_begin), 
          (eq, ":team", 1),
          (assign, "$coop_num_bots_team_1", ":value"),
        (else_try),
          (eq, ":team", 2),
          (assign, "$coop_num_bots_team_2", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_subtype", coop_event_return_battle_state),
        (store_script_param, ":value", 4),
        (assign, "$coop_battle_state", ":value"), 
      (else_try),
        (eq, ":event_subtype", coop_event_result_saved),
        (assign, "$coop_battle_started", -1),
        (display_message, "@Battle result saved."),
      (try_end), 





    (try_end),  
  (try_end),  

      ]),





#script_coop_server_send_admin_setttings_to_player
  # Input: arg1 = player_agent
  # Output: none
  ("coop_server_send_admin_setttings_to_player",
    [
     (store_script_param, ":player_no", 1),
            (server_get_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
            (server_get_max_num_players, ":max_num_players"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_max_num_players, ":max_num_players"),
            # (server_get_anti_cheat, ":server_anti_cheat"),
            # (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_anti_cheat, ":server_anti_cheat"),
            (server_get_friendly_fire, ":server_friendly_fire"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire, ":server_friendly_fire"),
            (server_get_melee_friendly_fire, ":server_melee_friendly_fire"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_melee_friendly_fire, ":server_melee_friendly_fire"),
            (server_get_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
            (server_get_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
            (server_get_ghost_mode, ":server_ghost_mode"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_ghost_mode, ":server_ghost_mode"),
            (server_get_control_block_dir, ":server_control_block_dir"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_control_block_dir, ":server_control_block_dir"),
            (server_get_combat_speed, ":server_combat_speed"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_combat_speed, ":server_combat_speed"),
            (server_get_add_to_game_servers_list, ":server_add_to_servers_list"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_add_to_servers_list, ":server_add_to_servers_list"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_player_respawn_as_bot, "$g_multiplayer_player_respawn_as_bot"),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_valid_vote_ratio, "$g_multiplayer_valid_vote_ratio"),
            (str_store_server_name, s0),
            (multiplayer_send_string_to_player, ":player_no", multiplayer_event_return_server_name, s0),
            (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_team_faction, 1, "$coop_team_1_faction"),
            (multiplayer_send_3_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_team_faction, 2, "$coop_team_2_faction"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_spawn_formation, "$coop_battle_spawn_formation"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_battle_size, "$coop_battle_size"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_game_type, "$g_multiplayer_game_type"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_castle_party, "$coop_map_party"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_battle_scene, "$coop_battle_scene"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_disable_inventory, "$coop_disable_inventory"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_return_reduce_damage, "$coop_reduce_damage"),
      ]),


#script_coop_player_access_inventory
  # Input: arg1 = player_agent
  # Output: none
  ("coop_player_access_inventory",
    [
     (store_script_param, ":player_agent", 1),
        (try_begin),
          (eq, "$coop_disable_inventory", 0),#inventory access is optional
          (agent_get_player_id,":player_no",":player_agent"),#only let troops from main party use box
          (agent_get_troop_id,":player_troop", ":player_agent"),
          (agent_get_slot, ":player_agent_party",":player_agent", "slot_agent_coop_spawn_party"), #SP party
          (eq, ":player_agent_party", "$coop_main_party_spawn"),
          (troop_is_hero, ":player_troop"),
          
          #first add agent items to troop
          (call_script, "script_coop_player_agent_save_items", ":player_agent"),

          #then send what troop has
          (try_for_range, ":slot", 0, 9),
            (troop_get_inventory_slot, ":player_cur_item", ":player_troop", ":slot"),
            (troop_get_inventory_slot_modifier, ":player_cur_imod", ":player_troop", ":slot"),
            (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_inv_troop_set_slot, ":slot", ":player_cur_item", ":player_cur_imod"),
          (try_end),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_prsnt_coop_item_select), #done
        (try_end),

      ]),

#NEW
#script_coop_player_agent_save_items
  # Input: arg1 = player_agent
  # Output: none
  ("coop_player_agent_save_items",
    [
     (store_script_param, ":player_agent", 1),
      (agent_get_troop_id, ":agent_troop_id", ":player_agent"),
      #store items from agents
      (try_begin), 
        (neg|is_vanilla_warband),
        (try_for_range, ":slot", 0, 4), #only check weapons
          (agent_get_item_slot, ":agent_item_id", ":player_agent", ":slot"), 
          (agent_get_item_slot_modifier, ":agent_imod", ":player_agent", ":slot"),
          (troop_set_inventory_slot, ":agent_troop_id", ":slot", ":agent_item_id"),
          (troop_set_inventory_slot_modifier, ":agent_troop_id", ":slot", ":agent_imod"),
        (try_end),
      (try_end),
      ]),



#ITEM BUG WORKAROUND BEGIN#####################################################
# these scripts avoid a bug that removes ranged weapons when certain thrown weapons are equiped
#script_coop_equip_player_agent
  # Input: arg1 = player_agent
  # Output: none
  ("coop_equip_player_agent",
    [
     (store_script_param, ":player_agent", 1),
        (try_begin),
          (agent_get_troop_id,":cur_troop", ":player_agent"),
          (troop_is_hero, ":cur_troop"),
          (troop_slot_eq, ":cur_troop", 19, 1), 

          (try_for_range, ":slot", 0, 4), #only check weapons
            (store_add, ":itm_slot", ":slot", 20),
            (troop_get_slot, ":item", ":cur_troop", ":itm_slot"), 
            (troop_set_inventory_slot, ":cur_troop", ":slot", ":item"),

            (store_add, ":imod_slot", ":slot", 30),
            (troop_get_slot, ":imod", ":cur_troop", ":imod_slot"), 
            (troop_set_inventory_slot_modifier, ":cur_troop", ":slot", ":imod"),
            (agent_set_item_slot, ":player_agent", ":slot", ":item", ":imod"),#NEW
          (try_end),
        (try_end),
      ]),
#script_coop_check_item_bug
  ("coop_check_item_bug",
    [
     (store_script_param, ":troop_id", 1),
      (try_begin),
        (troop_is_hero, ":troop_id"),
        (try_for_range, ":slot", 19, 34), #clear slots here
          (troop_set_slot, ":troop_id", ":slot", 0), 
        (try_end),
        (assign, ":has_throw",0),
        (assign, ":has_ranged",0),

        (try_for_range, ":slot", 0, 4), #weapon slots
          (troop_get_inventory_slot, ":item", ":troop_id", ":slot"),
          (troop_get_inventory_slot_modifier, ":imod", ":troop_id", ":slot"),
          (gt, ":item", 0),
          (store_add, ":itm_slot", ":slot", 20),
          (store_add, ":imod_slot", ":slot", 30),
          (troop_set_slot, ":troop_id", ":itm_slot", ":item"), 
          (troop_set_slot, ":troop_id", ":imod_slot", ":imod"), 
          (item_get_type, ":type", ":item"),
          (try_begin),
            (eq, ":type", itp_type_thrown),
            (assign, ":has_throw", 1),
          (else_try),
            (this_or_next|eq, ":type", itp_type_pistol),
            (this_or_next|eq, ":type", itp_type_musket),
            (this_or_next|eq, ":type", itp_type_bow),
            (eq, ":type", itp_type_crossbow),
            (assign, ":has_ranged",1),
          (try_end),
        (try_end),
        (eq, ":has_throw", 1),
        (eq, ":has_ranged", 1),
        (troop_set_slot, ":troop_id", 19, 1), #troop has thrown and ranged
      (try_end),
      ]),
#ITEM BUG WORKAROUND END#####################################################



  #script_coop_display_available_items_from_inventory
  # Input: arg1 = troop_no, arg2 = item_classes_begin, arg3 = item_classes_end, arg4 = pos_x_begin, arg5 = pos_y_begin
  # Output: none
  ("coop_display_available_items_from_inventory",
   [
     #sorting
      (store_add, ":item_slots_end", "$coop_num_available_items", multi_data_item_button_indices_begin),
     (store_sub, ":item_slots_end_minus_one", ":item_slots_end", 1),
     (try_for_range, ":cur_slot", multi_data_item_button_indices_begin, ":item_slots_end_minus_one"),
       (store_add, ":cur_slot_2_begin", ":cur_slot", 1),
       (try_for_range, ":cur_slot_2", ":cur_slot_2_begin", ":item_slots_end"),
         (troop_get_slot, ":item_1", "trp_multiplayer_data", ":cur_slot"),
         (troop_get_slot, ":item_2", "trp_multiplayer_data", ":cur_slot_2"),

         (store_item_value, ":item_1_point", ":item_1"),
         (store_item_value, ":item_2_point", ":item_2"),
         (item_get_type, ":item_1_class", ":item_1"),
         (item_get_type, ":item_2_class", ":item_2"),

         (try_begin),
           (eq, ":item_1_class", 7),
           (assign, ":item_1_class", 12),
         (try_end),
         (try_begin),
           (eq, ":item_2_class", 7),
           (assign, ":item_2_class", 12),
         (try_end),

         (val_mul, ":item_1_class", 1000000), #assuming maximum item price is 1000000
         (val_mul, ":item_2_class", 1000000), #assuming maximum item price is 1000000
         (val_sub, ":item_1_point", ":item_1_class"),
         (val_sub, ":item_2_point", ":item_2_class"),

         (gt, ":item_2_point", ":item_1_point"),
         (troop_set_slot, "trp_multiplayer_data", ":cur_slot", ":item_2"),
         (troop_set_slot, "trp_multiplayer_data", ":cur_slot_2", ":item_1"),

         (troop_get_slot, ":inv_slot_1", "trp_temp_troop", ":cur_slot"), #also sort other data slots
         (troop_get_slot, ":inv_slot_2", "trp_temp_troop", ":cur_slot_2"),
         (troop_set_slot, "trp_temp_troop", ":cur_slot", ":inv_slot_2"),
         (troop_set_slot, "trp_temp_troop", ":cur_slot_2", ":inv_slot_1"),

         (store_add, ":imod_slot", ":cur_slot", 100),
         (store_add, ":imod_slot_2", ":cur_slot_2", 100),
         (troop_get_slot, ":imod_1", "trp_temp_troop", ":imod_slot"),
         (troop_get_slot, ":imod_2", "trp_temp_troop", ":imod_slot_2"),
         (troop_set_slot, "trp_temp_troop", ":imod_slot", ":imod_2"),
         (troop_set_slot, "trp_temp_troop", ":imod_slot_2", ":imod_1"),

       (try_end),
     (try_end),

      (str_clear, s0),
      (create_text_overlay, reg0, s0, tf_scrollable_style_2),
      (position_set_x, pos1, 200),#260
      (position_set_y, pos1, 75),
      (overlay_set_position, reg0, pos1),
      (position_set_x, pos1, 604),
      (position_set_y, pos1, 604),
      (overlay_set_area_size, reg0, pos1),
      (set_container_overlay, reg0),

     (assign, ":x_adder", 100),
     (assign, ":pos_x_begin", 0),
     (store_sub, ":pos_y_begin", "$coop_num_available_items", 1),  #number of items / 6 = number of rows
     (val_div, ":pos_y_begin", 6),
     (val_mul, ":pos_y_begin", 100),
     (val_add, ":pos_y_begin", 10),

     (assign, ":cur_x", ":pos_x_begin"),
     (assign, ":cur_y", ":pos_y_begin"),
     (try_for_range, ":cur_slot", multi_data_item_button_indices_begin, ":item_slots_end"),
       (troop_get_slot, ":item_no", "trp_multiplayer_data", ":cur_slot"),

       (create_image_button_overlay, ":cur_obj", "mesh_mp_inventory_choose", "mesh_mp_inventory_choose"),
       (position_set_x, pos1, 800),#800
       (position_set_y, pos1, 800),#800
       (overlay_set_size, ":cur_obj", pos1),
       (position_set_x, pos1, ":cur_x"),
       (position_set_y, pos1, ":cur_y"),
       (overlay_set_position, ":cur_obj", pos1),
       (create_mesh_overlay_with_item_id, reg0, ":item_no"),
       (store_add, ":item_x", ":cur_x", 50),
       (store_add, ":item_y", ":cur_y", 50),
       (position_set_x, pos1, ":item_x"),
       (position_set_y, pos1, ":item_y"),
       (overlay_set_position, reg0, pos1),

       (val_add, ":cur_x", ":x_adder"),
       (try_begin),
         (gt, ":cur_x", 500),
         (val_sub, ":cur_y", 100),
         (assign, ":cur_x", ":pos_x_begin"),
       (try_end),
     (try_end),
     ]),



  #script_coop_move_belfries_to_their_first_entry_point
  # INPUT: none
  # OUTPUT: none
  ("coop_move_belfries_to_their_first_entry_point",
   [
    (store_script_param, ":belfry_body_scene_prop", 1),
     
    (set_fixed_point_multiplier, 100),    
    (scene_prop_get_num_instances, ":num_belfries", ":belfry_body_scene_prop"),
    
    (try_for_range, ":belfry_no", 0, ":num_belfries"),
      #belfry 
      (scene_prop_get_instance, ":belfry_scene_prop_id", ":belfry_body_scene_prop", ":belfry_no"),
      (prop_instance_get_position, pos0, ":belfry_scene_prop_id"),

      (try_begin),
        (eq, ":belfry_body_scene_prop", "spr_belfry_a"),
        #belfry platform_a
        (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
        #belfry platform_b
        (scene_prop_get_instance, ":belfry_platform_b_scene_prop_id", "spr_belfry_platform_b", ":belfry_no"),
      (else_try),
        #belfry platform_a
        (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
      (try_end),
    
      #belfry wheel_1
      (store_mul, ":wheel_no", ":belfry_no", 3),
      (try_begin),
        (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
        (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),    
        (store_mul, ":number_of_belfry_a_wheels", ":number_of_belfry_a", 3),
        (val_add, ":wheel_no", ":number_of_belfry_a_wheels"),
      (try_end),    
      (scene_prop_get_instance, ":belfry_wheel_1_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
      #belfry wheel_2
      (val_add, ":wheel_no", 1),
      (scene_prop_get_instance, ":belfry_wheel_2_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
      #belfry wheel_3
      (val_add, ":wheel_no", 1),
      (scene_prop_get_instance, ":belfry_wheel_3_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),


#      (store_add, ":belfry_first_entry_point_id", 11, ":belfry_no"), #belfry entry points are 110..119 and 120..129 and 130..139
      (store_add, ":belfry_first_entry_point_id", 5, ":belfry_no"), #belfry entry points are 110..119 and 120..129 and 130..139


      (try_begin),
        (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
        (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),
        (val_add, ":belfry_first_entry_point_id", ":number_of_belfry_a"),
      (try_end),    
      (val_mul, ":belfry_first_entry_point_id", 10),
      (entry_point_get_position, pos1, ":belfry_first_entry_point_id"),

      #this code block is taken from .module_mission_templates.py (multiplayer_server_check_belfry_movement)
      #up down rotation of belfry's next entry point
      (init_position, pos9),
      (position_set_y, pos9, -500), #go 5.0 meters back
      (position_set_x, pos9, -300), #go 3.0 meters left
      (position_transform_position_to_parent, pos10, pos1, pos9), 
      (position_get_distance_to_terrain, ":height_to_terrain_1", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at left part of belfry

      (init_position, pos9),
      (position_set_y, pos9, -500), #go 5.0 meters back
      (position_set_x, pos9, 300), #go 3.0 meters right
      (position_transform_position_to_parent, pos10, pos1, pos9), 
      (position_get_distance_to_terrain, ":height_to_terrain_2", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at right part of belfry

      (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),
      (val_mul, ":height_to_terrain", 100), #because of fixed point multiplier

      (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 2 degrees. #ac sonra
      (init_position, pos20),    
      (position_rotate_x_floating, pos20, ":rotate_angle_of_next_entry_point"),
      (position_transform_position_to_parent, pos23, pos1, pos20),

      #right left rotation of belfry's next entry point
      (init_position, pos9),
      (position_set_x, pos9, -300), #go 3.0 meters left
      (position_transform_position_to_parent, pos10, pos1, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
      (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
      (init_position, pos9),
      (position_set_x, pos9, 300), #go 3.0 meters left
      (position_transform_position_to_parent, pos10, pos1, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
      (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
      (store_sub, ":height_to_terrain_1", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

      (init_position, pos9),
      (position_set_x, pos9, -300), #go 3.0 meters left
      (position_set_y, pos9, -500), #go 5.0 meters forward
      (position_transform_position_to_parent, pos10, pos1, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
      (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
      (init_position, pos9),
      (position_set_x, pos9, 300), #go 3.0 meters left
      (position_set_y, pos9, -500), #go 5.0 meters forward
      (position_transform_position_to_parent, pos10, pos1, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
      (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
      (store_sub, ":height_to_terrain_2", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

      (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),    
      (val_mul, ":height_to_terrain", 100), #100 is because of fixed_point_multiplier
      (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 25 degrees. 
      (val_mul, ":rotate_angle_of_next_entry_point", -1),

      (init_position, pos20),
      (position_rotate_y_floating, pos20, ":rotate_angle_of_next_entry_point"),
      (position_transform_position_to_parent, pos22, pos23, pos20),

      (copy_position, pos1, pos22),
      #end of code block

      #belfry 
      (prop_instance_stop_animating, ":belfry_scene_prop_id"),
      (prop_instance_set_position, ":belfry_scene_prop_id", pos1),
      # (prop_instance_animate_to_position, ":belfry_scene_prop_id", pos1,1), #NEW
    
      #belfry platforms
      (try_begin),
        (eq, ":belfry_body_scene_prop", "spr_belfry_a"),

        #belfry platform_a
        (prop_instance_get_position, pos6, ":belfry_platform_a_scene_prop_id"),
        (position_transform_position_to_local, pos7, pos0, pos6),
        (position_transform_position_to_parent, pos8, pos1, pos7),
        (try_begin),
          (neg|scene_prop_slot_eq, ":belfry_scene_prop_id", "slot_scene_prop_belfry_platform_moved", 0),
     
          (init_position, pos20),
          (position_rotate_x, pos20, 90),
          (position_transform_position_to_parent, pos8, pos8, pos20),
        (try_end),
        (prop_instance_stop_animating, ":belfry_platform_a_scene_prop_id"),
        # (prop_instance_set_position, ":belfry_platform_a_scene_prop_id", pos8),  
        (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos8,1), #NEW
        #belfry platform_b
        (prop_instance_get_position, pos6, ":belfry_platform_b_scene_prop_id"),
        (position_transform_position_to_local, pos7, pos0, pos6),
        (position_transform_position_to_parent, pos8, pos1, pos7),
        (prop_instance_stop_animating, ":belfry_platform_b_scene_prop_id"),
        # (prop_instance_set_position, ":belfry_platform_b_scene_prop_id", pos8),
      (prop_instance_animate_to_position, ":belfry_platform_b_scene_prop_id", pos8,1), #NEW
      (else_try),
        #belfry platform_a
        (prop_instance_get_position, pos6, ":belfry_platform_a_scene_prop_id"),
        (position_transform_position_to_local, pos7, pos0, pos6),
        (position_transform_position_to_parent, pos8, pos1, pos7),
        (try_begin),
          (neg|scene_prop_slot_eq, ":belfry_scene_prop_id", "slot_scene_prop_belfry_platform_moved", 0),
     
          (init_position, pos20),
          (position_rotate_x, pos20, 50),
          (position_transform_position_to_parent, pos8, pos8, pos20),
        (try_end),
        (prop_instance_stop_animating, ":belfry_platform_a_scene_prop_id"),
        # (prop_instance_set_position, ":belfry_platform_a_scene_prop_id", pos8),    
      (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos8,1), #NEW
      (try_end),
    
      #belfry wheel_1
      (store_mul, ":wheel_no", ":belfry_no", 3),
      (try_begin),
        (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
        (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),    
        (store_mul, ":number_of_belfry_a_wheels", ":number_of_belfry_a", 3),
        (val_add, ":wheel_no", ":number_of_belfry_a_wheels"),
      (try_end),
      (prop_instance_get_position, pos6, ":belfry_wheel_1_scene_prop_id"),
      (position_transform_position_to_local, pos7, pos0, pos6),
      (position_transform_position_to_parent, pos8, pos1, pos7),
      (prop_instance_stop_animating, ":belfry_wheel_1_scene_prop_id"),
      # (prop_instance_set_position, ":belfry_wheel_1_scene_prop_id", pos8),
      (prop_instance_animate_to_position, ":belfry_wheel_1_scene_prop_id", pos8,1), #NEW
      #belfry wheel_2
      (prop_instance_get_position, pos6, ":belfry_wheel_2_scene_prop_id"),
      (position_transform_position_to_local, pos7, pos0, pos6),
      (position_transform_position_to_parent, pos8, pos1, pos7),
      (prop_instance_stop_animating, ":belfry_wheel_2_scene_prop_id"),
      # (prop_instance_set_position, ":belfry_wheel_2_scene_prop_id", pos8),
      (prop_instance_animate_to_position, ":belfry_wheel_2_scene_prop_id", pos8,1), #NEW
      #belfry wheel_3
      (prop_instance_get_position, pos6, ":belfry_wheel_3_scene_prop_id"),
      (position_transform_position_to_local, pos7, pos0, pos6),
      (position_transform_position_to_parent, pos8, pos1, pos7),
      (prop_instance_stop_animating, ":belfry_wheel_3_scene_prop_id"),
      # (prop_instance_set_position, ":belfry_wheel_3_scene_prop_id", pos8),
      (prop_instance_animate_to_position, ":belfry_wheel_3_scene_prop_id", pos8,1), #NEW
    (try_end),
    ]),


  # script_cf_coop_siege_assign_men_to_belfry
  # Input: none
  # Output: none (required for siege mission templates)
  ("cf_coop_siege_assign_men_to_belfry",
   [
    (store_script_param, ":pos_no", 1),

    (try_begin),
      (lt, "$belfry_positioned", 3),

      (copy_position, pos42, ":pos_no"),
      (assign, ":belfry_num_men", 0),
        (try_for_agents, ":cur_agent"),#count how many targeting belfry
          (agent_is_alive, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (agent_get_team, ":cur_agent_team", ":cur_agent"),
          (eq, "$attacker_team", ":cur_agent_team"),
          # (agent_get_group, ":agent_group", ":cur_agent"),
          # (eq, ":agent_group", -1),#not player commanded
          (try_begin),
            (agent_get_slot, ":x_pos", ":cur_agent", "slot_agent_target_x_pos"),
            (neq, ":x_pos", 0),
            (agent_get_slot, ":y_pos", ":cur_agent", "slot_agent_target_y_pos"),
            (val_add, ":belfry_num_men", 1),
            (init_position, pos41),
            (position_move_x, pos41, ":x_pos"),
            (position_move_y, pos41, ":y_pos"),
            (init_position, pos43),
            (val_mul, ":x_pos", 3),
            (position_move_x, pos43, ":x_pos"),
            (position_move_y, pos43, -1100),
            (position_transform_position_to_parent, pos44, pos42, pos41),
            (position_transform_position_to_parent, pos45, pos42, pos43),
            (agent_get_position, pos46, ":cur_agent"),
            (get_distance_between_positions, ":target_distance", pos46, pos44),
            (get_distance_between_positions, ":waypoint_distance", pos46, pos45),
            (try_begin),
              (this_or_next|lt, ":target_distance", ":waypoint_distance"),
              (lt, ":waypoint_distance", 1600), # > 1/2 pos1 - pos4
              (agent_set_scripted_destination, ":cur_agent", pos44, 1),
            (else_try),
              (agent_set_scripted_destination, ":cur_agent", pos45, 1),
              #(display_message, "@assigned to waypoint"),
            (try_end),

          (try_end),
        (try_end),

      (try_begin),
        (lt, ":belfry_num_men", 20), 
          (try_for_agents, ":cur_agent"), #add more troops if low
            (lt, ":belfry_num_men", 20), #stop adding when max number to push
            (agent_is_alive, ":cur_agent"),
            (agent_get_team, ":cur_agent_team", ":cur_agent"),
            (eq, "$attacker_team", ":cur_agent_team"),
            (agent_get_slot, ":x_pos", ":cur_agent", "slot_agent_target_x_pos"),
            (eq, ":x_pos", 0),
            (assign, ":y_pos", 0),
            (store_random_in_range, ":side", 0, 2),
            (try_begin),
              (eq, ":side", 1),
              (assign, ":x_pos", -400),
            (else_try),
              (assign, ":x_pos", 400),
            (try_end),
            (val_add, ":belfry_num_men", 1),
            (agent_set_slot, ":cur_agent", "slot_agent_target_x_pos", ":x_pos"),
            (agent_set_slot, ":cur_agent", "slot_agent_target_y_pos", ":y_pos"),
          (try_end),
      (try_end),
    # (else_try), #we already clear scripted in mission template
      # (try_for_agents, ":cur_agent"),
        # (agent_get_team, ":cur_agent_team", ":cur_agent"),
        # (eq, "$attacker_team", ":cur_agent_team"),
        # (agent_clear_scripted_mode, ":cur_agent"),
      # (try_end),
    (try_end),

  ]),

######## 	
  # script_coop_spawn_formation
  # Input: arg1 = agent_no
  # Output: none
  ("coop_spawn_formation",
    [
      (store_script_param, ":agent_no", 1),
      (try_begin),

        (try_begin),
          (agent_is_human, ":agent_no"), #horse spawns after rider
          (assign, ":human_agent", ":agent_no"), 
        (else_try),
          (agent_get_rider, ":human_agent", ":agent_no"),
        (try_end),

        (agent_get_team, ":agent_team", ":human_agent"),
        (agent_get_division, ":agent_class", ":human_agent"), #agent_get_class only works after horsemen have horses

        (try_begin),
          (neg|agent_is_human, ":agent_no"),
          (assign, ":pos", "$coop_form_line_last_pos"),
        (else_try),
          (eq, ":agent_team", 0),
          (try_begin),
            (eq, ":agent_class", grc_archers),   
            (assign, ":pos", pos25),
            (try_begin),
              (eq, "$coop_form_line_grp_1", 1),  
              (assign, "$coop_form_line_grp_1", 0),    
              (position_move_y, ":pos", -200),
            (else_try),
              (assign, "$coop_form_line_grp_1", 1),   
              (position_move_y, ":pos", 200),
              (position_move_x, ":pos", 100),
            (try_end),
          (else_try),
            (eq, ":agent_class", grc_infantry), 
            (assign, ":pos", pos26), 
            (try_begin),
              (eq, "$coop_form_line_grp_2", 1),  
              (assign, "$coop_form_line_grp_2", 0),    
              (position_move_y, ":pos", -200),
            (else_try),
              (assign, "$coop_form_line_grp_2", 1),   
              (position_move_y, ":pos", 200),
              (position_move_x, ":pos", 100),
            (try_end),
          (else_try),
            (eq, ":agent_class", grc_cavalry),   
            (assign, ":pos", pos27),
            (try_begin),
              (eq, "$coop_form_line_grp_3", 1),  
              (assign, "$coop_form_line_grp_3", 0),    
              (position_move_y, ":pos", -300),
            (else_try),
              (assign, "$coop_form_line_grp_3", 1),   
              (position_move_y, ":pos", 300),
              (position_move_x, ":pos", 100),
            (try_end),
          (try_end),

        (else_try),
          (eq, ":agent_team", 1),
          (try_begin),
            (eq, ":agent_class", grc_archers),   
            (assign, ":pos", pos30),
            (try_begin),
              (eq, "$coop_form_line_grp_4", 1),  
              (assign, "$coop_form_line_grp_4", 0),    
              (position_move_y, ":pos", -200),
            (else_try),
              (assign, "$coop_form_line_grp_4", 1),   
              (position_move_y, ":pos", 200),
              (position_move_x, ":pos", 100),
            (try_end),
          (else_try),
            (eq, ":agent_class", grc_infantry), 
            (assign, ":pos", pos31), 
            (try_begin),
              (eq, "$coop_form_line_grp_5", 1),  
              (assign, "$coop_form_line_grp_5", 0),    
              (position_move_y, ":pos", -200),
            (else_try),
              (assign, "$coop_form_line_grp_5", 1),   
              (position_move_y, ":pos", 200),
              (position_move_x, ":pos", 100),
            (try_end),
          (else_try),
            (eq, ":agent_class", grc_cavalry),  
            (assign, ":pos", pos32),
            (try_begin),
              (eq, "$coop_form_line_grp_6", 1),  
              (assign, "$coop_form_line_grp_6", 0),    
              (position_move_y, ":pos", -300),
            (else_try),
              (assign, "$coop_form_line_grp_6", 1),   
              (position_move_y, ":pos", 300),
              (position_move_x, ":pos", 100),
            (try_end),
          (try_end),
        (try_end),

        # (try_begin),
          # (agent_is_human, ":agent_no"),
          # (position_move_x, ":pos", 100),
        # (try_end),
        (assign, "$coop_form_line_last_pos", ":pos"), #store last pos for horses
        (agent_set_position, ":agent_no", ":pos"),
        (agent_set_scripted_destination, ":agent_no", ":pos", 1),

      (try_end),

      ]),

######## 	
  # script_coop_form_line
  # Input: arg1 = agent_no
  # Output: none
  ("coop_form_line",
    [
      (store_script_param, ":pos_no", 1),
      (store_script_param, ":team", 2),
      (store_script_param, ":class", 3),
      (store_script_param, ":dist_to_next_row", 4),
      (store_script_param, ":dist_to_next_troop", 5),
      (store_script_param, ":num_rows", 6),
      (store_script_param, ":move_to_pos", 7),#set agent at position like spawning

      (store_sub, ":dist_to_first_row", 1, ":num_rows"),
      (val_mul, ":dist_to_first_row", ":dist_to_next_row"),

      (init_position, pos35),
      (copy_position, pos35, ":pos_no"),
      (assign, ":row", 1),
      (try_for_agents, ":agent_no"),
        (agent_is_alive, ":agent_no"),
        (agent_is_human, ":agent_no"),
        (agent_get_team, ":agent_team", ":agent_no"),
        (eq, ":agent_team", ":team"),
        (agent_get_slot, ":x_pos", ":agent_no", "slot_agent_target_x_pos"), #if agent is not pushing belfry
        (eq, ":x_pos", 0),
        # (agent_get_group, ":agent_group", ":agent_no"),
        # (eq, ":agent_group", -1),
        (agent_get_class, ":agent_class", ":agent_no"),
        (this_or_next|eq, ":class", grc_everyone),   
        (eq, ":agent_class", ":class"),   
        (try_begin),
          (eq, ":move_to_pos", 1), #set agent at position like spawning
          (agent_get_horse, ":agent_horse", ":agent_no"),
          (agent_set_position, ":agent_horse", pos35),
          (agent_set_position, ":agent_no", pos35),
        (try_end),
        (agent_set_scripted_destination, ":agent_no", pos35, 1),
        (try_begin),
          (eq, ":row", ":num_rows"),
          (assign, ":row", 1),
          (position_move_x, pos35, ":dist_to_next_troop"),
          (position_move_y, pos35, ":dist_to_first_row"),
        (else_try),
          (position_move_y, pos35, ":dist_to_next_row"),
          (val_add, ":row", 1),
        (try_end),
      (try_end),

      ]),

######## 	all in party doesnot include castle garrison, by type includes allies
  # script_coop_change_leader_of_bot
  # Input: arg1 = agent_no
  # Output: none
  ("coop_change_leader_of_bot",
    [
      (store_script_param, ":agent_no", 1),

      (agent_get_team, ":team_no", ":agent_no"),
      (agent_get_troop_id,":agent_troop", ":agent_no"),
      (troop_get_slot, ":troop_class", ":agent_troop", "slot_troop_current_rumor"), #use to store class in MP (so we dont affect ai classes too)
      # (troop_get_class, ":troop_class", ":agent_troop"),
      (agent_get_class, ":agent_class", ":agent_no"),
      (agent_get_slot, ":agent_party_no",":agent_no", "slot_agent_coop_spawn_party"),# coop party
      (agent_get_group, ":agent_group", ":agent_no"),

      (assign, ":leader_player", -1),
      (get_max_players, ":num_players"),
      (assign, ":end_cond", ":num_players"),
      (try_for_range, ":cur_player", 0, ":end_cond"), #try players till we find one, server gets first pick
        (player_is_active, ":cur_player"),
        (player_get_team_no, ":player_team", ":cur_player"),
        (eq, ":team_no", ":player_team"),
        (player_get_agent_id, ":player_agent", ":cur_player"),
        (ge, ":player_agent", 0),
        (agent_is_alive, ":player_agent"),
        (agent_get_slot, ":player_party_no",":player_agent", "slot_agent_coop_spawn_party"),# coop party

        (try_begin),#check if players party is garrison commander party
          (eq, ":agent_party_no", "$coop_garrison_party"), #if bot is part of garrison
          (eq, ":player_party_no", "$coop_garrison_commander_party"), #and player is commander of garrison
          (assign, ":player_party_no", ":agent_party_no"), #then player is also part of garrison party
        (try_end),
        (eq, ":agent_party_no", ":player_party_no"), #remove this if hero should command troops in other parties
        (try_begin),
          (eq, ":agent_class", grc_infantry),
          (player_get_slot, ":type_2_wanted", ":cur_player", "slot_player_bot_type_2_wanted"),
          (eq, ":type_2_wanted", 1), #player wants type 2
          (assign, ":leader_player", ":cur_player"),
          (assign, ":end_cond", 0),
        (else_try),
          (eq, ":agent_class", grc_archers),
          (player_get_slot, ":type_3_wanted", ":cur_player", "slot_player_bot_type_3_wanted"),
          (eq, ":type_3_wanted", 1), #player wants type 3
          (assign, ":leader_player", ":cur_player"),
          (assign, ":end_cond", 0), 
        (else_try),
          (eq, ":agent_class", grc_cavalry),
          (player_get_slot, ":type_4_wanted", ":cur_player", "slot_player_bot_type_4_wanted"),
          (eq, ":type_4_wanted", 1), #player wants type 4
          (assign, ":leader_player", ":cur_player"),
          (assign, ":end_cond", 0),
        (else_try),

          (eq, ":agent_party_no", "$coop_main_party_spawn"), #if agent is from main party
          (try_begin),
            (eq, ":troop_class", 0),
            (player_get_slot, ":class_0_wanted", ":cur_player", "slot_player_coop_class_0_wanted"),
            (eq, ":class_0_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 1),
            (player_get_slot, ":class_1_wanted", ":cur_player", "slot_player_coop_class_1_wanted"),
            (eq, ":class_1_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 2),
            (player_get_slot, ":class_2_wanted", ":cur_player", "slot_player_coop_class_2_wanted"),
            (eq, ":class_2_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 3),
            (player_get_slot, ":class_3_wanted", ":cur_player", "slot_player_coop_class_3_wanted"),
            (eq, ":class_3_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 4),
            (player_get_slot, ":class_4_wanted", ":cur_player", "slot_player_coop_class_4_wanted"),
            (eq, ":class_4_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 5),
            (player_get_slot, ":class_5_wanted", ":cur_player", "slot_player_coop_class_5_wanted"),
            (eq, ":class_5_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 6),
            (player_get_slot, ":class_6_wanted", ":cur_player", "slot_player_coop_class_6_wanted"),
            (eq, ":class_6_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 7),
            (player_get_slot, ":class_7_wanted", ":cur_player", "slot_player_coop_class_7_wanted"),
            (eq, ":class_7_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (else_try),
            (eq, ":troop_class", 8),
            (player_get_slot, ":class_8_wanted", ":cur_player", "slot_player_coop_class_8_wanted"),
            (eq, ":class_8_wanted", 1),
            (assign, ":leader_player", ":cur_player"),
            (assign, ":end_cond", 0), 
          (try_end),
        (try_end),
      (try_end),

  # if nobody wants agent check for someone who wants all in party
      (try_begin),
        (eq, ":leader_player", -1),
        (get_max_players, ":num_players"),
        (assign, ":end_cond", ":num_players"),
        (try_for_range, ":cur_player", 0, ":end_cond"), #try players till we find one, server gets first pick
          (player_is_active, ":cur_player"),
          (player_get_team_no, ":player_team", ":cur_player"),
          (eq, ":team_no", ":player_team"),
          (player_get_agent_id, ":player_agent", ":cur_player"),
          (ge, ":player_agent", 0),
          (agent_is_alive, ":player_agent"),
          (agent_get_slot, ":player_party_no",":player_agent", "slot_agent_coop_spawn_party"),# coop party
          (try_begin),#check if players party is garrison commander party
            (eq, ":agent_party_no", "$coop_garrison_party"), #if bot is part of garrison
            (eq, ":player_party_no", "$coop_garrison_commander_party"), #and player is commander of garrison
            (assign, ":player_party_no", ":agent_party_no"), #then player is also part of garrison party
          (try_end),
          (eq, ":player_party_no",":agent_party_no"), #remove this if hero should command troops in other parties
          (this_or_next|eq, ":agent_group", -1),#not already commanded
          (eq, ":agent_group", ":cur_player"),#commanded by me
          (player_get_slot, ":type_1_wanted", ":cur_player", "slot_player_bot_type_1_wanted"),
          (eq, ":type_1_wanted", 1), #player wants type 1
          (assign, ":leader_player", ":cur_player"),
          (assign, ":end_cond", 0),
        (try_end),
      (try_end),
      (agent_set_group, ":agent_no", ":leader_player"),

    # (assign, reg13, ":agent_no"), 
    # (str_store_troop_name, s40, ":agent_troop"),
    # (assign, reg10, ":leader_player"), 
    # (assign, reg11, ":team_no"), 
    # (display_message, "@{reg11} leader {reg10} agent{reg13}   {s40}"),


      ]),


#
  # script_coop_find_bot_troop_for_spawn
  # Input: arg1 = team_no
  # Output: reg0 = troop_id, reg1 = group_id
  ("coop_find_bot_troop_for_spawn",
    [
      (store_script_param, ":team_no", 1),


      (assign, ":selected_troop", 0), #if no troop is found (error) spawn trp_player
      (try_begin),	  
        (eq, ":team_no", 0), #enemy team

        (assign, ":end", 40), 
        (try_for_range, ":unused", 0, ":end"),
          (party_stack_get_troop_id, ":selected_troop", "$coop_cur_temp_party_enemy", 0), #get one troop from each party per cycle

          (try_begin),
            (gt, ":selected_troop", 0), 
            (assign, ":party", "$coop_cur_temp_party_enemy"), 
            (party_remove_members, ":party", ":selected_troop", 1),	
            (store_sub, ":slot_pos", ":party", coop_temp_party_enemy_begin), 
            (troop_get_slot, "$coop_agent_banner", "trp_temp_array_a", ":slot_pos"),
            (assign, "$coop_agent_party", ":party"),
            (assign, ":end", 0), 
          (try_end),
          (try_begin),
            (store_add, ":last_party", coop_temp_party_enemy_begin, "$coop_no_enemy_parties"), 
            (val_sub, ":last_party", 1), 
            (eq, "$coop_cur_temp_party_enemy", ":last_party"),
            (assign, "$coop_cur_temp_party_enemy", coop_temp_party_enemy_begin),
          (else_try),
            (val_add, "$coop_cur_temp_party_enemy", 1),
          (try_end),
        (try_end),


      (else_try),
	  	  (eq, ":team_no", 1), #player team + allies

        (assign, ":end", 40), 
        (try_for_range, ":unused", 0, ":end"),
          (party_stack_get_troop_id, ":selected_troop", "$coop_cur_temp_party_ally", 0), #get one troop from each party per cycle
          (try_begin),
            (gt, ":selected_troop", 0), 
            (assign, ":party", "$coop_cur_temp_party_ally"), 
            (party_remove_members, ":party", ":selected_troop", 1),	
            (store_sub, ":slot_pos", ":party", coop_temp_party_ally_begin), 
            (troop_get_slot, "$coop_agent_banner", "trp_temp_array_b", ":slot_pos"),
            (assign, "$coop_agent_party", ":party"),
            (assign, ":end", 0), 
          (try_end),
          (try_begin),
            (store_add, ":last_party", coop_temp_party_ally_begin, "$coop_no_ally_parties"), #= one more than total
            (val_sub, ":last_party", 1), 
            (eq, "$coop_cur_temp_party_ally", ":last_party"),
            (assign, "$coop_cur_temp_party_ally", coop_temp_party_ally_begin),
          (else_try),
            (val_add, "$coop_cur_temp_party_ally", 1),
          (try_end),
        (try_end),

      (try_end), 


      #send banner for troop
      (get_max_players, ":num_players"),
      (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
        (player_is_active, ":player_no"),
        (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_troop_banner, "$coop_agent_banner"),
      (try_end),
      (call_script, "script_coop_check_item_bug", ":selected_troop"), #ITEM BUG WORKAROUND

      #  debug
      # (assign, reg4, "$coop_agent_banner"), 
      # (str_store_troop_name, s41, ":selected_troop"),
      # (assign, reg6, ":party"), 
      # (display_message, "@spawn {s41} from party {reg6} banner {reg4}"),

      (assign, reg0, ":selected_troop"),
    ]),	


  
    # 
   # script_coop_server_on_agent_killed_or_wounded_common
  # Input: arg1 = dead_agent_no
  ("coop_server_on_agent_killed_or_wounded_common",
   [
    (store_script_param, ":dead_agent_no", 1),
    (store_script_param, ":killer_agent_no", 2),

    (try_begin),
      (ge, ":dead_agent_no", 0),
      (ge, ":killer_agent_no", 0),
      (agent_is_human, ":dead_agent_no"),
      #(agent_is_human, ":killer_agent_no"), #comment if horse can kill human?
      (agent_get_troop_id, ":killer_troop_id", ":killer_agent_no"),
      (agent_get_troop_id, ":dead_troop_id", ":dead_agent_no"),
      (agent_get_team, ":dead_agent_team", ":dead_agent_no"),

      #xp function = (x*x/10 + x*2 + 10)* 2
      (store_character_level,":dead_troop_level",":dead_troop_id"),
      (store_mul, ":xp_gain", ":dead_troop_level", ":dead_troop_level"), 
      (val_div, ":xp_gain", 10), 
      (val_add, ":xp_gain", ":dead_troop_level"),
      (val_add, ":xp_gain", ":dead_troop_level"),
      (val_add, ":xp_gain", 10),
      (val_mul, ":xp_gain", 2),

      #xp message
      (try_begin),
        (eq, ":killer_troop_id", "$coop_my_troop_no"),
        (troop_is_hero, ":killer_troop_id"),
        (eq, "$coop_toggle_messages", 0),
        (assign, reg1, ":xp_gain"), 
        (display_message, "@You got {reg1} experience."),
      (try_end), 

      (try_begin),
        (troop_is_hero, ":dead_troop_id"),
        (try_begin),
          (eq, ":dead_agent_team", 0),
          (party_remove_members, coop_temp_party_enemy_heroes, ":dead_troop_id", 1),	
        (else_try),
          (eq, ":dead_agent_team", 1),
          (party_remove_members, coop_temp_party_ally_heroes, ":dead_troop_id", 1),
        (try_end),
      (try_end),

#only server continue
      (multiplayer_is_server),
      (agent_get_slot, ":killer_agent_party",":killer_agent_no", "slot_agent_coop_spawn_party"), #"slot_agent_coop_spawn_party" = SP party
      (agent_get_slot, ":dead_agent_party",":dead_agent_no", "slot_agent_coop_spawn_party"), #"slot_agent_coop_spawn_party" = SP party

      (try_begin),
        (eq, ":dead_agent_team", 0),
        (store_sub, ":casualties_party", ":dead_agent_party", coop_temp_party_enemy_begin),
        (val_add, ":casualties_party", coop_temp_casualties_enemy_begin),
      (else_try),
        (eq, ":dead_agent_team", 1),
        (store_sub, ":casualties_party", ":dead_agent_party", coop_temp_party_ally_begin),
        (val_add, ":casualties_party", coop_temp_casualties_ally_begin),
      (try_end),

      (try_begin), #store xp earned from kill for regular troops (heros copy directly from troop stats)
        (eq, ":killer_agent_party", "$coop_main_party_spawn"),
        (neg|troop_is_hero,":killer_troop_id"),#only regular troops in main party
        (store_mul, ":xp_for_regulars", ":xp_gain", 71), #regular troops get 71% of heroes
        (val_div, ":xp_for_regulars", 100),
        (troop_get_slot, ":temp_xp", ":killer_troop_id", "slot_troop_temp_slot"),
        (store_add, ":new_xp", ":temp_xp", ":xp_for_regulars"),
        (troop_set_slot, ":killer_troop_id", "slot_troop_temp_slot", ":new_xp"),
      (try_end), 

      (party_add_members, ":casualties_party", ":dead_troop_id", 1),
      (try_begin),
        (this_or_next|troop_is_hero,":dead_troop_id"),
        (agent_is_wounded, ":dead_agent_no"),
        (party_wound_members, ":casualties_party", ":dead_troop_id", 1),
      (try_end),

      (try_begin), #save hit points for dead heroes (15% of pre battle health)
        (troop_is_hero, ":dead_troop_id"),   
        (store_troop_health, ":old_health", ":dead_troop_id"),
        (val_div, ":old_health", 6),
        (troop_set_health, ":dead_troop_id", ":old_health"),
      (try_end), 

#moved from multiplayer_server_on_agent_killed_or_wounded_common for this game type only
      (agent_get_player_id, ":dead_player_no", ":dead_agent_no"),
      (try_begin),
        (ge, ":dead_player_no", 0),
        (player_is_active, ":dead_player_no"),
        (neg|agent_is_non_player, ":dead_agent_no"), #dead agent was player    
        (try_for_agents, ":cur_agent"),
          (agent_is_non_player, ":cur_agent"), #agent is bot
          (agent_is_human, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (agent_get_group, ":agent_group", ":cur_agent"),
          (try_begin),
            (eq, ":dead_player_no", ":agent_group"),
            (agent_set_group, ":cur_agent", -1),                 
          (try_end),
        (try_end),
      (try_end),
    (try_end),  


#SERVER BUG WORKAROUND BEGIN ################################################################
    (try_begin), #do this so client doesnt crash when rejoining, remove weapons from agent when his player quits
      (ge, ":dead_agent_no", 0),
      (lt, ":killer_agent_no", 0),
      (agent_is_human, ":dead_agent_no"),
      (try_for_range, ":slot", 0, 8),
        (agent_get_item_slot, ":cur_item", ":dead_agent_no", ":slot"), 
        (ge, ":cur_item", 0),
        (agent_unequip_item,":dead_agent_no",":cur_item"),
      (try_end),
      (remove_agent, ":dead_agent_no"),
    (try_end), 
#SERVER BUG WORKAROUND END ################################################################
   ]),	

  # 
  # script_coop_sort_party
  # copies heroes first then troops to p_temp_party, and copies back to original party
  # Input: arg1 = dead_agent_no
  ("coop_sort_party",
   [
    (store_script_param, ":party_no", 1),
 

        (party_clear, "p_temp_party"), 
        (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
        (try_for_range, ":stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop",":party_no",":stack"),	
	        (troop_is_hero, ":stack_troop"),
          (party_stack_get_size, ":stack_size", ":party_no", ":stack"),
          (party_add_members, "p_temp_party", ":stack_troop", ":stack_size"),
        (try_end),

        (try_for_range, ":stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", ":party_no", ":stack"),	
	        (neg|troop_is_hero, ":stack_troop"),
          (party_stack_get_size, ":stack_size", ":party_no", ":stack"),
          (party_add_members, "p_temp_party", ":stack_troop", ":stack_size"),
        (try_end),


		    (party_clear, ":party_no"), 
        (party_get_num_companion_stacks, ":num_stacks", "p_temp_party"),
        (try_for_range, ":stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", "p_temp_party", ":stack"),	
          (party_stack_get_size, ":stack_size", "p_temp_party", ":stack"),
          (party_add_members, ":party_no", ":stack_troop", ":stack_size"),
        (try_end),

   ]),	



###### DATA SCRIPTS ##########################################################################################################

   # 
  # used to copy parties from SP to registers and temp casualty parties from MP to registers 
  # script_coop_copy_parties_to_file_sp
  # Input: arg1 = party_no
  ("coop_copy_parties_to_file_sp",
   [
    (try_begin), 
      (neg|is_vanilla_warband),
        (dict_create, "$coop_dict"),
        (dict_save, "$coop_dict", "@coop_battle"), #clear battle file

        (dict_set_int, "$coop_dict", "@battle_state", coop_battle_state_setup_sp),

        (call_script, "script_coop_copy_settings_to_file"),	#copy game settings here

#SP ONLY MISC DATA

      #store scene
      (assign, ":scene_to_use", 0),
      (assign, ":scene_castle", 0),
      (assign, ":scene_street", 0),
      (assign, ":scene_party", 0),
      (assign, ":encountered_party", "$g_encountered_party"),

      (try_begin),
        (this_or_next|eq, "$coop_battle_type", coop_battle_type_siege_player_defend),
        (eq, "$coop_battle_type", coop_battle_type_siege_player_attack),
        (try_begin),
          (party_slot_eq, ":encountered_party", "slot_party_type", spt_town),
          (party_get_slot, ":scene_to_use", ":encountered_party", "slot_town_walls"),
          (party_get_slot, ":scene_castle", ":encountered_party", "slot_town_castle"),
          (party_get_slot, ":scene_street", ":encountered_party", "slot_town_center"),
          (assign, ":scene_party", ":encountered_party"),
        (else_try),
          (party_slot_eq, ":encountered_party", "slot_party_type", spt_castle),
          (party_get_slot, ":scene_to_use", ":encountered_party", "slot_castle_exterior"),
          (party_get_slot, ":scene_castle", ":encountered_party", "slot_town_castle"),
          (assign, ":scene_party", ":encountered_party"),
        (try_end),

      (else_try),
        (this_or_next|eq, "$coop_battle_type", coop_battle_type_village_player_attack),
        (eq, "$coop_battle_type", coop_battle_type_village_player_defend),
        (try_begin),
          (party_slot_eq, ":encountered_party", "slot_party_type", spt_village),
          (party_get_slot, ":scene_to_use", ":encountered_party", "slot_castle_exterior"),
          (assign, ":scene_party", ":encountered_party"),
        (else_try),
          (assign, ":encountered_party", "$g_encounter_is_in_village"),
          (party_get_slot, ":scene_to_use", ":encountered_party", "slot_castle_exterior"),
          (assign, ":scene_party", ":encountered_party"),
        (try_end),

      (else_try),
        (eq, "$coop_battle_type", coop_battle_type_bandit_lair),
        (party_slot_eq, ":encountered_party", "slot_party_type", spt_bandit_lair),
        (party_stack_get_troop_id, ":bandit_type", "$g_encountered_party", 0),
        (try_begin),
          (eq, ":bandit_type", "trp_desert_bandit"),
          (assign, ":scene_to_use", "scn_lair_desert_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_mountain_bandit"),
          (assign, ":scene_to_use", "scn_lair_mountain_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_forest_bandit"),
          (assign, ":scene_to_use", "scn_lair_forest_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_taiga_bandit"),
          (assign, ":scene_to_use", "scn_lair_taiga_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_steppe_bandit"),
          (assign, ":scene_to_use", "scn_lair_steppe_bandits"),
        (else_try),
          (eq, ":bandit_type", "trp_sea_raider"),
          (assign, ":scene_to_use", "scn_lair_sea_raiders"),
        (else_try), #chief anade
          (assign, ":scene_to_use", "scn_lair_sea_raiders"),
        (try_end),

      (else_try),
         #if field battle or we did not find one
        (party_get_current_terrain, ":terrain_type", "p_main_party"),
        (assign, ":scene_to_use", "scn_coop_random_med_plain"),
        (assign, ":scene_to_use_large", "scn_coop_random_lrg_plain"),
        (try_begin),
          (eq, ":terrain_type", rt_steppe),
          (assign, ":scene_to_use", "scn_coop_random_med_steppe"),
          (assign, ":scene_to_use_large", "scn_coop_random_lrg_steppe"),
        (else_try),
          (eq, ":terrain_type", rt_plain),
          (assign, ":scene_to_use", "scn_coop_random_med_plain"),
          (assign, ":scene_to_use_large", "scn_coop_random_lrg_plain"),
        (else_try),
          (eq, ":terrain_type", rt_snow),
          (assign, ":scene_to_use", "scn_coop_random_med_snow"),
          (assign, ":scene_to_use_large", "scn_coop_random_lrg_snow"),
        (else_try),
          (eq, ":terrain_type", rt_desert),
          (assign, ":scene_to_use", "scn_coop_random_med_desert"),
          (assign, ":scene_to_use_large", "scn_coop_random_lrg_desert"),
        (else_try),
          (eq, ":terrain_type", rt_steppe_forest),
          (assign, ":scene_to_use", "scn_coop_random_med_steppe_forest"),
          (assign, ":scene_to_use_large", "scn_coop_random_lrg_steppe_forest"),
        (else_try),
          (eq, ":terrain_type", rt_forest),
          (assign, ":scene_to_use", "scn_coop_random_med_plain_forest"),
          (assign, ":scene_to_use_large", "scn_coop_random_lrg_plain_forest"),
        (else_try),
          (eq, ":terrain_type", rt_snow_forest),
          (assign, ":scene_to_use", "scn_coop_random_med_snow_forest"),
          (assign, ":scene_to_use_large", "scn_coop_random_lrg_snow_forest"),
        (else_try),
          (eq, ":terrain_type", rt_desert_forest),
          (assign, ":scene_to_use", "scn_coop_random_med_desert_forest"),
          (assign, ":scene_to_use_large", "scn_coop_random_lrg_desert_forest"),
        (else_try),
          (eq, ":terrain_type", rt_water),
          (assign, ":scene_to_use", "scn_water"),
        (try_end),

        (try_begin),
          (store_add, ":total_fit_for_battle", "$g_enemy_fit_for_battle", "$g_friend_fit_for_battle"), #get number of troops for large or medium scene size
          (gt, ":total_fit_for_battle", 80),
          (assign, ":scene_to_use", ":scene_to_use_large"), #switch to larger scene 
        (try_end),
      (try_end),

      (dict_set_int, "$coop_dict", "@map_type", "$coop_battle_type"),
      (dict_set_int, "$coop_dict", "@map_scn", ":scene_to_use"),
      (dict_set_int, "$coop_dict", "@map_castle", ":scene_castle"),
      (dict_set_int, "$coop_dict", "@map_street", ":scene_street"),
      (dict_set_int, "$coop_dict", "@map_party_id", ":scene_party"),


      #find which party is castle garrison and which party is commander of garrison
      (dict_set_int, "$coop_dict", "@p_castle_lord", -1), #store null (0 could be a valid number for this variable)
      (assign, ":garrison_lord_party", -1),
      (try_begin), 
        (this_or_next|party_slot_eq, ":encountered_party", "slot_party_type", spt_village),
        (this_or_next|party_slot_eq, ":encountered_party", "slot_party_type", spt_town),
        (party_slot_eq, ":encountered_party", "slot_party_type", spt_castle),
        (party_get_slot, ":cur_leader", ":encountered_party", "slot_town_lord"),
        (ge, ":cur_leader", 0),
        (troop_get_slot, ":lord_party", ":cur_leader", "slot_troop_leaded_party"),
        (ge, ":lord_party", 0),
        (assign, ":garrison_lord_party", ":lord_party"),
      (try_end),


      #decide weather
      (party_get_current_terrain, ":terrain_type", "p_main_party"),
      (try_begin),
        (this_or_next|eq, ":terrain_type", rt_plain),
        (this_or_next|eq, ":terrain_type", rt_steppe_forest),
        (this_or_next|eq, ":terrain_type", rt_forest),
        (this_or_next|eq, ":terrain_type", rt_water),
        (this_or_next|eq, ":terrain_type", rt_bridge),
        (eq, ":terrain_type", rt_steppe),

        (assign, ":rain", 1),
      (else_try),
        (this_or_next|eq, ":terrain_type", rt_snow_forest),
        (eq, ":terrain_type", rt_snow),

        (assign, ":rain", 2),
      (else_try),        
        (this_or_next|eq, ":terrain_type", rt_desert_forest),
        (eq, ":terrain_type", rt_desert),

        (assign, ":rain", 0),
      (try_end),

      (store_time_of_day, ":time"),
	    (get_global_cloud_amount, ":cloud"),
	    (get_global_haze_amount, ":haze"),
      (dict_set_int, "$coop_dict", "@map_time", ":time"),
      (dict_set_int, "$coop_dict", "@map_cloud", ":cloud"),
      (dict_set_int, "$coop_dict", "@map_haze", ":haze"),
      (dict_set_int, "$coop_dict", "@map_rain", ":rain"),



      (call_script, "script_calculate_battle_advantage"),
           # (val_mul, reg0, 2),
           # (val_div, reg0, 3), #scale down the advantage a bit in sieges.
      (dict_set_int, "$coop_dict", "@battle_adv", reg0),



      #store faction of parties
      (store_faction_of_party, ":team_faction", "$coop_encountered_party"),
      (dict_set_int, "$coop_dict", "@tm0_fac", ":team_faction"),


      (try_begin),
        (gt, "$g_ally_party", 0),
        (store_faction_of_party, ":team_faction", "$g_ally_party"),
      (else_try),
        (gt, "$players_kingdom", 0),
        (assign, ":team_faction", "$players_kingdom"),
      (else_try),
        (assign, ":team_faction", "fac_player_faction"),
      (try_end),
      (dict_set_int, "$coop_dict", "@tm1_fac", ":team_faction"),

      (str_store_faction_name, s0, "$players_kingdom"),
      (dict_set_str, "$coop_dict", "@tm1_name", s0),

      (try_for_range, reg1, 0, 9),
        (str_store_class_name, s0, reg1), #(str_store_class_name,<string_register>,<class_id>)
        (dict_set_str, "$coop_dict", "@cls{reg1}_name", s0),
      (try_end),


##COPY PARTIES TO REG##


#ADD ENEMY PARTIES

    (assign, reg22, 0), #count heroes

    (party_get_num_attached_parties, ":no_enemy_parties", "$coop_encountered_party"),
    (val_add, ":no_enemy_parties", 1), 
    (dict_set_int, "$coop_dict", "@num_parties_enemy", ":no_enemy_parties"),

    (try_for_range, reg20, 0, ":no_enemy_parties"),
      (try_begin),
        (eq, reg20, 0),#first party
        (assign, ":party_no", "$coop_encountered_party"),
      (else_try),
        (store_sub, ":attached_party_rank", reg20, 1), #sub 1 so rank starts from 0
        (party_get_attached_party_with_rank, ":party_no", "$coop_encountered_party", ":attached_party_rank"),
      (try_end),

      (assign, ":banner_spr", 0), 
      (assign, ":banner_mesh", "mesh_banners_default_d"),  
      (try_begin),
        (this_or_next|party_slot_eq, ":party_no", "slot_party_type", spt_village),
        (this_or_next|party_slot_eq, ":party_no", "slot_party_type", spt_town),
        (party_slot_eq, ":party_no", "slot_party_type", spt_castle),
        (dict_set_int, "$coop_dict", "@p_garrison", reg20), #store rank of garrison party
        (party_get_slot, ":cur_leader", ":party_no", "slot_town_lord"), #can't store index of leader party here because we don't know it yet
        (ge, ":cur_leader", 0),
        (troop_get_slot, ":banner_spr", ":cur_leader", "slot_troop_banner_scene_prop"),
        (dict_set_int, "$coop_dict", "@p_garrison_banner", ":banner_spr"),
      (else_try),
        (party_stack_get_troop_id, ":leader_troop", ":party_no", 0),
        (troop_slot_eq, ":leader_troop", "slot_troop_occupation", slto_kingdom_hero),
        (troop_get_slot, ":banner_spr", ":leader_troop", "slot_troop_banner_scene_prop"),
      (try_end),
      (try_begin),
        (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
        (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
        (val_sub, ":banner_spr", banner_scene_props_begin),
        (store_add, ":banner_mesh", ":banner_spr", arms_meshes_begin),	
      (try_end),
      (try_begin), #store which party is garrison commander
        (eq, ":party_no", ":garrison_lord_party"),
        (dict_set_int, "$coop_dict", "@p_castle_lord", reg20), #store INDEX of garrison party (not party id)
      (try_end),
	
      (dict_set_int, "$coop_dict", "@p_enemy{reg20}_banner", ":banner_mesh"),
      (dict_set_int, "$coop_dict", "@p_enemy{reg20}_partyid", ":party_no"),


      (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
      (dict_set_int, "$coop_dict", "@p_enemy{reg20}_numstacks", ":num_stacks"),

      (try_for_range, reg21, 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", ":party_no", reg21),
        (party_stack_get_size, ":total_stack_size", ":party_no", reg21),
        (party_stack_get_num_wounded, ":num_wounded",":party_no", reg21),

        (try_begin),
          (troop_is_hero, ":stack_troop"),
          (store_troop_health, ":hero_health", ":stack_troop"),
          (le, ":hero_health", 15),
          (assign, ":num_wounded", 1),  
        (try_end),
        (store_sub, ":stack_size", ":total_stack_size", ":num_wounded"), 
        (ge, ":stack_size",1), #if alive
        (try_begin),
          (troop_is_hero, ":stack_troop"),
          (dict_set_int, "$coop_dict", "@hero_{reg22}_trp", ":stack_troop"),
          (val_add, reg22, 1), 
        (try_end),
        (dict_set_int, "$coop_dict", "@p_enemy{reg20}_{reg21}_trp", ":stack_troop"),
        (dict_set_int, "$coop_dict", "@p_enemy{reg20}_{reg21}_num", ":stack_size"),
      (try_end),
    (try_end),



#ADD ALLY PARTIES
      (assign, ":no_ally_parties", 1), # start from 1 because main party
      (try_begin),
        (gt, "$g_ally_party", 0), #if allies are attached to ally party
        (assign, ":ally_party", "$g_ally_party"),
        (assign, ":rank_start", 2),
        (val_add, ":no_ally_parties", 1), #add one for ally
      (else_try),
        (assign, ":rank_start", 1),
        (assign, ":ally_party", "p_main_party"), #if allies are attached to us
      (try_end),

    (party_get_num_attached_parties, ":num_attached_parties", ":ally_party"),
    (val_add, ":no_ally_parties", ":num_attached_parties"), 
    (dict_set_int, "$coop_dict", "@num_parties_ally", ":no_ally_parties"),

    (try_for_range, reg20, 0, ":no_ally_parties"),
      (try_begin),
        (eq, reg20, 0),#first party
        (assign, ":party_no", "p_main_party"),
      (else_try),
        (gt, "$g_ally_party", 0),
        (eq, reg20, 1),#second party
        (assign, ":party_no", "$g_ally_party"),
      (else_try),
        (store_sub, ":attached_party_rank", reg20, ":rank_start"), #sub 1 or 2 so rank starts from 0
        (party_get_attached_party_with_rank, ":party_no", ":ally_party", ":attached_party_rank"),
      (try_end),

      (assign, ":banner_spr", 0), 
      (assign, ":banner_mesh", "mesh_banners_default_d"), 
      (try_begin),
        (eq, ":party_no", "p_main_party"),
        (assign, ":banner_mesh", "mesh_banners_default_b"),  
      (try_end),
      (try_begin),
        (this_or_next|party_slot_eq, ":party_no", "slot_party_type", spt_village),
        (this_or_next|party_slot_eq, ":party_no", "slot_party_type", spt_town),
        (party_slot_eq, ":party_no", "slot_party_type", spt_castle),
        (dict_set_int, "$coop_dict", "@p_garrison", reg20), #store rank of garrison party
        (party_get_slot, ":cur_leader", ":party_no", "slot_town_lord"), #can't store index of leader party here because we don't know it yet
        (ge, ":cur_leader", 0),
        (troop_get_slot, ":banner_spr", ":cur_leader", "slot_troop_banner_scene_prop"),
        (dict_set_int, "$coop_dict", "@p_garrison_banner", ":banner_spr"),
      (else_try),
        (party_stack_get_troop_id, ":leader_troop", ":party_no", 0),
        (troop_is_hero, ":leader_troop"),
        (troop_get_slot, ":banner_spr", ":leader_troop", "slot_troop_banner_scene_prop"),
      (try_end),
      (try_begin),
        (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
        (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
        (val_sub, ":banner_spr", banner_scene_props_begin),
        (store_add, ":banner_mesh", ":banner_spr", arms_meshes_begin),	
      (try_end),

      (try_begin), #store which party is garrison commander
        (eq, ":party_no", ":garrison_lord_party"),
        (dict_set_int, "$coop_dict", "@p_castle_lord", reg20),  #store INDEX of garrison party (not party id)
      (try_end),
	
      (dict_set_int, "$coop_dict", "@p_ally{reg20}_banner", ":banner_mesh"),
      (dict_set_int, "$coop_dict", "@p_ally{reg20}_partyid", ":party_no"), #store party id for SP



      (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
      (dict_set_int, "$coop_dict", "@p_ally{reg20}_numstacks", ":num_stacks"),
      (try_for_range, reg21, 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", ":party_no", reg21),
        (party_stack_get_size, ":total_stack_size", ":party_no", reg21),
        (party_stack_get_num_wounded, ":num_wounded",":party_no", reg21),
        (try_begin),
          (troop_is_hero, ":stack_troop"),
          (store_troop_health, ":hero_health", ":stack_troop"),
          (le, ":hero_health", 15),
          (assign, ":num_wounded", 1),  
        (try_end),
        (store_sub, ":stack_size", ":total_stack_size", ":num_wounded"), 
        (ge, ":stack_size",1), #if alive

        (try_begin), #if storing main party
          (eq, ":party_no", "p_main_party"),
          (troop_get_class, ":troop_class", ":stack_troop"),
          (dict_set_int, "$coop_dict", "@p_ally{reg20}_{reg21}_cls", ":troop_class"),
          (eq, ":stack_troop", "trp_player"), 
          (troop_get_type, ":gender", "trp_player"),
              (val_mod, ":gender", 2),    #gender fix chief moto
         (try_begin),
            (eq, ":gender", 1),
            (assign, ":stack_troop",  "trp_multiplayer_profile_troop_female"),  
          (else_try),
            (assign, ":stack_troop",  "trp_multiplayer_profile_troop_male"),  
          (try_end),
        (try_end),

        (try_begin),
          (troop_is_hero, ":stack_troop"),
          (dict_set_int, "$coop_dict", "@hero_{reg22}_trp", ":stack_troop"),
          (val_add, reg22, 1), 
        (try_end),
        (dict_set_int, "$coop_dict", "@p_ally{reg20}_{reg21}_trp", ":stack_troop"),
        (dict_set_int, "$coop_dict", "@p_ally{reg20}_{reg21}_num", ":stack_size"),
      (try_end),
    (try_end),

    (dict_set_int, "$coop_dict", "@hero_num", reg22),

    (call_script, "script_coop_copy_hero_to_file"), 



    (dict_save, "$coop_dict", "@coop_battle"), #save new data
    (dict_free, "$coop_dict"),
    (display_message, "@Battle setup complete."),
    (try_end),

    ]),	





  # 
   #script_coop_copy_file_to_parties_mp
  # Input: arg1 = party_no
  ("coop_copy_file_to_parties_mp",
   [
    (try_begin), 
      (neg|is_vanilla_warband),

      (dict_get_int, "$coop_no_enemy_parties", "$coop_dict", "@num_parties_enemy"),
      (dict_get_int, "$coop_no_ally_parties", "$coop_dict", "@num_parties_ally"),

  #BOTH MODES
      (call_script, "script_coop_copy_file_to_settings"),	#copy game settings here
      (call_script, "script_coop_copy_file_to_hero"),

  #CLEAR casualty parties
      (try_for_range, ":party_rank", 0, "$coop_no_enemy_parties"),
        (store_add, ":party_no", ":party_rank", coop_temp_casualties_enemy_begin), 
        (party_clear, ":party_no"),
      (try_end),
      (try_for_range, ":party_rank", 0, "$coop_no_ally_parties"),
        (store_add, ":party_no", ":party_rank", coop_temp_casualties_ally_begin), 
        (party_clear, ":party_no"),
      (try_end),

  #ADD TROOPS TO TEMP SPAWN PARTIES 
  #ENEMY TEAM
      (assign, ":total_enemy_troops", 0),
      # (assign, ":cur_slot", 101),
        (party_clear, coop_temp_party_enemy_heroes),
      (try_for_range, reg20, 0, "$coop_no_enemy_parties"), #number of enemy parties
        (dict_get_int, ":num_stacks", "$coop_dict", "@p_enemy{reg20}_numstacks"),
        (dict_get_int, ":banner_mesh", "$coop_dict", "@p_enemy{reg20}_banner"),
        (troop_set_slot, "trp_temp_array_a", reg20, ":banner_mesh"),#encountered party banner
        (store_add, ":party_no", reg20, coop_temp_party_enemy_begin), 
        (party_clear, ":party_no"),
        (try_for_range, reg21, 0, ":num_stacks"),
          (dict_get_int, ":stack_troop", "$coop_dict", "@p_enemy{reg20}_{reg21}_trp"),
          (dict_get_int, ":stack_size", "$coop_dict", "@p_enemy{reg20}_{reg21}_num"),
          (party_add_members, ":party_no", ":stack_troop", ":stack_size"), #when copy to MP wounded troops have already been removed
          (val_add, ":total_enemy_troops", ":stack_size"),

          (try_begin),
            (troop_is_hero, ":stack_troop"),
            (eq, ":stack_size",1), #if alive
            (party_add_members, coop_temp_party_enemy_heroes, ":stack_troop", 1),
          (try_end),
        (try_end),
      (try_end), #end enemy parties
      # (troop_set_slot, "trp_temp_array_a", 100, ":cur_slot"),# slot 100 = 100 + number heroes + 1
      (assign, "$coop_num_bots_team_1", ":total_enemy_troops"), #count troops in battle




  #PLAYER TEAM  
      (assign, ":total_ally_troops", 0),
      # (assign, ":cur_slot", 101),
        (party_clear, coop_temp_party_ally_heroes),


      (try_for_range, reg20, 0, "$coop_no_ally_parties"), 
        (dict_get_int, ":num_stacks", "$coop_dict", "@p_ally{reg20}_numstacks"),
        (dict_get_int, ":banner_mesh", "$coop_dict", "@p_ally{reg20}_banner"),
        (troop_set_slot, "trp_temp_array_b", reg20, ":banner_mesh"),#encountered party banner
        (store_add, ":party_no", reg20, coop_temp_party_ally_begin),
        (party_clear, ":party_no"),
        (try_for_range, reg21, 0, ":num_stacks"),
          (dict_get_int, ":stack_troop", "$coop_dict", "@p_ally{reg20}_{reg21}_trp"),
          (dict_get_int, ":stack_size", "$coop_dict", "@p_ally{reg20}_{reg21}_num"),
          (party_add_members, ":party_no", ":stack_troop", ":stack_size"), #when copy to MP wounded troops have already been removed
          (val_add, ":total_ally_troops", ":stack_size"),
          (try_begin),
            (eq, reg20, 0), #main party
            (dict_get_int, ":troop_class", "$coop_dict", "@p_ally0_{reg21}_cls"),
            (troop_set_slot, ":stack_troop", "slot_troop_current_rumor", ":troop_class"), #store main party troop class in this slot
          (try_end),
          (try_begin),
            (troop_is_hero, ":stack_troop"),
            (eq, ":stack_size",1), #if alive
            (party_add_members, coop_temp_party_ally_heroes, ":stack_troop", 1),
          (try_end),

        (try_end),
      (try_end), #end ally parties
      # (troop_set_slot, "trp_temp_array_b", 100, ":cur_slot"),# slot 100 = 100 + number heroes + 1
      (assign, "$coop_num_bots_team_2", ":total_ally_troops"), #count troops in battle

    (try_end),

      ]),




  # 
   #script_coop_copy_parties_to_file_mp
  # Input: arg1 = party_no
  ("coop_copy_parties_to_file_mp",
   [
    (try_begin), 
      (neg|is_vanilla_warband),
      (dict_create, "$coop_dict"),
      (dict_load_file, "$coop_dict", "@coop_battle", 2),

        (dict_set_int, "$coop_dict", "@battle_state", coop_battle_state_end_mp),

        (call_script, "script_coop_copy_settings_to_file"),	

#At end of MP battle:

      #copy health from ALIVE agents to hero troops here before copying to registers (dead agents health is copied at coop_server_on_agent_killed_or_wounded_common)
      (try_for_agents, ":cur_agent"),
        (agent_is_human, ":cur_agent"),  
        (agent_is_alive, ":cur_agent"),
        (agent_get_troop_id, ":agent_troop_id", ":cur_agent"),
        (troop_is_hero, ":agent_troop_id"),   
        (store_agent_hit_points, ":agent_hit_points", ":cur_agent"),
        (troop_set_health, ":agent_troop_id", ":agent_hit_points"),

        # store items from agents
        (call_script, "script_coop_player_agent_save_items", ":cur_agent"),
      (try_end),

      (try_begin), 
        (eq, "$coop_winner_team", 0),#0 = enemy won
        (dict_set_int, "$coop_dict", "@battle_result", -1), # = battle_result
      (else_try),
        (eq, "$coop_winner_team", 1), #1 = player won
        (dict_set_int, "$coop_dict", "@battle_result", 1),
      (else_try),
        (dict_set_int, "$coop_dict", "@battle_result", 0),
      (try_end),


#ENEMY TEAM
      (try_for_range, reg20, 0, "$coop_no_enemy_parties"),
        (store_add, ":party_no", reg20, coop_temp_casualties_enemy_begin), 
        (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
        (dict_set_int, "$coop_dict", "@p_enemy{reg20}_numstacks_cas", ":num_stacks"),
        (try_for_range, reg21, 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", ":party_no", reg21),
          (party_stack_get_size, ":total_stack_size", ":party_no", reg21),
          (party_stack_get_num_wounded, ":num_wounded",":party_no", reg21),
          (try_begin),
            (troop_is_hero, ":stack_troop"),
            (store_troop_health, ":hero_health", ":stack_troop"),
            (le, ":hero_health", 15),
            (assign, ":num_wounded", 1),  
          (try_end),
          (store_sub, ":dead_size", ":total_stack_size", ":num_wounded"), 
          (dict_set_int, "$coop_dict", "@p_enemy{reg20}_{reg21}_trp_cas", ":stack_troop"),
          (dict_set_int, "$coop_dict", "@p_enemy{reg20}_{reg21}_ded", ":dead_size"),
          (dict_set_int, "$coop_dict", "@p_enemy{reg20}_{reg21}_wnd", ":num_wounded"),
        (try_end),
      (try_end),




#ADD PARTIES ATTACHED TO MAIN PARTY
      (try_for_range, reg20, 0, "$coop_no_ally_parties"),
        (store_add, ":party_no", reg20, coop_temp_casualties_ally_begin), 
        (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
        (dict_set_int, "$coop_dict", "@p_ally{reg20}_numstacks_cas", ":num_stacks"),
        (try_for_range, reg21, 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", ":party_no", reg21),
          (party_stack_get_size, ":total_stack_size", ":party_no", reg21),
          (party_stack_get_num_wounded, ":num_wounded",":party_no", reg21),
          (try_begin),
            (troop_is_hero, ":stack_troop"),
            (store_troop_health, ":hero_health", ":stack_troop"),
            (le, ":hero_health", 15),
            (assign, ":num_wounded", 1),  
          (try_end),
          (store_sub, ":dead_size", ":total_stack_size", ":num_wounded"), 
          (dict_set_int, "$coop_dict", "@p_ally{reg20}_{reg21}_trp_cas", ":stack_troop"),
          (dict_set_int, "$coop_dict", "@p_ally{reg20}_{reg21}_ded", ":dead_size"),
          (dict_set_int, "$coop_dict", "@p_ally{reg20}_{reg21}_wnd", ":num_wounded"),
        (try_end),
      (try_end),



#store xp for regular troop stacks in main party
      (dict_get_int, ":num_stacks", "$coop_dict", "@p_ally0_numstacks"), #num stacks from spawn party
      (try_for_range, reg21, 0, ":num_stacks"),
        (dict_get_int, ":stack_troop", "$coop_dict", "@p_ally0_{reg21}_trp"),
        (neg|troop_is_hero, ":stack_troop"),
        (troop_get_slot, ":stack_xp", ":stack_troop", "slot_troop_temp_slot"),
        (dict_set_int, "$coop_dict", "@p_ally0_{reg21}_stk_xp", ":stack_xp"),
      (try_end),

      (call_script, "script_coop_copy_hero_to_file"), 

      (get_max_players, ":num_players"),
      (try_for_range, ":player_no", 0, ":num_players"), 
        (player_is_active, ":player_no"),
        (player_is_admin, ":player_no"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_coop_send_to_player, coop_event_result_saved),
      (try_end),
      (assign, "$coop_battle_started", -1),

      (dict_save, "$coop_dict", "@coop_battle"),
      (dict_free, "$coop_dict"),
    (try_end),
    ]),	




  #
   #script_coop_copy_file_to_parties_sp
  # Input: arg1 = party_no
  ("coop_copy_file_to_parties_sp",
   [
    (try_begin), 
      (neg|is_vanilla_warband),
    (dict_create, "$coop_dict"),
    (dict_load_file, "$coop_dict", "@coop_battle", 2),

    (dict_set_int, "$coop_dict", "@battle_state", coop_battle_state_none),
    (dict_save, "$coop_dict", "@coop_battle"),

    (dict_get_int, "$coop_no_enemy_parties", "$coop_dict", "@num_parties_enemy"),
    (dict_get_int, "$coop_no_ally_parties", "$coop_dict", "@num_parties_ally"),

#BOTH MODES
    (call_script, "script_coop_copy_file_to_settings"),	#copy game settings here before heroes
    (call_script, "script_coop_copy_file_to_hero"), #this sets hero health from battle

#create temp parties or wound parties
    (party_clear, "p_total_enemy_casualties"),
    (party_clear, "p_enemy_casualties"),

    (try_for_range, reg20, 0, "$coop_no_enemy_parties"), #number of enemy parties
      (dict_get_int, ":num_casualty_stacks", "$coop_dict", "@p_enemy{reg20}_numstacks_cas"),
      (dict_get_int, ":party_to_kill", "$coop_dict", "@p_enemy{reg20}_partyid"),

      (try_for_range, reg21, 0, ":num_casualty_stacks"),
        (dict_get_int, ":stack_troop", "$coop_dict", "@p_enemy{reg20}_{reg21}_trp_cas"),
        (dict_get_int, ":stack_dead", "$coop_dict", "@p_enemy{reg20}_{reg21}_ded"),
        (dict_get_int, ":stack_wounded", "$coop_dict", "@p_enemy{reg20}_{reg21}_wnd"),

          (store_add, ":stack_total_casualties", ":stack_dead", ":stack_wounded"), 
          (try_begin),
            (troop_is_hero,":stack_troop"),
            (store_random_in_range, ":rand_wound", 40, 71),
            (store_troop_health, ":troop_hp",":stack_troop"),
            (val_sub, ":troop_hp", ":rand_wound"),
            (val_max, ":troop_hp", 1),
            (troop_set_health, ":stack_troop", ":troop_hp"),
          (else_try),
            (party_remove_members, ":party_to_kill", ":stack_troop", ":stack_dead"),#remove from parties
          (try_end),
          (party_wound_members, ":party_to_kill", ":stack_troop", ":stack_wounded"),
          (party_add_members, "p_total_enemy_casualties", ":stack_troop", ":stack_total_casualties"), #add casualties for loot
          (party_wound_members, "p_total_enemy_casualties", ":stack_troop", ":stack_wounded"),
          (party_add_members, "p_enemy_casualties", ":stack_troop", ":stack_total_casualties"), #add casualties for reports/morale
          (party_wound_members, "p_enemy_casualties", ":stack_troop", ":stack_wounded"),
      (try_end),
    (try_end), #end enemy parties




#PLAYER TEAM  

     #add regular troop xp BEFORE removing dead troops from party
      (dict_get_int, ":num_stacks", "$coop_dict", "@p_ally0_numstacks"), #num stacks from spawn party
      (try_for_range, reg21, 0, ":num_stacks"),
        (dict_get_int, ":stack_troop", "$coop_dict", "@p_ally0_{reg21}_trp"),
        (neg|troop_is_hero, ":stack_troop"),
        (dict_get_int, ":stack_xp", "$coop_dict", "@p_ally0_{reg21}_stk_xp"),
        (party_add_xp_to_stack, "p_main_party", reg21, ":stack_xp"),
      (try_end),

    (assign, "$any_allies_at_the_last_battle", 0),
    (party_clear, "p_player_casualties"),
    (party_clear, "p_ally_casualties"),
    (try_for_range, reg20, 0, "$coop_no_ally_parties"), 
      (dict_get_int, ":num_casualty_stacks", "$coop_dict", "@p_ally{reg20}_numstacks_cas"),
      (dict_get_int, ":party_to_kill", "$coop_dict", "@p_ally{reg20}_partyid"),

      (try_begin),
        (eq, ":party_to_kill", "p_main_party"),
        (assign, ":casualties_party", "p_player_casualties"),
        (party_get_skill_level, ":player_party_surgery", "p_main_party", "skl_surgery"),
        (val_mul, ":player_party_surgery", 4),    #4% per skill level
      (else_try),
        (assign, "$any_allies_at_the_last_battle", 1),
        (assign, ":casualties_party", "p_ally_casualties"),
      (try_end),

      (try_for_range, reg21, 0, ":num_casualty_stacks"),
        (dict_get_int, ":stack_troop", "$coop_dict", "@p_ally{reg20}_{reg21}_trp_cas"),
        (dict_get_int, ":stack_dead", "$coop_dict", "@p_ally{reg20}_{reg21}_ded"),
        (dict_get_int, ":stack_wounded", "$coop_dict", "@p_ally{reg20}_{reg21}_wnd"),
        (store_add, ":stack_total_casualties", ":stack_dead", ":stack_wounded"), 

        (try_begin), 
          (eq, ":party_to_kill", "p_main_party"),
          (try_begin),
            (this_or_next|eq, ":stack_troop",  "trp_multiplayer_profile_troop_female"),  
            (eq, ":stack_troop",  "trp_multiplayer_profile_troop_male"),  
            (assign, ":stack_troop", "trp_player"),
          (try_end),
          (try_begin),#use surgey to heal regular troops in stack
            (neg|troop_is_hero, ":stack_troop"),
            (assign, ":end", ":stack_dead"),
            (try_for_range, ":unused", 0, ":end"),#try each dead troop in stack
              (store_random_in_range, ":rand", 0, 100),
              (lt, ":rand", ":player_party_surgery"),
              (val_add, ":stack_wounded", 1),
              (val_sub, ":stack_dead", 1),
            (try_end),
          (try_end),
        (else_try), #ally party
          (troop_is_hero,":stack_troop"),#ally lord
          (store_random_in_range, ":rand_wound", 40, 71),
          (store_troop_health, ":troop_hp",":stack_troop"),
          (val_sub, ":troop_hp", ":rand_wound"),
          (val_max, ":troop_hp", 1),
          (troop_set_health, ":stack_troop", ":troop_hp"),
        (try_end),

        (party_wound_members, ":party_to_kill", ":stack_troop", ":stack_wounded"), #wound regular and heroes
        (try_begin),
          (neg|troop_is_hero,":stack_troop"),
          (party_remove_members, ":party_to_kill", ":stack_troop", ":stack_dead"), #kill regulars
        (try_end),

        #add dead and wounded for casualty report
        (party_add_members, ":casualties_party", ":stack_troop", ":stack_total_casualties"),#dead
        (party_wound_members, ":casualties_party", ":stack_troop", ":stack_wounded"),#wounded
      (try_end),
    (try_end),


#SP USE RESULT needs to be after troops are healed to count them as routed

      (dict_get_int, "$g_battle_result", "$coop_dict", "@battle_result"),  #-1 = enemy won, 1 = player won
      (try_begin),
        (eq, "$g_battle_result", -1), #enemy won
        (call_script, "script_party_count_members_with_full_health", "p_main_party"), 
        (assign, "$num_routed_us", reg0), 
        (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),        
        (assign, "$num_routed_allies", reg0), #use routed troops to avoid a 2nd round of battle
      (else_try),
        (eq, "$g_battle_result", 1), #player won
        (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
        (assign, "$num_routed_enemies", reg0), #use routed troops to avoid a 2nd round of battle
      (else_try),
        (eq, "$g_battle_result", 0), #retreat
      (try_end),


    (dict_free, "$coop_dict"),
    (try_end),
    ]),	




 # 
   # script_coop_copy_register_to_hero_xp
  ("coop_copy_register_to_hero_xp",
    [
      (store_script_param, ":troop", 1),
      (store_script_param, ":troop_xp", 2),
      (try_begin),
        (troop_get_xp, ":troop_default_xp", ":troop"),
        (store_sub, ":xp_to_add", ":troop_xp", ":troop_default_xp"), 

         # (str_store_troop_name, s40, ":troop"),
         # (assign, reg1, ":xp_to_add"),
         # (assign, reg2, ":troop_default_xp"),
         # (assign, reg3, ":troop_xp"),
         # (display_message, "@Adding {reg1} xp to {s40}   {reg2} / {reg3}"),

        (try_begin),
          (gt, ":xp_to_add", 29999),
          (store_div, ":num_times", ":xp_to_add", 29999), 
          (try_for_range, ":unused", 0, ":num_times"),
            (add_xp_to_troop, 29999, ":troop"),
            (val_sub, ":xp_to_add", 29999), 
          (try_end),		 
        (try_end),		 
        (add_xp_to_troop, ":xp_to_add", ":troop"),		 #add leftover xp
      (try_end),	




    ]),	 



# SET heroes SKILL/EQUIPMENT 
  # script_coop_copy_hero_to_file
  # Input: arg1 = hero troop
  # Output: none
  ("coop_copy_hero_to_file",
    [
    (try_begin), 
      (neg|is_vanilla_warband),

      (dict_get_int, ":number_heroes", "$coop_dict", "@hero_num"),
      (try_for_range, reg21, 0, ":number_heroes"),
        (dict_get_int, ":cur_troop", "$coop_dict", "@hero_{reg21}_trp"),
        (try_begin),
          (neg|game_in_multiplayer_mode),
          (this_or_next|eq, ":cur_troop",  "trp_multiplayer_profile_troop_female"),  
          (eq, ":cur_troop",  "trp_multiplayer_profile_troop_male"),  
          (assign, ":cur_troop", "trp_player"),
         # (store_troop_gold, ":gold", ":cur_troop"), #use this if needed
          # (dict_set_int, "$coop_dict", "@hero_{reg21}_gld", ":gold"),
        (try_end),

				(str_store_troop_name, s0, ":cur_troop"),
        (troop_get_xp, ":xp", ":cur_troop"),
        (store_troop_health, ":health", ":cur_troop"),
        (dict_set_str, "$coop_dict", "@hero_{reg21}_name", s0),
        (dict_set_int, "$coop_dict", "@hero_{reg21}_xp", ":xp"),
        (dict_set_int, "$coop_dict", "@hero_{reg21}_hp", ":health"),

#NEW
        (face_keys_init, reg1),
        (troop_get_face_keys, reg1, ":cur_troop"),
        (str_store_face_keys, s0, reg1),
        (dict_set_str, "$coop_dict", "@hero_{reg21}_face", s0),

        (store_attribute_level, ":ca_strength", ":cur_troop", ca_strength),
        (store_attribute_level, ":ca_agility", ":cur_troop", ca_agility),
        # (store_attribute_level, ":ca_intelligence", ":cur_troop", ca_intelligence),
        # (store_attribute_level, ":ca_charisma", ":cur_troop", ca_charisma),

        (dict_set_int, "$coop_dict", "@hero_{reg21}_str", ":ca_strength"),
        (dict_set_int, "$coop_dict", "@hero_{reg21}_agi", ":ca_agility"),
        # (dict_set_int, "$coop_dict", "@hero_{reg21}_int", ":ca_intelligence"),
        # (dict_set_int, "$coop_dict", "@hero_{reg21}_cha", ":ca_charisma"),


        (try_for_range, reg20, "skl_horse_archery", "skl_reserved_14"), #start from "skl_trade" if all skills are needed
          (neg|is_between, reg20, "skl_reserved_9", "skl_power_draw"), #skip these skills
          (store_skill_level, ":skill", reg20, ":cur_troop"),
          (dict_set_int, "$coop_dict", "@hero_{reg21}_skl{reg20}", ":skill"),
        (try_end),

        (try_for_range, reg20, wpt_one_handed_weapon, 7),  #wpt_firearm = 6 
          (store_proficiency_level, ":prof", ":cur_troop", reg20),
          (dict_set_int, "$coop_dict", "@hero_{reg21}_wp{reg20}", ":prof"),
        (try_end),

        (try_begin),
          (neg|is_between, ":cur_troop", kings_begin, pretenders_end), #need this so we dont equip lords with civilian clothes in battle
          (try_for_range, reg20, ek_item_0, ek_food), 
            (troop_get_inventory_slot, ":item", ":cur_troop", reg20),
            (troop_get_inventory_slot_modifier, ":imod", ":cur_troop", reg20),
            (dict_set_int, "$coop_dict", "@hero_{reg21}_itm{reg20}", ":item"),
            (dict_set_int, "$coop_dict", "@hero_{reg21}_imd{reg20}", ":imod"),
          (try_end),

        (try_end),

      (try_end), #end of hero loop


      (try_begin),
        (game_in_multiplayer_mode),
        (assign, ":cur_troop", "trp_temp_troop"),
      (else_try),
        (assign, ":cur_troop", "trp_player"),
        (store_skill_level, ":skill", "skl_inventory_management", ":cur_troop"),
        (dict_set_int, "$coop_dict", "@player_inv_mgt", ":skill"),
      (try_end),
      (troop_get_inventory_capacity, ":end", ":cur_troop"),
      (val_add,":end", 1), 
      (try_for_range, reg20, 10, ":end"),
        (troop_get_inventory_slot, ":item", ":cur_troop", reg20),
        (troop_get_inventory_slot_modifier, ":imod", ":cur_troop", reg20),
        (dict_set_int, "$coop_dict", "@party_inv{reg20}_itm", ":item"),
        (dict_set_int, "$coop_dict", "@party_inv{reg20}_imd", ":imod"),
        # (troop_inventory_slot_get_item_amount, ":number", ":cur_troop", reg20),
        # (dict_set_int, "$coop_dict", "@party_inv{reg20}_num", ":number"),
      (try_end),
    (try_end),
    ]),	 



# SET heroes SKILL/EQUIPMENT 
  # script_coop_copy_file_to_hero
  # Input: arg1 = hero troop
  # Output: none
  ("coop_copy_file_to_hero",
    [
    (try_begin), 
      (neg|is_vanilla_warband),
      (dict_get_int, ":number_heroes", "$coop_dict", "@hero_num"),
      (try_for_range, reg21, 0, ":number_heroes"),
        (dict_get_int, ":cur_troop", "$coop_dict", "@hero_{reg21}_trp"),
        (try_begin),
          (neg|game_in_multiplayer_mode), 
          (this_or_next|eq, ":cur_troop",  "trp_multiplayer_profile_troop_female"),  
          (eq, ":cur_troop",  "trp_multiplayer_profile_troop_male"),  
          (assign, ":cur_troop", "trp_player"),  #in SP use player instead of profile
        (try_end),

        (dict_get_int, ":ca_strength", "$coop_dict", "@hero_{reg21}_str"),
        (dict_get_int, ":ca_agility", "$coop_dict", "@hero_{reg21}_agi"),
        # (dict_get_int, ":ca_intelligence", "$coop_dict", "@hero_{reg21}_int"),
        # (dict_get_int, ":ca_charisma", "$coop_dict", "@hero_{reg21}_cha"),

        (store_attribute_level, ":value", ":cur_troop", ca_strength),
        (val_sub, ":ca_strength", ":value"),
        (store_attribute_level, ":value", ":cur_troop", ca_agility),
        (val_sub, ":ca_agility", ":value"),

        (troop_raise_attribute, ":cur_troop", ca_strength, ":ca_strength"),
        (troop_raise_attribute, ":cur_troop", ca_agility, ":ca_agility"),
        # (troop_raise_attribute, ":cur_troop", ca_intelligence, ":ca_intelligence"),
        # (troop_raise_attribute, ":cur_troop", ca_charisma, ":ca_charisma"),

        (try_for_range, reg20, "skl_horse_archery", "skl_reserved_14"), #start from "skl_trade" if all skills are needed
          (neg|is_between, reg20, "skl_reserved_9", "skl_power_draw"), #skip these skills
          (dict_get_int, ":skill", "$coop_dict", "@hero_{reg21}_skl{reg20}"),
          (store_skill_level, ":value", reg20,":cur_troop"),
          (val_sub, ":skill", ":value"),
          (troop_raise_skill, ":cur_troop", reg20, ":skill"),
          # (try_begin), #NEW
            # (eq, reg20, "skl_ironflesh"),
            # (store_mul, ":added_ironflesh", ":skill", 2), #get number of hit point that will be added when spawning
          # (try_end),
        (try_end),

        (try_for_range, reg20, wpt_one_handed_weapon, 7),  #wpt_firearm = 6 
          (dict_get_int, ":wprof", "$coop_dict", "@hero_{reg21}_wp{reg20}"),
          (store_proficiency_level, ":value", ":cur_troop", reg20),
          (val_sub, ":wprof", ":value"),
          (troop_raise_proficiency_linear, ":cur_troop", reg20, ":wprof"),
        (try_end),

        (try_begin),
          (neg|is_between, ":cur_troop", kings_begin, pretenders_end), #need this so we dont equip lords with civilian clothes in battle
          (dict_get_str, s0, "$coop_dict", "@hero_{reg21}_name"),
          (try_begin),
            (str_is_empty, s0),
            (str_store_string, s0, "@Player"), #set default name
          (try_end),
          (troop_set_name, ":cur_troop", s0),
      
          (try_begin),#inventory is optional
            (this_or_next|game_in_multiplayer_mode), 
            (eq, "$coop_disable_inventory", 0),
            (try_for_range, reg20, ek_item_0, ek_food), 
              (dict_get_int, ":item", "$coop_dict", "@hero_{reg21}_itm{reg20}"),
              (dict_get_int, ":imod", "$coop_dict", "@hero_{reg21}_imd{reg20}"),
              (troop_set_inventory_slot, ":cur_troop", reg20, ":item"),
              (troop_set_inventory_slot_modifier, ":cur_troop", reg20, ":imod"),
            (try_end),
          (try_end),
        (try_end),
#NEW
        (try_begin),#only set face in MP
          (game_in_multiplayer_mode),
          (dict_get_str, s0, "$coop_dict", "@hero_{reg21}_face"),
          (face_keys_store_string, reg1, s0),
          (troop_set_face_keys, ":cur_troop", reg1),
        (try_end),

        (dict_get_int, ":xp", "$coop_dict", "@hero_{reg21}_xp"),
        (call_script, "script_coop_copy_register_to_hero_xp", ":cur_troop", ":xp"),

        (dict_get_int, ":battle_health", "$coop_dict", "@hero_{reg21}_hp"),
        (try_begin),#set health after attributes
          (neg|game_in_multiplayer_mode),
          (main_party_has_troop, ":cur_troop"),
          (party_get_skill_level, ":player_party_first_aid", "p_main_party", "skl_first_aid"), #currently we get medic skill before wounding heroes
          (val_mul, ":player_party_first_aid", 5),  #5% per skill level
          (store_troop_health, ":old_health", ":cur_troop"),
          (store_sub, ":lost_health", ":old_health",":battle_health"),
          (val_max, ":lost_health", 0), # if <0 we would gain health
          (val_mul, ":lost_health", ":player_party_first_aid"),
          (val_div, ":lost_health", 100),
          (val_add, ":battle_health", ":lost_health"), #add recovered percentage
          (troop_set_health, ":cur_troop", ":battle_health"),
        (else_try),
          #NEW not getting this bug anymore 
          #  when setup MP: ironflesh will add alive hitpoint later when troop spawns, so find what % troop should be now to compensate
          # (troop_set_health, ":cur_troop", ":battle_health"), 
          # (store_mul, ":hp_x10", ":battle_health",10), 
          # (store_troop_health, ":hp", ":cur_troop",1),
          # (val_max, ":hp", 1),
          # (val_div, ":hp_x10", ":hp"), 
          # (val_mul, ":hp_x10", ":added_ironflesh"), 
          # (val_div, ":hp_x10", 10), 
          # (val_sub, ":battle_health", ":hp_x10"), 
          (troop_set_health, ":cur_troop", ":battle_health"), 
        (try_end),

        #use this if needed
        # (try_begin),
          # (dict_get_int, ":new_gold", "$coop_dict", "@hero_{reg21}_gld"),
          # (store_troop_gold, ":cur_gold", ":cur_troop"), 
          # (gt, ":new_gold", ":cur_gold"),
          # (val_sub, ":new_gold", ":cur_gold"),
          # (troop_add_gold,":cur_troop",":new_gold"),
        # (try_end),

      (try_end), #end of hero loop

    
      (try_begin),
        (eq, "$coop_disable_inventory", 0),  #inventory is optional
        (try_begin),
          (game_in_multiplayer_mode),
          (assign, ":cur_troop", "trp_temp_troop"),
          (dict_get_int, ":skill", "$coop_dict", "@player_inv_mgt"),
          (store_skill_level, ":value", "skl_inventory_management",":cur_troop"),
          (val_sub, ":skill", ":value"),
          (troop_raise_skill, ":cur_troop", "skl_inventory_management", ":skill"),
        (else_try),
          (assign, ":cur_troop", "trp_player"),
        (try_end),
        (troop_get_inventory_capacity, ":end", ":cur_troop"),
        (val_add,":end", 1), 
        (try_for_range, reg20, 10, ":end"),
          (dict_get_int, ":item", "$coop_dict", "@party_inv{reg20}_itm"),
          (dict_get_int, ":imod", "$coop_dict", "@party_inv{reg20}_imd"),

          (assign, ":skip",0),
          (try_begin),
            (neg|game_in_multiplayer_mode),
            (is_between, ":item", trade_goods_begin, trade_goods_end), #these items would need to copy correct quantity still need to copy to MP to take up inv capacity 
            (assign, ":skip",1),
          (try_end),

          (eq, ":skip",0),
          (troop_set_inventory_slot, ":cur_troop", reg20, ":item"),
          (troop_set_inventory_slot_modifier, ":cur_troop", reg20, ":imod"),

          # (dict_get_int, ":number", "$coop_dict", "@party_inv{reg20}_num"),
          # (try_begin),
            # (gt, ":number", 0), 
            # (troop_inventory_slot_set_item_amount, ":cur_troop", reg20, ":number"),
          # (try_end),

        (try_end),
      (try_end),

    (try_end),
    ]),	 


]
