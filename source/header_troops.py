from .header_common import bignum

###################################################
# header_troops.py
# This file contains declarations for troops
# DO NOT EDIT THIS FILE!
###################################################

#Troop flags chief cambios
tf_male           = 0
tf_female         = 1
tf_alto         = 2
tf_alta         = 3
tf_bajo         = 4
tf_baja         = 5
tf_oso         = 6
tf_osa         = 7
tf_undead         = 8
#tf_nino         = 8
troop_type_mask   = 0x0000000f
tf_hero              = 0x00000010
tf_inactive          = 0x00000020
tf_unkillable        = 0x00000040
tf_allways_fall_dead = 0x00000080
tf_no_capture_alive  = 0x00000100
tf_mounted           = 0x00000400 #Troop's movement speed on map is determined by riding skill.
tf_is_merchant       = 0x00001000 #When set, troop does not equip stuff he owns
tf_randomize_face    = 0x00008000 #randomize face at the beginning of the game.

tf_guarantee_boots            = 0x00100000
tf_guarantee_armor            = 0x00200000
tf_guarantee_helmet           = 0x00400000
tf_guarantee_gloves           = 0x00800000
tf_guarantee_horse            = 0x01000000
tf_guarantee_shield           = 0x02000000
tf_guarantee_ranged           = 0x04000000
tf_unmoveable_in_party_window = 0x10000000

# Character attributes...
ca_strength     = 0
ca_agility      = 1
ca_intelligence = 2
ca_charisma     = 3

wpt_one_handed_weapon = 0
wpt_two_handed_weapon = 1
wpt_polearm           = 2
wpt_archery           = 3
wpt_crossbow          = 4
wpt_throwing          = 5
wpt_firearm           = 6


#personality modifiers:
# courage 8 means neutral
courage_4  = 0x0004
courage_5  = 0x0005
courage_6  = 0x0006
courage_7  = 0x0007
courage_8  = 0x0008
courage_9  = 0x0009
courage_10 = 0x000A
courage_11 = 0x000B
courage_12 = 0x000C
courage_13 = 0x000D
courage_14 = 0x000E
courage_15 = 0x000F

aggresiveness_1  = 0x0010
aggresiveness_2  = 0x0020
aggresiveness_3  = 0x0030
aggresiveness_4  = 0x0040
aggresiveness_5  = 0x0050
aggresiveness_6  = 0x0060
aggresiveness_7  = 0x0070
aggresiveness_8  = 0x0080
aggresiveness_9  = 0x0090
aggresiveness_10 = 0x00A0
aggresiveness_11 = 0x00B0
aggresiveness_12 = 0x00C0
aggresiveness_13 = 0x00D0
aggresiveness_14 = 0x00E0
aggresiveness_15 = 0x00F0

is_bandit        = 0x0100
#-----------------------------------
#these also in sentences.py
tsf_site_id_mask = 0x0000ffff
tsf_entry_mask   = 0x00ff0000
tsf_entry_bits   = 16

def entry(n):
  return (((n) << tsf_entry_bits) & tsf_entry_mask)
#-------------------------------------

str_3            = bignum | 0x00000003
str_4            = bignum | 0x00000004
str_5            = bignum | 0x00000005
str_6            = bignum | 0x00000006
str_7            = bignum | 0x00000007
str_8            = bignum | 0x00000008
str_9            = bignum | 0x00000009
str_10           = bignum | 0x0000000a
str_11           = bignum | 0x0000000b
str_12           = bignum | 0x0000000c
str_13           = bignum | 0x0000000d
str_14           = bignum | 0x0000000e
str_15           = bignum | 0x0000000f
str_16           = bignum | 0x00000010
str_17           = bignum | 0x00000011
str_18           = bignum | 0x00000012
str_19           = bignum | 0x00000013
str_20           = bignum | 0x00000014
str_21           = bignum | 0x00000015
str_22           = bignum | 0x00000016
str_23           = bignum | 0x00000017
str_24           = bignum | 0x00000018
str_25           = bignum | 0x00000019
str_26           = bignum | 0x0000001a
str_27           = bignum | 0x0000001b
str_28           = bignum | 0x0000001c
str_29           = bignum | 0x0000001d
str_30           = bignum | 0x0000001e

