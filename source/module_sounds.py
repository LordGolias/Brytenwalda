from header_sounds import *

sounds = [
#chief cambiado entero
 ("click", sf_2d|sf_vol_3,["click_01.wav"]),
 ("tutorial_1", sf_2d|sf_vol_7,["tutorial_1.wav"]),
 ("tutorial_2", sf_2d|sf_vol_7,["tutorial_2.wav"]),
 ("gong", sf_2d|sf_priority_9|sf_vol_9, ["cymbal_01.wav"]),
 ("quest_taken", sf_2d|sf_priority_9|sf_vol_10, ["get_quest_01.wav"]),
 ("quest_completed", sf_2d|sf_priority_9|sf_vol_8, ["quest_completed.wav"]),
 ("quest_succeeded", sf_2d|sf_priority_9|sf_vol_6, ["quest_succeeded.wav"]),
 ("quest_concluded", sf_2d|sf_priority_9|sf_vol_7, ["quest_concluded.wav"]),
 ("quest_failed", sf_2d|sf_priority_9|sf_vol_7, ["quest_failed.wav"]),
 ("quest_cancelled", sf_2d|sf_priority_9|sf_vol_7, ["quest_cancelled.wav"]),
 ("rain",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["rain_1.wav"]),
 ("money_received",sf_2d|sf_priority_10|sf_vol_4, ["coins_dropped_1.wav"]),
 ("money_paid",sf_2d|sf_priority_10|sf_vol_10, ["coins_dropped_2.wav"]),
 ("sword_clash_1", sf_priority_5|sf_vol_8,["sword_clank_metal_09.wav","sword_clank_metal_09b.wav","sword_clank_metal_10.wav","sword_clank_metal_10b.wav","sword_clank_metal_12.wav","sword_clank_metal_12b.wav","sword_clank_metal_13.wav","sword_clank_metal_13b.wav"]),
 ("sword_clash_2", sf_priority_5|sf_vol_9,["s_swordClash2.wav"]),
 ("sword_clash_3", sf_priority_5|sf_vol_9,["s_swordClash3.wav"]),
 ("sword_swing", sf_vol_8|sf_priority_2,["weapon_swing_01.wav","weapon_swing_02.wav","weapon_swing_03.wav","weapon_swing_04.wav","weapon_swing_05.wav"]),
 ("footstep_grass", sf_vol_4|sf_priority_1,["footstep_grass_light_01.wav","footstep_grass_light_02.wav","footstep_grass_light_03.wav","footstep_grass_light_04.wav","footstep_grass_light_05.wav","footstep_grass_light_06.wav","footstep_grass_light_07.wav","footstep_grass_light_08.wav","footstep_grass_light_09.wav","footstep_grass_light_10.wav","footstep_grass_light_11.wav","footstep_grass_light_12.wav","footstep_grass_light_13.wav","footstep_grass_light_14.wav","footstep_grass_light_15.wav"]),
 ("footstep_wood", sf_vol_5|sf_priority_1,["footstep_wood_light_01.wav","footstep_wood_light_02.wav","footstep_wood_light_03.wav","footstep_wood_light_04.wav","footstep_wood_light_05.wav","footstep_wood_light_06.wav","footstep_wood_light_07.wav","footstep_wood_light_08.wav","footstep_wood_light_09.wav","footstep_wood_light_10.wav"]),
# ("footstep_wood", sf_vol_3|sf_priority_1,["footstep_stone_1.wav","footstep_stone_3.wav","footstep_stone_4.wav"]),
 ("footstep_water", sf_vol_7|sf_priority_3,["footstep_water_01.wav","footstep_water_02.wav","footstep_water_03.wav","footstep_water_04.wav","footstep_water_05.wav","footstep_water_06.wav","footstep_water_07.wav","footstep_water_08.wav","footstep_water_09.wav","footstep_water_10.wav"]),
 ("footstep_horse",sf_priority_3|sf_vol_8, ["footstep_horse_5.wav","footstep_horse_2.wav","footstep_horse_3.wav","footstep_horse_4.wav"]),
# ("footstep_horse",0, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
 ("footstep_horse_1b",sf_priority_3|sf_vol_8, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
 ("footstep_horse_1f",sf_priority_3|sf_vol_8, ["s_footstep_horse_2b.wav","s_footstep_horse_2f.wav","s_footstep_horse_3b.wav","s_footstep_horse_3f.wav"]),
# ("footstep_horse_1f",sf_priority_3|sf_vol_15, ["footstep_horse_5.wav","footstep_horse_2.wav","footstep_horse_3.wav","footstep_horse_4.wav"]),
 ("footstep_horse_2b",sf_priority_3|sf_vol_8, ["s_footstep_horse_2b.wav"]),
 ("footstep_horse_2f",sf_priority_3|sf_vol_8, ["s_footstep_horse_2f.wav"]),
 ("footstep_horse_3b",sf_priority_3|sf_vol_8, ["s_footstep_horse_3b.wav"]),
 ("footstep_horse_3f",sf_priority_3|sf_vol_8, ["s_footstep_horse_3f.wav"]),
 ("footstep_horse_4b",sf_priority_3|sf_vol_8, ["s_footstep_horse_4b.wav"]),
 ("footstep_horse_4f",sf_priority_3|sf_vol_8, ["s_footstep_horse_4f.wav"]),
 ("footstep_horse_5b",sf_priority_3|sf_vol_8, ["s_footstep_horse_5b.wav"]),
 ("footstep_horse_5f",sf_priority_3|sf_vol_8, ["s_footstep_horse_5f.wav"]),
 ("jump_begin", sf_vol_6|sf_priority_9,["jump_light_b_01.wav","jump_light_b_02.wav","jump_light_b_03.wav"]),
 ("jump_end", sf_vol_5|sf_priority_9,["jump_light_e_01.wav","jump_light_e_02.wav"]),
 ("jump_begin_water", sf_vol_3|sf_priority_9,["water_jump_01.wav","water_jump_02.wav","water_jump_03.wav"]),
 ("jump_end_water", sf_vol_3|sf_priority_9,["water_splash_01.wav","water_splash_02.wav","water_splash_03.wav","water_splash_04.wav","water_splash_05.wav"]),
 ("horse_jump_begin", sf_vol_6|sf_priority_9,["horse_jump_b_01.wav","horse_jump_b_02.wav"]),
 ("horse_jump_end", sf_vol_7|sf_priority_9,["horse_jump_e_01.wav","horse_jump_e_02.wav"]),
 ("horse_jump_begin_water", sf_vol_10|sf_priority_9,["water_jump_large_01.wav","water_jump_large_02.wav","water_jump_large_03.wav"]),
 ("horse_jump_end_water", sf_vol_10|sf_priority_9,["water_splash_large_01.wav","water_splash_large_02.wav","water_splash_large_03.wav","water_splash_large_04.wav","water_splash_large_05.wav"]),

 ("release_bow",sf_vol_4, ["bow_shoot_01.wav","bow_shoot_02.wav","bow_shoot_03.wav","bow_shoot_04.wav","bow_shoot_05.wav","bow_shoot_06.wav","bow_shoot_07.wav","bow_shoot_08.wav","bow_shoot_09.wav","bow_shoot_10.wav"]),
 ("release_crossbow",sf_vol_7, ["crossbow_shoot_01.wav","crossbow_shoot_02.wav","crossbow_shoot_03.wav","crossbow_shoot_04.wav","crossbow_shoot_05.wav","crossbow_shoot_06.wav"]),
 ("throw_javelin",sf_vol_5, ["throw_javelin_2.wav","throw_javelin_01.wav","throw_javelin_02.wav","throw_javelin_03.wav"]),
 ("throw_axe",sf_vol_7, ["throw_axe_1.wav"]),
 ("throw_knife",sf_vol_5, ["throw_knife_01.wav","throw_knife_02.wav","throw_knife_03.wav","throw_knife_04.wav"]),
 ("throw_stone",sf_vol_5, ["throw_stone_01.wav","throw_stone_02.wav","throw_stone_03.wav"]),

 ("reload_crossbow",sf_vol_3, ["pull_crossbow_string_01.wav","pull_crossbow_string_02.wav","pull_crossbow_string_03.wav","pull_crossbow_string_04.wav","pull_crossbow_string_05.wav"]),
 ("reload_crossbow_continue",sf_vol_6, ["put_back_dagger.wav"]),
 ("pull_bow",sf_vol_5, ["pull_bow_string_01.wav","pull_bow_string_02.wav","pull_bow_string_03.wav","pull_bow_string_04.wav","pull_bow_string_05.wav"]),
 ("pull_arrow",sf_vol_5, ["draw_arrow_01.wav","draw_arrow_02.wav","draw_arrow_03.wav"]),

 ("arrow_pass_by",sf_priority_7, ["arrow_pass_01.wav","arrow_pass_02.wav","arrow_pass_03.wav","arrow_pass_04.wav","arrow_pass_05.wav","arrow_pass_06.wav","arrow_pass_07.wav","arrow_pass_08.wav","arrow_pass_09.wav","arrow_pass_10.wav"]),
 ("bolt_pass_by",sf_priority_7, ["bolt_pass_01.wav","bolt_pass_02.wav","bolt_pass_03.wav","bolt_pass_04.wav","bolt_pass_05.wav","bolt_pass_06.wav","bolt_pass_07.wav","bolt_pass_08.wav"]),
 ("javelin_pass_by",sf_priority_7, ["javelin_pass_by_1.wav","javelin_pass_by_2.wav"]),
 ("stone_pass_by",sf_vol_9|sf_priority_7, ["stone_pass_01.wav","stone_pass_02.wav","stone_pass_03.wav"]),
 ("axe_pass_by",sf_priority_7, ["axe_pass_by_1.wav"]),
 ("knife_pass_by",sf_priority_7, ["knife_pass_01.wav","knife_pass_02.wav","knife_pass_03.wav","knife_pass_04.wav"]),
 ("bullet_pass_by",sf_priority_7, ["bullet_pass_01.wav","bullet_pass_02.wav","bullet_pass_03.wav","bullet_pass_04.wav","bullet_pass_05.wav","bullet_pass_06.wav","bullet_pass_07.wav","bullet_pass_08.wav","bullet_pass_09.wav","bullet_pass_10.wav","bullet_pass_11.wav","bullet_pass_12.wav"]),
 
 ("incoming_arrow_hit_ground",sf_priority_7|sf_vol_7, ["arrow_ground_01.wav","arrow_ground_02.wav","arrow_ground_03.wav","arrow_ground_04.wav","arrow_ground_05.wav","arrow_ground_06.wav","arrow_ground_07.wav","arrow_ground_08.wav"]),
 ("incoming_bolt_hit_ground",sf_priority_7|sf_vol_7, ["bolt_ground_01.wav","bolt_ground_02.wav","bolt_ground_03.wav","bolt_ground_04.wav","bolt_ground_05.wav","bolt_ground_06.wav","bolt_ground_07.wav","bolt_ground_08.wav"]),
 ("incoming_javelin_hit_ground",sf_priority_7|sf_vol_7, ["javelin_ground_01.wav","javelin_ground_02.wav","javelin_ground_03.wav"]),
 ("incoming_stone_hit_ground",sf_priority_7|sf_vol_7, ["stone_ground_01.wav","stone_ground_02.wav","stone_ground_03.wav"]),
 ("incoming_axe_hit_ground",sf_priority_7|sf_vol_7, ["axe_ground_01.wav","axe_ground_02.wav","axe_ground_03.wav"]),
 ("incoming_knife_hit_ground",sf_priority_7|sf_vol_7, ["knife_ground_01.wav","knife_ground_02.wav","knife_ground_03.wav"]),
 ("incoming_bullet_hit_ground",sf_priority_7|sf_vol_7, ["bullet_ric_01.wav","bullet_ric_02.wav","bullet_ric_03.wav","bullet_ric_04.wav","bullet_ric_05.wav","bullet_ric_06.wav","bullet_ric_07.wav","bullet_ric_08.wav"]),

 ("outgoing_arrow_hit_ground",sf_priority_7|sf_vol_7, ["arrow_ground_01.wav","arrow_ground_02.wav","arrow_ground_03.wav","arrow_ground_04.wav","arrow_ground_05.wav","arrow_ground_06.wav","arrow_ground_07.wav","arrow_ground_08.wav"]),
 ("outgoing_bolt_hit_ground",sf_priority_7|sf_vol_7,  ["bolt_ground_01.wav","bolt_ground_02.wav","bolt_ground_03.wav","bolt_ground_04.wav","bolt_ground_05.wav","bolt_ground_06.wav","bolt_ground_07.wav","bolt_ground_08.wav"]),
 ("outgoing_javelin_hit_ground",sf_priority_7|sf_vol_10, ["javelin_ground_01.wav","javelin_ground_02.wav","javelin_ground_03.wav"]),
 ("outgoing_stone_hit_ground",sf_priority_7|sf_vol_7, ["stone_ground_01.wav","stone_ground_02.wav","stone_ground_03.wav"]),
 ("outgoing_axe_hit_ground",sf_priority_7|sf_vol_7, ["axe_ground_01.wav","axe_ground_02.wav","axe_ground_03.wav"]),
 ("outgoing_knife_hit_ground",sf_priority_7|sf_vol_7, ["knife_ground_01.wav","knife_ground_02.wav","knife_ground_03.wav"]),
 ("outgoing_bullet_hit_ground",sf_priority_7|sf_vol_7, ["bullet_ric_01.wav","bullet_ric_02.wav","bullet_ric_03.wav","bullet_ric_04.wav","bullet_ric_05.wav","bullet_ric_06.wav","bullet_ric_07.wav","bullet_ric_08.wav"]),


 ("draw_sword",sf_priority_2|sf_vol_4, ["draw_sword_02.wav","draw_sword_03.wav"]),
 ("put_back_sword",sf_priority_1|sf_vol_4, ["put_away_sword_01.wav"]),
 ("draw_greatsword",sf_priority_2|sf_vol_4, ["draw_greatsword_01.wav","draw_greatsword_03.wav"]),
 ("put_back_greatsword",sf_priority_1|sf_vol_4, ["put_away_greatsword_01.wav"]),
 ("draw_axe",sf_priority_2|sf_vol_4, ["draw_axe_01.wav","draw_axe_02.wav"]),
 ("put_back_axe",sf_priority_1|sf_vol_4, ["put_away_axe_01.wav"]),
 ("draw_greataxe",sf_priority_2|sf_vol_4, ["draw_greataxe_01.wav","draw_greataxe_02.wav"]),
 ("put_back_greataxe",sf_priority_1|sf_vol_4, ["put_away_greataxe_01.wav"]),
 ("draw_spear",sf_priority_2|sf_vol_4, ["draw_spear_01.wav","draw_spear_02.wav"]),
 ("put_back_spear",sf_priority_1|sf_vol_4, ["put_away_spear_01.wav"]),
 ("draw_crossbow",sf_priority_2|sf_vol_4, ["draw_crossbow_01.wav","draw_crossbow_02.wav"]),
 ("put_back_crossbow",sf_priority_1|sf_vol_4, ["put_away_crossbow_01.wav"]),
 ("draw_revolver",sf_priority_2|sf_vol_4, ["draw_from_holster.wav"]),
 ("put_back_revolver",sf_priority_1|sf_vol_4, ["put_back_to_holster.wav"]),
 ("draw_dagger",sf_priority_2|sf_vol_4, ["draw_dagger_01.wav","draw_dagger_02.wav"]),
 ("put_back_dagger",sf_priority_1|sf_vol_4, ["put_away_dagger_01.wav"]),
 ("draw_bow",sf_priority_2|sf_vol_4, ["draw_bow_01.wav","draw_bow_02.wav"]),
 ("put_back_bow",sf_priority_1|sf_vol_4, ["put_away_bow_01.wav"]),
 ("draw_shield",sf_priority_2|sf_vol_4, ["draw_shield_01.wav","draw_shield_02.wav"]),
 ("put_back_shield",sf_priority_1|sf_vol_4, ["put_away_shield_01.wav"]),
 ("draw_other",sf_priority_2|sf_vol_4, ["draw_other.wav"]),
 ("put_back_other",sf_priority_1|sf_vol_4, ["draw_other2.wav"]),

 ("body_fall_small",sf_priority_5|sf_vol_9, ["body_fall_small_01.wav","body_fall_small_02.wav","body_fall_small_03.wav","body_fall_small_04.wav","body_fall_small_05.wav","body_fall_small_06.wav","body_fall_small_07.wav","body_fall_small_08.wav"]),
 ("body_fall_big",sf_priority_6|sf_vol_8, ["body_fall_large_01.wav","body_fall_large_02.wav","body_fall_large_03.wav","body_fall_large_04.wav","body_fall_large_05.wav","body_fall_large_06.wav","body_fall_large_07.wav","body_fall_large_08.wav"]),
# ("body_fall_very_big",sf_priority_9|sf_vol_10, ["body_fall_very_big_1.wav"]),
 ("horse_body_fall_begin",sf_priority_7|sf_vol_10, ["horse_fall_b_01.wav","horse_fall_b_02.wav","horse_fall_b_03.wav"]),
 ("horse_body_fall_end",sf_priority_7|sf_vol_10, ["horse_fall_e_01.wav","horse_fall_e_02.wav","horse_fall_e_03.wav"]),
 
## ("clang_metal",sf_priority_9, ["clang_metal_1.wav","clang_metal_2.wav","s_swordClash1.wav","s_swordClash2.wav","s_swordClash3.wav"]),
 ("hit_wood_wood",sf_priority_7|sf_vol_12, ["wood_on_wood_01.wav","wood_on_wood_02.wav","wood_on_wood_03.wav","wood_on_wood_04.wav","wood_on_wood_05.wav","wood_on_wood_06.wav","wood_on_wood_07.wav","wood_on_wood_08.wav"]),#dummy
 ("hit_metal_metal",sf_priority_7|sf_vol_10, ["Sword_clash_01.wav","Sword_clash_02.wav","Sword_clash_03.wav","Sword_clash_04.wav","Sword_clash_05.wav","Sword_clash_06.wav","Sword_clash_07.wav","Sword_clash_08.wav","Sword_clash_09.wav","Sword_clash_10.wav","Sword_clash_11.wav","Sword_clash_12.wav","Sword_clash_13.wav","Sword_clash_14.wav","Sword_clash_15.wav","Sword_clash_16.wav","Sword_clash_17.wav","Sword_clash_18.wav","Sword_clash_19.wav","Sword_clash_20.wav","Sword_clash_21.wav","Sword_clash_22.wav","Sword_clash_23.wav","Sword_clash_24.wav","Sword_clash_25.wav","Sword_clash_26.wav","Sword_clash_27.wav"]),
 ("hit_wood_metal",sf_priority_7|sf_vol_10, ["metal_on_wood_01.wav","metal_on_wood_02.wav","metal_on_wood_03.wav","metal_on_wood_04.wav","metal_on_wood_05.wav","metal_on_wood_06.wav","metal_on_wood_07.wav","metal_on_wood_08.wav","metal_on_wood_09.wav","metal_on_wood_10.wav"]),
# ("clang_metal", sf_priority_9,["sword_clank_metal_09.wav","sword_clank_metal_10.wav","sword_clank_metal_12.wav","sword_clank_metal_13.wav"]),
## ("shield_hit_cut",sf_priority_5, ["shield_hit_cut_3.wav","shield_hit_cut_4.wav","shield_hit_cut_5.wav"]),
 ("shield_hit_wood_wood",sf_priority_7|sf_vol_9, ["shield_wood_wood_01.wav","shield_wood_wood_02.wav","shield_wood_wood_03.wav","shield_wood_wood_04.wav","shield_wood_wood_05.wav","shield_wood_wood_06.wav","shield_wood_wood_07.wav","shield_wood_wood_08.wav","shield_wood_wood_09.wav","shield_wood_wood_10.wav","shield_wood_wood_11.wav","shield_wood_wood_12.wav"]),
 ("shield_hit_metal_metal",sf_priority_7|sf_vol_10, ["shield_metal_metal_01.wav","shield_metal_metal_02.wav","shield_metal_metal_03.wav","shield_metal_metal_04.wav","shield_metal_metal_05.wav","shield_metal_metal_06.wav","shield_metal_metal_07.wav","shield_metal_metal_08.wav","shield_metal_metal_09.wav","shield_metal_metal_10.wav","shield_metal_metal_11.wav","shield_metal_metal_12.wav"]),
 ("shield_hit_wood_metal",sf_priority_7|sf_vol_10, ["shield_metal_wood_01.wav","shield_metal_wood_02.wav","shield_metal_wood_03.wav","shield_metal_wood_04.wav","shield_metal_wood_05.wav","shield_metal_wood_06.wav","shield_metal_wood_07.wav","shield_metal_wood_08.wav","shield_metal_wood_09.wav","shield_metal_wood_10.wav"]), #(shield is wood)
 ("shield_hit_metal_wood",sf_priority_7|sf_vol_10, ["shield_wood_metal_01.wav","shield_wood_metal_02.wav","shield_wood_metal_03.wav","shield_wood_metal_04.wav","shield_wood_metal_05.wav","shield_wood_metal_06.wav","shield_wood_metal_07.wav","shield_wood_metal_08.wav"]),#(shield is metal)
 ("shield_broken",sf_priority_9, ["shield_break_01.wav","shield_break_02.wav"]),
 ("man_hit",sf_priority_2|sf_vol_7, ["man_grunt_pain_01.wav","man_grunt_pain_02.wav","man_grunt_pain_03.wav","man_grunt_pain_04.wav","man_grunt_pain_05.wav","man_grunt_pain_06.wav","man_grunt_pain_07.wav","man_grunt_pain_08.wav","man_grunt_pain_09.wav","man_grunt_pain_10.wav","man_grunt_pain_11.wav","man_grunt_pain_12.wav","man_grunt_pain_13.wav","man_grunt_pain_14.wav","man_grunt_pain_15.wav","man_grunt_pain_16.wav","man_grunt_pain_17.wav","man_grunt_pain_18.wav","man_grunt_pain_19.wav","man_grunt_pain_20.wav"]),
 ("man_die",sf_priority_10|sf_vol_8,  ["man_die_01.wav","man_die_02.wav","man_die_03.wav","man_die_04.wav","man_die_05.wav","man_die_06.wav","man_die_07.wav","man_die_08.wav","man_die_09.wav","man_die_10.wav","man_die_11.wav","man_die_12.wav","man_die_13.wav","man_die_14.wav","man_die_15.wav","man_die_16.wav","man_die_17.wav","man_die_18.wav","man_die_19.wav","man_die_20.wav","man_die_21.wav","man_die_22.wav","man_die_23.wav","man_die_24.wav","man_die_25.wav","man_die_26.wav","man_die_27.wav","man_die_28.wav","man_die_29.wav","man_die_30.wav","man_die_31.wav","man_die_32.wav"]),
 ("woman_hit",sf_priority_7, ["woman_hit_2.wav","woman_hit_3.wav","woman_hit_b_2.wav","woman_hit_b_4.wav","woman_hit_b_6.wav","woman_hit_b_7.wav","woman_hit_b_8.wav","woman_hit_b_11.wav","woman_hit_b_14.wav","woman_hit_b_16.wav"]),
 ("woman_die",sf_priority_10|sf_vol_9, ["woman_fall_1.wav","woman_hit_b_5.wav"]),
 ("woman_yell",sf_priority_8|sf_vol_9, ["woman_yell_1.wav","woman_yell_2.wav"]),
 ("hide",0, ["s_hide.wav"]),
 ("unhide",0, ["s_unhide.wav"]),
 ("neigh",0, ["horse_exterior_whinny_01.wav","horse_exterior_whinny_02.wav","horse_exterior_whinny_03.wav","horse_exterior_whinny_04.wav","horse_exterior_whinny_05.wav","horse_whinny.wav"]),
 ("gallop",sf_vol_4, ["horse_gallop_3.wav","horse_gallop_4.wav","horse_gallop_5.wav"]),
 ("battle",sf_vol_4, ["battle.wav"]),
# ("bow_shoot_player",sf_priority_10|sf_vol_10, ["bow_shoot_4.wav"]),
# ("bow_shoot",sf_priority_4, ["bow_shoot_4.wav"]),
# ("crossbow_shoot",sf_priority_4, ["bow_shoot_2.wav"]),
 ("arrow_hit_body",sf_priority_4, ["missile_flesh_01.wav","missile_flesh_02.wav","missile_flesh_03.wav","missile_flesh_04.wav","missile_flesh_05.wav","missile_flesh_06.wav","missile_flesh_07.wav","missile_flesh_08.wav"]),
 ("metal_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_low_low_01.wav","metal_low_low_02.wav","metal_low_low_03.wav","metal_low_low_04.wav","metal_low_low_05.wav","metal_low_low_06.wav","metal_low_low_07.wav","metal_low_low_08.wav"]),
 ("metal_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["metal_low_high_01.wav","metal_low_high_02.wav","metal_low_high_03.wav","metal_low_high_04.wav","metal_low_high_05.wav","metal_low_high_06.wav","metal_low_high_07.wav","metal_low_high_08.wav","metal_low_high_09.wav","metal_low_high_10.wav","metal_low_high_11.wav","metal_low_high_12.wav","metal_low_high_13.wav","metal_low_high_14.wav","metal_low_high_15.wav","metal_low_high_16.wav","metal_low_high_17.wav","metal_low_high_18.wav","metal_low_high_19.wav","metal_low_high_20.wav","metal_low_high_21.wav","metal_low_high_22.wav","metal_low_high_23.wav","metal_low_high_24.wav","metal_low_high_25.wav","metal_low_high_26.wav","metal_low_high_27.wav"]),
 ("metal_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_high_low_01.wav","metal_high_low_02.wav","metal_high_low_03.wav","metal_high_low_04.wav","metal_high_low_05.wav","metal_high_low_06.wav","metal_high_low_07.wav","metal_high_low_08.wav","metal_high_low_09.wav","metal_high_low_10.wav","metal_high_low_11.wav","metal_high_low_12.wav","metal_high_low_13.wav","metal_high_low_14.wav","metal_high_low_15.wav","metal_high_low_16.wav","metal_high_low_17.wav","metal_high_low_18.wav","metal_high_low_19.wav","metal_high_low_20.wav","metal_high_low_21.wav","metal_high_low_22.wav","metal_high_low_23.wav","metal_high_low_24.wav","metal_high_low_25.wav"]),
 ("metal_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["metal_high_high_01.wav","metal_high_high_02.wav","metal_high_high_03.wav","metal_high_high_04.wav","metal_high_high_05.wav","metal_high_high_06.wav","metal_high_high_07.wav","metal_high_high_08.wav","metal_high_high_09.wav","metal_high_high_10.wav","metal_high_high_11.wav","metal_high_high_12.wav","metal_high_high_13.wav","metal_high_high_14.wav","metal_high_high_15.wav","metal_high_high_16.wav","metal_high_high_17.wav","metal_high_high_18.wav","metal_high_high_19.wav","metal_high_high_20.wav","metal_high_high_21.wav","metal_high_high_22.wav","metal_high_high_23.wav","metal_high_high_24.wav","metal_high_high_25.wav","metal_high_high_26.wav","metal_high_high_27.wav","metal_high_high_28.wav","metal_high_high_29.wav","metal_high_high_30.wav","metal_high_high_31.wav","metal_high_high_32.wav"]),
 ("wooden_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["blunt_low_low_01.wav","blunt_low_low_02.wav","blunt_low_low_03.wav","blunt_low_low_04.wav","blunt_low_low_05.wav","blunt_low_low_06.wav","blunt_low_low_07.wav","blunt_low_low_08.wav","blunt_low_low_09.wav","blunt_low_low_10.wav"]),
 ("wooden_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_low_high_01.wav","blunt_low_high_02.wav","blunt_low_high_03.wav","blunt_low_high_04.wav","blunt_low_high_05.wav","blunt_low_high_06.wav","blunt_low_high_07.wav","blunt_low_high_08.wav","blunt_low_high_09.wav","blunt_low_high_10.wav","blunt_low_high_11.wav","blunt_low_high_12.wav","blunt_low_high_13.wav"]),
 ("wooden_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["blunt_high_low_01.wav","blunt_high_low_02.wav","blunt_high_low_03.wav","blunt_high_low_04.wav","blunt_high_low_05.wav","blunt_high_low_06.wav","blunt_high_low_07.wav","blunt_high_low_08.wav","blunt_high_low_09.wav","blunt_high_low_10.wav"]),
 ("wooden_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_high_high_01.wav","blunt_high_high_02.wav","blunt_high_high_03.wav","blunt_high_high_04.wav","blunt_high_high_05.wav","blunt_high_high_06.wav","blunt_high_high_07.wav","blunt_high_high_08.wav","blunt_high_high_09.wav","blunt_high_high_10.wav","blunt_high_high_11.wav","blunt_high_high_12.wav","blunt_high_high_13.wav","blunt_high_high_14.wav","blunt_high_high_15.wav","blunt_high_high_16.wav","blunt_high_high_17.wav","blunt_high_high_18.wav","blunt_high_high_19.wav","blunt_high_high_20.wav","blunt_high_high_21.wav","blunt_high_high_22.wav"]),
 ("mp_arrow_hit_target",sf_2d|sf_priority_15|sf_vol_9, ["mp_arrow_hit_target.wav"]),
 ("blunt_hit",sf_priority_5|sf_vol_10, ["horse_charge_01.wav","horse_charge_02.wav","horse_charge_03.wav","horse_charge_04.wav","horse_charge_05.wav","horse_charge_06.wav","horse_charge_07.wav","horse_charge_08.wav"]),
 ("player_hit_by_arrow",sf_priority_10|sf_vol_10, ["player_hit_by_arrow.wav"]),
 ("pistol_shot",sf_priority_10|sf_vol_10, ["gun_shoot_01.wav","gun_shoot_02.wav","gun_shoot_03.wav","gun_shoot_04.wav","gun_shoot_05.wav","gun_shoot_06.wav","gun_shoot_07.wav","gun_shoot_08.wav","gun_shoot_09.wav","gun_shoot_10.wav","gun_shoot_11.wav"]),
 ("man_grunt",sf_priority_3|sf_vol_4, ["man_heavy_grunt_01.wav","man_heavy_grunt_02.wav","man_heavy_grunt_03.wav","man_heavy_grunt_04.wav","man_heavy_grunt_05.wav","man_heavy_grunt_06.wav","man_heavy_grunt_07.wav","man_heavy_grunt_08.wav","man_heavy_grunt_09.wav","man_heavy_grunt_10.wav","man_heavy_grunt_11.wav","man_heavy_grunt_12.wav","man_heavy_grunt_13.wav","man_heavy_grunt_14.wav","man_heavy_grunt_15.wav"]),
 ("man_breath_hard",sf_priority_3|sf_vol_8, ["man_heavy_grunt_01.wav","man_heavy_grunt_02.wav","man_heavy_grunt_03.wav","man_heavy_grunt_04.wav","man_heavy_grunt_05.wav","man_heavy_grunt_06.wav","man_heavy_grunt_07.wav","man_heavy_grunt_08.wav","man_heavy_grunt_09.wav","man_heavy_grunt_10.wav","man_heavy_grunt_11.wav","man_heavy_grunt_12.wav","man_heavy_grunt_13.wav","man_heavy_grunt_14.wav","man_heavy_grunt_15.wav"]),
 ("man_stun",sf_priority_3|sf_vol_8, ["man_short_grunt_01.wav","man_short_grunt_02.wav"]),
 ("man_grunt_long",sf_priority_6|sf_vol_7, ["man_heavy_grunt_01.wav","man_heavy_grunt_02.wav","man_heavy_grunt_03.wav","man_heavy_grunt_04.wav","man_heavy_grunt_05.wav","man_heavy_grunt_06.wav","man_heavy_grunt_07.wav","man_heavy_grunt_08.wav","man_heavy_grunt_09.wav","man_heavy_grunt_10.wav","man_heavy_grunt_11.wav","man_heavy_grunt_12.wav","man_heavy_grunt_13.wav","man_heavy_grunt_14.wav","man_heavy_grunt_15.wav"]),
 ("man_yell",sf_priority_5|sf_vol_8, ["man_yell_4.wav","man_yell_7.wav","man_yell_9.wav","man_yell_11.wav","man_yell_13.wav","man_yell_15.wav","man_yell_16.wav","man_yell_17.wav","man_yell_20.wav","man_shortyell_4.wav","man_shortyell_5.wav","man_shortyell_6.wav","man_shortyell_9.wav","man_shortyell_11.wav","man_shortyell_11b.wav","man_yell_b_18.wav","man_yell_b_21.wav","man_yell_b_22.wav","man_yell_b_23.wav","man_yell_c_20.wav","man_yell_01.wav","man_yell_02.wav","man_yell_03.wav","man_yell_04.wav","man_yell_05.wav","man_yell_06.wav","man_yell_07.wav","man_yell_08.wav","man_yell_09.wav","man_yell_10.wav","man_yell_11b.wav","man_yell_12.wav"]),
## not adequate, removed: "man_yell_b_21.wav","man_yell_b_22.wav","man_yell_b_23.wav"]),
#TODONOW:
 ("man_warcry",sf_priority_5, ["man_insult_2.wav","man_insult_3.wav","man_insult_7.wav","man_insult_9.wav","man_insult_13.wav","man_insult_15.wav","man_insult_16.wav"]),

 ("encounter_looters",sf_2d|sf_vol_8, ["encounter_river_pirates_5.wav","encounter_river_pirates_6.wav","encounter_river_pirates_9.wav","encounter_river_pirates_10.wav","encounter_river_pirates_4.wav"]),

 ("encounter_bandits",sf_2d|sf_vol_8, ["encounter_bandit_2.wav","encounter_bandit_9.wav","encounter_bandit_12.wav","encounter_bandit_13.wav","encounter_bandit_15.wav","encounter_bandit_16.wav","encounter_bandit_10.wav",]),
 ("encounter_farmers",sf_2d|sf_vol_8, ["encounter_farmer_2.wav","encounter_farmer_5.wav","encounter_farmer_7.wav","encounter_farmer_9.wav"]),
 ("encounter_sea_raiders",sf_2d|sf_vol_8, ["encounter_sea_raider_5.wav","encounter_sea_raider_9.wav","encounter_sea_raider_9b.wav","encounter_sea_raider_10.wav"]),
 ("encounter_steppe_bandits",sf_2d|sf_vol_8, ["encounter_steppe_bandit_3.wav","encounter_steppe_bandit_3b.wav","encounter_steppe_bandit_8.wav","encounter_steppe_bandit_10.wav","encounter_steppe_bandit_12.wav"]),
 ("encounter_nobleman",sf_2d|sf_vol_8, ["encounter_nobleman_1.wav"]),
 ("encounter_vaegirs_ally",sf_2d|sf_vol_8, ["encounter_vaegirs_ally.wav","encounter_vaegirs_ally_2.wav"]),
 ("encounter_vaegirs_neutral",sf_2d|sf_vol_8, ["encounter_vaegirs_neutral.wav","encounter_vaegirs_neutral_2.wav","encounter_vaegirs_neutral_3.wav","encounter_vaegirs_neutral_4.wav"]),
 ("encounter_vaegirs_enemy",sf_2d|sf_vol_8, ["encounter_vaegirs_neutral.wav","encounter_vaegirs_neutral_2.wav","encounter_vaegirs_neutral_3.wav","encounter_vaegirs_neutral_4.wav"]),
 ("sneak_town_halt",sf_2d, ["sneak_halt_1.wav","sneak_halt_2.wav"]),
 ("horse_walk",sf_priority_3|sf_vol_5, ["horse_walk_01.wav","horse_walk_02.wav","horse_walk_03.wav","horse_walk_04.wav","horse_walk_05.wav","horse_walk_06.wav","horse_walk_07.wav","horse_walk_08.wav"]),
 ("horse_trot",sf_priority_4|sf_vol_6, ["horse_trot_01.wav","horse_trot_02.wav","horse_trot_03.wav","horse_trot_04.wav","horse_trot_05.wav","horse_trot_06.wav","horse_trot_07.wav","horse_trot_08.wav","horse_trot_09.wav","horse_trot_10.wav"]),
 ("horse_canter",sf_priority_4|sf_vol_7, ["horse_canter_01.wav","horse_canter_02.wav","horse_canter_03.wav","horse_canter_04.wav","horse_canter_05.wav","horse_canter_06.wav","horse_canter_07.wav","horse_canter_08.wav"]),
 ("horse_gallop",sf_priority_5|sf_vol_8, ["horse_gallop_01.wav","horse_gallop_02.wav","horse_gallop_03.wav","horse_gallop_04.wav","horse_gallop_05.wav","horse_gallop_06.wav","horse_gallop_07.wav","horse_gallop_08.wav","horse_gallop_09.wav","horse_gallop_10.wav"]),
 ("horse_breath",sf_priority_1|sf_vol_4, ["horse_breath_4.wav","horse_breath_5.wav","horse_breath_6.wav","horse_breath_7.wav"]),
 ("horse_snort",sf_priority_1|sf_vol_2, ["horse_snort_1.wav","horse_snort_2.wav","horse_snort_3.wav","horse_snort_4.wav","horse_snort_5.wav"]),
 ("horse_low_whinny",sf_vol_12, ["horse_whinny-1.wav","horse_whinny-2.wav"]),
 ("block_fist",0, ["block_fist_3.wav","block_fist_4.wav"]),
 ("man_hit_blunt_weak",sf_priority_5|sf_vol_10, ["man_hit_13.wav","man_hit_29.wav","man_hit_32.wav","man_hit_47.wav","man_hit_57.wav"]),
 ("man_hit_blunt_strong",sf_priority_5|sf_vol_10, ["man_hit_13.wav","man_hit_29.wav","man_hit_32.wav","man_hit_47.wav","man_hit_57.wav"]),
 ("man_hit_pierce_weak",sf_priority_5|sf_vol_10, ["man_hit_13.wav","man_hit_29.wav","man_hit_32.wav","man_hit_47.wav","man_hit_57.wav"]),
 ("man_hit_pierce_strong",sf_priority_5|sf_vol_10, ["man_hit_13.wav","man_hit_29.wav","man_hit_32.wav","man_hit_47.wav","man_hit_57.wav"]),
 ("man_hit_cut_weak",sf_priority_5|sf_vol_10, ["man_hit_13.wav","man_hit_29.wav","man_hit_32.wav","man_hit_47.wav","man_hit_57.wav"]),
 ("man_hit_cut_strong",sf_priority_5|sf_vol_10, ["man_hit_13.wav","man_hit_29.wav","man_hit_32.wav","man_hit_47.wav","man_hit_57.wav"]),
 ("man_victory",sf_priority_5|sf_vol_9, ["man_victory_3.wav","man_victory_4.wav","man_victory_5.wav","man_victory_8.wav","man_victory_15.wav","man_victory_49.wav","man_victory_52.wav","man_victory_54.wav","man_victory_57.wav","man_victory_71.wav","man_victory_01.wav","man_victory_02.wav","man_victory_03.wav"]),
 ("fire_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.wav"]),
 ("torch_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.wav"]),
 ("dummy_hit",sf_priority_9, ["dummy_hit_01.wav","dummy_hit_02.wav","dummy_hit_03.wav"]),
 ("dummy_destroyed",sf_priority_9, ["dummy_break_01.wav","dummy_break_02.wav","dummy_break_03.wav","dummy_break_04.wav","dummy_break_05.wav"]),
 ("gourd_destroyed",sf_priority_9, ["dummy_break_01.wav","dummy_break_02.wav","dummy_break_03.wav","dummy_break_04.wav","dummy_break_05.wav"]),#TODO
 ("cow_moo", sf_2d|sf_priority_9|sf_vol_8, ["cow_moo_1.wav"]),
 ("cow_slaughter", sf_2d|sf_priority_3|sf_vol_8, ["cow_slaughter_01.wav","cow_slaughter_02.wav"]),
 ("distant_dog_bark", sf_2d|sf_priority_3|sf_vol_8, ["d_dog1.wav","d_dog2.wav","d_dog3.wav","d_dog7.wav"]),
 ("distant_owl", sf_2d|sf_priority_3|sf_vol_9, ["d_owl2.wav","d_owl3.wav","d_owl4.wav"]),
 ("distant_chicken", sf_2d|sf_priority_3|sf_vol_8, ["d_chicken1.wav","d_chicken2.wav"]),
 ("distant_carpenter", sf_2d|sf_priority_3|sf_vol_3, ["d_carpenter1.wav","d_saw_short3.wav"]),
 ("distant_blacksmith", sf_2d|sf_priority_3|sf_vol_4, ["d_blacksmith2.wav"]),
 ("arena_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["arena_loop11.wav"]),
 ("town_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["town_loop_3.wav"]),
 ("tutorial_fail", sf_2d|sf_vol_7,["cue_failure.wav"]),
 ("your_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["your_flag_taken.wav"]),
 ("enemy_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["enemy_flag_taken.wav"]),
 ("flag_returned", sf_2d|sf_priority_10|sf_vol_10, ["your_flag_returned.wav"]),
 ("team_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["you_scored_a_point.wav"]),
 ("enemy_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["enemy_scored_a_point.wav"]),
 #chief anade sonidos sot
 ("wolf_short", sf_2d|sf_priority_9|sf_vol_6,["wolf_short.mp3"]),
 ("morning_birds", sf_2d|sf_priority_9|sf_vol_4,["morning_birds.wav"]),
 ("bells", sf_2d|sf_priority_9|sf_vol_8,["bells.wav"]),
  ("pickaxesound",sf_2d|sf_vol_6, ["pickaxesound.mp3"]),
  ("rockslide",sf_2d|sf_vol_6, ["rockslide.mp3"]),
 ("woman_cough",sf_2d|sf_priority_5|sf_vol_2, ["FA_female_cough_1.wav","FA_female_cough_2.wav","FA_female_cough_3.wav","FA_female_cough_4.wav"]),
("man_cough",sf_2d|sf_priority_5|sf_vol_2, ["FA_male_cough_1.wav","FA_male_cough_2.wav","FA_male_cough_3.wav","FA_male_cough_4.wav",]),
("burn",sf_priority_10|sf_vol_2|sf_start_at_random_pos,["FA_Fire_Small_Crackle_Slick_op.wav", "Fire_Torch_Loop3.wav"]),
("sizzle",sf_priority_10|sf_vol_2|sf_start_at_random_pos,["FA_sizzle.wav"]),
("horn", sf_2d|sf_priority_9|sf_vol_8,["horn.wav"]),
 ("marchingdrums", sf_2d|sf_priority_9|sf_vol_9, ["marchingdrums.wav"]),
 ("ciervomuerto", sf_2d|sf_priority_9|sf_vol_10,["ciervomuerto.wav"]),
 ("boarmuerto", sf_2d|sf_priority_9|sf_vol_10,["cerdo.mp3"]),
 ("campanas", sf_2d|sf_priority_9|sf_vol_10,["campanas.mp3"]),
#sonidos batallas marinas
  ### KLABAUTERMANN sounds
 ("set_sail", sf_vol_12|sf_priority_1,["segelsetzung.mp3"]),
 ("ship_drive", sf_vol_6|sf_priority_1|sf_looping,["harte_fahrt.mp3"]),
 ("ship_stay", sf_vol_6|sf_priority_1|sf_looping,["schiff_liegt.mp3"]),
 ("front_water", sf_vol_8|sf_priority_1,["jump_begin_water.wav"]),
 ("crash", sf_vol_15|sf_priority_1,["drum_3.wav"]),
#chief acaba
#multiplayer chief
 ("corazon_late", sf_vol_1|sf_priority_1,["Latidocorazonrapido.mp3"]),
# ("corazon_late2", sf_vol_3|sf_priority_1,["Latidocorazonrapido.mp3"]),
 ("breathing_heavy", sf_vol_15|sf_priority_1,["breathing_heavy.mp3"]),
 ("wind_heavy", sf_vol_7|sf_priority_3,["wind_heavy.mp3"]),
 ("desert_winds", sf_vol_7|sf_priority_3,["desert_winds.mp3"]),
 ("heavy_waves_on_shore", sf_vol_7|sf_priority_3,["heavy_waves_on_shore.mp3"]),
 ("marsh_bugs", sf_vol_7|sf_priority_3,["marsh_bugs.mp3"]),
 ("wind_solobird", sf_vol_7|sf_priority_3,["wind_solobird.mp3"]),
 ("wind_through_trees", sf_vol_7|sf_priority_3,["wind_through_trees.mp3"]),
 ("mp_killing_opponent", sf_vol_7|sf_priority_3,["mp_killing_opponent.mp3"]),
 ("mp_battle_lost", sf_vol_7|sf_priority_3,["mp_battle_lost.mp3"]),
 ("mp_battle_won", sf_vol_7|sf_priority_3,["mp_battle_won.mp3"]),
 ("horn2", sf_2d|sf_priority_9|sf_vol_8,["horn.wav"]),
 ("chain", sf_vol_8|sf_priority_2, ["chain.ogg"]),
 ("draw_flail",sf_priority_4, ["draw_flail.ogg"]),
]
