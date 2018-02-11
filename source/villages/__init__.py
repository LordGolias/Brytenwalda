from source.header_operations import *
from source.header_common import *

from source.header_game_menus import mnf_enable_hot_keys
from source.header_terrain_types import *

from source.statement import StatementBlock

from source.module_constants import *

from . import hostile_actions, buy_cattle, recruit, bandits_infestation


def _create_bounty_visitor(bounty_name, bounty_target):
    return StatementBlock(
        (try_begin),
            (check_quest_active, bounty_name),
            (neg|is_currently_night),
            (quest_slot_eq, bounty_name, "slot_quest_target_center", "$current_town"),
            (neg|check_quest_succeeded, bounty_name),
            (neg|check_quest_failed, bounty_name),
            (store_random_in_range, ":random", 0, 8),
            (try_begin),
                (eq, ":random", 0),
                (store_random_in_range, bounty_target, fugitives_begin, fugitives_end),
            (else_try),
                (eq, ":random", 1),
                (store_random_in_range, bounty_target, outlaws_begin, outlaws_end),
            (else_try),
                (eq, ":random", 2),
                (store_random_in_range, bounty_target, rogues_begin, rogues_end),
            (else_try),
                (eq, ":random", 3),
                (store_random_in_range, bounty_target, goblin_outlaws_begin, goblin_outlaws_end),
            (else_try),
                (eq, ":random", 4),
                (store_random_in_range, bounty_target, orc_outlaws_begin, orc_outlaws_end),
            (else_try),
                (eq, ":random", 5),
                (store_random_in_range, bounty_target, elf_outlaws_begin, elf_outlaws_end),
            (else_try),
                (eq, ":random", 6),
                (store_random_in_range, bounty_target, darkelf_outlaws_begin, darkelf_outlaws_end),
            (else_try),
                (store_random_in_range, bounty_target, saracen_outlaws_begin, saracen_outlaws_end),
            (try_end),
            (set_visitor, 45, bounty_target),
        (try_end),
    )


