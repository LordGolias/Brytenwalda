from .header_skills import *

#############################
#  Each skill contains the following fields:
#  1) Skill id (string): used for referencing skills in other files. The prefix skl_ is automatically added before each skill-id .
#  2) Skill name (string).
#  3) Skill flags (int). See header_skills.py for a list of available flags
#  4) Maximum level of the skill (int).
#  5) Skill description (string): used in character window for explaining the skills.
# 
####################################################################################################################
#Hardcoded skills are {names (indexes, beginning with 0)}:
# Trade (1)
# Leadership (2)
# Prisoner Management (3)
# First Aid (9)
# Surgery (10)
# Wound Treatment (11)
# Inventory Management (12)
# Spotting (13)
# Pathfinding (14)
# Tactics (15)
# Tracking (16)
# Trainer (17)
# Engineer (18)
# Horse Archery (24)
# Riding (25)
# Athletics (26)
# Shield (27)
# Weapon Master (28)
# Power Draw (34)
# Power Throw (35)
# Power Strike (36)
# Ironflesh (37)
# The effects of these skills can only be removed if the skill is disabled with sf_inactive flag.
# If you want to add a new skill, use the reserved skills or use non-hardcoded skills.
#gdwSkills raised to 15 cap. Some very unrealistic, but let people live their own fantasies. The ones at 12 are usually capped out below 5.
skills = [
  ("trade","Trade",sf_base_att_cha|sf_effects_party,15,"Every level of this skill reduces your trade penalty by 5%%. (Party skill)"),
  ("leadership","Leadership",sf_base_att_cha|sf_effects_party,15,"Every point increases maximum number of troops you can command by 1, and  every leader point reduces troop wages by 5%%. (Party/Leader skill)"), #cambiado chief motomataru
  ("prisoner_management", "Prisoner Management",sf_base_att_cha|sf_effects_party,15,"Every level of this skill increases maximum number of prisoners by 10 and reduces imprisoned Lord escape chances by 2%%. Lords have a chance to escape captivity each week: 30%% held in the party, 15%% held in castle/town, 5%% held in a castle/town with prison tower. (Leader skill)"), 
#  ("reserved_1","Reserved Skill 1",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."), 
  ("entertain","Entertain",sf_base_att_cha|sf_effects_party,15,"Every day that you rest, each hero with this skill increases the morale of the party. It also helps you while begging or performing. Drive it past 10, and you could become the next bardic sensation! (Personal skill)."),    #MOTO tweak entertainment
  ("reserved_2","Reserved Skill 2",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_3","Reserved Skill 3",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_4","Reserved Skill 4",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."), 
  ("persuasion","Persuasion", sf_base_att_cha, 15, "This skill helps you make other people accept your point of view. Increases ability to negotiate surrender in sieges. Each rank increases number of troops recruited from villages by 1 and reduces the commission of each recruited villager by 1 scillinga. Increases amount of supplies you convince villagers to hand over by 3%%. (Personal skill)"),
  ("engineer","Engineer",sf_base_att_int|sf_effects_party,15,"This skill allows you to construct siege equipment and fief improvements more efficiently. (Party skill)"),
  ("first_aid", "First Aid",sf_base_att_int|sf_effects_party,15,"Heroes regain 5%% per skill level of hit-points lost during mission. (Party skill)"), 
  ("surgery","Surgery",sf_base_att_int|sf_effects_party,15,"Each point to this skill gives a 4%% chance that a mortally struck party member will be wounded rather than killed. (Party skill)"), 
  ("wound_treatment","Wound Treatment",sf_base_att_int|sf_effects_party,15,"Party healing speed is increased by 20%% per level of this skill. (Party skill)"), 
  ("inventory_management","Inventory Management",sf_base_att_int|sf_effects_party,15,"Increases inventory capacity by +6 per skill level. (Leader skill)"), 
  ("spotting","Spotting",sf_base_att_str|sf_effects_party,15,"Party seeing range is increased by 10%% per skill level. (Party skill)"),
  ("pathfinding","Path-finding",sf_base_att_int|sf_effects_party,15,"Party map speed is increased by 3%% per skill level. (Party skill)"), 
  ("tactics","Tactics",sf_base_att_int|sf_effects_party,15,"Every two levels of this skill increases starting battle advantage by 1. (Party skill)"),
  ("tracking","Tracking",sf_base_att_int|sf_effects_party,15,"Tracks become more informative. (Party skill)"),
  ("trainer","Trainer",sf_base_att_int|sf_effects_party,15,"Every day, each hero with this skill adds some experience to every other member of the party whose level is lower than his/hers. Experience gained goes as: {0,4,10,16,23,30,38,46,55,65,80}. (Personal skill)"),
  ("reserved_5","Reserved Skill 5",sf_base_att_int|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_6","Reserved Skill 6",sf_base_att_int|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_7","Reserved Skill 7",sf_base_att_int|sf_inactive,10,"This is a reserved skill."), 
  #("reserved_8","Reserved Skill 8",sf_base_att_int|sf_inactive,10,"This is a reserved skill."),
  ("foraging","Foraging",sf_base_att_int|sf_effects_party,15,"Allows the party to forage for 5 food per skill level (camp, siege, raiding) and increase foraging range (Party skill) Max level: 10."),
## Jrider + FORAGING 1.0 adding skill chief#gdw fixed order per Kalarhan finding
  ("looting","Looting",sf_base_att_cha|sf_effects_party,15,"This skill increases the amount of loot obtained by 10%% per skill level. (Party skill)"), 
  ("horse_archery","Horse Archery",sf_base_att_str,10,"Reduces damage and accuracy penalties for archery and throwing from horseback. Max level - (Personal skill)"),
  ("riding","Riding",sf_base_att_cha|sf_effects_party,12,"Enables you to ride horses of higher difficulty levels and increases your riding speed and manuever. Slightly increases party speed (Party skill)"),
  ("athletics","Athletics",sf_base_att_str,15,"Improves your running speed. If you use heavy armor, you will be slower. Max Level 6 (Personal skill)"),
  ("shield","Shield",sf_base_att_str,12,"Reduces damage to shields (by 8%% per skill level) and improves shield speed and coverage. Max level: 3 (Personal skill)"),
  ("weapon_master","Weapon Master",sf_base_att_str,15,"Makes it easier to learn weapon proficiencies and increases the proficiency limits. Limits go as: 60, 100, 140, 180, 220, 260, 300, 340, 380, 420. (Personal skill)"),
  ("reserved_9","Reserved Skill 9",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_10","Reserved Skill 10",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_11","Reserved Skill 11",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_12","Reserved Skill 12",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_13","Reserved Skill 13",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."), 
  ("power_draw","Power Draw",sf_base_att_str,15,"Lets character use more powerful bows. Each point to this skill (up to four plus power-draw requirement of the bow) increases bow damage by 14%%. Max Level 5 (Personal skill)"),
  ("power_throw","Power Throw",sf_base_att_str,12,"Each point to this skill increases throwing damage by 10%%.Max Level 5 (Personal skill)"),
  ("power_strike","Power Strike",sf_base_att_str,15,"Each point to this skill increases melee damage by 8%%. Max Level 5 (Personal skill)"),
  ("ironflesh","Ironflesh",sf_base_att_str,15,"Each point to this skill increases hit points by +2. (Personal skill)"), 
  ("reserved_14","Reserved Skill 14",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_15","Reserved Skill 15",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_16","Reserved Skill 16",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_17","Reserved Skill 17",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
  ("reserved_18","Reserved Skill 18",sf_base_att_str|sf_inactive,10,"This is a reserved skill."), 
]