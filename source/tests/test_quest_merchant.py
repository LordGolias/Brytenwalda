from source.header_operations import *
from source.header_common import pos0, pos1, reg0

from source.header_game_menus import mnf_disable_all_keys
from source.header_parties import pf_always_visible, ai_bhvr_patrol_location


menus = [
    ("test_quest_merchant", mnf_disable_all_keys,
     "Select situation.", "none", [], [

        ("back", [], "Back", [
            (jump_to_menu, "mnu_tests"),
        ]),

        ("a", [], "Alley fight", [
            (jump_to_menu, "mnu_start_phase_3"),
        ]),

        ("b", [], "At merchant house", [
            (assign, "$g_killed_first_bandit", 1),
            (jump_to_menu, "mnu_b_merchant_house"),
        ]),

        ("c", [], "Next to town after collecting 5 men.", [
            (call_script, "script_start_quest", "qst_collect_men", "$g_talk_troop"),
            (party_add_members, "p_main_party", "trp_briton_recruit", 5),

            (party_get_position, pos1, "$current_town"),
            (party_set_position, "p_main_party", pos1),
            (change_screen_map),
        ]),

        ("d", [], "Next to town after bandit leader appears.", [
            (party_get_position, pos1, "$current_town"),
            (party_set_position, "p_main_party", pos1),

            (call_script, "script_start_quest", "qst_learn_where_merchant_brother_is", "$g_talk_troop"),

            # create bandits
            (set_spawn_radius, 2),
            (spawn_around_party, "$current_town", "pt_leaded_looters"),
            (assign, ":spawned_bandits", reg0),

            (party_get_position, pos0, "$current_town"),
            (party_set_ai_behavior, ":spawned_bandits", ai_bhvr_patrol_location),
            (party_set_ai_patrol_radius, ":spawned_bandits", 2),
            (party_set_ai_target_position, ":spawned_bandits", pos0),
            (change_screen_map),
        ]),

        ("e", [], "Next to town after bandit lair appears.", [
            (party_get_position, pos1, "$current_town"),
            (party_set_position, "p_main_party", pos1),

            (assign, "$lair_neighboor_village", "$current_town"),
            (set_spawn_radius, 2),
            (spawn_around_party, "$lair_neighboor_village", "pt_looter_lair"),
            (party_set_flags, reg0, pf_always_visible, 1),

            (call_script, "script_start_quest", "qst_save_relative_of_merchant", "trp_briton_merchant"),
            (change_screen_map),
        ]),

        ("f", [], "Next to town before town fight.", [
            (party_get_position, pos1, "$current_town"),
            (party_set_position, "p_main_party", pos1),

            (call_script, "script_start_quest", "qst_save_relative_of_merchant", "trp_briton_merchant"),
            (call_script, "script_succeed_quest", "qst_save_relative_of_merchant"),
            (change_screen_map),
        ]),
    ]),
]
