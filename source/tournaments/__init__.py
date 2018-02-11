from ..header_operations import *
from ..header_common import *
from ..header_dialogs import anyone, plyr
from ..header_game_menus import menu_text_color, mnf_disable_all_keys

from ..module_constants import *

from .scripts import scripts
from .menus import menus


town_menu_options = [
    ("join_tournament", [(neg|is_currently_night),(party_slot_ge, "$current_town", "slot_town_has_tournament", 1),]
       ,"Join the Competition.", #chief cambia sot
       [
           (call_script, "script_fill_tournament_participants_troop", "$current_town", 1),
           (assign, "$g_tournament_cur_tier", 0),
           (assign, "$g_tournament_player_team_won", -1),
           (assign, "$g_tournament_bet_placed", 0),
           (assign, "$g_tournament_bet_win_amount", 0),
           (assign, "$g_tournament_last_bet_tier", -1),
           (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),
           (jump_to_menu, "mnu_town_tournament"),
        ]),
]


simple_triggers = [

    # Updates player odds at tournaments.
    (72,
     [
         (try_for_range, ":cur_center", centers_begin, centers_end),
             (party_get_slot, ":player_odds", ":cur_center", "slot_town_player_odds"),
             (try_begin),
                 (gt, ":player_odds", 1000),
                 (val_mul, ":player_odds", 95),
                 (val_div, ":player_odds", 100),
                 (val_max, ":player_odds", 1000),
             (else_try),
                 (lt, ":player_odds", 1000),
                 (val_mul, ":player_odds", 105),
                 (val_div, ":player_odds", 100),
                 (val_min, ":player_odds", 1000),
             (try_end),
             (party_set_slot, ":cur_center", "slot_town_player_odds", ":player_odds"),
         (try_end),
     ]),

    # create and destroy tournaments
    (24,
    [
        (assign, ":num_active_tournaments", 0),

        (try_for_range, ":center_no", towns_begin, towns_end),
          (party_get_slot, ":has_tournament", ":center_no", "slot_town_has_tournament"),

          (try_begin),
            (eq, ":has_tournament", 1),
            (call_script, "script_fill_tournament_participants_troop", ":center_no", 0),
            (call_script, "script_get_num_tournament_participants"),
            (store_sub, ":needed_to_remove_randomly", reg0, 1),
            (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
            (call_script, "script_sort_tournament_participant_troops"),

            (troop_get_slot, ":winner_troop", "trp_tournament_participants", 0),
            (try_begin),
              (is_between, ":winner_troop", active_npcs_begin, active_npcs_end),
              (str_store_troop_name_link, s1, ":winner_troop"),
              (str_store_party_name_link, s2, ":center_no"),
              (display_message, "@{s1} has won the tournament at {s2}.", color_hero_news),
              (call_script, "script_change_troop_renown", ":winner_troop", 20),
            (try_end),
          (try_end),

          (val_sub, ":has_tournament", 1),
          (val_max, ":has_tournament", 0),
          (party_set_slot, ":center_no", "slot_town_has_tournament", ":has_tournament"),
          (try_begin),
            (gt, ":has_tournament", 0),
            (val_add, ":num_active_tournaments", 1),
          (try_end),
        (try_end),

        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
          (faction_slot_eq, ":faction_no", "slot_faction_ai_state", sfai_feast),

          (faction_get_slot, ":faction_object", ":faction_no", "slot_faction_ai_object"),
          (is_between, ":faction_object", towns_begin, towns_end),

          (party_slot_ge, ":faction_object", "slot_town_has_tournament", 1),
          # continue holding tournaments during the feast
          (party_set_slot, ":faction_object", "slot_town_has_tournament", 2),
        (try_end),

        (try_begin),
          # Add new tournaments with a 30% chance when there are 3 or less.
          (lt, ":num_active_tournaments", 3),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", 30),
          (store_random_in_range, ":random_town", towns_begin, towns_end),
          (store_random_in_range, ":random_days", 12, 15),
          (party_set_slot, ":random_town", "slot_town_has_tournament", ":random_days"),

          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s1, ":random_town"),
            (display_message, "@{!}{s1} is holding a tournament."),
          (try_end),
        (try_end),
    ]),

    # Resets the variable storing a recent position in a tournament.
    (3, [(assign, "$g_player_tournament_placement", 0)]),
]

