from ..header_operations import *
from ..header_common import *
from ..header_scenes import *
from ..header_presentations import tf_right_align, tf_single_line
from ..header_dialogs import anyone, plyr, auto_proceed

from ..module_constants import *

from ..statement import StatementBlock

from . import troops as _troops


simple_triggers = [
    (24,
     [
      (try_for_range, ":town", towns_begin, towns_end),
        (party_get_slot, ":days_to_completion", ":town", "slot_center_player_enterprise_days_until_complete"),
        (ge, ":days_to_completion", 1),
        (val_sub, ":days_to_completion", 1),
        (party_set_slot, ":town", "slot_center_player_enterprise_days_until_complete", ":days_to_completion"),
      (try_end),
     ]),
]


scripts = [

  #script_get_enterprise_name
  # INPUT: arg1 = item_no
  # Output: reg0: production string
  ("get_enterprise_name",
    [
        (store_script_param_1, ":item_produced"),
        (assign, ":enterprise_name", "str_bread_site"),
        (try_begin),
            (eq, ":item_produced", "itm_bread"),
            (assign, ":enterprise_name", "str_bread_site"),
        (else_try),
            (eq, ":item_produced", "itm_ale"),
            (assign, ":enterprise_name", "str_ale_site"),
        (else_try),
            (eq, ":item_produced", "itm_mead"),
            (assign, ":enterprise_name", "str_ale_site"),
        (else_try),
            (eq, ":item_produced", "itm_oil"),
            (assign, ":enterprise_name", "str_oil_site"),
        (else_try),
            (eq, ":item_produced", "itm_wine"),
            (assign, ":enterprise_name", "str_wine_site"),
        (else_try),
            (eq, ":item_produced", "itm_leatherwork"),
            (assign, ":enterprise_name", "str_leather_site"),
        (else_try),
            (eq, ":item_produced", "itm_wool_cloth"),
            (assign, ":enterprise_name", "str_wool_cloth_site"),
        (else_try),
            (eq, ":item_produced", "itm_linen"),
            (assign, ":enterprise_name", "str_linen_site"),
        (else_try),
            (eq, ":item_produced", "itm_velvet"),
            (assign, ":enterprise_name", "str_velvet_site"),
        (else_try),
            (eq, ":item_produced", "itm_tools"),
            (assign, ":enterprise_name", "str_tool_site"),
        (try_end),
        (assign, reg0, ":enterprise_name"),
    ]),

    # inputs1 :item_type
    # inputs2 :center
    # reg0  :profit
    # reg1  :revenue
    # reg2  :input_cost
    # reg3  :labor_cost
    # reg4  :revenue_per_unit
    # reg5  :cost_per_primary_input
    # reg10 :cost_per_secondary_input
    ("process_player_enterprise",
    [
      (store_script_param, ":item_type", 1),
      (store_script_param, ":center", 2),

      (item_get_slot, ":labor_cost", ":item_type", "slot_item_overhead_per_run"),

      # product (output)
      (item_get_slot, ":base_price", ":item_type", "slot_item_base_price"),

      (store_sub, ":cur_good_price_slot", ":item_type", trade_goods_begin),
      (val_add, ":cur_good_price_slot", "slot_town_trade_good_prices_begin"),
      (party_get_slot, ":cur_price_modifier", ":center", ":cur_good_price_slot"),

      # todo: multiply two prices and divide by 1000? why?
      (store_mul, ":revenue_per_unit", ":base_price", ":cur_price_modifier"),
      (val_div, ":revenue_per_unit", 1000),

      (item_get_slot, ":output_units", ":item_type", "slot_item_output_per_run"),
      (store_mul, ":revenue", ":output_units", ":revenue_per_unit"),

      # raw materials (input)
      (item_get_slot, ":primary_raw_material", ":item_type", "slot_item_primary_raw_material"),
      (item_get_slot, ":base_price", ":primary_raw_material", "slot_item_base_price"),
      (store_sub, ":cur_good_price_slot", ":primary_raw_material", trade_goods_begin),
      (val_add, ":cur_good_price_slot", "slot_town_trade_good_prices_begin"),
      (party_get_slot, ":cur_price_modifier", ":center", ":cur_good_price_slot"),
      (store_mul, ":cost_per_primary_input", ":base_price", ":cur_price_modifier"),
      (val_div, ":cost_per_primary_input", 1150),
      (item_get_slot, ":input_units", ":item_type", "slot_item_input_number"),

      (try_begin),
        (lt, ":input_units", 0),
        (store_div, ":input_cost", ":cost_per_primary_input", 2),
      (else_try),
        (store_mul, ":input_cost", ":cost_per_primary_input", ":input_units"),
      (try_end),

      (try_begin),
        (item_slot_ge, ":item_type", "slot_item_secondary_raw_material", 1),

        (item_get_slot, ":secondary_raw_material", ":item_type", "slot_item_secondary_raw_material"),
        (item_get_slot, ":base_price", ":secondary_raw_material", "slot_item_base_price"),
        (store_sub, ":cur_good_price_slot", ":secondary_raw_material", trade_goods_begin),
        (val_add, ":cur_good_price_slot", "slot_town_trade_good_prices_begin"),
        (party_get_slot, ":cur_price_modifier", ":center", ":cur_good_price_slot"),
        (store_mul, ":cost_per_secondary_input", ":base_price", ":cur_price_modifier"),
        (try_begin),
          (lt, ":input_units", 0),
          (store_div, ":cost_per_secondary_input", ":cost_per_secondary_input", 2),
        (else_try),
          (store_mul, ":cost_per_secondary_input", ":cost_per_secondary_input", ":input_units"),
        (try_end),

        (val_div, ":cost_per_secondary_input", 1300),
      (else_try),
        (assign, ":cost_per_secondary_input", 0),
      (try_end),

      (store_sub, ":profit", ":revenue", ":input_cost"),
      (val_sub, ":profit", ":labor_cost"),
      (val_sub, ":profit", ":cost_per_secondary_input"),

      (assign, reg0, ":profit"),
      (assign, reg1, ":revenue"),
      (assign, reg2, ":input_cost"),
      (assign, reg3, ":labor_cost"),
      (assign, reg4, ":revenue_per_unit"),
      (assign, reg5, ":cost_per_primary_input"),
      (assign, reg10, ":cost_per_secondary_input"),
    ]),
]


