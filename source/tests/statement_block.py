from source.header_operations import *

from compiler import Compiler
from source.statement import StatementBlock

compiler = Compiler('./output', log_dir='./logs')


result1 = compiler.process_statement_block(0, 1, [
    (assign, ":net_change", 0),
    (try_begin),
        (eq, ":net_change", 0),
        (assign, ":net_change", 1),
    (end_try),
])

result2 = compiler.process_statement_block(0, 1, [
    (assign, ":net_change", 0),
    StatementBlock(
        (try_begin),
            (eq, ":net_change", 0),
            (assign, ":net_change", 1),
        (end_try),
    )
])

assert(result2 == result1)
