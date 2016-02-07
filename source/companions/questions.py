from source.header_operations import *
from source.header_common import s5, s11, s12, s14, s17, s18, s21, s22, reg0

from source.header_dialogs import anyone, plyr, repeat_for_parties

from source.module_constants import *


dialogs = [

    # the the entry state of this dialogs
    [anyone, "member_question", [],
     "Very well. What did you want to ask?", "member_question_2", []],

    # this dialog is the only thay uses a different dialog branch (duels).
    [anyone|plyr, "member_question_2", [],
     "I would like to challenge you to a friendly duel.", "duel_accept", []],

    [anyone | plyr, "member_question_2", [],
     "How do you feel about the way things are going in this company?",
     "member_morale", []],

    [anyone, "member_morale", [
        (call_script, "script_npc_morale", "$g_talk_troop"),
    ], "{s21}", "do_member_trade", []],

    [anyone | plyr, "member_question_2", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
    ], "Tell me your story again.", "member_background_recap", []],

    [anyone | plyr, "member_question_2", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (troop_slot_ge, "$g_talk_troop", "slot_troop_home", 1),
        (troop_slot_ge, "$g_talk_troop", "slot_troop_home_recap", 1),
        (troop_slot_ge, "$g_talk_troop", "slot_troop_backstory_b", 1),
        (troop_slot_eq, "$g_talk_troop", "slot_troop_kingsupport_state", 0),
    ], "I suppose you know that I aspire to be {king/queen} of this land?",
     "member_kingsupport_1", []],

    [anyone | plyr, "member_question_2", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
    ], "Do you have any connections that we could use to our advantage?",
     "member_intelgathering_1", []],

    [anyone | plyr, "member_question_2", [
        (faction_slot_eq, "$players_kingdom", "slot_faction_leader", "trp_player"),
    ], "Would you be interested in holding a fief?", "member_fief_grant_1", []],

    [anyone | plyr, "member_question_2", [], "Never mind.", "close_window", []],

]