town_menu_options = [
    ("town_enterprise",
      [
        (party_slot_eq, "$current_town", "slot_party_type", spt_town),
        (party_get_slot, ":item_produced", "$current_town", "slot_center_player_enterprise"),
        (gt, ":item_produced", 1),
        (eq, "$entry_to_town_forbidden", 0),

        (call_script, "script_get_enterprise_name", ":item_produced"),
        (str_store_string, s3, reg0),
        (neq, "$freelancer_state", 1),
      ],
      "Visit your {s3}.",
      [
        (store_sub, ":town_order", "$current_town", towns_begin),
        (store_add, ":master_craftsman", "trp_town_1_master_craftsman", ":town_order"),
        (party_get_slot, ":item_produced", "$current_town", "slot_center_player_enterprise"),

        (assign, ":enterprise_scene", "scn_enterprise_mill"),
        (try_begin),
            (eq, ":item_produced", "itm_bread"),
            (assign, ":enterprise_scene", "scn_enterprise_mill"),
        (else_try),
            (eq, ":item_produced", "itm_ale"),
            (assign, ":enterprise_scene", "scn_enterprise_brewery"),
        (else_try),
            (eq, ":item_produced", "itm_oil"),
            (assign, ":enterprise_scene", "scn_enterprise_oil_press"),
        (else_try),
            (eq, ":item_produced", "itm_wine"),
            (assign, ":enterprise_scene", "scn_enterprise_winery"),
        (else_try),
            (eq, ":item_produced", "itm_leatherwork"),
            (assign, ":enterprise_scene", "scn_enterprise_tannery"),
        (else_try),
            (eq, ":item_produced", "itm_wool_cloth"),
            (assign, ":enterprise_scene", "scn_enterprise_wool_weavery"),
        (else_try),
            (eq, ":item_produced", "itm_linen"),
            (assign, ":enterprise_scene", "scn_enterprise_linen_weavery"),
        (else_try),
            (eq, ":item_produced", "itm_velvet"),
            (assign, ":enterprise_scene", "scn_enterprise_dyeworks"),
        (else_try),
            (eq, ":item_produced", "itm_tools"),
            (assign, ":enterprise_scene", "scn_enterprise_smithy"),
        (try_end),
        (modify_visitors_at_site, ":enterprise_scene"),
        (reset_visitors),
        (set_visitor, 0, "trp_player"),
        (set_visitor, 17, ":master_craftsman"),
        (set_jump_mission, "mt_town_default"),
        (jump_to_scene, ":enterprise_scene"),
        (change_screen_mission),
      ], "Door to your enterprise."),
]

presentations = [

]


