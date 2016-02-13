from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *
from source.header_parties import ai_bhvr_hold, ai_bhvr_travel_to_party, pf_show_faction, merchant_personality
from source.header_troops import *
from source.header_skills import *

from source.lazy_flag import LazyFlag
from source.statement import StatementBlock

from source.module_constants import spt_town, dplmc_spt_recruiter, \
    kingdoms_begin, kingdoms_end, \
    npc_kingdoms_begin, npc_kingdoms_end, \
    svs_looted, svs_being_raided, \
    villages_begin, villages_end, centers_begin, centers_end
from source.module_items_horses import horses

PRICE_TO_RECRUIT = 10
PRICE_PER_RECRUIT = 20


def dialog_recruits_amount(amount):
    return \
        [anyone | plyr, "dplmc_constable_recruit_amount_select", [
            (store_troop_gold, ":gold", "trp_household_possessions"),
            (ge, ":gold", PRICE_TO_RECRUIT + amount * PRICE_PER_RECRUIT)
            ], "%d." % amount, "dplmc_constable_recruit_confirm_ask", [
            (assign, "$diplomacy_var", amount),
        ]]


recruiter_village_conditions = StatementBlock(

    # own village or village from faction with non-negative relations
    (store_faction_of_party, ":village_current_faction", ":village"),
    (store_relation, ":faction_relation", "$players_kingdom", ":village_current_faction"),
    (this_or_next | eq, ":village_current_faction", "$players_kingdom"),
    (ge, ":faction_relation", 0),

    # village with non-negative relations
    (party_get_slot, ":village_relation", ":village", "slot_center_player_relation"),
    (ge, ":village_relation", 0),

    # village with recruits
    (party_get_slot, ":volunteers_in_village", ":village", "slot_center_volunteer_troop_amount"),
    (gt, ":volunteers_in_village", 0),

    # village with correct recruits, if any (i.e. != -1)
    (party_get_slot, ":village_faction", ":village", "slot_center_original_faction"),
    (this_or_next | eq, ":recruit_faction", -1),
    (eq, ":village_faction", ":recruit_faction"),

    # village not under fire
    (neg | party_slot_eq, ":village", "slot_village_state", svs_looted),
    (neg | party_slot_eq, ":village", "slot_village_state", svs_being_raided),
    (neg | party_slot_ge, ":village", "slot_village_infested_by_bandits", 1),
)


dialog_option = \
    [anyone | plyr, "dplmc_constable_recruits_and_training", [],
     "I want to recruit new soldiers.", "dplmc_constable_recruit", []
    ]

