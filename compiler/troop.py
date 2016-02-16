#######################################################################################  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string)..
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
####################################################################################################################
import logging

from .generic_entity import GenericEntity

import source.header_troops as h_trp
import source.header_skills as h_skills
import source.module_troops as m_troops

from source.process_common import convert_to_identifier, replace_spaces


# hard-coded value in M&B
_MAX_ITEMS = 64


class Troop(GenericEntity):
    tag = 'trp'
    raw_objects = m_troops.troops

    def __init__(self, index, id, name, plural, flags, scene, reserved, faction,
                 inventory, attributes, proficiencies, skills, face_code,
                 face_code2=0, image=0, upgradable1=0, upgradable2=0):
        super(Troop, self).__init__(index, id)
        self._name = name
        self._plural = plural
        self._flags = flags
        if isinstance(scene, list):
            self._scene = scene[0]
            self._scene_entry = scene[1]
        else:
            self._scene = scene
            self._scene_entry = h_trp.entry(0)

        if reserved != 0:
            logging.warning('Reserved in troop "%d" is not 0' % id)
        self._reserved = 0
        self._faction = faction

        if len(inventory) > _MAX_ITEMS:
            raise IndexError('Inventory size of troop cannot exceed 64 items. '
                             '%d item/s too many in "%s"' % (len(inventory) - _MAX_ITEMS, self.no_tag_id))
        self._inventory = inventory
        self._attributes = attributes
        self._proficiencies = proficiencies
        self._skills = skills
        self._face_code = face_code
        self._face_code2 = face_code2
        self._image = image
        self._upgradable_to = (upgradable1, upgradable2)

    def export(self, compiler):
        result = ''

        faction_index = compiler.index(self._faction)
        scene_index = compiler.index(self._scene)
        scene_index |= self._scene_entry

        result += "%s %s %s %s %d %d %d %d " % (
            convert_to_identifier(self._id),
            replace_spaces(self._name),
            replace_spaces(self._plural),
            replace_spaces(str(self._image)),
            self._flags, scene_index, self._reserved, faction_index)

        result += '%d %d' % tuple(compiler.index(x) for x in self._upgradable_to)

        result += '\n  '

        for inventory_item in self._inventory:
            result += "%d 0 " % compiler.index(inventory_item)

        for i in range(_MAX_ITEMS - len(self._inventory)):
            result += "-1 0 "
        result += "\n "

        strength = (self._attributes & 0xff)
        agility = ((self._attributes >> 8) & 0xff)
        intelligence = ((self._attributes >> 16) & 0xff)
        charisma = ((self._attributes >> 24) & 0xff)
        starting_level = (self._attributes >> h_trp.level_bits) & h_trp.level_mask

        result += " %d %d %d %d %d\n" % (strength, agility, intelligence, charisma,
                                         starting_level)

        wp_word = self._proficiencies
        for wp in range(h_trp.num_weapon_proficiencies):
            wp_level = wp_word & 0x3FF
            result += " %d" % wp_level
            wp_word >>= 10
        result += "\n"

        for i in range(h_skills.num_skill_words):
            result += "%d " % ((self._skills >> (i * 32)) & 0xffffffff)
        result += "\n  "

        for fckey in (self._face_code, self._face_code2):
            word_keys = []
            for word_no in range(4):
                word_keys.append((fckey >> (64 * word_no)) & 0xFFFFFFFFFFFFFFFF)
            for word_no in range(4):
                result += "%d " % word_keys[(4 - 1) - word_no]

        result += '\n\n'
        return result