scenes = [
("enterprise_tannery",sf_generate,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0x000000012004480500040902000041cb00005ae800000ff5",
    [],[]),
  ("enterprise_winery",sf_indoors,"winery_interior", "bo_winery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_mill",sf_indoors,"mill_interior", "bo_mill_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_smithy",sf_indoors,"smithy_interior", "bo_smithy_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_dyeworks",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_linen_weavery",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_wool_weavery",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_brewery",sf_indoors,"brewery_interior", "bo_brewery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_oil_press",sf_indoors,"oil_press_interior", "bo_oil_press_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
]


# Adds enterprise information to the budget report
budget_report_statement_block = StatementBlock(

    # creates space for printing enterprise information
    (try_for_range, ":center_no", centers_begin, centers_end),
        (try_begin),
          (party_get_slot, ":product_type", ":center_no", "slot_center_player_enterprise"),
          (gt, ":product_type", 1),
          (neg|party_slot_ge, ":center_no", "slot_center_player_enterprise_days_until_complete", 1),
          (store_add, ":cur_y", 27),
        (try_end),
    (try_end),

    # computes and prints information
    (try_for_range, ":center_no", centers_begin, centers_end),
        (try_begin),
          (party_get_slot, ":product_type", ":center_no", "slot_center_player_enterprise"),
          (gt, ":product_type", 1),
          (neg|party_slot_ge, ":center_no", "slot_center_player_enterprise_days_until_complete", 1),

          (call_script, "script_process_player_enterprise", ":product_type", ":center_no"),
          (assign, ":net_profit", reg0),
          (assign, ":price_of_single_output", reg4),
          (assign, ":price_of_single_input", reg5),
          (assign, ":price_of_secondary_input", reg10),

          (store_sub, ":town_order", ":center_no", towns_begin),
          (store_add, ":craftsman_troop", ":town_order", "trp_town_1_master_craftsman"),

          # Compute goods produced and stored:
          # - qnt_sold: products to be sold
          # - qnt_stored: products to be stored in the warehouse
          (item_get_slot, ":qnt_sold", ":product_type", "slot_item_output_per_run"),
          (assign, ":qnt_stored", 0),

          (try_begin),
            (party_slot_eq, ":center_no", "slot_center_player_enterprise_production_order", 1),
            # orders are to store production; fulfill them by storing the maximum
            # possible.

            # compute empty space in warehouse
            (assign, ":empty_slots", 0),
            (troop_get_inventory_capacity, ":total_capacity", ":craftsman_troop"),
            (try_for_range, ":capacity_iterator", 0, ":total_capacity"),
                (troop_get_inventory_slot, ":slot", ":craftsman_troop", ":capacity_iterator"),
                (lt, ":slot", 1),
                (val_add, ":empty_slots", 1),
            (try_end),

            # try to store everything
            (assign, ":qnt_stored", ":qnt_sold"),

            # limited by the available space
            (val_min, ":qnt_stored", ":empty_slots"),

            # and sell the rest.
            (val_sub, ":qnt_sold", ":qnt_stored"),
          (try_end),

          # Compute goods bought and used
          # - qnt_bought: input bought from market
          # - qnt_used: input used from storage
          (item_get_slot, ":qnt_bought", ":product_type", "slot_item_input_number"),
          (assign, ":qnt_used", 0),

          (try_begin),
            (item_slot_ge, ":product_type", "slot_item_secondary_raw_material", 1),
            (assign, ":2ary_qnt_bought", ":qnt_bought"),
          (else_try),
            (assign, ":2ary_qnt_bought", 0),
          (try_end),
          (assign, ":2ary_qnt_used", 0),

          # compute `qut_used` and `2ary_qnt_used`
          (troop_get_inventory_capacity, ":total_capacity", ":craftsman_troop"),
          (try_for_range, ":capacity_iterator", 0, ":total_capacity"),
              (troop_get_inventory_slot, ":item_in_slot", ":craftsman_troop", ":capacity_iterator"),

              (lt, ":qnt_used", ":qnt_bought"),
              (item_slot_eq, ":product_type", "slot_item_primary_raw_material", ":item_in_slot"),
              (val_add, ":qnt_used", 1),
          (else_try),
              (lt, ":2ary_qnt_used", ":2ary_qnt_bought"),
              (item_slot_eq, ":product_type", "slot_item_secondary_raw_material", ":item_in_slot"),
              (val_add, ":2ary_qnt_used", 1),
          (try_end),

          (val_sub, ":qnt_bought", ":qnt_used"),
          (val_sub, ":2ary_qnt_bought", ":2ary_qnt_used"),

          # update net profit from the goods
          (store_mul, ":cancelled_sales", ":price_of_single_output", ":qnt_stored"),
          (val_sub, ":net_profit", ":cancelled_sales"),

          (store_mul, ":savings_from_warehoused_inputs", ":price_of_single_input", ":qnt_used"),
          (val_add, ":net_profit", ":savings_from_warehoused_inputs"),

          (assign, ":savings_from_warehoused_inputs", ":price_of_secondary_input"),
          (val_add, ":net_profit", ":savings_from_warehoused_inputs"),

          # if the town belongs to faction at war, production is halted.
          (assign, ":production_halted", 0),
          (try_begin),
            (store_faction_of_party, ":faction_no", ":center_no"),
            (store_relation, ":relation", ":faction_no", "$players_kingdom"),
            (lt, ":relation", 0),

            (assign, ":production_halted", 1),

            (assign, ":qnt_sold", 0),
            (assign, ":qnt_stored", 0),
            (assign, ":qnt_used", 0),
            (assign, ":qnt_bought", 0),
            (assign, ":2ary_qnt_used", 0),
            (assign, ":2ary_qnt_bought", 0),
            (assign, ":net_profit", 0),
          (try_end),

          # if the transaction is for real and not just a budget check
          (try_begin),
            (eq, "$g_apply_budget_report_to_gold", 1),
            (eq, ":production_halted", 0),

            # add products to warehouse
            (troop_add_items, ":craftsman_troop", ":product_type", ":qnt_stored"),

            # remove raw materials from warehouse
            (try_begin),
                (gt, ":qnt_used", 0),
                    (item_get_slot, ":raw_material", ":product_type", "slot_item_primary_raw_material"),
                    (troop_remove_items, ":craftsman_troop", ":raw_material", ":qnt_used"),
            (try_end),
            (try_begin),
                (gt, ":2ary_qnt_used", 0),
                    (item_get_slot, ":2ary_raw_material", ":product_type", "slot_item_secondary_raw_material"),
                    (troop_remove_items, ":craftsman_troop", ":2ary_raw_material", ":2ary_qnt_used"),
            (try_end),

            # (virtually) sell products to market
            (store_sub, ":item_slot_no", ":product_type", trade_goods_begin),
            (val_add, ":item_slot_no", "slot_town_trade_good_prices_begin"),
            (party_get_slot, ":multiplier", ":center_no", ":item_slot_no"),

            # todo: this can lead to a negative multiplier, which is forbidden.
            # Use same idiom as buy/sell operations.
            (store_mul, ":impact_on_price", ":qnt_sold", 15),
            (val_sub, ":multiplier", ":impact_on_price"),
            (party_set_slot, ":center_no", ":item_slot_no", ":multiplier"),

            # (virtually) buy goods from market
            (try_begin),
                (gt, ":qnt_bought", 0),

                (item_get_slot, ":raw_material", ":product_type", "slot_item_primary_raw_material"),
                (store_sub, ":item_slot_no", ":raw_material", trade_goods_begin),
                (val_add, ":item_slot_no", "slot_town_trade_good_prices_begin"),
                (party_get_slot, ":multiplier", ":center_no", ":item_slot_no"),

                # todo: this can lead to a negative multiplier, which is forbidden.
                # Use same idiom as buy/sell operations.
                (store_mul, ":impact_on_price", ":qnt_bought", 15),
                (val_add, ":multiplier", ":impact_on_price"),
                (party_set_slot, ":center_no", ":item_slot_no",":multiplier"),
            (try_end),

            (try_begin),
                (gt, ":2ary_qnt_bought", 0),

                (item_get_slot, ":2ary_raw_material", ":product_type", "slot_item_secondary_raw_material"),
                (store_sub, ":item_slot_no", ":2ary_raw_material", trade_goods_begin),
                (val_add, ":item_slot_no", "slot_town_trade_good_prices_begin"),
                (party_get_slot, ":multiplier", ":center_no", ":item_slot_no"),

                # todo: this can lead to a negative multiplier, which is forbidden.
                # Use same idiom as buy/sell operations.
                (store_mul, ":impact_on_price", ":2ary_qnt_bought", 15),
                (val_add, ":multiplier", ":impact_on_price"),
                (party_set_slot, ":center_no", ":item_slot_no", ":multiplier"),
            (try_end),
          (try_end),  # end real transaction

          # update grand totals for where the script was called.
          (val_add, ":all_centers_accumulated_total", ":net_profit"),
          (val_add, ":net_change", ":net_profit"),

          # print summary on the presentation
          (call_script, "script_get_enterprise_name", ":product_type"),
          (str_store_string, s3, reg0),
          (str_store_party_name, s0, ":center_no"),

          (create_text_overlay, reg1, "@Profits from producing {s3} at {s0}", 0),
          (position_set_x, pos1, 900),
          (position_set_y, pos1, 900),
          (overlay_set_size, reg1, pos1),
          (position_set_x, pos1, 25),
          (position_set_y, pos1, ":cur_y"),
          (overlay_set_position, reg1, pos1),

          (assign, reg0, ":net_profit"),
          (try_begin),
            (eq, ":production_halted", 1),

            (create_text_overlay, reg1, "@At war, production halted.", tf_right_align|tf_single_line),
            (overlay_set_color, reg1, 0xFF0000),
          (else_try),
            (create_text_overlay, reg1, "@{!}{reg0}", tf_right_align|tf_single_line),
            (overlay_set_color, reg1, 0xFF0000),  # red
            (ge, reg0, 0),
            (overlay_set_color, reg1, 0x00AA00),  # todo: this color is invalid.
          (try_end),
          (position_set_x, pos1, 900),
          (position_set_y, pos1, 900),
          (overlay_set_size, reg1, pos1),
          (position_set_x, pos1, 500),
          (position_set_y, pos1, ":cur_y"),
          (overlay_set_position, reg1, pos1),

          # decrease y for the next item.
          (val_sub, ":cur_y", 27),
        (try_end),
    (try_end)
)


dialogs = [

    [anyone|plyr, "mayor_talk", [
        (ge, "$cheat_mode", 0),
        (item_slot_ge, "itm_velvet", "slot_item_secondary_raw_material", "itm_raw_dyes"), #ie, the item information has been updated, to ensure savegame compatibility
    ], "I wish to buy land in this town for a productive enterprise", "mayor_investment_possible",[
     ]],

    [anyone, "mayor_investment_possible", [
        (party_slot_ge, "$g_encountered_party", "slot_center_player_enterprise", 1),
        (party_get_slot, ":item_produced", "$g_encountered_party", "slot_center_player_enterprise"),
        (call_script, "script_get_enterprise_name", ":item_produced"),
        (str_store_string, s4, reg0),
    ], "You already operate a {s4} here. There probably aren't enough skilled tradesmen to start a second enterprise.", "mayor_pretalk",[
     ]],

    [anyone, "mayor_investment_possible", [
        (ge, "$cheat_mode", 3)
    ], "{!}CHEAT: Yes, we're playtesting this feature, and you're in cheat mode. Go right ahead.",
     "mayor_investment_advice",[]
    ],

    [anyone,"mayor_investment_possible", [
        (lt,"$g_encountered_party_relation", 0),
    ], "{Sir/Madame}, you are an enemy of this realm. We cannot allow you to buy land here.", "mayor_pretalk", []
    ],

    [anyone,"mayor_investment_possible", [
        (party_slot_eq, "$g_encountered_party", "slot_town_lord", "trp_player"),
    ], "Of course, {sir/my lady}. You are the lord of this town, and no one is going to stop you.", "mayor_investment_advice",[
     ]],

    [anyone,"mayor_investment_possible", [
        (party_get_slot, ":town_liege", "$g_encountered_party", "slot_town_lord"),
        (is_between, ":town_liege", active_npcs_begin, active_npcs_end),
        (call_script, "script_troop_get_relation_with_troop", "trp_player", ":town_liege"),
        (assign, ":relation", reg0),
        (lt, ":relation", 0),
        (str_store_troop_name, s4, ":town_liege"),
    ], "Well... Given your relationship with our liege, {s4}, I think that you will not find many here who are brave enough to sell you any land.", "mayor_investment",[
     ]],

    [anyone|auto_proceed,"mayor_investment",[], "{!}.", "mayor_pretalk",[]],


    [anyone,"mayor_investment_possible", [
        (assign, ":required_relation", 0), # need 0+ normally
        (try_begin),
          (neq, "$g_encountered_party", "$g_starting_town"),
          (val_add, ":required_relation", 1),
        (try_end),
        (neg|party_slot_ge, "$current_town", "slot_center_player_relation", ":required_relation"),
    ], "Well... To be honest, I think that we in the guild would like to know you a little better. "
       "We can be very particular about outsiders coming in here and buying land.", "mayor_pretalk", []
     ],

    [anyone, "mayor_investment_possible", [],
     "Very good, {sir/my lady}. We in the guild know and trust you, and I think I "
     "could find someone to sell you the land you need.",
     "mayor_investment_advice", []
     ],

    [anyone, "mayor_investment_advice",[],
     "A couple of things to keep in mind -- skilled laborers are always at a "
     "premium, so I doubt that you will be able to open up more than one enterprise "
     "here. In order to make a profit for yourself, you should choose a commodity "
     "which is in relatively short supply, but for which the raw materials are "
     "cheap. What sort of enterprise would you like to start?", "investment_choose_enterprise", []
     ],

    [anyone|plyr, "investment_choose_enterprise", [],
     "A mill and bakery, to make bread from grain", "investment_summary",
     [(assign, "$enterprise_production", "itm_bread")]
     ],

    [anyone|plyr, "investment_choose_enterprise", [],
     "A brewery, to make ale from grain", "investment_summary",
     [(assign, "$enterprise_production", "itm_ale")]
     ],

    [anyone|plyr, "investment_choose_enterprise", [],
     "A tannery, to make leather from hides", "investment_summary",
     [(assign, "$enterprise_production", "itm_leatherwork")]
     ],

    [anyone|plyr, "investment_choose_enterprise", [],
     "A wine press, to make wine from grapes", "investment_summary",
     [(assign, "$enterprise_production", "itm_wine")]
     ],

    [anyone|plyr, "investment_choose_enterprise", [],
     "An oil press, to make oil from olives", "investment_summary",
     [(assign, "$enterprise_production", "itm_oil")]
     ],

    [anyone|plyr, "investment_choose_enterprise", [],
     "An ironworks, to make tools from iron", "investment_summary",
     [(assign, "$enterprise_production", "itm_tools")]
    ],

    [anyone|plyr, "investment_choose_enterprise", [],
     "A weavery and dyeworks, to make fine cloth from tile and dye", "investment_summary",
     [(assign, "$enterprise_production", "itm_velvet")]
    ],

    [anyone|plyr, "investment_choose_enterprise", [],
     "A weavery, to make wool cloth from wool", "investment_summary",
     [(assign, "$enterprise_production", "itm_wool_cloth")]
    ],

    [anyone|plyr, "investment_choose_enterprise",[],
     "A weavery, to make linen from flax", "investment_summary",
     [(assign, "$enterprise_production", "itm_linen")]
    ],

    [anyone|plyr, "investment_choose_enterprise", [],
     "Never mind", "mayor_pretalk", []
     ],

  [anyone, "investment_summary", [],
   "Very good, sir. The land and the materials on which you may build your {s3} "
   "will cost you {reg7} scillingas. Right now, your {s3} will produce {s4} worth "
   "{reg1} scillingas each week, while the {s6} needed to manufacture that batch "
   "will be {reg2} and labor and upkeep will be {reg3}.{s9} I should guess that "
   "your profit would be {reg0} scillingas a week. This assumes of course that "
   "prices remain constant -- which, I can virtually guarantee you, they will not. "
   "Do you wish to proceed?", "mayor_investment_confirm", [

    (item_get_slot, "$enterprise_cost", "$enterprise_production", "slot_item_enterprise_building_cost"),

    (assign, reg7, "$enterprise_cost"),

    (str_store_item_name, s4, "$enterprise_production"),

    (call_script, "script_get_enterprise_name", "$enterprise_production"),
    (str_store_string, s3, reg0),

    (call_script, "script_process_player_enterprise", "$enterprise_production", "$g_encountered_party"),
    #reg0: Profit per cycle
    #reg1: Selling price of total goods
    #reg2: Selling price of total goods

    (item_get_slot, ":primary_raw_material", "$enterprise_production", "slot_item_primary_raw_material"),
    (str_store_item_name, s6, ":primary_raw_material"),

    (str_clear, s9),
    (assign, ":cost_of_secondary_input", reg10),
    (try_begin),
      (gt, ":cost_of_secondary_input", 0),
      (item_get_slot, ":secondary_raw_material", "$enterprise_production", "slot_item_secondary_raw_material"),
      (str_store_item_name, s11, ":secondary_raw_material"),
      (str_store_string, s9, "str_describe_secondary_input"),
    (try_end),
    ]
   ],

  [anyone|plyr, "mayor_investment_confirm", [
    (store_troop_gold, ":player_gold", "trp_player"),
    (ge, ":player_gold","$enterprise_cost"),
  ], "Yes. Here is money for the land.", "mayor_investment_purchase", [

      (party_set_slot, "$g_encountered_party", "slot_center_player_enterprise", "$enterprise_production"),
      (party_set_slot, "$g_encountered_party", "slot_center_player_enterprise_days_until_complete", 7),

      (troop_remove_gold, "trp_player", "$enterprise_cost"),
      (store_sub, ":current_town_order", "$current_town", towns_begin),
      (store_add, ":craftsman_troop", ":current_town_order", "trp_town_1_master_craftsman"),
      (try_begin),
        (eq, "$enterprise_production", "itm_bread"),
        (troop_set_name, ":craftsman_troop", "str_master_miller"),
      (else_try),
        (eq, "$enterprise_production", "itm_ale"),
        (troop_set_name, ":craftsman_troop", "str_master_brewer"),
      (else_try),
        (eq, "$enterprise_production", "itm_oil"),
        (troop_set_name, ":craftsman_troop", "str_master_presser"),
      (else_try),
        (eq, "$enterprise_production", "itm_tools"),
        (troop_set_name, ":craftsman_troop", "str_master_smith"),
      (else_try),
        (eq, "$enterprise_production", "itm_wool_cloth"),
        (troop_set_name, ":craftsman_troop", "str_master_weaver"),
      (else_try),
        (eq, "$enterprise_production", "itm_linen"),
        (troop_set_name, ":craftsman_troop", "str_master_weaver"),
      (else_try),
        (eq, "$enterprise_production", "itm_leatherwork"),
        (troop_set_name, ":craftsman_troop", "str_master_tanner"),
      (else_try),
        (eq, "$enterprise_production", "itm_velvet"),
        (troop_set_name, ":craftsman_troop", "str_master_dyer"),
      (else_try),
        (eq, "$enterprise_production", "itm_wine"),
        (troop_set_name, ":craftsman_troop", "str_master_vinter"),
      (try_end),
    ]
   ],

  [anyone|plyr, "mayor_investment_confirm", [],
   "No -- that's not economical for me at the moment.", "mayor_pretalk", []
   ],

  [anyone, "mayor_investment_purchase", [],
   "Very good. Your enterprise should be up and running in about a week. When "
   "next you come, and thereafter, you should speak to your {s4} about its "
   "operations.", "mayor_pretalk", [
      (store_sub, ":current_town_order", "$current_town", towns_begin),
      (store_add, ":craftsman_troop", ":current_town_order", "trp_town_1_master_craftsman"),
      (str_store_troop_name, s4, ":craftsman_troop"),
  ]],
]


dialogs += [

  [anyone|auto_proceed,"start", [
  (is_between,"$g_talk_troop","trp_town_1_master_craftsman", "trp_zendar_chest"),
  (party_get_slot, ":days_until_complete", "$g_encountered_party", "slot_center_player_enterprise_days_until_complete"),
  (ge, ":days_until_complete", 2),
  (assign, reg4, ":days_until_complete"),
  ],
   "{!}.", "start_craftsman_soon",[]
  ],

  [anyone,"start_craftsman_soon", [
  ],
   "Good day, my {lord/lady}. We hope to begin production in about {reg4} days", "close_window",[]],

  [anyone,"start", [
  (is_between,"$g_talk_troop","trp_town_1_master_craftsman", "trp_zendar_chest"),
  ],
   "Good day, my {lord/lady}. We are honored that you have chosen to visit us. What do you require?", "master_craftsman_talk",[]],

  [anyone,"master_craftsman_pretalk", [],
   "Very good, my {lord/lady}. Do you require anything else?", "master_craftsman_talk",[]],

  [anyone|plyr,"master_craftsman_talk", [],
   "Let's go over the accounts.", "master_craftsman_accounts",[]],

  [anyone|plyr,"master_craftsman_talk", [],
   "Let's check the inventories.", "master_craftsman_pretalk",[
   (change_screen_loot, "$g_talk_troop"),
   ]],

  [anyone|plyr,"master_craftsman_talk", [
  (party_slot_eq, "$g_encountered_party", "slot_center_player_enterprise_production_order", 1),
  ],
   "I'd like you to sell goods as they are produced.", "master_craftsman_pretalk",[
  (party_set_slot, "$g_encountered_party", "slot_center_player_enterprise_production_order", 0),
   ]],

  [anyone|plyr,"master_craftsman_talk", [
  (party_slot_eq, "$g_encountered_party", "slot_center_player_enterprise_production_order", 0),
  ],
   "I'd like you to keep all goods in the warehouse until I arrive.", "master_craftsman_pretalk",[
  (party_set_slot, "$g_encountered_party", "slot_center_player_enterprise_production_order", 1),
   ]],

  [anyone,"master_craftsman_accounts", [
  ], "We currently produce {s3} worth {reg1} scillingas each week, while the quantity of {s4} needed to manufacture it costs {reg2}, and labor and upkeep are {reg3}.{s9} This means that we theoretically make a {s12} of {reg0} scillingas a week, assuming that we have no raw materials in the inventories, and that we sell directly to the market.", "master_craftsman_pretalk",
  [
    (party_get_slot, ":item_produced", "$g_encountered_party", "slot_center_player_enterprise"),
    (call_script, "script_process_player_enterprise", ":item_produced", "$g_encountered_party"),

    (try_begin),
	  (ge, reg0, 0),
	  (str_store_string, s12, "str_profit"),
    (else_try),
	  (str_store_string, s12, "str_loss"),
    (try_end),

    (str_store_item_name, s3, ":item_produced"),
    (item_get_slot, ":primary_raw_material", ":item_produced", "slot_item_primary_raw_material"),
    (str_store_item_name, s4, ":primary_raw_material"),

    (item_get_slot, ":secondary_raw_material", ":item_produced", "slot_item_secondary_raw_material"),
    (str_clear, s9),
    (try_begin),
	  (gt, ":secondary_raw_material", 0),
	  (str_store_item_name, s11, ":secondary_raw_material"),
	  (str_store_string, s9, "str_describe_secondary_input"),
    (try_end),
  ]],

  [anyone|plyr,"master_craftsman_talk", [
  ], "Could you explain my options related to production?", "master_craftsman_production_options",[]],

  [anyone,"master_craftsman_production_options", [
  (str_store_party_name, s5, "$g_encountered_party"),
  ], "Certainly, my {lord/lady}. Most of the time, the most profitable thing for you to do would be to let us buy raw materials and sell the finished goods directly to the market. Because of our longstanding relations with the local merchants, we can usually get a very good price.", "master_craftsman_production_options_2",[]],

  [anyone,"master_craftsman_production_options_2", [
  (str_store_party_name, s5, "$g_encountered_party"),
  ], "However, if you find that you can acquire raw materials cheaper outside {s5}, you may place them in the inventories, and we will use them instead of buying from the market. Likewise, if you feel that you can get a better price for the finished goods elsewhere, then you may ask us to deposit what we produce in our warehouses for you to take.", "master_craftsman_pretalk",[]],

  [anyone|plyr,"master_craftsman_talk", [
  ], "It will no longer be possible for me to continue operating this enterprise.", "master_craftsman_auction_price",[]],

  [anyone,"master_craftsman_auction_price", [
  (party_get_slot, ":item_produced", "$g_encountered_party", "slot_center_player_enterprise"),
  (item_get_slot, ":base_price",":item_produced", "slot_item_base_price"),
  (item_get_slot, ":number_runs", ":item_produced", "slot_item_output_per_run"),
  (store_mul, "$liquidation_price", ":base_price", ":number_runs"),
  (val_mul, "$liquidation_price", 4),

  (troop_get_inventory_capacity, ":total_capacity", "$g_talk_troop"),
  (try_for_range, ":capacity_iterator", 0, ":total_capacity"),
		(troop_get_inventory_slot, ":item_in_slot", "$g_talk_troop", ":capacity_iterator"),
		(gt, ":item_in_slot", 0),
		(item_get_slot, ":price_for_inventory_item", ":item_in_slot", "slot_item_base_price"),
#		(troop_inventory_slot_get_item_amount, ":item_ammo", "$g_talk_troop", ":capacity_iterator"),
#		(troop_inventory_slot_get_item_max_amount, ":item_max_ammo", "$g_talk_troop", ":capacity_iterator"),
#		(try_begin),
#			(lt, ":item_ammo", ":item_max_ammo"),
#			(val_mul, ":price_for_inventory_item", ":item_ammo"),
#			(val_div, ":price_for_inventory_item", ":item_max_ammo"),
#		(try_end),

        (store_sub, ":item_slot_no", ":item_in_slot", trade_goods_begin),
        (val_add, ":item_slot_no", "slot_town_trade_good_prices_begin"),
        (party_get_slot, ":index", "$g_encountered_party", ":item_slot_no"),
		(val_mul, ":price_for_inventory_item", ":index"),
		(val_div, ":price_for_inventory_item", 1200),
		#modify by site
		#divide by 1200 not 1000
		(val_add, "$liquidation_price", ":price_for_inventory_item"),
  (try_end),

  (assign, reg4, "$liquidation_price"),

  ], "A pity, my {lord/lady}. If we sell the land and the equipment, and liquidate the inventories, I estimate that we can get {reg4} scillingas.", "master_craftsman_auction_decide",[]],

  [anyone|plyr,"master_craftsman_auction_decide", [
  ], "That sounds reasonable. Please proceed with the sale.", "master_craftsman_liquidation",[
  (troop_add_gold, "trp_player", "$liquidation_price"),
  (troop_clear_inventory, "$g_talk_troop"),
  (party_set_slot, "$g_encountered_party", "slot_center_player_enterprise", 0),
  (party_set_slot, "$g_encountered_party", "slot_center_player_enterprise_production_order", 0),

  ]],

  [anyone|plyr,"master_craftsman_auction_decide", [
  ], "Hmm. Let's hold off on that.", "master_craftsman_pretalk",[]],

  [anyone,"master_craftsman_liquidation", [
  ], "As you wish. It was an honor to have been in your employ.", "close_window",[
    (finish_mission),
  ]],

  [anyone|plyr,"master_craftsman_talk", [],
   "That is all for now.", "close_window",[]],
]

troops = _troops.troops
