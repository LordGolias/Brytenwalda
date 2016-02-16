from ..header_operations import *
from ..header_common import s3
from ..header_skills import *
from ..header_troops import *
from ..header_game_menus import mnf_disable_all_keys

from source.header_dialogs import anyone, plyr, auto_proceed

from ..module_constants import *

from source.lazy_flag import LazyFlag


menu = (
    "tutorial", mnf_disable_all_keys,
    "You approach a field where the locals are training with weapons. You can "
    "practice here to improve your combat skills.",
    "none", [
        (try_begin),
            (eq, "$g_tutorial_entered", 1),
            (change_screen_quit),
        (else_try),
            (set_passage_menu, "mnu_tutorial"),
            (assign, "$g_tutorial_entered", 1),
        (try_end),
    ], [
        ("continue", [], "Continue...", [
            (modify_visitors_at_site, "scn_tutorial_training_ground"),
            (reset_visitors, 0),
            (set_player_troop, "trp_player"),
            (assign, "$g_player_troop", "trp_player"),
            (troop_raise_attribute, "$g_player_troop", ca_strength, 12),
            (troop_raise_attribute, "$g_player_troop", ca_agility, 9),
            (troop_raise_attribute, "$g_player_troop", ca_charisma, 5),
            (troop_raise_skill, "$g_player_troop", skl_shield, 3),
            (troop_raise_skill, "$g_player_troop", skl_athletics, 2),
            (troop_raise_skill, "$g_player_troop", skl_riding, 3),
            (troop_raise_skill, "$g_player_troop", skl_power_strike, 1),
            (troop_raise_skill, "$g_player_troop", skl_power_draw, 5),
            (troop_raise_skill, "$g_player_troop", skl_weapon_master, 4),
            (troop_raise_skill, "$g_player_troop", skl_ironflesh, 1),
            (troop_raise_skill, "$g_player_troop", skl_horse_archery, 6),
            (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 70),
            (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 70),
            (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 70),
            (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 70),
            (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 70),

            (troop_clear_inventory, "$g_player_troop"),
            (troop_add_item, "$g_player_troop", "itm_leather_tunic1", 0),
            (troop_add_item, "$g_player_troop", ARENA_FOOTWEAR, 0),
            (troop_add_item, "$g_player_troop", "itm_practice_sword", 0),
            (troop_add_item, "$g_player_troop", "itm_quarter_staff", 0),
            (troop_equip_items, "$g_player_troop"),
            (set_visitor, 0, "trp_player"),
            (set_visitor, 32, "trp_tutorial_fighter_1"),
            (set_visitor, 33, "trp_tutorial_fighter_2"),
            (set_visitor, 34, "trp_tutorial_fighter_3"),
            (set_visitor, 35, "trp_tutorial_fighter_4"),
            (set_visitor, 40, "trp_tutorial_master_archer"),
            (set_visitor, 41, "trp_tutorial_archer_1"),
            (set_visitor, 42, "trp_tutorial_archer_1"),
            (set_visitor, 60, "trp_tutorial_master_horseman"),
            (set_visitor, 61, "trp_tutorial_rider_1"),
            (set_visitor, 62, "trp_tutorial_rider_1"),
            (set_visitor, 63, "trp_tutorial_rider_2"),
            (set_visitor, 64, "trp_tutorial_rider_2"),
            (set_jump_mission, "mt_tutorial_training_ground"),
            (jump_to_scene, "scn_tutorial_training_ground"),
            (change_screen_mission),
        ]),

        ("go_back_dot", [], "Go back.", [(change_screen_quit)]),
    ]
)


