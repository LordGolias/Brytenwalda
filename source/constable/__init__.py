from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *
from source.header_items import ek_body, ek_foot
from source.header_troops import tf_hero, tf_male, knight_attrib_4, wp
from source.header_skills import *

from source.module_constants import *
from source.module_items_footwear import footwear

from source.statement import StatementBlock

from . import patrols, scouts, recruit, train, move_troops, reports, release_prisoner


WEEKLY_COST_OF_CONSTABLE = 15


simple_triggers = [
    (2, [
        (assign, ":has_walled_center", 0),
        (try_for_range, ":center_no", centers_begin, centers_end),
            (party_get_slot, ":lord_troop_id", ":center_no", "slot_town_lord"),
            (eq, ":lord_troop_id", "trp_player"),

            (is_between, ":center_no", walled_centers_begin, walled_centers_end),
            (assign, ":has_walled_center", 1),
            (assign, ":center_no", centers_end),
        (try_end),

        # todo: confirm that this somehow does not leave traces of the constable. (e.g. trainer, recruiter)
        (try_begin),
            (eq, ":has_walled_center", 0),
            (neq, "$g_player_constable", 0),
            (assign, "$g_player_constable", 0),
        (try_end),
    ]),
] \
    + recruit.simple_triggers \
    + scouts.simple_triggers \
    + train.simple_triggers \


