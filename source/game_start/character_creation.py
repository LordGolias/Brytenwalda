from source.header_operations import *
from source.header_common import *
from source.header_troops import *
from source.header_skills import *
from source.header_item_modifiers import *
from source.header_game_menus import mnf_disable_all_keys, menu_text_color

from source.module_constants import *
from source.module_items_shields import shields

_a1_noble = "@You came into the world a {reg3?daughter:son} of declining " \
            "nobility, owning only the house in which they lived. However, " \
            "despite your family's hardships, they afforded you a good " \
            "education and trained you from childhood for the rigors of " \
            "aristocracy and life at court."

_a1_merchant = "@You were born the {reg3?daughter:son} of travelling merchants, " \
               "always moving from place to place in search of a profit. " \
               "Although your parents were wealthier than most and educated you " \
               "as well as they could, you found little opportunity to make " \
               "friends on the road, living mostly for the moments when you " \
               "could sell something to somebody."

_a1_guard = "@As a child, your family scrabbled out a meagre living from your " \
            "father's wages as a guardsman to the local lord. It was not an " \
            "easy existence, and you were too poor to get much of an education. " \
            "You learned mainly how to defend yourself on the streets, with or " \
            "without a weapon in hand."

_a1_forester = "@You were the {reg3?daughter:son} of a family who lived off " \
               "the woods, doing whatever they needed to make ends meet. " \
               "Hunting, woodcutting, making arrows, even a spot of poaching " \
               "whenever things got tight. Winter was never a good time for " \
               "your family as the cold took animals and people alike, but you " \
               "always lived to see another dawn, though your brothers and " \
               "sisters might not be so fortunate."

_a1_nomad = "@You were a child of the steppe, born to a tribe of wandering nomads who lived\
 in great camps throughout the arid grasslands.\
 Like the other tribesmen, your family revered horses above almost everything else, and they taught you\
 how to ride almost before you learned how to walk. "

_a1_thief = "@As the {reg3?daughter:son} of a thief, you had very little 'formal' education.\
 Instead you were out on the street, begging until you learned how to cut purses, cutting purses\
 until you learned how to pick locks, all the way through your childhood.\
 Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."

_a2_page = "@As a {reg3?girl:boy} growing out of childhood,\
 you were sent to live in the court of one of the nobles of the land.\
 There, your first lessons were in humility, as you waited upon the lords and ladies of the household.\
 But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict\
 and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."

_a2_apprentice = "@As a {reg3?girl:boy} growing out of childhood,\
 you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your\
 new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as\
 you wished to stay."

