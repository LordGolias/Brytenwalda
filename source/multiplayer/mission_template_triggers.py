from source.header_operations import *
from source.header_common import *

from source.header_triggers import *
from source.header_items import *

from source.module_constants import *
from source.module_items_shields import HEAVY_SHIELD_WIDTH


from shield_bash import mp_shield_bash_1, mp_shield_bash_2


#respiracion chief para multi Anade respiracion mas bleed - bloodloss
respiracion_moribunda = (0, 0, 12, [
    ], # o pressed?
##
        [
####      (multiplayer_is_server),
####          (try_for_agents,":agent"),
####              (agent_is_alive,":agent"),
####                          (store_agent_hit_points, ":cur_hp",":agent",0),
####                          (try_begin),
####                              (lt,":cur_hp",30),
####
         (try_for_agents,":cur_agent"), # loops through all players.
            (agent_is_alive,":cur_agent"), #  test for alive players.
            (agent_is_human,":cur_agent"), # test for player that are human.
            (store_agent_hit_points,":cur_agent_hp",":cur_agent", 1), # stores the hp value of the alive and human players.
            (le, ":cur_agent_hp",25), #55 = max? #27.5 = 50% # test if the players hp is greater than 27.5 and if true exit the loop.
            #(store_add,":cur_full_health", ":cur_agent_hp",0),
            #(agent_set_hit_points,":cur_agent", ":cur_full_health",1),
        #(else_try),
            (store_sub,":damage",":cur_agent_hp",1), # if the above try_for_agents statement failed, store the players hp and subtract 1 from it.
         (agent_get_position, pos1, ":cur_agent"),
         (position_move_z, pos1, 150), #makes the blood higher, otherwise it's on ground level
         (position_move_x, pos1, -35), #makes the blood out from the torso towards the arm stump
         (position_move_y, pos1, -10), #makes the blood come out severed stump
         (position_rotate_x, pos1, -90), #makes the blood spurt downwards
         (particle_system_burst, "psys_game_blood_2", pos1, 100), #100 as power.

         (agent_set_hit_points,":cur_agent", ":damage",1), # update the players hp value with the new calculation value from above.
                    (agent_play_sound, ":cur_agent", "snd_breathing_heavy"), # if the value is one then play death sound.
                                       # (display_message, "@You take 1 damage from blood loss."),
                 (try_begin),
                    (le,":cur_agent_hp",1),
                    (agent_stop_sound, ":cur_agent"),
                                        (agent_set_hit_points,":cur_agent",0,1),#insta-death, muerte fija al decapitar
                (try_end),
##                          (try_begin),
##                                          (agent_get_player_id,":player",":cur_agent"),
##                                          (player_is_active, ":player"),
####                 (try_begin),
####                    (le,":cur_agent_hp",2),
####                                          (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 2, ":player"), ### 1 ist the number of healing
######                          (else_try), #puesto off para no saturar
######                                          (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 1, ":player"), ### 1 ist the number of healing
####                (try_end),
##                                (try_end),
                      #  (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_breathing_heavy"),
####                (agent_get_player_id,":player",":agent"), #msg
####                     (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 1, ":player"),
####             (display_message, "@You heallllll ally."),
####                          (try_end),
                         (try_end),
        ])

###fatiga multiplayer
sistema_fatiga_multi = (ti_on_agent_spawn, 0, 0, [

    ],[    #determina fatiga al principio de la batalla para todos
        (store_trigger_param_1, ":agent_no"),
        (multiplayer_get_my_player,":player_no"),
           (player_is_active, ":player_no"),
           #(neg|player_is_busy_with_menus, ":player_no"),
           # (neg|is_presentation_active, "prsnt_staminabar"),

             (player_get_agent_id, ":my_agent_id",":player_no"),
           (eq, ":agent_no", ":my_agent_id"),

        (agent_is_alive,":agent_no"), #
      (agent_is_human, ":agent_no"),
     #    (neg|agent_is_non_player, ":agent_no"),

        (store_agent_hit_points,":cur_agent_hp",":agent_no", 1), # stores the hp value of the alive and human players.
        (assign, ":basic_stamina",":cur_agent_hp"),
        (val_add, ":basic_stamina", 20), #obtenemos total fatigue min 60 max 141
        (agent_set_slot, ":agent_no", "slot_agent_fatiga_inicial", ":basic_stamina"), #se la aplicamos al agente
        (agent_set_slot, ":agent_no", "slot_agent_fatiga", ":basic_stamina"), #se la aplicamos al agente

           (start_presentation, "prsnt_staminabar_multi"),
        #    (try_end),
#    (try_end),
    ])