menus = [

    ("village", mnf_enable_hot_keys, "{s10} {s12}^{s11}^{s6}{s7} {s15}", "none", [
        (assign, "$current_town", "$g_encountered_party"),
        (call_script, "script_update_center_recon_notes", "$current_town"),

        # todo: remove these assigns from here
        (assign, "$g_defending_against_siege", 0), #required for bandit check
        (assign, "$g_battle_result", 0),
        (assign, "$qst_collect_taxes_currently_collecting", 0),
        (assign, "$qst_train_peasants_against_bandits_currently_training", 0),

        # todo: remove this try (so it is not required in this menu)
        (try_begin),
            (gt, "$auto_enter_menu_in_center", 0),
            (jump_to_menu, "$auto_enter_menu_in_center"),
            (assign, "$auto_enter_menu_in_center", 0),
        (try_end),

        # todo: remove this.
        (try_begin),
            (neq, "$g_player_raiding_village",  "$current_town"),
            (assign, "$g_player_raiding_village", 0),
        (else_try),
            (jump_to_menu, "mnu_village_loot_continue"),
        (try_end),

        # todo: remove this
        (try_begin),  # Fix for collecting taxes
            (eq, "$g_town_visit_after_rest", 1),
            (assign, "$g_town_visit_after_rest", 0),
        (try_end),

        # religion -> s15
        (try_begin),
            (this_or_next|eq, "$g_sod_faith", 1),
            (eq, "$g_sod_faith", 4),
            (party_get_slot, ":faith", "$current_town", "slot_center_sod_local_faith"),
            (try_begin),
                (party_slot_eq, "$current_town", "slot_center_religion_pagan", 1),
                (str_store_string, s15, "@ ...(Pagan Village) Your faith is hated among the population..."),
            (else_try),
                (lt, ":faith", 30),
                (str_store_string, s15, "@ ...(Christian Village) Your faith is tolerated here..."),
            (else_try),
                (lt, ":faith", 50),
                (str_store_string, s15, "@ ...(Christian Village) Your faith is accepted here..."),
            (else_try),
                (lt, ":faith", 80),
                (str_store_string, s15, "@ ...(Christian Village) Your faith is dominant here..."),
            (else_try),
                (lt, ":faith", 101),
                (str_store_string, s15, "@ ...(Christian Village) This village is a bastion of Your faith..."),
            (else_try),
                (str_store_string, s15, "@ ...Rumor spreads that Christian faith is nothing more than a veil, and the population continues to worship pagan gods..."),
            (try_end),
        (try_end),

        (try_begin),
            (this_or_next|eq, "$g_sod_faith", 2),
            (eq, "$g_sod_faith", 3),
            (party_get_slot, ":faith", "$current_town", "slot_center_sod_local_faith"),
            (try_begin),
                (neg|party_slot_ge, "$current_town", "slot_center_religion_pagan", 1),
                (str_store_string, s15, "@ ...(Christian Village) Your faith is hated among the population..."),
            (else_try),
                (party_slot_eq, "$current_town", "slot_center_religion_pagan", 1),
                (lt, ":faith", 30),
                (str_store_string, s15, "@ ...(Pagan Village) Your faith is liked here..."),
            (else_try),
                (party_slot_eq, "$current_town", "slot_center_religion_pagan", 1),
                (lt, ":faith", 50),
                (str_store_string, s15, "@ ...(Pagan Village) Your faith is accepted here..."),
            (else_try),
                (party_slot_eq, "$current_town", "slot_center_religion_pagan", 1),
                (lt, ":faith", 80),
                (str_store_string, s15, "@ ...(Pagan Village) Your faith is dominant here..."),
            (else_try),
                (party_slot_eq, "$current_town", "slot_center_religion_pagan", 1),
                (lt, ":faith", 101),
                (str_store_string, s15, "@ ...(Pagan Village) This village is a bastion of Your faith..."),
            (else_try),
                (str_store_string, s15, "@ ...Rumor spreads that old pagan gods are being forgotten in favour of Christendom..."),
            (try_end),
        (try_end),

        # village prosperity -> (s10, s12)
        (str_clear, s10),
        (str_clear, s12),
        (try_begin),
            (neg | party_slot_eq, "$current_town", "slot_village_state", svs_looted),

            # str_ of property uses s60 as village name
            (str_store_party_name, s60, "$current_town"),
            (party_get_slot, ":prosperity", "$current_town", "slot_town_prosperity"),

            (try_begin),
                (eq, "$cheat_mode", 1),
                (assign, reg4, ":prosperity",),
                (display_message, "@{!}Prosperity: {reg4}"),
            (try_end),

            (store_div, ":str_id", ":prosperity", 10),
            (val_min, ":str_id", 9),
            (val_add, ":str_id", "str_village_prosperity_0"),
            (str_store_string, s10, ":str_id"),

            (store_div, ":str_id", ":prosperity", 20),
            (val_min, ":str_id", 4),
            (try_begin),
                # string for oasis
                (is_between, "$current_town", "p_village_91", villages_end),
                (val_add, ":str_id", "str_oasis_village_alt_prosperity_0"),
            (else_try),
                (val_add, ":str_id", "str_village_alt_prosperity_0"),
            (try_end),

            (str_store_string, s12, ":str_id"),
        (try_end),

        # owner -> s11
        (party_get_slot, ":center_lord", "$current_town", "slot_town_lord"),
        (str_clear, s11),
        (try_begin),
            (party_slot_eq, "$current_town", "slot_village_state", svs_looted),
        (else_try),
            (eq, ":center_lord", "trp_player"),
            (str_store_string, s11, "@ This village and the surrounding lands belong to you."),
        (else_try),
            (ge, ":center_lord", 0),
            (str_store_troop_name, s8, ":center_lord"),
            (store_faction_of_party, ":center_faction", "$current_town"),
            (str_store_faction_name, s9, ":center_faction"),
            (str_store_string, s7, "@{s8} of {s9}"),
            (str_store_string, s11, "@ You remember that this village and the surrounding lands belong to {s7}."),
        (else_try),
            (str_store_string, s11, "@ These lands belong to no one."),
        (try_end),

        # relation with player -> s7
        (str_clear, s7),
        (try_begin),
            (neg | party_slot_eq, "$current_town", "slot_village_state", svs_looted),
            (party_get_slot, ":center_relation", "$current_town", "slot_center_player_relation"),
            (call_script, "script_describe_center_relation_to_s3", ":center_relation"),
            (assign, reg9, ":center_relation"),
            (str_store_string, s7, "@{!} {s3} ({reg9})."),
        (try_end),

        # village is infested -> s6
        (str_clear, s6),
        (try_begin),
            (party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            (party_get_slot, ":bandit_troop", "$current_town", "slot_village_infested_by_bandits"),
            (store_character_level, ":player_level", "trp_player"),

            (store_add, "$qst_eliminate_bandits_infesting_village_num_bandits", ":player_level", 20),
            (val_mul, "$qst_eliminate_bandits_infesting_village_num_bandits", 22),
            (val_div, "$qst_eliminate_bandits_infesting_village_num_bandits", 20),
            (store_random_in_range, "$qst_eliminate_bandits_infesting_village_num_villagers", 25, 30),
            (assign, reg8, "$qst_eliminate_bandits_infesting_village_num_bandits"),

            (str_store_troop_name_by_count, s35, ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),

            (str_store_string, s6, "@ The village is infested by {reg8} {s35}."),

            # todo: remove this assign from here
            (assign, "$g_enemy_party", -1),
            (assign, "$g_ally_party", -1),

            (try_begin),
                (eq, ":bandit_troop", "trp_forest_bandit"),
                (set_background_mesh, "mesh_pic_forest_bandits1"),
            (else_try),
                (eq, ":bandit_troop", "trp_steppe_bandit"),
                (set_background_mesh, "mesh_pic_steppe_bandits1"),
            (else_try),
                (eq, ":bandit_troop", "trp_taiga_bandit"),
                (set_background_mesh, "mesh_pic_steppe_bandits1"),
            (else_try),
                (eq, ":bandit_troop", "trp_mountain_bandit"),
                (set_background_mesh, "mesh_pic_mountain_bandits1"),
            (else_try),
                (eq, ":bandit_troop", "trp_sea_raider"),
                (set_background_mesh, "mesh_pic_sea_raiders1"),
            (else_try),
                (eq, ":bandit_troop", "trp_dena_pirate"),
                (set_background_mesh, "mesh_pic_sea_raiders1"),
            (else_try),
                (eq, ":bandit_troop", "trp_peasant_woman"),
                (str_store_string, s6, "@ The peasants hired mercenaries and are rebelling against you."),
                (set_background_mesh, "mesh_pic_villageriot"),
            (else_try),
                (set_background_mesh, "mesh_pic_bandits1"),
            (try_end),

        # village is pillaged -> s6
        (else_try),
            (party_slot_eq, "$current_town", "slot_village_state", svs_looted),
            (str_store_string, s6, "@ The village has been pillaged. A handful of souls scatter as you pass through the burnt out houses."),

            (try_begin),
                (neq, "$g_player_raid_complete", 1),
                (play_track, "track_empty_village", 1),
            (try_end),

            (set_background_mesh, "mesh_pic_looted_village1"),

        # village is being raided -> s6
        (else_try),
            (party_slot_eq, "$current_town", "slot_village_state", svs_being_raided),
            (str_store_string, s6, "@ The village is being raided."),

        # nothing special happening
        (else_try),
            (party_get_current_terrain, ":cur_terrain", "$current_town"),
            (try_begin),
                (this_or_next | eq, ":cur_terrain", rt_steppe),
                (this_or_next | eq, ":cur_terrain", rt_steppe_forest),
                (this_or_next | eq, ":cur_terrain", rt_desert),
                (eq, ":cur_terrain", rt_desert_forest),
                (set_background_mesh, "mesh_pic_village_s1"),
            (else_try),
                (this_or_next | eq, ":cur_terrain", rt_snow),
                (eq, ":cur_terrain", rt_snow_forest),
                (set_background_mesh, "mesh_pic_village_w1"),
            (else_try),
                (set_background_mesh, "mesh_pic_village_p1"),
            (try_end),
        (try_end),

        # todo: remove this code from here
        (try_begin),
            (eq, "$g_player_raid_complete", 1),
            (assign, "$g_player_raid_complete", 0),
            (jump_to_menu, "mnu_village_loot_complete"),
        (else_try),
            (party_get_slot, ":raider_party", "$current_town", "slot_village_raided_by"),
            (gt, ":raider_party", 0),
        (try_end),

        # todo: remove this code from here
        (try_begin),
            (eq, "$g_leave_town", 1),
            (assign, "$g_leave_town", 0),
            (change_screen_return),
        (try_end),

        # todo: remove this code from here
        (try_begin),
            (store_time_of_day, ":cur_hour"),
            (ge, ":cur_hour", 5),
            (lt, ":cur_hour", 21),
            (assign, "$town_nighttime", 0),
        (else_try),
            (assign, "$town_nighttime", 1),
        (try_end),
        ], [
        ("village_manage", [
            (neg|party_slot_eq, "$current_town", "slot_village_state", svs_looted),
            (neg|party_slot_eq, "$current_town", "slot_village_state", svs_being_raided),
            (neg|party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            (party_slot_eq, "$current_town", "slot_town_lord", "trp_player")
            ], "Manage this village.", [
                (assign, "$g_next_menu", "mnu_village"),
                (jump_to_menu, "mnu_center_manage"),
        ]),

        ("Meet_with_village_elder", [
            (party_slot_eq, "$current_town", "slot_village_state", 0),
            (neg | party_slot_eq, "$current_town", "slot_village_state", svs_looted),
            (neg | party_slot_eq, "$current_town", "slot_village_state", svs_being_raided),
            (neg | party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            ], "Meet with the elder.", [
                (try_begin),
                    (call_script, "script_cf_enter_center_location_bandit_check"),
                (else_try),
                    (party_get_slot, ":conversation_troop", "$current_town", "slot_town_elder"),
                    (call_script, "script_setup_troop_meeting", ":conversation_troop", -1),
                (try_end),
        ]),

        # -> recruit.py
        ("recruit_volunteers", [
            (call_script, "script_cf_village_recruit_volunteers_condition", 0, 0),
            # todo: remove $freelancer_state from here
            (neq, "$freelancer_state", 1), # +freelancer chief #prevents player freelancer brytenwalda

            ], "Recruit Volunteers.", [
            (try_begin),
                (troop_slot_ge, "trp_player", "slot_troop_renown", 30),
                (try_begin),
                   (call_script, "script_cf_enter_center_location_bandit_check"),
                (else_try),
                   (jump_to_menu, "mnu_recruit_volunteers"),
                (try_end),
            (else_try),
                (display_message, "@You need more renown to ask the Village Elder for help.", 0xFFFFAAAA),
            (try_end),
        ]),

        ("village_center", [
            (neg|party_slot_eq, "$current_town", "slot_village_state", svs_looted),
            (neg|party_slot_eq, "$current_town", "slot_village_state", svs_being_raided),
            (neg|party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1)
        ], "Go to the village center.", [
            (try_begin),
                (call_script, "script_cf_enter_center_location_bandit_check"),
            (else_try),
                (party_get_slot, ":village_scene", "$current_town", "slot_castle_exterior"),
                (modify_visitors_at_site,":village_scene"),
                (reset_visitors),
                (party_get_slot, ":village_elder_troop", "$current_town","slot_town_elder"),
                (set_visitor, 11, ":village_elder_troop"),

                (try_begin),
                    (gt, "$g_player_chamberlain", 0),
                    (call_script, "script_dplmc_appoint_chamberlain"),
                    (party_get_slot, ":town_lord", "$current_town", "slot_town_lord"),
                    (eq, ":town_lord", "trp_player"),
                    (set_visitor, 9, "$g_player_chamberlain"),
                (try_end),

                (call_script, "script_init_town_walkers"),

                (try_begin),
                    (check_quest_active, "qst_hunt_down_fugitive"),
                    (neg|is_currently_night),
                    (quest_slot_eq, "qst_hunt_down_fugitive", "slot_quest_target_center", "$current_town"),
                    (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
                    (neg|check_quest_failed, "qst_hunt_down_fugitive"),
                    (set_visitor, 45, "trp_fugitive"),
                (try_end),

                # Bounty hunting
                _create_bounty_visitor("qst_bounty_1", "$bounty_target_1"),
                _create_bounty_visitor("qst_bounty_3", "$bounty_target_2"),
                _create_bounty_visitor("qst_bounty_3", "$bounty_target_3"),
                _create_bounty_visitor("qst_bounty_4", "$bounty_target_4"),
                _create_bounty_visitor("qst_bounty_5", "$bounty_target_5"),
                _create_bounty_visitor("qst_bounty_6", "$bounty_target_6"),

                (set_jump_mission, "mt_village_center"),
                (jump_to_scene, ":village_scene"),
                (change_screen_mission),
            (try_end),
            ], "Door to the village center."),

        ("village_buy_food", [
            (party_slot_eq, "$current_town", "slot_village_state", 0),
            (neg|party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            ], "Buy supplies from the peasants.", [
                (try_begin),
                    (call_script, "script_cf_enter_center_location_bandit_check"),
                (else_try),
                    (party_get_slot, ":merchant_troop", "$current_town", "slot_town_elder"),
                    (change_screen_trade, ":merchant_troop"),
                (try_end),
            ]),

        # -> buy_cattle.py
        ("village_buy_cattle", [
            (party_slot_eq, "$current_town", "slot_village_state", 0),
            (neg|party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            ], "Buy cattle.", [
            (jump_to_menu,"mnu_buy_cattle")
        ]),

        ("village_attack_bandits", [
            (party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            (neg|party_slot_eq, "$current_town", "slot_village_infested_by_bandits", "trp_peasant_woman"),
            ], "Attack the bandits.", [

            (party_get_slot, ":bandit_troop", "$current_town", "slot_village_infested_by_bandits"),
            (party_get_slot, ":scene_to_use", "$current_town", "slot_castle_exterior"),

            (modify_visitors_at_site,":scene_to_use"),
            (reset_visitors),
            (set_visitors, 0, ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
            (set_visitors, 2, "trp_farmer", "$qst_eliminate_bandits_infesting_village_num_villagers"),

            (set_party_battle_mode),

            (set_battle_advantage, 0),
            (assign, "$g_battle_result", 0),

            (set_jump_mission,"mt_village_attack_bandits"),
            (jump_to_scene, ":scene_to_use"),
            (assign, "$g_next_menu", "mnu_village_infest_bandits_result"),

            (jump_to_menu, "mnu_battle_debrief"),
            (assign, "$g_mt_mode", vba_normal),
            (change_screen_mission),
        ]),

        ("village_wait", [
            (party_slot_eq, "$current_town", "slot_center_has_manor", 1),
            (party_slot_eq, "$current_town", "slot_town_lord", "trp_player"),
            ], "Rest here for some time.", [

            (assign,"$auto_enter_town", "$current_town"),
            (assign, "$g_last_rest_center", "$current_town"),

            (try_begin),
                (party_is_active, "p_main_party"),
                (party_get_current_terrain, ":cur_terrain", "p_main_party"),
                (try_begin),
                    (eq, ":cur_terrain", rt_desert),
                    (unlock_achievement, ACHIEVEMENT_SARRANIDIAN_NIGHTS),
                (try_end),
            (try_end),

            (rest_for_hours_interactive, 24 * 7, 5, 1),  # rest while attackable

            (change_screen_return),
        ]),

        ("village_guest_wait", [
            (neg|party_slot_eq, "$current_town", "slot_village_state", svs_looted),
            (neg|party_slot_eq, "$current_town", "slot_village_state", svs_being_raided),
            (neg|party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            (assign,":continue",0),
            (try_begin),
                (ge, "$commoner_trust", 60),
                (assign,":continue", 1),
            (try_end),
            (try_begin),
                (party_slot_eq, "$current_town", "slot_center_has_manor", 1),
                (party_slot_eq, "$current_town", "slot_town_lord", "trp_player"),
                (assign, ":continue", 0),
            (try_end),
            (eq, ":continue", 1),
            ], "The villagers invite you to rest here as their honored guest.", [

            (assign,"$auto_enter_town","$current_town"),
            (assign, "$g_last_rest_center", "$current_town"),
            (rest_for_hours_interactive, 24 * 7, 5, 1), #rest while attackable
            (change_screen_return),
        ]),

        ("dplmc_village_counter_insurgency", [
            (party_slot_eq, "$current_town", "slot_village_infested_by_bandits", "trp_peasant_woman"),
            ], "Counter the insurgency.", [

            (store_random_in_range, ":enmity", -10, -5),
            (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
            (call_script, "script_calculate_battle_advantage"),
            (set_battle_advantage, reg0),
            (set_party_battle_mode),
            (assign, "$g_battle_result", 0),
            (assign, "$g_village_raid_evil", 1), #check
            (set_jump_mission,"mt_village_raid"),
            (party_get_slot, ":scene_to_use", "$current_town", "slot_castle_exterior"),
            (jump_to_scene, ":scene_to_use"),
            (assign, "$g_next_menu", "mnu_dplmc_village_riot_result"),

            (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
            (jump_to_menu, "mnu_battle_debrief"),
            (change_screen_mission),
        ]),

        ("dplmc_village_negotiate",[
            (party_slot_eq, "$current_town", "slot_village_infested_by_bandits", "trp_peasant_woman"),
            ], "Begin negotiations.", [
            (jump_to_menu, "mnu_dplmc_riot_negotiate"),
        ]),

        ("collect_taxes_qst", [
            (party_slot_eq, "$current_town", "slot_village_state", 0),
            (neg|party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            (check_quest_active, "qst_collect_taxes"),
            (quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", "slot_quest_giver_troop"),
            (quest_slot_eq, "qst_collect_taxes", "slot_quest_target_center", "$current_town"),
            (neg|quest_slot_eq, "qst_collect_taxes", "slot_quest_current_state", 4),
            (str_store_troop_name, s1, ":quest_giver_troop"),
            (quest_get_slot, reg5, "qst_collect_taxes", "slot_quest_current_state"),
            ], "{reg5?Continue collecting taxes:Collect taxes} due to {s1}.", [
            (jump_to_menu, "mnu_collect_taxes")
        ]),

        ("train_peasants_against_bandits_qst", [
            (party_slot_eq, "$current_town", "slot_village_state", 0),
            (check_quest_active, "qst_train_peasants_against_bandits"),
            (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
            (quest_slot_eq, "qst_train_peasants_against_bandits", "slot_quest_target_center", "$current_town"),
            ], "Train the peasants.", [
            (jump_to_menu, "mnu_train_peasants_against_bandits")
        ]),

        # -> hostile_actions.py
        ("village_hostile_action", [
            (party_slot_eq, "$current_town", "slot_village_state", 0),
            (neg|party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            (neq, "$players_kingdom", "$g_encountered_party_faction"),
            ], "Take a hostile action.", [
            (jump_to_menu,"mnu_village_hostile_action")
        ]),

        ("village_reports", [
            (eq, "$cheat_mode", 1)
            ], "{!}CHEAT! Show reports.", [
            (jump_to_menu,"mnu_center_reports")]),

        ("village_perform_basic_work", [
            (neg|party_slot_eq, "$current_town", "slot_village_state", svs_looted),
            (neg|party_slot_eq, "$current_town", "slot_village_state", svs_being_raided),
            (neg|party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            # todo: remove this freelancer thing
            (neq, "$freelancer_state", 1), #+freelancer chief #prevents player freelancer brytenwalda
            ], "Perform some very basic work for the village (be farmer).", [

            (display_message, "@ You start performing these hard peasantry basic work.", 0xFF0000),
            (try_begin),
                (troop_slot_ge, "trp_player", "slot_troop_renown", 40),
                (display_message,"@ Like farmer, you lose renown and reputation.", 0xFF0000),
                (call_script, "script_change_troop_renown", "trp_player", -2),
                (call_script, "script_change_player_honor", -1),
            (try_end),

            (rest_for_hours_interactive, 2, 5, 1),
            (change_screen_map),
            (assign, "$g_work_for_village_ongoing", 24),
        ]),

        ("village_leave", [], "Leave...", [(change_screen_return, 0)]),
    ]),
] + [
###rigale chief village work
     (
    "village_basic_work",0,
    "{s3}",
    "none",
    [
        (str_clear,s1),
        (str_clear,s2),
        (str_clear,s3),

        (try_begin),
            (eq, "$g_player_is_captive", 1), #motomataru chief repara
                  (str_store_string,s3,"@ You've been carried off as prisoner. You stop your work."),
              (else_try),
                (party_slot_eq, "$current_town", "slot_village_state", svs_being_raided),
            (str_store_string,s3,"@ The village is being raided. You stop your work."),
        (else_try),
            (party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            (str_store_string,s3,"@ The village is being infested by bandits. You stop your work."),
        (else_try),
            (store_random_in_range,reg1,10,30),
            (add_xp_to_troop, reg1, "trp_player"),
            (store_random_in_range,":item_to_give",1,11),
            (try_begin),
                (eq,":item_to_give",1),(assign,":item_to_give","itm_cheese",1),(else_try),
                (eq,":item_to_give",2),(assign,":item_to_give","itm_sausages",1),(else_try),
                (eq,":item_to_give",3),(assign,":item_to_give","itm_apples",1),(else_try),
                (eq,":item_to_give",4),(assign,":item_to_give","itm_pork",1),(else_try),
                (eq,":item_to_give",5),(assign,":item_to_give","itm_grain",1),(else_try),
                (eq,":item_to_give",6),(assign,":item_to_give","itm_honey",1),(else_try),
                (eq,":item_to_give",7),(assign,":item_to_give","itm_bread",1),(else_try),
                (eq,":item_to_give",8),(assign,":item_to_give","itm_ale",1),(else_try),
                (eq,":item_to_give",9),(assign,":item_to_give","itm_mead",1),(else_try),
                (eq,":item_to_give",10),(assign,":item_to_give","itm_chicken",1),(else_try),
            (try_end),
            (str_store_item_name,s1,":item_to_give"),
            (store_random_in_range,":increase_renown",1,6),
            (try_begin),
                (eq,":increase_renown",1),
                (call_script, "script_change_player_relation_with_center", "$current_town", 1),
                (str_store_string,s2,"@ You improve your renown with this village"),
            (else_try),
                (str_store_string,s2,"@ Alas, you don't improve your renown with this village"),
            (try_end),

            (troop_add_items,"trp_player",":item_to_give",1),
            (str_store_string,s3,"@Here are the results of your hard work: You exhaust yourself, You gain {reg1} xps, you receive some {s1}. {s2}. Peasant life is hard, but you feel good."),
        (try_end),
    ],
    [
      ("continue",[],
      "Continue",[
        (try_begin), #motomataru chief repara
                  (this_or_next|eq, "$g_player_is_captive", 1),
                  (this_or_next|party_slot_eq, "$current_town",      "slot_village_state", svs_being_raided),
                  (party_slot_ge, "$current_town",      "slot_village_infested_by_bandits", 1),
                  (change_screen_return),
              (else_try),
                  (jump_to_menu,"mnu_village"),
              (try_end),
            ]),
      ],
  ),

  (
    "village_hunt_down_fugitive_defeated",0,
    "A heavy blow from the fugitive sends you to the ground, and your vision spins and goes dark.\
 Time passes. When you open your eyes again you find yourself battered and bloody,\
 but luckily none of the wounds appear to be lethal.",
    "none",
    [],
    [
      ("continue",[],"Continue...",[(jump_to_menu, "mnu_village"),]),
    ],
  ),
]


def upgrade_tier(max_trials):
    return StatementBlock(
        # set the tier
        (assign, ":tier", 1),
        (try_for_range, ":unused", 0, max_trials),
            # upgrade with 10% chance
            (store_random_in_range, ":random_no", 0, 100),
            (le, ":random_no", 10),

            # select branch of the ugrade tree
            (store_random_in_range, ":random_no", 0, 2),
            (troop_get_upgrade_troop, ":upgrade_troop_no", ":troop_type", ":random_no"),
            (try_begin),
                # if chosen does not exist, set it to be the first branch.
                (le, ":upgrade_troop_no", 0),
                (troop_get_upgrade_troop, ":upgrade_troop_no", ":troop_type", 0),
            (try_end),

            # confirm that it still exists (i.e. not in the maximum)
            (gt, ":upgrade_troop_no", 0),

            # upgrade troop
            (val_add, ":tier", 1),
            (assign, ":troop_type", ":upgrade_troop_no"),
        (try_end),
    )


scripts = [

    ("update_volunteer_troops_in_village", [
        (store_script_param, ":center_no", 1),

        (party_get_slot, ":player_relation", ":center_no", "slot_center_player_relation"),
        (party_get_slot, ":center_culture", ":center_no", "slot_center_culture"),
        (faction_get_slot, ":troop_type", ":center_culture", "slot_faction_tier_1_troop"),

        (store_div, ":tier_upgrades", ":player_relation", 10),
        upgrade_tier(":tier_upgrades"),

        # multiplier to max recruits
        (assign, ":percent", 100),
        (try_begin), #-40% if not owner
            (neg|party_slot_eq, ":center_no", "slot_town_lord", "trp_player"),
            (val_sub, ":percent", 40),
        (try_end),
        (try_begin), #1%/3 renown
            (troop_get_slot, ":player_renown", "trp_player", "slot_troop_renown"),
            (val_div, ":player_renown", 3),
            (val_add, ":percent", ":player_renown"),
        (try_end),
        (try_begin), #+8% if king
            (faction_get_slot, ":faction_leader", "fac_player_supporters_faction", "slot_faction_leader"),
            (eq, ":faction_leader", "trp_player"),
            (val_add, ":percent", 8),

            (try_begin), #-6% for each point of serfdom
                (faction_get_slot, ":serfdom", "fac_player_supporters_faction", "slot_faction_serfdom"),
                (neq, ":serfdom", 0),
                (val_mul, ":serfdom", 6),
                (val_sub, ":percent", ":serfdom"),
            (try_end),

            (try_begin),  #+7% if king of village
                (store_faction_of_party, ":faction", ":center_no"),
                (eq, ":faction", "fac_player_supporters_faction"),
                (val_add, ":percent", 7),
            (try_end),
        (try_end),
        (val_clamp, ":percent", 0, 201),

        (assign, ":max_recruits", 8),
        (try_begin),
            (ge, ":player_relation", 4),
            (assign, ":max_recruits", ":player_relation"),
            (val_div, ":max_recruits", 2),
            (val_add, ":max_recruits", 6),
        (else_try),
            (lt, ":player_relation", 0),
            (assign, ":max_recruits", 0),
        (try_end),

        # max_recruits *= percentage
        (val_mul, ":max_recruits", ":percent"),
        (val_div, ":max_recruits", 100),

        # reduce number of recruits due to increasing tier
        # max_recruits *= 3/(2+tier)
        (val_mul, ":max_recruits", 3),
        (store_add, ":reduce_by_tier", 2, ":tier"),
        (val_div, ":max_recruits", ":reduce_by_tier"),

        (store_random_in_range, ":recruits", 0, ":max_recruits"),

        (party_set_slot, "p_village_8", "slot_center_volunteer_troop_type", "trp_fresna_recruit"), #anadido en aldea reclutar frisios chief
        (party_set_slot, "p_village_14", "slot_center_volunteer_troop_type", "trp_fresna_recruit"), #anadido en aldea reclutar frisios chief
        (party_set_slot, "p_village_56", "slot_center_volunteer_troop_type", "trp_fresna_recruit"), #anadido en aldea reclutar frisios chief
        (party_set_slot, "p_village_74", "slot_center_volunteer_troop_type", "trp_fresna_recruit"), #anadido en aldea reclutar frisios chief
        (party_set_slot, "p_village_86", "slot_center_volunteer_troop_type", "trp_fresna_recruit"), #anadido en aldea reclutar frisios chief

        (party_set_slot, ":center_no", "slot_center_volunteer_troop_type", ":troop_type"),
        (party_set_slot, ":center_no", "slot_center_volunteer_troop_amount", ":recruits"),
     ]),

    ("update_npc_volunteer_troops_in_village", [
        (store_script_param, ":center_no", 1),
        (party_get_slot, ":center_culture", ":center_no", "slot_center_culture"),
        (faction_get_slot, ":troop_type", ":center_culture", "slot_faction_tier_1_troop"),

        upgrade_tier(5),

        (assign, ":max_recruits", 12),

        # reduce number of recruits due to increasing tier
        # max_recruits *= 3/(2+tier)
        (val_mul, ":max_recruits", 3),
        (store_add, ":amount_random_divider", 2, ":tier"),
        (val_div, ":max_recruits", ":amount_random_divider"),

        (store_random_in_range, ":recruits", 0, ":max_recruits"),

        (party_set_slot, "p_village_8", "slot_center_npc_volunteer_troop_type", "trp_fresna_recruit"), #anadido en aldea reclutar frisios chief
        (party_set_slot, "p_village_14", "slot_center_npc_volunteer_troop_type", "trp_fresna_recruit"), #anadido en aldea reclutar frisios chief
        (party_set_slot, "p_village_56", "slot_center_npc_volunteer_troop_type", "trp_fresna_recruit"), #anadido en aldea reclutar frisios chief
        (party_set_slot, "p_village_74", "slot_center_npc_volunteer_troop_type", "trp_fresna_recruit"), #anadido en aldea reclutar frisios chief
        (party_set_slot, "p_village_86", "slot_center_npc_volunteer_troop_type", "trp_fresna_recruit"), #anadido en aldea reclutar frisios chief

        (party_set_slot, ":center_no", "slot_center_npc_volunteer_troop_type", ":troop_type"),
        (party_set_slot, ":center_no", "slot_center_npc_volunteer_troop_amount", ":recruits"),
    ]),

    # -> bandits_infestation.py
    ("update_villages_infested_by_bandits", [
        (try_for_range, ":village_no", villages_begin, villages_end),
            (try_begin),
                # moves the quest in time
                (check_quest_active, "qst_eliminate_bandits_infesting_village"),
                (quest_slot_eq, "qst_eliminate_bandits_infesting_village", "slot_quest_target_center", ":village_no"),
                (quest_get_slot, ":cur_state", "qst_eliminate_bandits_infesting_village", "slot_quest_current_state"),

                (val_add, ":cur_state", 1),
                (try_begin),
                    (lt, ":cur_state", 4),
                    (quest_set_slot, "qst_eliminate_bandits_infesting_village", "slot_quest_current_state", ":cur_state"),
                (else_try),
                    (party_set_slot, ":village_no", "slot_village_infested_by_bandits", 0),
                    (call_script, "script_abort_quest", "qst_eliminate_bandits_infesting_village", 2),
                (try_end),
            (else_try),
                # moves the quest in time
                (check_quest_active, "qst_deal_with_bandits_at_lords_village"),
                (quest_slot_eq, "qst_deal_with_bandits_at_lords_village", "slot_quest_target_center", ":village_no"),
                (quest_get_slot, ":cur_state", "qst_deal_with_bandits_at_lords_village", "slot_quest_current_state"),

                (val_add, ":cur_state", 1),
                (try_begin),
                    (lt, ":cur_state", 4),
                    (quest_set_slot, "qst_deal_with_bandits_at_lords_village", "slot_quest_current_state", ":cur_state"),
                (else_try),
                    (party_set_slot, ":village_no", "slot_village_infested_by_bandits", 0),
                    (call_script, "script_abort_quest", "qst_deal_with_bandits_at_lords_village", 2),
                (try_end),
            (else_try),
                # starts a new quest with a chance
                (party_set_slot, ":village_no", "slot_village_infested_by_bandits", 0),
                (assign, ":continue", 1),

                # don't start when collect taxes or train peasants is activated here.
                # todo: why isn't this with any quest in the village?
                (try_begin),
                    (check_quest_active, "qst_collect_taxes"),
                    (quest_slot_eq, "qst_collect_taxes", "slot_quest_target_center", ":village_no"),
                    (assign, ":continue", 0),
                (else_try),
                    (check_quest_active, "qst_train_peasants_against_bandits"),
                    (quest_slot_eq, "qst_train_peasants_against_bandits", "slot_quest_target_center", ":village_no"),
                    (assign, ":continue", 0),
                (try_end),
                (eq, ":continue", 1),

                # 3% chance
                (store_random_in_range, ":random_no", 0, 100),
                (lt, ":random_no", 3),

                # select type of bandits
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

                (party_set_slot, ":village_no", "slot_village_infested_by_bandits", ":bandit_troop"),
                #Reduce prosperity of the village by 3: reduce to -1
                (call_script, "script_change_center_prosperity", ":village_no", -1),

                # todo: this global is not being used
                (val_add, "$newglob_total_prosperity_from_bandits", -1),

                (try_begin),
                    (eq, "$cheat_mode", 2),
                    (str_store_party_name, s1, ":village_no"),
                    (display_message, "@{!}DEBUG --{s1} is infested by bandits."),
                (try_end),
            (try_end),
        (try_end),
    ]),
]

simple_triggers = [
    (72, [
        (call_script, "script_update_villages_infested_by_bandits"),
        (try_for_range, ":village_no", villages_begin, villages_end),
            (call_script, "script_update_volunteer_troops_in_village", ":village_no"),
            (call_script, "script_update_npc_volunteer_troops_in_village", ":village_no"),
        (try_end),
    ])
]


menus += hostile_actions.menus + buy_cattle.menus + recruit.menus \
         + bandits_infestation.menus
scripts += recruit.scripts + hostile_actions.scripts

simple_triggers += hostile_actions.simple_triggers
