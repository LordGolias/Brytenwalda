from source.header_operations import *
from source.header_common import *

from source.module_constants import *


scripts = [
    ("initialize_multiplayer", [
        #for multiplayer mode
      (assign, "$g_multiplayer_selected_map", multiplayer_scenes_begin),
      (assign, "$g_multiplayer_respawn_period", 5),
      (assign, "$g_multiplayer_round_max_seconds", 900), #chief capitan cambia para que sean 900 seg -15 m- en vez de 300, que es muy corto
      (assign, "$g_multiplayer_game_max_minutes", 60), #chief capitan cambia para que sean 60 m en vez de 30
      (assign, "$g_multiplayer_game_max_points", 300),
#fire arrow multiplayer chief
            (troop_set_slot, "trp_global_value", slot_gloval_show_fire_arrow_particle, 0),
      (troop_set_slot, "trp_global_value", slot_gloval_fire_arrow_key, 0x23), #key h
      (troop_set_slot, "trp_global_value", slot_gloval_max_fire_arrow, 100),
      (troop_set_slot, "trp_global_value", slot_gloval_max_flame_slot, 40),
#fire arrow chief acaba

     (server_get_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
      (server_get_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
      (assign, "$g_multiplayer_point_gained_from_flags", 100),
      (assign, "$g_multiplayer_point_gained_from_capturing_flag", 5),
      (assign, "$g_multiplayer_game_type", 0),
      (assign, "$g_multiplayer_team_1_faction", "fac_kingdom_1"),
      (assign, "$g_multiplayer_team_2_faction", "fac_kingdom_2"),
      (assign, "$g_multiplayer_next_team_1_faction", "$g_multiplayer_team_1_faction"),
      (assign, "$g_multiplayer_next_team_2_faction", "$g_multiplayer_team_2_faction"),
      (assign, "$g_multiplayer_num_bots_team_1", 0),
      (assign, "$g_multiplayer_num_bots_team_2", 0),
      (assign, "$g_multiplayer_number_of_respawn_count", 0),
      (assign, "$g_multiplayer_num_bots_voteable", 50),
      (assign, "$g_multiplayer_max_num_bots", 900), #multiplayer chief cambia de 101 a 900
      (assign, "$g_multiplayer_factions_voteable", 1),
      (assign, "$g_multiplayer_maps_voteable", 1),
      (assign, "$g_multiplayer_kick_voteable", 1),
      (assign, "$g_multiplayer_ban_voteable", 1),
      (assign, "$g_multiplayer_valid_vote_ratio", 51), #more than 50 percent
      (assign, "$g_multiplayer_auto_team_balance_limit", 3), #auto balance when difference is more than 2
      (assign, "$g_multiplayer_player_respawn_as_bot", 1),
      (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
      (assign, "$g_multiplayer_mission_end_screen", 0),
      (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
      (assign, "$g_multiplayer_welcome_message_shown", 0),
      (assign, "$g_multiplayer_allow_player_banners", 1),
      (assign, "$g_multiplayer_force_default_armor", 1),
      (assign, "$g_multiplayer_disallow_ranged_weapons", 0),

      (assign, "$g_multiplayer_initial_gold_multiplier", 100),
##      (assign, "$g_multiplayer_initial_gold_team1", 100), #chief capitan
##      (assign, "$g_multiplayer_initial_gold_team2", 100), #chief capitan
      (assign, "$g_multiplayer_battle_earnings_multiplier", 100),
      (assign, "$g_multiplayer_round_earnings_multiplier", 100),

      #faction banners chief
      (faction_set_slot, "fac_kingdom_1", "slot_faction_banner", "mesh_banner_kingdom_a"),
      (faction_set_slot, "fac_kingdom_2", "slot_faction_banner", "mesh_banner_kingdom_b"),
      (faction_set_slot, "fac_kingdom_3", "slot_faction_banner", "mesh_banner_kingdom_c"),
      (faction_set_slot, "fac_kingdom_4", "slot_faction_banner", "mesh_banner_kingdom_d"),
      (faction_set_slot, "fac_kingdom_5", "slot_faction_banner", "mesh_banner_kingdom_e"),
      (faction_set_slot, "fac_kingdom_6", "slot_faction_banner", "mesh_banner_kingdom_f"),
      (faction_set_slot, "fac_kingdom_7", "slot_faction_banner", "mesh_banner_kingdom_g"),
      (faction_set_slot, "fac_kingdom_8", "slot_faction_banner", "mesh_banner_kingdom_h"),
      (faction_set_slot, "fac_kingdom_9", "slot_faction_banner", "mesh_banner_kingdom_i"),
      (faction_set_slot, "fac_kingdom_10", "slot_faction_banner", "mesh_banner_kingdom_j"),
      (faction_set_slot, "fac_kingdom_11", "slot_faction_banner", "mesh_banner_kingdom_k"),
      (faction_set_slot, "fac_kingdom_12", "slot_faction_banner", "mesh_banner_kingdom_l"),
      (faction_set_slot, "fac_kingdom_13", "slot_faction_banner", "mesh_banner_kingdom_ll"),
      (faction_set_slot, "fac_kingdom_14", "slot_faction_banner", "mesh_banner_kingdom_m"),
      (faction_set_slot, "fac_kingdom_15", "slot_faction_banner", "mesh_banner_kingdom_n"),
      (faction_set_slot, "fac_kingdom_16", "slot_faction_banner", "mesh_banner_kingdom_o"),
      (faction_set_slot, "fac_kingdom_17", "slot_faction_banner", "mesh_banner_kingdom_p"),
      (faction_set_slot, "fac_kingdom_18", "slot_faction_banner", "mesh_banner_kingdom_q"),
      (faction_set_slot, "fac_kingdom_19", "slot_faction_banner", "mesh_banner_kingdom_r"),
      (faction_set_slot, "fac_kingdom_20", "slot_faction_banner", "mesh_banner_kingdom_s"),
      (faction_set_slot, "fac_kingdom_21", "slot_faction_banner", "mesh_banner_kingdom_t"),
      (faction_set_slot, "fac_kingdom_22", "slot_faction_banner", "mesh_banner_kingdom_u"),
      (faction_set_slot, "fac_kingdom_23", "slot_faction_banner", "mesh_banner_kingdom_v"),
      (faction_set_slot, "fac_kingdom_24", "slot_faction_banner", "mesh_banner_kingdom_w"),
      (faction_set_slot, "fac_kingdom_25", "slot_faction_banner", "mesh_banner_kingdom_x"),
      (faction_set_slot, "fac_kingdom_26", "slot_faction_banner", "mesh_banner_kingdom_y"),
      (faction_set_slot, "fac_kingdom_27", "slot_faction_banner", "mesh_banner_kingdom_z"),
      (faction_set_slot, "fac_kingdom_28", "slot_faction_banner", "mesh_banner_kingdom_2a"),
      (faction_set_slot, "fac_kingdom_29", "slot_faction_banner", "mesh_banner_kingdom_2b"),
      (faction_set_slot, "fac_kingdom_30", "slot_faction_banner", "mesh_banner_kingdom_2c"),
      (faction_set_slot, "fac_kingdom_31", "slot_faction_banner", "mesh_banner_kingdom_2d"),
#chief acaba multiplayer chief

      (try_for_range, ":cur_item", all_items_begin, all_items_end),
        (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end),
          (store_sub, ":faction_index", ":cur_faction", npc_kingdoms_begin),
          (val_add, ":faction_index", "slot_item_multiplayer_faction_price_multipliers_begin"),
          (item_set_slot, ":cur_item", ":faction_index", 100), #100 is the default price multiplier
        (try_end),
      (try_end),
      (store_sub, ":swadian_price_slot", "fac_kingdom_1", npc_kingdoms_begin),
      (val_add, ":swadian_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":vaegir_price_slot", "fac_kingdom_2", npc_kingdoms_begin),
      (val_add, ":vaegir_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":khergit_price_slot", "fac_kingdom_3", npc_kingdoms_begin),
      (val_add, ":khergit_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":nord_price_slot", "fac_kingdom_4", npc_kingdoms_begin),
      (val_add, ":nord_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":rhodok_price_slot", "fac_kingdom_5", npc_kingdoms_begin),
      (val_add, ":rhodok_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":sarranid_price_slot", "fac_kingdom_6", npc_kingdoms_begin),
      (val_add, ":sarranid_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":swadian2_price_slot", "fac_kingdom_7", npc_kingdoms_begin),
      (val_add, ":swadian2_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":vaegir2_price_slot", "fac_kingdom_8", npc_kingdoms_begin),
      (val_add, ":vaegir2_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":khergit2_price_slot", "fac_kingdom_9", npc_kingdoms_begin),
      (val_add, ":khergit2_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":nord2_price_slot", "fac_kingdom_10", npc_kingdoms_begin),
      (val_add, ":nord2_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":rhodok2_price_slot", "fac_kingdom_11", npc_kingdoms_begin),
      (val_add, ":rhodok2_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":sarranid2_price_slot", "fac_kingdom_12", npc_kingdoms_begin),
      (val_add, ":sarranid2_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":swadian3_price_slot", "fac_kingdom_13", npc_kingdoms_begin),
      (val_add, ":swadian3_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":vaegir3_price_slot", "fac_kingdom_14", npc_kingdoms_begin),
      (val_add, ":vaegir3_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":khergit3_price_slot", "fac_kingdom_15", npc_kingdoms_begin),
      (val_add, ":khergit3_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":nord3_price_slot", "fac_kingdom_16", npc_kingdoms_begin),
      (val_add, ":nord3_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":rhodok3_price_slot", "fac_kingdom_17", npc_kingdoms_begin),
      (val_add, ":rhodok3_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":sarranid3_price_slot", "fac_kingdom_18", npc_kingdoms_begin),
      (val_add, ":sarranid3_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":swadian4_price_slot", "fac_kingdom_19", npc_kingdoms_begin),
      (val_add, ":swadian4_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":vaegir4_price_slot", "fac_kingdom_20", npc_kingdoms_begin),
      (val_add, ":vaegir4_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":khergit4_price_slot", "fac_kingdom_21", npc_kingdoms_begin),
      (val_add, ":khergit4_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":nord4_price_slot", "fac_kingdom_22", npc_kingdoms_begin),
      (val_add, ":nord4_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":rhodok4_price_slot", "fac_kingdom_23", npc_kingdoms_begin),
      (val_add, ":rhodok4_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":sarranid4_price_slot", "fac_kingdom_24", npc_kingdoms_begin),
      (val_add, ":sarranid4_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":swadian5_price_slot", "fac_kingdom_25", npc_kingdoms_begin),
      (val_add, ":swadian5_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":vaegir5_price_slot", "fac_kingdom_26", npc_kingdoms_begin),
      (val_add, ":vaegir5_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":khergit5_price_slot", "fac_kingdom_27", npc_kingdoms_begin),
      (val_add, ":khergit5_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":nord5_price_slot", "fac_kingdom_28", npc_kingdoms_begin),
      (val_add, ":nord5_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":rhodok5_price_slot", "fac_kingdom_29", npc_kingdoms_begin),
      (val_add, ":rhodok5_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":sarranid5_price_slot", "fac_kingdom_30", npc_kingdoms_begin),
      (val_add, ":sarranid5_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
      (store_sub, ":sarranid6_price_slot", "fac_kingdom_31", npc_kingdoms_begin),
      (val_add, ":sarranid6_price_slot", "slot_item_multiplayer_faction_price_multipliers_begin"),
#chief anade hasta aqui faciones multiplayer chief
#      (item_set_slot, "itm_spanish_horset2", ":khergit_price_slot", 50),

      #arrows
      (item_set_slot, "itm_arrows1", "slot_item_multiplayer_item_class", multi_item_class_type_arrow),
      #bolts
      (item_set_slot, "itm_bolts", "slot_item_multiplayer_item_class", multi_item_class_type_bolt),
      (item_set_slot, "itm_slingrocks", "slot_item_multiplayer_item_class", multi_item_class_type_bolt),
      #bows
      (item_set_slot, "itm_basic_sling", "slot_item_multiplayer_item_class", multi_item_class_type_bow),
      (item_set_slot, "itm_pict_crossbow", "slot_item_multiplayer_item_class", multi_item_class_type_bow),
      (item_set_slot, "itm_huntingbow", "slot_item_multiplayer_item_class", multi_item_class_type_bow),
      (item_set_slot, "itm_shortbow", "slot_item_multiplayer_item_class", multi_item_class_type_bow),
      (item_set_slot, "itm_cavbowbandit", "slot_item_multiplayer_item_class", multi_item_class_type_bow),
      (item_set_slot, "itm_longbow", "slot_item_multiplayer_item_class", multi_item_class_type_bow),
      #swords
      (item_set_slot, "itm_espada_kirkburn", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_briton_richswordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_spathaswordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_gaelicsword1", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_rich_spathaswordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_spathasword", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_sword2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_sword3", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_sword4t2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_angleswordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_saxonswordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_bamburghsword2t2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_bamburghsword2t2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_saxonswordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_germanicswordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_saxondenaswordt3", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_britonswordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_saxonswordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_sciansword", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_scianswordbone", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_irish_longsword", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_irish_shsword", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_noble_shswordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_rich_shswordt3", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_pictish_longsword1", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_godelic_swordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_britonswordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_pommel_swordt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_pommel_swordt3", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_jute_richsword", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_bamburghsword2t2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
#espada 2h
      (item_set_slot, "itm_britonswordt2", "slot_item_multiplayer_item_class", multi_item_class_type_two_handed_sword),

#cuchillas cortas
      (item_set_slot, "itm_hunting_knife", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_lang_knifet2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_knife1", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_scianshswordt1", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_scianshswordbone", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_talak_seaxkni", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_seaxt4", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_langseaxt2", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_knisxclearvert3", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_seaxt3", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
      (item_set_slot, "itm_ornate_seaxt3", "slot_item_multiplayer_item_class", multi_item_class_type_sword),
#axe
      (item_set_slot, "itm_axe1", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_axe3", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_axe2_crude", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_maul1h_blunt", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_ironhammerlong", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_ironhammerlong", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_axe4", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_germanic_axelongt2", "slot_item_multiplayer_item_class", multi_item_class_type_axe),

      (item_set_slot, "itm_axe2", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_axe_englet2", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_axe_longfrankisht3", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_axe_britonbattlet2", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_decor_axet3", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_saxon_axet2", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_axe_1hlongt2", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_commonhammer_blunt", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_blackened_axet2", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
      (item_set_slot, "itm_pictish_waraxet2", "slot_item_multiplayer_item_class", multi_item_class_type_axe),
#hachas 2h
      (item_set_slot, "itm_battle_axe2ht2", "slot_item_multiplayer_item_class", multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_tree_axe2h", "slot_item_multiplayer_item_class", multi_item_class_type_two_handed_axe),

      #blunt
	  (item_set_slot, "itm_club_stick", "slot_item_multiplayer_item_class", multi_item_class_type_blunt),
      (item_set_slot, "itm_clubsmooth", "slot_item_multiplayer_item_class", multi_item_class_type_blunt),
      (item_set_slot, "itm_clubcudgel", "slot_item_multiplayer_item_class", multi_item_class_type_blunt),
      (item_set_slot, "itm_club_thorny", "slot_item_multiplayer_item_class", multi_item_class_type_blunt),
      (item_set_slot, "itm_club3", "slot_item_multiplayer_item_class", multi_item_class_type_blunt),
      (item_set_slot, "itm_club3", "slot_item_multiplayer_item_class", multi_item_class_type_blunt),
      (item_set_slot, "itm_club3", "slot_item_multiplayer_item_class", multi_item_class_type_blunt),

      #spears
      (item_set_slot, "itm_staff1", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_quarter_staff", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spear_lightgael", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_warspear_godelict3", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spear_hvy", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spear1", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spearlight", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spear_hasta", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spearboar", "slot_item_multiplayer_item_class", multi_item_class_type_spear),

      (item_set_slot, "itm_spearlong", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spearwarlong", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spear_blade2t2", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spear_blade2t2", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spear_blade2t2", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spear_briton2ht3", "slot_item_multiplayer_item_class", multi_item_class_type_spear), #a dos manos
      (item_set_slot, "itm_spear_britonshortt2", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spear_britonmedt2", "slot_item_multiplayer_item_class", multi_item_class_type_spear),

      (item_set_slot, "itm_spear_britonlight", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_spear_briton_longt2", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_longspeart3", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_germanshortspeart2", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_engle_speart2", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_twohand_speart3", "slot_item_multiplayer_item_class", multi_item_class_type_spear), #a dos manos
      (item_set_slot, "itm_hunting_spear", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_hunting_spear", "slot_item_multiplayer_item_class", multi_item_class_type_spear),
      (item_set_slot, "itm_medium_speaript3", "slot_item_multiplayer_item_class", multi_item_class_type_spear),

      (item_set_slot, "itm_wessexbanner1", "slot_item_multiplayer_item_class", multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_cavalrybannert2", "slot_item_multiplayer_item_class", multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_spearbannert2", "slot_item_multiplayer_item_class", multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_spearbanner4", "slot_item_multiplayer_item_class", multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_spearbanner5", "slot_item_multiplayer_item_class", multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_wessexbanner6", "slot_item_multiplayer_item_class", multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_wessexbanner7", "slot_item_multiplayer_item_class", multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_wessexbanner8", "slot_item_multiplayer_item_class", multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_wessexbanner9", "slot_item_multiplayer_item_class", multi_item_class_type_two_handed_sword),

      # shields
      (try_for_range, ":shield", shields_begin, shields_end),
          (item_set_slot, ":shield", "slot_item_multiplayer_item_class", multi_item_class_type_small_shield),
      (try_end),

      #throwing
      (item_set_slot, "itm_cavaljavelins", "slot_item_multiplayer_item_class", multi_item_class_type_throwing),
      (item_set_slot, "itm_wooden_javelins", "slot_item_multiplayer_item_class", multi_item_class_type_throwing),
      (item_set_slot, "itm_javelins", "slot_item_multiplayer_item_class", multi_item_class_type_throwing),
      (item_set_slot, "itm_throwing_spear", "slot_item_multiplayer_item_class", multi_item_class_type_throwing),
      (item_set_slot, "itm_cavaljavelins", "slot_item_multiplayer_item_class", multi_item_class_type_throwing),
      (item_set_slot, "itm_angons", "slot_item_multiplayer_item_class", multi_item_class_type_throwing),
      (item_set_slot, "itm_angonst2", "slot_item_multiplayer_item_class", multi_item_class_type_throwing),
      (item_set_slot, "itm_darts", "slot_item_multiplayer_item_class", multi_item_class_type_throwing),

      (item_set_slot, "itm_horn_multiplayer", "slot_item_multiplayer_item_class", multi_item_class_type_throwing),  #cuerno

      (item_set_slot, "itm_light_throwing_axes", "slot_item_multiplayer_item_class", multi_item_class_type_throwing_axe),
      (item_set_slot, "itm_throwing_axes", "slot_item_multiplayer_item_class", multi_item_class_type_throwing_axe),
       #armors
#metal
      (item_set_slot, "itm_mailtunic_brownclk", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_olive", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_gry", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_wht", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),

      (item_set_slot, "itm_noblearmor6res", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_brown", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
       (item_set_slot, "itm_longmail_coat_king4", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_longmail_coat_kingred", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_longmail_coat_king3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mail_goatist", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_ltbrown", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_redclk", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_blkclk", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_ltgreen", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_brown", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_brownclk", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_greycheap", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_noblemanshirt3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailnoble_redclk1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_scale_white_armor", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_blk", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailnoble_greenclk", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailnoble_deerbrclk", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_lorica_pink", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_scale_bronze_blueorange", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_noblearmor14res", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_lorica_eggwht", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_lorica_white", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_noblearmor16res", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailshirt_3_trig", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_lorica_brightgreen", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_wht", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_olive", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_gry", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
       (item_set_slot, "itm_mailtunic_brownclk", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
       (item_set_slot, "itm_mailtunic_wht", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
    (item_set_slot, "itm_mailbyrnie_longfurred", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
     (item_set_slot, "itm_mailbyrniegreen", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
     (item_set_slot, "itm_mailbyrnieyelo", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
     (item_set_slot, "itm_noblearmor7res", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_lamellar2blue", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_lamellarred1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_lamellargrey", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_lamellarbrown", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailcuir_bouilli", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_scale_bronzegreen", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_scale_vestgrey", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_scale_vest_red", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailtunic_redbrown", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_scale_armor1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_scale_greyvestelite", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_scale_greykhergitfemale", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_scale_bronze_blueorange", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_scale_brown_armor", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mail_sleevelessgrn", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_lamellar2yellow", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mailshirt_yellow", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
#cuero
      (item_set_slot, "itm_pelt_coat1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_pelt_coat2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_vae_thickcoat1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_vae_thickcoat2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_vae_thickcoat3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_hide_coat6", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_hide_coat1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_merch_furjacketwhite", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_merch_furjacket2t3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_merch_furjacketyelo", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_merch_furjacketyelo", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_merch_furjacketyelo", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_gatheredcloaks1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_gatheredcloaks3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_gatheredcloaks4", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mail_furredt2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rawhide_vest_green", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rawhide_coat9grey", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rawhide_vest_blue", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rawhide_coat2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rawhide_coat3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rawhide_coat2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rawhide_coat5t3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rawhide_vest_red", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rawhide_coat6white", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rawhide_coat7green", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rawhide_coat7green", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rawhide_coat1tier2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_linen_coatbrown", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_linen_coatwhite", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_linen_coatblue", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_linen_coattan", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_linen_coatwcloak", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_jack_armorpaddedred", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_jack_armorgreen", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_scale_bronzegreen", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_jack_armorfadedblue", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_jack_armorfadedblue", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_jack_armorgreen", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_jack_armorfadedblue", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_jack_armorpaddedred", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_goatist_tuniccoat", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_redpantsbody_woad11", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bluepantsbody_woad02t2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_blue_cloak_hood", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),

#ropa
      (item_set_slot, "itm_thick_body", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_richlong_tunic1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),

      (item_set_slot, "itm_leather_tunic1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bluepantsbody_woad05", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),

      (item_set_slot, "itm_blue_shorttunic2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_celtcloakedbody03", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_celtcloakedbody02", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bluepantsbody_woad04", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bluepantsbody_woad04", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_nobleman_outfit", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bluepantsbody_woad04", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bluepantsbody_woad02t2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_blue_linendress", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_courtly_outfit", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_gaelic_jacketgray", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_gaelic_jacketgray", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_robe_beige", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_monk_robe", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_cloaked_tunic1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_cloaked_leathertunict2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_cloaked_tunic2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_gaelic_jacketgrn", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_cloaked_tunicorange", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_cloaked_tunicgreen", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_german_tunica", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_wessex_tunic1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_wessex_tunic4", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_german_tunic5", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_saxon_tunic7", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_saxon_tunic7", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunicwhite", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_ptunic3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_ptunic3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_shirtblue", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_briton_tunic2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_noblemanshirt1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_noblemanshirt2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_noblemanshirt3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_wessex_tunic3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_peasant_ftunic", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),

	  (item_set_slot, "itm_noblearmor4res", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_noblearmor5res", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_noblearmor6res", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_noblearmor7res", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_noblearmor8res", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_gatheredcloaks1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_gatheredcloaks2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_gatheredcloaks3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_gatheredcloaks5", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_vaelicus_tunic27", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_byrnietunice", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_striped_tunic26", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_vaelicus_tunic27", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
	  (item_set_slot, "itm_vaelicus_tunic35", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),

      (item_set_slot, "itm_tunicsleevelessb", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic9", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_farmertunic26", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic5", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_german_tunica", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_peasant_etunic", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_peasant_ftunic", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic11", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_german_tunic2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_tunicblue8", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_tunicsleeveless3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_tunicsleeveless6", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_tunicsleevelessgreen7", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_tunicsleeveless8", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic10", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic5", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_tunicsleeveless2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_shirtblue", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_shirtaqua", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_shirtylw", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_shirtblue", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_shirtgrey", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_briton_tunic2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_german_tunic2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bltunicgrn", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bltunic01", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic12", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mercia_tunicgrn", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mercia_tunicgrn", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_blue_shorttunic", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_yellowtunic1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic7", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_peasant_archertunic", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_noblemanshirt2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_noblemanshirt3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_noblemanshirt4", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ladytunicgodelic", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),

      (item_set_slot, "itm_bltunic05", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bltunic06", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bltunic08", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bltunic07", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bltunic11", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_ptunic2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bl_tunicred", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bluenorthmanshirt", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_rednorthmanshirt", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_mercia_tunicgrn", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_war_paintbody_two", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_war_paintbodyus", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_war_paintbody1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_war_paintbody5", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_war_paintbody6", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_war_paintbody4", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_war_paintbody13", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_war_paintbody4", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_war_paintbody4", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_war_paintbody8", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_picto_paintfat1", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_picto_paintfat2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_celtcloakedbody01", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_celtcloakedbody02", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_celtcloakedbody06", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bluepantsbody_woad04", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_richlong_tunic3", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_german_tunic5", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),

      (item_set_slot, "itm_bluepantsbody_woad04", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_greenpantsbody_woad03", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_redpantsbody_woad11", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bluepantsbody_woad05", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bluepantsbody_woad04", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bluepantsbody_woad02t2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_bluepantsbody_woad02t2", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_greypantsbody_woad01", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),
      (item_set_slot, "itm_blackpantsbody_woad10", "slot_item_multiplayer_item_class", multi_item_class_type_light_armor),

      #boots
      (item_set_slot, "itm_cheap_shoes", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_ankleboots", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_leather_shoes", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_shoes2bare", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_shoes2bare", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_shoes1", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_shoes1", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_shoes1green", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_shoes1blue", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_shoes1blue", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_shoes1green", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_shoes2grey", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_shoes2grey", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_greaves1", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_splinted_leather_greaves", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_greaves1", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_light_leather_boots", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_noble_shoesorange", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
      (item_set_slot, "itm_noble_shoesorange", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
	  (item_set_slot, "itm_shoes2green", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
	  (item_set_slot, "itm_leather_bootstall", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
	  (item_set_slot, "itm_greaves1", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
	  (item_set_slot, "itm_noble_shoesblue", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
	  (item_set_slot, "itm_noble_shoesorange", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
	  (item_set_slot, "itm_noble_shoesorange", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),
	  (item_set_slot, "itm_splinted_leather_greaves", "slot_item_multiplayer_item_class", multi_item_class_type_light_foot),


      #helmets
      (item_set_slot, "itm_plaincloakltblue", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_plaincloakbeige", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_plaincloakbrown", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_plaincloakltblue", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_plaincloakred", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_plaincloakbeige", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_plaincloakbrown", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_irishcloak", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_cloak_boar_furcap", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_celta_cloak1", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_celta_cloak1", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_green_cloak", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_blue_cloak_hood", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_red_cloak", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_wealthytunic5", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),

      (item_set_slot, "itm_looseblackhood", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_assassinhood", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_woolencap_newblu", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_woolencap_newblk", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_woolencap_newblk", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_woolencap_red", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_woolencap_newgrn", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_woolencap", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_blue_cloak_hood", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),

      (item_set_slot, "itm_hoodnewwht", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_hoodnewblu", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_hoodnewblk", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_blackhood", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_bandanawht", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_bandanablack", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_common_hood", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_cloak_boar_furcap", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_goatcap1", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_helm_leathert2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
	  (item_set_slot, "itm_leathercap1", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
	  (item_set_slot, "itm_roman_helmlatet2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
	  (item_set_slot, "itm_skullcap_reinforcedt2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_skullcap_reinforcedt1", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_skullcapt1", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_helmboar3", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_leather_captainhelm", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_leather_helm_tan", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_leather_helm_grey", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_rathos_bowlhelmet", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_bowlhelmet", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_bowl_helmet_nasal", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_roman_helmlate", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_spangenhelmgerm_trim", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_elite_helm1boar", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),

      (item_set_slot, "itm_arming_cap", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_roman_helmlate", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_helmboar2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_spangenhelmblight", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_helmet_stripedt3", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_saxon_helmt2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_briton_helm", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_romanelitehelmt3", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dux_ridgehelm", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_spangenhelma_ornate", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),

      (item_set_slot, "itm_angloblackbrownhelm", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_briton_helmengravedt2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_briton_helm_3", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_briton_helmtrimt2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_briton_helmslvtrimt3", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_spangenhelma1", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_spangenhelmb1", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_frisian_helm1", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_hornhelmet1", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_hornhelmet2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_hornhelmet3_t2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_copper_helmet", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_jutehelmt3", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_khergit_cavalry_helmet", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_frisian_helm3t2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_spangenhelmalight", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_spangenhelma_yellow", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),

      (item_set_slot, "itm_mierce_helmt3", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_helmboar2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_helmboar5", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_elite_helm1boar", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_elite_helm1boar", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_elite_helm2boar", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_frisian_helm3t2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_elite_helm1boar", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_helmboar2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_helmboar2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_frisian_helm1", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_elite_helm1boar", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),


      (item_set_slot, "itm_bronzebowlhelmet", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_ironceltbowlhelmet", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_szpadelhelm1", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_szpadelhelm5engravedt3", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_szpadelhelm2engraved", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_szpadelhelm3t2", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_ironceltbowlhelmet", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_bronze_warlord_helmetboar", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),
      (item_set_slot, "itm_dena_elite_helm2boar", "slot_item_multiplayer_item_class", multi_item_class_type_light_helm),

	  #gloves
      (item_set_slot, "itm_leather_gloves1", "slot_item_multiplayer_item_class", multi_item_class_type_glove),

      #1-Swadian Warriors
      #1a-Swadian Crossbowman britones
#arqueros britones################################
      #1
      # ['itm_throwing_spear','itm_noble_shoesblue','itm_shoes2green','itm_shoes2grey','itm_shoes1','itm_mailbyrniegrey',
        # 'itm_mailbyrniewhitered','itm_mailbyrnieblue','itm_mail_sleevelessbrn','itm_noblearmor7res','itm_mailbyrnie_longfurred',
        # 'itm_mailcuir_bouilli','itm_mail_largering','itm_linen_coatblue','itm_spear_blade2t2','itm_spear_blade2t2',
        # 'itm_knife1','itm_britonswordt2','itm_arming_cap','itm_roman_helmlate'] + items_shields['briton'][1]['heavy']
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer"),
##
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_1", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer"),
##
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleevelessb", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic9", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic5", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer"),
      #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_23", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtylw", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunicgrn", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer2"),
      #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_1", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic12", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_german_tunica", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_ftunic", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_archertunic", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer3"),
      #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_9", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleevelessb", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic9", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic5", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_farmertunic26", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer4"),
      #5
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_8", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleevelessb", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic9", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer5"),
      #6
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_1", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleevelessb", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic9", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic5", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_farmertunic26", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer6"),
      #7
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_23", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic12", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_german_tunica", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_ftunic", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_archertunic", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer7"),
      #8
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_1", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtylw", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunicgrn", "trp_briton_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer8"),
      #9
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_1", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_ftunic", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_archertunic", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtylw", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer9"),
      #10
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_9", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleevelessb", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic9", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic5", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_farmertunic26", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer10"),
      #11
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_8", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic5", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_farmertunic26", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer11"),
      #12
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_1", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtylw", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunicgrn", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer12"),
      #13
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_23", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic12", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_german_tunica", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_ftunic", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_archertunic", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer13"),
      #14
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_8", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic12", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_ftunic", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_archertunic", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_farmertunic26", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer14"),
      #15
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club_stick", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_briton_infantryt4_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longbow", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackened_axet2", "trp_briton_infantryt4_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_9", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_infantryt4_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_archertunic", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtylw", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_briton_infantryt4_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_briton_infantryt4_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_briton_infantryt4_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_briton_infantryt4_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_briton_infantryt4_multiplayer15"),

###################################

      #infanteria
      #1b-Swadian Infantry
      #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatblue", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_22", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_1", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_17", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt2", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_briton_skirmishert3_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_briton_skirmishert3_multiplayer"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer"),

###

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer"),
      #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_briton_skirmishert3_multiplayer2"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_8", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_4", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt3", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_briton_skirmishert3_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_briton_skirmishert3_multiplayer2"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_briton_skirmishert3_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer2"),
      #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_briton_skirmishert3_multiplayer3"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_5", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_6", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt4", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_briton_skirmishert3_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakred", "trp_briton_skirmishert3_multiplayer3"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_briton_skirmishert3_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer3"),
      #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatblue", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer4"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_22", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_1", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_2", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt2", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_skirmishert3_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_briton_skirmishert3_multiplayer4"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_briton_skirmishert3_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer4"),
      #5
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_briton_skirmishert3_multiplayer5"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_8", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_4", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt3", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_skirmishert3_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_briton_skirmishert3_multiplayer5"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_briton_skirmishert3_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer5"),
      #6
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_briton_skirmishert3_multiplayer6"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_5", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_6", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt4", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtylw", "trp_briton_skirmishert3_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_briton_skirmishert3_multiplayer6"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_briton_skirmishert3_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer6"),
      #7
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatblue", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer7"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_12", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_10", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt4", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_briton_skirmishert3_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_briton_skirmishert3_multiplayer7"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_briton_skirmishert3_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer7"),
      #8
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_briton_skirmishert3_multiplayer8"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_16", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_17", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt2", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_briton_skirmishert3_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakred", "trp_briton_skirmishert3_multiplayer8"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_briton_skirmishert3_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer8"),
      #9
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_briton_skirmishert3_multiplayer9"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_22", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_1", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_17", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt3", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_briton_skirmishert3_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_briton_skirmishert3_multiplayer9"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_briton_skirmishert3_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer9"),
      #10
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_briton_skirmishert3_multiplayer10"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_2", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_16", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt2", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_briton_skirmishert3_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_briton_skirmishert3_multiplayer10"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_briton_skirmishert3_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer10"),
      #11
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatblue", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer11"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_8", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_10", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_16", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_skirmishert3_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakred", "trp_briton_skirmishert3_multiplayer11"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_briton_skirmishert3_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer11"),
      #12
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_briton_skirmishert3_multiplayer12"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_29", "trp_briton_skirmishert3_multiplayer12"),
       (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_4", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_17", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtylw", "trp_briton_skirmishert3_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_briton_skirmishert3_multiplayer12"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_briton_skirmishert3_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer12"),
      #13
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatblue", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_briton_skirmishert3_multiplayer13"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_4", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_10", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_briton_skirmishert3_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_briton_skirmishert3_multiplayer13"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_briton_skirmishert3_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer13"),
      #14
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_briton_skirmishert3_multiplayer14"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_29", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_4", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_16", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_briton_skirmishert3_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_briton_skirmishert3_multiplayer14"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_briton_skirmishert3_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer14"),
      #15
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_briton_skirmishert3_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_skirmishert3_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_briton_skirmishert3_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_briton_skirmishert3_multiplayer15"),

#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_22", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_5", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_6", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_briton_skirmishert3_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_briton_skirmishert3_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakred", "trp_briton_skirmishert3_multiplayer15"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_briton_skirmishert3_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_briton_skirmishert3_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_briton_skirmishert3_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_briton_skirmishert3_multiplayer15"),


##########################################################
      #1c-Swadian Man At Arms
       #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer"),

#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_1", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_2", "trp_briton_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_briton_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer2"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_3", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_4", "trp_briton_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_briton_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer2"),
       #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer3"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_5", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_6", "trp_briton_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_briton_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer3"),
       #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer4"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_7", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_8", "trp_briton_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_briton_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer4"),
       #5
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer5"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_8", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_11", "trp_briton_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer5"),
       #6
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer6"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_1", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_11", "trp_briton_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_briton_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer6"),
       #7
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer7"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_2", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_8", "trp_briton_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_briton_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer7"),
       #8
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer8"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_3", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_8", "trp_briton_horseman_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_briton_horseman_multiplayer8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer8"),
       #9
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer9"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_5", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_7", "trp_briton_horseman_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_briton_horseman_multiplayer9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer9"),
       #10
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer10"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_4", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_7", "trp_briton_horseman_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_briton_horseman_multiplayer10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer10"),
       #11
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer11"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_5", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_8", "trp_briton_horseman_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer11"),
       #12
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer12"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_3", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_8", "trp_briton_horseman_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer12"),
       #13
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer13"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_4", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_11", "trp_briton_horseman_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer13"),
       #14
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer14"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_1", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_5", "trp_briton_horseman_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_briton_horseman_multiplayer14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer14"),
       #15
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_briton_horseman_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_briton_horseman_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_briton_horseman_multiplayer15"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_4", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_8", "trp_briton_horseman_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_briton_horseman_multiplayer15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_briton_horseman_multiplayer15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_briton_horseman_multiplayer15"),
####################################################
      # #1d-Swadian Mounted Crossbowman britones acaban

      #2-Vaegir Warriors
      #2a-Vaegir Archer
      #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_axet2", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic12", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_tunic2", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic2", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic1", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cheap_shoes", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblu", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_red", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newgrn", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap", "trp_saxon_infantryt4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club3", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_seaxkni", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_13", "trp_saxon_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_6", "trp_saxon_infantryt4_multiplayer"),
      #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_axet2", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic12", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_tunic2", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic2", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic1", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cheap_shoes", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblu", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_red", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newgrn", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap", "trp_saxon_infantryt4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club3", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_seaxkni", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_10", "trp_saxon_infantryt4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_11", "trp_saxon_infantryt4_multiplayer2"),
      #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_axet2", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic12", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_tunic2", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic2", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic1", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cheap_shoes", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblu", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_red", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newgrn", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap", "trp_saxon_infantryt4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club3", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_seaxkni", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_11", "trp_saxon_infantryt4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_12", "trp_saxon_infantryt4_multiplayer3"),

      #2b-Vaegir Spearman
      #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe4", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2_crude", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_vaegir_spearman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hvy", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jute_richsword", "trp_vaegir_spearman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_2", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_vaegir_spearman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_7", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_vaegir_spearman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_32", "trp_vaegir_spearman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_vaegir_spearman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_vaegir_spearman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluenorthmanshirt", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rednorthmanshirt", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_vest_blue", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat2", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor6res", "trp_vaegir_spearman_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_brown", "trp_vaegir_spearman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_vaegir_spearman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblk", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_vaegir_spearman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner1", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_vaegir_spearman_multiplayer"),
      #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe4", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2_crude", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_vaegir_spearman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hvy", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jute_richsword", "trp_vaegir_spearman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_3", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_10", "trp_vaegir_spearman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_10", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_h", "trp_vaegir_spearman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_1", "trp_vaegir_spearman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_vaegir_spearman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_vaegir_spearman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic12", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bl_tunicred", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat5t3", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_vest_red", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor6res", "trp_vaegir_spearman_multiplayer2"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_brown", "trp_vaegir_spearman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_vaegir_spearman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblk", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner1", "trp_vaegir_spearman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_vaegir_spearman_multiplayer2"),
      #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe4", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2_crude", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_vaegir_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hvy", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jute_richsword", "trp_vaegir_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_3", "trp_vaegir_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_10", "trp_vaegir_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_5", "trp_vaegir_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_vaegir_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_vaegir_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_shorttunic", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic1", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat1tier2", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_vest_green", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor6res", "trp_vaegir_spearman_multiplayer3"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_brown", "trp_vaegir_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_vaegir_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblk", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner1", "trp_vaegir_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_vaegir_spearman_multiplayer3"),

#frisian

            (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul1h_blunt", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2_crude", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_commonhammer_blunt", "trp_frisian_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear1", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword4t2", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_frisian_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_frisian_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_frisian_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_wht", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessex_tunic4", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_shorttunic2", "trp_frisian_spearman_multiplayer3"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_frisian_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesblue", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_frisian_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar5", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar3", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_frisian_helm1", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_frisian_helm3t2", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_frisian_spearman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_frisian_spearman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_frisian_spearman_multiplayer3"),


      #2c-Vaegir Horseman
     #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul1h_blunt", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanicswordt2", "trp_saxon_horseman1_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_saxon_horseman1_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_18", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_h", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_12", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_12", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_12", "trp_saxon_horseman1_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_shorttunic2", "trp_saxon_horseman1_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pelt_coat1", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat1", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor16res", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat3", "trp_saxon_horseman1_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailshirt_3_trig", "trp_saxon_horseman1_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_saxon_horseman1_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma1", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_frisian_helm3t2", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet2", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_saxon_horseman1_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_copper_helmet", "trp_saxon_horseman1_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_saxon_horseman1_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_saxon_horseman1_multiplayer"),
     #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul1h_blunt", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanicswordt2", "trp_saxon_horseman1_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_13", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_13", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_18", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_8", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_3", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_12", "trp_saxon_horseman1_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluenorthmanshirt", "trp_saxon_horseman1_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pelt_coat1", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat1", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor16res", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat3", "trp_saxon_horseman1_multiplayer2"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailshirt_3_trig", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_saxon_horseman1_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma1", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_frisian_helm3t2", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet2", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_copper_helmet", "trp_saxon_horseman1_multiplayer2"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_saxon_horseman1_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_saxon_horseman1_multiplayer2"),
     #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul1h_blunt", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanicswordt2", "trp_saxon_horseman1_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_saxon_horseman1_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_10", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_11", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_12", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_6", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_6", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_8", "trp_saxon_horseman1_multiplayer3"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_saxon_horseman1_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pelt_coat1", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat1", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor16res", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat3", "trp_saxon_horseman1_multiplayer3"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailshirt_3_trig", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_saxon_horseman1_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma1", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_frisian_helm3t2", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet2", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_copper_helmet", "trp_saxon_horseman1_multiplayer3"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_saxon_horseman1_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_saxon_horseman1_multiplayer3"),

      #3-Khergit Warriors
      #3a-Khergit Veteran Horse Archer
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bolts", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pict_crossbow", "trp_pict_horsesquiret3_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblu", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewblk", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_pict_horsesquiret3_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pictish_waraxet2", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_pict_horsesquiret3_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_square_25", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_square_12", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_a_5", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_11", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_24", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_2", "trp_pict_horsesquiret3_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_pict_horsesquiret3_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_paintbody_two", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluepantsbody_woad05", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless8", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celtcloakedbody01", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic10", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_tunic7", "trp_pict_horsesquiret3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic7", "trp_pict_horsesquiret3_multiplayer"),

      #3a-Khergit Lancer
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_twohand_speart3", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sciansword", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_pict_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_pict_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowl_helmet_nasal", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm_3", "trp_pict_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_square_10", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_square_28", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_8", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_a_4", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_a_5", "trp_pict_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_bootstall", "trp_pict_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluepantsbody_woad04", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_richlong_tunic3", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_redpantsbody_woad11", "trp_pict_skirmishert4_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_paintbody13", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_paintbody4", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vest_red", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_redbrown", "trp_pict_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner6", "trp_pict_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_pict_skirmishert4_multiplayer"),

      #3a-picto horse
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_khergit_horse_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_a_3", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_square_7", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_2", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_1", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_12", "trp_khergit_horse_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_khergit_horse_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluepantsbody_woad02t2", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_coat6", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_paintbody4", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lorica_brightgreen", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pelt_coat1", "trp_khergit_horse_multiplayer"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ladytunicgodelic", "trp_khergit_horse_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm2engraved", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmslvtrimt3", "trp_khergit_horse_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_khergit_horse_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irish_longsword", "trp_khergit_horse_multiplayer"),

      #Nord Warriors

      #4c-Nord Archer
       #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cheap_shoes", "trp_engle_skirmishert5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_ftunic", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic12", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic2", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_shorttunic", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacketyelo", "trp_engle_skirmishert5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club3", "trp_engle_skirmishert5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblu", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newgrn", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_engle_skirmishert5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_7", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_8", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_9", "trp_engle_skirmishert5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_engle_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_englet2", "trp_engle_skirmishert5_multiplayer"),
       #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cheap_shoes", "trp_engle_skirmishert5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_tunic2", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic2", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_shorttunic", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic1", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_etunic", "trp_engle_skirmishert5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacket2t3", "trp_engle_skirmishert5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club3", "trp_engle_skirmishert5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblu", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newgrn", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_engle_skirmishert5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_9", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_10", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_10", "trp_engle_skirmishert5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_engle_skirmishert5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_englet2", "trp_engle_skirmishert5_multiplayer2"),
       #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cheap_shoes", "trp_engle_skirmishert5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic1", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_etunic", "trp_engle_skirmishert5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessex_tunic3", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_ftunic", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_tunic1", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacket2t3", "trp_engle_skirmishert5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club3", "trp_engle_skirmishert5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblu", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newgrn", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_engle_skirmishert5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_8", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_9", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_10", "trp_engle_skirmishert5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_engle_skirmishert5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_englet2", "trp_engle_skirmishert5_multiplayer3"),
       #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cheap_shoes", "trp_engle_skirmishert5_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic12", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_etunic", "trp_engle_skirmishert5_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_ftunic", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_tunic1", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacketyelo", "trp_engle_skirmishert5_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club3", "trp_engle_skirmishert5_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblu", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newgrn", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_engle_skirmishert5_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_7", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_9", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_10", "trp_engle_skirmishert5_multiplayer4"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_engle_skirmishert5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_englet2", "trp_engle_skirmishert5_multiplayer4"),

      #4a-Nord Veteran
       #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_axet2", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_englet2", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_engle_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bamburghsword2t2", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_engle_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_engle_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_greycheap", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailnoble_redclk1", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_brownclk", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_engle_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt3", "trp_engle_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bl_tunicred", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_yellowtunic1", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_engle_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_32", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_33", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_engle_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmslvtrimt3", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_cavalry_helmet", "trp_engle_skirmishert4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavalrybannert2", "trp_engle_skirmishert4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_engle_skirmishert4_multiplayer"),
       #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_axet2", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_englet2", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bamburghsword2t2", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_engle_skirmishert4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_engle_skirmishert4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_greycheap", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailnoble_redclk1", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_olive", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_engle_skirmishert4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt2", "trp_engle_skirmishert4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic13", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rednorthmanshirt", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_engle_skirmishert4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_31", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_32", "trp_engle_skirmishert4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmslvtrimt3", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_cavalry_helmet", "trp_engle_skirmishert4_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbannert2", "trp_engle_skirmishert4_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_engle_skirmishert4_multiplayer2"),
       #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_axet2", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_englet2", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bamburghsword2t2", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_engle_skirmishert4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_engle_skirmishert4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_greycheap", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailnoble_redclk1", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_gry", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_engle_skirmishert4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt2", "trp_engle_skirmishert4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic13", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_tunic2", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_engle_skirmishert4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_18", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_20", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_engle_skirmishert4_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmslvtrimt3", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_cavalry_helmet", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavalrybannert2", "trp_engle_skirmishert4_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_engle_skirmishert4_multiplayer3"),
       #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_axet2", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_englet2", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bamburghsword2t2", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_engle_skirmishert4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_engle_skirmishert4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_greycheap", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailnoble_redclk1", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_wht", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_engle_skirmishert4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt3", "trp_engle_skirmishert4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic14", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorpaddedred", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorfadedblue", "trp_engle_skirmishert4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_engle_skirmishert4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmslvtrimt3", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_cavalry_helmet", "trp_engle_skirmishert4_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbannert2", "trp_engle_skirmishert4_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_engle_skirmishert4_multiplayer4"),

#dena pirate

            (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_dena_veteran_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword2", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe4", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_battle_axe2ht2", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hvy", "trp_dena_veteran_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_dena_veteran_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_olive", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_gry", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_greycheap", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_brownclk", "trp_dena_veteran_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_farmertunic26", "trp_dena_veteran_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_plain_2", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_plain_1", "trp_dena_veteran_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar3", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar2", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_frisian_helm3t2", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar5", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar2", "trp_dena_veteran_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_veiled_helmet_plumed", "trp_dena_veteran_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_dena_veteran_multiplayer4"),


      #4b-Nord Scout
       #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesblue", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorfadedblue", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lorica_pink", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knisxclearvert3", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_18", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_1", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_shorttunic2", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluenorthmanshirt", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat7green", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacketyelo", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmengravedt2", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm2boar", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet3_t2", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_nord_scout_multiplayer"),
       #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_nord_scout_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesblue", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorfadedblue", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_nord_scout_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lorica_pink", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knisxclearvert3", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_20", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_2", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessex_tunic4", "trp_nord_scout_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat7green", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacketyelo", "trp_nord_scout_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmengravedt2", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm2boar", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet3_t2", "trp_nord_scout_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_nord_scout_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_nord_scout_multiplayer2"),
       #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_nord_scout_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesblue", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorfadedblue", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lorica_pink", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knisxclearvert3", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_40", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_20", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat7green", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacketyelo", "trp_nord_scout_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_yellowtunic1", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bl_tunicred", "trp_nord_scout_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmengravedt2", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm2boar", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet3_t2", "trp_nord_scout_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_nord_scout_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_nord_scout_multiplayer3"),
       #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_nord_scout_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesblue", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorfadedblue", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lorica_pink", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knisxclearvert3", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_20", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_42", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_3", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessex_tunic4", "trp_nord_scout_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat7green", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacketyelo", "trp_nord_scout_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bl_tunicred", "trp_nord_scout_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmengravedt2", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm2boar", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet3_t2", "trp_nord_scout_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_nord_scout_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_nord_scout_multiplayer4"),


      #5-Rhodok Warriors
      #5a-Rhodok Veteran Crossbowman
       #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_godelic_swordt2", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubsmooth", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_20", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_19", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_6", "trp_irish_horseman_multiplayer"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_red_cloak", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcapt1", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic9", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_tunic2", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celtcloakedbody06", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluepantsbody_woad04", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluepantsbody_woad04", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nobleman_outfit", "trp_irish_horseman_multiplayer"),

       #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_godelic_swordt2", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubsmooth", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_21", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_12", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_7", "trp_irish_horseman_multiplayer2"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_red_cloak", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcapt1", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_redpantsbody_woad11", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluepantsbody_woad05", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_german_tunic2", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic7", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wealthytunic5", "trp_irish_horseman_multiplayer2"),

       #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_godelic_swordt2", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubsmooth", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_22", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_14", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_7", "trp_irish_horseman_multiplayer3"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcapt1", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless6", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless8", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic5", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless3", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_byrnietunice", "trp_irish_horseman_multiplayer3"),
       #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_godelic_swordt2", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubsmooth", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_23", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_16", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_6", "trp_irish_horseman_multiplayer4"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blackhood", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcapt1", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless8", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless8", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless3", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicblue8", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaelicus_tunic27", "trp_irish_horseman_multiplayer4"),
       #5
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_godelic_swordt2", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubsmooth", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_24", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_19", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_7", "trp_irish_horseman_multiplayer5"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_red_cloak", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcapt1", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_tunic2", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless6", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_german_tunic2", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless3", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_nobleman_outfit", "trp_irish_horseman_multiplayer5"),

       #6
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_godelic_swordt2", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubsmooth", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_24", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_19", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_7", "trp_irish_horseman_multiplayer6"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hoodnewwht", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcapt1", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless8", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless8", "trp_irish_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celtcloakedbody06", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluepantsbody_woad04", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicblue8", "trp_irish_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaelicus_tunic27", "trp_irish_horseman_multiplayer6"),
       #7
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_godelic_swordt2", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubsmooth", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_20", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_19", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_6", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcapt1", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluepantsbody_woad05", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless8", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluepantsbody_woad04", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_german_tunic2", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wealthytunic5", "trp_irish_horseman_multiplayer7"),

	  #5b-Rhodok Sergeant
       #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_irish_infantryt5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_irish_infantryt5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_irish_infantryt5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_7", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_21", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_11", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_28", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_1", "trp_irish_infantryt5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_infantryt5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_infantryt5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courtly_outfit", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_linendress", "trp_irish_infantryt5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor4res", "trp_irish_infantryt5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner7", "trp_irish_infantryt5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_irish_infantryt5_multiplayer"),
#scoti

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irish_shsword", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_scoti_sergeant_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_medium_speaript3", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_spear", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_scoti_sergeant_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_scoti_sergeant_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_12", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_square_8", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_square_9", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_10", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_1", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_a", "trp_scoti_sergeant_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_scoti_sergeant_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatblue", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_german_tunic2", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic1", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless3", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicblue8", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_german_tunic5", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_scoti_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_scoti_sergeant_multiplayer"),


       #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_irish_infantryt5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_irish_infantryt5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_7", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_21", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_28", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_2", "trp_irish_infantryt5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_infantryt5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_infantryt5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelic_jacketgray", "trp_irish_infantryt5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor5res", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks5", "trp_irish_infantryt5_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner8", "trp_irish_infantryt5_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_irish_infantryt5_multiplayer2"),
       #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_irish_infantryt5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_irish_infantryt5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_8", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_9", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_11", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_28", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_3", "trp_irish_infantryt5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_infantryt5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_infantryt5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelic_jacketgray", "trp_irish_infantryt5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor6res", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks1", "trp_irish_infantryt5_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner7", "trp_irish_infantryt5_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_irish_infantryt5_multiplayer3"),
       #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_irish_infantryt5_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_irish_infantryt5_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_4", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_4", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_21", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_28", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_5", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_6", "trp_irish_infantryt5_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_infantryt5_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_infantryt5_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_german_tunic5", "trp_irish_infantryt5_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor7res", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks2", "trp_irish_infantryt5_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner8", "trp_irish_infantryt5_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_irish_infantryt5_multiplayer4"),
       #5
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_irish_infantryt5_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_irish_infantryt5_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_13", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_27", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_11", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_28", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_6", "trp_irish_infantryt5_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_infantryt5_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_infantryt5_multiplayer5"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless6", "trp_irish_infantryt5_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor7res", "trp_irish_infantryt5_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks3", "trp_irish_infantryt5_multiplayer5"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner7", "trp_irish_infantryt5_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_irish_infantryt5_multiplayer5"),
       #6
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_irish_infantryt5_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_irish_infantryt5_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_1", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_2", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_21", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_11", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_3", "trp_irish_infantryt5_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_infantryt5_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_infantryt5_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic7", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunic08", "trp_irish_infantryt5_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor8res", "trp_irish_infantryt5_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner8", "trp_irish_infantryt5_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_irish_infantryt5_multiplayer6"),
       #7
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_irish_infantryt5_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_irish_infantryt5_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_5", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_21", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_28", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_1", "trp_irish_infantryt5_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_infantryt5_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_infantryt5_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunic11", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunic05", "trp_irish_infantryt5_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks2", "trp_irish_infantryt5_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner7", "trp_irish_infantryt5_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_irish_infantryt5_multiplayer7"),

	  #5c-Rhodok Horseman
       #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_irish_horseman_multiplayer"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_cloak_hood", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelic_jacketgray", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaelicus_tunic35", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_1", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_25", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_9", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_10", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_5", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_h", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_horseman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer"),
       #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_irish_horseman_multiplayer2"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelic_jacketgrn", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaelicus_tunic27", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_10", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_2", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_6", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_h", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_irish_horseman_multiplayer2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer2"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_horseman_multiplayer2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer2"),
       #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_irish_horseman_multiplayer3"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cloaked_tunicorange", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_striped_tunic26", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_11", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_7", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_h", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_6", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_g", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_irish_horseman_multiplayer3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer3"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_horseman_multiplayer3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer3"),
       #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_irish_horseman_multiplayer4"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_green_cloak", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cloaked_tunicgreen", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaelicus_tunic27", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_12", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_7", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_h", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_g", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_irish_horseman_multiplayer4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer4"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_horseman_multiplayer4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer4"),
       #5
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_irish_horseman_multiplayer5"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunic07", "trp_irish_horseman_multiplayer5"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks1", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_7", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_16", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_i", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_6", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_g", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_5", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_irish_horseman_multiplayer5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer5"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_horseman_multiplayer5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer5"),
       #6
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_irish_horseman_multiplayer6"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_irish_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_irish_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_horseman_multiplayer6"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunic11", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_byrnietunice", "trp_irish_horseman_multiplayer6"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_6", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_16", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_g", "trp_irish_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_irish_horseman_multiplayer6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer6"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_horseman_multiplayer6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer6"),
       #7
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_irish_horseman_multiplayer7"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_green_cloak", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunic06", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks4", "trp_irish_horseman_multiplayer7"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_7", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_19", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_6", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_f", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_g", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_irish_horseman_multiplayer7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_irish_horseman_multiplayer7"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_irish_horseman_multiplayer7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_irish_horseman_multiplayer7"),

      #6-Sarranid Warriors
      #5a-Sarranid archer
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arrows1", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shortbow", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_huntingbow", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_jute_infantryt4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cheap_shoes", "trp_jute_infantryt4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblk", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblk", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakred", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_jute_infantryt4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_club3", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_6", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_7", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_8", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_9", "trp_jute_infantryt4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacketyelo", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_peasant_ftunic", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_shorttunic", "trp_jute_infantryt4_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_clubcudgel", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_jute_infantryt4_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_britonbattlet2", "trp_jute_infantryt4_multiplayer"),

	  #Sarranid footman
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_jute_footmant2_multiplayer"),
   #   (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_throwing_axes", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_jute_footmant2_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1orange", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_jute_footmant2_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet2", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar2", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblk", "trp_jute_footmant2_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_talak_seaxkni", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear1", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul1h_blunt", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironhammerlong", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tree_axe2h", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_medium_speart2", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_richswordt2", "trp_jute_footmant2_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailshirt_yellow", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat9grey", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_vest_red", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar2yellow", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluenorthmanshirt", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt1", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pelt_coat2", "trp_jute_footmant2_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_1", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_2", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_7", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_16", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_19", "trp_jute_footmant2_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner5", "trp_jute_footmant2_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_jute_footmant2_multiplayer"),

	  #frankish
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_throwing_axes", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_axes", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_frankish_footman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_frankish_footman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmb1", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlatet2", "trp_frankish_footman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spathaswordt2", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_britonbattlet2", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_longfrankisht3", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironhammerlong", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_frankish_footman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellarred1", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor7res", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lorica_eggwht", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_frankish_footman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_plain_1", "trp_frankish_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_10", "trp_frankish_footman_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_frankish_footman_multiplayer"),


	  #Sarranid mamluke
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_axes", "trp_jute_skirmishert5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_jute_skirmishert5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor6res", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailnoble_ltbrwnclk", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rednorthmanshirt", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorfadedblue", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat2", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt3", "trp_jute_skirmishert5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblk", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_cavalry_helmet", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet3_t2", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_jute_skirmishert5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironhammerlong", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_longfrankisht3", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ornate_seaxt3", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_richswordt2", "trp_jute_skirmishert5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_jute_skirmishert5_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_6", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_6", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_7", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_10", "trp_jute_skirmishert5_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_8", "trp_jute_skirmishert5_multiplayer"),
#chief capitan#capitan juto
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_axes", "trp_capitan1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_capitan1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor6res", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailnoble_ltbrwnclk", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rednorthmanshirt", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorfadedblue", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat2", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt3", "trp_capitan1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblk", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_cavalry_helmet", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet3_t2", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironhammerlong", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_longfrankisht3", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ornate_seaxt3", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_richswordt2", "trp_capitan1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_capitan1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_6", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_6", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_7", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_10", "trp_capitan1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan1"),
#mercenario
            (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_tropa1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1orange", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_tropa1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet2", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar2", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblk", "trp_tropa1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_talak_seaxkni", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear1", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul1h_blunt", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironhammerlong", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tree_axe2h", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_medium_speart2", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_richswordt2", "trp_tropa1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailshirt_yellow", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat9grey", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_vest_red", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellar2yellow", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluenorthmanshirt", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt1", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pelt_coat2", "trp_tropa1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_1", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_2", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_7", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_16", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_19", "trp_tropa1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner5", "trp_tropa1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa1"),
#franco
            (call_script, "script_multiplayer_set_item_available_for_troop", "itm_light_throwing_axes", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_axes", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_mercenario1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_mercenario1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmb1", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlatet2", "trp_mercenario1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spathaswordt2", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_britonbattlet2", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_longfrankisht3", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironhammerlong", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_mercenario1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lamellarred1", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor7res", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lorica_eggwht", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_mercenario1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_plain_2", "trp_mercenario1"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_10", "trp_mercenario1"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_mercenario1"),
#sajones      #lord
            (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul1h_blunt", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanicswordt2", "trp_capitan2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_18", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_h", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_12", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_12", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_12", "trp_capitan2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_shorttunic2", "trp_capitan2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pelt_coat1", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat1", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor16res", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat3", "trp_capitan2"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailshirt_3_trig", "trp_capitan2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_capitan2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma1", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_frisian_helm3t2", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet2", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_copper_helmet", "trp_capitan2"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_capitan2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan2"),
     #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul1h_blunt", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanicswordt2", "trp_capitan3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_13", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_13", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_18", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_8", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_3", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_12", "trp_capitan3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluenorthmanshirt", "trp_capitan3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pelt_coat1", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat1", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor16res", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat3", "trp_capitan3"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailshirt_3_trig", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_capitan3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma1", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_frisian_helm3t2", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet2", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_copper_helmet", "trp_capitan3"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan3"),
     #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul1h_blunt", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanicswordt2", "trp_capitan5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_10", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_11", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_12", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_6", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_6", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_8", "trp_capitan5"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_capitan5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pelt_coat1", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat1", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor16res", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat3", "trp_capitan5"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailshirt_3_trig", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_capitan5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma1", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_frisian_helm3t2", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet2", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_copper_helmet", "trp_capitan5"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan5"),


      #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe4", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2_crude", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_tropa2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hvy", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jute_richsword", "trp_tropa2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_2", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_tropa2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_7", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_tropa2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_32", "trp_tropa2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_tropa2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluenorthmanshirt", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rednorthmanshirt", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_vest_blue", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat2", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor6res", "trp_tropa2"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_brown", "trp_tropa2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_tropa2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblk", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_tropa2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner1", "trp_tropa2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa2"),
      #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe4", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2_crude", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_tropa3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hvy", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jute_richsword", "trp_tropa3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_3", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_10", "trp_tropa3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_10", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_h", "trp_tropa3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_1", "trp_tropa3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_tropa3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic12", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bl_tunicred", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat5t3", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_vest_red", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor6res", "trp_tropa3"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_brown", "trp_tropa3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_tropa3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblk", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner1", "trp_tropa3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa3"),
      #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe4", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2_crude", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_tropa5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hvy", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jute_richsword", "trp_tropa5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_3", "trp_tropa5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_10", "trp_tropa5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_5", "trp_tropa5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_tropa5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_shorttunic", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic1", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat1tier2", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_vest_green", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor6res", "trp_tropa5"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_brown", "trp_tropa5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_tropa5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap_newblk", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jutehelmt3", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner1", "trp_tropa5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa5"),
#frisian
            (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_maul1h_blunt", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2_crude", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_commonhammer_blunt", "trp_mercenario3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear1", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword4t2", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_mercenario3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_mercenario3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_mercenario3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_wht", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessex_tunic4", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_shorttunic2", "trp_mercenario3"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_mercenario3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesblue", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_mercenario3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar5", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar3", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_frisian_helm1", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_frisian_helm3t2", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_mercenario3"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_mercenario3"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_mercenario3"),
#dena capitan
                  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_mercenario2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sword2", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe4", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_battle_axe2ht2", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hvy", "trp_mercenario2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_mercenario2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_olive", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_gry", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_greycheap", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_brownclk", "trp_mercenario2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_farmertunic26", "trp_mercenario2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_plain_1", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_plain_2", "trp_mercenario2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar3", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar2", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_frisian_helm3t2", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar5", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_helmboar2", "trp_mercenario2"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_veiled_helmet_plumed", "trp_mercenario2"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_mercenario2"),
       #1 capitan anglo       #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesblue", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_capitan4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorfadedblue", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_capitan4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lorica_pink", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knisxclearvert3", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_18", "trp_capitan4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_1", "trp_capitan4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_shorttunic2", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluenorthmanshirt", "trp_capitan4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat7green", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacketyelo", "trp_capitan4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmengravedt2", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm2boar", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet3_t2", "trp_capitan4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_capitan4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan4"),
       #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesblue", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorfadedblue", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_capitan9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lorica_pink", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knisxclearvert3", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_20", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_2", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mercia_tunicgrn", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessex_tunic4", "trp_capitan9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat7green", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacketyelo", "trp_capitan9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmengravedt2", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm2boar", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet3_t2", "trp_capitan9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_capitan9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan9"),
       #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesblue", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorfadedblue", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lorica_pink", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knisxclearvert3", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_40", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_20", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat7green", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacketyelo", "trp_capitan13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_yellowtunic1", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bl_tunicred", "trp_capitan13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmengravedt2", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm2boar", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet3_t2", "trp_capitan13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_capitan13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan13"),
       #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesblue", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorfadedblue", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lorica_pink", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knisxclearvert3", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_20", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_42", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_3", "trp_nord_scout_multiplayer"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessex_tunic4", "trp_capitan14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rawhide_coat7green", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_merch_furjacketyelo", "trp_capitan14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bl_tunicred", "trp_capitan14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmengravedt2", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm1boar", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dena_elite_helm2boar", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet1", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hornhelmet3_t2", "trp_capitan14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearwarlong", "trp_capitan14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan14"),
       #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_axet2", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_englet2", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_tropa4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bamburghsword2t2", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_tropa4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_greycheap", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailnoble_redclk1", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_brownclk", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_tropa4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt3", "trp_tropa4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bl_tunicred", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_yellowtunic1", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorgreen", "trp_tropa4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_32", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_33", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_tropa4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmslvtrimt3", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_cavalry_helmet", "trp_tropa4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavalrybannert2", "trp_tropa4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa4"),
       #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_axet2", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_englet2", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bamburghsword2t2", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_tropa9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_greycheap", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailnoble_redclk1", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_olive", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_tropa9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt2", "trp_tropa9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic13", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rednorthmanshirt", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat3", "trp_tropa9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_31", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_32", "trp_tropa9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmslvtrimt3", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_cavalry_helmet", "trp_tropa9"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbannert2", "trp_tropa9"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa9"),
       #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_axet2", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_englet2", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bamburghsword2t2", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_tropa13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_greycheap", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailnoble_redclk1", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_gry", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_tropa13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt2", "trp_tropa13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic13", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_tunic2", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vae_thickcoat2", "trp_tropa13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_saxon_18", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_20", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_tropa13"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmslvtrimt3", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_cavalry_helmet", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavalrybannert2", "trp_tropa13"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa13"),
       #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angons", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angonst2", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_seaxt3", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxon_axet2", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_englet2", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlight", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_germanic_axelongt2", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_langseaxt2", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angleswordt2", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bamburghsword2t2", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_greaves1", "trp_tropa14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_greycheap", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailnoble_redclk1", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_wht", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_tropa14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt3", "trp_tropa14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic14", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorpaddedred", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_jack_armorfadedblue", "trp_tropa14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_9", "trp_tropa14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_woolencap", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_angloblackbrownhelm", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmslvtrimt3", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_tan", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_khergit_cavalry_helmet", "trp_tropa14"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbannert2", "trp_tropa14"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa14"),
#capitan irlandes             #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_capitan17"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_cloak_hood", "trp_capitan17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_capitan17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_capitan17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelic_jacketgray", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaelicus_tunic35", "trp_capitan17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_1", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_small_25", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_9", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_10", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_5", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_h", "trp_capitan17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_capitan17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_capitan17"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan17"),
       #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_capitan19"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_capitan19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_capitan19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_capitan19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelic_jacketgrn", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaelicus_tunic27", "trp_capitan19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_10", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_2", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_6", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_h", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_capitan19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_capitan19"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan19"),
       #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_capitan27"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_capitan27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_capitan27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_capitan27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cloaked_tunicorange", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_striped_tunic26", "trp_capitan27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_11", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_7", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_h", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_6", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_g", "trp_capitan27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_capitan27"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan27"),
       #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_capitan28"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_green_cloak", "trp_capitan28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_capitan28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_capitan28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cloaked_tunicgreen", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_vaelicus_tunic27", "trp_capitan28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_12", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_7", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_h", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_g", "trp_capitan28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_capitan28"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan28"),
       #5
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_capitan29"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_capitan29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_capitan29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_capitan29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunic07", "trp_capitan29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks1", "trp_capitan29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_7", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_16", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_i", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_6", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_g", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_5", "trp_capitan29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_capitan29"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan29"),
       #6
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_capitan30"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_celta_cloak1", "trp_capitan30"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_capitan30"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_capitan30"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunic11", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_byrnietunice", "trp_capitan30"),


      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_6", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_16", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_g", "trp_capitan30"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_capitan30"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan30"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan30"),
       #7
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearlong", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_helm_leathert2", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelmgerm_trim", "trp_capitan31"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_green_cloak", "trp_capitan31"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wooden_javelins", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_espada_kirkburn", "trp_capitan31"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronzegreen", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vestgrey", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessgrn", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_capitan31"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunic06", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks4", "trp_capitan31"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_7", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_19", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_6", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_f", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_g", "trp_capitan31"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton2ht3", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_capitan31"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan31"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan31"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan31"),
#soldados irlandeses             #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_tropa17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_tropa17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_7", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_21", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_11", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_28", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_1", "trp_tropa17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_tropa17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_courtly_outfit", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_blue_linendress", "trp_tropa17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor4res", "trp_tropa17"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner7", "trp_tropa17"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa17"),
#scoti
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_darts", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irish_shsword", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_mercenario5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_medium_speaript3", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_spear", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt2", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_mercenario5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bronzebowlhelmet", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ironceltbowlhelmet", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_mercenario5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_12", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_square_8", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_square_9", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_10", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_c_1", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_a", "trp_mercenario5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_mercenario5"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatblue", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_german_tunic2", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic1", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless3", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicblue8", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_german_tunic5", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_mercenario5"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_mercenario5"),
       #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_tropa19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_7", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_21", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_28", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_2", "trp_tropa19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_tropa19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelic_jacketgray", "trp_tropa19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor5res", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks5", "trp_tropa19"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner8", "trp_tropa19"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa19"),
       #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_tropa27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_8", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_9", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_11", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_28", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_3", "trp_tropa27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_tropa27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelic_jacketgray", "trp_tropa27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor6res", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks1", "trp_tropa27"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner7", "trp_tropa27"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa27"),
      #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_tropa28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_4", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_4", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_21", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_28", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_5", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_6", "trp_tropa28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_tropa28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_german_tunic5", "trp_tropa28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor7res", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks2", "trp_tropa28"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner8", "trp_tropa28"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa28"),
       #5
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_tropa29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_13", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_27", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_11", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_28", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_6", "trp_tropa29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_tropa29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_tunicsleeveless6", "trp_tropa29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor7res", "trp_tropa29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks3", "trp_tropa29"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner7", "trp_tropa29"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa29"),
       #6
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa30"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_tropa30"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_1", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_2", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_21", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_11", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_3", "trp_tropa30"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_tropa30"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa30"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic7", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunic08", "trp_tropa30"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblearmor8res", "trp_tropa30"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner8", "trp_tropa30"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa30"),
       #7
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe_1hlongt2", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pommel_swordt3", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa32"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_common_hood", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_tropa32"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_5", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_b_21", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_rectangle_28", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_1", "trp_tropa32"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_tropa32"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_sleevelessbrn", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_fadedgrn", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa32"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunic11", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bltunic05", "trp_tropa32"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gatheredcloaks2", "trp_tropa32"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner7", "trp_tropa32"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa32"),
#picto
            (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_lightgael", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_warspear_godelict3", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_twohand_speart3", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sciansword", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_gaelicsword1", "trp_tropa20"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa20"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt1", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowl_helmet_nasal", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm3t2", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm_3", "trp_tropa20"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_square_10", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_square_28", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_8", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_a_4", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_a_5", "trp_tropa20"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_bootstall", "trp_tropa20"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluepantsbody_woad04", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_richlong_tunic3", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_redpantsbody_woad11", "trp_tropa20"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_paintbody13", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_paintbody4", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_vest_red", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_redbrown", "trp_tropa20"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner6", "trp_tropa20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa20"),

      #3a-picto capitan
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan20"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_pict_a_3", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_square_7", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_2", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_1", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_7", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_caledonian_12", "trp_capitan20"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan20"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bluepantsbody_woad02t2", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hide_coat6", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_war_paintbody4", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lorica_brightgreen", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_pelt_coat1", "trp_capitan20"),
	  (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ladytunicgodelic", "trp_capitan20"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_skullcap_reinforcedt2", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mierce_helmt3", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_szpadelhelm2engraved", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helmslvtrimt3", "trp_capitan20"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordbone", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianswordbone", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_axe2", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irish_longsword", "trp_capitan20"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan20"),
#capitan briton             #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan6"),

#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan6"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_1", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_2", "trp_capitan6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_capitan6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan6"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan6"),
       #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan7"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_3", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_4", "trp_capitan7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_capitan7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan7"),
       #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan8"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_5", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_6", "trp_capitan8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_capitan8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan8"),
       #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan10"),

#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_7", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_8", "trp_capitan10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_capitan10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan10"),
       #5
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan11"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_8", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_11", "trp_capitan11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan11"),
       #6
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan12"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_1", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_11", "trp_capitan12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_capitan12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan12"),
       #7
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan15"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_2", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_8", "trp_capitan15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_capitan15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan15"),
       #8
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan16"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan16"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan16"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_3", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_8", "trp_capitan16"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan16"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_capitan16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan16"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan16"),
       #9
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan18"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_briton_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan18"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan18"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_5", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_7", "trp_capitan18"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan18"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_capitan18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan18"),

       #10
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan21"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan21"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan21"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_4", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_7", "trp_capitan21"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan21"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_capitan21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan21"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan21"),
       #11
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan22"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan22"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan22"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_5", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_8", "trp_capitan22"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan22"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan22"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan22"),
       #12
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan23"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan23"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan23"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_3", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_8", "trp_capitan23"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan23"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan23"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan23"),
       #13
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan24"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan24"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan24"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_4", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_11", "trp_capitan24"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan24"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan24"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan24"),
       #14
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan25"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan25"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan25"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_1", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_5", "trp_capitan25"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coattan", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_brown_armor", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan25"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_helm_grey", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_yellow", "trp_capitan25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan25"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan25"),
       #15
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_cavaljavelins", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_briton_longt2", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_saxonswordt2", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_longspeart3", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_capitan26"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rich_spathaswordt2", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_bronze_blueorange", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_goatist", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwhite", "trp_capitan26"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma_ornate", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_dux_ridgehelm", "trp_capitan26"),
#-
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_gaelic_j", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_4", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_briton_8", "trp_capitan26"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatbrown", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrniegreen", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailbyrnieyelo", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ankleboots", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shoesorange", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_splinted_leather_greaves", "trp_capitan26"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_irishcloak", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_rathos_bowlhelmet", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_capitan26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_capitan26"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_capitan26"),
#soldado briton            #1
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa6"),
#
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatblue", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa6"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_22", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_1", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_17", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt2", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_tropa6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_tropa6"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa6"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa6"),
###
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_tropa6"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa6"),

      #2
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa7"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_8", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_4", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt3", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_tropa7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_tropa7"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa7"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_tropa7"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa7"),

      #3
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa8"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_5", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_6", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt4", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_tropa8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakred", "trp_tropa8"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa8"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_tropa8"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa8"),

      #4
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatblue", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa10"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_22", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_1", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_2", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt2", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_tropa10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_tropa10"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa10"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_tropa10"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa10"),

      #5
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa11"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_8", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_4", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt3", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_tropa11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_tropa11"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa11"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_tropa11"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa11"),

      #6
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa12"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_5", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_6", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt4", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtylw", "trp_tropa12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_tropa12"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa12"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_tropa12"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa12"),

      #7
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatblue", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa15"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_12", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_10", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt4", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_tropa15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_tropa15"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa15"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_tropa15"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa15"),

      #8
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa16"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa16"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa16"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa16"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_16", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_17", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa16"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt2", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_tropa16"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakred", "trp_tropa16"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa16"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa16"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_tropa16"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa16"),
      #9
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa18"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa18"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa18"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa18"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_22", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_1", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_17", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa18"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt3", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_tropa18"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_tropa18"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa18"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa18"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_tropa18"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa18"),

      #10
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa21"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa21"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa21"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa21"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_2", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_16", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa21"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noblemanshirt2", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_tropa21"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_tropa21"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa21"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa21"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_tropa21"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa21"),

      #11
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa22"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa22"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa22"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatblue", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa22"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_24", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_8", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_10", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_16", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa22"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_tropa22"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakred", "trp_tropa22"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa22"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa22"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_tropa22"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa22"),
      #12
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa23"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa23"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa23"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa23"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_29", "trp_tropa23"),
       (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_4", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_17", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa23"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtylw", "trp_tropa23"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakltblue", "trp_tropa23"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa23"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa23"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_tropa23"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa23"),
      #13
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa24"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa24"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_briton_skirmishert3_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa24"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatblue", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa24"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_23", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_4", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_10", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa24"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtaqua", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_tropa24"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbeige", "trp_tropa24"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa24"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa24"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_tropa24"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa24"),
      #14
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa25"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa25"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa25"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa25"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_28", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_4", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_16", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa25"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_tropa25"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakbrown", "trp_tropa25"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa25"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa25"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spearbanner4", "trp_tropa25"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa25"),
      #15
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonmedt2", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_britonlight", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_knife1", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scianshswordt1", "trp_tropa26"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_tropa26"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_throwing_spear", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_lang_knifet2", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_tropa26"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_white_armor", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_blk", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mail_furredt2", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_goatist_tuniccoat", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_linen_coatwcloak", "trp_tropa26"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_22", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_viking_26", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_5", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_round_6", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_celtic_adorno_8", "trp_tropa26"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtgrey", "trp_tropa26"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_plaincloakred", "trp_tropa26"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_helm", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_arming_cap", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_roman_helmlate", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_romanelitehelmt3", "trp_tropa26"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1blue", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2grey", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes1green", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2green", "trp_tropa26"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_wessexbanner9", "trp_tropa26"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_tropa26"),
#mercenario cantabro
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_javelins", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_hasta", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spathaswordt2", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_hunting_knife", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spear_blade2t2", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_noble_shswordt2", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_britonswordt2", "trp_mercenario4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunicwhite", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ptunic3", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shirtblue", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_briton_tunic2", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_scale_armor1", "trp_mercenario4"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_banner_heavy_3", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_cantabro_1", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_cantabro_2", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_cantabro_3", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_cantabro_4", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_cantabro_5", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_cantabro_6", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shield_cantabro_7", "trp_mercenario4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_ltbrown", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_mailtunic_redclk", "trp_mercenario4"),
#---
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_spangenhelma1", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bowlhelmet", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_captainhelm", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leathercap1", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bandanawht", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bandanablack", "trp_mercenario4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_shoes", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_shoes2bare", "trp_mercenario4"),

      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_leather_gloves1", "trp_mercenario4"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_horn_multiplayer", "trp_mercenario4"),
#chief capitan tropas
    ]),
]
