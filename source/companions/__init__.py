from source.header_common import s6
from source.statement import StatementBlock
from ..header_operations import *
from ..module_constants import *

import quit
import separate
import questions
import sisterly_advice
import local_histories
import personality_clashes
import rejoin
import object_king_support
import objectionable_action


dialogs = quit.dialogs \
          + separate.dialogs \
          + questions.dialogs \
          + sisterly_advice.dialogs \
          + local_histories.dialogs \
          + personality_clashes.dialogs \
          + rejoin.dialogs \
          + object_king_support.dialogs \
          + objectionable_action.dialogs \


triggers = [
    # Move unemployed NPCs around taverns
    (24 * 15, 0, 0, [
        (call_script, "script_update_companion_candidates_in_taverns"),
    ], []),

    (0, 0, 24, [], [

        (try_for_range, ":npc", companions_begin, companions_end),

            # Reset meeting variables
            # todo: what does this do exactly?
            (troop_set_slot, ":npc", "slot_troop_turned_down_twice", 0),
            (try_begin),
                (troop_slot_eq, ":npc", "slot_troop_met", 1),
                (troop_set_slot, ":npc", "slot_troop_met_previously", 1),
            (try_end),

            # Check for coming out of retirement
            # todo: why isn't this done after hiring?
            (try_begin),
                (troop_get_slot, ":occupation", ":npc", "slot_troop_occupation"),
                (eq, ":occupation", slto_retirement),
                (troop_get_slot, ":renown_min", ":npc", "slot_troop_return_renown"),

                (troop_get_slot, ":player_renown", "trp_player", "slot_troop_renown"),

                (gt, ":player_renown", ":renown_min"),
                (troop_set_slot, ":npc", "slot_troop_personalityclash_penalties", 0),
                (troop_set_slot, ":npc", "slot_troop_morality_penalties", 0),
                (troop_set_slot, ":npc", "slot_troop_occupation", 0),
            (try_end),

            object_king_support.trigger_event_block,

            quit.trigger_event_block,

            (try_begin),
                (main_party_has_troop, ":npc"),
            (else_try),
                (troop_slot_eq, ":npc", "slot_troop_occupation", slto_player_companion),

                # update days on mission slot
                # todo: move this to another trigger
                (try_begin),
                    (troop_get_slot, ":days_on_mission", ":npc", "slot_troop_days_on_mission"),
                    (gt, ":days_on_mission", 0),
                    (val_sub, ":days_on_mission", 1),
                    (troop_set_slot, ":npc", "slot_troop_days_on_mission", ":days_on_mission"),
                (else_try),
                    # todo: this is related to spy missions; move it to another trigger.
                    # return npc after spy mission
                    (troop_slot_eq, ":npc", "slot_troop_current_mission", dplmc_npc_mission_spy_request),
                    (troop_slot_ge, ":npc", "slot_troop_mission_diplomacy", 1),

                    # trp_merc_infantryt5 is the troop for failed spy missions
                    (troop_set_slot, "trp_merc_infantryt5", "slot_troop_mission_object", ":npc"),
                    (assign, "$npc_to_rejoin_party", "trp_merc_infantryt5"),
                (else_try),
                    # todo: rewrite this trigger block to put it outside the else.
                    rejoin.trigger_event_block,
                (try_end),
            (try_end),
        (try_end),
    ]),
]

simple_triggers = [
    (1, [
        (try_begin),
            rejoin.trigger_dialog_block,
        (else_try),
            quit.trigger_dialog_block,
        (else_try),
            personality_clashes.trigger_dialog_block,
        (else_try),
            object_king_support.trigger_dialog_block,
        (else_try),
            sisterly_advice.trigger_dialog_block,
        (else_try),
            local_histories.trigger_dialog_block,
        (try_end),
    ]),
] + personality_clashes.simple_triggers