dialogs = [
    [anyone ,"start", [
        (troop_slot_eq, "$g_talk_troop", "slot_troop_occupation", slto_kingdom_lady),
        (eq, "$g_talk_troop_met", 0),
        (gt, "$g_player_tournament_placement", 4),
        (str_clear, s8),
    ],
     "You must be {playername}. We have just had the honor of watching you "
     "distinguish yourself in the recent tournament{s8}.",
     "lady_meet_end", []
     ],

    [anyone ,"start", [
        (troop_slot_eq,"$g_talk_troop","slot_troop_occupation", slto_kingdom_lady),
        (eq, "$g_talk_troop_met", 0),
        (gt, "$g_player_tournament_placement", 4),
        (ge, "$g_talk_troop_relation", 0),
    ],
     "Ah, {playername}. How spendid it was to see you distinguish yourself in the "
     "recent tournament.",
     "lady_meet_end", []
     ],

    [anyone|plyr,"lady_talk",
     [
         (troop_get_type, ":is_female", "trp_player"),
         (val_mod, ":is_female", 2),	#gender fix chief moto
         (eq, ":is_female", 0),
         (gt, "$g_player_tournament_placement", 3),
         (neg|troop_slot_ge, "trp_player", "slot_troop_spouse", active_npcs_begin),
     ],
     "My lady, I would like to dedicate my successes in this recent tournament "
     "to you", "lady_tournament_dedication_reaction",
     [
         (try_begin),
             (gt, "$g_player_tournament_placement", 3),
             (val_sub, "$g_player_tournament_placement", 3),
             (val_mul, "$g_player_tournament_placement", 2),
         (else_try),
             (assign, "$g_player_tournament_placement", 0),
         (try_end),

         (try_begin),
             (troop_slot_eq, "$g_talk_troop", "slot_lady_used_tournament", 1),
             (val_div, "$g_player_tournament_placement", 3),
             (str_store_string, s9, "str_another_tournament_dedication_oh_i_suppose_it_is_always_flattering"),
         (else_try),
             (troop_slot_eq, "$g_talk_troop", "slot_lord_reputation_type", lrep_conventional),
             (val_mul, "$g_player_tournament_placement", 2),
             (str_store_string, s9, "str_do_you_why_what_a_most_gallant_thing_to_say"),
         (else_try),
             (troop_slot_eq, "$g_talk_troop", "slot_lord_reputation_type", lrep_moralist),
             (val_div, "$g_player_tournament_placement", 2),
             (str_store_string, s9, "str_hmm_i_cannot_say_that_i_altogether_approve_of_such_frivolity_but_i_must_confess_myself_a_bit_flattered"),
         (else_try),
             (str_store_string, s9, "str_why_thank_you_you_are_most_kind_to_do_so"),
         (try_end),

         (call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", "$g_player_tournament_placement"),
         (assign, "$g_player_tournament_placement", 0),
         (troop_set_slot, "$g_talk_troop", "slot_lady_used_tournament", 1),
     ]
     ],

    [anyone, "lady_tournament_dedication_reaction", [],
     "{s9}", "lady_pretalk", []],

    [anyone, "arena_master_ask_tournaments", [],
     "{reg2?There won't be any tournaments any time soon.:"
     "{reg1?Tournaments are:A tournament is} going to be held at {s15}.}",
     "arena_master_talk",
     [
         (assign, ":num_tournaments", 0),
         (try_for_range_backwards, ":town_no", towns_begin, towns_end),
             (party_slot_ge, ":town_no", "slot_town_has_tournament", 1),
             (val_add, ":num_tournaments", 1),
             (try_begin),
                (eq, ":num_tournaments", 1),
                (str_store_party_name, s15, ":town_no"),
             (else_try),
                (str_store_party_name, s16, ":town_no"),
                (eq, ":num_tournaments", 2),
                (str_store_string, s15, "@{s16} and {s15}"),
             (else_try),
                (str_store_string, s15, "@{!}{s16}, {s15}"),
             (try_end),
         (try_end),
         (try_begin),
             (eq, ":num_tournaments", 0),
             (assign, reg2, 1),
         (else_try),
             (assign, reg2, 0),
             (store_sub, reg1, ":num_tournaments", 1),
         (try_end),
     ]
    ],
]


preferences_menu = (
    "tournament_options", menu_text_color(0xFF000000)|mnf_disable_all_keys,
    "Preferences",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger1"),
    ],
    [
        ("disable_avdificultad", [(eq, "$g_avdificultad", 1)],
         "Click to disable extra difficulty.",
         [
             (assign, "$g_avdificultad", 0),
             (jump_to_menu, "mnu_tournament_options"),
         ]),
        ("enable_avdificultad", [(eq, "$g_avdificultad", 0)],
         "Click to enable extra difficulty (you receive double the damage and give half).",
         [
             (assign, "$g_avdificultad", 1),
             (jump_to_menu, "mnu_tournament_options"),
         ]),
        ("tournament_back", [], "Back...",
         [
             (jump_to_menu, "mnu_town_tournament"),
         ]),
    ]
)


arena_master_option = [
    anyone|plyr, "arena_master_talk",
    [(eq, "$arena_tournaments_asked", 0)],
    "Will there be a tournament in nearby towns soon?",
    "arena_master_ask_tournaments",
    [(assign, "$arena_tournaments_asked", 1)]
]