gather_intel = [

    [anyone, "member_intelgathering_1", [
        (troop_get_slot, ":town_with_contacts", "$g_talk_troop", "slot_troop_town_with_contacts"),
        (str_store_party_name, s17, ":town_with_contacts"),
        (store_faction_of_party, ":contact_town_faction", ":town_with_contacts"),
        (str_store_faction_name, s18, ":contact_town_faction"),

        (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
        (store_add, ":connections_string", "str_npc1_intel_mission", ":npc_no"),
        (str_store_string, s21, ":connections_string"),
    ], "{s21}", "member_intelgathering_3", []],

    [anyone | plyr, "member_intelgathering_3", [],
     "Splendid idea -- you do that.", "member_intelgathering_4", []],

    [anyone | plyr, "member_intelgathering_3", [],
     "Actually, hold off for now.", "do_member_trade", []],

    [anyone, "member_intelgathering_4", [
        (troop_set_slot, "$g_talk_troop", "slot_troop_days_on_mission", 5),
        (troop_set_slot, "$g_talk_troop", "slot_troop_current_mission",
         npc_mission_gather_intel),

        (remove_member_from_party, "$g_talk_troop", "p_main_party"),

        (troop_get_slot, ":string", "$g_talk_troop", "slot_troop_honorific"),
        (str_store_string, s21, ":string"),
    ], "Good. I should be ready to report in about five days. Farewell then, "
       "{s21}, for a little while.", "close_window", []],
]

background_dialogs = [
    [anyone, "member_background_recap", [
        (troop_get_slot, ":first_met", "$g_talk_troop",
         "slot_troop_first_encountered"),
        (str_store_party_name, 20, ":first_met"),
        (troop_get_slot, ":home", "$g_talk_troop", "slot_troop_home"),
        (str_store_party_name, 21, ":home"),
        (troop_get_slot, ":recap", "$g_talk_troop", "slot_troop_home_recap"),
        (str_store_string, 5, ":recap"),
    ], "{s5}", "member_background_recap_2", []],

    [anyone, "member_background_recap_2", [
        (str_clear, 19),
        (troop_get_slot, ":background", "$g_talk_troop", "slot_troop_backstory_b"),
        (str_store_string, 5, ":background"),
    ], "{s5}", "member_background_recap_3", []],

    [anyone, "member_background_recap_3", [
    ], "Then shortly after, I joined up with you.", "do_member_trade", []],
]

king_support_dialogs = [

    # option 1: npc does not like enough the player
    [anyone, "member_kingsupport_1", [
        (troop_get_slot, ":grievances", "$g_talk_troop", "slot_troop_morality_penalties"),
        (gt, ":grievances", 10),
    ], "Um... Yes. I had heard.", "do_member_trade", []],

    # option 2: npc likes the enough player
    [anyone, "member_kingsupport_1", [
        (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
        (store_add, ":string", "str_npc1_kingsupport_1", ":npc_no"),
        (str_store_string, s21, ":string"),
    ], "{s21}", "member_kingsupport_1a", []],

    [anyone | plyr, "member_kingsupport_1a", [
    ], "Would you then support my cause?", "member_kingsupport_2", []],

    [anyone | plyr, "member_kingsupport_1a", [
    ], "Very good. I shall keep that in mind.", "do_member_trade", []],

    # Another companion is already on a mission. Cancel.
    [anyone, "member_kingsupport_2", [
        (assign, ":companion_already_on_mission", -1),
        (try_for_range, ":companion", companions_begin, companions_end),
            (troop_slot_eq, ":companion", "slot_troop_occupation", slto_player_companion),
            (troop_get_slot, ":days_on_mission", ":companion", "slot_troop_days_on_mission"),
            (gt, ":days_on_mission", 17),
            (neg | main_party_has_troop, ":companion"),
            (assign, ":companion_already_on_mission", ":companion"),
        (try_end),

        (gt, ":companion_already_on_mission", -1),
        (troop_get_slot, ":honorific", "$g_talk_troop", "slot_troop_honorific"),
        (str_store_string, s21, ":honorific"),
        (str_store_troop_name, s22, ":companion_already_on_mission"),
    ],
     "I would, {s21}. Moreover, I have a proposal on how I might help you "
     "attain your throne. But you recently sent {s22} off on a similar mission. "
     "Perhaps we should wait for a couple of weeks to avoid drawing too much "
     "attention to ourselves.", "do_member_trade", []],

    # npc explains the plan
    [anyone, "member_kingsupport_2", [
        (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
        (store_add, ":string", "str_npc1_kingsupport_2", ":npc_no"),
        (str_store_string, s21, ":string"),
    ], "{s21}", "member_kingsupport_2a", []],

    # player answers positively
    [anyone | plyr, "member_kingsupport_2a", [
        (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
        (store_add, ":string", "str_npc1_kingsupport_2a", ":npc_no"),
        (str_store_string, s21, ":string"),
    ], "{s21}", "member_kingsupport_3", []],

    # player answers negatively
    [anyone | plyr, "member_kingsupport_2a", [
        (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
        (store_add, ":string", "str_npc1_kingsupport_2b", ":npc_no"),
        (str_store_string, s21, ":string"),

    ], "{s21}", "do_member_trade", []],

    # npc answers positively
    [anyone, "member_kingsupport_3", [
        (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
        (store_add, ":string", "str_npc1_kingsupport_3", ":npc_no"),
        (str_store_string, s21, ":string"),
    ], "{s21}", "member_kingsupport_3a", []],

    # player confirms
    [anyone | plyr, "member_kingsupport_3a", [],
     "Very good. You do that", "member_kingsupport_4", []],

    # player rejects
    [anyone | plyr, "member_kingsupport_3a", [],
     "On second thought, stay with me for a while", "do_member_trade", []],

    # npc leaves party
    [anyone, "member_kingsupport_4", [
        (troop_set_slot, "$g_talk_troop", "slot_troop_days_on_mission", 21),
        (troop_set_slot, "$g_talk_troop", "slot_troop_current_mission", npc_mission_kingsupport),

        (remove_member_from_party, "$g_talk_troop", "p_main_party"),

        (troop_get_slot, ":string", "$g_talk_troop", "slot_troop_honorific"),
        (str_store_string, s21, ":string"),

    ], "Farewell then, {s21}, for a little while", "close_window", []],
]

grant_fief_dialogs = [

    [anyone, "member_fief_grant_1", [],
     "Which fief did you have in mind?", "member_fief_grant_2", []],

    # list all the available fiefs to grant
    [anyone | plyr | repeat_for_parties, "member_fief_grant_2", [
        (store_repeat_object, ":center"),
        (is_between, ":center", centers_begin, centers_end),
        (neq, ":center", "$g_player_court"),
        (store_faction_of_party, ":center_faction", ":center"),
        (eq, ":center_faction", "fac_player_supporters_faction"),
        (neg | party_slot_ge, ":center", "slot_town_lord", active_npcs_begin),
        # ie, owned by player or unassigned
        (str_store_party_name, s11, ":center"),

        ], "{s11}", "member_fief_grant_3", [(store_repeat_object, "$temp")]
     ],

    [anyone | plyr, "member_fief_grant_2", [],
     "Never mind -- there is no fief I can offer.", "do_member_trade", []
     ],

    # make npc a lord (kindom_hero) of player_supporters_faction and assign him
    # the fief
    [anyone, "member_fief_grant_3", [],
     "{s5}", "close_window", [
         (call_script, "script_npc_morale", "$g_talk_troop"),
         (assign, ":npc_morale", reg0),
         (assign, ":fief", "$temp"),

         (remove_member_from_party, "$g_talk_troop", "p_main_party"),

         # if companion is not a kindom_hero, make him one and give him a banner.
         (try_begin),
            (neg | troop_slot_eq, "$g_talk_troop", "slot_troop_occupation", slto_kingdom_hero),

            (assign, ":companion_banner_offset", 0),
            (store_sub, ":companion_banner_offset", "$g_talk_troop", active_npcs_begin),
            (store_add, ":companion_banner_id", companion_banner_begin, ":companion_banner_offset"),

            (troop_set_slot, "$g_talk_troop", "slot_troop_banner_scene_prop", ":companion_banner_id"),
            (troop_set_slot, "$g_talk_troop", "slot_troop_occupation", slto_kingdom_hero),
         (try_end),

         (troop_set_faction, "$g_talk_troop", "fac_player_supporters_faction"),

         (call_script, "script_give_center_to_lord", ":fief", "$g_talk_troop", 0),

         # todo: what does this do?
         (try_begin),
            (faction_slot_eq, "$players_kingdom", "slot_faction_political_issue", ":fief"),
            (faction_set_slot, "$players_kingdom", "slot_faction_political_issue", -1),
         (try_end),

         # If the npc did not have an original faction, set it up.
         (try_begin),
            (troop_slot_eq, "$g_talk_troop", "slot_troop_original_faction", 0),
            (party_get_slot, ":fief_culture", ":fief", "slot_center_original_faction"),
            (troop_set_slot, "$g_talk_troop", "slot_troop_original_faction", ":fief_culture"),
         (try_end),

         # set character initial renown = 15*lvl
         (store_character_level, ":renown", "$g_talk_troop"),
         (val_mul, ":renown", 15),
         # todo: why cap renown at 200?
         (val_max, ":renown", 200),
         (troop_set_slot, "$g_talk_troop", "slot_troop_renown", ":renown"),

         # initial gold = 3600 * (1 + trade/10 + looting/10)
         # todo: gold is created out of no where.
         (assign, ":initial_gold", 3600),
         (store_skill_level, ":modifier", "skl_trade", "$g_talk_troop"),
         (store_skill_level, ":skill_level", "skl_looting", "$g_talk_troop"),
         (val_add, ":modifier", ":skill_level"),
         (val_add, ":modifier", 10),
         (val_mul, ":initial_gold", ":modifier"),
         (val_add, ":initial_gold", 5),  # for rounding
         (val_div, ":initial_gold", 10),
         (troop_set_slot, "$g_talk_troop", "slot_troop_wealth", ":initial_gold"),

         # set troop name
         (str_store_troop_name_plural, s12, "$g_talk_troop"),
         (troop_get_type, ":is_female", "$g_talk_troop"),
         (try_begin),
             # if it is a special female
             (eq, "$g_talk_troop", "trp_npclady2"),
             (str_store_string, s14, "str_tribune_s12"),
         (else_try),
             # if it is female
             (this_or_next | eq, ":is_female", 1),
             (this_or_next | eq, ":is_female", 3),
             (this_or_next | eq, ":is_female", 5),
             (eq, ":is_female", 7),
             (str_store_string, s14, "str_lady_s12"),
         (else_try),
             # if it is male
             (str_store_string, s14, "str_lord_s12"),
         (try_end),
         (troop_set_name, "$g_talk_troop", s14),

         # todo: what is this?
         (unlock_achievement, ACHIEVEMENT_I_DUB_THEE),
         (call_script, "script_check_concilio_calradi_achievement"),

         # add items to troop
         (troop_add_item, "$g_talk_troop", "itm_frankishhorse1", 0),
         (troop_add_item, "$g_talk_troop", "itm_horsecourser2", 0),
         (troop_add_item, "$g_talk_troop", "itm_rednorthmanshirt", 0),
         (troop_add_item, "$g_talk_troop", "itm_mailtunic_brown", 0),
         (troop_add_item, "$g_talk_troop", "itm_bishop_robe1", 0),
         (troop_add_item, "$g_talk_troop", "itm_saxonswordt2", 0),
         (troop_add_item, "$g_talk_troop", "itm_shield_round_19", 0),
         (troop_add_item, "$g_talk_troop", "itm_spear_hvy", 0),

         # convert current morale to an improvement in relations:
         # relation += morale/3 + 10
         (store_div, ":relation_boost", ":npc_morale", 3),
         (val_add, ":relation_boost", 10),
         (call_script, "script_troop_change_relation_with_troop", "$g_talk_troop",
          "trp_player", ":relation_boost"),

         # create answer to player
         # town name -> s17  (all acceptance speeches use s17)
         # npc speech of fief acceptance -> s5
         (str_store_party_name, s17, ":fief"),
         (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
         (store_add, ":speech", "str_npc1_fief_acceptance", ":npc_no"),
         (str_store_string, s5, ":speech"),
     ]],
]

dialogs += gather_intel \
           + background_dialogs \
           + king_support_dialogs \
           + grant_fief_dialogs \
