from source.header_operations import *
from source.header_common import pos1

from source.header_game_menus import mnf_disable_all_keys

import test_quest_merchant
import test_battles
import test_items


menus = [
    ("tests", mnf_disable_all_keys,
     "Select test to go to.", "none", [
        (assign, "$debug_game_mode", 1),
        (assign, "$current_town", "p_town_6"),
        (assign, "$g_starting_town", "$current_town"),
        ], [

        ("map", [], "Jump to map", [
            (party_get_position, pos1, "$current_town"),
            (party_set_position, "p_main_party", pos1),
            (change_screen_map),
        ]),

        ("test_quest_merchant", [], "Quest merchant tests", [
            (jump_to_menu, "mnu_test_quest_merchant"),
        ]),

        ("test_battles", [], "Battle tests", [
            (jump_to_menu, "mnu_test_battle"),
        ]),

         ("test_items", [], "Items tests", [
             (jump_to_menu, "mnu_test_items"),
        ]),
    ]),
] + test_quest_merchant.menus \
    + test_battles.menus \
    + test_items.menus \