agi_3            = bignum | 0x00000300
agi_4            = bignum | 0x00000400
agi_5            = bignum | 0x00000500
agi_6            = bignum | 0x00000600
agi_7            = bignum | 0x00000700
agi_8            = bignum | 0x00000800
agi_9            = bignum | 0x00000900
agi_10           = bignum | 0x00000a00
agi_11           = bignum | 0x00000b00
agi_12           = bignum | 0x00000c00
agi_13           = bignum | 0x00000d00
agi_14           = bignum | 0x00000e00
agi_15           = bignum | 0x00000f00
agi_16           = bignum | 0x00001000
agi_17           = bignum | 0x00001100
agi_18           = bignum | 0x00001200
agi_19           = bignum | 0x00001300
agi_20           = bignum | 0x00001400
agi_21           = bignum | 0x00001500
agi_22           = bignum | 0x00001600
agi_23           = bignum | 0x00001700
agi_24           = bignum | 0x00001800
agi_25           = bignum | 0x00001900
agi_26           = bignum | 0x00001a00
agi_27           = bignum | 0x00001b00
agi_28           = bignum | 0x00001c00
agi_29           = bignum | 0x00001d00
agi_30           = bignum | 0x00001e00

int_3            = bignum | 0x00030000
int_4            = bignum | 0x00040000
int_5            = bignum | 0x00050000
int_6            = bignum | 0x00060000
int_7            = bignum | 0x00070000
int_8            = bignum | 0x00080000
int_9            = bignum | 0x00090000
int_10           = bignum | 0x000a0000
int_11           = bignum | 0x000b0000
int_12           = bignum | 0x000c0000
int_13           = bignum | 0x000d0000
int_14           = bignum | 0x000e0000
int_15           = bignum | 0x000f0000
int_16           = bignum | 0x00100000
int_17           = bignum | 0x00110000
int_18           = bignum | 0x00120000
int_19           = bignum | 0x00130000
int_20           = bignum | 0x00140000
int_21           = bignum | 0x00150000
int_22           = bignum | 0x00160000
int_23           = bignum | 0x00170000
int_24           = bignum | 0x00180000
int_25           = bignum | 0x00190000
int_26           = bignum | 0x001a0000
int_27           = bignum | 0x001b0000
int_28           = bignum | 0x001c0000
int_29           = bignum | 0x001d0000
int_30           = bignum | 0x001e0000


cha_3            = bignum | 0x03000000
cha_4            = bignum | 0x04000000
cha_5            = bignum | 0x05000000
cha_6            = bignum | 0x06000000
cha_7            = bignum | 0x07000000
cha_8            = bignum | 0x08000000
cha_9            = bignum | 0x09000000
cha_10           = bignum | 0x0a000000
cha_11           = bignum | 0x0b000000
cha_12           = bignum | 0x0c000000
cha_13           = bignum | 0x0d000000
cha_14           = bignum | 0x0e000000
cha_15           = bignum | 0x0f000000
cha_16           = bignum | 0x10000000
cha_17           = bignum | 0x11000000
cha_18           = bignum | 0x12000000
cha_19           = bignum | 0x13000000
cha_20           = bignum | 0x14000000
cha_21           = bignum | 0x15000000
cha_22           = bignum | 0x16000000
cha_23           = bignum | 0x17000000
cha_24           = bignum | 0x18000000
cha_25           = bignum | 0x19000000
cha_26           = bignum | 0x1a000000
cha_27           = bignum | 0x1b000000
cha_28           = bignum | 0x1c000000
cha_29           = bignum | 0x1d000000
cha_30           = bignum | 0x1e000000

level_mask       = 0x000000FF
level_bits       = 32

def level(v):
  if (v > level_mask):
    v = level_mask
  return (bignum|v) << level_bits
  
def_attrib = str_5 | agi_5 | int_4 | cha_4

