from lark import Lark

from ast_transform import AST, CreateAST
from grammar import grammar
from symbol_table import SymTable

OP1 = "ax"
OP2 = "bx"

TMP = "cx"


def code_gen(ast: AST, prevLoopEnd=None):
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
        return "\n".join([code_gen(a, prevLoopEnd) for a in list(res)])

    if ast.name == "assign_exp":
        lvalue = ast.children[0]
        exp = ast.children[1]
        body = ""
        if exp.name == "constant":
            # $rt register for address
            const = exp.children[0]
            # it depends on lvalue type!
            body += "li $rt, " + const + " # load constant to $ra\n"
            # TODO should find the lvalue label in the symbol table
            label = lvalue.children[0]
            body += "sw $rt, " + label + " # store word in $rt to address " + label + "\n"
        return body

    if ast.name == "print_stmt":
        pass
    if ast.name == "add_expr":
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "add %s, %s %s\n" % (OP1, OP2, TMP)
            return body
    if ast.name == "sub_expr":
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "sub %s, %s %s\n" % (OP1, OP2, TMP)
            return body
    if ast.name == "mult_expr":
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "muhi %s\n" % (OP1)
            return body
    if ast.name == "div_expr":
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP1)
            body += "div %s, %s \n" % (OP1, OP2)
            body += "mflo %s\n" % (OP1)
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
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "slt %s, %s %s\n" % (OP1, OP2, TMP)
            return body
    if ast.name == "gt_expr":
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "slt %s, %s %s\n" % (OP1, TMP, OP2)
            return body
    if ast.name == "le_expr":
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "sle %s, %s %s\n" % (OP1, OP2, TMP)
    if ast.name == "ge_expr":
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "sle %s, %s %s\n" % (OP1, TMP, OP2)
            return body
    if ast.name == "eq_expr":
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "seq %s, %s %s\n" % (OP1, OP2, TMP)
            return body
    if ast.name == "ne_expr":
        if True:
            body = code_gen(ast.children[0]) + '\n'
            body += code_gen(ast.children[1]) + '\n'
            body += "move %s, %s \n" % (TMP, OP2)
            body += "move %s, %s \n" % (OP2, OP1)
            body += "sne %s, %s %s\n" % (OP1, OP2, TMP)
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
        body += code_gen(ast.children[0], prevLoopEnd) + '\n'
        body += 'beq %s, $0, %s\n' % (OP1, not_if)
        body += 'sll $0, $0, 0\n'
        body += code_gen(ast.children[1], prevLoopEnd) + '\n'
        body += '%s: sll $0, $0, 0\n' % (not_if)
        if len(ast.children) == 3:
            body += code_gen(ast.children[2], prevLoopEnd) + '\n'
        return body


parser = Lark(grammar, parser='lalr', transformer=CreateAST())

easy_code = """
int main(){
    int a;
    a = 2;

}
"""

ast = parser.parse(easy_code)
sym_table = SymTable(ast)
sym_table.symbolize()
print(code_gen(ast))