dialogs = [

    [anyone, "dplmc_constable_recruit", [
        (le, "$g_player_chamberlain", 0),
        ], "We need a treasury to recruit new soldiers. You have to appoint a "
           "chamberlain first.", "dplmc_constable_pretalk", []
    ],

    [anyone, "dplmc_constable_recruit", [
        (gt, "$g_player_chamberlain", 0),
        (assign, ":recruiter_amount", 0),

        (try_begin),
            (party_slot_eq, "$current_town", "slot_party_type", spt_town),
            (assign, ":max_recruiters", 4),
            (assign, reg0, 1),
        (else_try),
            (assign, ":max_recruiters", 2),
            (assign, reg0, 0),
        (try_end),

        (try_for_parties, ":party_no"),
            (party_slot_eq, ":party_no", "slot_party_type", dplmc_spt_recruiter),
            (party_slot_eq, ":party_no", "slot_party_recruiter_origin", "$current_town"),
            (val_add, ":recruiter_amount", 1),
        (try_end),

        (ge, ":recruiter_amount", ":max_recruiters"),
        ], "You have already hired the maximum amount of {reg0?4:2} recruiters from "
           "this {reg0?town:castle}.", "dplmc_constable_pretalk", []
    ],

    [anyone, "dplmc_constable_recruit", [
        (gt, "$g_player_chamberlain", 0),
        (assign, ":recruiter_amount", 0),

        (try_begin),
            (party_slot_eq, "$current_town", "slot_party_type", spt_town),
            (assign, ":max_recruiters", 4),
        (else_try),
            (assign, ":max_recruiters", 2),
        (try_end),

        (try_for_parties, ":party_no"),
            (party_slot_eq, ":party_no", "slot_party_type", dplmc_spt_recruiter),
            (party_slot_eq, ":party_no", "slot_party_recruiter_origin", "$current_town"),
            (val_add, ":recruiter_amount", 1),
        (try_end),
        (lt, ":recruiter_amount", ":max_recruiters"),
        ], "If you want, I will send someone to visit the villages and recruit their "
           "population to your forces. After he has collected the amount you ordered "
           "he returns to this {reg0?town:castle} and puts the recruits in the garrison. "
           "There's a limit for concurrent recruiters, which is 2 for castles "
           "and 4 for towns. What kind of recruits do you want?",
        "dplmc_constable_recruit_select", []
    ],

    [anyone | plyr | repeat_for_factions, "dplmc_constable_recruit_select", [
        (store_repeat_object, ":faction_no"),
        (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
        (str_store_faction_name, s11, ":faction_no"),
        ], "{s11}.", "dplmc_constable_recruit_amount", [
        (store_repeat_object, ":faction_no"),
        (assign, "$temp", ":faction_no"),
    ]],

    [anyone, "dplmc_constable_recruit_amount", [],
     "You have to pay %d scillingas for each recruit and %d scillingas for the "
     "recruiter. I will take the money from the treasury. How many recruits "
     "are you willing to pay for?" % (PRICE_PER_RECRUIT, PRICE_TO_RECRUIT),
     "dplmc_constable_recruit_amount_select", []
    ],

    dialog_recruits_amount(5),
    dialog_recruits_amount(10),
    dialog_recruits_amount(20),
    dialog_recruits_amount(30),
    dialog_recruits_amount(40),
    dialog_recruits_amount(50),

    [anyone | plyr, "dplmc_constable_recruit_amount_select", [],
     "None.", "dplmc_constable_pretalk", []
    ],

    [anyone | plyr, "dplmc_constable_recruit_confirm_ask", [
        (assign, reg2, "$diplomacy_var"),
        (str_store_string, s6, "@{!}{reg2}"),
        (store_sub, ":offset", "$temp", "fac_kingdom_1"),
        (val_add, ":offset", "str_kingdom_1_adjective"),
        (str_store_string, s11, ":offset"),
        ], "Do you really want to recruit {s6} peasants?",
        "dplmc_constable_recruit_confirm", []
    ],

    [anyone | plyr, "dplmc_constable_recruit_confirm", [],
     "Yes.", "dplmc_constable_pretalk", [
         (call_script, "script_dplmc_send_recruiter", "$diplomacy_var", "$temp"),
    ]],

    [anyone | plyr, "dplmc_constable_recruit_confirm", [],
     "No.", "dplmc_constable_pretalk", []
    ],

    [anyone | plyr, "dplmc_constable_recruits_and_training", [],
     "I changed my mind.", "dplmc_constable_pretalk", []
    ],
]

dialogs += [

    ['trp_recruiter', "start", [],
     "Hello {reg65?madame:sir}. If it's ok with you, I would like to get "
     "on with my assignment.", "dplmc_recruiter_talk", []
    ],

    [LazyFlag('trp_recruiter') | plyr, "dplmc_recruiter_talk", [],
     "Ok, keep going.", "close_window", [
         (assign, "$g_leave_encounter", 1)
    ]],
   
    [LazyFlag('trp_recruiter') | plyr, "dplmc_recruiter_talk", [],
     "I want you to recruit different soldiers.", "dplmc_recruiter_talk_2", []
    ],
   
    ['trp_recruiter', "dplmc_recruiter_talk_2", [
        (party_get_slot, reg1, "$g_encountered_party", "slot_party_recruiter_needed_recruits"),
        (party_get_slot, ":recruit_faction", "$g_encountered_party", "slot_party_recruiter_needed_recruits_faction"),

        (store_sub, ":offset", ":recruit_faction", "fac_kingdom_1"),
        (val_add, ":offset", "str_kingdom_1_adjective"),
        (str_store_string, s1, ":offset"),    
        ], "My current task is to recruit {reg1} {s1} troops for you. Should I recruit "
           "different soldiers from now on?", "dplmc_recruiter_talk_3", []
    ],
   
    [LazyFlag('trp_recruiter') | plyr, "dplmc_recruiter_talk_3", [],
     "No, keep going.", "close_window", [
         (assign, "$g_leave_encounter", 1)
    ]],

    # todo: this loops over `npc_kingdoms_begin`, but loop above is over `kingdoms_begin`
    [LazyFlag('trp_recruiter') | plyr | repeat_for_factions, "dplmc_recruiter_talk_3", [
        (store_repeat_object, ":faction_no"),
        (is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
        (store_sub, ":offset", ":faction_no", "fac_kingdom_1"),
        (val_add, ":offset", "str_kingdom_1_adjective"),
        (str_store_string, s11, ":offset"),    
        ], "{s11}.", "dplmc_recruiter_talk_4", [
        (store_repeat_object, ":faction_no"),
        (assign, "$temp", ":faction_no"),
    ]],

    [LazyFlag('trp_recruiter') | plyr, "dplmc_recruiter_talk_3", [],
     "Recruit any troops.", "dplmc_recruiter_talk_4", [
        (assign, "$temp", -1)
    ]],
 
    ['trp_recruiter', "dplmc_recruiter_talk_4", [
        (party_set_slot, "$g_encountered_party", "slot_party_recruiter_needed_recruits_faction", "$temp")
        ], "Sure, {reg65?madame:sir}. I will. Anything else you want?", "dplmc_recruiter_talk", []
    ],
]


scripts = [
    ("dplmc_send_recruiter", [
        (store_script_param, ":number_of_recruits", 1),
        (store_script_param, ":faction_of_recruits", 2),

        (assign, ":expenses", ":number_of_recruits"),
        (val_mul, ":expenses", PRICE_PER_RECRUIT),
        (val_add, ":expenses", PRICE_TO_RECRUIT),

        (call_script, "script_dplmc_withdraw_from_treasury", ":expenses"),
        (set_spawn_radius, 1),
        (spawn_around_party, "$current_town", "pt_recruiter"),
        (assign, ":spawned_party", reg0),
        (party_set_ai_behavior, ":spawned_party", ai_bhvr_hold),
        (party_set_slot, ":spawned_party", "slot_party_type", dplmc_spt_recruiter),
        (party_set_slot, ":spawned_party", "slot_party_recruiter_needed_recruits", ":number_of_recruits"),
        (party_set_slot, ":spawned_party", "slot_party_recruiter_needed_recruits_faction", ":faction_of_recruits"),

        (party_set_slot, ":spawned_party", "slot_party_recruiter_origin", "$current_town"),
        (assign, ":faction", "$players_kingdom"),
        (party_set_faction, ":spawned_party", ":faction"),
    ]),
]

# This block is added to the script `game_event_simulate_battle`.
consequences_battle_lost = StatementBlock(
    (try_begin),
        (party_slot_eq, ":root_defeated_party", "slot_party_type", dplmc_spt_recruiter),

        (assign, ":minimum_distance", 1000000),
        (try_for_range, ":center", centers_begin, centers_end),
            (store_distance_to_party_from_party, ":dist", ":root_defeated_party", ":center"),
            (try_begin),
                (lt, ":dist", ":minimum_distance"),
                (assign, ":minimum_distance", ":dist"),
                (assign, ":nearest_center", ":center"),
            (try_end),
        (try_end),

        (str_clear, s10),
        (try_begin),
            (gt, ":nearest_center", 0),
            (str_store_party_name, s10, ":nearest_center"),
            (str_store_string, s10, "@ near {s10}"),
        (try_end),

        (party_get_slot, reg10, ":root_defeated_party", "slot_party_recruiter_needed_recruits"),
        (party_get_slot, ":party_origin", ":root_defeated_party", "slot_party_recruiter_origin"),
        (str_store_party_name_link, s13, ":party_origin"),
        (display_log_message, "@Your recruiter who was commissioned to recruit {reg10} recruits "
                              "to {s13} has been defeated{s10}!", 0xFF0000),
    (try_end),
)


simple_triggers = [
    (0.5, [
        (try_for_parties, ":party_no"),
            (party_slot_eq, ":party_no", "slot_party_type", dplmc_spt_recruiter),

            (party_get_slot, ":needed", ":party_no", "slot_party_recruiter_needed_recruits"),

            (party_get_num_companion_stacks, ":stacks", ":party_no"),
            (assign, ":destruction", 1),
            (assign, ":quit", 0),

            (try_for_range, ":stack_no", 0, ":stacks"),
                (party_stack_get_troop_id, ":troop_id", ":party_no", ":stack_no"),
                (eq, ":troop_id", "trp_recruiter"),
                (assign, ":destruction", 0),
            (try_end),

            (try_begin),
                (party_get_battle_opponent, ":opponent", ":party_no"),
                (lt, ":opponent", 0),
                (eq, ":destruction", 1),
                (party_get_slot, ":party_origin", ":party_no", "slot_party_recruiter_origin"),
                (str_store_party_name_link, s13, ":party_origin"),
                (assign, reg10, ":needed"),
                (display_log_message, "@Your recruiter who was commissioned to recruit {reg10} "
                                      "recruits to {s13} has been killed!", 0xFF0000),
                (remove_party, ":party_no"),
                (assign, ":quit", 1),
            (try_end),

            (eq, ":quit", 0),

            # todo: vanished why?
            (try_begin),
                (party_get_slot, ":party_origin", ":party_no", "slot_party_recruiter_origin"),
                (store_faction_of_party, ":origin_faction", ":party_origin"),
                (neq, ":origin_faction", "$players_kingdom"),
                (str_store_party_name_link, s13, ":party_origin"),
                (assign, reg10, ":needed"),
                (display_log_message, "@{s13} has been taken by the enemy and your recruiter who "
                                      "was commissioned to recruit {reg10} recruits vanished without a trace!", 0xFF0000),
                (remove_party, ":party_no"),
                (assign, ":quit", 1),
            (try_end),

            (eq, ":quit", 0),

            (party_get_num_companions, ":amount", ":party_no"),
            (val_sub, ":amount", 1),  # the recruiter himself doesn't count.

            (party_get_slot, ":recruit_faction", ":party_no", "slot_party_recruiter_needed_recruits_faction"),

            # If the recruiter has less troops than player ordered, new village will be set as target.
            # todo: why is this outside the try_begin?
            (lt, ":amount", ":needed"),

            (try_begin),
                (get_party_ai_object, ":previous_target", ":party_no"),
                (get_party_ai_behavior, ":previous_behavior", ":party_no"),
                (try_begin),
                    (neq, ":previous_behavior", ai_bhvr_hold),
                    (neq, ":previous_target", -1),
                    (party_set_slot, ":previous_target", "slot_village_reserved_by_recruiter", 0),
                (try_end),

                (assign, ":min_distance", 999999),
                (assign, ":closest_village", -1),
                (try_for_range, ":village", villages_begin, villages_end),
                    (store_distance_to_party_from_party, ":distance", ":party_no", ":village"),
                    (lt, ":distance", ":min_distance"),

                    recruiter_village_conditions,

                    (neg | party_slot_eq, ":village", "slot_village_reserved_by_recruiter", 1),
                    (assign, ":min_distance", ":distance"),
                    (assign, ":closest_village", ":village"),
                (try_end),

                # village found; travel to it.
                (gt, ":closest_village", -1),
                (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
                (party_set_ai_object, ":party_no", ":closest_village"),
                (party_set_slot, ":party_no", "slot_party_ai_object", ":closest_village"),
                (party_set_slot, ":closest_village", "slot_village_reserved_by_recruiter", 1),
            (try_end),

            # conditi
            (party_get_slot, ":village", ":party_no", "slot_party_ai_object"),
            (gt, ":village", -1),
            (store_distance_to_party_from_party, ":distance_from_target", ":party_no", ":village"),

            (try_begin),
                (le, ":distance_from_target", 0),
                recruiter_village_conditions,

                # recruit
                (party_get_slot, ":volunteers_in_village", ":village", "slot_center_volunteer_troop_amount"),
                (party_get_slot, ":village_volunteer_type", ":village", "slot_center_volunteer_troop_type"),
                (assign, ":still_needed", ":needed"),
                (val_sub, ":still_needed", ":amount"),
                (try_begin),
                    (gt, ":volunteers_in_village", ":still_needed"),

                    (assign, ":santas_little_helper", ":volunteers_in_village"),
                    (val_sub, ":santas_little_helper", ":still_needed"),
                    (assign, ":amount_to_recruit", ":volunteers_in_village"),
                    (val_sub, ":amount_to_recruit", ":santas_little_helper"),
                    (assign, ":village_new_volunteer_amount", ":volunteers_in_village"),
                    (val_sub, ":village_new_volunteer_amount", ":amount_to_recruit"),

                    # remove from village
                    (party_set_slot, ":village", "slot_center_volunteer_troop_amount", ":village_new_volunteer_amount"),

                    # add to party
                    (party_add_members, ":party_no", ":village_volunteer_type", ":amount_to_recruit"),

                    # make party search new village
                    (party_set_ai_behavior, ":party_no", ai_bhvr_hold),

                    # make village non-reserved so party does not return here.
                    (party_set_slot, ":village", "slot_village_reserved_by_recruiter", 0),
                (else_try),
                    (le, ":volunteers_in_village", ":still_needed"),
                    (gt, ":volunteers_in_village", 0),

                    (party_set_slot, ":village", "slot_center_volunteer_troop_amount", -1),

                    (party_add_members, ":party_no", ":village_volunteer_type", ":volunteers_in_village"),
                    (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
                    (party_set_slot, ":village", "slot_village_reserved_by_recruiter", 0),
                (else_try),
                    (le, ":volunteers_in_village", 0),
                    (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
                    (party_set_slot, ":village", "slot_village_reserved_by_recruiter", 0),
                (else_try),
                    (display_message, "@ERROR IN THE RECRUITER KIT SIMPLE TRIGGERS!", 0xFF2222),
                    (party_set_slot, ":village", "slot_village_reserved_by_recruiter", 0),
                (try_end),
            (try_end),
        (try_end),

        # bring recruiters to center
        (try_for_parties, ":p_recruiter"),
            (party_slot_eq, ":p_recruiter", "slot_party_type", dplmc_spt_recruiter),

            (party_get_num_companions, ":amount", ":p_recruiter"),
            (val_sub, ":amount", 1),  # the recruiter himself doesn't count
            (party_get_slot, ":needed", ":p_recruiter", "slot_party_recruiter_needed_recruits"),
            (eq, ":amount", ":needed"),

            # set to travel back to town
            (party_get_slot, ":party_origin", ":p_recruiter", "slot_party_recruiter_origin"),
            (try_begin),
                (neg|party_slot_eq, ":p_recruiter", "slot_party_ai_object", ":party_origin"),
                (party_set_slot, ":p_recruiter", "slot_party_ai_object", ":party_origin"),
                (party_set_ai_behavior, ":p_recruiter", ai_bhvr_travel_to_party),
                (party_set_ai_object, ":p_recruiter", ":party_origin"),
            (try_end),

            # if within distance, transfer recruits and remove recruiter
            (try_begin),
                (store_distance_to_party_from_party, ":distance_from_origin", ":p_recruiter", ":party_origin"),
                (le, ":distance_from_origin", 0),
                (party_get_num_companion_stacks, ":stacks", ":p_recruiter"),

                # stack 0 is the recruiter
                (try_for_range, ":stack_no", 1, ":stacks"),
                    (party_stack_get_size, ":size", ":p_recruiter", ":stack_no"),
                    (party_stack_get_troop_id, ":troop_id", ":p_recruiter", ":stack_no"),
                    (party_add_members, ":party_origin", ":troop_id", ":size"),
                (try_end),

                (str_store_party_name_link, s13, ":party_origin"),
                (assign, reg10, ":amount"),
                (display_log_message, "@A recruiter has brought {reg10} recruits to {s13}.", 0x00FF00),
                (remove_party, ":p_recruiter"),
            (try_end),
        (try_end),
    ]),

    # updates the "slot_village_reserved_by_recruiter"
    (12, [
        (try_for_range, ":village", villages_begin, villages_end),
            (party_set_slot, ":village", "slot_village_reserved_by_recruiter", 0),
        (try_end),
    ]),
]


troops = [
    ["recruiter","Recruiter","Recruiter",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,'fac_neutral',['itm_spathaswordt2','itm_leather_tunic1','itm_leather_boots1','itm_leather_gloves1','itm_pict_crossbow','itm_bolts'] + horses[1]['light'],def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,swadian_face_young_1,swadian_face_old_2],
]

party_templates = [
    ("recruiter", "Recruiter", LazyFlag("icon_gray_knight")|pf_show_faction, 0, "fac_neutral", merchant_personality, [("trp_recruiter", 1, 1)]),
]
