from .header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_religion_relations = [
    ("outlaws", -0.05), ("mountain_bandits", -0.05), ("forest_bandits", -0.05)
]

default_kingdom_relations = [
    ("outlaws", -0.05), ("peasant_rebels", -0.1),
    ("deserters", -0.02), ("mountain_bandits", -0.05),
    ("forest_bandits", -0.05)
]

factions = [
    ("no_faction", "No Faction", 0, 0.9, [], []),
    ("commoners", "Commoners", 0, 0.1, [
        ("player_faction", 0.1)
    ], []),

    ("outlaws", "Outlaws", max_player_rating(-30), 0.5, [
        ("commoners", -0.6), ("player_faction", -0.15),
    ], [], 0x888888),
    # Factions before this point are hardwired into the game end their order should not be changed.

    ("neutral", "Neutral", 0, 0.1, [
        ("player_faction", 0.0)
    ], [], 0xFFFFFF),
    ("innocents", "Innocents", ff_always_hide_label, 0.5, [
        ("outlaws", -0.05)
    ], []),
    ("merchants", "Merchants", ff_always_hide_label, 0.5, [
        ("outlaws", -0.5)
    ], []),

    ("dark_knights", "{!}Dark Knights", 0, 0.5, [
        ("innocents", -0.9), ("player_faction", -0.4)
    ], []),

    ("culture_1", "{!}culture_1", 0, 0.9, [], []),
    ("culture_2", "{!}culture_2", 0, 0.9, [], []),
    ("culture_3", "{!}culture_3", 0, 0.9, [], []),
    ("culture_4", "{!}culture_4", 0, 0.9, [], []),
    ("culture_5", "{!}culture_5", 0, 0.9, [], []),
    ("culture_6", "{!}culture_6", 0, 0.9, [], []),
    ("culture_7", "{!}culture_7", 0, 0.9, [], []),
    ("culture_8", "{!}culture_8", 0, 0.9, [], []),
    ("culture_9", "{!}culture_9", 0, 0.9, [], []),
    ("culture_10", "{!}culture_10", 0, 0.9, [], []),
    ("culture_11", "{!}culture_11", 0, 0.9, [], []),
    ("culture_12", "{!}culture_12", 0, 0.9, [], []),
    ("culture_13", "{!}culture_13", 0, 0.9, [], []),
    ("culture_14", "{!}culture_14", 0, 0.9, [], []),
    ("culture_15", "{!}culture_15", 0, 0.9, [], []),
    ("culture_16", "{!}culture_16", 0, 0.9, [], []),
    ("culture_17", "{!}culture_17", 0, 0.9, [], []),
    ("culture_18", "{!}culture_18", 0, 0.9, [], []),
    ("culture_19", "{!}culture_19", 0, 0.9, [], []),
    ("culture_20", "{!}culture_20", 0, 0.9, [], []),
    ("culture_21", "{!}culture_21", 0, 0.9, [], []),
    ("culture_22", "{!}culture_22", 0, 0.9, [], []),
    ("culture_23", "{!}culture_23", 0, 0.9, [], []),
    ("culture_24", "{!}culture_24", 0, 0.9, [], []),
    ("culture_25", "{!}culture_25", 0, 0.9, [], []),
    ("culture_26", "{!}culture_26", 0, 0.9, [], []),
    ("culture_27", "{!}culture_27", 0, 0.9, [], []),
    ("culture_28", "{!}culture_28", 0, 0.9, [], []),
    ("culture_29", "{!}culture_29", 0, 0.9, [], []),
    ("culture_30", "{!}culture_30", 0, 0.9, [], []),
    ("culture_31", "{!}culture_31", 0, 0.9, [], []),

    # -#-#-#-#-#-#-#-#-#-#-#-#-#-#
    # -#-#-#Hunting chief Mod begin#-#-#-#
    # -#-#-#-#-#-#-#-#-#-#-#-#-#-#
    ("wild_animals", "Wild Animals", 0, 0.1, [
        ("player_faction", -0.85)
    ], [], 0xFFFFFF),
    # -#-#-#-#-#-#-#-#-#-#-#-#-#-#
    # -#-#-#Hunting chief Mod end#-#-#-#
    # -#-#-#-#-#-#-#-#-#-#-#-#-#-#

    ("player_faction", "Player Faction", 0, 0.9, [], [], 0x000000FF),
    ("player_supporters_faction", "Player's Supporters", 0, 0.9, [
        ("player_faction", 1.00), ("outlaws", -0.08), ("peasant_rebels", -0.1),
        ("deserters", -0.08), ("mountain_bandits", -0.08),
        ("forest_bandits", -0.08)
    ], [], 0xDDFF00),

    ("kingdom_1", "Cantware", 0, 0.9, default_kingdom_relations + [
        ("pagans", -0.05)
    ], [], 0xFF0000),
    ("kingdom_2", "Suth Seaxe", 0, 0.9, default_kingdom_relations, [], 0x8800FF),
    ("kingdom_3", "East Seaxna", 0, 0.9, default_kingdom_relations, [], 0x88FF88),
    ("kingdom_4", "East Engla", 0, 0.9, default_kingdom_relations + [
        ("kingdom_9", -0.7), ("kingdom_3", -0.03), ("kingdom_13", 0.1)
    ], [], 0xBB99FF),
    ("kingdom_5", "Gewissae", 0, 0.9, default_kingdom_relations + [
        ("kingdom_13", 0.3), ("kingdom_9", -0.1), ("kingdom_8", -0.1),
        ("kingdom_7", -0.1)
    ], [], 0xFFAA88),
    ("kingdom_6", "Hwicce", 0, 0.9, default_kingdom_relations + [
        ("kingdom_9", 0.7), ("kingdom_26", -0.05)
    ], [], 0x3355FF),
    ("kingdom_7", "Glastenic", 0, 0.9, default_kingdom_relations + [
        ("kingdom_8", 0.1), ("kingdom_11", 0.7), ("kingdom_22", 0.5)
    ], [], 0xBBFF00),
    ("kingdom_8", "Dumnonia", 0, 0.9, default_kingdom_relations + [
        ("kingdom_7", 0.1), ("kingdom_11", 0.05), ("kingdom_23", 0.05),
        ("kingdom_5", -0.1), ("kingdom_24", 0.05)
    ], [], 0xFF5533),
    ("kingdom_9", "Mierce", 0, 0.9, default_kingdom_relations + [
        ("christians", -0.05),
        ("kingdom_13", -0.7), ("kingdom_5", -0.1), ("kingdom_4", -0.7),
        ("kingdom_11", 0.2), ("kingdom_23", 0.06), ("kingdom_6", 0.7),
        ("kingdom_14", 0.03)
    ], [], 0xFF0088),
    ("kingdom_10", "Ynys Manau", 0, 0.9, default_kingdom_relations, [], 0x88FFBB),
    ("kingdom_11", "Pengwern", 0, 0.9, default_kingdom_relations + [
        ("kingdom_7", 0.7), ("kingdom_26", 0.05), ("kingdom_22", 0.7),
        ("kingdom_9", 0.2), ("kingdom_13", -0.1)
    ], [], 0xFFBB00),
    ("kingdom_12", "Goutodin", 0, 0.9, default_kingdom_relations + [
        ("kingdom_13", -0.1)
    ], [], 0xEE1166),
    ("kingdom_13", "Bernaccia", 0, 0.9, default_kingdom_relations + [
        ("pagans", -0.05),
        ("kingdom_12", -0.1), ("kingdom_9", -0.7), ("kingdom_15", -0.03),
        ("kingdom_5", 0.3), ("kingdom_19", 0.5)
    ], [], 0x88FFFF),
    ("kingdom_14", "Lindisware", 0, 0.9, default_kingdom_relations + [
        ("christians", -0.05),
        ("kingdom_13", -0.1), ("kingdom_9", 0.03)
    ], [], 0x88CC00),
    ("kingdom_15", "Rheged", 0, 0.9, default_kingdom_relations + [
        ("kingdom_18", -0.1)
    ], [], 0x6644FF),
    ("kingdom_16", "Crafu", 0, 0.9, default_kingdom_relations, [], 0xCC00DD),
    ("kingdom_17", "Connaught", 0, 0.9, default_kingdom_relations + [
        ("kingdom_30", -0.1)
    ], [], 0xAA00FF),
    ("kingdom_18", "Alt Clut", 0, 0.9, default_kingdom_relations + [
        ("kingdom_13", -0.05), ("kingdom_15", -0.1)
    ], [], 0xFFDD00),
    ("kingdom_19", "Dal Riata", 0, 0.9, default_kingdom_relations + [
        ("kingdom_13", 0.5),
        ("kingdom_20", -0.7), ("kingdom_29", 0.1), ("kingdom_30", -0.1)
    ], [], 0xFF00EE),
    ("kingdom_20", "Fortriu", 0, 0.9, default_kingdom_relations + [
        ("kingdom_19", -0.7)
    ], [], 0xBB99FF),
    ("kingdom_21", "Ceredigion", 0, 0.9, default_kingdom_relations + [
    ], [], 0x88FF00),
    ("kingdom_22", "Powys", 0, 0.9, default_kingdom_relations + [
        ("kingdom_11", 0.7), ("kingdom_7", 0.5)
    ], [], 0xCC5511),
    ("kingdom_23", "Gwynedd", 0, 0.9, default_kingdom_relations + [
        ("kingdom_9", 0.06),
        ("kingdom_11", 0.07)
    ], [], 0xFF8899),
    ("kingdom_24", "Dyfed", 0, 0.9, default_kingdom_relations, [], 0x77DDFF),
    ("kingdom_25", "Brycheiniog", 0, 0.9, default_kingdom_relations, [], 0xFFFF00),
    ("kingdom_26", "Gwent", 0, 0.9, default_kingdom_relations + [
        ("kingdom_6", -0.05), ("kingdom_11", 0.05)
    ], [], 0xFF88DD),
    ("kingdom_27", "Laigin", 0, 0.9, default_kingdom_relations + [
        ("kingdom_28", -0.1)
    ], [], 0x0000FF),
    ("kingdom_28", "Mumain", 0, 0.9, default_kingdom_relations + [
        ("kingdom_27", -0.1), ("kingdom_17", -0.1)
    ], [], 0xDDFFCC),
    ("kingdom_29", "Ulaid", 0, 0.9, default_kingdom_relations + [
        ("kingdom_30", -0.1), ("kingdom_19", 0.1)
    ], [], 0xFF8800),
    ("kingdom_30", "Ui Neill", 0, 0.9, default_kingdom_relations + [
        ("kingdom_29", -0.1), ("kingdom_19", -0.1)
    ], [], 0xDD2244),
    ("kingdom_31", "Airgialla", 0, 0.9, default_kingdom_relations + [
        ("kingdom_29", -0.1)
    ], [], 0x66BBFF),

    ("kingdoms_end", "{!}kingdoms_end", 0, 0, [], []),

    ("robber_knights", "{!}robber_knights", 0, 0.1, [], []),

    ("khergits", "{!}Khergits", 0, 0.5, [
        ("player_faction", 0.0)
    ], []),
    ("black_khergits", "{!}Black Khergits", 0, 0.5, [
        ("player_faction", -0.3), ("kingdom_1", -0.02), ("kingdom_2", -0.02)
    ], []),

    ("neko", "Neko", 0, 0.5, [("player_faction", -1.0), ], [], 0x888888),

    ("arrians", "Arrians", 0, 0.5, [
        ("player_faction", -1.0)
    ], []),

    ("eadfrith", "Eadfrith", 0, 0.5, [
        ("player_faction", -1.0)
    ], []),

    ("christians", "Christian", 0, 0.5, default_religion_relations + [
        ("pagans", -0.05),
    ], []),
    ("pagans", "Pagan", 0, 0.5, default_religion_relations + [
        ("christians", -0.05),
    ], []),

    ("manhunters", "Manhunters", 0, 0.5, [
        ("outlaws", -0.6), ("player_faction", 0.1)
    ], []),
    ("deserters", "Deserters", 0, 0.5, [
        ("outlaws", -0.5), ("manhunters", -0.6), ("merchants", -0.5),
        ("player_faction", -0.1)
    ], [], 0x888888),

    # Scoti, frank and Dena pirates.
    ("mountain_bandits", "Sea Warriors", 0, 0.5, [
        ("outlaws", -0.5), ("commoners", -0.2), ("merchants", -0.5),
        ("manhunters", -0.6), ("player_faction", -0.15),
    ], [], 0x888888),
    ("forest_bandits", "Forest Bandits", 0, 0.5, [
        ("outlaws", -0.5), ("commoners", -0.2), ("merchants", -0.5),
        ("manhunters", -0.6), ("player_faction", -0.15),
    ], [], 0x888888),

    ("undeads", "{!}Undeads", max_player_rating(-30), 0.5, [
        ("commoners", -0.7), ("player_faction", -0.5)
    ], []),
    ("slavers", "{!}Slavers", 0, 0.1, [], []),
    ("peasant_rebels", "{!}Peasant Rebels", 0, 1.0, [
        ("noble_refugees", -1.0), ("player_faction", -0.4)
    ], []),
    ("noble_refugees", "{!}Noble Refugees", 0, 0.5, [], []),
    ("apoyoplayer", "Neutral", 0, 0.9, [
        ("player_faction", 1.00)
    ], [], 0xFFFFFF),

    # slots for new factions below
    ("merc1", "Neutral", 0, 0.9, [
        ("player_faction", 1.00)
    ], [], 0xFFFFFF),
    ("merc2", "Neutral", 0, 0.9, [
        ("player_faction", 1.00)
    ], [], 0xFFFFFF),
    ("merc3", "Neutral", 0, 0.9, [
        ("player_faction", 1.00)
    ], [], 0xFFFFFF),
    ("merc4", "Neutral", 0, 0.9, [
        ("player_faction", 1.00)
    ], [], 0xFFFFFF),
    ("merc5", "Neutral", 0, 0.9, [
        ("player_faction", 1.00)
    ], [], 0xFFFFFF),
    ("merc6", "Neutral", 0, 0.9, [
        ("player_faction", 1.00)
    ], [], 0xFFFFFF),
    ("merc7", "Neutral", 0, 0.9, [
        ("player_faction", 1.00)
    ], [], 0xFFFFFF),
]
