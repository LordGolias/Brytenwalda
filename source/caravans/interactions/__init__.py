from source.header_common import s9
from source.header_dialogs import anyone, plyr
from source.module_constants import *
from source.header_operations import *

from . import attack, attack_quest, demand_toll, journey_explanation, escort_quest

_start_dialogs = [

    # the caravan being escorted (continues in `escort_quest.py`)
    [anyone, "start", [
        (eq, "$caravan_escort_state", 1),
        (eq, "$g_encountered_party", "$caravan_escort_party_id"),
        (eq, "$talk_context", tc_party_encounter),
        ], "We've made it this far... Is everything clear up ahead?",
     "talk_caravan_escort", []
     ],

    # meet a caravan that recently paid.
    [anyone, "start", [
        (eq, "$talk_context", tc_party_encounter),
        (eq, "$g_encountered_party_type", spt_kingdom_caravan),
        (party_slot_ge, "$g_encountered_party", "slot_party_last_toll_paid_hours", "$g_current_hours"),
    ], "What do you want? We paid our toll to you less than three days ago.",
     "merchant_talk", []],

    # meet a caravan that recently paid.
    [anyone, "start", [
        (eq, "$talk_context", tc_party_encounter),
        (eq, "$g_encountered_party_type", spt_kingdom_caravan),
        (party_slot_ge, "$g_encountered_party", "slot_party_last_toll_paid_hours", "$g_current_hours"),
    ], "What do you want? We paid our toll to you less than three days ago.",
     "merchant_talk", []],

    # meet a friendly caravan
    [anyone, "start", [
        (eq, "$talk_context", tc_party_encounter),
        (eq, "$g_encountered_party_type", spt_kingdom_caravan),
        (ge, "$g_encountered_party_relation", 0)],
     "Hail, friend.", "merchant_talk", []],

    # meet an enemy merchant caravan (fac_merchants)
    # todo: are these ever spawn?
    [anyone, "start", [
        (eq, "$talk_context", tc_party_encounter),
        (eq, "$g_encountered_party_type", spt_kingdom_caravan),
        (lt, "$g_encountered_party_relation", 0),
        (eq, "$g_encountered_party_faction", "fac_merchants"),
    ],
     "What do you want? We are but simple merchants, we've no quarrel with you, "
     "so leave us alone.", "merchant_talk", []],

    # meet a caravan from a faction at war
    [anyone, "start", [
        (eq, "$talk_context", tc_party_encounter),
        (eq, "$g_encountered_party_type", spt_kingdom_caravan),
        (lt, "$g_encountered_party_relation", 0),
        (faction_get_slot, ":faction_leader", "$g_encountered_party_faction", "slot_faction_leader"),
        (str_store_troop_name, s9, ":faction_leader"),
    ], "Be warned, knave! This caravan is under the protection of {s9}. Step out "
       "of our way or you will face his fury!", "merchant_talk", []],

    # catch all cases
    # todo: does this ever happen?
    [anyone, "start", [
        (party_slot_eq, "$g_encountered_party", "slot_party_type", spt_kingdom_caravan),
        (this_or_next | eq, "$talk_context", tc_party_encounter),
        (eq, "$talk_context", 0)
        ], "Yes? What do you want?", "merchant_talk", []
     ],

    # to create a loop in the merchant talk
    [anyone, "merchant_pretalk", [], "Anything else?", "merchant_talk", []],
]

