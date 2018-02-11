
#################################################################################
# Each item record contains the following fields:
# 1) Item id: used for referencing items in other files.
# The prefix itm_ is automatically added before each item id.
# 2) Item name. Name of item as it'll appear in inventory window
# 3) List of meshes. Each mesh record is a tuple containing the following fields:
#  3.1) Mesh name.
#  3.2) Modifier bits that this mesh matches.
# Note that the first mesh record is the default.
# 4) Item flags. See header_items.py for a list of available flags.
# 5) Item capabilities. Used for which animations this item is used with.
# See header_items.py for a list of available flags.
# 6) Item value.
# 7) Item stats: Bitwise-or of various stats about the item such as:
# weight, abundance(60)fficulty, head_armor, body_armor,leg_armor, etc...
# 8) Modifier bits: Modifiers that can be applied to this item.
# 9) [Optional] Triggers: List of simple triggers to be associated with the item.
# 10) [Optional] Factions: List of factions that item can be found as merchandise.
#################################################################################
from source.process_common import convert_to_identifier, replace_spaces
import source.module_items as m_items
import source.header_items as hi

from .generic_entity import GenericEntity


class Item(GenericEntity):
    tag = 'itm'
    raw_objects = m_items.items

    def __init__(self, index, id, name, meshes, flags, capabilities, slot_no,
                 stats, value, weapon_flags=0, triggers=None, factions_ids=None,
                 factions2_ids=None):
        super(Item, self).__init__(index, id)
        self._name = name
        self._meshes = meshes
        self._flags = flags
        if not isinstance(flags, int):
            raise TypeError('"flags" of %s is not an int' % id)

        if not isinstance(capabilities, int):
            raise TypeError('"capabilities" of %s is not an int: %s' % (id, capabilities))
        self._capabilities = capabilities

        self._slot_no = slot_no
        self._value = value
        if not isinstance(stats, int):
            raise TypeError('"stats" of %s is not an int' % id)
        self._stats = stats

        if not isinstance(weapon_flags, int):
            factions_ids = triggers
            triggers = weapon_flags
            #raise TypeError('"weapon_flags" (9th entry) of "%s" is not an int: %s' % (id, weapon_flags))
            self._weapon_flags = 0
        else:
            self._weapon_flags = weapon_flags

        if factions_ids is None:
            factions_ids = []

        if factions2_ids is None:
            factions2_ids = []

        if triggers is None:
            triggers = []

        self._triggers = triggers

        assert(isinstance(factions_ids, list))
        self._factions = factions_ids
        self._factions2 = factions2_ids

    @property
    def meshes(self):
        return [mesh[0] for mesh in self._meshes]

    def export(self, compiler):
        result = " {id} {name} {name} {meshes_number} ".format(
            id=convert_to_identifier(self._id),
            name=replace_spaces(self._name),
            meshes_number=len(self._meshes))

        for mesh in self._meshes:
            result += " %s %d " % (mesh[0], mesh[1])

        # hp share the same bits as attack type since items cannot have both.
        hp = hi.get_hit_points(self._stats)
        if hi.get_thrust_damage(self._stats) + hi.get_swing_damage(self._stats) >0:
            hp = 0
        result += " %d %d %d %d %f %d %d %d %d %d %d %d %d %d %d %d %d\n" % \
                  (self._flags, self._capabilities, self._slot_no, self._value,
                   hi.get_weight(self._stats),
                   hi.get_abundance(self._stats),
                   hi.get_head_armor(self._stats),
                   hi.get_body_armor(self._stats),
                   hi.get_leg_armor(self._stats),
                   hi.get_difficulty(self._stats),
                   hp,
                   hi.get_speed_rating(self._stats),
                   hi.get_missile_speed(self._stats),
                   hi.get_weapon_length(self._stats),
                   hi.get_max_ammo(self._stats),
                   hi.get_thrust_damage(self._stats),
                   hi.get_swing_damage(self._stats))

        result += " %d\n" % len(self._factions)
        for faction in self._factions:
            result += " %d" % compiler.index(faction)
        if self._factions:
            result += "\n"

        result += "%d\n" % len(self._triggers)
        for trigger in self._triggers:
            result += "%f " % trigger[0]
            result += compiler.process_statement_block(self.name, 1, trigger[1])
            result += "\n"
        result += "\n"

        return result
