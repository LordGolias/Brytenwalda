from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *

from source.statement import StatementBlock

from source.module_constants import *
from source.module_troops import troops

from . import indict_vassal, emissary, change_marshal, grant_fief, persuade, center_captured_lord_advice, replace


consequences_staff_salary = StatementBlock(
    (try_begin),
        (gt, "$g_player_minister", 0),
        (val_add, ":staff_salary", 15),
    (try_end),
)

consequences_deactivate_faction = StatementBlock(
    # todo: confirm this is enough to stop all minister activity (e.g. quests)
    (try_begin),
        (is_between, "$g_player_minister", companions_begin, companions_end),
        (assign, "$npc_to_rejoin_party", "$g_player_minister"),
    (try_end),
    (assign, "$g_player_minister", -1),
)


court_visitor = StatementBlock(
    (try_begin),
        (eq, "$g_player_court", ":center_no"),
        (gt, "$g_player_minister", 0),
        (neg | troop_slot_eq, "trp_player", "slot_troop_spouse", "$g_player_minister"),
        (set_visitor, ":cur_pos", "$g_player_minister"),
        (val_add, ":cur_pos", 1),
    (try_end),
)


dialogs = [

    [anyone, "start", [
        (gt, "$g_talk_troop", 0),
        (eq, "$g_talk_troop", "$g_player_minister"),
        (neg | troop_slot_eq, "trp_player", "slot_troop_spouse", "$g_talk_troop")],
     "I am at your service, {sire/my lady}", "minister_issues", []
    ],

    [anyone, "start", [
        (eq, "$g_talk_troop", "trp_temporary_minister"),
        (neq, "$g_talk_troop", "$g_player_minister")
        ], "It has been an honor to serve you, {sire/my lady}", "close_window", []
    ],

    # Ministerial issues: issues that exist and need to be solved on the spot

    [anyone, "minister_issues", [
        (check_quest_active, "qst_consult_with_minister"),
        (eq, "$g_minister_notification_quest", "qst_resolve_dispute"),

        (setup_quest_text, "qst_resolve_dispute"),

        (quest_get_slot, ":lord_1", "qst_resolve_dispute", "slot_quest_target_troop"),
        (str_store_troop_name, s11, ":lord_1"),

        (quest_get_slot, ":lord_2", "qst_resolve_dispute", "slot_quest_object_troop"),
        (str_store_troop_name, s12, ":lord_2"),

        (str_store_string, s2, "str_resolve_the_dispute_between_s11_and_s12"),
        (call_script, "script_start_quest", "qst_resolve_dispute", -1),
        (quest_set_slot, "qst_resolve_dispute", "slot_quest_expiration_days", 30),
        (quest_set_slot, "qst_resolve_dispute", "slot_quest_giver_troop", "$g_player_minister"),
        (quest_set_slot, "qst_resolve_dispute", "slot_quest_target_state", 0),
        (quest_set_slot, "qst_resolve_dispute", "slot_quest_object_state", 0),

        (quest_get_slot, ":lord_1", "qst_resolve_dispute", "slot_quest_target_troop"),  # this block just to check if the slots work
        (str_store_troop_name, s11, ":lord_1"),
        (quest_get_slot, ":lord_2", "qst_resolve_dispute", "slot_quest_object_troop"),
        (str_store_troop_name, s12, ":lord_2"),
        ], "There is a matter which needs your attention. The quarrel between {s11} and {s12} has esclatated "
           "to a point where it has become unseemly. If you do intervene, you risk offending one of the lords. "
           "However, if you do nothing, you risk appearing weak. Such are the burdens of kingship, {sire/my lady}.",
        "minister_pretalk", [
        (call_script, "script_end_quest", "qst_consult_with_minister"),
    ]],

    [anyone, "minister_issues", [
        (assign, "$g_center_taken_by_player_faction", -1),
        (try_for_range, ":center_no", centers_begin, centers_end),
            (eq, "$g_center_taken_by_player_faction", -1),
            (store_faction_of_party, ":center_faction", ":center_no"),
            (eq, ":center_faction", "fac_player_supporters_faction"),
            (neg | party_slot_ge, ":center_no", "slot_town_lord", 0),
            (assign, "$g_center_taken_by_player_faction", ":center_no"),
        (try_end),
        (is_between, "$g_center_taken_by_player_faction", centers_begin, centers_end),
        (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
        ], "{s1} currently does not have a lord. You may wish to keep it this way, as lords will "
           "sometimes gravitate towards lieges who have land to offer, but for the time being, no one "
           "is collecting any of its rents.", "minister_talk", []
    ],

    [anyone, "minister_issues", [
        (neg | is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
        ], "At this point, there are no particularly urgent matters which need your attention. "
           "I should point out though, sire, that I am not very skilled in the ways of politics, and "
           "that I am anxious to return to private life. If you wish to issue any but the most basic "
           "directives, I suggest appointing a trusted companion in my stead. In the meantime, is "
           "there anything you wish done?", "minister_talk", []
    ],

    center_captured_lord_advice.dialog_option,

    [anyone, "minister_issues", [
        (lt, "$player_right_to_rule", 30),
        ], "If I may offer you a world of advice, my {lord/lady}, it seems that your right to "
           "rule as an independent monarch is not sufficiently recognized, and this may bring "
           "us problems further down the road. It may be advisable to find a kingdom with "
           "whom you have shared interests and seek its recognition, to establish yourself "
           "as an equal with other kings.", "minister_talk", []
    ],

    [anyone, "minister_issues", [],
     "At this point, there are no particularly urgent matters which need your attention. "
     "Is there anything you wish done?", "minister_talk", []
    ],

    [anyone, "minister_pretalk", [], "Is there anything you wish done?", "minister_talk", []],

    [anyone | plyr, "minister_talk", [
        (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
        ], "Do you have any ideas to strengthen our kingdom's unity?", "combined_political_quests", [

        (call_script, "script_get_political_quest", "$g_talk_troop"),
        (assign, "$political_quest_found", reg0),
        (assign, "$political_quest_target_troop", reg1),
        (assign, "$political_quest_object_troop", reg2),
    ]],

    # quest offer gift
    [anyone | plyr, "minister_talk", [
        (check_quest_active, "qst_offer_gift"),
        (quest_slot_eq, "qst_offer_gift", "slot_quest_giver_troop", "$g_talk_troop"),

        (quest_get_slot, ":target_troop", "qst_offer_gift", "slot_quest_target_troop"),
        (str_store_troop_name, s4, ":target_troop"),
        (player_has_item, "itm_furs"),
        (player_has_item, "itm_velvet"),
        ], "I have the materials for {s4}'s gift.", "offer_gift_quest_complete", [
    ]],

    [anyone, "offer_gift_quest_complete", [
        (quest_get_slot, ":target_troop", "qst_offer_gift", "slot_quest_target_troop"),
        (troop_get_type, reg4, ":target_troop"),
        ], "Ah, let me take those. Hopefully this will mend the quarrel between you two. You may wish to "
           "speak to {reg4?her:him}, and see if I had any success.", "close_window", [
        (quest_set_slot, "qst_offer_gift", "slot_quest_current_state", 2),
        (quest_set_slot, "qst_offer_gift", "slot_quest_expiration_days", 365),
        (troop_remove_item, "trp_player", "itm_furs"),
        (troop_remove_item, "trp_player", "itm_velvet"),
        (assign, "$g_leave_encounter", 1),
    ]],

    [anyone | plyr, "minister_talk", [
        (assign, "$political_quest_to_cancel", -1),
        (try_begin),
            (check_quest_active, "qst_offer_gift"),
            (quest_slot_eq, "qst_offer_gift", "slot_quest_giver_troop", "$g_talk_troop"),
            (assign, "$political_quest_to_cancel", "qst_offer_gift"),
            (str_store_string, s10, "str_offer_gift_description"),
        (else_try),
            (check_quest_active, "qst_resolve_dispute"),
            (quest_slot_eq, "qst_resolve_dispute", "slot_quest_giver_troop", "$g_talk_troop"),
            (assign, "$political_quest_to_cancel", "qst_resolve_dispute"),
            (str_store_string, s10, "str_resolve_dispute_description"),
        (try_end),
        (gt, "$political_quest_to_cancel", 0),
        ], "Let's abandon our plan to {s10}.", "minister_cancel_political_quest", [
    ]],

    [anyone, "minister_cancel_political_quest", [],
     "Are you sure you want to drop that idea?", "minister_cancel_political_quest_confirm", []
    ],

    [anyone | plyr, "minister_cancel_political_quest_confirm", [],
     "Yes, I am sure. Let's abandon that idea.", "minister_pretalk", [
        (call_script, "script_abort_quest", "$political_quest_to_cancel", 1),
    ]],

    [anyone | plyr, "minister_cancel_political_quest_confirm", [],
     "Actually, never mind.", "minister_pretalk", []
    ],

    emissary.dialog_option,

    indict_vassal.dialog_option,

    change_marshal.dialog_option,

    [anyone | plyr, "minister_talk", [
        (neg | is_between, "$g_player_minister", active_npcs_begin, active_npcs_end),
        ], "I wish for you to retire as minister.", "minister_replace", []
    ],

    [anyone | plyr, "minister_talk", [
        (is_between, "$g_player_minister", active_npcs_begin, active_npcs_end),
        (neg | troop_slot_eq, "$g_talk_troop", "slot_troop_occupation", slto_kingdom_hero),
        ], "I wish you to rejoin my campaign party.", "minister_replace", []
    ],

    grant_fief.dialog_option,

    [anyone | plyr, "minister_talk", [
        (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),

        # $temp = fief to grant
        (assign, "$temp", -1),
        (try_for_range, ":center", centers_begin, centers_end),
            (eq, "$temp", -1),
            (store_faction_of_party, ":center_faction", ":center"),
            (eq, ":center_faction", "fac_player_supporters_faction"),
            (party_get_slot, ":town_lord", ":center", "slot_town_lord"),
            (try_begin),
                (ge, ":town_lord", active_npcs_begin),
                (store_faction_of_troop, ":town_lord_faction", ":town_lord"),
                (neq, ":town_lord_faction", "fac_player_supporters_faction"),
                (assign, ":town_lord", -1),
            (try_end),
            (lt, ":town_lord", 0),
            (assign, "$temp", ":center"),
        (try_end),
        (gt, "$temp", -1),
        (str_store_party_name, s4, "$temp"),
        ], "I wish to make myself lord of {s4}.", "minister_grant_self_fief", []
    ],

    [anyone, "minister_grant_self_fief", [],
     "As you wish. You shall be lord of {s4}.", "minister_pretalk", [
        # $temp = fief to grant
        (call_script, "script_give_center_to_lord", "$temp", "trp_player", 0),
        (try_begin),
            (faction_slot_eq, "$players_kingdom", "slot_faction_political_issue", "$temp"),
            (faction_set_slot, "$players_kingdom", "slot_faction_political_issue", -1),
        (try_end),
        (str_store_party_name, s4, "$temp"),
    ]],

    persuade.dialog_option,

    [anyone | plyr, "minister_talk", [], "That is all for now.", "close_window", []],
]

dialogs += indict_vassal.dialogs \
    + grant_fief.dialogs \
    + emissary.dialogs \
    + change_marshal.dialogs \
    + persuade.dialogs \
    + center_captured_lord_advice.dialogs \
    + replace.dialogs


def _appoint_options():
    options = []

    spouse = \
        ("appoint_spouse", [
            (troop_slot_ge, "trp_player", "slot_troop_spouse", 1),
            (troop_get_slot, ":player_spouse", "trp_player", "slot_troop_spouse"),
            (neg | troop_slot_eq, ":player_spouse", "slot_troop_occupation", slto_kingdom_hero),
            (str_store_troop_name, s10, ":player_spouse"),
            ], "Appoint your wife, {s10}...", [
            (troop_get_slot, ":player_spouse", "trp_player", "slot_troop_spouse"),
            (assign, "$g_player_minister", ":player_spouse"),
            (jump_to_menu, "mnu_minister_confirm"),
        ])
    options.append(spouse)

    # todo: this is an hack to solve a previous error. Consider reformulating as try_for_parties's dialog with the spouse instead of menu options
    troops_ids = [troop[0] for troop in troops]

    for index in range(troops_ids.index("npc1"), troops_ids.index("companions_end")):
        name = "trp_%s" % troops_ids[index]
        option = \
            ("appoint_%s" % troops_ids[index], [
                (main_party_has_troop, name),
                (str_store_troop_name, s10, name),
                ], "Appoint {s10}", [
                (assign, "$g_player_minister", name),
                (jump_to_menu, "mnu_minister_confirm")
            ])
        options.append(option)

    default = \
        ("appoint_default", [], "Appoint a prominent citizen from the area...", [
            (assign, "$g_player_minister", "trp_temporary_minister"),
            (troop_set_faction, "trp_temporary_minister", "fac_player_supporters_faction"),
            (jump_to_menu, "mnu_minister_confirm"),
        ])

    options.append(default)

    return options


menus = [
    ("notification_player_faction_active", 0,
     "You now possess land in your name, without being tied to any kingdom. This makes you a "
     "monarch in your own right, with your court temporarily located at {s12}. However, the "
     "other kings in Britannia and Hibernia will at first consider you a threat, for if any "
     "upstart warlord can grab a throne, then their own legitimacy is called into question."
     "^^You may find it desirable at this time to pledge yourself to an existing kingdom. "
     "If you want to continue as a sovereign monarch, then your first priority should be "
     "to establish an independent right to rule. You can establish your right to rule "
     "through several means -- marrying into a high-born family, recruiting new lords, "
     "governing your lands, treating with other kings, or dispatching your companions "
     "on missions.^^At any rate, your first step should be to appoint a chief minister "
     "from among your companions, to handle affairs of state. Different companions have "
     "different capabilities.^You may appoint new ministers from time to time. You may "
     "also change the location of your court, by speaking to the minister.", "none", [
        (set_fixed_point_multiplier, 100),
        (position_set_x, pos0, 65),
        (position_set_y, pos0, 30),
        (position_set_z, pos0, 170),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),

        (unlock_achievement, ACHIEVEMENT_CALRADIAN_TEA_PARTY),
        (play_track, "track_coronation"),
        (troop_add_item, "trp_player", "itm_crown_lombardy", 0),

        # select court position
        (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
            (lt, "$g_player_court", walled_centers_begin),
            (store_faction_of_party, ":walled_center_faction", ":walled_center"),
            (eq, ":walled_center_faction", "fac_player_supporters_faction"),

            (assign, "$g_player_court", ":walled_center"),

            (try_begin),
                (troop_get_slot, ":spouse", "trp_player", "slot_troop_spouse"),
                (is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
                (troop_set_slot, ":spouse", "slot_troop_cur_center", "$g_player_court"),
            (try_end),

            (str_store_party_name, s12, "$g_player_court"),
        (try_end),
        ], _appoint_options()
    ),

    ("minister_confirm", 0, "{s9}can be found at your court in {s12}. You should consult periodically, "
                            "to avoid the accumulation of unresolved issues that may sap your authority...",
        "none", [

        (try_begin),
            (eq, "$players_kingdom_name_set", 1),
            (change_screen_return),
        (try_end),
        (try_begin),
            (eq, "$g_player_minister", "trp_temporary_minister"),
            (str_store_string, s9, "str_your_new_minister_"),
        (else_try),
            (str_store_troop_name, s10, "$g_player_minister"),
            (str_store_string, s9, "str_s10_is_your_new_minister_and_"),
        (try_end),
        (try_begin),
            (main_party_has_troop, "$g_player_minister"),
            (remove_member_from_party, "$g_player_minister", "p_main_party"),
        (try_end),
        ], [
        ("continue", [], "Continue...", [
            (start_presentation, "prsnt_name_kingdom"),
        ]),
    ]),
]
