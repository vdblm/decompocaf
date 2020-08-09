from lark import Lark

from ast_transform import AST, CreateAST
from grammar import grammar
from symbol_table import SymTable

OP1 = "$s0"
OP2 = "$s1"

TMP = "$s2"

FOP1 = "$f0"
FOP2 = "$f1"
FOP3 = "$f3"

SW = "$t0"
LW = "$t0"
SYS_CODE = "$v0"
SYS_ARG = "$a0"
PRINT_INT = 1
PRINT_DOUBLE = 2
PRINT_STRING = 4
NEW_LINE = "newLINE"


def code_gen(ast: AST, prevLoopEnd=None):
    global child1
    if len(ast.children) > 0:
        child1 = ast.children[0]
    if ast.name == "program":
        return "\n".join([code_gen(child, prevLoopEnd) for child in ast.children])

    if ast.name == "variable_decl":
        pass
    if ast.name == "function_decl":
        if ast.children[1] == "main":
            body = code_gen(ast.children[3], prevLoopEnd)
            return "main:\n" + body
        else:
            # TODO
            pass
    if ast.name == "stmt_block":
        # iterate till variable declaration is finished
        res = filter(lambda x: x.name != "variable_decl", ast.children)
        # print(list(res)[0])
        return "\n".join([code_gen(a, prevLoopEnd) for a in list(res)])

    if ast.name == "lvalue":
        if ast.type == "int":
            body = "lw {}, {}\n".format(LW, ast.children[0])
            body += "move {}, {}\n".format(OP1, LW)
            return body
        else:
            # todo
            pass

    if ast.name == "assign_expr":
        lvalue = ast.children[0]
        exp = ast.children[1]
        body = code_gen(exp)
        if lvalue.type == "int":
            body += "move {}, {}\n".format(SW, OP1)
            body += "sw {}, {}\n".format(SW, lvalue.children[0])
        elif lvalue.type == "double":
            # todo
            pass
        elif lvalue.type == "string":
            # todo
            pass
        elif lvalue.type == "bool":
            # todo
            pass
        else:
            raise Exception("not defined type")

        return body

    if ast.name == "print_stmt":
        body = ""
        for child in ast.children:
            if child.type == "int":
                body += code_gen(child)
                body += "move {}, {}\n".format(SYS_ARG, OP1)
                body += "li {}, {}\n".format(SYS_CODE, PRINT_INT)
                body += "syscall    # print!\n"
            else:
                # todo
                pass
        # add newline
        body += "li {}, {}\n".format(SYS_CODE, PRINT_STRING)
        body += "la {}, {}\n".format(SYS_ARG, NEW_LINE)
        body += "syscall #print new line\n"
        return body

    if ast.name == "constant":
        # todo
        if ast.type == "int":
            return "li {}, {}\n".format(OP1, ast.children[0].children[0])
        else:
            # todo handle double, string, ...
            pass

    if ast.name == "add_expr":
        if child1.type == "int":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "add %s, %s %s\n" % (OP1, OP2, TMP)
            return body
        elif child1.type == "double":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "mov.d %s, %s \n" % (FOP3, FOP2)
            body += "mov.d %s, %s \n" % (FOP2, FOP1)
            body += "add.d %s, %s %s\n" % (FOP1, FOP2, FOP3)
            return body
    if ast.name == "sub_expr":
        if child1.type == "int":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "sub %s, %s %s\n" % (OP1, OP2, TMP)
            return body
        elif child1.type == "double":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "mov.d %s, %s \n" % (FOP3, FOP2)
            body += "mov.d %s, %s \n" % (FOP2, FOP1)
            body += "sub.d %s, %s %s\n" % (FOP1, FOP2, FOP3)
            return body

    if ast.name == "mult_expr":
        if child1.type == "int":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "muhi %s\n" % (OP1)
            return body
        elif child1.type == "double":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "mov.d %s, %s \n" % (FOP3, FOP2)
            body += "mov.d %s, %s \n" % (FOP2, FOP1)
            body += "mul.d %s, %s %s\n" % (FOP1, FOP2, FOP3)
            return body

    if ast.name == "div_expr":
        if child1.type == "int":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP1)
            body += "div %s, %s \n" % (OP1, OP2)
            body += "mflo %s\n" % (OP1)
            return body
        elif child1.type == "double":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "mov.d %s, %s \n" % (FOP3, FOP2)
            body += "mov.d %s, %s \n" % (FOP2, FOP1)
            body += "mul.d %s, %s %s\n" % (FOP1, FOP2, FOP3)
            return body

    if ast.name == "mod_expr":
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP1)
            body += "div %s, %s \n" % (OP1, OP2)
            body += "mfhi %s\n" % (OP1)
            return body
    if ast.name == "lt_expr":
        if child1.type == "int":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "slt %s, %s %s\n" % (OP1, OP2, TMP)
            return body
        if child1.type == "double":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "c.lt.d %s, %s\n" % (FOP1, FOP2)
            return body

    if ast.name == "gt_expr":
        if child1.type == "int":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "slt %s, %s %s\n" % (OP1, TMP, OP2)
            return body
        if child1.type == "double":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "c.lt.d %s, %s\n" % (FOP2, FOP1)
            return body
    if ast.name == "le_expr":
        if child1.type == "int":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "sle %s, %s %s\n" % (OP1, OP2, TMP)
            return body
        if child1.type == "double":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "c.le.d %s, %s\n" % (FOP1, FOP2)
            return body
    if ast.name == "ge_expr":
        if child1.type == "int":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "sle %s, %s %s\n" % (OP1, TMP, OP2)
            return body
        if child1.type == "double":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "c.le.d %s, %s\n" % (FOP2, FOP1)
            return body
    if ast.name == "eq_expr":
        if child1.type == "int":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "seq %s, %s %s\n" % (OP1, OP2, TMP)
            return body
        elif child1.type == "double":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "c.eq.d %s, %s\n" % (FOP1, FOP2)
            return body
    if ast.name == "ne_expr":
        if child1.type == "int":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "sne %s, %s %s\n" % (OP1, OP2, TMP)
            return body
        if child1.type == "double":
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "c.eq.d %s, %s\n" % (FOP1, FOP2)
            # float instruction does not have not equal so swap the answer
            return body
    if ast.name == "and_expr":
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "and %s, %s %s\n" % (OP1, OP2, TMP)
            return body
    if ast.name == "or_expr":
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "or %s, %s %s\n" % (OP1, OP2, TMP)
            return body

    if ast.name == "while_stmt":
        while_start, while_end = sym_table.get_label('while')
        body = '%s:\n' % (while_start)
        body += code_gen(ast.children[0], while_end) + '\n'
        body += 'beq %s, $0, %s\n' % (OP1, while_end)
        body += 'sll $0, $0, 0\n'
        body += code_gen(ast.children[1], while_end) + '\n'
        body += 'j %s\n' % (while_start)
        body += '%s: sll $0, $0, 0\n' % (while_end)
        return body

    if ast.name == "for_stmt":
        for_start, for_end = sym_table.get_label('for')
        body = code_gen(ast.children[0], for_end) + '\n'
        body = '%s:\n' % (for_start)
        body += code_gen(ast.children[1], for_end) + '\n'
        body += 'beq %s, $0, %s\n' % (OP1, for_end)
        body += 'sll $0, $0, 0\n'
        body += code_gen(ast.children[2], for_end) + '\n'
        body += 'j %s\n' % (for_start)
        body += '%s: sll $0, $0, 0\n' % (for_end)
        return body

    if ast.name == "break":
        return 'j %s' % (prevLoopEnd)

    if ast.name == "if_stmt":
        not_if = sym_table.get_label('if')
        body = code_gen(ast.children[0], prevLoopEnd) + '\n'
        body += 'beq %s, $0, %s\n' % (OP1, not_if)
        body += 'sll $0, $0, 0\n'
        body += code_gen(ast.children[1], prevLoopEnd) + '\n'
        body += '%s: sll $0, $0, 0\n' % (not_if)
        if len(ast.children) == 3:
            body += code_gen(ast.children[2], prevLoopEnd) + '\n'
        return body


def final_code(code):
    parser = Lark(grammar, parser='lalr', transformer=CreateAST())
    ast = parser.parse(code)
    global sym_table
    sym_table = SymTable(ast)
    sym_table.symbolize()
    return sym_table.data_code + "\n" + NEW_LINE + ": .asciiz \"\n\" \n" + ".text\n" + code_gen(ast)


easy_code = """
int main(){
    int a;
    a = 2;
    Print(a);

}
"""

# print(final_code(easy_code))
