from source.header_operations import *

from source.module_constants import towns_begin, towns_end, slot_town_prosperity, \
    slot_center_population, slot_town_acres, slot_town_player_acres, slot_town_bank_rent, \
    slot_town_bank_assets, slot_town_bank_upkeep


simple_triggers = [
    # Adjust Population Depending on Prosperity
    (24*14,
    [
        (try_for_range, ":town_no", towns_begin, towns_end),
            (party_get_slot, ":prosperity", ":town_no", slot_town_prosperity),
            (party_get_slot, ":population", ":town_no", slot_center_population),
            (assign,":change",0),
            (try_begin),
                (ge, ":prosperity", 60),
                (store_sub, ":change", ":prosperity",60),
                (val_div, ":change", 5),
                (val_add, ":change", 3),
            (else_try),
                (le, ":prosperity", 40),
                (store_sub, ":change", ":prosperity", 40),
                (val_div, ":change", 5),
                (val_sub, ":change", 3),
            (try_end),
            (store_div,":base", ":population", 100),  # 1%
            (val_mul,":change", ":base"),
            (val_add,":population", ":change"),            
            (try_begin),
                # max pop is 10k
                (gt, ":population", 10000),
                (assign, ":population", 10000),
                (party_set_slot, ":town_no", slot_center_population, ":population"),
            (else_try),
                # min pop is 1k
                (lt, ":population", 1000),
                (assign, ":population", 1000),
                (party_set_slot, ":town_no", slot_center_population, ":population"),
            (else_try),
                (party_set_slot, ":town_no", slot_center_population, ":population"),
            (try_end),
        (try_end),    

        # Compute land demand and consequences for supply, pricing and renting
        (try_for_range, ":town_no", towns_begin, towns_end),
            (party_get_slot, ":population", ":town_no", slot_center_population),
            (party_get_slot, ":land_town", ":town_no", slot_town_acres),
            (party_get_slot, ":land_player", ":town_no", slot_town_player_acres),
            (party_get_slot, ":prosperity", ":town_no", slot_town_prosperity),
            (store_sub, ":revenue", ":prosperity", 50),
            (val_add, ":revenue", 100),
            (try_begin),
                # 200 People warrant 1 acre of cultivated land
                (store_div, ":acres_needed", ":population", 200),
                (store_add, ":total_land", ":land_town", ":land_player"),
                (store_sub, ":surplus", ":total_land", ":acres_needed"),

                # AI Consequences
                (try_begin),
                    (lt, ":total_land", ":acres_needed"),
                    (store_sub, ":new_acres", ":acres_needed", ":total_land"),
                    (val_add, ":land_town", ":new_acres"),
                    (party_set_slot, ":town_no", slot_town_acres, ":land_town"),
                (else_try),
                    (ge, ":surplus", 20),
                    (ge, ":land_town", 10),
                    (val_sub, ":land_town", 10),
                    (party_set_slot, ":town_no", slot_town_acres, ":land_town"),
                (try_end),

                # Player Consequences
                (try_begin),
                    (gt, ":land_player", 0),
                    (try_begin),
                        (le, ":total_land", ":acres_needed"),
                        (val_mul, ":land_player", ":revenue"),                                        
                        (party_set_slot, ":town_no", slot_town_bank_rent, ":land_player"),
                    (else_try),
                        (store_mul, ":penalty", ":surplus", -1),
                        (val_add, ":penalty", ":revenue"),
                        (try_begin),
                            (ge, ":penalty", 85),
                            (val_mul, ":land_player", ":penalty"),
                            (party_set_slot, ":town_no", slot_town_bank_rent, ":land_player"),
                        (else_try),
                            (store_sub, ":non_rented", ":surplus", 15),
                            (val_sub, ":land_player", ":non_rented"),
                            # Safety check : penalty on rent should turn rent negative.
                            (try_begin),
                                (lt, ":penalty", 0),
                                (assign, ":penalty", 0),
                            (try_end),
                            (val_mul, ":land_player", ":penalty"),
                            (party_set_slot, ":town_no", slot_town_bank_rent, ":land_player"),
                            (val_mul, ":non_rented", -50),
                            (party_set_slot, ":town_no", slot_town_bank_upkeep, ":non_rented"),
                        (try_end),
                    (try_end),
                    # Adding/Subtracting profits/losses
                    (party_get_slot, ":assets", ":town_no", slot_town_bank_assets),
                    (party_get_slot, ":rent", ":town_no", slot_town_bank_rent),
                    (party_get_slot, ":upkeep", ":town_no", slot_town_bank_upkeep),
                    (val_add, ":assets", ":rent"),
                    (val_add, ":assets", ":upkeep"),
                    (party_set_slot, ":town_no", slot_town_bank_assets, ":assets"),    
                (try_end),
            (try_end),
        (try_end),
    ]),
]

scripts = [
    ("initialize_acres",
    [
      (try_for_range, ":town_no", towns_begin, towns_end),
        (this_or_next|eq, ":town_no","p_town_1"),
        (this_or_next|eq, ":town_no","p_town_10"),
        (this_or_next|eq, ":town_no","p_town_13"),
        (this_or_next|eq, ":town_no","p_town_14"),
        (this_or_next|eq, ":town_no","p_town_28"),
        (this_or_next|eq, ":town_no","p_town_30"),
        (this_or_next|eq, ":town_no","p_town_33"),
        (this_or_next|eq, ":town_no","p_town_35"),
        (eq,"$current_town", "p_town_41"),
        (store_random_in_range, ":amount", 6000, 10000),
        (party_set_slot, ":town_no", slot_center_population, ":amount"),
        (val_div, ":amount", 200),
        (party_set_slot, ":town_no", slot_town_acres, ":amount"),
      (else_try),
        (store_random_in_range, ":amount", 1000, 4000),
        (party_set_slot, ":town_no", slot_center_population, ":amount"),
        (val_div, ":amount", 200),
        (party_set_slot, ":town_no", slot_town_acres, ":amount"),
      (try_end),
  ]),
]
