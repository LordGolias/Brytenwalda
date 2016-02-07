from source.header_operations import *
from source.header_troops import *
from source.header_skills import *
from source.header_game_menus import mnf_disable_all_keys, menu_text_color

import introduction, tutorial, character_creation, quest_merchant
import game_start_script
import game_quick_start_script
import initialization_scripts


start_menu_0 = \
    ("start_game_0", menu_text_color(0xFF000000) | mnf_disable_all_keys,
     "It rains. It is cold, too cold and for a moment you are afraid... "
     "but then you start to remember who you are.",
     "none",
     [], [
         ("introduction", [], "Prelude",
          [(jump_to_menu, "mnu_introduction_2")]),

         ("continue", [], "Character Creation",
          [(jump_to_menu, "mnu_start_game_1")]),

         ("start_mod", [], "Quick Character (for mod testing)", [
              (assign, "$debug_game_mode", 1),
              (troop_set_type, "trp_player", 0),
              (assign, "$character_gender", tf_male),
              (set_show_messages, 0),

              (troop_add_gold, "trp_player", 43000),
              (troop_raise_attribute, "trp_player", ca_strength, 5),
              (troop_raise_attribute, "trp_player", ca_agility, 5),
              (troop_raise_attribute, "trp_player", ca_intelligence, 5),
              (troop_raise_attribute, "trp_player", ca_charisma, 5),
              (troop_raise_skill, "trp_player", skl_weapon_master, 5),
              (troop_raise_skill, "trp_player", skl_leadership, 5),
              (troop_raise_skill, "trp_player", skl_looting, 5),
              (troop_raise_skill, "trp_player", skl_shield, 20),
              (troop_raise_skill, "trp_player", skl_inventory_management, 5),
              (troop_raise_skill, "trp_player", skl_power_throw, 5),
              (troop_raise_skill, "trp_player", skl_pathfinding, 5),
              (troop_raise_skill, "trp_player", skl_riding, 5),
              (troop_raise_proficiency_linear, "trp_player", wp(100), 10),
              (troop_add_item, "trp_player", "itm_spear2", 1),
              (troop_add_item, "trp_player", "itm_noblearmor21res", 0),
              (troop_add_item, "trp_player", "itm_roman_horse1", 0),
              (troop_equip_items, "trp_player"),

              (add_xp_to_troop, 1000, "trp_player"),
              (troop_set_slot, "trp_player", "slot_troop_renown", 450),
              (set_show_messages, 1),

              (change_screen_map),
          ]),

         ("go_back", [], "Go back", [(jump_to_menu, "mnu_start_game_0")])
     ])

custom_game_menu = (
    "start_game_3", mnf_disable_all_keys,
    "Choose your scenario:",
    "none",
    [
        (assign, "$g_custom_battle_scenario", 0),
        (assign, "$g_custom_battle_scenario", "$g_custom_battle_scenario"),
    ],
    [("go_back", [], "Go back", [(change_screen_quit),])]
)

# the first menu of `first_missions` is the one that the game hard-hiredly goes
# after the menu of skill choice.
# the other menus must also be in this specific order
first_menus = [start_menu_0, quest_merchant.menus[0], custom_game_menu,
               tutorial.menu]

menus = quest_merchant.menus[1:] + character_creation.menus + introduction.menus

scripts = character_creation.scripts \
          + quest_merchant.scripts \
          + game_start_script.scripts \
          + game_quick_start_script.scripts \
          + initialization_scripts.scripts \

dialogs = tutorial.dialogs \
          + quest_merchant.dialogs

mission_templates = quest_merchant.mission_templates
