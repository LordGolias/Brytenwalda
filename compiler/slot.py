from .generic_entity import GenericEntity

import source.slots_party


class Slot(GenericEntity):
    """
    Slots are generated by creating the slot and allocating a number of slots
    for it. In the simplest case, the slot corresponds to 1 slot, but some slots
    require more than one slot to be sequentially followed by others
    (e.g. `town_trade_routes` requires X slots, one for each trade route).

    These extra slots are stored in `_index_shift` that stores the extra shift that
    a slot requires.
    """
    tag = 'slot'
    raw_objects = source.slots_party.slots

    _index_shift = 0

    def __init__(self, index, id, slots_allocated):
        # index => position in the list of slots
        super(Slot, self).__init__(index + Slot._index_shift, id)
        self._slots_allocated = slots_allocated

        Slot._index_shift += slots_allocated - 1

    @property
    def slots_allocated(self):
        return self._slots_allocated
