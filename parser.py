from lark import Lark
from ast_transform import AST, CreateAST
from grammar import grammar
from symbol_table import SymTable

OP1 = "ax"
OP2 = "bx"

TMP = "cx"

sym_table = SymTable()
# TODO walk over AST to update sym_table (vahid)


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

    if ast.name == "while_stmt":
        while_start, while_end = sym_table.get_label('while')
        body = '%s:\n'%(while_start)
        body += code_gen(ast.children[0], while_end) + '\n'
        body += 'beq %s, $0, %s\n'%(OP1, while_end)
        body += 'sll $0, $0, 0\n'
        body += code_gen(ast.children[1], while_end) + '\n'
        body += 'j %s\n'%(while_start)
        body += '%s: sll $0, $0, 0\n'%(while_end)
        return body
    
    if ast.name == "for_stmt":
        for_start, for_end = sym_table.get_label('for')
        body = code_gen(ast.children[0], for_end) + '\n'
        body = '%s:\n'%(for_start)
        body += code_gen(ast.children[1], for_end) + '\n'
        body += 'beq %s, $0, %s\n'%(OP1, for_end)
        body += 'sll $0, $0, 0\n'
        body += code_gen(ast.children[2], for_end) + '\n'
        body += 'j %s\n'%(for_start)
        body += '%s: sll $0, $0, 0\n'%(for_end)
        return body
    
    if ast.name == "break":
        return 'j %s'%(prevLoopEnd)
    
    if ast.name == "if_stmt":
        not_if = sym_table.get_label('if')
        body += code_gen(ast.children[0], prevLoopEnd) + '\n'
        body += 'beq %s, $0, %s\n'%(OP1, not_if)
        body += 'sll $0, $0, 0\n'
        body += code_gen(ast.children[1], prevLoopEnd) + '\n'
        body += '%s: sll $0, $0, 0\n'%(not_if)
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

print((parser.parse(easy_code)))