_talk_dialogs = [

    # todo: quest related move to somewhere else.
    [anyone | plyr, "merchant_talk", [
         (check_quest_active, "qst_track_down_bandits"),
        ], "I am hunting a group of bandits with the following description... "
       "Have you seen them?", "merchant_bandit_information", []
    ],

    # todo: quest related move to somewhere else.
    # bandit information
    [anyone, "merchant_bandit_information", [
        (call_script, "script_get_manhunt_information_to_s15", "qst_track_down_bandits"),
        ], "{s15}", "merchant_pretalk", []
    ],

    # journey explanation
    [anyone | plyr, "merchant_talk", [
        (eq, "$talk_context", tc_party_encounter),
    ], "Tell me about your journey", "merchant_trip_explanation", []],

    # offer something
    [anyone | plyr, "merchant_talk", [
        (le, "$talk_context", tc_party_encounter),
        (eq, "$g_encountered_party_faction", "$players_kingdom")
        ], "I have an offer for you.", "merchant_talk_offer", []],

    # demand something
    [anyone | plyr, "merchant_talk", [
        (eq, "$talk_context", tc_party_encounter),
        (party_slot_lt, "$g_encountered_party", "slot_party_last_toll_paid_hours", "$g_current_hours")
        ], "I demand something from you!", "merchant_demand", []
     ],

    # if nothing, allow to leave.
    [anyone | plyr, "merchant_talk", [], "[Leave]", "close_window", [
        (assign, "$g_leave_encounter", 1)
    ]],
]


_demand_dialogs = [

    # answer to demand request
    [anyone, "merchant_demand", [
        (eq, "$talk_context", tc_party_encounter),
        ], "What do you want?", "merchant_demand_2", []
     ],

    # see `attack` module
    [anyone | plyr, "merchant_demand_2", [
        (neq, "$g_encountered_party_faction", "$players_kingdom")
        ], "Hand over your gold and valuables now!", "merchant_attack_begin", []
     ],

    # see `demand_toll` module
    [anyone | plyr, "merchant_demand_2", [
        (neq, "$g_encountered_party_faction", "$players_kingdom"),
        ],
     "There is a toll for free passage here!", "merchant_demand_toll", []
     ],

    [anyone | plyr, "merchant_demand_2", [], "Nothing. Forget it.",
     "merchant_pretalk", []
     ],
]

_offer_dialogs = [
    [anyone, "merchant_talk_offer", [], "What is it?",
     "merchant_talk_offer_2", []
     ],

    # offer protection
    [anyone | plyr, "merchant_talk_offer_2", [
        (eq, "$talk_context", tc_party_encounter),
        (eq, "$g_encountered_party_faction", "$players_kingdom"),
        (eq, "$caravan_escort_state", 0),
    ], "I can escort you to your destination for a price.",
       "caravan_offer_protection", []],

    # offer trade
    [anyone | plyr, "merchant_talk", [],
     "I'd like to trade goods with you.", "merchant_talk_offer_goods", []],

    # offer trade accepted
    [anyone, "merchant_talk_offer_goods", [],
     "Hmm. We don't normally pick up goods on the road, but...^I see that "
     "you have some goods worth buying.^Let us make an offer.",
     "merchant_pretalk", [
         (try_begin),
             (eq, "$g_caravan_master_gold_refilled", 0),
             (store_troop_gold, ":cur_gold", "trp_caravan_master"),
             (lt, ":cur_gold", 1000),
             (store_random_in_range, ":new_gold", 1000, 5000),
             (call_script, "script_troop_add_gold", "trp_caravan_master", ":new_gold"),
             (assign, "$g_caravan_master_gold_refilled", 1),
         (try_end),
         (change_screen_trade, "trp_caravan_master")]],

    [anyone | plyr, "merchant_talk_offer_2", [], "Nothing. Forget it",
     "merchant_pretalk", []],
]

simple_triggers = [
    # avoids the caravan master to be an infinite source of money
    # by only making him receive money every 3 hours.
    # todo: make this a consequence of its profit.
    (6, [(assign, "$g_caravan_master_gold_refilled", 0)])
]

dialogs = _start_dialogs + _talk_dialogs + _offer_dialogs + _demand_dialogs \
          + escort_quest.dialogs \
          + demand_toll.dialogs \
          + attack.dialogs \
          + journey_explanation.dialogs \

simple_triggers += escort_quest.simple_triggers
triggers = escort_quest.triggers
scripts = []