scripts = [
    ('initialize_companions', [
        # todo: convert these lists of commands into a single Python function
        # that accepts the values

        # Osmund
        (troop_set_slot, "trp_npc1", "slot_troop_morality_type", tmt_egalitarian),  #borcha
        (troop_set_slot, "trp_npc1", "slot_troop_morality_value", 4),  #osmund
        (troop_set_slot, "trp_npc1", "slot_troop_2ary_morality_type", tmt_aristocratic),  #borcha
        (troop_set_slot, "trp_npc1", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc1", "slot_troop_personalityclash_object", "trp_npcpictlady"),  #borcha - deshavi
        (troop_set_slot, "trp_npc1", "slot_troop_personalityclash2_object", "trp_npc16cleric"),  #borcha - klethi
        (troop_set_slot, "trp_npc1", "slot_troop_personalitymatch_object", "trp_npc_tradecompanion"),  #borcha - marnid
        (troop_set_slot, "trp_npc1", "slot_troop_home", "p_town_2"), #Dashbiga
        (troop_set_slot, "trp_npc1", "slot_troop_payment_request", 300),
        (troop_set_slot, "trp_npc1", "slot_troop_kingsupport_argument", argument_ruler),
        (troop_set_slot, "trp_npc1", "slot_troop_kingsupport_opponent", "trp_npc14"), #lezalit
        (troop_set_slot, "trp_npc1", "slot_troop_town_with_contacts", "p_town_2"), #ichamur
        (troop_set_slot, "trp_npc1", "slot_troop_original_faction", 0), #ichamur
        (troop_set_slot, "trp_npc1", "slot_lord_reputation_type", lrep_roguish), #

        #aleifr
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_morality_type", tmt_humanitarian), #marnid
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_morality_value", 2),
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_2ary_morality_type", tmt_honest),
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_2ary_morality_value", 1),
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_personalityclash_object", "trp_npc5"), #marnid - beheshtur
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_personalityclash2_object", "trp_npc9"), #marnid - alayen
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_personalitymatch_object", "trp_npc1"),  #marnid - borcha
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_home", "p_town_1"), #Sargoth
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_payment_request", 0),
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_kingsupport_argument", argument_victory),
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_kingsupport_opponent", "trp_npc16cleric"), #klethi
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_town_with_contacts", "p_town_1"), #Sargoth
        (troop_set_slot, "trp_npc_tradecompanion", "slot_troop_original_faction", 0), #ichamur
        (troop_set_slot, "trp_npc_tradecompanion", "slot_lord_reputation_type", lrep_custodian), #lrep_custodian

        #eithne
        (troop_set_slot, "trp_npclady1", "slot_troop_morality_type", tmt_humanitarian), #Ymira
        (troop_set_slot, "trp_npclady1", "slot_troop_morality_value", 4),
        (troop_set_slot, "trp_npclady1", "slot_troop_2ary_morality_type", tmt_aristocratic),
        (troop_set_slot, "trp_npclady1", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npclady1", "slot_troop_personalityclash_object", "trp_npc14"), #Ymira - artimenner
        (troop_set_slot, "trp_npclady1", "slot_troop_personalityclash2_object", "trp_npc8"), #Ymira - matheld
        (troop_set_slot, "trp_npclady1", "slot_troop_personalitymatch_object", "trp_npc9"), #Ymira - alayen
        (troop_set_slot, "trp_npclady1", "slot_troop_home", "p_town_32"), #Veluca
        (troop_set_slot, "trp_npclady1", "slot_troop_payment_request", 0),
        (troop_set_slot, "trp_npclady1", "slot_troop_kingsupport_argument", argument_lords),
        (troop_set_slot, "trp_npclady1", "slot_troop_kingsupport_opponent", "trp_npc5"), #klethi
        (troop_set_slot, "trp_npclady1", "slot_troop_town_with_contacts", "p_town_32"), #yalen
        (troop_set_slot, "trp_npclady1", "slot_troop_original_faction", 0), #ichamur
        (troop_set_slot, "trp_npclady1", "slot_lord_reputation_type", lrep_benefactor), #lrep_benefactor

        #athrwys
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_morality_type", tmt_aristocratic), #Rolf
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_morality_value", 4),
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_2ary_morality_type", tmt_honest),
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_personalityclash_object", "trp_npc10"), #Rolf - bunduk
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_personalityclash2_object", "trp_npcpictlady"), #Rolf - deshavi
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_personalitymatch_object", "trp_npc5"), #Rolf - beheshtur
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_home", "p_castle_49"), #Ehlerdah
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_payment_request", 300),
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_kingsupport_argument", argument_claim),
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_kingsupport_opponent", "trp_npc6"), #firentis
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_town_with_contacts", "p_town_22"), #veluca
        (troop_set_slot, "trp_npc_noblebriton", "slot_troop_original_faction", 0), #ichamur
        (troop_set_slot, "trp_npc_noblebriton", "slot_lord_reputation_type", lrep_cunning), #lrep_cunning)

        #frioc
        (troop_set_slot, "trp_npc5", "slot_troop_morality_type", tmt_egalitarian),  #beheshtur
        (troop_set_slot, "trp_npc5", "slot_troop_morality_value", 3),  #beheshtur
        (troop_set_slot, "trp_npc5", "slot_troop_2ary_morality_type", -1),
        (troop_set_slot, "trp_npc5", "slot_troop_2ary_morality_value", 0),
        (troop_set_slot, "trp_npc5", "slot_troop_personalityclash_object", "trp_npc_tradecompanion"),  #beheshtur - marnid
        (troop_set_slot, "trp_npc5", "slot_troop_personalityclash2_object", "trp_npclady2"),  #beheshtur- katrin
        (troop_set_slot, "trp_npc5", "slot_troop_personalitymatch_object", "trp_npc_noblebriton"),  #beheshtur - rolf
        (troop_set_slot, "trp_npc5", "slot_troop_home", "p_village_64"), #Halmar
        (troop_set_slot, "trp_npc5", "slot_troop_payment_request", 400),
        (troop_set_slot, "trp_npc5", "slot_troop_kingsupport_argument", argument_ruler),
        (troop_set_slot, "trp_npc5", "slot_troop_kingsupport_opponent", "trp_npc9"), #firentis
        (troop_set_slot, "trp_npc5", "slot_troop_town_with_contacts", "p_town_17"), #tulga
        (troop_set_slot, "trp_npc5", "slot_troop_original_faction", "fac_kingdom_8"), #khergit
        (troop_set_slot, "trp_npc5", "slot_lord_reputation_type", lrep_cunning), #

        #bodero
        (troop_set_slot, "trp_npc6", "slot_troop_morality_type", tmt_humanitarian), #firenz
        (troop_set_slot, "trp_npc6", "slot_troop_morality_value", 2),  #beheshtur
        (troop_set_slot, "trp_npc6", "slot_troop_2ary_morality_type", tmt_honest),
        (troop_set_slot, "trp_npc6", "slot_troop_2ary_morality_value", 1),
        (troop_set_slot, "trp_npc6", "slot_troop_personalityclash_object", "trp_npclady2"), #firenz
        (troop_set_slot, "trp_npc6", "slot_troop_personalityclash2_object", "trp_npc13"), #firenz - nizar
        (troop_set_slot, "trp_npc6", "slot_troop_personalitymatch_object", "trp_npc12"),  #firenz - jeremus
        (troop_set_slot, "trp_npc6", "slot_troop_home", "p_town_10"), #Suno
        (troop_set_slot, "trp_npc6", "slot_troop_payment_request", 0),
        (troop_set_slot, "trp_npc6", "slot_troop_kingsupport_argument", argument_victory),
        (troop_set_slot, "trp_npc6", "slot_troop_kingsupport_opponent", "trp_npc8"), #firentis
        (troop_set_slot, "trp_npc6", "slot_troop_town_with_contacts", "p_town_27"), #uxkhal
        (troop_set_slot, "trp_npc6", "slot_troop_original_faction", "fac_kingdom_13"), #swadia
        (troop_set_slot, "trp_npc6", "slot_lord_reputation_type", lrep_upstanding), #

        
        #bridei
        (troop_set_slot, "trp_npcpictlady", "slot_troop_morality_type", tmt_egalitarian),  #deshavi
        (troop_set_slot, "trp_npcpictlady", "slot_troop_morality_value", 3),  #beheshtur
        (troop_set_slot, "trp_npcpictlady", "slot_troop_2ary_morality_type", -1),
        (troop_set_slot, "trp_npcpictlady", "slot_troop_2ary_morality_value", 0),
        (troop_set_slot, "trp_npcpictlady", "slot_troop_personalityclash_object", "trp_npc1"),  #deshavi
        (troop_set_slot, "trp_npcpictlady", "slot_troop_personalityclash2_object", "trp_npc_noblebriton"),  #deshavi - rolf
        (troop_set_slot, "trp_npcpictlady", "slot_troop_personalitymatch_object", "trp_npc16cleric"),  #deshavi - klethi
        (troop_set_slot, "trp_npcpictlady", "slot_troop_home", "p_town_39"), #Kulum
        (troop_set_slot, "trp_npcpictlady", "slot_troop_payment_request", 300),
        (troop_set_slot, "trp_npcpictlady", "slot_troop_kingsupport_argument", argument_victory),
        (troop_set_slot, "trp_npcpictlady", "slot_troop_kingsupport_opponent", "trp_npclady1"), #ymira
        (troop_set_slot, "trp_npcpictlady", "slot_troop_town_with_contacts", "p_town_37"), #tihr
        (troop_set_slot, "trp_npcpictlady", "slot_troop_original_faction", 0), #swadia
        (troop_set_slot, "trp_npcpictlady", "slot_lord_reputation_type", lrep_custodian), #

        #siwi
        (troop_set_slot, "trp_npc8", "slot_troop_morality_type", tmt_aristocratic), #matheld
        (troop_set_slot, "trp_npc8", "slot_troop_morality_value", 3),  #beheshtur
        (troop_set_slot, "trp_npc8", "slot_troop_2ary_morality_type", -1),
        (troop_set_slot, "trp_npc8", "slot_troop_2ary_morality_value", 0),
        (troop_set_slot, "trp_npc8", "slot_troop_personalityclash_object", "trp_npc12"), #matheld
        (troop_set_slot, "trp_npc8", "slot_troop_personalityclash2_object", "trp_npclady1"), #matheld - ymira
        (troop_set_slot, "trp_npc8", "slot_troop_personalitymatch_object", "trp_npc13"),  #matheld - nizar
        (troop_set_slot, "trp_npc8", "slot_troop_home", "p_town_18"), #Gundig's Point
        (troop_set_slot, "trp_npc8", "slot_troop_payment_request", 500),
        (troop_set_slot, "trp_npc8", "slot_troop_kingsupport_argument", argument_lords),
        (troop_set_slot, "trp_npc8", "slot_troop_kingsupport_opponent", "trp_npc_tradecompanion"), #marnid
        (troop_set_slot, "trp_npc8", "slot_troop_town_with_contacts", "p_town_16"), #wercheg
        (troop_set_slot, "trp_npc8", "slot_troop_original_faction", "fac_kingdom_5"), #nords
        (troop_set_slot, "trp_npc8", "slot_lord_reputation_type", lrep_martial), #

        #lothar
        (troop_set_slot, "trp_npc9", "slot_troop_morality_type", tmt_aristocratic), #alayen
        (troop_set_slot, "trp_npc9", "slot_troop_morality_value", 2),  #beheshtur
        (troop_set_slot, "trp_npc9", "slot_troop_2ary_morality_type", tmt_honest),
        (troop_set_slot, "trp_npc9", "slot_troop_2ary_morality_value", 1),
        (troop_set_slot, "trp_npc9", "slot_troop_personalityclash_object", "trp_npc13"), #alayen vs nizar
        (troop_set_slot, "trp_npc9", "slot_troop_personalityclash2_object", "trp_npc_tradecompanion"), #alayen vs marnid
        (troop_set_slot, "trp_npc9", "slot_troop_personalitymatch_object", "trp_npclady1"),  #alayen - ymira
        (troop_set_slot, "trp_npc9", "slot_troop_home", "p_town_14"), #Rivacheg
        (troop_set_slot, "trp_npc9", "slot_troop_payment_request", 300),
        (troop_set_slot, "trp_npc9", "slot_troop_kingsupport_argument", argument_lords),
        (troop_set_slot, "trp_npc9", "slot_troop_kingsupport_opponent", "trp_npc1"), #borcha
        (troop_set_slot, "trp_npc9", "slot_troop_town_with_contacts", "p_town_14"), #reyvadin
        (troop_set_slot, "trp_npc9", "slot_troop_original_faction", "fac_kingdom_4"), #vaegirs
        (troop_set_slot, "trp_npc9", "slot_lord_reputation_type", lrep_martial), #

        #ceawlin
        (troop_set_slot, "trp_npc10", "slot_troop_morality_type", tmt_humanitarian), #bunduk
        (troop_set_slot, "trp_npc10", "slot_troop_morality_value", 2),
        (troop_set_slot, "trp_npc10", "slot_troop_2ary_morality_type", tmt_egalitarian),
        (troop_set_slot, "trp_npc10", "slot_troop_2ary_morality_value", 1),
        (troop_set_slot, "trp_npc10", "slot_troop_personalityclash_object", "trp_npc_noblebriton"), #bunduk vs rolf
        (troop_set_slot, "trp_npc10", "slot_troop_personalityclash2_object", "trp_npc14"), #bunduk vs lazalet
        (troop_set_slot, "trp_npc10", "slot_troop_personalitymatch_object", "trp_npclady2"),  #bunduk likes katrin
        (troop_set_slot, "trp_npc10", "slot_troop_home", "p_town_12"), #Grunwalder Castle
        (troop_set_slot, "trp_npc10", "slot_troop_payment_request", 200),
        (troop_set_slot, "trp_npc10", "slot_troop_kingsupport_argument", argument_ruler),
        (troop_set_slot, "trp_npc10", "slot_troop_kingsupport_opponent", "trp_npcpictlady"), #nizar
        (troop_set_slot, "trp_npc10", "slot_troop_town_with_contacts", "p_town_12"), #jelkala
        (troop_set_slot, "trp_npc10", "slot_troop_original_faction", "fac_kingdom_3"), #rhodoks
        (troop_set_slot, "trp_npc10", "slot_lord_reputation_type", lrep_benefactor), #

        
        #gwenallian
        (troop_set_slot, "trp_npclady2", "slot_troop_morality_type", tmt_egalitarian),  #katrin
        (troop_set_slot, "trp_npclady2", "slot_troop_morality_value", 3),
        (troop_set_slot, "trp_npclady2", "slot_troop_2ary_morality_type", -1),
        (troop_set_slot, "trp_npclady2", "slot_troop_2ary_morality_value", 0),
        (troop_set_slot, "trp_npclady2", "slot_troop_personalityclash_object", "trp_npc6"),  #katrin vs firenz
        (troop_set_slot, "trp_npclady2", "slot_troop_personalityclash2_object", "trp_npc5"),  #katrin - beheshtur
        (troop_set_slot, "trp_npclady2", "slot_troop_personalitymatch_object", "trp_npc10"),  #katrin likes bunduk
        (troop_set_slot, "trp_npclady2", "slot_troop_home", "p_town_13"), #Praven
        (troop_set_slot, "trp_npclady2", "slot_troop_payment_request", 100),
        (troop_set_slot, "trp_npclady2", "slot_troop_kingsupport_argument", argument_claim),
        (troop_set_slot, "trp_npclady2", "slot_troop_kingsupport_opponent", "trp_npcengineer"), #borcha
        (troop_set_slot, "trp_npclady2", "slot_troop_town_with_contacts", "p_town_13"), #praven
        (troop_set_slot, "trp_npclady2", "slot_troop_original_faction", 0), #
        (troop_set_slot, "trp_npclady2", "slot_lord_reputation_type", lrep_custodian), #
        
        #orosio
        (troop_set_slot, "trp_npc12", "slot_troop_morality_type", tmt_humanitarian), #jeremus
        (troop_set_slot, "trp_npc12", "slot_troop_morality_value", 3),
        (troop_set_slot, "trp_npc12", "slot_troop_2ary_morality_type", -1),
        (troop_set_slot, "trp_npc12", "slot_troop_2ary_morality_value", 0),
        (troop_set_slot, "trp_npc12", "slot_troop_personalityclash_object", "trp_npc8"), #jerem
        (troop_set_slot, "trp_npc12", "slot_troop_personalityclash2_object", "trp_npcengineer"), #jeremus - artimenner
        (troop_set_slot, "trp_npc12", "slot_troop_personalitymatch_object", "trp_npc6"),  #jeremus - firenz
        (troop_set_slot, "trp_npc12", "slot_troop_home", "p_town_7"), #undetermined #University
        (troop_set_slot, "trp_npc12", "slot_troop_payment_request", 0),
        (troop_set_slot, "trp_npc12", "slot_troop_kingsupport_argument", argument_claim),
        (troop_set_slot, "trp_npc12", "slot_troop_kingsupport_opponent", "trp_npc13"), #nizar
        (troop_set_slot, "trp_npc12", "slot_troop_town_with_contacts", "p_town_7"), #halmar
        (troop_set_slot, "trp_npc12", "slot_troop_original_faction", 0), #
        (troop_set_slot, "trp_npc12", "slot_lord_reputation_type", lrep_benefactor), #

        
        #liuva
        (troop_set_slot, "trp_npc13", "slot_troop_morality_type", tmt_aristocratic), #nizar
        (troop_set_slot, "trp_npc13", "slot_troop_morality_value", 3),
        (troop_set_slot, "trp_npc13", "slot_troop_2ary_morality_type", -1),
        (troop_set_slot, "trp_npc13", "slot_troop_2ary_morality_value", 0),
        (troop_set_slot, "trp_npc13", "slot_troop_personalityclash_object", "trp_npc9"), #nizar
        (troop_set_slot, "trp_npc13", "slot_troop_personalityclash2_object", "trp_npc6"), #nizar - firenz
        (troop_set_slot, "trp_npc13", "slot_troop_personalitymatch_object", "trp_npc8"), #nizar - matheld
        (troop_set_slot, "trp_npc13", "slot_troop_home", "p_town_33"), #Ergellon Castle
        (troop_set_slot, "trp_npc13", "slot_troop_payment_request", 300),
        (troop_set_slot, "trp_npc13", "slot_troop_kingsupport_argument", argument_claim),
        (troop_set_slot, "trp_npc13", "slot_troop_kingsupport_opponent", "trp_npc10"), #nizar
        (troop_set_slot, "trp_npc13", "slot_troop_town_with_contacts", "p_town_33"), #suno
        (troop_set_slot, "trp_npc13", "slot_troop_original_faction", 0), #
        (troop_set_slot, "trp_npc13", "slot_lord_reputation_type", lrep_roguish), #

        
        #brian
        (troop_set_slot, "trp_npc14", "slot_troop_morality_type", tmt_aristocratic), #lezalit
        (troop_set_slot, "trp_npc14", "slot_troop_morality_value", 4),
        (troop_set_slot, "trp_npc14", "slot_troop_2ary_morality_type", tmt_egalitarian),
        (troop_set_slot, "trp_npc14", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc14", "slot_troop_personalityclash_object", "trp_npclady1"), #lezalit
        (troop_set_slot, "trp_npc14", "slot_troop_personalityclash2_object", "trp_npc10"), #lezalit - bunduk
        (troop_set_slot, "trp_npc14", "slot_troop_personalitymatch_object", "trp_npc_paintrain"), #lezalit - artimenner
        (troop_set_slot, "trp_npc14", "slot_troop_home", "p_town_35"), #Ismirala Castle
        (troop_set_slot, "trp_npc14", "slot_troop_payment_request", 400),
        (troop_set_slot, "trp_npc14", "slot_troop_kingsupport_argument", argument_victory),
        (troop_set_slot, "trp_npc14", "slot_troop_kingsupport_opponent", "trp_npclady2"), #nizar
        (troop_set_slot, "trp_npc14", "slot_troop_town_with_contacts", "p_town_35"), #dhirim
        (troop_set_slot, "trp_npc14", "slot_troop_original_faction", 0), #
        (troop_set_slot, "trp_npc14", "slot_lord_reputation_type", lrep_selfrighteous), #

        #agasicles 
        (troop_set_slot, "trp_npcengineer", "slot_troop_morality_type", tmt_egalitarian),  #artimenner
        (troop_set_slot, "trp_npcengineer", "slot_troop_morality_value", 2),
        (troop_set_slot, "trp_npcengineer", "slot_troop_2ary_morality_type", tmt_honest),
        (troop_set_slot, "trp_npcengineer", "slot_troop_2ary_morality_value", 1),
        (troop_set_slot, "trp_npcengineer", "slot_troop_personalityclash_object", "trp_npc16cleric"), #artimenner - klethi
        (troop_set_slot, "trp_npcengineer", "slot_troop_personalityclash2_object", "trp_npc12"), #artimenner - jeremus
        (troop_set_slot, "trp_npcengineer", "slot_troop_personalitymatch_object", "trp_npc_grim"), ##lazalit - artimenner
        (troop_set_slot, "trp_npcengineer", "slot_troop_home", "p_town_4"), #Culmarr Castle
        (troop_set_slot, "trp_npcengineer", "slot_troop_payment_request", 300),
        (troop_set_slot, "trp_npcengineer", "slot_troop_kingsupport_argument", argument_ruler),
        (troop_set_slot, "trp_npcengineer", "slot_troop_kingsupport_opponent", "trp_npc_noblebriton"), #nizar
        (troop_set_slot, "trp_npcengineer", "slot_troop_town_with_contacts", "p_town_4"), #narra
        (troop_set_slot, "trp_npcengineer", "slot_lord_reputation_type", lrep_custodian), #

        #aedh
        (troop_set_slot, "trp_npc16cleric", "slot_troop_morality_type", tmt_aristocratic), #klethi
        (troop_set_slot, "trp_npc16cleric", "slot_troop_morality_value", 4),
        (troop_set_slot, "trp_npc16cleric", "slot_troop_2ary_morality_type", tmt_humanitarian),
        (troop_set_slot, "trp_npc16cleric", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc16cleric", "slot_troop_personalityclash_object", "trp_npcengineer"), #klethi
        (troop_set_slot, "trp_npc16cleric", "slot_troop_personalityclash2_object", "trp_npc1"), #klethi - borcha
        (troop_set_slot, "trp_npc16cleric", "slot_troop_personalitymatch_object", "trp_npcpictlady"),  #deshavi - klethi
        (troop_set_slot, "trp_npc16cleric", "slot_troop_home", "p_town_30"), #Uslum
        (troop_set_slot, "trp_npc16cleric", "slot_troop_payment_request", 200),
        (troop_set_slot, "trp_npc16cleric", "slot_troop_kingsupport_argument", argument_lords),
        (troop_set_slot, "trp_npc16cleric", "slot_troop_kingsupport_opponent", "trp_npc12"), #nizar
        (troop_set_slot, "trp_npc16cleric", "slot_troop_town_with_contacts", "p_town_30"), #khudan
        (troop_set_slot, "trp_npc16cleric", "slot_lord_reputation_type", lrep_roguish), #

        #ciniod
        (troop_set_slot, "trp_npc_pict1", "slot_troop_morality_type", tmt_aristocratic), #Ciniod
        (troop_set_slot, "trp_npc_pict1", "slot_troop_morality_value", 2),
        (troop_set_slot, "trp_npc_pict1", "slot_troop_2ary_morality_type", tmt_humanitarian),
        (troop_set_slot, "trp_npc_pict1", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc_pict1", "slot_troop_personalityclash_object", "trp_npclady2"), #klethi
        (troop_set_slot, "trp_npc_pict1", "slot_troop_personalityclash2_object", "trp_npcengineer"), #klethi - borcha
        (troop_set_slot, "trp_npc_pict1", "slot_troop_personalitymatch_object", "trp_npc_pict2"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_pict1", "slot_troop_home", "p_town_39"), #Uslum
        (troop_set_slot, "trp_npc_pict1", "slot_troop_payment_request", 400),
        (troop_set_slot, "trp_npc_pict1", "slot_troop_kingsupport_argument", argument_lords),
        (troop_set_slot, "trp_npc_pict1", "slot_troop_kingsupport_opponent", "trp_npc5"), #nizar
        (troop_set_slot, "trp_npc_pict1", "slot_troop_town_with_contacts", "p_town_39"), #khudan
        (troop_set_slot, "trp_npc_pict1", "slot_lord_reputation_type", lrep_martial), #

        #onuist
        (troop_set_slot, "trp_npc_pict2", "slot_troop_morality_type", tmt_aristocratic), #Onuist
        (troop_set_slot, "trp_npc_pict2", "slot_troop_morality_value", 2),
        (troop_set_slot, "trp_npc_pict2", "slot_troop_2ary_morality_type", tmt_humanitarian),
        (troop_set_slot, "trp_npc_pict2", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc_pict2", "slot_troop_personalityclash_object", "trp_npc12"), #klethi
        (troop_set_slot, "trp_npc_pict2", "slot_troop_personalityclash2_object", "trp_npcpictlady"), #klethi - borcha
        (troop_set_slot, "trp_npc_pict2", "slot_troop_personalitymatch_object", "trp_npc_pict1"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_pict2", "slot_troop_home", "p_town_39"), #Uslum
        (troop_set_slot, "trp_npc_pict2", "slot_troop_payment_request", 350),
        (troop_set_slot, "trp_npc_pict2", "slot_troop_kingsupport_argument", argument_lords),
        (troop_set_slot, "trp_npc_pict2", "slot_troop_kingsupport_opponent", "trp_npc_noblebriton"), #nizar
        (troop_set_slot, "trp_npc_pict2", "slot_troop_town_with_contacts", "p_town_37"), #khudan
        (troop_set_slot, "trp_npc_pict2", "slot_lord_reputation_type", lrep_martial), #

        #eadwin
        (troop_set_slot, "trp_npc_paintrain", "slot_troop_morality_type", tmt_honest), #edwin
        (troop_set_slot, "trp_npc_paintrain", "slot_troop_morality_value", 4),
        (troop_set_slot, "trp_npc_paintrain", "slot_troop_2ary_morality_type", tmt_egalitarian),
        (troop_set_slot, "trp_npc_paintrain", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc_paintrain", "slot_troop_personalityclash_object", "trp_npc_hammertime"), #klethi
        (troop_set_slot, "trp_npc_paintrain", "slot_troop_personalityclash2_object", "trp_npc_deadeye"), #klethi - borcha
        (troop_set_slot, "trp_npc_paintrain", "slot_troop_personalitymatch_object", "trp_npclady3"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_paintrain", "slot_troop_home", "p_town_8"), #Uslum
        (troop_set_slot, "trp_npc_paintrain", "slot_troop_payment_request", 200),
        (troop_set_slot, "trp_npc_paintrain", "slot_troop_kingsupport_argument", argument_victory),
        (troop_set_slot, "trp_npc_paintrain", "slot_troop_kingsupport_opponent", "trp_npc_hammertime"), #nizar
        (troop_set_slot, "trp_npc_paintrain", "slot_troop_town_with_contacts", "p_town_8"), #khudan
        (troop_set_slot, "trp_npc_paintrain", "slot_lord_reputation_type", lrep_martial), #

        #Mihael ap cad
        (troop_set_slot, "trp_npc_hammertime", "slot_troop_morality_type", tmt_aristocratic), #mihael
        (troop_set_slot, "trp_npc_hammertime", "slot_troop_morality_value", 4),
        (troop_set_slot, "trp_npc_hammertime", "slot_troop_2ary_morality_type", tmt_egalitarian),
        (troop_set_slot, "trp_npc_hammertime", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc_hammertime", "slot_troop_personalityclash_object", "trp_npc_paintrain"), #klethi
        (troop_set_slot, "trp_npc_hammertime", "slot_troop_personalityclash2_object", "trp_npc_deadeye"), #klethi - borcha
        (troop_set_slot, "trp_npc_hammertime", "slot_troop_personalitymatch_object", "trp_npclady3"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_hammertime", "slot_troop_home", "p_town_23"), #licidfelh
        (troop_set_slot, "trp_npc_hammertime", "slot_troop_payment_request", 150),
        (troop_set_slot, "trp_npc_hammertime", "slot_troop_kingsupport_argument", argument_victory),
        (troop_set_slot, "trp_npc_hammertime", "slot_troop_kingsupport_opponent", "trp_npc_paintrain"), #nizar
        (troop_set_slot, "trp_npc_hammertime", "slot_troop_town_with_contacts", "p_town_15"), #khudan
        (troop_set_slot, "trp_npc_hammertime", "slot_lord_reputation_type", lrep_cunning), #gdw lrep_selfrighteous

        #Inka
        (troop_set_slot, "trp_npclady3", "slot_troop_morality_type", tmt_aristocratic), #Inka
        (troop_set_slot, "trp_npclady3", "slot_troop_morality_value", 4),
        (troop_set_slot, "trp_npclady3", "slot_troop_2ary_morality_type", tmt_humanitarian),
        (troop_set_slot, "trp_npclady3", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npclady3", "slot_troop_personalityclash_object", "trp_npc_pict1"), #klethi
        (troop_set_slot, "trp_npclady3", "slot_troop_personalityclash2_object", "trp_npc_pict1"), #klethi - borcha
        (troop_set_slot, "trp_npclady3", "slot_troop_personalitymatch_object", "trp_npc_deadeye"),  #deshavi - klethi
        (troop_set_slot, "trp_npclady3", "slot_troop_home", "p_town_2"), #Uslum
        (troop_set_slot, "trp_npclady3", "slot_troop_payment_request", 150),
        (troop_set_slot, "trp_npclady3", "slot_troop_kingsupport_argument", argument_victory),
        (troop_set_slot, "trp_npclady3", "slot_troop_kingsupport_opponent", "trp_npc_pict1"), #nizar
        (troop_set_slot, "trp_npclady3", "slot_troop_town_with_contacts", "p_town_2"), #khudan
        (troop_set_slot, "trp_npclady3", "slot_lord_reputation_type", lrep_goodnatured), #gdw selfrighteous

        #Ultan
        (troop_set_slot, "trp_npc_surgeon", "slot_troop_morality_type", tmt_humanitarian),
        (troop_set_slot, "trp_npc_surgeon", "slot_troop_morality_value", 4),
        (troop_set_slot, "trp_npc_surgeon", "slot_troop_2ary_morality_type", tmt_honest),
        (troop_set_slot, "trp_npc_surgeon", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc_surgeon", "slot_troop_personalityclash_object", "trp_npc_pict1"), #klethi
        (troop_set_slot, "trp_npc_surgeon", "slot_troop_personalityclash2_object", "trp_npc_deadeye"), #klethi - borcha
        (troop_set_slot, "trp_npc_surgeon", "slot_troop_personalitymatch_object", "trp_npclady3"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_surgeon", "slot_troop_home", "p_town_3"), #Uslum
        (troop_set_slot, "trp_npc_surgeon", "slot_troop_payment_request", 150),
        (troop_set_slot, "trp_npc_surgeon", "slot_troop_kingsupport_argument", argument_victory),
        (troop_set_slot, "trp_npc_surgeon", "slot_troop_kingsupport_opponent", "trp_npc_deadeye"), #nizar
        (troop_set_slot, "trp_npc_surgeon", "slot_troop_town_with_contacts", "p_town_3"), #khudan
        (troop_set_slot, "trp_npc_surgeon", "slot_lord_reputation_type", lrep_goodnatured), #gdw cunning

        #eadfrith
        (troop_set_slot, "trp_npc_deadeye", "slot_troop_morality_type", tmt_aristocratic), #Eadfrith Cearling
        (troop_set_slot, "trp_npc_deadeye", "slot_troop_morality_value", 4),
        (troop_set_slot, "trp_npc_deadeye", "slot_troop_2ary_morality_type", tmt_humanitarian),
        (troop_set_slot, "trp_npc_deadeye", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc_deadeye", "slot_troop_personalityclash_object", "trp_npc_surgeon"), #klethi
        (troop_set_slot, "trp_npc_deadeye", "slot_troop_personalityclash2_object", "trp_npc_probulator"), #klethi - borcha
        (troop_set_slot, "trp_npc_deadeye", "slot_troop_personalitymatch_object", "trp_npclady3"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_deadeye", "slot_troop_home", "p_town_4"), #Uslum
        (troop_set_slot, "trp_npc_deadeye", "slot_troop_payment_request", 150),
        (troop_set_slot, "trp_npc_deadeye", "slot_troop_kingsupport_argument", argument_victory),
        (troop_set_slot, "trp_npc_deadeye", "slot_troop_kingsupport_opponent", "trp_npc_surgeon"), #nizar
        (troop_set_slot, "trp_npc_deadeye", "slot_troop_town_with_contacts", "p_town_4"), #khudan
        (troop_set_slot, "trp_npc_deadeye", "slot_lord_reputation_type", lrep_cunning), #

        #matui
        (troop_set_slot, "trp_npc_probulator", "slot_troop_morality_type", tmt_aristocratic), #Domnaill
        (troop_set_slot, "trp_npc_probulator", "slot_troop_morality_value", 4),
        (troop_set_slot, "trp_npc_probulator", "slot_troop_2ary_morality_type", tmt_egalitarian),
        (troop_set_slot, "trp_npc_probulator", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc_probulator", "slot_troop_personalityclash_object", "trp_npc_grim"), #klethi
        (troop_set_slot, "trp_npc_probulator", "slot_troop_personalityclash2_object", "trp_npc_irish1"), #klethi - borcha
        (troop_set_slot, "trp_npc_probulator", "slot_troop_personalitymatch_object", "trp_npc_deadeye"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_probulator", "slot_troop_home", "p_town_31"), #Uslum
        (troop_set_slot, "trp_npc_probulator", "slot_troop_payment_request", 150),
        (troop_set_slot, "trp_npc_probulator", "slot_troop_kingsupport_argument", argument_victory),
        (troop_set_slot, "trp_npc_probulator", "slot_troop_kingsupport_opponent", "trp_npc_grim"), #nizar
        (troop_set_slot, "trp_npc_probulator", "slot_troop_town_with_contacts", "p_town_31"), #khudan
        (troop_set_slot, "trp_npc_probulator", "slot_lord_reputation_type", lrep_cunning), #gdw self-ri

        #clovis
        (troop_set_slot, "trp_npc_grim", "slot_troop_morality_type", tmt_honest), #domnaill
        (troop_set_slot, "trp_npc_grim", "slot_troop_morality_value", 2),
        (troop_set_slot, "trp_npc_grim", "slot_troop_2ary_morality_type", tmt_egalitarian),
        (troop_set_slot, "trp_npc_grim", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc_grim", "slot_troop_personalityclash_object", "trp_npc_probulator"), #klethi
        (troop_set_slot, "trp_npc_grim", "slot_troop_personalityclash2_object", "trp_npc_deadeye"), #klethi - borcha
        (troop_set_slot, "trp_npc_grim", "slot_troop_personalitymatch_object", "trp_npc_irish1"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_grim", "slot_troop_home", "p_town_6"), #Uslum
        (troop_set_slot, "trp_npc_grim", "slot_troop_payment_request", 100),
        (troop_set_slot, "trp_npc_grim", "slot_troop_kingsupport_argument", argument_victory),
        (troop_set_slot, "trp_npc_grim", "slot_troop_kingsupport_opponent", "trp_npc_probulator"), #nizar
        (troop_set_slot, "trp_npc_grim", "slot_troop_town_with_contacts", "p_town_6"), #khudan
        (troop_set_slot, "trp_npc_grim", "slot_lord_reputation_type", lrep_martial), #

        #connor
        (troop_set_slot, "trp_npc_irish1", "slot_troop_morality_type", tmt_aristocratic), #Connor
        (troop_set_slot, "trp_npc_irish1", "slot_troop_morality_value", 2),
        (troop_set_slot, "trp_npc_irish1", "slot_troop_2ary_morality_type", tmt_honest),
        (troop_set_slot, "trp_npc_irish1", "slot_troop_2ary_morality_value", -1),
        (troop_set_slot, "trp_npc_irish1", "slot_troop_personalityclash_object", "trp_npc_grim"), #klethi
        (troop_set_slot, "trp_npc_irish1", "slot_troop_personalityclash2_object", "trp_npc_surgeon"), #klethi - borcha
        (troop_set_slot, "trp_npc_irish1", "slot_troop_personalitymatch_object", "trp_npc_probulator"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_irish1", "slot_troop_home", "p_castle_6"), #Rath Cormac
        (troop_set_slot, "trp_npc_irish1", "slot_troop_payment_request", 100),
        (troop_set_slot, "trp_npc_irish1", "slot_troop_kingsupport_argument", argument_victory),
        (troop_set_slot, "trp_npc_irish1", "slot_troop_kingsupport_opponent", "trp_npc_surgeon"), #nizar
        (troop_set_slot, "trp_npc_irish1", "slot_troop_town_with_contacts", "p_town_33"), #Aileach
        (troop_set_slot, "trp_npc_irish1", "slot_lord_reputation_type", lrep_cunning), #

        (troop_set_slot, "trp_npc17", "slot_troop_morality_type", tmt_honest),
        (troop_set_slot, "trp_npc17", "slot_troop_morality_value", 1),
        (troop_set_slot, "trp_npc17", "slot_troop_2ary_morality_type", -1),
        (troop_set_slot, "trp_npc17", "slot_troop_2ary_morality_value", 0),
        (troop_set_slot, "trp_npc17", "slot_troop_personalityclash_object", "trp_npc12"),
        (troop_set_slot, "trp_npc17", "slot_troop_personalityclash2_object", "trp_npc18"),
        (troop_set_slot, "trp_npc17", "slot_troop_personalitymatch_object", "trp_npc_deadeye"),
        (troop_set_slot, "trp_npc17", "slot_troop_home", 0),
        (troop_set_slot, "trp_npc17", "slot_troop_payment_request", 1450),
        (troop_set_slot, "trp_npc17", "slot_troop_kingsupport_argument", argument_claim),
        (troop_set_slot, "trp_npc17", "slot_troop_kingsupport_opponent", "trp_npc_grim"),
        (troop_set_slot, "trp_npc17", "slot_troop_town_with_contacts", "p_town_22"),
        (troop_set_slot, "trp_npc17", "slot_troop_original_faction", 0),
        (troop_set_slot, "trp_npc17", "slot_lord_reputation_type", lrep_custodian),

        # Bronn
        (troop_set_slot, "trp_npc18", "slot_troop_morality_type", tmt_humanitarian),
        (troop_set_slot, "trp_npc18", "slot_troop_morality_value", 3),
        (troop_set_slot, "trp_npc18", "slot_troop_2ary_morality_type", -1),
        (troop_set_slot, "trp_npc18", "slot_troop_2ary_morality_value", 0),
        (troop_set_slot, "trp_npc18", "slot_troop_personalityclash_object", "trp_npclady1"),
        (troop_set_slot, "trp_npc18", "slot_troop_personalityclash2_object", "trp_npc17"),
        (troop_set_slot, "trp_npc18", "slot_troop_personalitymatch_object", "trp_npc10"),
        (troop_set_slot, "trp_npc18", "slot_troop_home", 0),
        (troop_set_slot, "trp_npc18", "slot_troop_payment_request", 1450),
        (troop_set_slot, "trp_npc18", "slot_troop_kingsupport_argument", argument_claim),
        (troop_set_slot, "trp_npc18", "slot_troop_kingsupport_opponent", "trp_npc_grim"),
        (troop_set_slot, "trp_npc18", "slot_troop_town_with_contacts", "p_town_6"),
        (troop_set_slot, "trp_npc18", "slot_troop_original_faction", 0),
        (troop_set_slot, "trp_npc18", "slot_lord_reputation_type", lrep_roguish),

        (store_sub, ":number_of_npc_slots", "slot_troop_strings_end", "slot_troop_intro"),

        (try_for_range, ":npc", companions_begin, companions_end),
            (try_for_range, ":slot_addition", 0, ":number_of_npc_slots"),
                (store_add, ":slot", ":slot_addition", "slot_troop_intro"),

                (store_mul, ":string_addition", ":slot_addition", 29), #chief cambiado
                (store_add, ":string", "str_npc1_intro", ":string_addition"), 
                (val_add, ":string", ":npc"),
                (val_sub, ":string", companions_begin),

                (troop_set_slot, ":npc", ":slot", ":string"),
            (try_end),
        (try_end),

        # set personality clashes
        (try_for_range, ":companion", companions_begin, companions_end),
            (try_for_range, ":other_companion", companions_begin, companions_end),
                (neq, ":other_companion", ":companion"),
                (neg|troop_slot_eq, ":companion", "slot_troop_personalityclash_object", ":other_companion"),
                (neg|troop_slot_eq, ":companion", "slot_troop_personalityclash2_object", ":other_companion"),

                # todo: how come that the initial relation is set when they do not clash?
                (call_script, "script_troop_change_relation_with_troop", ":companion", ":other_companion", 7),
            (try_end),
        (try_end),

        (call_script, "script_update_companion_candidates_in_taverns"),
    ]),

    #script_update_companion_candidates_in_taverns
    # INPUT: none
    # OUTPUT: none
    ("update_companion_candidates_in_taverns", [
        (try_begin),
            (eq, "$cheat_mode", 1),
            (display_message, "str_shuffling_companion_locations"),
        (try_end),

        (try_for_range, ":troop_no", companions_begin, companions_end),
            (troop_set_slot, ":troop_no", "slot_troop_cur_center", -1),
            (troop_slot_eq, ":troop_no", "slot_troop_days_on_mission", 0),
            (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_inactive),

            (neg|troop_slot_ge, ":troop_no", "slot_troop_prisoner_of_party", 0),

            (store_random_in_range, ":town_no", towns_begin, towns_end),
            (try_begin),
                (neg|troop_slot_eq, ":troop_no", "slot_troop_home", ":town_no"),
                (neg|troop_slot_eq, ":troop_no", "slot_troop_first_encountered", ":town_no"),
                (troop_set_slot, ":troop_no", "slot_troop_cur_center", ":town_no"),
                (try_begin),
                    (eq, "$cheat_mode", 1),
                    (str_store_troop_name, 4, ":troop_no"),
                    (str_store_party_name, 5, ":town_no"),
                    (display_message, "@{!}{s4} is in {s5}"),
                (try_end),
            (try_end),
        (try_end),
    ]),

    # script_recruit_troop_as_companion
    # Input: arg1 = troop_no,
    # Output: none
    ("recruit_troop_as_companion", [

        (store_script_param_1, ":troop_no"),
        (troop_set_slot, ":troop_no", "slot_troop_occupation", slto_player_companion),
        (troop_set_slot, ":troop_no", "slot_troop_cur_center", -1),
        (troop_set_auto_equip, ":troop_no", 0),

        (party_add_members, "p_main_party", ":troop_no", 1),
        (str_store_troop_name, s6, ":troop_no"),
        (display_message, "@{s6} has joined your party.", color_hero_news),

        (troop_set_note_available, ":troop_no", 1),

        # ACHIEVEMENT_KNIGHTS_OF_THE_ROUND
        (try_begin),
            (is_between, ":troop_no", companions_begin, companions_end),
            (store_sub, ":companion_number", ":troop_no", companions_begin),

            (set_achievement_stat, ACHIEVEMENT_KNIGHTS_OF_THE_ROUND, ":companion_number", 1),

            (assign, ":number_of_companions_hired", 0),
            (try_for_range, ":cur_companion", 0, 18),
                (get_achievement_stat, ":is_hired", ACHIEVEMENT_KNIGHTS_OF_THE_ROUND, ":cur_companion"),
                (eq, ":is_hired", 1),
                (val_add, ":number_of_companions_hired", 1),
            (try_end),

            (try_begin),
                (ge, ":number_of_companions_hired", 10),
                (unlock_achievement, ACHIEVEMENT_KNIGHTS_OF_THE_ROUND),
            (try_end),
        (try_end),
    ]),

    ("retire_companion", [
        (store_script_param_1, ":npc"),
        (store_script_param_2, ":length"),

        (remove_member_from_party, ":npc", "p_main_party"),
        (troop_set_slot, ":npc", "slot_troop_personalityclash_penalties", 0),
        (troop_set_slot, ":npc", "slot_troop_morality_penalties", 0),
        (troop_get_slot, ":renown", "trp_player", "slot_troop_renown"),
        (store_add, ":return_renown", ":renown", ":length"),
        (troop_set_slot, ":npc", "slot_troop_occupation", slto_retirement),
        (troop_set_slot, ":npc", "slot_troop_return_renown", ":return_renown"),
    ]),
] + objectionable_action.scripts + personality_clashes.scripts


def _loop_quest_available_companions(*args):
    return StatementBlock(
        (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
            (troop_is_hero, ":stack_troop"),
            (is_between, ":stack_troop", companions_begin, companions_end),

            (store_character_level, ":stack_level", ":stack_troop"),
            # todo: what this 15 represent? that only +15 lvl heros can be used?
            (ge, ":stack_level", 15),

            # check that hero is not being used in another quest.
            (assign, ":is_quest_hero", 0),
            (try_for_range, ":i_quest", all_quests_begin, all_quests_end),
                (check_quest_active, ":i_quest"),
                (this_or_next|quest_slot_eq, ":i_quest", "slot_quest_target_troop", ":stack_troop"),
                (quest_slot_eq, ":i_quest", "slot_quest_object_troop", ":stack_troop"),
                (assign, ":is_quest_hero", 1),
                # todo: it was found: break the loop.
            (try_end),
            (eq, ":is_quest_hero", 0),

            StatementBlock(*args),
        (try_end),
    )


quest = StatementBlock(
    (eq, ":quest_no", "qst_lend_companion"),
    (try_begin),
        (ge, "$g_talk_troop_faction_relation", 0),
        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),

        # count the number of available companions for the quest
        (assign, ":total_heroes", 0),
        _loop_quest_available_companions((val_add, ":total_heroes", 1),),

        # Skip if party has no eligible heroes
        (gt, ":total_heroes", 0),

        # select a random hero (:target_hero)
        (store_random_in_range, ":random_hero", 0, ":total_heroes"),
        (assign, ":target_hero", -1),
        (assign, ":total_heroes", 0),
        _loop_quest_available_companions(
            (val_add, ":total_heroes", 1),
            (gt, ":total_heroes", ":random_hero"),
            (assign, ":target_hero", ":stack_troop")
            # todo: break the loop or the last hero is always chosen
        ),

        # I'm almost certain that by construction it always finds, but well.
        (try_begin),
            (eq, ':target_hero', -1),
            (display_debug_message, "@qst_lend_companion quest failed to find "
                                    "a hero when it should."),
        (try_end),
        (neq, ':target_hero', -1),

        # build the quest
        (assign, ":quest_target_troop", ":target_hero"),
        (store_current_day, ":quest_target_amount"),
        (val_add, ":quest_target_amount", 8),

        (assign, ":quest_importance", 1),
        (assign, ":quest_xp_reward", 500),
        (assign, ":quest_gold_reward", 400),
        (assign, ":result", ":quest_no"),
        (assign, ":quest_dont_give_again_period", 25),
    (try_end),
)
