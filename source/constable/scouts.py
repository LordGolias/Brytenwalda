from source.header_operations import *
from source.header_common import *

from source.header_dialogs import anyone, plyr, repeat_for_factions, repeat_for_parties
from source.header_parties import ai_bhvr_travel_to_point, ai_bhvr_travel_to_party, carries_goods, pf_show_faction, \
    bandit_personality
from source.header_troops import *
from source.header_skills import *
from source.lazy_flag import LazyFlag
from source.module_constants import spt_scout, \
    kingdoms_begin, kingdoms_end, walled_centers_begin, walled_centers_end, \
    towns_begin, towns_end, castles_begin, castles_end

# todo: Make it consistent: the dialog only allows to choose "walled centers"
# but the menu accepts castles and towns.
from source.module_items_shields import shields
from source.module_items_horses import horses

dialog_option = \
    [anyone | plyr, "dplmc_constable_talk", [],
     "I want information about a settlement.", "dplmc_constable_scout_ask", []
    ]

dialogs = [

    # constable talk to hire a scout
    [anyone, "dplmc_constable_scout_ask", [],
     "We can send a spy which will cost you 300 scillingas. Where do you want "
     "to send the spy?", "dplmc_constable_scout_location", []
    ],

    [anyone | plyr | repeat_for_factions, "dplmc_constable_scout_location", [
        (store_troop_gold, ":cur_gold", "trp_household_possessions"),
        (ge, ":cur_gold", 300),
        (store_repeat_object, ":faction"),
        (is_between, ":faction", kingdoms_begin, kingdoms_end),
        (str_store_faction_name, s11, ":faction")
        ], "{!}{s11}.", "dplmc_constable_scout_location_confirm_ask", [
        (store_repeat_object, "$diplomacy_var"),
    ]],

    [anyone | plyr, "dplmc_constable_scout_location", [],
     "I changed my mind.", "dplmc_constable_pretalk", []
    ],

    [anyone, "dplmc_constable_scout_location_confirm_ask", [],
     "Which settlement do you want to infiltrate?", "dplmc_constable_scout_location2", []
    ],

    [anyone | plyr | repeat_for_parties, "dplmc_constable_scout_location2", [
        (store_repeat_object, ":party_no"),
        (is_between, ":party_no", walled_centers_begin, walled_centers_end),
        (store_faction_of_party, ":faction", ":party_no"),
        (eq, ":faction", "$diplomacy_var"),
        (str_store_party_name, s11, ":party_no"),
        ], "{!}{s11}.", "dplmc_constable_scout_location_confirm_ask2", [
        (store_repeat_object, "$diplomacy_var"),
    ]],

    [anyone | plyr, "dplmc_constable_scout_location2", [],
     "I changed my mind.", "dplmc_constable_pretalk", []
    ],

    [anyone, "dplmc_constable_scout_location_confirm_ask2", [
        (str_store_party_name, s11, "$diplomacy_var"),
        ], "As you wish, I will send a spy to {s11} and withdraw 300 scillingas "
           "from your treasury.", "dplmc_constable_scout_location_confirm", []
    ],

    [anyone | plyr, "dplmc_constable_scout_location_confirm", [],
     "Great.", "dplmc_constable_pretalk", [
        (call_script, "script_dplmc_withdraw_from_treasury", 300),
        (call_script, "script_send_scout_party", "$current_town", "$diplomacy_var", "$players_kingdom"),
    ]],

    [anyone | plyr, "dplmc_constable_scout_location_confirm", [],
     "Hold on!", "dplmc_constable_pretalk", []
    ],

    # talk to a moving scout
    ['trp_scout', "start", [], "Sire, I haven't finished my mission yet.", "scout_talk", []],

    [anyone | plyr, "scout_talk", [], "Ok, please go on.", "close_window", []],
]


scripts = [
    ("send_scout_party", [
        (store_script_param, ":start_party", 1),
        (store_script_param, ":target_party", 2),
        (store_script_param, ":faction", 3),

        (set_spawn_radius, 1),
        (spawn_around_party, ":start_party", "pt_scout_party"),
        (assign, ":spawned_party", reg0),
        (party_set_faction, ":spawned_party", ":faction"),
        (party_set_slot, ":spawned_party", "slot_party_type", spt_scout),
        (party_set_slot, ":spawned_party", "slot_party_home_center", ":start_party"),
        (str_store_party_name, s5, ":target_party"),
        (party_set_name, ":spawned_party", "@{s5} scout"),

        (party_add_members, ":spawned_party", "trp_scout", 1),

        (party_get_position, pos1, ":target_party"),
        (map_get_random_position_around_position, pos2, pos1, 1),
        (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_point),
        (party_set_ai_target_position, ":spawned_party", pos2),
        (party_set_slot, ":spawned_party", "slot_party_ai_object", ":target_party"),
        (party_set_slot, ":spawned_party", "slot_party_orders_object", ":target_party"),
        (party_set_aggressiveness, ":spawned_party", 0),
        (party_set_courage, ":spawned_party", 3),
        (party_set_ai_initiative, ":spawned_party", 100),
    ]),
]


