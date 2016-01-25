from source.header_operations import *
from source.header_common import pos1, reg0

from source.header_parties import ai_bhvr_hold
from source.header_game_menus import mnf_disable_all_keys


menus = [
    ("test_battle", mnf_disable_all_keys,
     "Select situation.", "none", [], [

        ("back", [], "Back", [
            (jump_to_menu, "mnu_tests"),
        ]),

        ("d", [], "Alone close to easy bandits.", [
            (party_get_position, pos1, "$current_town"),
            (party_set_position, "p_main_party", pos1),

            # create bandits
            (set_spawn_radius, 1),
            (spawn_around_party, "$current_town", "pt_looters"),
            (assign, ":spawned_bandits", reg0),
            (party_clear, ":spawned_bandits"),
            (party_add_members, ":spawned_bandits", "trp_looter", 2),

            (party_set_ai_behavior, ":spawned_bandits", ai_bhvr_hold),
            (change_screen_map),
        ]),

        ("d", [], "40+40+40 army close to 40 bandits.", [
            (party_get_position, pos1, "$current_town"),
            (party_set_position, "p_main_party", pos1),

            # create bandits
            (set_spawn_radius, 1),
            (spawn_around_party, "$current_town", "pt_looters"),
            (assign, ":spawned_bandits", reg0),
            (party_clear, ":spawned_bandits"),
            (party_add_members, ":spawned_bandits", "trp_looter", 40),

            # add troops
            (party_add_members, "p_main_party", "trp_saxon_infantryt3", 40),
            (party_add_members, "p_main_party", "trp_saxon_archer", 40),
            (party_add_members, "p_main_party", "trp_saxon_horseman1", 40),
            (options_set_battle_size, 1000),

            (party_set_ai_behavior, ":spawned_bandits", ai_bhvr_hold),
            (change_screen_map),
        ]),
    ])
]