# Weapon proficiencies:
one_handed_bits = 0
two_handed_bits = 10
polearm_bits    = 20
archery_bits    = 30
crossbow_bits   = 40
throwing_bits   = 50
firearm_bits    = 60

num_weapon_proficiencies = 7
def wp_one_handed(x):
  return (((bignum | x) & 0x3FF) << one_handed_bits)
def wp_two_handed(x):
  return (((bignum | x) & 0x3FF) << two_handed_bits)
def wp_polearm(x):
  return (((bignum | x) & 0x3FF) << polearm_bits)
def wp_archery(x):
  return (((bignum | x) & 0x3FF) << archery_bits)
def wp_crossbow(x):
  return (((bignum | x) & 0x3FF) << crossbow_bits)
def wp_throwing(x):
  return (((bignum | x) & 0x3FF) << throwing_bits)
def wp_firearm(x):
  return (((bignum | x) & 0x3FF) << firearm_bits)

def find_troop(troops,troop_id):
  result = -1
  num_troops = len(troops)
  i_troop = 0
  while (i_troop < num_troops) and (result == -1):
    troop = troops[i_troop]
    if (troop[0] == troop_id):
      result = i_troop
    else:
      i_troop += 1
  return result



def upgrade(troops,troop1_id,troop2_id):
  troop1_no = find_troop(troops,troop1_id)
  troop2_no = find_troop(troops,troop2_id)
  if (troop1_no == -1):
    print("Error with upgrade def: Unable to find troop1-id: " + troop1_id)
  elif (troop2_no == -1):
    print("Error with upgrade def: Unable to find troop2-id: " + troop2_id)
  else:
    cur_troop = troops[troop1_no]
    cur_troop_length = len(cur_troop)
    if cur_troop_length == 11:
      cur_troop[11:11] = [0, 0, 0, troop2_no, 0]
    elif cur_troop_length == 12:
      cur_troop[12:12] = [0, 0, troop2_no, 0]
    elif cur_troop_length == 13:
      cur_troop[13:13] = [0, troop2_no, 0]
    else:
      cur_troop[14:14] = [troop2_no, 0]
      

def upgrade2(troops,troop1_id,troop2_id,troop3_id):
  troop1_no = find_troop(troops,troop1_id)
  troop2_no = find_troop(troops,troop2_id)
  troop3_no = find_troop(troops,troop3_id)
  if (troop1_no == -1):
    print("Error with upgrade2 def: Unable to find troop1-id: " + troop1_id)
  elif (troop2_no == -1):
    print("Error with upgrade2 def: Unable to find troop2-id: " + troop2_id)
  elif (troop3_no == -1):
    print("Error with upgrade2 def: Unable to find troop3-id: " + troop3_id)
  else:
    cur_troop = troops[troop1_no]
    cur_troop_length = len(cur_troop)
    if cur_troop_length == 11:
      cur_troop[11:11] = [0, 0, 0, troop2_no, troop3_no]
    elif cur_troop_length == 12:
      cur_troop[12:12] = [0, 0, troop2_no, troop3_no]
    elif cur_troop_length == 13:
      cur_troop[13:13] = [0, troop2_no, troop3_no]
    else:
      cur_troop[14:14] = [troop2_no, troop3_no]


####################################################################################################################
# Some constant and function declarations
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
   n = 0
   r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
   n |= wp_one_handed(x)
   n |= wp_two_handed(x)
   n |= wp_polearm(x)
   n |= wp_archery(x) #chief quita para hacerlo especifico
   n |= wp_crossbow(x) #chief quita para hacerlo especifico
   n |= wp_throwing(x)
   n |= wp_firearm(x) #chief anade para hondas//slingshots
   return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wp_archer(x):
   n = 0
   r = 10 + int(x / 10)
   n |= wp_one_handed(x-12)
   n |= wp_two_handed(x-30)
   n |= wp_polearm(x-5)
   n |= wp_archery(x+20) #chief quita para hacerlo especifico
   n |= wp_crossbow(x+20) #chief quita para hacerlo especifico
   n |= wp_throwing(x)
   n |= wp_firearm(x+20)
   return n