# the last menu of this list is the one the hard-wired creation menu points to.
menus = [

    ("start_game_1", menu_text_color(0xFF000000) | mnf_disable_all_keys,
     "Select your character's gender.",
     "none", [],
     [
         ("start_male", [], "Male",
          [
              (troop_set_type, "trp_player", 0),
              (assign, "$character_gender", tf_male),
              (jump_to_menu, "mnu_start_character_1"),
          ]),

         ("start_female", [], "Female",
          [
              (troop_set_type, "trp_player", 1),
              (assign, "$character_gender", tf_female),
              (jump_to_menu, "mnu_start_character_1"),
          ]),

         ("go_back", [], "Go back", [(change_screen_quit)]),
     ]),

    ("start_character_1", mnf_disable_all_keys,
     "You were born years ago, in a land far away. Your father was...",
     "none",
     [
         (str_clear, s10),
         (str_clear, s11),
         (str_clear, s12),
         (str_clear, s13),
         (str_clear, s14),
         (str_clear, s15),
     ],
     [
         ("start_noble", [], "An impoverished noble.", [
             (assign, "$background_type", cb_noble),
             (assign, reg3, "$character_gender"),
             (str_store_string, s10, _a1_noble),
             (jump_to_menu, "mnu_start_character_2")
         ]),

         ("start_merchant", [], "A travelling merchant.", [
             (assign, "$background_type", cb_merchant),
             (assign, reg3, "$character_gender"),
             (str_store_string, s10, _a1_merchant),
             (jump_to_menu, "mnu_start_character_2"),
         ]),

         ("start_guard", [], "A veteran warrior.", [
             (assign, "$background_type", cb_guard),
             (assign, reg3, "$character_gender"),
             (str_store_string, s10, _a1_guard),
             (jump_to_menu, "mnu_start_character_2"),
         ]),

         ("start_forester", [], "A hunter.", [
             (assign, "$background_type", cb_forester),
             (assign, reg3, "$character_gender"),
             (str_store_string, s11, "@{reg3?daughter:son}"),
             (str_store_string, s10, _a1_forester),
             (jump_to_menu, "mnu_start_character_2"),
         ]),

         ("start_nomad", [], "A steppe nomad.", [
             (assign, "$background_type", cb_nomad),
             (assign, reg3, "$character_gender"),
             (str_store_string, s11, "@{reg3?daughter:son}"),
             (str_store_string, s10, _a1_nomad),
             (jump_to_menu, "mnu_start_character_2"),
         ]),

         ("start_thief", [], "A thief.", [
             (assign, "$background_type", cb_thief),
             (assign, reg3, "$character_gender"),
             (str_store_string, s10, _a1_thief),
             (jump_to_menu, "mnu_start_character_2"),
         ]),

         ("go_back", [], "Go back", [
             (jump_to_menu, "mnu_start_game_1"),
         ]),
     ]),

    ("start_character_2", 0,
     "{s10}^^ You started to learn about the world almost as soon as you "
     "could walk and talk. You spent your early life as...", "none", [], [

         ("page", [], "A page at a nobleman's court.", [
             (assign, "$background_answer_2", cb2_page),
             (assign, reg3, "$character_gender"),
             (str_store_string, s11, _a2_page),
             (jump_to_menu, "mnu_start_character_3"),
         ]),

         ("apprentice", [], "A craftsman's apprentice.", [
             (assign, "$background_answer_2", cb2_apprentice),
             (assign, reg3, "$character_gender"),
             (str_store_string, s11, _a2_apprentice),
             (jump_to_menu, "mnu_start_character_3"),
         ]),

         ("stockboy", [
         ], "A shop assistant.", [
              (assign, "$background_answer_2", cb2_merchants_helper),
              (assign, reg3, "$character_gender"),
              (str_store_string, s11, "@As a {reg3?girl:boy} growing out of childhood,\
 you apprenticed to a wealthy merchant, picking up the trade over years of working shops and driving caravans.\
 You soon became adept at the art of buying low, selling high, and leaving the customer thinking they'd\
 got the better deal."),
              (jump_to_menu, "mnu_start_character_3"),
          ]),
         ("urchin", [
         ], "A street urchin.", [
              (assign, "$background_answer_2", cb2_urchin),
              (assign, reg3, "$character_gender"),
              (str_store_string, s11, "@As a {reg3?girl:boy} growing out of childhood,\
 you took to the streets, doing whatever you must to survive.\
 Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world,\
 always one step ahead of the law and those who wished you ill."),
              (jump_to_menu, "mnu_start_character_3"),
          ]),
         ("nomad", [
         ], "A steppe child.", [
              (assign, "$background_answer_2", cb2_steppe_child),
              (assign, reg3, "$character_gender"),
              (str_store_string, s11, "@As a {reg3?girl:boy} growing out of childhood,\
 you rode the great steppes on a horse of your own, learning the ways of the grass and the desert.\
 Although you sometimes went hungry, you became a skillful hunter and pathfinder in this trackless country.\
 Your body too started to harden with muscle as you grew into the life of a nomad {reg3?woman:man}."),
              (jump_to_menu, "mnu_start_character_3"),
          ]),
         ("go_back", [], "Go back.",
          [(jump_to_menu, "mnu_start_character_1"),
           ]),
     ]
     ),

    ("start_character_3", mnf_disable_all_keys,
        "{s11}^^ Then, as a young adult, life changed as it always does. You became...",
        "none",
        [(assign, reg3, "$character_gender"), ],
        [
            ("squire", [(eq, "$character_gender", tf_male)], "A squire.", [
                (assign, "$background_answer_3", cb3_squire),
                (str_store_string, s14, "@{reg3?daughter:man}"),
                (str_store_string, s12, "@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
 When you were named squire to a noble at court, you practiced long hours with weapons,\
 learning how to deal out hard knocks and how to take them, too.\
 You were instructed in your obligations to your lord, and of your duties to those who might one day be your vassals.\
 But in addition to learning the chivalric ideal, you also learned about the less uplifting side\
 -- old warriors' stories of ruthless power politics, of betrayals and usurpations,\
 of men who used guile as well as valor to achieve their aims."),
                (jump_to_menu, "mnu_start_character_4"),
            ]),
            (
                "lady", [(eq, "$character_gender", tf_female)], "A lady-in-waiting.", [
                    (assign, "$background_answer_3", cb3_lady_in_waiting),
                    (str_store_string, s14, "@{reg3?daughter:man}"),
                    (str_store_string, s13, "@{reg3?woman:man}"),
                    (str_store_string, s12, "@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You joined the tightly-knit circle of women at court, ladies who all did proper ladylike things,\
 the wives and mistresses of noble men as well as maidens who had yet to find a husband.\
 However, even here you found politics at work as the ladies schemed for prominence and fought each other\
 bitterly to catch the eye of whatever unmarried man was in fashion at court.\
 You soon learned ways of turning these situations and goings-on to your advantage. With it came the\
 realisation that you yourself could wield great influence in the world, if only you applied yourself\
 with a little bit of subtlety."),
                    (jump_to_menu, "mnu_start_character_4"),
                ]),
            ("troubadour", [], "A troubadour.", [
                (assign, "$background_answer_3", cb3_troubadour),
                (str_store_string, s14, "@{reg3?daughter:man}"),
                (str_store_string, s13, "@{reg3?woman:man}"),
                (str_store_string, s12, "@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You set out on your own with nothing except the instrument slung over your back and your own voice.\
 It was a poor existence, with many a hungry night when people failed to appreciate your play,\
 but you managed to survive on your music alone. As the years went by you became adept at playing the\
 drunken crowds in your taverns, and even better at talking anyone out of anything you wanted."),
                (jump_to_menu, "mnu_start_character_4"),
            ]),
            ("student", [], "A university student.", [
                (assign, "$background_answer_3", cb3_student),
                (str_store_string, s12, "@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
 You found yourself as a student in the university of one of the great cities,\
 where you studied theology, philosophy, and medicine.\
 But not all your lessons were learned in the lecture halls.\
 You may or may not have joined in with your fellows as they roamed the alleys in search of wine, women, and a good fight.\
 However, you certainly were able to observe how a broken jaw is set,\
 or how an angry townsman can be persuaded to set down his club and accept cash compensation for the destruction of his shop."),
                (jump_to_menu, "mnu_start_character_4"),
            ]),
            ("peddler", [], "A goods peddler.", [
                (assign, "$background_answer_3", cb3_peddler),
                (str_store_string, s14, "@{reg3?daughter:man}"),
                (str_store_string, s13, "@{reg3?woman:man}"),
                (str_store_string, s12, "@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 Heeding the call of the open road, you travelled from village to village buying and selling what you could.\
 It was not a rich existence, but you became a master at haggling even the most miserly elders into\
 giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire..."),
                (jump_to_menu, "mnu_start_character_4"),
            ]),
            ("craftsman", [], "A smith.", [
                (assign, "$background_answer_3", cb3_craftsman),
                (str_store_string, s14, "@{reg3?daughter:man}"),
                (str_store_string, s13, "@{reg3?woman:man}"),
                (str_store_string, s12, "@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 You pursued a career as a smith, crafting items of function and beauty out of simple metal.\
 As time wore on you became a master of your trade, and fine work started to fetch fine prices.\
 With food in your belly and logs on your fire, you could take pride in your work and your growing reputation."),
                (jump_to_menu, "mnu_start_character_4"),
            ]),
            ("poacher", [], "A game poacher.", [
                (assign, "$background_answer_3", cb3_poacher),
                (str_store_string, s14, "@{reg3?daughter:man}"),
                (str_store_string, s13, "@{reg3?woman:man}"),
                (str_store_string, s12, "@Though the distinction felt sudden to you,\
 somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests\
 and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold\
 the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into\
 firewood that warmed many freezing homes during winter. All for a few silvers, of course."),
                (jump_to_menu, "mnu_start_character_4"),
            ]),
            ("go_back", [], "Go back.",
             [(jump_to_menu, "mnu_start_character_2"),
              ]
             ),
        ]
    ),

    ("start_character_4", mnf_disable_all_keys,
     "{s12}^^But soon everything changed and you decided to strike out on "
     "your own as an adventurer. What made you take this decision was...",
     "none",
     [],
     [
         ("revenge", [], "Personal revenge.", [
             (assign, "$background_answer_4", cb4_revenge),
             (str_store_string, s13, "@Only you know exactly what caused you to give up your old life and become an adventurer.\
 Still, it was not a difficult choice to leave, with the rage burning brightly in your heart.\
 You want vengeance. You want justice. What was done to you cannot be undone,\
 and these debts can only be paid in blood..."),
             (jump_to_menu, "mnu_choose_skill"),
         ]),

         ("death", [], "The loss of a loved one.", [
             (assign, "$background_answer_4", cb4_loss),
             (str_store_string, s13, "@Only you know exactly what caused you to give up your old life and become an adventurer.\
 All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so\
 painful. Perhaps your new life will let you forget,\
 or honour the name that you can no longer bear to speak..."),
             (jump_to_menu, "mnu_choose_skill"),
         ]),

         ("wanderlust", [], "Wanderlust.", [
             (assign, "$background_answer_4", cb4_wanderlust),
             (str_store_string, s13, "@Only you know exactly what caused you to give up your old life and become an adventurer.\
 You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of\
 wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the\
 freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back..."),
             (jump_to_menu, "mnu_choose_skill"),
         ]),

         ("disown", [], "Being forced out of your home.", [
             (assign, "$background_answer_4", cb4_disown),
             (str_store_string, s13, "@Only you know exactly what caused you to give up your old life and become an adventurer.\
 However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone\
 now, and you must face the fact that you're out in the wide wide world. Alone to sink or swim..."),
             (jump_to_menu, "mnu_choose_skill"),
         ]),

         ("greed", [], "Lust for money and power.", [
             (assign, "$background_answer_4", cb4_greed),
             (str_store_string, s13, "@Only you know exactly what caused you to give up your old life and become an adventurer.\
 To everyone else, it's clear that you're now motivated solely by personal gain.\
 You want to be rich, powerful, respected, feared.\
 You want to be the one whom others hurry to obey.\
 You want people to know your name, and tremble whenever it is spoken.\
 You want everything, and you won't let anyone stop you from having it..."),
             (jump_to_menu, "mnu_choose_skill"),
         ]),

         ("go_back", [], "Go back.", [(jump_to_menu, "mnu_start_character_3")]),
     ]
     ),

    ("choose_skill", mnf_disable_all_keys,
     "{s13}",
     "none",
        [(assign, "$current_string_reg", 10),
      (assign, ":difficulty", 0),

      (try_begin),
          (eq, "$character_gender", tf_female),
          (str_store_string, s14, "str_woman"),
          (val_add, ":difficulty", 1),
      (else_try),
          (str_store_string, s14, "str_man"),
      (try_end),

      (try_begin),
          (eq, "$background_type", cb_noble),
          (str_store_string, s15, "str_noble"),
          (val_sub, ":difficulty", 1),
      (else_try),
          (str_store_string, s15, "str_common"),
      (try_end),

      (try_begin),
          (eq, ":difficulty", -1),
          (str_store_string, s16,
           "str_may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly"),
      (else_try),
          (eq, ":difficulty", 0),
          (str_store_string, s16,
           "str_may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
      (else_try),
          (eq, ":difficulty", 1),
          (str_store_string, s16,
           "str_may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
      (try_end),
      ],

     [("begin_adventuring", [], "Become an adventurer and ride to your destiny.",
       [
           (set_show_messages, 1),

           (call_script, "script_build_character_from_answers"),

           (try_begin),
               (eq, "$background_type", cb_noble),
               (jump_to_menu, "mnu_auto_return"),
               (start_presentation, "prsnt_banner_selection"),
           (else_try),
               (change_screen_return, 0),
           (try_end),

           (set_show_messages, 1),
       ]),

      ("go_back_dot", [], "Go back.", [(jump_to_menu, "mnu_start_character_4")]),
      ]),
]


scripts = [
    ('build_character_from_answers', [
        (try_begin),
            (eq, "$character_gender", 0),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
        (else_try),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
        (try_end),

        (troop_raise_attribute, "trp_player", ca_strength, 1),
        (troop_raise_attribute, "trp_player", ca_agility, 1),
        (troop_raise_attribute, "trp_player", ca_charisma, 1),

        (troop_raise_skill, "trp_player", "skl_leadership", 1),
        (troop_raise_skill, "trp_player", "skl_riding", 1),

        (try_begin),
            (eq, "$background_type", cb_noble),
            (eq, "$character_gender", tf_male),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_attribute, "trp_player", ca_charisma, 2),
            (troop_raise_skill, "trp_player", skl_weapon_master, 1),
            (troop_raise_skill, "trp_player", skl_power_strike, 1),
            (troop_raise_skill, "trp_player", skl_riding, 1),
            (troop_raise_skill, "trp_player", skl_tactics, 1),
            (troop_raise_skill, "trp_player", skl_leadership, 1),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
            (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 10),
            (troop_raise_proficiency, "trp_player", wpt_polearm, 10),

            (troop_add_item, "trp_player", shields['common'][0]['light'][0], imod_battered),
            (troop_set_slot, "trp_player", "slot_troop_renown", 100),
            (call_script, "script_change_player_honor", 3),

            (troop_add_gold, "trp_player", 100),
        (else_try),
            (eq, "$background_type", cb_noble),
            (eq, "$character_gender", tf_female),
            (troop_raise_attribute, "trp_player", ca_intelligence, 2),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
            (troop_raise_skill, "trp_player", skl_wound_treatment, 1),
            (troop_raise_skill, "trp_player", skl_riding, 2),
            (troop_raise_skill, "trp_player", skl_first_aid, 1),
            (troop_raise_skill, "trp_player", skl_leadership, 1),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 20),

            (troop_set_slot, "trp_player", "slot_troop_renown", 50),
            (troop_add_item, "trp_player", shields['common'][0]['light'][0], 0),

            (troop_add_gold, "trp_player", 100),
        (else_try),
            (eq, "$background_type", cb_merchant),
            (troop_raise_attribute, "trp_player", ca_intelligence, 2),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
            (troop_raise_skill, "trp_player", skl_riding, 1),
            (troop_raise_skill, "trp_player", skl_leadership, 1),
            (troop_raise_skill, "trp_player", skl_trade, 2),
            (troop_raise_skill, "trp_player", skl_inventory_management, 1),
            (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 10),
            (troop_add_gold, "trp_player", 250),
            (troop_set_slot, "trp_player", "slot_troop_renown", 20),
        (else_try),
            (eq, "$background_type", cb_guard),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
            (troop_raise_skill, "trp_player", "skl_ironflesh", 1),
            (troop_raise_skill, "trp_player", "skl_power_strike", 1),
            (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
            (troop_raise_skill, "trp_player", "skl_leadership", 1),
            (troop_raise_skill, "trp_player", "skl_trainer", 1),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
            (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 15),
            (troop_raise_proficiency, "trp_player", wpt_polearm, 20),
            (troop_raise_proficiency, "trp_player", wpt_throwing, 10),
            (troop_add_item, "trp_player", shields['common'][0]['light'][0], 0),
            (troop_add_gold, "trp_player", 50),
            (troop_set_slot, "trp_player", "slot_troop_renown", 10),
        (else_try),
            (eq, "$background_type", cb_forester),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 2),
            (troop_raise_skill, "trp_player", "skl_power_draw", 1),
            (troop_raise_skill, "trp_player", "skl_tracking", 1),
            (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
            (troop_raise_skill, "trp_player", "skl_spotting", 1),
            (troop_raise_skill, "trp_player", "skl_athletics", 1),
            (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 10),
            (troop_raise_proficiency, "trp_player", wpt_archery, 30),
            (troop_add_gold, "trp_player", 30),
        (else_try),
            (eq, "$background_type", cb_nomad),
            (eq, "$character_gender", tf_male),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_skill, "trp_player", "skl_power_draw", 1),
            (troop_raise_skill, "trp_player", "skl_horse_archery", 1),
            (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
            (troop_raise_skill, "trp_player", "skl_riding", 2),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
            (troop_raise_proficiency, "trp_player", wpt_archery, 30),
            (troop_raise_proficiency, "trp_player", wpt_throwing, 10),
            (troop_add_item, "trp_player", shields['common'][0]['light'][0], imod_battered),
            (troop_add_gold, "trp_player", 15),
            (troop_set_slot, "trp_player", "slot_troop_renown", 10),
        (else_try),
            (eq, "$background_type", cb_nomad),
            (eq, "$character_gender", tf_female),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_skill, "trp_player", "skl_wound_treatment", 1),
            (troop_raise_skill, "trp_player", "skl_first_aid", 1),
            (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
            (troop_raise_skill, "trp_player", "skl_riding", 2),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 5),
            (troop_raise_proficiency, "trp_player", wpt_archery, 20),
            (troop_raise_proficiency, "trp_player", wpt_throwing, 5),
            (troop_add_item, "trp_player", shields['common'][0]['light'][0], imod_battered),
            (troop_add_gold, "trp_player", 20),
        (else_try),
            (eq, "$background_type", cb_thief),
            (troop_raise_attribute, "trp_player", ca_agility, 3),
            (troop_raise_skill, "trp_player", "skl_athletics", 2),
            (troop_raise_skill, "trp_player", "skl_power_throw", 1),
            (troop_raise_skill, "trp_player", "skl_inventory_management", 1),
            (troop_raise_skill, "trp_player", "skl_looting", 1),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 20),
            (troop_raise_proficiency, "trp_player", wpt_throwing, 20),
            (troop_add_item, "trp_player", "itm_wooden_javelins", 0),
            (troop_add_gold, "trp_player", 25),
        (try_end),

        (try_begin),
            (eq, "$background_answer_2", cb2_page),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_skill, "trp_player", "skl_power_strike", 1),
            (troop_raise_skill, "trp_player", "skl_persuasion", 1),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 15),
            (troop_raise_proficiency, "trp_player", wpt_polearm, 5),
        (else_try),
            (eq, "$background_answer_2", cb2_apprentice),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_skill, "trp_player", "skl_engineer", 1),
            (troop_raise_skill, "trp_player", "skl_trade", 1),
        (else_try),
            (eq, "$background_answer_2", cb2_urchin),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_skill, "trp_player", "skl_spotting", 1),
            (troop_raise_skill, "trp_player", "skl_looting", 1),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 15),
            (troop_raise_proficiency, "trp_player", wpt_throwing, 5),
        (else_try),
            (eq, "$background_answer_2", cb2_steppe_child),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_skill, "trp_player", "skl_horse_archery", 1),
            (troop_raise_skill, "trp_player", "skl_power_throw", 1),
            (troop_raise_proficiency, "trp_player", wpt_archery, 15),
            (call_script, "script_change_troop_renown", "trp_player", 5),
        (else_try),
            (eq, "$background_answer_2", cb2_merchants_helper),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
            (troop_raise_skill, "trp_player", "skl_inventory_management", 1),
            (troop_raise_skill, "trp_player", "skl_trade", 1),
        (try_end),

        (try_begin),
            (eq, "$background_answer_3", cb3_poacher),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_skill, "trp_player", "skl_power_draw", 1),
            (troop_raise_skill, "trp_player", "skl_tracking", 1),
            (troop_raise_skill, "trp_player", "skl_spotting", 1),
            (troop_raise_skill, "trp_player", "skl_athletics", 1),
            (troop_add_gold, "trp_player", 10),
            (troop_raise_proficiency, "trp_player", wpt_polearm, 10),
            (troop_raise_proficiency, "trp_player", wpt_archery, 35),

            (troop_add_item, "trp_player", "itm_axe_englet2", imod_chipped),
            (troop_add_item, "trp_player", "itm_rawhide_vest_green", 0),
            (troop_add_item, "trp_player", "itm_footwear_0m_1", 0),
            (troop_add_item, "trp_player", "itm_huntingbow", 0),
            (troop_add_item, "trp_player", "itm_barbed_arrows", 0),
            (troop_add_item, "trp_player", "itm_horse_pony", imod_heavy),
            (troop_add_item, "trp_player", "itm_dried_meat", 0),
            (troop_add_item, "trp_player", "itm_dried_meat", 0),
            (troop_add_item, "trp_player", "itm_furs", 0),
            (troop_add_item, "trp_player", "itm_furs", 0),
        (else_try),
            (eq, "$background_answer_3", cb3_craftsman),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),

            (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
            (troop_raise_skill, "trp_player", "skl_engineer", 1),
            (troop_raise_skill, "trp_player", "skl_tactics", 1),
            (troop_raise_skill, "trp_player", "skl_trade", 1),

            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 15),
            (troop_add_gold, "trp_player", 100),

            (troop_add_item, "trp_player", "itm_footwear_1m_1", imod_ragged),
            (troop_add_item, "trp_player", "itm_merch_tunicwt", 0),

            (troop_add_item, "trp_player", "itm_espada_historic1", imod_balanced),
            (troop_add_item, "trp_player", "itm_pict_crossbow", 0),
            (troop_add_item, "trp_player", "itm_bolts", 0),

            (troop_add_item, "trp_player", "itm_tools", 0),
            (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
            (eq, "$background_answer_3", cb3_peddler),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_skill, "trp_player", "skl_riding", 1),
            (troop_raise_skill, "trp_player", "skl_trade", 1),
            (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
            (troop_raise_skill, "trp_player", "skl_inventory_management", 1),

            (troop_add_item, "trp_player", "itm_leather_gloves1", imod_plain),
            (troop_add_gold, "trp_player", 90),
            (troop_raise_proficiency, "trp_player", wpt_polearm, 15),

            (troop_add_item, "trp_player", "itm_gaelic_jacketgray", 0),
            (troop_add_item, "trp_player", "itm_footwear_1c_1", imod_ragged),
            (troop_add_item, "trp_player", "itm_dena_helmgoat", 0),
            (troop_add_item, "trp_player", "itm_staff1", 0),
            (troop_add_item, "trp_player", "itm_pict_crossbow", 0),
            (troop_add_item, "trp_player", "itm_bolts", 0),
            (troop_add_item, "trp_player", "itm_horse_0l_1", 0),
            (troop_add_item, "trp_player", "itm_horse_pony", 0),

            (troop_add_item, "trp_player", "itm_linen", 0),
            (troop_add_item, "trp_player", "itm_pottery", 0),
            (troop_add_item, "trp_player", "itm_wool", 0),
            (troop_add_item, "trp_player", "itm_wool", 0),
            (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
            (eq, "$background_answer_3", cb3_troubadour),
            (troop_raise_attribute, "trp_player", ca_charisma, 2),

            (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
            (troop_raise_skill, "trp_player", "skl_persuasion", 1),
            (troop_raise_skill, "trp_player", "skl_leadership", 1),
            (troop_raise_skill, "trp_player", "skl_pathfinding", 1),

            (troop_add_gold, "trp_player", 80),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 25),
            (troop_raise_proficiency, "trp_player", wpt_crossbow, 10),

            (troop_add_item, "trp_player", "itm_bluepantsbody_woad04", imod_sturdy),
            (troop_add_item, "trp_player", "itm_footwear_1m_1", imod_ragged),
            (troop_add_item, "trp_player", "itm_espada_historic1", imod_rusty),
            (troop_add_item, "trp_player", "itm_pict_crossbow", 0),
            (troop_add_item, "trp_player", "itm_bolts", 0),
            (troop_add_item, "trp_player", "itm_horse_0l_3", imod_swaybacked),
            (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
            (eq, "$background_answer_3", cb3_squire),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_skill, "trp_player", "skl_riding", 1),
            (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
            (troop_raise_skill, "trp_player", "skl_power_strike", 1),
            (troop_raise_skill, "trp_player", "skl_leadership", 1),

            (troop_add_gold, "trp_player", 20),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 30),
            (troop_raise_proficiency, "trp_player", wpt_two_handed_weapon, 30),
            (troop_raise_proficiency, "trp_player", wpt_polearm, 30),
            (troop_raise_proficiency, "trp_player", wpt_archery, 10),
            (troop_raise_proficiency, "trp_player", wpt_crossbow, 10),
            (troop_raise_proficiency, "trp_player", wpt_throwing, 10),

            (troop_add_item, "trp_player", "itm_leather_tunic1", imod_ragged),
            (troop_add_item, "trp_player", "itm_footwear_0m_1", imod_tattered),

            (troop_add_item, "trp_player", "itm_espada_historic1", imod_rusty),
            (troop_add_item, "trp_player", "itm_pict_crossbow", 0),
            (troop_add_item, "trp_player", "itm_bolts", 0),
            (troop_add_item, "trp_player", "itm_horse_0n_3", imod_swaybacked),
            (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
            (eq, "$background_answer_3", cb3_lady_in_waiting),
            (eq, "$character_gender", tf_female),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_attribute, "trp_player", ca_charisma, 1),

            (troop_raise_skill, "trp_player", "skl_persuasion", 2),
            (troop_raise_skill, "trp_player", "skl_riding", 1),
            (troop_raise_skill, "trp_player", "skl_wound_treatment", 1),

            (troop_add_item, "trp_player", "itm_seaxt3", 0),
            (troop_add_item, "trp_player", "itm_pict_crossbow", 0),
            (troop_add_item, "trp_player", "itm_bolts", 0),
            (troop_add_item, "trp_player", "itm_horse_0l_2", imod_spirited),
            (troop_add_item, "trp_player", "itm_ptunic11", imod_sturdy),
            (troop_add_item, "trp_player", "itm_woolen_dressplain", imod_sturdy),
            (troop_add_gold, "trp_player", 100),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 10),
            (troop_raise_proficiency, "trp_player", wpt_crossbow, 15),
            (troop_add_item, "trp_player", "itm_smoked_fish", 0),
        (else_try),
            (eq, "$background_answer_3", cb3_student),
            (troop_raise_attribute, "trp_player", ca_intelligence, 2),

            (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
            (troop_raise_skill, "trp_player", "skl_surgery", 1),
            (troop_raise_skill, "trp_player", "skl_wound_treatment", 1),
            (troop_raise_skill, "trp_player", "skl_persuasion", 1),

            (troop_add_gold, "trp_player", 80),
            (troop_raise_proficiency, "trp_player", wpt_one_handed_weapon, 20),
            (troop_raise_proficiency, "trp_player", wpt_crossbow, 20),

            (troop_add_item, "trp_player", "itm_ptunic3", imod_sturdy),
            (troop_add_item, "trp_player", "itm_footwear_0c_1", 0),
            (troop_add_item, "trp_player", "itm_espada_historic1", imod_rusty),
            (troop_add_item, "trp_player", "itm_pict_crossbow", 0),
            (troop_add_item, "trp_player", "itm_bolts", 0),
            (troop_add_item, "trp_player", "itm_smoked_fish", 0),
            (store_random_in_range, ":book_no", books_begin, books_end),
            (troop_add_item, "trp_player", ":book_no", 0),
        (try_end),

        (try_begin),
            (eq, "$background_answer_4", cb4_revenge),
            (troop_raise_attribute, "trp_player", ca_strength, 2),
            (troop_raise_skill, "trp_player", "skl_power_strike", 1),
        (else_try),
            (eq, "$background_answer_4", cb4_loss),
            (troop_raise_attribute, "trp_player", ca_charisma, 2),
            (troop_raise_skill, "trp_player", "skl_ironflesh", 1),
        (else_try),
            (eq, "$background_answer_4", cb4_wanderlust),
            (troop_raise_attribute, "trp_player", ca_agility, 2),
            (troop_raise_skill, "trp_player", "skl_pathfinding", 1),
        (else_try),
            (eq, "$background_answer_4", cb4_disown),
            (troop_raise_attribute, "trp_player", ca_strength, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
        (else_try),
            (eq, "$background_answer_4", cb4_greed),
            (troop_raise_attribute, "trp_player", ca_agility, 1),
            (troop_raise_attribute, "trp_player", ca_intelligence, 1),
            (troop_raise_skill, "trp_player", "skl_looting", 1),
        (try_end),
    ]),
]
