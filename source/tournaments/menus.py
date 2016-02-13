from ..header_operations import *
from ..header_common import *
from ..header_game_menus import mnf_disable_all_keys

from ..module_constants import *


menus = [
(
    "town_tournament_won", mnf_disable_all_keys,
    "You have won the tournament of {s3}! You are filled with pride as the crowd cheers your name. "
    "In addition to honour, fame and glory, you earn a prize of {reg9} scillingas. {s8}",
    "none",
    [
        (try_begin),
            (set_fixed_point_multiplier, 100),
            (position_set_x, pos0, 70),
            (position_set_y, pos0, 30),
            (position_set_z, pos0, 75),
            (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "trp_player", pos0),
        (try_end),
        (str_store_party_name, s3, "$current_town"),
        (call_script, "script_change_troop_renown", "trp_player", 15), #chief aumentado renombre ganado en torneo a 30
        (store_random_in_range, ":rand", 0, 20),

        (try_begin),
            (eq, ":rand", 0),
            (troop_add_item, "trp_player", "itm_horse_1n_3", 0),
            (display_message, "@An horse has been gifted to you for your victory.", 0xFF0000),
        (else_try),
            (eq, ":rand", 1),
            (troop_add_item, "trp_player", "itm_barbed_arrows", 0),
            (display_message, "@A merchant gift you strange arrows, he tells you "
                              "that he brought it from Constantinople.", 0xFF0000),
        (else_try),
            (eq, ":rand", 2),
            (troop_add_item, "trp_player", "itm_wolfpelt_mail_coat", 0),
            (display_message, "@They giving you a beautiful lorica adorned with a "
                              "wolf skin. Armor fit for a Warlord.", 0xFF0000),
        (else_try),
            (eq, ":rand", 3),
            (troop_add_item, "trp_player", "itm_pict_princep_swordt3res", 0),
            (display_message, "@They gift you with a sword fit for a prince.", 0xFF0000),
        (else_try),
            (le, ":rand", 7),
            (display_message, "@They will appreciate your participation in the "
                              "tournament, and they apologize for not having a "
                              "great gift to offer.", 0xFF0000),
        (try_end),

        (call_script, "script_change_player_relation_with_center", "$current_town", 6),
        (assign, reg9, 200),
        (add_xp_to_troop, 300, "trp_player"),
        (troop_add_gold, "trp_player", reg9),
        (str_clear, s8),

        (store_add, ":total_win", "$g_tournament_bet_placed", "$g_tournament_bet_win_amount"),
        (try_begin),
            (gt, "$g_tournament_bet_win_amount", 0),
            (assign, reg8, ":total_win"),
            (str_store_string, s8, "@Moreover, you earn {reg8} scillingas from the clever bets you placed on yourself..."),
        (try_end),

        (try_begin),
            (this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
            (neg|troop_slot_ge, "trp_player", "slot_troop_renown", 70),
            (neg|troop_slot_ge, "trp_player", "slot_troop_renown", 145),

            (faction_slot_eq, "$g_encountered_party_faction", "slot_faction_ai_state", sfai_feast),
            (faction_slot_eq, "$g_encountered_party_faction", "slot_faction_ai_object", "$g_encountered_party"),
            (str_store_string, s8, "str_s8_you_are_also_invited_to_attend_the_ongoing_feast_in_the_castle"),
        (try_end),

        (troop_add_gold, "trp_player", ":total_win"),
        (assign, ":player_odds_sub", 0),
        (store_div, ":player_odds_sub", "$g_tournament_bet_win_amount", 5),
        (party_get_slot, ":player_odds", "$current_town", "slot_town_player_odds"),
        (val_sub, ":player_odds", ":player_odds_sub"),
        (val_max, ":player_odds", 250),
        (party_set_slot, "$current_town", "slot_town_player_odds", ":player_odds"),
        (call_script, "script_play_victorious_sound"),

        (unlock_achievement, ACHIEVEMENT_MEDIEVAL_TIMES),
    ],
    [
        ("continue", [], "Continue...", [(jump_to_menu, "mnu_town")]),
    ]
  ),

  (
    "town_tournament_won_by_another",mnf_disable_all_keys,
    "As the only {reg3?fighter:man} to remain undefeated this day, {s1} wins the "
    "lists and the glory of this tournament.",
    "none",
    [
      (call_script, "script_get_num_tournament_participants"),
      (store_sub, ":needed_to_remove_randomly", reg0, 1),
      (try_begin),
        (troop_slot_eq, "trp_tournament_participants", 0, 0), #delete player from the participants
        (troop_set_slot, "trp_tournament_participants", 0, -1),
        (val_sub, ":needed_to_remove_randomly", 1),
      (try_end),
        (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
        (call_script, "script_sort_tournament_participant_troops"),
        (troop_get_slot, ":winner_troop", "trp_tournament_participants", 0),
        (str_store_troop_name, s1, ":winner_troop"),
        (try_begin),
          (troop_is_hero, ":winner_troop"),
          (call_script, "script_change_troop_renown", ":winner_troop", 20),
        (try_end),
 ## Gender fix chief para alturas
        (troop_get_type, reg3, ":winner_troop"),
    (val_mod, reg3, 2),
#gender fix chief acaba
      ## CC
        (try_begin),
          (set_fixed_point_multiplier, 100),
          (position_set_x, pos0, 70),
          (position_set_y, pos0, 30),
          (position_set_z, pos0, 75),
          (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", ":winner_troop", pos0),
        (try_end),
      ## CC
        ],
    [
      ("continue", [], "Continue...",
       [(jump_to_menu, "mnu_town"),
        ]),
    ]
  ),

  (
    "town_tournament",mnf_disable_all_keys,
    "{s1}You are at tier {reg0} of the tournament, with {reg1} participants remaining. In the next round, there will be {reg2} teams with {reg3} {reg4?fighters:fighter} each.",
    "none",
    [
        (party_set_slot, "$current_town", "slot_town_has_tournament", 0), #No way to return back if this menu is left
        (call_script, "script_sort_tournament_participant_troops"),#Moving trp_player to the top of the list
        (call_script, "script_get_num_tournament_participants"),
        (assign, ":num_participants", reg0),
        (try_begin),
          (neg|troop_slot_eq, "trp_tournament_participants", 0, 0),#Player is defeated

          (assign, ":player_odds_add", 0),
          (store_div, ":player_odds_add", "$g_tournament_bet_placed", 5),
          (party_get_slot, ":player_odds", "$current_town", "slot_town_player_odds"),
          (val_add, ":player_odds", ":player_odds_add"),
          (val_min, ":player_odds", 4000),
          (party_set_slot, "$current_town", "slot_town_player_odds", ":player_odds"),

          (jump_to_menu, "mnu_town_tournament_lost"),
        (else_try),
          (eq, ":num_participants", 1),#Tournament won
          (jump_to_menu, "mnu_town_tournament_won"),
        (else_try),
          (try_begin),
            (le, "$g_tournament_next_num_teams", 0),
            (call_script, "script_get_random_tournament_team_amount_and_size"),
            (assign, "$g_tournament_next_num_teams", reg0),
            (assign, "$g_tournament_next_team_size", reg1),
          (try_end),
          (assign, reg2, "$g_tournament_next_num_teams"),
          (assign, reg3, "$g_tournament_next_team_size"),
          (store_sub, reg4, reg3, 1),
          (str_clear, s1),
          (try_begin),
            (eq, "$g_tournament_player_team_won", 1),
            (str_store_string, s1, "@Victory is yours! You have won this melee, but now you must prepare yourself for the next round. "),
          (else_try),
            (eq, "$g_tournament_player_team_won", 0),
            (str_store_string, s1, "@You have been bested in this melee, but the master of ceremonies declares a recognition of your skill and bravery, allowing you to take part in the next round. "),
          (try_end),
          (assign, reg1, ":num_participants"),
          (store_add, reg0, "$g_tournament_cur_tier", 1),
        (try_end),
        ],
    [
      ("tournament_view_participants", [], "View participants.",
       [(jump_to_menu, "mnu_tournament_participants"),
        ]),
      ("tournament_bet", [(neq, "$g_tournament_cur_tier", "$g_tournament_last_bet_tier")], "Place a bet on yourself.",
       [(jump_to_menu, "mnu_tournament_bet"),
        ]),
      ("tournament_join_next_fight", [], "Fight in the next round.",
       [
           (party_get_slot, ":arena_scene", "$current_town", "slot_town_arena"),
           (modify_visitors_at_site, ":arena_scene"),
           (reset_visitors),
           #Assuming that there are enough participants for the teams
           (assign, "$g_player_tournament_placement", "$g_tournament_cur_tier"),
           (try_begin),
             (gt, "$g_player_tournament_placement", 4),
             (assign, "$g_player_eligible_feast_center_no", "$current_town"),
           (try_end),
           (val_add, "$g_tournament_cur_tier", 1),

           (store_mul, "$g_tournament_num_participants_for_fight", "$g_tournament_next_num_teams", "$g_tournament_next_team_size"),
           (troop_set_slot, "trp_tournament_participants", 0, -1),#Removing trp_player from the list
           (troop_set_slot, "trp_temp_array_a", 0, "trp_player"),
           (try_for_range, ":slot_no", 1, "$g_tournament_num_participants_for_fight"),
             (call_script, "script_get_random_tournament_participant"),
             (troop_set_slot, "trp_temp_array_a", ":slot_no", reg0),
           (try_end),
           (call_script, "script_shuffle_troop_slots", "trp_temp_array_a", 0, "$g_tournament_num_participants_for_fight"),


           (try_for_range, ":slot_no", 0, 4),#shuffle teams
             (troop_set_slot, "trp_temp_array_b", ":slot_no", ":slot_no"),
           (try_end),
           (call_script, "script_shuffle_troop_slots", "trp_temp_array_b", 0, 4),

           (assign, ":cur_slot", 0),
           (try_for_range, ":cur_team_offset", 0, "$g_tournament_next_num_teams"),
             (troop_get_slot, ":cur_team", "trp_temp_array_b", ":cur_team_offset"),

             (try_for_range, ":slot_no", 0, 8),#shuffle entry_points
               (troop_set_slot, "trp_temp_array_c", ":slot_no", ":slot_no"),
             (try_end),
             (call_script, "script_shuffle_troop_slots", "trp_temp_array_c", 0, 8),

             (try_for_range, ":cur_index", 0, "$g_tournament_next_team_size"),
               (store_mul, ":cur_entry_point", ":cur_team", 8),
               (troop_get_slot, ":entry_offset", "trp_temp_array_c", ":cur_index"),
               (val_add, ":cur_entry_point", ":entry_offset"),
               (troop_get_slot, ":troop_no", "trp_temp_array_a", ":cur_slot"),
               (set_visitor, ":cur_entry_point", ":troop_no"),
               (val_add, ":cur_slot", 1),
             (try_end),
           (try_end),

           (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),

           (assign, "$g_mt_mode", abm_tournament),

           (party_get_slot, ":town_original_faction", "$current_town", "slot_center_original_faction"),
           (assign, ":town_index_within_faction", 0),
           (assign, ":end_cond", towns_end),
           (try_for_range, ":cur_town", towns_begin, ":end_cond"),
             (try_begin),
               (eq, ":cur_town", "$current_town"),
               (assign, ":end_cond", 0), #break
             (else_try),
               (party_slot_eq, ":cur_town", "slot_center_original_faction", ":town_original_faction"),
               (val_add, ":town_index_within_faction", 1),
             (try_end),
           (try_end),

           (set_jump_mission, "mt_arena_melee_fight"),

           (try_begin),
             (eq, ":town_original_faction", "fac_kingdom_1"),
             #Swadia
             (store_mod, ":mod", ":town_index_within_faction", 4),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 0, 0, 0, 0, "itm_arena_armor_red", "itm_arena_helm_red"),
             (else_try),
               (eq, ":mod", 1),
               (call_script, "script_set_items_for_tournament", 100, 100, 0, 0, 0, 0, 0, 0, "itm_arena_armor_red", "itm_arena_helm_red"),
             (else_try),
               (eq, ":mod", 2),
               (call_script, "script_set_items_for_tournament", 100, 0, 100, 0, 0, 0, 0, 0, "itm_arena_armor_red", "itm_arena_helm_red"),
             (else_try),
               (eq, ":mod", 3),
               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 40, 0, 0, 0, "itm_arena_armor_red", "itm_arena_helm_red"),
             (try_end),
           (else_try),
             (eq, ":town_original_faction", "fac_kingdom_2"),
             #Vaegirs
             (store_mod, ":mod", ":town_index_within_faction", 4),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 0, 0, 0, 0, "itm_arena_armor_red", "itm_skullcapt1"),
             (else_try),
               (eq, ":mod", 1),
               (call_script, "script_set_items_for_tournament", 100, 50, 0, 0, 0, 20, 30, 0, "itm_arena_armor_red", "itm_skullcapt1"),
             (else_try),
               (eq, ":mod", 2),
               (call_script, "script_set_items_for_tournament", 100, 0, 50, 0, 0, 20, 30, 0, "itm_arena_armor_red", "itm_skullcapt1"),
             (else_try),
               (eq, ":mod", 3),
               (call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 30, 0, 60, 0, "itm_arena_armor_red", "itm_skullcapt1"),
             (try_end),
           (else_try),
             (eq, ":town_original_faction", "fac_kingdom_3"),
             #Khergit
             (store_mod, ":mod", ":town_index_within_faction", 2),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 100, 0, 0, 0, 0, 40, 60, 0, "itm_arena_tunic_red", "itm_skullcapt1"),
             (else_try),
               (eq, ":mod", 1),
               (call_script, "script_set_items_for_tournament", 100, 50, 25, 0, 0, 30, 50, 0, "itm_arena_tunic_red", "itm_skullcapt1"),
             (try_end),
           (else_try),
             (eq, ":town_original_faction", "fac_kingdom_4"),
             #Nords
             (store_mod, ":mod", ":town_index_within_faction", 3),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 0, 0, 50, 80, 0, 0, 0, 0, "itm_arena_armor_red", -1),
             (else_try),
               (eq, ":mod", 1),
               (call_script, "script_set_items_for_tournament", 0, 0, 50, 80, 50, 0, 0, 0, "itm_arena_armor_red", -1),
             (else_try),
               (eq, ":mod", 2),
               (call_script, "script_set_items_for_tournament", 40, 0, 0, 100, 0, 0, 0, 0, "itm_arena_armor_red", -1),
             (try_end),
           (else_try),
             #Rhodoks
             (eq, ":town_original_faction", "fac_kingdom_5"),
             (call_script, "script_set_items_for_tournament", 25, 100, 60, 0, 30, 0, 30, 50, "itm_arena_tunic_red", "itm_skullcapt1"),
           (else_try),
             #Sarranids
             (store_mod, ":mod", ":town_index_within_faction", 2),
             (try_begin),
               (eq, ":mod", 0),
               (call_script, "script_set_items_for_tournament", 100, 40, 60, 0, 30, 30, 0, 0, "itm_arena_tunic_red", "itm_arena_skullcap_red"),
             (else_try),
               (call_script, "script_set_items_for_tournament", 50, 0, 60, 0, 30, 30, 0, 0, "itm_arena_tunic_red", "itm_arena_skullcap_red"),
             (try_end),
           (try_end),
           (jump_to_scene, ":arena_scene"),
           (change_screen_mission),
        ]),

      ("tournament_options", [], "Tournament Options", #chief anade options
       [(jump_to_menu, "mnu_tournament_options"),
        ]),
      ("leave_tournament",[],"Withdraw from the tournament.",
       [
           (jump_to_menu, "mnu_tournament_withdraw_verify"),
        ]),
    ]
  ),

  (
    "tournament_withdraw_verify", 0,
    "Are you sure you want to withdraw from the tournament?",
    "none",
    [],
    [
      ("tournament_withdraw_yes", [], "Yes. This is a pointless affectation.",
       [(jump_to_menu, "mnu_town_tournament_won_by_another"),
        ]),
      ("tournament_withdraw_no", [], "No, not as long as there is a chance of victory!",
       [(jump_to_menu, "mnu_town_tournament"),
        ]),
    ]
  ),

  (
    "tournament_bet",0,
    "The odds against you are {reg5} to {reg6}.{reg1? You have already bet {reg1} "
    "scillingas on yourself, and if you win, you will earn {reg2} scillingas.:} "
    "How much do you want to bet?",
    "none",
    [
      (assign, reg1, "$g_tournament_bet_placed"),
      (store_add, reg2, "$g_tournament_bet_win_amount", "$g_tournament_bet_placed"),
      (call_script, "script_get_win_amount_for_tournament_bet"),
      (assign, ":player_odds", reg0),
      (assign, ":min_dif", 100000),
      (assign, ":min_dif_divisor", 1),
      (assign, ":min_dif_multiplier", 1),
      (try_for_range, ":cur_multiplier", 1, 50),
        (try_for_range, ":cur_divisor", 1, 50),
          (store_mul, ":result", 100, ":cur_multiplier"),
          (val_div, ":result", ":cur_divisor"),
          (store_sub, ":difference", ":player_odds", ":result"),
          (val_abs, ":difference"),
          (lt, ":difference", ":min_dif"),
          (assign, ":min_dif", ":difference"),
          (assign, ":min_dif_divisor", ":cur_divisor"),
          (assign, ":min_dif_multiplier", ":cur_multiplier"),
        (try_end),
      (try_end),
      (assign, reg5, ":min_dif_multiplier"),
      (assign, reg6, ":min_dif_divisor"),
      ],
    [
      ("bet_100_denars", [(store_troop_gold, ":gold", "trp_player"),
                          (ge, ":gold", 500), (eq, "$g_avdificultad", 1),
                          ],
       "500 scillingas.",
       [
         (assign, "$temp", 500),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_50_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 100)
                         ],
       "100 scillingas.",
       [
         (assign, "$temp", 100),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_20_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 50)
                         ],
       "50 scillingas.",
       [
         (assign, "$temp", 50),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_10_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 25)
                         ],
       "25 scillingas.",
       [
         (assign, "$temp", 25),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_5_denars", [(store_troop_gold, ":gold", "trp_player"),
                        (ge, ":gold", 10)
                        ],
       "10 scillingas.",
       [
         (assign, "$temp", 10), # Increased bet amounts end. TML. F123 - Submod -> 1.41#gdwreduced amounts in simpletrigs didn't change tml here
         (jump_to_menu, "mnu_tournament_bet_confirm"),
         ]),
      ("go_back_dot", [], "Go back.",
       [
         (jump_to_menu, "mnu_town_tournament"),
        ]),
    ]
  ),

  (
    "tournament_bet_confirm",0,
    "If you bet {reg1} scillingas, you will earn {reg2} scillingas if you win the "
    "tournament. Is that all right?",
    "none",
    [
      (call_script, "script_get_win_amount_for_tournament_bet"),
      (assign, ":win_amount", reg0),
      (val_mul, ":win_amount", "$temp"),
      (val_div, ":win_amount", 100),
      (assign, reg1, "$temp"),
      (assign, reg2, ":win_amount"),
      ],
    [
      ("tournament_bet_accept", [],
       "Go ahead.",
       [(call_script, "script_tournament_place_bet", "$temp"),
        (jump_to_menu, "mnu_town_tournament"),
       ]),
      ("tournament_bet_cancel", [],
       "Forget it.",
       [(jump_to_menu, "mnu_tournament_bet")]),
    ]
  ),

  (
    "tournament_participants", 0,
    "You ask one of the criers for the names of the tournament participants. "
    "They are:^{s11}",
    "none",
    [
        (str_clear, s11),
        (call_script, "script_sort_tournament_participant_troops"),
        (call_script, "script_get_num_tournament_participants"),
        (assign, ":num_participants", reg0),
        (try_for_range, ":cur_slot", 0, ":num_participants"),
          (troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
          (str_store_troop_name, s12, ":troop_no"),
          (str_store_string, s11, "@{!}{s11}^{s12}"),
        (try_end),
        ],
    [
      ("go_back_dot", [], "Go back.",
       [(jump_to_menu, "mnu_town_tournament")]),
    ]
  ),

  ("town_tournament_lost", 0,
   "You have been eliminated from the tournament.{s8}",
   "none",
   [
        (str_clear, s8),
        (try_begin),
            (this_or_next|neq, "$players_kingdom", "$g_encountered_party_faction"),
                (neg|troop_slot_ge, "trp_player", "slot_troop_renown", 50),
            (neg|troop_slot_ge, "trp_player", "slot_troop_renown", 125),
            (gt, "$g_player_tournament_placement", 4),
            (faction_slot_eq, "$g_encountered_party_faction", "slot_faction_ai_state", sfai_feast),
            (faction_slot_eq, "$g_encountered_party_faction", "slot_faction_ai_object", "$g_encountered_party"),
            (str_store_string, s8, "str__however_you_have_sufficiently_distinguished_yourself_to_be_invited_to_attend_the_ongoing_feast_in_the_lords_castle"),
        (try_end),
   ],
    [("continue", [], "Continue...",
      [(jump_to_menu, "mnu_town_tournament_won_by_another")])]
  ),
]