simple_triggers = [
    # Scout ai
    (0.2, [
        (try_for_parties, ":party_no"),
            (party_slot_eq, ":party_no", "slot_party_type", spt_scout),

            (get_party_ai_behavior, ":ai_behavior", ":party_no"),
            (this_or_next|eq, ":ai_behavior", ai_bhvr_travel_to_point),
            (eq, ":ai_behavior", ai_bhvr_travel_to_party),

            (party_get_slot, ":target_party", ":party_no", "slot_party_ai_object"),
            (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
            (le, ":distance_to_target", 1),

            (try_begin),
                # spy arrived after successful mission
                (eq, ":target_party", "p_main_party"),

                (party_get_slot, ":mission_target", ":party_no", "slot_party_mission_diplomacy"),
                (call_script, "script_add_notification_menu", "mnu_dplmc_scout", ":mission_target", 0),

                (remove_party, ":party_no"),
            (else_try),
                (neq, ":target_party", "p_main_party"),
                (party_get_slot, ":hours", ":party_no", "slot_party_mission_diplomacy"),

                (try_begin),
                    (le, ":hours", 100),
                    (disable_party, ":party_no"),
                    (val_add, ":hours", 1),
                    (party_set_slot, ":party_no", "slot_party_mission_diplomacy", ":hours"),

                    (try_begin),
                        # spy was caught
                        # todo: 1 every 1000 is basically never. Make it more likely
                        # and dependent on something (spotting, leadership?)
                        (store_random_in_range, ":random", 0, 1000),
                        (eq, ":random", 0),
                        (str_store_party_name, s11, ":target_party"),
                        (display_log_message, "@It is rumoured that a spy has been caught in {s11}.", 0xFF0000),
                        (remove_party, ":party_no"),
                    (try_end),
                (else_try),
                    # successful spying, return to player's party.
                    (enable_party, ":party_no"),
                    (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
                    (party_set_ai_object, ":party_no", "p_main_party"),
                    (party_set_slot, ":party_no", "slot_party_ai_object", "p_main_party"),
                    (party_set_slot, ":party_no", "slot_party_mission_diplomacy", ":target_party"),
                (try_end),
            (try_end),
        (try_end),
    ]),
]

menus = [
    ("dplmc_scout", 0, "Your spy returned from {s10}^^{s11}{s12}", "none", [
        (set_background_mesh, "mesh_pic_messenger1"),
        (str_store_party_name, s10, "$g_notification_menu_var1"),

        (call_script, "script_game_get_center_note", "$g_notification_menu_var1", 0),
        (str_store_string, s11, "@{!}{s0}"),
        (try_begin),
            (this_or_next|is_between, "$g_notification_menu_var1", towns_begin, towns_end),
            (is_between, "$g_notification_menu_var1", castles_begin, castles_end),
            (party_get_slot, ":center_food_store", "$g_notification_menu_var1", "slot_party_food_store"),
            (call_script, "script_center_get_food_consumption", "$g_notification_menu_var1"),
            (assign, ":food_consumption", reg0),
            (store_div, reg6, ":center_food_store", ":food_consumption"),
            (store_party_size, reg5, "$g_notification_menu_var1"),
            (str_store_string, s11, "@{s11}^^ The current garrison consists of {reg5} men.^The food stock lasts for {reg6} days."),
        (try_end),

        (str_clear, s12),
        (party_get_num_attached_parties, ":num_attached_parties", "$g_notification_menu_var1"),
        (try_begin),
            (gt, ":num_attached_parties", 0),
            (str_store_string, s12, "@^^Additional the following parties are currently inside:^"),
            (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
                (party_get_attached_party_with_rank, ":attached_party", "$g_notification_menu_var1", ":attached_party_rank"),
                (str_store_party_name, s3, ":attached_party"),
                (store_party_size, reg1, ":attached_party"),
                (str_store_string, s12, "@{s12} {s3} with {reg1} troops.^"),
            (try_end),
        (try_end),
        (call_script, "script_update_center_recon_notes", "$g_notification_menu_var1"),
        ], [
        ("dplmc_continue",[],"Continue...", [
            (change_screen_return),
        ]),
    ]),
]

troops = [
    ["scout", "Scout", "Scouts", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged, 0, 0, 'fac_neutral', ['itm_leather_gloves1','itm_leather_gloves1','itm_javelins','itm_shoes1','itm_noble_shoesorange','itm_ptunic3','itm_ptunic3','itm_shirtylw','itm_shirtaqua','itm_shirtgrey','itm_bltunicgrn','itm_spear_briton2ht3','itm_spear_briton_longt2','itm_scianswordbone','itm_knife1'] + shields['briton'][1]['heavy'] + horses[1]['light'],def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],
]

party_templates = [
    ("scout_party","Scouts", LazyFlag("icon_gray_knight")|carries_goods(1)|pf_show_faction,0,"fac_commoners",bandit_personality,[]),
]