triggers = [
    # create notification to appoint constable
    (24, 0, 24 * 13, [], [
        (assign, ":has_fief", 0),
        (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            (party_get_slot, ":lord_troop_id", ":center_no", "slot_town_lord"),
            (eq, ":lord_troop_id", "trp_player"),
            (assign, ":has_fief", 1),
        (try_end),
        (eq, ":has_fief", 1),

        (try_begin),
            (eq, "$cheat_mode", 1),
            (assign, reg0, "$g_player_constable"),
            (display_message, "@{!}DEBUG : constable: {reg0}"),
        (try_end),

        (assign, ":notification", 0),
        (try_begin),
            (eq, "$g_player_constable", 0),
            (assign, ":notification", 1),
        (else_try),
            (neq, "$g_player_constable", -1),
            (neq, "$g_player_constable", "trp_dplmc_constable"),
            (assign, ":notification", 1),
        (try_end),

        (try_begin),
            (eq, ":notification", 1),
            (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_constable", 0, 0),
        (try_end),
    ]),
]


menus = [
    ("dplmc_notification_appoint_constable", 0,
     "As a lord of a fief you can now appoint a constable who resides at you court "
     "for a weekly salary of %d scillingas. He will recruit new troops and provide "
     "information about your army." % WEEKLY_COST_OF_CONSTABLE, "none", [], [

        ("dplmc_appoint_default", [], "Appoint a prominent nobleman from the area.", [
            (call_script, "script_dplmc_appoint_constable"),
            (jump_to_menu, "mnu_dplmc_constable_confirm"),
        ]),

        ("dplmc_continue", [], "Proceed without constable.", [
            (assign, "$g_player_constable", -1),
            (assign, "$g_constable_training_center", -1),
            (change_screen_return),
        ]),
    ]),

    ("dplmc_constable_confirm", 0,
     "Your constable can be found at your court. You should consult him if you "
     "want to recruit new troops or get detailed information about your standing army.", "none", [], [

        ("dplmc_continue", [], "Continue...", [
            (change_screen_return),
        ]),
    ]),
] \
    + scouts.menus


# this block is added to the enter_court script to add the constable to the scene.
court_visitor = StatementBlock(
    (try_begin),
        (gt, "$g_player_constable", 0),
        # todo: this is wrong: appoint constable should not be here
        (call_script, "script_dplmc_appoint_constable"),  #fix for wrong troops after update
        (party_get_slot, ":town_lord", ":center_no", "slot_town_lord"),
        (eq, ":town_lord", "trp_player"),
        (set_visitor, ":cur_pos", "$g_player_constable"),
        (val_add, ":cur_pos", 1),
    (try_end),
)


consequences_give_center = StatementBlock(
    (try_begin),
        (eq, "$g_constable_training_center", ":center_no"),
        (assign, "$g_constable_training_center", -1),
    (try_end),
)


consequences_staff_salary = StatementBlock(
    (try_begin),
        (gt, "$g_player_constable", 0),
        (val_add, ":staff_salary", WEEKLY_COST_OF_CONSTABLE),
    (try_end),
)

scripts = [
    ("dplmc_appoint_constable", [
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_dplmc_coat_of_plates_red_constable"),
        (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_footwear_1c_1"),
        (assign, "$g_player_constable", "trp_dplmc_constable"),
  ]),
] \
    + recruit.scripts \
    + scouts.scripts \
    + move_troops.scripts \


# entry point to appoint constable
appoint_dialog_option = \
    [anyone|plyr, "dplmc_talk_staff", [
        (le, "$g_player_constable", 0),
        (assign, ":has_fief", 0),
        (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            (party_get_slot,  ":lord_troop_id", ":center_no", "slot_town_lord"),
            (eq, ":lord_troop_id", "trp_player"),
            (assign, ":has_fief", 1),
        (try_end),
        (eq, ":has_fief", 1),
        ], "I want to appoint a constable.", "dplmc_talk_appoint_constable", []
    ]

dialogs = [

    # Appoint constable
    [anyone, "dplmc_talk_appoint_constable", [
        (troop_slot_ge, "trp_dplmc_constable", "slot_troop_met", 1),
        ], "I assume you will want to rehire your former constable? "
           "His rate is still %d scillingas each week, and the appointment "
           "will cost us 20 scillingas." % WEEKLY_COST_OF_CONSTABLE,
        "dplmc_talk_appoint_constable_confirm", []
    ],

    [anyone, "dplmc_talk_appoint_constable", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        ], "I have heard good things about a local nobleman, and I believe "
           "he would be well-suited for the job. He demands %d scillingas "
           "each week, though. The appointment will cost us 20 scillingas." % WEEKLY_COST_OF_CONSTABLE,
        "dplmc_talk_appoint_constable_confirm", []
    ],

    [anyone, "dplmc_talk_appoint_constable", [],
     "That's a wise idea. May I suggest a very capable nobleman and friend of my "
     "family? He demands %d scillingas each week, though. The appointment will "
     "cost us 20 scillingas." % WEEKLY_COST_OF_CONSTABLE,
     "dplmc_talk_appoint_constable_confirm", []
    ],

    [anyone | plyr, "dplmc_talk_appoint_constable_confirm", [
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", 20),
        ], "So be it.", "dplmc_talk_appoint_confirm_yes", [
        (call_script, "script_dplmc_appoint_constable"),
        (troop_remove_gold, "trp_player", 20),
    ]],

    [anyone | plyr, "dplmc_talk_appoint_constable_confirm", [
        (troop_get_slot, ":player_spouse", "trp_player", "slot_troop_spouse"),
        (eq, "$g_talk_troop", ":player_spouse"),
        ], "Maybe later.", "spouse_pretalk", []
    ],

    [anyone | plyr, "dplmc_talk_appoint_constable_confirm", [
        (eq, "$g_talk_troop", "$g_player_minister"),
        (troop_get_slot, ":player_spouse", "trp_player", "slot_troop_spouse"),
        (neq, ":player_spouse", "$g_player_minister"),
        ], "Maybe later.", "minister_pretalk", []
    ],

    [anyone, "dplmc_talk_appoint_confirm_yes", [
        (troop_get_slot, ":player_spouse", "trp_player", "slot_troop_spouse"),
        (eq, "$g_talk_troop", ":player_spouse"),
        ], "I will send him a letter he should arrive at the court soon.", "spouse_pretalk", []
    ],

    [anyone, "dplmc_talk_appoint_confirm_yes", [
        (eq, "$g_talk_troop", "$g_player_minister"),
        ], "I will send him a letter he should arrive at the court soon.", "minister_pretalk", []
    ],

    # Constable actions
    [anyone, "start", [
        (eq, "$g_player_constable", "$g_talk_troop"),
        ], "Always at your service!", "dplmc_constable_talk", []
    ],

    [anyone, "dplmc_constable_pretalk", [],
     "Do you need anything else, Sire?", "dplmc_constable_talk", []
    ],

    # faith report
    [anyone | plyr, "dplmc_constable_talk", [],
     "I want a report on the kingdom's faith.", "dplmc_constable_faith", []],

    [anyone, "dplmc_constable_faith", [
        (assign, reg13, "$g_sod_global_faith"),
        ], "Due to reports from our kingdom we managed to convert {reg13} people to our faith.",
     "dplmc_constable_faith1", []
    ],

    [anyone | plyr, "dplmc_constable_faith1", [],
     "It could always be better...", "dplmc_constable_pretalk", []
    ],

    # ask about war
    [anyone | plyr, "dplmc_constable_talk", [], "How goes the war?", "dplmc_constable_talk_ask_war",[]],

    [anyone, "dplmc_constable_talk_ask_war", [], "{s12}", "dplmc_constable_talk_ask_war_2", [
        (assign, ":num_enemies", 0),
        (try_for_range_backwards, ":cur_faction", kingdoms_begin, kingdoms_end),
            (faction_slot_eq, ":cur_faction", "slot_faction_state", sfs_active),
            (store_relation, ":cur_relation", ":cur_faction", "fac_player_supporters_faction"),
            (lt, ":cur_relation", 0),
            (try_begin),
                (eq, ":num_enemies", 0),
                (str_store_faction_name_link, s12, ":cur_faction"),
            (else_try),
                (eq, ":num_enemies", 1),
                (str_store_faction_name_link, s11, ":cur_faction"),
                (str_store_string, s12, "@{s11} and {s12}"),
            (else_try),
                (str_store_faction_name_link, s11, ":cur_faction"),
                (str_store_string, s12, "@{!}{s11}, {s12}"),
            (try_end),
            (val_add, ":num_enemies", 1),
        (try_end),

        (try_begin),
            (eq, ":num_enemies", 0),
            (str_store_string, s12, "@We are not at war with anyone."),
        (else_try),
            (str_store_string, s12, "@We are at war with {s12}."),
        (try_end),
    ]],

    [anyone | plyr | repeat_for_factions, "dplmc_constable_talk_ask_war_2", [
        (store_repeat_object, ":faction_no"),
        (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", "slot_faction_state", sfs_active),
        (store_relation, ":cur_relation", ":faction_no", "fac_player_supporters_faction"),
        (lt, ":cur_relation", 0),
        (str_store_faction_name, s1, ":faction_no")
        ], "Tell me more about the war with {s1}.", "dplmc_constable_talk_ask_war_details", [
        (store_repeat_object, "$faction_requested_to_learn_more_details_about_the_war_against")
    ]],

    [anyone | plyr, "dplmc_constable_talk_ask_war_2", [], "That's all I wanted to know. Thank you.", "dplmc_constable_pretalk",[]],

    [anyone, "dplmc_constable_talk_ask_war_details", [], "{!}{s9}.", "dplmc_constable_talk_ask_war_2", [
        (store_add, ":war_damage_slot", "$faction_requested_to_learn_more_details_about_the_war_against", "slot_faction_war_damage_inflicted_on_factions_begin"),
        (val_sub, ":war_damage_slot", kingdoms_begin),
        (faction_get_slot, ":war_damage_inflicted", "$players_kingdom", ":war_damage_slot"), #Floris 2.52 - Diplo bugfix was "fac_player_supporters_faction"

        (store_add, ":war_damage_slot", "$players_kingdom", "slot_faction_war_damage_inflicted_on_factions_begin"), #Floris 2.52 - Diplo bugfix was "fac_player_supporters_faction"
        (val_sub, ":war_damage_slot", kingdoms_begin),
        (faction_get_slot, ":war_damage_suffered", "$faction_requested_to_learn_more_details_about_the_war_against", ":war_damage_slot"),

        (val_max, ":war_damage_suffered", 1),

        (store_mul, ":war_damage_ratio", ":war_damage_inflicted", 100),
        (val_div, ":war_damage_ratio", ":war_damage_suffered"),

        (try_begin),
            (eq, "$cheat_mode", 1),
            (assign, reg3, ":war_damage_inflicted"),
            (assign, reg4, ":war_damage_suffered"),
            (assign, reg5, ":war_damage_ratio"),
            (display_message, "str_war_damage_inflicted_reg3_suffered_reg4_ratio_reg5"),
        (try_end),

        (str_store_string, s9, "str_error__did_not_calculate_war_progress_string_properly"),
        (try_begin),
            (lt, ":war_damage_inflicted", 5),
            (str_store_string, s9, "str_the_war_has_barely_begun_so_and_it_is_too_early_to_say_who_is_winning_and_who_is_losing"),
        (else_try),
            (gt, ":war_damage_inflicted", 100),
            (gt, ":war_damage_ratio", 200),
            (str_store_string, s9, "str_we_have_been_hitting_them_very_hard_and_giving_them_little_chance_to_recover"),
        (else_try),
            (gt, ":war_damage_inflicted", 80),
            (gt, ":war_damage_ratio", 150),
            (str_store_string, s9, "str_the_fighting_has_been_hard_but_we_have_definitely_been_getting_the_better_of_them"),
        (else_try),
            (gt, ":war_damage_suffered", 100),
            (lt, ":war_damage_ratio", 50),
            (str_store_string, s9, "str_they_have_been_hitting_us_very_hard_and_causing_great_suffering"),
        (else_try),
            (gt, ":war_damage_suffered", 80),
            (lt, ":war_damage_ratio", 68),
            (str_store_string, s9, "str_the_fighting_has_been_hard_and_i_am_afraid_that_we_have_been_having_the_worst_of_it"),
        (else_try),
            (gt, ":war_damage_suffered", 50),
            (gt, ":war_damage_inflicted", 50),
            (gt, ":war_damage_ratio", 65),
            (str_store_string, s9, "str_both_sides_have_suffered_in_the_fighting"),
        (else_try),
            (gt, ":war_damage_ratio", 125),
            (str_store_string, s9, "str_no_clear_winner_has_yet_emerged_in_the_fighting_but_i_think_we_are_getting_the_better_of_them"),
        (else_try),
            (gt, ":war_damage_ratio", 80),
            (str_store_string, s9, "str_no_clear_winner_has_yet_emerged_in_the_fighting_but_i_fear_they_may_be_getting_the_better_of_us"),
        (else_try),
            (str_store_string, s9, "str_no_clear_winner_has_yet_emerged_in_the_fighting"),
        (try_end),

        (try_begin),
            #(neg|faction_slot_eq, "fac_player_supporters_faction", "slot_faction_leader", "$g_talk_troop"),
            (call_script, "script_npc_decision_checklist_peace_or_war", "$players_kingdom", "$faction_requested_to_learn_more_details_about_the_war_against", -1),
            (str_store_string, s9, "str_s9_s14"),
        (try_end),
        ]],

    scouts.dialog_option,

    release_prisoner.dialog_option,

    # report
    [anyone | plyr, "dplmc_constable_talk", [],
     "I want a report.", "dplmc_constable_reports_ask", []
    ],

    [anyone, "dplmc_constable_reports_ask", [],
     "About what do you want to have a report?", "dplmc_constable_reports", []
    ],

    reports.kingdom_option,
    reports.army_option,
    reports.lord_convoy_option,
    reports.garrison_option,

    [anyone | plyr, "dplmc_constable_reports", [],
     "Thank you, that's all for now.", "dplmc_constable_pretalk", []
    ],

    # recruit and train
    [anyone | plyr, "dplmc_constable_talk", [],
     "Let's talk about recruits and training.", "dplmc_constable_recruits_and_training_ask", []
    ],

    [anyone, "dplmc_constable_recruits_and_training_ask", [],
     "Of course.", "dplmc_constable_recruits_and_training", []
    ],

    recruit.dialog_option,
    train.dialog_option,

    [anyone | plyr, "dplmc_constable_recruits_and_training", [],
     "Nevermind", "dplmc_constable_pretalk", []
    ],

    # patrols and troop movement
    [anyone | plyr, "dplmc_constable_talk", [],
     "Let's talk about patrols and troop movement.", "dplmc_constable_security_ask", []
    ],

    [anyone, "dplmc_constable_security_ask", [],
     "Of course.", "dplmc_constable_security", []
    ],

    move_troops.dialog_option,
    patrols.create_option,
    patrols.return_to_center_option,
    patrols.change_target_option,
    patrols.disband_option,

    [anyone | plyr, "dplmc_constable_security", [],
     "Nevermind.", "dplmc_constable_pretalk", []
    ],

    # sell prisoners
    [anyone | plyr, "dplmc_constable_talk", [
        (store_num_regular_prisoners, reg0),
        (ge, reg0, 1)
        ], "I have some prisoners can you sell them for me?", "dplmc_constable_prisoner", []
    ],

    [anyone, "dplmc_constable_prisoner", [],
     "Of course, Sire", "dplmc_constable_pretalk", [
         (change_screen_trade_prisoners)
    ]],

    # dismiss constable
    [anyone | plyr, "dplmc_constable_talk", [],
     "You are dismissed.", "dplmc_constable_dismiss_confirm_ask", []
    ],

    [anyone, "dplmc_constable_dismiss_confirm_ask", [],
     "Are you sure that you don't need me anymore?", "dplmc_constable_dismiss_confirm", []
    ],

    [anyone | plyr, "dplmc_constable_dismiss_confirm", [],
     "Yes I am.", "dplmc_constable_dismiss_confirm_yes", []
    ],

    [anyone, "dplmc_constable_dismiss_confirm_yes", [],
     "As you wish.", "close_window", [
        (assign, "$g_player_constable", -1),
        (assign, "$g_constable_training_center", -1),
    ]],

    [anyone | plyr, "dplmc_constable_dismiss_confirm", [],
     "No I am not.", "dplmc_constable_pretalk", []
    ],

    [anyone | plyr, "dplmc_constable_talk", [],
     "Thank you, I will come back to you later.", "close_window", []
    ],
] \
    + patrols.dialogs \
    + scouts.dialogs \
    + recruit.dialogs \
    + train.dialogs \
    + move_troops.dialogs \
    + reports.dialogs \
    + release_prisoner.dialogs \


troops = [
    ["dplmc_constable", "Constable Sextus", "Constables", tf_hero|tf_male, 0, 0, 'fac_commoners', ['itm_mailbyrniegreen'] + footwear[1]['civilian'], knight_attrib_4, wp(200), knows_common|knows_trainer_9|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_athletics_4, 0x0000000b4b1015054b1b4d591cba28d300000000001e472b0000000000000000]
] \
    + scouts.troops \
    + recruit.troops \

party_templates = scouts.party_templates \
    + recruit.party_templates