#Warrior
def_attrib = str_16 | agi_9 | int_6 | cha_8
def_attrib2 = str_22 | agi_14 | int_8 | cha_10
def_attrib3 = str_30 | agi_20 | int_12 | cha_14
def_attrib_multiplayer = str_14 | agi_14 | int_9 | cha_9

#Ranged
basic_ranged_attrib = str_10|agi_16|int_8|cha_7
veteran_ranged_attrib = str_17|agi_22|int_8|cha_7
elite_ranged_attrib = str_24|agi_30|int_12|cha_10

lord_attrib = str_23|agi_19|int_18|cha_22|level(32)

#cambiado chief
knight_attrib_1 = str_26|agi_26|int_17|cha_20|level(34)
knight_attrib_2 = str_27|agi_27|int_19|cha_22|level(38)
knight_attrib_3 = str_28|agi_28|int_23|cha_24|level(42)
knight_attrib_4 = str_29|agi_29|int_26|cha_26|level(46)
knight_attrib_5 = str_30|agi_30|int_30|cha_30|level(52)

reserved = 0

no_scene = 0

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.
#chief cambia caras nemchenk
swadian_face_younger_1 = 0x0000000000002001355335371861249200000000001c96520000000000000000
swadian_face_young_1   = 0x00000004400023c1355335371861249200000000001c96520000000000000000
swadian_face_middle_1  = 0x00000008000023c1355335371861249200000000001c96520000000000000000
swadian_face_old_1     = 0x0000000e000023c0355335371861249200000000001c96520000000000000000
swadian_face_older_1   = 0x0000000fc00023c0355335371861249200000000001c96520000000000000000

swadian_face_younger_2 = 0x000000003a0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_young_2   = 0x000000033a0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_middle_2  = 0x00000007ba0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_old_2     = 0x0000000e3b0045c549fddefdffffffff00000000001e6db60000000000000000
swadian_face_older_2   = 0x0000000ffa0045c549fddefdffffffff00000000001e6db60000000000000000
#cambias caras britones termina y empieza jutos
vaegir_face_younger_1 = 0x000000000008234958d1b515664a5aa200000000001f49510000000000000000
vaegir_face_young_1   = 0x000000030008234958d1b515664a5aa200000000001f49510000000000000000
vaegir_face_middle_1  = 0x000000080008234958d1b515664a5aa200000000001f49510000000000000000
vaegir_face_old_1     = 0x0000000dc008234958d1b515664a5aa200000000001f49510000000000000000
vaegir_face_older_1   = 0x0000000fc008234958d1b515664a5aa200000000001f49510000000000000000

vaegir_face_younger_2 = 0x00000000001002c7471d312321b14a9c00000000001ebae90000000000000000
vaegir_face_young_2   = 0x00000002801002c7471d312321b14a9c00000000001ebae90000000000000000
vaegir_face_middle_2  = 0x00000009001002c7471d312321b14a9c00000000001ebae90000000000000000
vaegir_face_old_2     = 0x0000000ec01002c7471d312321b14a9c00000000001ebae90000000000000000
vaegir_face_older_2   = 0x0000000fc01002c7471d312321b14a9c00000000001ebae90000000000000000
#chief cambio jutos y empieza pictos
khergit_face_younger_1 = 0x000000018000d00736db6db6db6db6db00000000001db6db0000000000000000
khergit_face_young_1   = 0x00000005ad00d10736db6db6db6db6db00000000001db6db0000000000000000
khergit_face_middle_1  = 0x0000000a7c00d34736db6db6db6db6db00000000001db6db0000000000000000
khergit_face_old_1     = 0x0000000d1d00d1c736db6db6db6db6db00000000001db6db0000000000000000
khergit_face_older_1   = 0x0000000fff00d1c736db6db6db6db6db00000000001db6db0000000000000000

