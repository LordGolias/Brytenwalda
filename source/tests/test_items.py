from source.header_operations import *
from source.header_common import pos1

from source.header_game_menus import mnf_disable_all_keys
from source.module_constants import *


menus = [
    ("test_items", mnf_disable_all_keys,
     "Select situation.", "none", [], [

        ("back", [], "Back", [
            (jump_to_menu, "mnu_tests"),
        ]),

        ("d", [], "Horses", [
            (party_get_position, pos1, "$current_town"),
            (party_set_position, "p_main_party", pos1),

            (try_for_range, ":horse", horses_begin, horses_end),
                (troop_add_item, "trp_player", ":horse", 0),
            (try_end),
            (change_screen_map),
        ]),

        ("d", [], "Shields", [
            (party_get_position, pos1, "$current_town"),
            (party_set_position, "p_main_party", pos1),

            (try_for_range, ":shield", shields_begin, shields_end),
                (troop_add_item, "trp_player", ":shield", 0),
            (try_end),
            (change_screen_map),
        ]),

        ("e", [], "Footwear", [
            (party_get_position, pos1, "$current_town"),
            (party_set_position, "p_main_party", pos1),

            (try_for_range, ":item", footwear_begin, footwear_end),
                (troop_add_item, "trp_player", ":item", 0),
            (try_end),
            (change_screen_map),
        ]),

        ("e", [], "Headwear", [
            (party_get_position, pos1, "$current_town"),
            (party_set_position, "p_main_party", pos1),

            (try_for_range, ":item", headwear_begin, headwear_end),
                (troop_add_item, "trp_player", ":item", 0),
            (try_end),
            (change_screen_map),
        ]),
    ])
]