recupera_fatiga_multi = (0, 0, 3, [
(game_key_clicked, gk_attack),
 #(game_key_is_down, gk_attack),
       # (key_clicked, gk_attack),
            ],[    #determina fatiga al principio de la batalla para todos

      (multiplayer_get_my_player, ":my_player"),
           (neg|player_is_busy_with_menus, ":my_player"),
           (player_is_active, ":my_player"),
      (player_get_agent_id, ":my_agent", ":my_player"),
      (try_for_agents, ":agent"),
        (agent_is_human, ":agent"),
        (agent_is_alive, ":agent"),
        (try_begin),
        (eq, ":agent", ":my_agent"),
          (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart_deathmatch"),
         (neg|is_presentation_active,        "prsnt_staminabar_multi"),
    (start_presentation, "prsnt_staminabar_multi"),
        (else_try),
            #(display_message,"@ "),
        (try_end),
        (try_end),
    ])

suma_fatigue_multi = (4, 0, 0, [(is_presentation_active, "prsnt_staminabar_multi"),
],[

    (try_for_agents, ":agent_no"),

        (agent_is_alive,":agent_no"), #  test for alive players.
      (agent_is_human, ":agent_no"),
##            (try_begin),
##        (is_presentation_active, "prsnt_staminabar_multi"),
        (agent_get_slot, ":basic_stamina", ":agent_no", "slot_agent_fatiga"),
        (agent_get_slot, ":basic_stamina_i", ":agent_no", "slot_agent_fatiga_inicial"),
        (lt, ":basic_stamina", ":basic_stamina_i"),

        (val_add, ":basic_stamina", 6), #siempre va a sumar un minimo de 1
        (agent_set_slot, ":agent_no", "slot_agent_fatiga", ":basic_stamina"), #se la aplicamos al agente
##            (else_try),
##           (start_presentation, "prsnt_staminabar_multi"),
##    (try_end),
    (try_end),
    ])

fatigue_bots_multi = (30, 0, 0, [
],[

    (try_for_agents, ":agent_no"),
      (agent_is_non_player, ":agent_no"),
        (agent_is_alive,":agent_no"), #  test for alive players.
      (agent_is_human, ":agent_no"),
        (assign, ":basic_stamina",70),
        (val_add, ":basic_stamina", 5), #obtenemos total fatigue min 60 max 141
        (agent_set_slot, ":agent_no", "slot_agent_fatiga_inicial", ":basic_stamina"), #se la aplicamos al agente
       (agent_set_slot, ":agent_no", "slot_agent_fatiga", ":basic_stamina"), #se la aplicamos al agente
    (try_end),
    ])

#gdw 3 0 0
resta_fatigue_porcorrer_multi = (4, 0, 0, [         (is_presentation_active, "prsnt_staminabar_multi"),
    (this_or_next|game_key_is_down, gk_move_forward),
   (this_or_next|game_key_is_down, gk_move_backward),
    (this_or_next|game_key_is_down, gk_move_left),
   (game_key_is_down, gk_move_right),
                                                    (neg|key_is_down,key_left_shift), #Don't trip if walking
       # (neg|main_hero_fallen),
                                     ],[

        (multiplayer_get_my_player,":player"),

              (player_get_agent_id, ":agent_no",":player"),
        (agent_is_alive,":agent_no"), #  test for alive players.
      (agent_is_human, ":agent_no"),
       (agent_get_horse,":agent_mounted",":agent_no"),
           (eq,":agent_mounted",-1),

        (assign, ":stamina_coste", 1),

           (agent_get_item_slot, ":cur_armor", ":agent_no", ek_body),#Here we are getting body armor
            (try_begin),
                (is_between, ":cur_armor", armadura_pesada_begin, armadura_pesada3_end),
               (val_add, ":stamina_coste", 2),
            (else_try),
                (is_between, ":cur_armor", armadura_media_begin, armadura_media_end),
                (val_add, ":stamina_coste", 1),
##           (else_try),
##                (eq, ":cur_armor", "itm_no_item"), #ni suma ni resta, no tiene nada
           (else_try),
                (is_between, ":cur_armor", desnudos_begin, desnudos_end), #es equipamiento ritual
                (val_sub, ":stamina_coste", 1),
            (try_end),

           (agent_get_item_slot, ":cur_armor", ":agent_no", ek_head),#Here we are getting head armor
                 (try_begin),
                    (is_between, ":cur_armor", yelmos_pesados2_begin, yelmos_pesados2_end),
                    (val_add, ":stamina_coste", 1),
                 (try_end),

             (agent_get_item_slot, ":cur_armor", ":agent_no", ek_foot),#Here we are getting leg armor
             (try_begin),
                 (is_between, ":cur_armor", calzado_pesados_begin, calzado_pesados_end),
                 (val_add, ":stamina_coste", 1),
             (try_end),

             #no heavy gloves in Brytenwalda.
            # (agent_get_item_slot, ":cur_armor", ":agent_no", ek_gloves),#Here we are getting arm armor
            # (try_begin),
                # (is_between, ":cur_armor", guantes_pesados_begin, guantes_pesados_end),
                # (val_add, ":stamina_coste", 1),
            # (try_end),

            # todo: exact copy found in other trigger at single player mission templates. DRY and make a common statement
            # Now for the four armaments every agent may carry (not wear)
            (try_begin),
                (agent_get_item_slot, ":cur_weapon", ":player", ek_item_0),
                (item_get_type, ":type", ":cur_weapon"),
                (eq, ":type", itp_type_shield),

                (item_get_weapon_length, ":width", ":cur_weapon"),
                (gt, ":width", HEAVY_SHIELD_WIDTH),
                (val_add, ":stamina_coste", 1),
            (try_end),

            (try_begin),
                (agent_get_item_slot, ":cur_weapon", ":player", ek_item_1),
                (item_get_type, ":type", ":cur_weapon"),
                (eq, ":type", itp_type_shield),

                (item_get_weapon_length, ":width", ":cur_weapon"),
                (gt, ":width", HEAVY_SHIELD_WIDTH),
                (val_add, ":stamina_coste", 1),
            (try_end),

            (try_begin),
                (agent_get_item_slot, ":cur_weapon", ":player", ek_item_2),
                (item_get_type, ":type", ":cur_weapon"),
                (eq, ":type", itp_type_shield),

                (item_get_weapon_length, ":width", ":cur_weapon"),
                (gt, ":width", HEAVY_SHIELD_WIDTH),
                (val_add, ":stamina_coste", 1),
            (try_end),

            (try_begin),
                (agent_get_item_slot, ":cur_weapon", ":player", ek_item_3),
                (item_get_type, ":type", ":cur_weapon"),
                (eq, ":type", itp_type_shield),

                (item_get_weapon_length, ":width", ":cur_weapon"),
                (gt, ":width", HEAVY_SHIELD_WIDTH),
                (val_add, ":stamina_coste", 1),
            (try_end),
              (try_begin),
        (game_key_clicked, gk_jump),#por saltar
         (val_add, ":stamina_coste", 4),
            (try_end),
                (agent_get_slot, ":basic_stamina", ":agent_no", "slot_agent_fatiga"),

            (try_begin),
        (le, ":basic_stamina", 4),
##                        (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_breathing_heavy"),
            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_strike_fall_back_rise"),
        (agent_play_sound, ":agent_no", "snd_breathing_heavy"), # if the value is one then play death sound.
                                         # (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 3, ":player"), ### 1 ist the number of healing
            #(display_message, "@ no puedes con el alma para correr mas"),
    (try_end),


        (val_sub, ":basic_stamina", ":stamina_coste"), #maximo 10 para un hombre totalmente equipado, y minimo 1 para un picto desnudo

        (val_max, ":basic_stamina", 1), #siempre va a restar un minimo de 1
        (agent_set_slot, ":agent_no", "slot_agent_fatiga", ":basic_stamina"), #se la aplicamos al agente
#    (try_end),
# (try_end),

    ])


resta_fatigue_multi= (1, 0, 0, [      (is_presentation_active, "prsnt_staminabar_multi"),
                                      (this_or_next|game_key_is_down, gk_defend),
        (game_key_is_down, gk_attack),
],[
        (multiplayer_get_my_player,":player"),
           (player_is_active, ":player"),
           (neg|player_is_busy_with_menus, ":player"),
              (player_get_agent_id, ":agent_no",":player"),

        (agent_is_alive,":agent_no"), #  test for alive players.
   (agent_is_human, ":agent_no"),
       (agent_get_horse,":agent_mounted",":agent_no"),
           (eq,":agent_mounted",-1),
    (set_trigger_result, -1),
    (try_begin),
            (agent_get_wielded_item, ":wielded",":agent_no", 0),
            (assign, ":stamina_cost", 1), #pierde fatiga cada golpe.
        (try_begin),
            (this_or_next|is_between, ":wielded", "itm_club_stick", "itm_spathaswordt2"), #armas pequenas
            (is_between, ":wielded", "itm_irish_shsword", "itm_pictish_longsword1"),
            (val_add, ":stamina_cost", 1), #pierde fatiga cada golpe.
        (else_try),
            (this_or_next|is_between, ":wielded", "itm_spathaswordt2", "itm_irish_shsword"),
            (this_or_next|is_between, ":wielded", "itm_staff1", "itm_spear_blade2t2"),
            (this_or_next|is_between, ":wielded", "itm_spear_britonshortt2", "itm_twohand_speart3"),
            (this_or_next|is_between, ":wielded", "itm_engle_speart2", "itm_wessexbanner1"),
            (this_or_next|is_between, ":wielded", "itm_darts", "itm_lyre"),
            (is_between, ":wielded", "itm_pictish_longsword1", "itm_tree_axe2h"),
            (val_add, ":stamina_cost", 2), #pierde fatiga cada golpe.
        (else_try),
            (this_or_next|is_between, ":wielded", "itm_tree_axe2h", "itm_staff1"),
            (this_or_next|is_between, ":wielded", "itm_twohand_speart3", "itm_germanshortspeart2"),
            (is_between, ":wielded", "itm_spear_briton2ht3", "itm_spear_britonshortt2"),
            (val_add, ":stamina_cost", 4), #pierde fatiga cada golpe.
        (try_end),
##        (try_begin), #player pierde stamina por correr yet
##            (this_or_next|is_between, ":wielded", "itm_celtic_shield_smalla", "itm_hshield"),
##            (is_between, ":wielded", "itm_shieldtarcza19", "itm_norman_shield_1"),
##            (val_add, ":stamina_cost", 1), #pierde fatiga cada golpe.
##        (try_end),
        (agent_get_slot, ":inflicted_stamina", ":agent_no", "slot_agent_fatiga"),
        (val_sub, ":inflicted_stamina", ":stamina_cost"),
        (val_max, ":inflicted_stamina", 1),
        (agent_set_slot, ":agent_no", "slot_agent_fatiga", ":inflicted_stamina"), #se la aplicamos al agente

    (try_end),

##    (store_trigger_param_3, ":damage"),
##   (gt, ":damage", 0),

    (agent_get_slot, ":basic_stamina", ":agent_no", "slot_agent_fatiga"),

    (try_begin),
##        (le, ":basic_stamina", 10), #animacion y sonido aplicados en correr ya
##            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_fatigues1"),
##                                          (multiplayer_send_2_int_to_server,multiplayer_event_message_server2, 3, ":player"), ### 1 ist the number of healing
#    (else_try),
        (lt, ":basic_stamina", 6),
            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_fatigues1"),
                                      #   (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 3, ":player"), ### 1 ist the number of healing
##   (else_try), #puesto off chief para no saturar
##        (lt, ":basic_stamina", 25),
##                                         (multiplayer_send_2_int_to_server,multiplayer_event_message_server2, 1, ":player"), ### 1 ist the number of healing
    (try_end),





                       # (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_corazon_late2"),

    ])
#fatiga multiplayer acaba
#rain multiplayer
rain_multi = (
    ti_before_mission_start, 0, ti_once, [
        (store_current_scene, ":cur_scene"),
           (neq, ":cur_scene", "scn_multi_scene_3"),
],
   [
        #(multiplayer_is_server), # test for a multiplayer server.
                (store_random_in_range, ":rain_chance", 1,11),
                (try_begin),
                    (eq, ":rain_chance", 1),
           (set_rain, 1, 80),
           (set_global_cloud_amount, 75),
           (set_global_haze_amount, 35),
##                    (store_random_in_range, ":rain_power", 50, 100),
##                    (store_random_in_range, ":haze_power", 25, 65),
##                    (set_global_haze_amount, ":haze_power"),
##                    (set_rain, 1, ":rain_power"),
                (else_try),
                    (eq, ":rain_chance", 2),
           (set_rain, 1, 50),
           (set_global_cloud_amount, 65),
           (set_global_haze_amount, 15),
##                    (store_random_in_range, ":rain_power", 50, 100),
##                    (store_random_in_range, ":haze_power", 25, 65),
##                    (set_global_haze_amount, ":haze_power"),
##                    (set_rain, 1, ":rain_power"),
                (else_try),
                    (eq, ":rain_chance", 3),
           (set_fog_distance, 55, 0x333333),
           (set_global_cloud_amount, 25),
           (set_global_haze_amount, 45),
##                    (store_random_in_range, ":fog_distance", 50, 75),
##                    (store_random_in_range, ":haze_power", 25, 65),
##                    (set_global_haze_amount, ":haze_power"),
##                                        (set_fog_distance, ":fog_distance", 0x333333),
                (else_try),
                    (eq, ":rain_chance", 4),
           (set_rain, 1, 60),
           (set_global_cloud_amount, 65),
           (set_global_haze_amount, 25),
##                    (store_random_in_range, ":rain_power", 50, 100),
##                    (store_random_in_range, ":haze_power", 25, 65),
##                    (set_global_haze_amount, ":haze_power"),
##                    (set_rain, 1, ":rain_power"),
##                                        (call_script, "script_change_rain_or_snow"),
                (else_try),
                    (eq, ":rain_chance", 5),
           (set_rain, 1, 100),
           (set_global_cloud_amount, 80),
           (set_global_haze_amount, 15),
##                    (store_random_in_range, ":rain_power", 50, 100),
##                    (store_random_in_range, ":haze_power", 25, 65),
##                    (set_global_haze_amount, ":haze_power"),
##                    (set_rain, 2, ":rain_power"),
                (else_try),
                    (set_global_haze_amount, 0),
                    (set_rain, 0, 0),
                (try_end),
   ])


multi_warcry = (0, 0, 60, [(key_clicked, key_b)], # o pressed?

        [

        (multiplayer_get_my_player,":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),
              (player_get_agent_id, ":player_agent",":player_no"),
      (agent_is_human, ":player_agent"),
       (agent_get_horse,":agent_mounted",":player_agent"),
           (eq,":agent_mounted",-1),

             (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_man_warcry"),
             (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_shield_hit_metal_wood"),
            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_taunt"),

        ])


hunt_taunting = (0, 0, 60, [(key_clicked, key_u)], # o pressed?

        [
                 #  (multiplayer_is_server),
        (multiplayer_get_my_player,":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),
              (player_get_agent_id, ":player_agent",":player_no"),
      (agent_is_human, ":player_agent"),
       (agent_get_horse,":agent_mounted",":player_agent"),
           (eq,":agent_mounted",-1),

               (try_begin),
                     (agent_get_wielded_item, ":wielded",":player_agent", 0),
                (this_or_next|eq, ":wielded", "itm_horn1"),#hornhealer
                   (this_or_next|eq, ":wielded", "itm_horn_of_arthur"),#horn of rheged
                   (eq, ":wielded", "itm_horn_multiplayer"), # tiene cuerno?

          (agent_get_position,pos6,":player_agent"),
          (agent_get_team, ":wielder_team", ":player_agent"),
          (assign, ":heal_count", 0),
          (try_for_agents,":agent"),
              (agent_is_alive,":agent"),
              (agent_get_team, ":target_team", ":agent"),
              (eq, ":target_team", ":wielder_team"),
                   (agent_set_slot,":agent", "slot_agent_has_been_healed", 0), #chief
              #(neq,":agent",":player_agent"),
              (agent_get_position,pos4,":agent"),
              (get_distance_between_positions,":dist",pos6,pos4),
              (le,":dist",3500),
              (agent_get_slot, ":healed", ":agent", "slot_agent_has_been_healed"),
              (eq, ":healed", 0),
                          (store_agent_hit_points, ":cur_hp",":agent",0),
                          (try_begin),
                              (lt,":cur_hp",100),
                              (store_agent_hit_points, ":cur_hit_points",":agent",1),
                              (val_add,":cur_hit_points",6),
                              (agent_set_hit_points,":agent",":cur_hit_points",1),

                              (agent_set_slot,":agent", "slot_agent_has_been_healed", 1),
                              (val_add, ":heal_count", 1),
##                (agent_get_player_id,":player",":agent"), #msg para heal #puesto off para no saturar de mensajes
##                     (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 6, ":player"), ### 1 ist the number of healing
                 #   (display_message, "@You heallllll ally."),
                          (try_end),
                 (try_end),
            (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_horn"),
            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_tekst"),
            #(multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_howl"),
        (else_try),
            (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_man_warcry"),
            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_howl"),
        (try_end),

        ])

multi_ambient_sounds = (1,0,30,[],[

        (store_current_scene,":current_scene"),
    #    (store_random_in_range,":random",0,8),

        (try_begin),
##            (eq,":random",0),
            (this_or_next|eq,":current_scene","scn_multi_scene_4"),
            (this_or_next|eq,":current_scene","scn_multi_scene_7"),
            (this_or_next|eq,":current_scene","scn_multi_scene_13"),
            (eq,":current_scene","scn_multi_scene_10"),
            (play_sound,"snd_desert_winds"),
        (else_try),
            (this_or_next|eq,":current_scene","scn_multi_scene_1"),
            (eq,":current_scene","scn_multi_scene_9"),
            (play_sound,"snd_marsh_bugs"),
        (else_try),
##            (eq,":random",1),
            (eq,":current_scene","scn_multi_scene_2"),
            (play_sound,"snd_heavy_waves_on_shore"),
        (else_try),
##            (eq,":random",2),
            (this_or_next|eq,":current_scene","scn_multi_scene_14"),
            (eq,":current_scene","scn_multi_scene_3"),
            (play_sound,"snd_wind_heavy"),
        (else_try),
##            (eq,":random",1),
            (this_or_next|eq,":current_scene","scn_multi_scene_12"),
            (this_or_next|eq,":current_scene","scn_multi_scene_16"),
            (this_or_next|eq,":current_scene","scn_multi_scene_17"),
            (eq,":current_scene","scn_multi_scene_8"),
            (play_sound,"snd_wind_solobird"),
        (else_try),
##            (eq,":random",2),
            (eq,":current_scene","scn_multi_scene_11"),
            (play_sound,"snd_wind_through_trees"),
        (end_try),
        ])

siege_multi_items = (1,0,800,[(multiplayer_is_server)],[

        (try_for_range,":entry",40,50), #para atacantes
            (entry_point_get_position,pos1,":entry"),
            (set_spawn_position,pos1),
            (spawn_item,"itm_torch",0),
        (end_try),

        (try_for_range,":entry",2,15), #para defensores
            (entry_point_get_position,pos1,":entry"),
            (set_spawn_position,pos1),
            (spawn_item,"itm_bolts",0),
        (end_try),

        (try_for_range,":entry",16,22), #para defensores
            (entry_point_get_position,pos1,":entry"),
            (set_spawn_position,pos1),
            (spawn_item,"itm_scale_arm_gloves",0),
        (end_try),

##        (store_random_in_range,":chance",0,3), # 1 in 3 chance of spawning salmon
##
##        (try_begin),
##            (eq,":chance",0),
##            (store_random_in_range,":salmon",0,50),
##            (entry_point_get_position,pos1,":salmon"),
##            (set_spawn_position,pos1),
##            (spawn_item,"itm_salmon_sword",0), # fear the salmon
##        (end_try),

        # For now removed pistol and replaced with hunting knife.

        # (try_for_range,":entry",95,100),
            # (entry_point_get_position,pos1,":entry"),
            # (set_spawn_position,pos1),
            # (spawn_item,"itm_basic_sling",0),
            # (position_move_x,pos1,10,0),
            # (spawn_item,"itm_cartridges",0),
        # (end_try),

        ])
#chief multiplayer acaba
############################################################################ banners dan vida a tropas cercanas age of blades
banner_heal_multi = (0, 0, 60, [(key_clicked, key_j)], # o pressed?

        [         # (multiplayer_is_server),
            (multiplayer_get_my_player,":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),

              (player_get_agent_id, ":player_agent",":player_no"),
                     (agent_get_wielded_item, ":wielded",":player_agent", 0),
#           (try_for_range,":spear","itm_wessexbanner1","itm_heraldicbannert3"),
              (this_or_next|eq,":wielded","itm_wessexbanner1"),
              (this_or_next|eq,":wielded","itm_cavalrybannert2"),
              (this_or_next|eq,":wielded","itm_spearbannert2"),
              (this_or_next|eq,":wielded","itm_spearbanner4"),
              (this_or_next|eq,":wielded","itm_spearbanner5"),
              (this_or_next|eq,":wielded","itm_wessexbanner6"),
              (this_or_next|eq,":wielded","itm_wessexbanner7"),
              (this_or_next|eq,":wielded","itm_wessexbanner8"),
              (eq,":wielded","itm_wessexbanner9"),
#cura
          (agent_get_position,pos6,":player_agent"),
          (agent_get_team, ":wielder_team", ":player_agent"),
          (assign, ":heal_count", 0),
          (try_for_agents,":agent"),
              (agent_is_alive,":agent"),
              (agent_get_team, ":target_team", ":agent"),
              (eq, ":target_team", ":wielder_team"),
              #(neq,":agent",":player_agent"),
                   (agent_set_slot,":agent", "slot_agent_has_been_healed", 0), #chief
              (agent_get_position,pos4,":agent"),
              (get_distance_between_positions,":dist",pos6,pos4),
              (le,":dist",1500),
              (agent_get_slot, ":healed", ":agent", "slot_agent_has_been_healed"),
              (eq, ":healed", 0),
                          (store_agent_hit_points, ":cur_hp",":agent",0),
                          (try_begin),
                              (lt,":cur_hp",100),
                              (store_agent_hit_points, ":cur_hit_points",":agent",1),
                              (val_add,":cur_hit_points",20),
                              (agent_set_hit_points,":agent",":cur_hit_points",1),

                              (agent_set_slot,":agent", "slot_agent_has_been_healed", 1),
                              (val_add, ":heal_count", 1),
##                (agent_get_player_id,":player",":agent"), #msg para heal #puesto off chief para no saturar
##                     (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 7, ":player"), ### 1 ist the number of healing
#             (display_message, "@You heallllll ally."),
                          (try_end),
                 (try_end),
#curas
                        (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_crash"),
            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_pevic_thrust"),

        ])

#1 fire arrow chief empieza siege warfare
fire_arrow_initialize_multi = (0, 0, ti_once, [],[
        (set_fixed_point_multiplier, 100),
        (get_scene_boundaries, pos20, pos21),
        (position_get_x, "$g_min_x", pos20),
        (position_get_y, "$g_min_y", pos20),
        (position_get_x, "$g_max_x", pos21),
        (position_get_y, "$g_max_y", pos21),
        (assign, "$g_min_z", 5),
        (assign, "$g_max_z", 6000),
        (val_add, "$g_min_x", 6),
        (val_add, "$g_min_x", 6),
        (val_sub, "$g_max_x", 6),
        (val_sub, "$g_max_y", 6),
        #(assign, reg1, "$g_min_x"),
        #(assign, reg2, "$g_max_x"),
        #(assign, reg3, "$g_min_y"),
        #(assign, reg4, "$g_max_y"),
        #(assign, reg5, "$g_min_z"),
        #(assign, reg6, "$g_max_z"),
        #(display_message, "@DEBUG: x({reg1}-{reg2}) y({reg3}-{reg4}) z({reg5}-{reg6})"),
])

fire_arrow_routine_multi = (0.01, 0, 0,
  [ ],#(troop_slot_ge, "trp_global_value", slot_gloval_max_fire_arrow, 1),
  [
      (multiplayer_is_server),
    (call_script, "script_fire_arrow_routine"),
  ])

toggle_fire_arrow_mode_multi = (0, 0, 0, [], #Highlander a esto le anadimos lo de los nombres chiefg
  [
        (try_begin),
    (troop_get_slot, ":key", "trp_global_value", slot_gloval_fire_arrow_key),
    (key_clicked, ":key"), ###tecla h chief
    (call_script,"script_toggle_fire_arrow_mode"),
        (try_end),
        (try_begin),
          (key_is_down, key_left_alt),
          (start_presentation, "prsnt_multiplayer_name_projection_display"),
        (try_end),
  ])

fire_element_life_multi = (3, 0, 0,
  [],#(troop_slot_ge, "trp_global_value", slot_gloval_max_flame_slot, 1),
  [

      (call_script, "script_flame_routine")])

destructible_object_initialize_multi  = (
  ti_before_mission_start, 0, 0, [],[
      (call_script,"script_initialize_agents_use_fire_arrow"),
      (call_script, "script_destructible_object_initialize")])

multiplayer_server_check_belfry_movement = (
  0, 0, 0, [],
  [
    (multiplayer_is_server),
    (set_fixed_point_multiplier, 100),

    (try_for_range, ":belfry_kind", 0, 2),
      (try_begin),
        (eq, ":belfry_kind", 0),
        (assign, ":belfry_body_scene_prop", "spr_belfry_a"),
      (else_try),
        (assign, ":belfry_body_scene_prop", "spr_belfry_b"),
      (try_end),

      (scene_prop_get_num_instances, ":num_belfries", ":belfry_body_scene_prop"),
      (try_for_range, ":belfry_no", 0, ":num_belfries"),
        (scene_prop_get_instance, ":belfry_scene_prop_id", ":belfry_body_scene_prop", ":belfry_no"),
        (prop_instance_get_position, pos1, ":belfry_scene_prop_id"), #pos1 holds position of current belfry
        (prop_instance_get_starting_position, pos11, ":belfry_scene_prop_id"),

        (store_add, ":belfry_first_entry_point_id", 11, ":belfry_no"), #belfry entry points are 110..119 and 120..129 and 130..139
        (try_begin),
          (eq, ":belfry_kind", 1),
          (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),
          (val_add, ":belfry_first_entry_point_id", ":number_of_belfry_a"),
        (try_end),

        (val_mul, ":belfry_first_entry_point_id", 10),
        (store_add, ":belfry_last_entry_point_id", ":belfry_first_entry_point_id", 10),

        (try_for_range, ":entry_point_id", ":belfry_first_entry_point_id", ":belfry_last_entry_point_id"),
          (entry_point_is_auto_generated, ":entry_point_id"),
          (assign, ":belfry_last_entry_point_id", ":entry_point_id"),
        (try_end),

        (assign, ":belfry_last_entry_point_id_plus_one", ":belfry_last_entry_point_id"),
        (val_sub, ":belfry_last_entry_point_id", 1),
        (assign, reg0, ":belfry_last_entry_point_id"),
        (neg|entry_point_is_auto_generated, ":belfry_last_entry_point_id"),

        (try_begin),
          (get_sq_distance_between_positions, ":dist_between_belfry_and_its_destination", pos1, pos11),
          (ge, ":dist_between_belfry_and_its_destination", 4), #0.2 * 0.2 * 100 = 4 (if distance between belfry and its destination already less than 20cm no need to move it anymore)

          (assign, ":max_dist_between_entry_point_and_belfry_destination", -1), #should be lower than 0 to allow belfry to go last entry point
          (assign, ":belfry_next_entry_point_id", -1),
          (try_for_range, ":entry_point_id", ":belfry_first_entry_point_id", ":belfry_last_entry_point_id_plus_one"),
            (entry_point_get_position, pos4, ":entry_point_id"),
            (get_sq_distance_between_positions, ":dist_between_entry_point_and_belfry_destination", pos11, pos4),
            (lt, ":dist_between_entry_point_and_belfry_destination", ":dist_between_belfry_and_its_destination"),
            (gt, ":dist_between_entry_point_and_belfry_destination", ":max_dist_between_entry_point_and_belfry_destination"),
            (assign, ":max_dist_between_entry_point_and_belfry_destination", ":dist_between_entry_point_and_belfry_destination"),
            (assign, ":belfry_next_entry_point_id", ":entry_point_id"),
          (try_end),

          (try_begin),
            (ge, ":belfry_next_entry_point_id", 0),
            (entry_point_get_position, pos5, ":belfry_next_entry_point_id"), #pos5 holds belfry next entry point target during its path
          (else_try),
            (copy_position, pos5, pos11),
          (try_end),

          (get_distance_between_positions, ":belfry_next_entry_point_distance", pos1, pos5),

          #collecting scene prop ids of belfry parts
          (try_begin),
            (eq, ":belfry_kind", 0),
            #belfry platform_a
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
            #belfry platform_b
            (scene_prop_get_instance, ":belfry_platform_b_scene_prop_id", "spr_belfry_platform_b", ":belfry_no"),
          (else_try),
            #belfry platform_a
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
          (try_end),

          #belfry wheel_1
          (store_mul, ":wheel_no", ":belfry_no", 3),
          (try_begin),
            (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
            (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),
            (store_mul, ":number_of_belfry_a_wheels", ":number_of_belfry_a", 3),
            (val_add, ":wheel_no", ":number_of_belfry_a_wheels"),
          (try_end),
          (scene_prop_get_instance, ":belfry_wheel_1_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
          #belfry wheel_2
          (val_add, ":wheel_no", 1),
          (scene_prop_get_instance, ":belfry_wheel_2_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
          #belfry wheel_3
          (val_add, ":wheel_no", 1),
          (scene_prop_get_instance, ":belfry_wheel_3_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),

          (init_position, pos17),
          (position_move_y, pos17, -225),
          (position_transform_position_to_parent, pos18, pos1, pos17),
          (position_move_y, pos17, -225),
          (position_transform_position_to_parent, pos19, pos1, pos17),

          (assign, ":number_of_agents_around_belfry", 0),
          (get_max_players, ":num_players"),
          (try_for_range, ":player_no", 0, ":num_players"),
            (player_is_active, ":player_no"),
            (player_get_agent_id, ":agent_id", ":player_no"),
            (ge, ":agent_id", 0),
            (agent_get_team, ":agent_team", ":agent_id"),
            (eq, ":agent_team", 1), #only team2 players allowed to move belfry (team which spawns outside the castle (team1 = 0, team2 = 1))
            (agent_get_horse, ":agent_horse_id", ":agent_id"),
            (eq, ":agent_horse_id", -1),
            (agent_get_position, pos2, ":agent_id"),
            (get_sq_distance_between_positions_in_meters, ":dist_between_agent_and_belfry", pos18, pos2),

            (lt, ":dist_between_agent_and_belfry", multi_distance_sq_to_use_belfry), #must be at most 10m * 10m = 100m away from the player
            (neg|scene_prop_has_agent_on_it, ":belfry_scene_prop_id", ":agent_id"),
            (neg|scene_prop_has_agent_on_it, ":belfry_platform_a_scene_prop_id", ":agent_id"),

            (this_or_next|eq, ":belfry_kind", 1), #there is this_or_next here because belfry_b has no platform_b
            (neg|scene_prop_has_agent_on_it, ":belfry_platform_b_scene_prop_id", ":agent_id"),

            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_1_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_2_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_3_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|position_is_behind_position, pos2, pos19),
            (position_is_behind_position, pos2, pos1),
            (val_add, ":number_of_agents_around_belfry", 1),
          (try_end),

          (val_min, ":number_of_agents_around_belfry", 16),

          (try_begin),
            (scene_prop_get_slot, ":pre_number_of_agents_around_belfry", ":belfry_scene_prop_id", "slot_scene_prop_number_of_agents_pushing"),
            (scene_prop_get_slot, ":next_entry_point_id", ":belfry_scene_prop_id", "slot_scene_prop_next_entry_point_id"),
            (this_or_next|neq, ":pre_number_of_agents_around_belfry", ":number_of_agents_around_belfry"),
            (neq, ":next_entry_point_id", ":belfry_next_entry_point_id"),

            (try_begin),
              (eq, ":next_entry_point_id", ":belfry_next_entry_point_id"), #if we are still targetting same entry point subtract
              (prop_instance_is_animating, ":is_animating", ":belfry_scene_prop_id"),
              (eq, ":is_animating", 1),

              (store_mul, ":sqrt_number_of_agents_around_belfry", "$g_last_number_of_agents_around_belfry", 100),
              (store_sqrt, ":sqrt_number_of_agents_around_belfry", ":sqrt_number_of_agents_around_belfry"),
              (val_min, ":sqrt_number_of_agents_around_belfry", 300),
              (assign, ":distance", ":belfry_next_entry_point_distance"),
              (val_mul, ":distance", ":sqrt_number_of_agents_around_belfry"),
              (val_div, ":distance", 100), #100 is because of fixed_point_multiplier
              (val_mul, ":distance", 4), #multiplying with 4 to make belfry pushing process slower,
                                                                 #with 16 agents belfry will go with 4 / 4 = 1 speed (max), with 1 agent belfry will go with 1 / 4 = 0.25 speed (min)
            (try_end),

            (try_begin),
              (ge, ":belfry_next_entry_point_id", 0),

              #up down rotation of belfry's next entry point
              (init_position, pos9),
              (position_set_y, pos9, -500), #go 5.0 meters back
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9),
              (position_get_distance_to_terrain, ":height_to_terrain_1", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at left part of belfry

              (init_position, pos9),
              (position_set_y, pos9, -500), #go 5.0 meters back
              (position_set_x, pos9, 300), #go 3.0 meters right
              (position_transform_position_to_parent, pos10, pos5, pos9),
              (position_get_distance_to_terrain, ":height_to_terrain_2", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at right part of belfry

              (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),
              (val_mul, ":height_to_terrain", 100), #because of fixed point multiplier

              (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 2 degrees. #ac sonra
              (init_position, pos20),
              (position_rotate_x_floating, pos20, ":rotate_angle_of_next_entry_point"),
              (position_transform_position_to_parent, pos23, pos5, pos20),

              #right left rotation of belfry's next entry point
              (init_position, pos9),
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
              (init_position, pos9),
              (position_set_x, pos9, 300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
              (store_sub, ":height_to_terrain_1", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

              (init_position, pos9),
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_set_y, pos9, -500), #go 5.0 meters forward
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
              (init_position, pos9),
              (position_set_x, pos9, 300), #go 3.0 meters left
              (position_set_y, pos9, -500), #go 5.0 meters forward
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
              (store_sub, ":height_to_terrain_2", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

              (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),
              (val_mul, ":height_to_terrain", 100), #100 is because of fixed_point_multiplier
              (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 25 degrees.
              (val_mul, ":rotate_angle_of_next_entry_point", -1),

              (init_position, pos20),
              (position_rotate_y_floating, pos20, ":rotate_angle_of_next_entry_point"),
              (position_transform_position_to_parent, pos22, pos23, pos20),
            (else_try),
              (copy_position, pos22, pos5),
            (try_end),

            (try_begin),
              (ge, ":number_of_agents_around_belfry", 1), #if there is any agents pushing belfry

              (store_mul, ":sqrt_number_of_agents_around_belfry", ":number_of_agents_around_belfry", 100),
              (store_sqrt, ":sqrt_number_of_agents_around_belfry", ":sqrt_number_of_agents_around_belfry"),
              (val_min, ":sqrt_number_of_agents_around_belfry", 300),
              (val_mul, ":belfry_next_entry_point_distance", 100), #100 is because of fixed_point_multiplier
              (val_mul, ":belfry_next_entry_point_distance", 3), #multiplying with 3 to make belfry pushing process slower,
                                                                 #with 9 agents belfry will go with 3 / 3 = 1 speed (max), with 1 agent belfry will go with 1 / 3 = 0.33 speed (min)
              (val_div, ":belfry_next_entry_point_distance", ":sqrt_number_of_agents_around_belfry"),
              #calculating destination coordinates of belfry parts
              #belfry platform_a
              (prop_instance_get_position, pos6, ":belfry_platform_a_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos1, pos6),
              (position_transform_position_to_parent, pos8, pos22, pos7),
              (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos8, ":belfry_next_entry_point_distance"),
              #belfry platform_b
              (try_begin),
                (eq, ":belfry_kind", 0),
                (prop_instance_get_position, pos6, ":belfry_platform_b_scene_prop_id"),
                (position_transform_position_to_local, pos7, pos1, pos6),
                (position_transform_position_to_parent, pos8, pos22, pos7),
                (prop_instance_animate_to_position, ":belfry_platform_b_scene_prop_id", pos8, ":belfry_next_entry_point_distance"),
              (try_end),
              #wheel rotation
              (store_mul, ":belfry_wheel_rotation", ":belfry_next_entry_point_distance", -25),
              #(val_add, "$g_belfry_wheel_rotation", ":belfry_wheel_rotation"),
              (assign, "$g_last_number_of_agents_around_belfry", ":number_of_agents_around_belfry"),

              #belfry wheel_1
              #(prop_instance_get_starting_position, pos13, ":belfry_wheel_1_scene_prop_id"),
              (prop_instance_get_position, pos13, ":belfry_wheel_1_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_1_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),

              #belfry wheel_2
              #(prop_instance_get_starting_position, pos13, ":belfry_wheel_2_scene_prop_id"),
              (prop_instance_get_position, pos13, ":belfry_wheel_2_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_2_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),

              #belfry wheel_3
              (prop_instance_get_position, pos13, ":belfry_wheel_3_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_3_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),

              #belfry main body
              (prop_instance_animate_to_position, ":belfry_scene_prop_id", pos22, ":belfry_next_entry_point_distance"),
            (else_try),
              (prop_instance_is_animating, ":is_animating", ":belfry_scene_prop_id"),
              (eq, ":is_animating", 1),

              #belfry platform_a
              (prop_instance_stop_animating, ":belfry_platform_a_scene_prop_id"),
              #belfry platform_b
              (try_begin),
                (eq, ":belfry_kind", 0),
                (prop_instance_stop_animating, ":belfry_platform_b_scene_prop_id"),
              (try_end),
              #belfry wheel_1
              (prop_instance_stop_animating, ":belfry_wheel_1_scene_prop_id"),
              #belfry wheel_2
              (prop_instance_stop_animating, ":belfry_wheel_2_scene_prop_id"),
              #belfry wheel_3
              (prop_instance_stop_animating, ":belfry_wheel_3_scene_prop_id"),
              #belfry main body
              (prop_instance_stop_animating, ":belfry_scene_prop_id"),
            (try_end),

            (scene_prop_set_slot, ":belfry_scene_prop_id", "slot_scene_prop_number_of_agents_pushing", ":number_of_agents_around_belfry"),
            (scene_prop_set_slot, ":belfry_scene_prop_id", "slot_scene_prop_next_entry_point_id", ":belfry_next_entry_point_id"),
          (try_end),
        (else_try),
          (le, ":dist_between_belfry_and_its_destination", 4),
          (scene_prop_slot_eq, ":belfry_scene_prop_id", "slot_scene_prop_belfry_platform_moved", 0),

          (scene_prop_set_slot, ":belfry_scene_prop_id", "slot_scene_prop_belfry_platform_moved", 1),

          (try_begin),
            (eq, ":belfry_kind", 0),
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
          (else_try),
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
          (try_end),

          (prop_instance_get_starting_position, pos0, ":belfry_platform_a_scene_prop_id"),
          (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos0, 400),
        (try_end),
      (try_end),
    (try_end),
    ])

multiplayer_server_spawn_bots = (
  0, 0, 0, [
           ],
  [

          (multiplayer_is_server),
    (eq, "$g_multiplayer_ready_for_spawning_agent", 1),
    (store_add, ":total_req", "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_required_team_2"), #aqui suma todos los bots
    (try_begin),
      (gt, ":total_req", 0),

      (try_begin),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),

        (team_get_score, ":team_1_score", 0),
        (team_get_score, ":team_2_score", 1),

        (store_add, ":current_round", ":team_1_score", ":team_2_score"),
        (eq, ":current_round", 0),

        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),
        (lt, ":round_time", 20),

        (assign, ":rounded_game_first_round_time_limit_past", 0),
      (else_try),
        (assign, ":rounded_game_first_round_time_limit_past", 1),
      (try_end),

      (eq, ":rounded_game_first_round_time_limit_past", 1),

      (store_random_in_range, ":random_req", 0, ":total_req"),
      (val_sub, ":random_req", "$g_multiplayer_num_bots_required_team_1"),
      (try_begin),
        (lt, ":random_req", 0),
        #add to team 1
        (assign, ":selected_team", 0),
      (else_try),
        #add to team 2
        (assign, ":selected_team", 1),
      (try_end),

      (try_begin),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),

        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),

        (try_begin),
          (le, ":round_time", 20),
          (assign, ":look_only_actives", 0),
        (else_try),
          (assign, ":look_only_actives", 1),
        (try_end),
      (else_try),
        (assign, ":look_only_actives", 1),
      (try_end),

      (call_script, "script_multiplayer_find_bot_troop_and_group_for_spawn", ":selected_team", ":look_only_actives"),
      (assign, ":selected_troop", reg0),
      (assign, ":selected_group", reg1),

      (team_get_faction, ":team_faction", ":selected_team"),
      (assign, ":num_ai_troops", 0),
      (try_for_range, ":cur_ai_troop", multiplayer_ai_troops_begin, multiplayer_ai_troops_end),
        (store_troop_faction, ":ai_troop_faction", ":cur_ai_troop"),
        (eq, ":ai_troop_faction", ":team_faction"),
        (val_add, ":num_ai_troops", 1),
      (try_end),

      (assign, ":number_of_active_players_wanted_bot", 0),

      (get_max_players, ":num_players"),
      (try_for_range, ":player_no", 0, ":num_players"),
        (player_is_active, ":player_no"),
        (player_get_team_no, ":player_team_no", ":player_no"),
        (eq, ":selected_team", ":player_team_no"),

        (assign, ":ai_wanted", 0),
        (store_add, ":end_cond", "slot_player_bot_type_1_wanted", ":num_ai_troops"),
        (try_for_range, ":bot_type_wanted_slot", "slot_player_bot_type_1_wanted", ":end_cond"),
          (player_slot_ge, ":player_no", ":bot_type_wanted_slot", 1),
          (assign, ":ai_wanted", 1),
          (assign, ":end_cond", 0),
        (try_end),

        (ge, ":ai_wanted", 1),

        (val_add, ":number_of_active_players_wanted_bot", 1),
      (try_end),

      (try_begin),
        (this_or_next|ge, ":selected_group", 0),
        (eq, ":number_of_active_players_wanted_bot", 0),

        (troop_get_inventory_slot, ":has_item", ":selected_troop", ek_horse),
        (try_begin),
          (ge, ":has_item", 0),
          (assign, ":is_horseman", 1),
        (else_try),
          (assign, ":is_horseman", 0),
        (try_end),

        (try_begin),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),

          (store_mission_timer_a, ":round_time"),
          (val_sub, ":round_time", "$g_round_start_time"),

          (try_begin),
            (lt, ":round_time", 20), #at start of game spawn at base entry point
            (try_begin),
              (eq, ":selected_team", 0),
              (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 1, ":is_horseman"),
            (else_try),
              (assign, reg0, multi_initial_spawn_point_team_2),
            (try_end),
          (else_try),
            (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 0, ":is_horseman"),
          (try_end),
        (else_try),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),

          (try_begin),
            (eq, ":selected_team", 0),
            (assign, reg0, 0),
          (else_try),
            (assign, reg0, 32),
          (try_end),

        (else_try),
          (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 0, ":is_horseman"),
        (try_end),

        (store_current_scene, ":cur_scene"),
        (modify_visitors_at_site, ":cur_scene"),
        (add_visitors_to_current_scene, reg0, ":selected_troop", 1, ":selected_team", ":selected_group"),
        (assign, "$g_multiplayer_ready_for_spawning_agent", 0),

        (try_begin),
          (eq, ":selected_team", 0),
          (val_sub, "$g_multiplayer_num_bots_required_team_1", 1),
        (else_try),
          (eq, ":selected_team", 1),
          (val_sub, "$g_multiplayer_num_bots_required_team_2", 1),
        (try_end),
      (try_end),
    (try_end),
    ])

###chief capitan cuando es el modo de batalla de lords
multiplayer_server_spawn_bots2 = (
  0, 0, 0, [#(eq, "$g_round_tropas", 1), #chief capitan
           ],
  [
         (multiplayer_is_server),
         (eq, "$g_round_tropas", 2), #chief capitan
      (try_begin),
         (eq, "$g_multiplayer_ready_for_spawning_agent", 1),
         (try_begin),
        (team_get_score, ":team_1_score", 0),
        (team_get_score, ":team_2_score", 1),

        (store_add, ":current_round", ":team_1_score", ":team_2_score"),
        (eq, ":current_round", 0),

        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),
        (lt, ":round_time", 20),

        (assign, ":rounded_game_first_round_time_limit_past", 0),
      (else_try),
        (assign, ":rounded_game_first_round_time_limit_past", 1),
      (try_end),
      (try_begin),

      (eq, ":rounded_game_first_round_time_limit_past", 1),

         (get_max_players, ":num_players"),
         (try_for_range, ":player", 0, ":num_players"),

#      (multiplayer_get_my_player, ":player"),
            (player_is_active, ":player"),
           (neg|player_is_busy_with_menus, ":player"),
          (multiplayer_get_my_troop, ":troop_no"),
        (player_get_team_no, ":player_team_no", ":player"),

          (player_get_slot, ":basic_dinero", ":player", "slot_agent_dinerotropas"),
             (try_begin), #chief capitan
                  (eq, ":basic_dinero", 1),

##           (player_get_gold, ":player_gold", ":player_no"),
         (assign, ":per_round_gold_addition", 1000),

                  (try_begin), #chief capitan
           (eq, ":player_team_no", 0),
         (val_mul, ":per_round_gold_addition", "$g_multiplayer_battle_earnings_multiplier"),
         (val_div, ":per_round_gold_addition", 100),
             (assign, ":player_gold", ":per_round_gold_addition"),
              (else_try),
           (eq, ":player_team_no", 1),
         (val_mul, ":per_round_gold_addition", "$g_multiplayer_round_earnings_multiplier"),
         (val_div, ":per_round_gold_addition", 100),
             (assign, ":player_gold", ":per_round_gold_addition"),
                (try_end), #chief capitan acaba
           (player_set_gold, ":player", ":player_gold", multi_max_gold_that_can_be_stored),
                 (player_set_slot, ":player", "slot_agent_dinerotropas", 0),
                (try_end), #chief capitan acaba

          (player_get_gold, ":player_gold", ":player"), #chief capitan
       (neq, ":troop_no", "trp_tropa1"),
       (neq, ":troop_no", "trp_tropa2"),
       (neq, ":troop_no", "trp_tropa3"),
       (neq, ":troop_no", "trp_tropa4"),
       (neq, ":troop_no", "trp_tropa5"),
       (neq, ":troop_no", "trp_tropa6"),
       (neq, ":troop_no", "trp_tropa7"),
       (neq, ":troop_no", "trp_tropa8"),
       (neq, ":troop_no", "trp_tropa9"),
       (neq, ":troop_no", "trp_tropa10"),
       (neq, ":troop_no", "trp_tropa11"),
       (neq, ":troop_no", "trp_tropa12"),
       (neq, ":troop_no", "trp_tropa13"),
       (neq, ":troop_no", "trp_tropa14"),
       (neq, ":troop_no", "trp_tropa15"),
       (neq, ":troop_no", "trp_tropa16"),
       (neq, ":troop_no", "trp_tropa17"),
       (neq, ":troop_no", "trp_tropa18"),
       (neq, ":troop_no", "trp_tropa19"),
       (neq, ":troop_no", "trp_tropa20"),
       (neq, ":troop_no", "trp_tropa21"),
       (neq, ":troop_no", "trp_tropa22"),
       (neq, ":troop_no", "trp_tropa23"),
       (neq, ":troop_no", "trp_tropa24"),
       (neq, ":troop_no", "trp_tropa25"),
       (neq, ":troop_no", "trp_tropa26"),
       (neq, ":troop_no", "trp_tropa27"),
       (neq, ":troop_no", "trp_tropa28"),
       (neq, ":troop_no", "trp_tropa29"),
       (neq, ":troop_no", "trp_tropa30"),
       (neq, ":troop_no", "trp_tropa32"),

    (store_add, ":total_req", "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_required_team_2"),
      (store_random_in_range, ":random_req", 0, ":total_req"),
      (val_sub, ":random_req", "$g_multiplayer_num_bots_required_team_1"),

      (try_begin), #EQUIPO 1 EMpieza
        (eq, ":player_team_no", 0),
          (gt, ":player_gold", 250), #chief capitan #si la suma de todos esta por encima de 0, sigue en tigger hasta que se agoten los bots. Podemos poner aqui que para el player sin dinero tampoco continue
        (lt, ":random_req", 0),

        (assign, ":selected_team", 0), #EQUIPO 1

      (try_begin),
        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),

        (try_begin),
          (le, ":round_time", 20),
          (assign, ":look_only_actives", 0),
        (else_try),
          (assign, ":look_only_actives", 1),
        (try_end),
      (else_try),
        (assign, ":look_only_actives", 1),
      (try_end),

      (call_script, "script_multiplayer_find_bot_troop_and_group_for_spawn", ":selected_team", ":look_only_actives"),
      (assign, ":selected_troop", reg0),
      (assign, ":selected_group", reg1),

      (team_get_faction, ":team_faction", ":selected_team"),
      (assign, ":num_ai_troops", 0),
      (try_for_range, ":cur_ai_troop", multiplayer_ai_troops_begin, multiplayer_ai_troops_end),
        (store_troop_faction, ":ai_troop_faction", ":cur_ai_troop"),
        (eq, ":ai_troop_faction", ":team_faction"),
        (val_add, ":num_ai_troops", 1),
      (try_end),

      (assign, ":number_of_active_players_wanted_bot", 0),


       (assign, ":unidad_cost", 50), #chief capitan
                # (player_set_slot, ":player_no", "slot_agent_dinerotropas", ":player_gold"),
        # (player_slot_ge, ":player_no", "slot_agent_dinerotropas", 250),

      (try_begin),
        (eq, ":selected_team", 0),
        (assign, ":ai_wanted", 0),
        (store_add, ":end_cond", "slot_player_bot_type_1_wanted", ":num_ai_troops"),
        (try_for_range, ":bot_type_wanted_slot", "slot_player_bot_type_1_wanted", ":end_cond"),
          (player_slot_ge, ":player", ":bot_type_wanted_slot", 1),
          (assign, ":ai_wanted", 1),
          (assign, ":end_cond", 0),
        (try_end),

    #  (try_begin),
        (ge, ":ai_wanted", 1),

        (val_add, ":number_of_active_players_wanted_bot", 1),
      (try_end),
      (try_begin),
       (neq, ":number_of_active_players_wanted_bot", 0),

            (store_random_in_range, reg0, 0, 2), #EQUIPO 1
##          (else_try),
##            (store_random_in_range, reg0, 32, 34),
##          (try_end),

        (store_current_scene, ":cur_scene"),
        (modify_visitors_at_site, ":cur_scene"),
        (add_visitors_to_current_scene, reg0, ":selected_troop", 1, ":selected_team", ":selected_group"),
        (assign, "$g_multiplayer_ready_for_spawning_agent", 0),
#        (try_end),

        (troop_get_inventory_slot, ":has_item", ":selected_troop", ek_horse),
        (try_begin),
          (ge, ":has_item", 0),
        #  (assign, ":is_horseman", 1),
       (val_add, ":unidad_cost", 50), #chief capitan
        (else_try),
      (val_add, ":unidad_cost", 1), #chief capitan
        #  (assign, ":is_horseman", 0),
        (try_end),

#chief capitan para tropas de nivel alto
        (store_character_level, ":troop_level", ":selected_troop"),
        (try_begin),
        (gt, ":troop_level", 21),
       (val_add, ":unidad_cost", 50), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 25),
       (val_add, ":unidad_cost", 20), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 26),
       (val_add, ":unidad_cost", 20), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 27),
       (val_add, ":unidad_cost", 30), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 28),
       (val_add, ":unidad_cost", 30), #chief capitan
        (try_end), #chief capitan

        (try_begin), #equipo 1
          (val_sub, "$g_multiplayer_num_bots_required_team_1", 1), #aqui se va restando un bot cada vez que spawn, quizas podemos poner otro limite en el dinero del player
          (val_sub, ":player_gold", ":unidad_cost"), #chief capitan
         (player_set_gold, ":player", ":player_gold", multi_max_gold_that_can_be_stored),
       (try_end),
    (try_end),

        (else_try), #EQUIPO 2
        (eq, ":player_team_no", 1),
          (gt, ":player_gold", 250), #chief capitan #si la suma de todos esta por encima de 0, sigue en tigger hasta que se agoten los bots. Podemos poner aqui que para el player sin dinero tampoco continue
        (gt, ":random_req", 0),
        (assign, ":selected_team", 1), #EQUIPO 2

      (try_begin),
        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),

        (try_begin),
          (le, ":round_time", 20),
          (assign, ":look_only_actives", 0),
        (else_try),
          (assign, ":look_only_actives", 1),
        (try_end),
      (else_try),
        (assign, ":look_only_actives", 1),
      (try_end),

      (call_script, "script_multiplayer_find_bot_troop_and_group_for_spawn", ":selected_team", ":look_only_actives"),
      (assign, ":selected_troop", reg0),
      (assign, ":selected_group", reg1),

      (team_get_faction, ":team_faction", ":selected_team"),
      (assign, ":num_ai_troops", 0),
      (try_for_range, ":cur_ai_troop", multiplayer_ai_troops_begin, multiplayer_ai_troops_end),
        (store_troop_faction, ":ai_troop_faction", ":cur_ai_troop"),
        (eq, ":ai_troop_faction", ":team_faction"),
        (val_add, ":num_ai_troops", 1),
      (try_end),

      (assign, ":number_of_active_players_wanted_bot", 0),


       (assign, ":unidad_cost", 50), #chief capitan

      (try_begin),
        (eq, ":selected_team", 1), #team2 equipo 2
        (assign, ":ai_wanted", 0),
        (store_add, ":end_cond", "slot_player_bot_type_1_wanted", ":num_ai_troops"),
        (try_for_range, ":bot_type_wanted_slot", "slot_player_bot_type_1_wanted", ":end_cond"),
          (player_slot_ge, ":player", ":bot_type_wanted_slot", 1),
          (assign, ":ai_wanted", 1),
          (assign, ":end_cond", 0),
        (try_end),

        (ge, ":ai_wanted", 1),

        (val_add, ":number_of_active_players_wanted_bot", 1),
      (try_end),
      (try_begin),
       (neq, ":number_of_active_players_wanted_bot", 0),

            (store_random_in_range, reg0, 32, 34), #equipo 2

        (store_current_scene, ":cur_scene"),
        (modify_visitors_at_site, ":cur_scene"),
        (add_visitors_to_current_scene, reg0, ":selected_troop", 1, ":selected_team", ":selected_group"),
        (assign, "$g_multiplayer_ready_for_spawning_agent", 0),

        (troop_get_inventory_slot, ":has_item", ":selected_troop", ek_horse),
        (try_begin),
          (ge, ":has_item", 0),
       (val_add, ":unidad_cost", 50), #chief capitan
        (else_try),
      (val_add, ":unidad_cost", 1), #chief capitan
        (try_end),

#chief capitan para tropas de nivel alto
        (store_character_level, ":troop_level", ":selected_troop"),
        (try_begin),
        (gt, ":troop_level", 21),
       (val_add, ":unidad_cost", 50), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 25),
       (val_add, ":unidad_cost", 20), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 26),
       (val_add, ":unidad_cost", 20), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 27),
       (val_add, ":unidad_cost", 30), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 28),
       (val_add, ":unidad_cost", 30), #chief capitan
        (try_end), #chief capitan

        (try_begin), #equipo 2
          (val_sub, "$g_multiplayer_num_bots_required_team_2", 1),
         (val_sub, ":player_gold", ":unidad_cost"), #chief capitan
         (player_set_gold, ":player", ":player_gold", multi_max_gold_that_can_be_stored),
       (try_end),
    (try_end),

      (try_end), #chief capitan
      (try_end), #chief capitan
      (try_end), #chief capitan
      (try_end), #chief capitan
    ])




multiplayer_server_manage_bots = (
  3, 0, 0, [],
  [
    (multiplayer_is_server),
    (try_for_agents, ":cur_agent"),
      (agent_is_non_player, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
      (agent_is_alive, ":cur_agent"),
      (agent_get_group, ":agent_group", ":cur_agent"),
      (try_begin),
        (neg|player_is_active, ":agent_group"),
        (call_script, "script_multiplayer_change_leader_of_bot", ":cur_agent"),
      (else_try),
        (player_get_team_no, ":leader_team_no", ":agent_group"),
        (agent_get_team, ":agent_team", ":cur_agent"),
        (neq, ":leader_team_no", ":agent_team"),
        (call_script, "script_multiplayer_change_leader_of_bot", ":cur_agent"),
      (try_end),
    (try_end),
    ])

multiplayer_server_check_polls = (
  1, 5, 0,
  [
    (multiplayer_is_server),
    (eq, "$g_multiplayer_poll_running", 1),
    (eq, "$g_multiplayer_poll_ended", 0),
    (store_mission_timer_a, ":mission_timer"),
    (store_add, ":total_votes", "$g_multiplayer_poll_no_count", "$g_multiplayer_poll_yes_count"),
    (this_or_next|eq, ":total_votes", "$g_multiplayer_poll_num_sent"),
    (gt, ":mission_timer", "$g_multiplayer_poll_end_time"),
    (call_script, "script_cf_multiplayer_evaluate_poll"),
    ],
  [
    (assign, "$g_multiplayer_poll_running", 0),
    (try_begin),
      (this_or_next|eq, "$g_multiplayer_poll_to_show", 0), #change map
      (eq, "$g_multiplayer_poll_to_show", 3), #change map with factions
      (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
      (start_multiplayer_mission, reg0, "$g_multiplayer_poll_value_to_show", 1),
      (call_script, "script_game_set_multiplayer_mission_end"),
    (try_end),
    ])

multiplayer_server_check_end_map = (
  1, 0, 0, [],
  [
    (multiplayer_is_server),
    #checking for restarting the map
    (assign, ":end_map", 0),
    (try_begin),
      (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
      (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_lords_battle), #chief capitan
      (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
      (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),

      (try_begin),
        (eq, "$g_round_ended", 1),

        (store_mission_timer_a, ":seconds_past_till_round_ended"),
        (val_sub, ":seconds_past_till_round_ended", "$g_round_finish_time"),
        (store_sub, ":multiplayer_respawn_period_minus_one", "$g_multiplayer_respawn_period", 1),
        (ge, ":seconds_past_till_round_ended", ":multiplayer_respawn_period_minus_one"),

        (store_mission_timer_a, ":mission_timer"),
        (try_begin),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_lords_battle), #chief capitan
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
          (assign, ":reduce_amount", 90),
        (else_try),
          (assign, ":reduce_amount", 120),
        (try_end),

        (store_mul, ":game_max_seconds", "$g_multiplayer_game_max_minutes", 60),
        (store_sub, ":game_max_seconds_min_n_seconds", ":game_max_seconds", ":reduce_amount"), #when round ends if there are 60 seconds to map change time then change map without completing exact map time.
        (gt, ":mission_timer", ":game_max_seconds_min_n_seconds"),
        (assign, ":end_map", 1),
      (try_end),

      (eq, ":end_map", 1),
    (else_try),
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_battle), #battle mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_lords_battle), #chief capitan
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy), #fight and destroy mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_siege), #siege mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #in headquarters mod game cannot limited by time, only can be limited by score.
      (store_mission_timer_a, ":mission_timer"),
      (store_mul, ":game_max_seconds", "$g_multiplayer_game_max_minutes", 60),
      (gt, ":mission_timer", ":game_max_seconds"),
      (assign, ":end_map", 1),
    (else_try),
      #assuming only 2 teams in scene
      (team_get_score, ":team_1_score", 0),
      (team_get_score, ":team_2_score", 1),
      (try_begin),
        (neq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #for not-headquarters mods
        (try_begin),
          (this_or_next|ge, ":team_1_score", "$g_multiplayer_game_max_points"),
          (ge, ":team_2_score", "$g_multiplayer_game_max_points"),
          (assign, ":end_map", 1),
        (try_end),
      (else_try),
        (assign, ":at_least_one_player_is_at_game", 0),
        (get_max_players, ":num_players"),
        (try_for_range, ":player_no", 0, ":num_players"),
          (player_is_active, ":player_no"),
          (player_get_agent_id, ":agent_id", ":player_no"),
          (ge, ":agent_id", 0),
          (neg|agent_is_non_player, ":agent_id"),
          (assign, ":at_least_one_player_is_at_game", 1),
          (assign, ":num_players", 0),
        (try_end),

        (eq, ":at_least_one_player_is_at_game", 1),

        (this_or_next|le, ":team_1_score", 0), #in headquarters game ends only if one team has 0 score.
        (le, ":team_2_score", 0),
        (assign, ":end_map", 1),
      (try_end),
    (try_end),
    (try_begin),
      (eq, ":end_map", 1),
      (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
      (start_multiplayer_mission, reg0, "$g_multiplayer_selected_map", 0),
      (call_script, "script_game_set_multiplayer_mission_end"),
    (try_end),
    ])

multiplayer_once_at_the_first_frame = (
  0, 0, ti_once, [], [
    (start_presentation, "prsnt_multiplayer_welcome_message"),
       (play_sound, "snd_marchingdrums", 1), #multiplayer chief sonido efectua sonido de empiece
    ])

multiplayer_battle_window_opened = (
  ti_battle_window_opened, 0, 0, [], [
    (start_presentation, "prsnt_multiplayer_team_score_display"),
    ])

###multiplayer chief
multi_battle_mode_triggers3 = [
mp_shield_bash_1,
mp_shield_bash_2,
banner_heal_multi,
siege_multi_items,
multi_warcry,
hunt_taunting,
rain_multi,
#multiplayer_critical_strike,
respiracion_moribunda,
sistema_fatiga_multi,
recupera_fatiga_multi,
suma_fatigue_multi,
resta_fatigue_porcorrer_multi,
resta_fatigue_multi,
]