khergit_face_younger_2 = 0x000000003f0cc00a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_young_2   = 0x00000002bf0cc00a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_middle_2  = 0x00000008bf0cc00a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_old_2     = 0x0000000cbf0cc00a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_older_4   = 0x0000000fff0cc00a0ed1b6adbbadb91200000000001eb8d80000000000000000

khergit_face_younger_3 = 0x00000001bf0ca00a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_young_3   = 0x000000067f0ca00a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_middle_3  = 0x000000087f0ca0470ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_old_3     = 0x0000000c3f0ca3130ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_older_3   = 0x0000000fff0ca3130ed1b6adbbadb91200000000001eb8d80000000000000000

khergit_face_younger_4 = 0x000000003f0c814f0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_young_4   = 0x000000027e0c808f0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_middle_4  = 0x00000006be0c810a0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_old_4     = 0x0000000c3f0c82ca0ed1b6adbbadb91200000000001eb8d80000000000000000
khergit_face_older_4   = 0x0000000fff0c82ca0ed1b6adbbadb91200000000001eb8d80000000000000000
#chief cambio acaba
nord_face_younger_1 = 0x000000000000014104c200928801249200000000001d24100000000000000000
nord_face_young_1   = 0x000000044000014104c200928801249200000000001d24100000000000000000
nord_face_middle_1  = 0x000000084000014104c200928801249200000000001d24100000000000000000
nord_face_old_1     = 0x0000000e0000014104c200928801249200000000001d24100000000000000000
nord_face_older_1   = 0x0000000e0000014004c200928801249200000000001d24100000000000000000

nord_face_younger_2 = 0x000000002b00218a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_young_2   = 0x000000036b00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_middle_2  = 0x00000007eb00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_old_2     = 0x0000000deb00234a5bfcbdbb67b7ff7f00000000001eeb6f0000000000000000
nord_face_older_2   = 0x0000000feb0023465bfcbdbb67b7ff7f00000000001eeb6f0000000000000000

rhodok_face_younger_1 = 0x0000000000003144355355370861008200000000001c96520000000000000000
rhodok_face_young_1   = 0x0000000500003141355355370861008200000000001c96520000000000000000
rhodok_face_middle_1  = 0x0000000840003141355355370861008200000000001c96520000000000000000
rhodok_face_old_1     = 0x0000000dc0003192355355370861008200000000001c96520000000000000000
rhodok_face_older_1   = 0x0000000fc0003192355355370861008200000000001c96520000000000000000

rhodok_face_younger_2 = 0x000000003e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_young_2   = 0x000000037e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_middle_2  = 0x000000083e0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_old_2     = 0x0000000dfe0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
rhodok_face_older_2   = 0x0000000ffe0040c649fc9e6f54b6dbbf00000000001d7b270000000000000000
#chief cambia
man_face_younger_1 = 0x000000003f0c1280478b74ca9a6ecd5c00000000001d39120000000000000000
man_face_young_1   = 0x000000033f0c1281478b74ca9a6ecd5c00000000001d39120000000000000000
man_face_middle_1  = 0x0000000cff0c1281478b74ca9a6ecd5c00000000001d39120000000000000000
man_face_old_1     = 0x0000000fff0c1281478b74ca9a6ecd5c00000000001d39120000000000000000
man_face_older_1   = 0x0000000fff0c1292478b74ca9a6ecd5c00000000001d39120000000000000000

man_face_younger_2 = 0x000000002c045184475aa2a4c9bc48a800000000001dca250000000000000000
man_face_young_2   = 0x000000046c045184475aa2a4c9bc48a800000000001dca250000000000000000
man_face_middle_2  = 0x0000000e6c045184475aa2a4c9bc48a800000000001dca250000000000000000
man_face_old_2     = 0x0000000fec045184475aa2a4c9bc48a800000000001dca250000000000000000
man_face_older_2   = 0x0000000fec0451c0475aa2a4c9bc48a800000000001dca250000000000000000

