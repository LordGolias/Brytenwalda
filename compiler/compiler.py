import logging

from collections import OrderedDict, defaultdict

import source.header_common as h_common
import source.process_common as p_common
import source.header_operations as h_operations

import compiler.objects as objects
from source.statement import StatementBlock


class Compiler(object):

    def __init__(self, export_dir='.', log_dir='.'):
        self._export_dir = export_dir
        self._log_dir = log_dir

        self._custom_tags = []

        # global variables are defined everywhere and start with a "$".
        # The index of this ordered dict contains the index of the
        # global variable, retrieved by `_get_global`.
        self._global_variables = OrderedDict()

        # local variables are defined within a block and start with a ":".
        # Therefore, these are reset on self.process_statement_block.
        # The index of this ordered dict contains the index of the
        # local variable, retrieved by `_get_local`.
        self._local_variables = OrderedDict()

        # Quick strings are defined everywhere and start with a "@".
        # The index of this ordered dict contains the index of the quick string.
        # Quick strings are added by `_get_quick_string_index`.
        self._quick_strings = OrderedDict()

        # a set of all entities defined. Populated during `compile`.
        self._all_entities = set()
        # frequency of entity variables used. Populated during `compile`.
        self._all_used_entities = defaultdict(int)

        # The current statement being processed by process_statement_block.
        # this is used to have more informative log messages
        self._current_statement_name = 'unknown'

    def _get_quick_string_index(self, sentence):
        text = p_common.convert_to_identifier_with_no_lowercase(sentence)
        sentence = p_common.replace_spaces(sentence)

        i = min(20, len(text))
        while i <= len(text):
            auto_id = "qstr_" + text[0:i]
            if auto_id in self._quick_strings:
                # string already exists, don't do anything
                if self._quick_strings[auto_id] == sentence:
                    break
                else:
                    # auto_id exists but contains other sentence.
                    # increase auto_id
                    i += 1
            else:
                # auto_id is free, store sentence
                self._quick_strings[auto_id] = sentence
                break
        else:
            # `"qstr_" + text` is already an auto_id, use numbers
            number = 1
            base_auto_id = "qstr_" + text
            auto_id = base_auto_id + str(number)
            while auto_id in self._quick_strings:
                number += 1
                auto_id = base_auto_id + str(number)
            self._quick_strings[auto_id] = sentence

        return list(self._quick_strings.keys()).index(auto_id)

    def index(self, id, tag=None):
        if not isinstance(id, str):
            return id

        if not tag:
            tag, no_tag_id = id.split("_", 1)  # splits on first occurrence
        else:
            no_tag_id = id

        try:
            object_list = objects.TAG_TO_OBJECT_TYPE[tag].objects
        except KeyError:
            raise KeyError('Tag "%s" of "%s" in "%s" does not exist' %
                           (tag, id, self._current_statement_name))

        self._all_used_entities["%s_%s" % (tag, no_tag_id)] += 1
        try:
            return object_list[no_tag_id].index
        except KeyError:
            logging.error('Object "%s" of "%s" in "%s" does not exist' %
                          (tag, id, self._current_statement_name))
            return 0

    def _get_identifier_value(self, variable):
        if not isinstance(variable, str):
            return variable

        if '_' not in variable:
            raise Exception('Object "%s" in "%s" has no tag' %
                            (variable, self._current_statement_name))
        tag, variable_name = variable.split("_", 1) # splits on first occurrence

        # slots are not transformed into tags via binary operators; they are integers
        if tag == 'slot':
            return self.index(variable_name, tag)

        try:
            tag_index = objects.TAG_TO_TAG_ID[tag]
        except KeyError:
            raise KeyError('Tag "%s" of "%s" in "%s" does not exist' %
                           (tag, variable_name, self._current_statement_name))

        index = self.index(variable_name, tag)

        return index | (tag_index << h_common.op_num_value_bits)

    def _add_local(self, param):
        if param in self._local_variables:
            self._local_variables[param] -= 1
        else:
            self._local_variables[param] = -1

    def _add_global(self, param):
        if param in self._global_variables:
            self._global_variables[param] -= 1
        else:
            self._global_variables[param] = -1

    def _get_local(self, param):
        if param in self._local_variables:
            self._local_variables[param] += 1
        else:
            logging.error('Local variable "%s" in "%s" used but not assigned' %
                          (param, self._current_statement_name))
            self._local_variables[param] = 1
        return list(self._local_variables.keys()).index(param)

    def _get_global(self, param):
        if param in self._global_variables:
            self._global_variables[param] += 1
        else:
            self._global_variables[param] = 1
        return list(self._global_variables.keys()).index(param)

    def _process_param(self, param):

        if not isinstance(param, str):
            return param

        error_message = '"%s" in "%s" is already a global variable, cannot be ' \
                        'a local variable or vice-versa' % \
                        (param[1:], self._current_statement_name)

        if param[0] == '$':
            # it is a global variable
            if param[1:] in self._local_variables:
                logging.error(error_message)
            #check_varible_not_defined(param[1:], local_vars_list)
            result = self._get_global(param[1:])
            result |= h_common.opmask_variable
        elif param[0] == ':':
            # it is a local variable
            if param[1:] in self._global_variables:
                logging.error(error_message)
            result = self._get_local(param[1:])
            result |= h_common.opmask_local_variable
        elif param[0] == '@':
            # it is a quick string, store it.
            result = self._get_quick_string_index(param[1:])
            result |= h_common.opmask_quick_string
        else:
            # it is a variable identifier
            result = self._get_identifier_value(param)

        return result

    def _process_statement(self, op_code, statement):
        result = ''
        if isinstance(statement, (tuple, list)):
            # count assignments of local variables
            if op_code in h_operations.lhs_operations:
                if len(statement) <= 1:
                    raise Exception('lhs operation "%d" in "%s" requires at least one parameter.' %
                                    (op_code, self._current_statement_name))
                param = statement[1]
                if isinstance(param, str) and param[0] == ':':
                    self._add_local(param[1:])

            # count assignments to global variables
            if op_code in (h_operations.lhs_operations +
                               h_operations.global_lhs_operations):
                if len(statement) <= 1:
                    raise Exception('lhs operation "%d" in "%s" requires at least one parameter.' %
                                    (op_code, self._current_statement_name))
                param = statement[1]
                if isinstance(param, str) and param[0] == '$':
                    self._add_global(param[1:])

        else:
            statement = [statement]

        result += "%d %d " % (op_code, len(statement) - 1)

        for i in range(len(statement) - 1):
            result += "%d " % self._process_param(statement[i + 1])

        return result

    def _process_statement_piece(self, statement_block):
        result = ''

        current_depth = 0

        for index, statement in enumerate(statement_block):
            if isinstance(statement, StatementBlock):
                result += self._process_statement_piece(statement)
                continue
            if isinstance(statement, (tuple, list)):
                opcode = statement[0]
            else:
                opcode = statement

            if opcode in [h_operations.try_begin,
                          h_operations.try_for_range,
                          h_operations.try_for_range_backwards,
                          h_operations.try_for_parties,
                          h_operations.try_for_agents,
                          h_operations.try_for_attached_parties,
                          h_operations.try_for_active_players,
                          h_operations.try_for_prop_instances]:
                current_depth += 1
            elif opcode == h_operations.try_end:
                current_depth -= 1

            result += self._process_statement(opcode, statement)

        if current_depth != 0:
            raise Exception('Statement in "%s" does not close all "try_*" '
                            'statements or closes them too many.' %
                            self._current_statement_name)

        return result

    def process_statement_block(self, statement_name, is_can_fail_statement,
                                statement_block):
        self._current_statement_name = statement_name

        self._local_variables = OrderedDict()

        statement_block = StatementBlock(*statement_block)

        result = " %d " % len(statement_block)

        store_script_param_1_uses = 0
        store_script_param_2_uses = 0
        current_depth = 0

        for index, statement in enumerate(statement_block):
            if isinstance(statement, StatementBlock):
                result += self._process_statement_piece(statement)
                continue

            if isinstance(statement, (tuple, list)):
                opcode = statement[0]
            else:
                opcode = statement

            if opcode in [h_operations.try_begin,
                          h_operations.try_for_range,
                          h_operations.try_for_range_backwards,
                          h_operations.try_for_parties,
                          h_operations.try_for_agents,
                          h_operations.try_for_attached_parties,
                          h_operations.try_for_active_players,
                          h_operations.try_for_prop_instances]:
                current_depth += 1
            elif opcode == h_operations.try_end:
                current_depth -= 1
            elif opcode == h_operations.store_script_param_1 or \
                    (opcode == h_operations.store_script_param and statement[2] == 1):
                store_script_param_1_uses += 1
            elif opcode == h_operations.store_script_param_2 or \
                    (opcode == h_operations.store_script_param and statement[2] == 2):
                store_script_param_2_uses += 1
            elif current_depth == 0 and not is_can_fail_statement \
                    and (opcode in h_operations.can_fail_operations or (
                                    opcode == h_operations.call_script and
                                statement[1].startswith("cf_", 7))) \
                    and not statement_name.startswith("cf_"):
                logging.warning('Script "%s" can fail at operation %d. Use cf_ at '
                                'the beginning of its name' % (statement_name, index))

            result += self._process_statement(opcode, statement)

        if current_depth != 0:
            if current_depth > 0:
                logging.critical('Statement "%s" misses %d "try_end" statement_blocks' %
                                 (statement_name, current_depth))
            else:
                logging.critical('Statement "%s" has %d "try_end" too many' %
                                 (statement_name, -current_depth))

        if store_script_param_1_uses > 1:
            logging.error('store_script_param_1 used more than once in "%s"' % statement_name)
        if store_script_param_2_uses > 1:
            logging.error('store_script_param_2 used more than once in "%s"' % statement_name)

        for local_variable in self._local_variables:
            if self._local_variables[local_variable] <= 0 and not \
                    local_variable.startswith("unused"):
                logging.warning('Local variable "%s" unused at statement "%s"' %
                                (local_variable, statement_name))

        if len(self._local_variables) > 128:
            logging.warning('Script "%s" uses %d>128 local wariables' %
                            (statement_name, len(self._local_variables)))

        self._current_statement_name = 'unknown'
        return result

    def process_simple_triggers(self, statement_name, triggers):
        result = "%d\n" % len(triggers)
        for trigger in triggers:
            trigger_name = statement_name + "(%.1f)" % trigger[0]

            result += "%f " % trigger[0]
            result += self.process_statement_block(trigger_name, 1, trigger[1])
            result += "\n"
        result += "\n"
        return result

    def save_logs(self):
        result = ''
        # sort by least used
        for variable in sorted(self._global_variables.keys(),
                               key=lambda x: self._global_variables[x]):
            result += '%s %d\n' % (variable, self._global_variables[variable])

        with open(self._log_dir + '/' + 'g_variables_usage.txt', 'wb') as f:
            f.write(result.replace('\n', '\r\n').encode('utf-8'))

        # print unused entities
        unused_entities = self._all_entities - set(self._all_used_entities.keys())

        result = ''
        for variable in sorted(unused_entities):
            result += '%s\n' % variable

        with open(self._log_dir + '/' + 'unused_entities.txt', 'wb') as f:
            f.write(result.replace('\n', '\r\n').encode('utf-8'))

        result = ''
        for slot in objects.Slot.objects.values():
            result += '%s %d\n' % (slot.no_tag_id, slot.index)

        with open(self._log_dir + '/' + 'slots.txt', 'wb') as f:
            f.write(result.replace('\n', '\r\n').encode('utf-8'))

    def compile(self, types=()):
        if not types:
            types = objects.ALL_TYPES

        for object_type in types:
            if object_type == objects.Slot:
                # slots are not exported
                continue

            logging.info('Compiling "%s"' % object_type.__name__)

            if objects.HEADERS[object_type]:
                result = objects.HEADERS[object_type] + '\n'
            else:
                result = ''

            # "sound" needs samples exported
            if object_type == objects.Sound:
                result += object_type.export_samples()

            # "Party" needs 2 len's.
            if object_type == objects.Party:
                result += "%d " % len(object_type.objects)
            result += "%d\n" % len(object_type.objects)

            for id in object_type.objects:
                logging.debug('Compiling "%s.%s"' % (object_type.__name__, id))
                # add to _all_entities keeps a track of all cases.
                if object_type in objects.TAG_TO_OBJECT_TYPE.values():
                    self._all_entities.add("%s_%s" % (object_type.tag, id))

                try:
                    result += object_type.objects[id].export(self)
                except Exception as e:
                    import sys
                    raise e

            with open(self._export_dir + '/' + objects.FILE_NAMES[object_type], 'wb') as f:
                f.write(result.replace('\n', '\r\n').encode('utf-8'))

        # save quick strings
        result = "%d\n" % len(self._quick_strings)
        for q_string in self._quick_strings:
            result += "%s %s\n" % \
                      (q_string,
                       p_common.replace_spaces(self._quick_strings[q_string]))

        with open(self._export_dir + '/quick_strings.txt', 'wb') as f:
            f.write(result.replace('\n', '\r\n').encode('utf-8'))

        # export dialog states
        result = ''
        for dialog_state in objects.Dialog.dialog_states:
            result += "%s\n" % dialog_state

        with open(self._export_dir + '/' + 'dialog_states.txt', 'wb') as f:
            f.write(result.replace('\n', '\r\n').encode('utf-8'))

        self.save_logs()
