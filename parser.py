from lark import Lark
from ast_transform import AST, CreateAST
from grammar import grammar


def code_gen(ast: AST):
    if ast.name == "program":
        return "\n".join([code_gen(child) for child in ast.children])

    if ast.name == "variable_decl":
        pass
    if ast.name == "function_decl":
        if ast.children[1] == "main":
            body = code_gen(ast.children[3])
            return "main:\n" + body
        else:
            # TODO
            pass
    if ast.name == "stmt_block":
        # iterate till variable declaration is finished
        res = filter(lambda x: x.name != "variable_decl", ast.children)
        return "\n".join([code_gen(a) for a in list(res)])

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


parser = Lark(grammar, parser='lalr', transformer=CreateAST())

easy_code = """
int main(){
    int a;
    a = 2;
}
"""

print(code_gen(parser.parse(easy_code)))
