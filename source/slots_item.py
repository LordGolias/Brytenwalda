

slots = [
    ["item_is_checked", 1],
    ["item_food_bonus", 1],
    ["item_book_reading_progress", 1],
    ["item_book_read", 1],
    ["item_intelligence_requirement", 1],

    ["item_amount_available", 1],

    ["item_urban_demand", 1],  # consumer demand for a good in town, measured in abstract units. The more essential the item (ie, like grain) the higher the price
    ["item_rural_demand", 1],  # consumer demand in villages, measured in abstract units
    ["item_desert_demand", 1],  # consumer demand in villages, measured in abstract units

    ["item_production_slot", 1],
    ["item_production_string", 1],

    # these two are used to move scene items around
    ["item_num_positions", 1],
    ["item_positions_begin", 5],  # reserve around 5 slots after this

    # number of factions < 50
    ["item_multiplayer_faction_price_multipliers_begin", 50],

    ["item_primary_raw_material", 1],
    ["item_is_raw_material_only_for", 1],
    ["item_input_number", 1],  # ie, how many items of inputs consumed per run
    ["item_base_price", 1],  # taken from .module_items
    ["item_output_per_run", 1],  # number of items produced per run
    ["item_overhead_per_run", 1],  # labor and overhead per run
    ["item_secondary_raw_material", 1],  # in this case, the amount used is only one
    ["item_enterprise_building_cost", 1],  # enterprise building cost

    ["item_multiplayer_item_class", 1],  # temporary, can be moved to higher values

    # number of multiplayer troops < 300
    ["item_multiplayer_availability_linked_list_begin", 300],

    ["item_needs_two_hands", 1],
    ["item_difficulty", 1],
    ["item_weight", 1],

    ["item_modifier_multiplier", 1],
    ["item_head_armor", 1],
    ["item_body_armor", 1],
    ["item_leg_armor", 1],
    ["item_length", 1],
    ["item_speed", 1],

    ["item_two_hand_one_hand", 1],
    ["item_alternate", 1],  # toggleable weapons gdw
    ["item_swing_damage", 1],
    ["item_thrust_damage", 1],

    ["item_horse_speed", 1],
    ["item_horse_armor", 1],
    ["item_horse_charge", 1],
]
