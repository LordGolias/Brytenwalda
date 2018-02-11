from source.header_operations import *
from source.header_common import s1, s16
from source.header_game_menus import mnf_disable_all_keys

from . import a_alley_fight, b_merchant_house, c_merchant_in_tavern, d_find_relative, \
    e_town_fight, f_ending

menus = [
    ("start_phase_2", mnf_disable_all_keys,
     "...Anno Domini 636...\
 ^The world is at war and respects only the law of the sword and spear. Realms are born and die every single day. Kings die on the battlefield.\
 ^In the north and east, the Angles consolidate domains and claim more land. Oswald, the new lord of the north, now rules Bernacia, Deira and Elmet.\
 ^In the south, the Saxons, led by Cynegils, have teamed up with Oswald and cornered Penda, King of the Angles of Mierce, The March. Will Mierce resist being surrounded by enemies? King Penda is bloody and violent -- many kings have been killed by his sword, and it seems his sword will kill many more.\
 ^Meanwhile, Christianity is extending out from Centware, land of the Jutes, converting the barbarians.\
 ^Pushed against the coast, the Welsh are fighting for every inch of land, but they are too divided. Dreaming of a king to unify them all and lead them to final victory, they wish for the return of King Arthur. But Arthur is dead, and all eyes look to Cynddylan, the king of Pengwern.\
 ^ And Gwynedd, the kingdom fertile with great warriors, is silent, unable to hear the sound of the armies advancing to threaten their land. Gwynedd mourns great king Cadwallon, scourge of the Angles and Saxons, who has left a son, a king three year old.\
 ^In the snowy lands of the far north fight the Irish, Dal Riata, and the Picts. Their kings share blood, but the Irish are invading the land of Cait, the Kingdom of the Picts. The Picts, with their faces painted and their female warriors, are now united under one king and are stronger than ever.\
 ^Across the sea, in Ireland, Domnaill mac Aedo of Ui Neill clan has emerged as High King in Temair after defeating his enemies, but it is nothing more than a prestigious title. Although he is called the most powerful of the island, around him clans are fighting for land, women and cattle in fratricidal wars. War in Ireland is endemic.\
 ^Who can bring light to this world of war and misery? The world was chaos, and chaos was war.\
 ^This is... BRYTENWALDA.",
     "none", [
         (set_background_mesh, "mesh_pic_extra_barco")
        ], [

        ("debug_option", [
            (eq, "$debug_game_mode", 1),
            ], "[Debug mode] go to map.", [
            (change_screen_return, 0),
        ]),

        ("town_1", [
            (is_between, "$character_nationality", 13, 19),
            ], "I need go to Alt Clut, in the Briton Kingdom of Alt Clut.", [
            (assign, "$current_town", "p_town_6"),
            (assign, "$g_starting_town", "$current_town"),
            (assign, "$g_journey_string", "str_journey_to_praven"),
            (jump_to_menu, "mnu_start_phase_2_5"),
        ]),

        ("town_2", [
            (neg | is_between, "$character_nationality", 13, 22),
            ], "I need go to Grantebrycge, in the Angle Kingdom of the East Englas", [
            (assign, "$current_town", "p_town_8"),
            (assign, "$g_starting_town", "$current_town"),
            (assign, "$g_journey_string", "str_journey_to_reyvadin"),
            (jump_to_menu, "mnu_start_phase_2_5"),
        ]),

        ("town_3", [
            (is_between, "$character_nationality", 16, 19),
            ], "I need go to Din Gonwy, in the Briton kingdom of Gwynedd.", [
            (assign, "$current_town", "p_town_13"),
            (assign, "$g_starting_town", "$current_town"),
            (assign, "$g_journey_string", "str_journey_to_tulga"),
            (jump_to_menu, "mnu_start_phase_2_5"),
        ]),

        ("town_4", [
            (neg | is_between, "$character_nationality", 13, 22),
            ], "I need go to Cantwaraburh, in the Christian Kingdom of Centware.", [
            (assign, "$current_town", "p_town_1"),
            (assign, "$g_starting_town", "$current_town"),
            (assign, "$g_journey_string", "str_journey_to_sargoth"),
            (jump_to_menu, "mnu_start_phase_2_5"),
        ]),

        ("town_5", [
            (is_between, "$character_nationality", 19, 22),  # Irish
            ], "I need go to Clochair, in the Irish Kingdom of Airgialla.", [
              (assign, "$current_town", "p_town_40"),
              (assign, "$g_starting_town", "$current_town"),
              (assign, "$g_journey_string", "str_journey_to_jelkala"),
              (jump_to_menu, "mnu_start_phase_2_5"),
          ]),

        ("town_6", [
            (is_between, "$character_nationality", 19, 22),
            ], "I need go to Dun Iasgach, in the Irish kingdom of Mumain.", [
            (assign, "$current_town", "p_town_35"),
            (assign, "$g_starting_town", "$current_town"),
            (assign, "$g_journey_string", "str_journey_to_shariz"),
            (jump_to_menu, "mnu_start_phase_2_5"),
        ]),
    ]),

    ("start_phase_2_5", mnf_disable_all_keys, "{!}{s16}", "none", [
        (str_store_party_name, s1, "$g_starting_town"),
        (str_store_string, s16, "$g_journey_string"),
        (set_background_mesh, "mesh_pic_extra_barco"),
        ], [
        ("continue", [], "Continue...", [(jump_to_menu, "mnu_start_phase_3")]),
    ]),
] + a_alley_fight.menus + b_merchant_house.menus


dialogs = a_alley_fight.dialogs + b_merchant_house.dialogs \
    + c_merchant_in_tavern.dialogs + d_find_relative.dialogs \
    + e_town_fight.dialogs + f_ending.dialogs


mission_templates = a_alley_fight.mission_templates + \
                    b_merchant_house.mission_templates \
                    + e_town_fight.mission_templates \

lair_mission_templates_triggers = d_find_relative.lair_mission_templates_triggers

scripts = b_merchant_house.scripts + e_town_fight.scripts
