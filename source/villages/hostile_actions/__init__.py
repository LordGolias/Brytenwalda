from source.header_operations import *

from source.header_items import num_equipment_kinds, max_inventory_items

from source.module_constants import svs_looted, svs_being_raided

from . import force_recruit, loot, make_prisoners, steal_cattle, take_food


menus = [
    ("village_hostile_action", 0, "What action do you have in mind?", "none", [], [

        ("village_take_food", [
            (party_slot_eq, "$current_town", "slot_village_state", 0),
            (neg | party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            (party_get_slot, ":merchant_troop", "$current_town", "slot_town_elder"),
            (assign, ":town_stores_not_empty", 0),
            (try_for_range, ":slot_no", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
                (troop_get_inventory_slot, ":slot_item", ":merchant_troop", ":slot_no"),
                (ge, ":slot_item", 0),
                (assign, ":town_stores_not_empty", 1),
            (try_end),
            (eq, ":town_stores_not_empty", 1),
        ], "Force the peasants to give you supplies.", [
             (jump_to_menu, "mnu_village_take_food_confirm")
        ]),

        ("village_steal_cattle", [
            (party_slot_eq, "$current_town", "slot_village_state", 0),
            (party_slot_eq, "$current_town", "slot_village_player_can_not_steal_cattle", 0),
            (neg | party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            (neg | party_slot_eq, "$current_town", "slot_town_lord", "trp_player"),
            (party_get_slot, ":num_cattle", "$current_town", "slot_village_number_of_cattle"),
            (gt, ":num_cattle", 0),
         ], "Steal cattle.", [
            (jump_to_menu, "mnu_village_steal_cattle_confirm")
        ]),

        ("force_recruit", [
            (call_script, "script_cf_village_recruit_volunteers_condition", -33, -33),
            (neq, "$freelancer_state", 1), #+freelancer chief #prevents player freelancer brytenwalda
            ], "Force recruitment.", [
            (try_begin),
                (call_script, "script_cf_enter_center_location_bandit_check"),
            (else_try),
                (jump_to_menu, "mnu_force_recruit"),
            (try_end),
        ]),

        ("make_prisoners", [
            (neg | party_slot_eq, "$current_town", "slot_village_state", svs_looted),
            (neg | party_slot_eq, "$current_town", "slot_village_state", svs_being_raided),
            (neg | party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
         ], "Enslave villagers.", [
            (jump_to_menu, "mnu_make_prisoners"),
        ]),

        ("village_loot", [
            (party_slot_eq, "$current_town", "slot_village_state", 0),
            (neg | party_slot_ge, "$current_town", "slot_village_infested_by_bandits", 1),
            (store_faction_of_party, ":center_faction", "$current_town"),
            (store_relation, ":reln", "fac_player_supporters_faction", ":center_faction"),
            (lt, ":reln", 0),
        ], "Pillage and burn this village.", [
            (jump_to_menu, "mnu_village_start_attack"),
        ]),

        ("forget_it", [], "Forget it.", [(jump_to_menu, "mnu_village")]),
    ]),
]

menus += force_recruit.menus + loot.menus + make_prisoners.menus \
         + steal_cattle.menus \
         + take_food.menus

scripts = loot.scripts + steal_cattle.scripts

simple_triggers = loot.simple_triggers