dialogs = [
    [anyone, "start", [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
        (eq, "$g_tutorial_training_ground_conversation_state", 0),
        (eq, "$g_tutorial_fighter_talk_before", 0)],
     "Hello there. We are polishing off our combat skills here with a bit of "
     "sparring practice. You look like you could use a bit of training. Why "
     "don't you join us, and we can show you a few tricks. And if you need "
     "explanation of any combat concepts, just ask, and I will do my best to "
     "fill you in.", "fighter_talk", [

         (try_begin),
             (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
             (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
             (tutorial_message, -1),
         (try_end),
         (assign, "$g_tutorial_fighter_talk_before", 1)
     ]],

    [anyone, "start", [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
        (eq, "$g_tutorial_training_ground_conversation_state", 0)],
     "What do you want to practice?", "fighter_talk", []
     ],

    [anyone, "fighter_pretalk", [],
     "Tell me what kind of practice you want.", "fighter_talk", []
     ],

    [anyone | plyr, "fighter_talk", [],
     "I want to practice attacking.", "fighter_talk_train_attack", []
     ],

    [anyone | plyr, "fighter_talk", [],
     "I want to practice blocking with my weapon.", "fighter_talk_train_parry", []
     ],

    [anyone | plyr, "fighter_talk", [],
     "Let's do some sparring practice.", "fighter_talk_train_combat", []
     ],

    [anyone | plyr, "fighter_talk", [],
     "[Leave]", "close_window", []
     ],

    [anyone, "fighter_talk_train_attack", [
        (get_player_agent_no, ":player_agent"),
        (agent_has_item_equipped, ":player_agent", "itm_practice_sword"),
        # todo: add other melee weapons
    ],
     "All right. There are four principle directions for attacking. These are "
     "overhead swing, right swing, left swing and thrust. Now, I will tell you "
     "which direction to attack from and you must try to do the correct attack."
     "^^(Move your mouse while you press the left mouse button to specify "
     "attack direction. For example, to execute an overhead attack, move the "
     "mouse up at the instant you press the left mouse button. The icons on "
     "your screen will help you do the correct action.)",
     "fighter_talk_train_attack_2", []
     ],

    [anyone | plyr, "fighter_talk_train_attack_2", [],
     "Let's begin then. I am ready.", "close_window", [
         (assign, "$g_tutorial_training_ground_melee_trainer_attack", "$g_talk_troop"),
         (assign, "$g_tutorial_training_ground_melee_state", 0),
         (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
         (assign, "$g_tutorial_training_ground_current_score", 0),
         (assign, "$g_tutorial_training_ground_current_score_2", 0),
         (assign, "$g_tutorial_update_mouse_presentation", 0),
     ]],

  [anyone|plyr, "fighter_talk_train_attack_2",  [],
   "Actually I want to do something else.", "fighter_pretalk", []
   ],

  [anyone, "fighter_talk_train_attack",
   [(str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon")],
   "{!}{s3}", "close_window", []
   ],

    [anyone, "fighter_talk_train_parry", [
        (get_player_agent_no, ":player_agent"),
        (agent_has_item_equipped, ":player_agent", "itm_practice_sword"),
        # TODO: add other melee weapons
    ],
     "Unlike a shield, blocking with a weapon can only stop attacks coming "
     "from one direction. For example if you block up, you'll deflect overhead "
     "attacks, but you can still be hit by side swings or thrust attacks. "
     "^^(You must press and hold down the right mouse button to block.)",
     "fighter_talk_train_parry_2", []
     ],

    [anyone, "fighter_talk_train_parry_2", [],
     "I'll now attack you with different types of strokes, and I will wait "
     "until you do the correct block before attacking. Try to do the correct "
     "block as soon as you can. ^^(This practice is easy to do with the "
     "'automatic block direction' setting which is the default. If you go "
     "to the Options menu and change defend direction control to "
     "'mouse movement' or 'keyboard', you'll need to manually choose "
     "block direction. This is much more challenging, but makes the game "
     "much more interesting. This practice can be very useful if you "
     "use manual blocking.)",
     "fighter_talk_train_parry_3", []
     ],

    [anyone | plyr, "fighter_talk_train_parry_3", [],
     "Let's begin then. I am ready.", "close_window", [
         (assign, "$g_tutorial_training_ground_melee_trainer_parry", "$g_talk_troop"),
         (assign, "$g_tutorial_training_ground_melee_state", 0),
         (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
         (assign, "$g_tutorial_training_ground_current_score", 0),
     ]],

    [anyone | plyr, "fighter_talk_train_parry_3", [],
     "Actually I want to do something else.", "fighter_pretalk", []
     ],

    [anyone, "fighter_talk_train_parry", [
        (str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon")
    ],
     "{!}{s3}", "close_window", []
     ],

    [anyone, "fighter_talk_train_combat", [
         (get_player_agent_no, ":player_agent"),
         (agent_has_item_equipped, ":player_agent", "itm_practice_sword"),
         # TODO: add other melee weapons
     ],
     "Sparring is an excellent way to prepare for actual combat.\
   We'll fight each other with non-lethal weapons now, until one of us falls to the ground.\
   You can get some bruises of course, but better that than being cut down in the real thing.",
     "fighter_talk_train_combat_2", []
     ],

    [anyone | plyr, "fighter_talk_train_combat_2", [],
     "Let's begin then. I am ready.", "close_window", [

         (assign, "$g_tutorial_training_ground_melee_trainer_combat", "$g_talk_troop"),
         (assign, "$g_tutorial_training_ground_melee_state", 0),
         (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
     ]],

    [anyone | plyr, "fighter_talk_train_combat_2", [],
     "Actually I want to do something else.", "fighter_pretalk", []
     ],

    [anyone, "fighter_talk_train_combat",
     [(str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon")],
     "{!}{s3}", "close_window", []
     ],

    [anyone, "start", [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
        (eq, "$g_tutorial_training_ground_conversation_state", 1)
    ],  # parry complete
     "Good. You were able to block my attacks successfully. You may repeat "
     "this practice and try to get faster each time, until you are confident "
     "of your defense skills. Do you want to have another go?",
     "fighter_parry_try_again", [
         (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],

    [anyone, "start", [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
        (eq, "$g_tutorial_training_ground_conversation_state", 2)],

     "Well that didn't go too well, did it? (Remember, you must press and hold "
     "down the right mouse button to keep your block effective.) Do you want "
     "to try again?", "fighter_parry_try_again", [
         (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],

    [anyone | plyr, "fighter_parry_try_again", [],
     "Yes. Let's try again.", "fighter_talk_train_parry", []
     ],

    [anyone | plyr, "fighter_parry_try_again", [],
     "No, I think I am done for now.", "fighter_talk_leave_parry", []
     ],

    # trainer knocked down in parry
    [anyone, "start", [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
        (eq, "$g_tutorial_training_ground_conversation_state", 3)
    ],
     "Hey! We are doing a blocking practice, mate! You are supposed to block my attacks, not attack me back.",
     "fighter_parry_warn", [
         (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],

    [anyone | plyr, "fighter_parry_warn", [],
     "I am sorry. Let's try once again.", "fighter_talk_train_parry", []
     ],

    [anyone | plyr, "fighter_parry_warn", [],
     "Sorry. I must leave this practice now.", "fighter_talk_leave_parry", []
     ],

    [anyone, "fighter_talk_leave_parry", [],
     "All right. As you wish.", "close_window", []
     ],

    # player knocked down in combat
    [anyone, "start", [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
        (eq, "$g_tutorial_training_ground_conversation_state", 4)],
     "Well that didn't go too well, did it?  Don't feel bad, and try not to do "
     "same mistakes next time. Do you want to have a go again?",
     "fighter_combat_try_again", [
         (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],

    [anyone | plyr, "fighter_combat_try_again", [],
     "Yes. Let's do another round.", "fighter_talk_train_combat", []
     ],

    [anyone | plyr, "fighter_combat_try_again", [],
     "No. That was enough for me.", "fighter_talk_leave_combat", []
     ],

    [anyone, "fighter_talk_leave_combat", [],
     "Well, all right. Talk to me again if you change your mind.", "close_window",
     []
     ],

    # trainer knocked down in combat
    [anyone, "start", [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
        (eq, "$g_tutorial_training_ground_conversation_state", 5)],
     "Hey, that was good sparring. You defeated me, but next time I'll be more careful. Do you want to have a go again?",
     "fighter_combat_try_again", [
         (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],

    # attack complete
    [anyone, "start", [
        (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
        (eq, "$g_tutorial_training_ground_conversation_state", 9)],

     "Very good. You have learned how to attack from any direction you want. "
     "If you like we can try this again or move to a different exercise.",
     "fighter_talk", [
        (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],

    [LazyFlag('trp_tutorial_archer_1') | auto_proceed, "start", [],
     "{!}.", "tutorial_troop_default", []
     ],

    ['trp_tutorial_master_archer', "start", [
        (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 1),
     ],
     "Not bad. Not bad at all! You seem to have grasped the basics of archery. "
     "Now, try to do the same thing with a crossbow. Take the crossbow and "
     "the bolts over there and shoot those three targets. The crossbow is much "
     "easier to shoot with compared with the bow, but you need to reload it "
     "after each shot.", "archer_challenge_2", []
     ],

    ['trp_tutorial_master_archer', "start", [
        (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 2),
     ],
     "Good. You didn't have too much difficulty using the crossbow either. "
     "Next you will learn to use throwing weapons. Pick up the javelins you "
     "see over there and try to hit those three targets. ",
     "archer_challenge_2", []
     ],

    ['trp_tutorial_master_archer', "start", [
        (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 3),
     ],
     "Well, with that you have recevied the basic skills to use all three "
     "types of ranged weapons. The rest will come with practice. Train each "
     "and every day, and in time you will be as good as the best marksmen in "
     "Britannia and Hibernia.", "ranged_end", []
     ],

    ['trp_tutorial_master_archer', "ranged_end", [],
     "Now, you can go talk with the melee fighters or the horsemanship trainer "
     "if you haven't already done so. They can teach you important skills too.",
     "close_window", []
     ],

    ['trp_tutorial_master_archer', "start", [
        (try_begin),
            (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
            (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
            (tutorial_message, -1),
        (try_end),

     ],
     "Good day to you, young fellow. I spend my days teaching about ranged "
     "weapons to anyone that is willing to learn. If you need a tutor, let me "
     "know and I'll teach you how to use the bow, the crossbow and the javelin.",
     "archer_talk", []
     ],

    [anyone | plyr, "archer_talk", [
        (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
     ],
     "Yes, show me how to use ranged weapons.", "archer_challenge", []
     ],

    [anyone | plyr, "archer_talk", [],
     "No, not now.", "close_window", []
     ],

    ['trp_tutorial_master_archer', "archer_challenge", [
         (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
     ],
     "All right. Your first training will be in bowmanship. The bow is a "
     "difficult weapon to master. But once you are sufficiently good at it, "
     "you can shoot quickly and with great power. Go pick up the bow and arrows "
     "you see over there now and shoot those targets.",
     "archer_challenge_2", []
     ],

    [anyone | plyr, "archer_challenge_2", [],
     "All right. I am ready.", "close_window", [
        (assign, "$g_tutorial_training_ground_archer_trainer_state", 1),
        (try_begin),
            (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
            (assign, "$g_tutorial_training_ground_archer_trainer_item_1", "itm_practice_bow"),
            (assign, "$g_tutorial_training_ground_archer_trainer_item_2", "itm_practice_arrows_75amount"),
        (else_try),
            (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 1),
            (assign, "$g_tutorial_training_ground_archer_trainer_item_1", "itm_pict_crossbow"),
            (assign, "$g_tutorial_training_ground_archer_trainer_item_2", "itm_bolts"),
        (else_try),
            (assign, "$g_tutorial_training_ground_archer_trainer_item_1", "itm_practice_javelin_40amount"),
            (assign, "$g_tutorial_training_ground_archer_trainer_item_2", -1),
        (try_end),
     ]],

    [anyone | plyr, "archer_challenge_2", [],
     "Just a minute. I want to do something else first.", "close_window", []
     ],

    ['trp_tutorial_master_horseman', "start", [
        (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 1),
     ],
     "I hope you enjoyed the ride. Now we move on to something a bit more "
     "difficult. Grab the lance you see over there and ride around the course "
     "hitting each target at least once.",
     "horseman_melee_challenge_2", []
     ],

    ['trp_tutorial_master_horseman', "start", [
         (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 2),
     ],
     "Good! You have been able to hit all targets on horseback. That's no easy "
     "feat for a starter. Your next challange will be using a bow and arrows to "
     "shoot at the archery targets by the road. You need to put an arrow to "
     "each target to consider yourself successful.",
     "horseman_melee_challenge_2", []
     ],

    ['trp_tutorial_master_horseman', "start",[
         (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 3),
     ],
     "Very good. You were able to shoot all targets from horseback. Keep riding "
     "and practicing each day and in time you will be an expert horseman.",
     "horsemanship_end", []
     ],

    ['trp_tutorial_master_horseman', "horsemanship_end", [],
     "Now, you can go talk with the melee fighters or the archery trainer if "
     "you haven't already done so. You need to learn everything you can to be "
     "prepared when you have to defend yourself.",
     "close_window", []
     ],

    ['trp_tutorial_master_horseman', "start", [
        (try_begin),
            (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
            (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
            (tutorial_message, -1),
        (try_end),
     ],
     "Good day! I have come here for some riding practice, but my old bones "
     "are aching badly so I decided to give myself a rest today. If you would "
     "like to practice your horsemanship, you can take my horse here. The "
     "exercise would be good for her.",
     "horseman_talk", []
     ],

    [anyone | plyr, "horseman_talk", [],
     "Yes, I would like to practice riding.", "horseman_challenge", []
     ],

    [anyone | plyr, "horseman_talk", [],
     "Uhm. Maybe later.", "close_window", []
     ],

    ['trp_tutorial_master_horseman', "horseman_challenge", [
        (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 0),
     ],
     "Good. Now, I will give you a few exercises that'll teach you riding and "
     "horseback weapon use. Your first assignment is simple. Just take your "
     "horse for a ride around the course. Go as slow or as fast as you like. "
     "Come back when you feel confident as a rider and I'll give you some "
     "tougher exercises.",
     "horseman_melee_challenge_2", []
     ],

    [anyone | plyr, "horseman_melee_challenge_2", [],
     "All right. I am ready.", "close_window", [
        (assign, "$g_tutorial_training_ground_horseman_trainer_state", 1),
        (try_begin),
            (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 0),
            (assign, "$g_tutorial_training_ground_horseman_trainer_item_1", -1),
            (assign, "$g_tutorial_training_ground_horseman_trainer_item_2", -1),
        (else_try),
            (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 1),
            (assign, "$g_tutorial_training_ground_horseman_trainer_item_1", "itm_spear_hvy"),
            (assign, "$g_tutorial_training_ground_horseman_trainer_item_2", -1),
        (else_try),
            (assign, "$g_tutorial_training_ground_horseman_trainer_item_1", "itm_practice_bow"),
            (assign, "$g_tutorial_training_ground_horseman_trainer_item_2", "itm_practice_arrows_75amount"),
        (try_end),
     ]],

    [anyone | plyr, "horseman_melee_challenge_2", [],
     "Just a minute. I need to do something else first.", "close_window", []
     ],

    [LazyFlag('trp_tutorial_rider_1') | auto_proceed, "start", [],
     "{!}Warning: This line is never displayed.", "tutorial_troop_default", []
     ],

    [LazyFlag('trp_tutorial_rider_2') | auto_proceed, "start", [],
     "{!}Warning: This line is never displayed.", "tutorial_troop_default", []
     ],

    [anyone, "tutorial_troop_default", [
        (try_begin),
            (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
            (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
            (tutorial_message, -1),
        (try_end),
     ],
     "Hey, I am trying to practice here. Go, talk with the archery trainer if "
     "you need guidance about ranged weapons.",
     "close_window", []
     ],
]