bandit_face_younger_1 = 0x00000000391071443a5d4e491a136b0d00000000001e99140000000000000000
bandit_face_young_1   = 0x00000005f91071443a5d4e491a136b0d00000000001e99140000000000000000
bandit_face_middle_1  = 0x0000000d391071443a5d4e491a136b0d00000000001e99140000000000000000
bandit_face_old_1     = 0x0000000ff91071443a5d4e491a136b0d00000000001e99140000000000000000
bandit_face_older_1   = 0x0000000ff91071853a5d4e491a136b0d00000000001e99140000000000000000

bandit_face_younger_2 = 0x0000000016089111316b361aaf74e41d00000000001e469a0000000000000000
bandit_face_young_2   = 0x00000004d6089111316b361aaf74e41d00000000001e469a0000000000000000
bandit_face_middle_2  = 0x0000000b96089111316b361aaf74e41d00000000001e469a0000000000000000
bandit_face_old_2     = 0x0000000fd608a111316b361aaf74e41d00000000001e469a0000000000000000
bandit_face_older_2   = 0x0000000fd6089100316b361aaf74e41d00000000001e469a0000000000000000
#chief bandidos acaba
#quastuosa chief empieza
quastuosa_woman_face_1 = 0x0000000199041002736b7b6b14cab89b00000000001a390d0000000000000000
quastuosa_woman_face_2 = 0x00000001ae10500129a5aeb52b3a186300000000001d44dc0000000000000000
quastuosa_woman_face_3 = 0x000000018010800116ee82411c98cc6300000000001d169c0000000000000000
quastuosa_woman_face_4 = 0x0000000182007003689d8cb92a70c69b00000000001ca85a0000000000000000
quastuosa_woman_face_5 = 0x000000048000900624ddb1d75b7d653400000000001e6b1a0000000000000000
quastuosa_woman_face_6 = 0x0000000480000005450b0f48dd2568d600000000001deb740000000000000000
#quastuosa termina
#chief caras de sacerdotes batalla
sac_face_younger_1 = 0x000000003100000e478b8a27137238ec00000000001e651c0000000000000000
sac_face_young_1   = 0x000000023100000e478b8a27137238ec00000000001e651c0000000000000000
sac_face_middle_1  = 0x000000043100000e478b8a27137238ec00000000001e651c0000000000000000
sac_face_old_1     = 0x0000000e3100000e478b8a27137238ec00000000001e651c0000000000000000
sac_face_older_1   = 0x0000000ff100000e478b8a27137238ec00000000001e651c0000000000000000

sac_face_younger_2 = 0x000000000208e5d2485d71cb1b7346db00000000001da72d0000000000000000
sac_face_young_2   = 0x000000030208e5d2485d71cb1b7346db00000000001da72d0000000000000000
sac_face_middle_2  = 0x000000090208e5d2485d71cb1b7346db00000000001da72d0000000000000000
sac_face_old_2     = 0x0000000e4208e5d2485d71cb1b7346db00000000001da72d0000000000000000
sac_face_older_2   = 0x0000000fc208e5d2485d71cb1b7346db00000000001da72d0000000000000000


sac_face_1    = sac_face_younger_1
sac_face_2    = sac_face_older_2
#chief sacerdotes acaba
merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

#chief ampliado
khergit_woman_face_1 = 0x000000026d10c0011854c9ed2c79345100000000001ec9f50000000000000000
khergit_woman_face_2 = 0x000000003900c00448d5aa6c5235591400000000001ed88c0000000000000000
khergit_woman_face_3 = 0x000000097f08e0013b996ddc93cd58df00000000001eaa630000000000000000
khergit_woman_face_4 = 0x000000095c0cf0053a646ae69b31c4b200000000001eab240000000000000000
khergit_woman_face_5 = 0x0000000fed1020011854c9ed2c79345100000000001ec9f50000000000000000
khergit_woman_face_6 = 0x0000000fcc08b00152da31d4997638f600000000001cb7210000000000000000
#chief ampliado

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2
#cambiados chief bandidos
bandit_face1  = bandit_face_young_1
bandit_face2  = bandit_face_older_2
#cambiados chief bandidos acaba
undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#
tf_guaranteeexhorhelm = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield
tho = tf_hero|tf_unmoveable_in_party_window|tf_guarantee_all
