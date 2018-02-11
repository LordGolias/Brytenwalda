####################################################################################################################
# During a dialog, the dialog lines are scanned from top to bottom.
# If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
# If the dialog-line is spoken by another, the first (top-most) matching line is selected.
#
#  Each dialog line contains the following fields:
# 1) Dialogue partner: This should match the person player is talking to.
#    Usually this is a troop-id.
#    You can also use a party-template-id by appending '|party_tpl' to this field.
#    Use the constant 'anyone' if you'd like the line to match anybody.
#    Appending '|plyr' to this field means that the actual line is spoken by the player
#    Appending '|other(troop_id)' means that this line is spoken by a third person on the scene.
#       (You must make sure that this third person is present on the scene)
#
# 2) Starting dialog-state:
#    During a dialog there's always an active Dialog-state.
#    A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
#    If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
#    If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
#    If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
#    If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
#    If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
#    If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
# 3) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.
# 4) Dialog Text (string):
# 5) Ending dialog-state:
#    If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
# 6) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
# 7) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over
####################################################################################################################
import logging
from collections import OrderedDict

import source.module_dialogs as m_dialogs
import source.process_common as p_common

from .generic_entity import GenericEntity


speaker_pos = 0
ipt_token_pos = 1
sentence_conditions_pos = 2
text_pos = 3
opt_token_pos = 4
sentence_consequences_pos = 5
sentence_voice_over_pos = 6


def compile_sentence_tokens(sentences):
    input_tokens = []
    output_tokens = []
    # default states
    _dialog_states = [
        "start", "party_encounter", "prisoner_liberated", "enemy_defeated",
        "party_relieved", "event_triggered", "close_window", "trade",
        "exchange_members", "trade_prisoners", "buy_mercenaries", "view_char",
        "training", "member_chat", "prisoner_chat",
    ]

    dialog_states = OrderedDict()
    for state in _dialog_states:
        dialog_states[state] = 1

    # create output_tokens
    for sentence in sentences:
        output_token = sentence[opt_token_pos]

        try:
            output_token_id = list(dialog_states.keys()).index(output_token)
        except ValueError:
            dialog_states[output_token] = 0
            output_token_id = len(dialog_states) - 1
        output_tokens.append(output_token_id)

    # create input_tokens
    for sentence in sentences:
        input_token = sentence[ipt_token_pos]

        try:
            input_token_id = list(dialog_states.keys()).index(input_token)
            dialog_states[input_token] += 1
        except ValueError:
            input_token_id = -1
            logging.error('Input token "%s" not found in dialog "%s"' %
                          (input_token, sentence))
        input_tokens.append(input_token_id)

    for state in dialog_states:
        if dialog_states[state] == 0:
            logging.error('Dialog state "%s" not used' % state)
    return input_tokens, output_tokens, dialog_states


class Dialog(GenericEntity):
    tag = 'dlga'
    raw_objects = m_dialogs.dialogs

    _auto_ids = {}
    _input_states, _output_states, dialog_states = compile_sentence_tokens(m_dialogs.dialogs)

    def __init__(self, index, partner, start, condition, text, end,
                 consequences, voice_over="NO_VOICEOVER"):
        super(Dialog, self).__init__(index, index)
        self._partner = partner
        self._start = start
        self._condition = condition
        self._text = text
        self._end = end
        self._consequences = consequences
        self._voice_over = voice_over

    @property
    def name(self):
        return "%s[%s -> %s]" % (self.__class__.__name__, self._start, self._end)

    def create_auto_id(self):
        token_ipt = p_common.convert_to_identifier(self._start)
        token_opt = p_common.convert_to_identifier(self._end)

        auto_id = self.tag + "_" + token_ipt + ":" + token_opt

        if auto_id in self._auto_ids and self._auto_ids[auto_id] != self._text:
            number = 1
            new_auto_id = auto_id + "." + str(number)
            while new_auto_id in self._auto_ids:
                number += 1
                new_auto_id = auto_id + "." + str(number)
            auto_id = new_auto_id
        else:
            self._auto_ids[auto_id] = self._text
        return auto_id

    def export(self, compiler):
        result = ''

        dialog_id = self.create_auto_id()

        if isinstance(self._partner, str):
            partner = compiler.index(self._partner)
        elif isinstance(self._partner, int):
            partner = self._partner
        else:
            partner = self._partner.as_index(compiler)

        result += "%s %d %d " % (dialog_id, partner, self._input_states[self._index])
        result += compiler.process_statement_block(
            self.name + "[conditions]", 1, self._condition)

        if self._text:
            result += "%s " % self._text.replace(" ", "_")
        else:
            result += "NO_TEXT "

        result += " %d " % self._output_states[self._index]
        result += compiler.process_statement_block(
            self.name + "[consequences]", 1, self._consequences)

        result += "%s " % self._voice_over
        result += '\n'
        return result

    @property
    def statement_blocks(self):
        return [self._condition, self._consequences]
