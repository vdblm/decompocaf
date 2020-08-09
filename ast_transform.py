from lark import Transformer


class AST:
    def __init__(self, name, children):
        self.name = name

        # list of AST nodes
        self.children = children
        self.type = None

    def __str__(self):
        return self.__print()

    def __print(self, indent=0):
        ret = "*" * indent + self.name + ", type: " + str(self.type) + "\n"
        for child in self.children:
            if isinstance(child, AST):
                ret += child.__print(indent + 1) + "\n"
            else:
                ret += "*" * (indent + 1) + str(child) + "\n"
        return ret


class CreateAST(Transformer):
    def start(self, args):
        return args[0]

    def program(self, args):
        # print("program", args)
        return AST("program", args)

    def decl(self, args):
        # print('decl', args)
        return args[0]

    def variable_decl(self, args):
        # print('variable_decl', args)
        return AST("variable_decl", [args[0]])

    def variable(self, args):
        # print('variable', args)
        return AST("variable", args)

    def type(self, args):
        if len(args) == 1:
            return AST("type", [args[0]])
        else:
            # todo arrays
            raise Exception("No array type")

    def function_decl(self, args):
        # print("function_decl", args)
        return AST("function_decl", [args[0], args[1], args[3], args[5]])

    def void_type(self, args):
        return AST("void_type", [])

    def formals(self, args):
        # print('formals', args)
        if len(args) == 0:
            return None
        else:
            return AST("formals", args)

    #
    # def class_decl(self, args):
    #     # print('class_decl', args)
    #     # "class" IDENT ["extends" IDENT] ["implements" IDENT ("," IDENT)*] "{" field* "}"
    #     return ';;;;;;; WE ARE FUCKED BROs'
    #
    # def field(self, args):
    #     # print('field', args)
    #     return args[0]
    #
    # def interface_decl(self, args):
    #     # print('interface_decl', args)
    #     #"interface" IDENT "{" prototype* "}"
    #     return ';;;;;;; WE ARE FUCKED BROs'
    #
    # def prototype(self, args):
    #     # print('prototype', args)
    #     # type IDENT "(" formals ")" ";"
    #     #     | "void" IDENT "(" formals ")" ";"
    #     return ';;;;;;; WE ARE FUCKED BROs'

    def stmt_block(self, args):
        # print('stmt_block', args)
        return AST("stmt_block", args)

    def stmt(self, args):
        # print('stmt', args)
        return args[0]

    def if_stmt(self, args):
        children = [args[2], args[4]]
        if args[6] is not None:
            children.append(args[6])
        return AST('if_stmt', children)

    def while_stmt(self, args):
        return AST('while_stmt', [args[0], args[1]])

    def for_stmt(self, args):
        # TODO handle  "for" "(" [expr] ";" expr ";" [expr] ")" stmt
        return AST('for_stmt', [args[2], args[4], args[6], args[8]])

    def return_stmt(self, args):
        # print('return_stmt', args)
        children = []
        if len(args) == 1:
            children.append(args[0])
        return AST("return_stmt", children)

    def break_stmt(self, args):
        return AST("break", [])

    def print_stmt(self, args):
        # print('print_stmt', args)
        return AST("print_stmt", args)

    def expr(self, args):
        if len(args) == 1:
            # | constant | lvalue | "this" | call
            if str(args[0]) == "this":
                return AST("this", [])
            else:
                return args[0]
        if len(args) == 2:
            # "-" expr | "!" expr
            if str(args[0]) == "-":
                return AST("minus_expr", [args[1]])
            if str(args[0]) == "!":
                return AST("not_expr", [args[1]])

        if len(args) == 3:
            #      "(" expr ")" | lvalue "=" expr
            #      | expr "+" expr | expr "-" expr | expr "*" expr | expr "/" expr
            #      | expr "%" expr |  | expr "<" expr | expr "<=" expr | expr ">" expr
            #      | expr ">=" expr | expr "!=" expr | expr "==" expr | expr "&&" expr
            #      | expr "||" expr
            if str(args[0]) == "(":
                return AST("par_expr", [args[1]])
            op = str(args[1])
            if op == '=':
                return AST("assign_expr", [args[0], args[2]])
            if op == '+':
                return AST("add_expr", [args[0], args[2]])
            if op == '-':
                return AST("sub_expr", [args[0], args[2]])
            if op == '*':
                return AST("mult_expr", [args[0], args[2]])
            if op == '/':
                return AST("div_expr", [args[0], args[2]])
            if op == '%':
                return AST("mod_expr", [args[0], args[2]])
            if op == '<':
                return AST("lt_expr", [args[0], args[2]])
            if op == '>':
                return AST("gt_expr", [args[0], args[2]])
            if op == '<=':
                return AST("le_expr", [args[0], args[2]])
            if op == '>=':
                return AST("ge_expr", [args[0], args[2]])
            if op == '==':
                return AST("eq_expr", [args[0], args[2]])
            if op == '!=':
                return AST("ne_expr", [args[0], args[2]])
            if op == '&&':
                return AST("and_expr", [args[0], args[2]])
            if op == '||':
                return AST("or_expr", [args[0], args[2]])

        # "ReadInteger" "(" ")" | "ReadLine" "(" ")"
        #      | "new" IDENT | "NewArray" "(" expr "," type ")"
        if str(args[0]) == "ReadInteger":
            return AST("read_integer", [])
        elif str(args[0]) == "ReadLine":
            return AST("read_line", [])
        elif str(args[0]) == "new" or str(args[0]) == "NewArray":
            raise Exception("No array or class")

        raise Exception("Expr error")

    def lvalue(self, args):
        # print('lvalue', args)
        # return 'mov ax, ' + '___'.join(args)
        if len(args) == 1:
            return AST("lvalue", [args[0]])

        else:
            # TODO fix this
            raise Exception("No array or class")

    def call(self, args):
        # print('call', args)
        # retVal = '\n'.join(list(map(lambda x: 'mov ax,+x', args[1:]))) + '\n'
        # retVal += 'jump ' + args[0]
        if str(args[1]) == "(":
            return AST("call", [args[0], args[2]])
        else:
            raise Exception("Not defined class func call")

    def actuals(self, args):
        # print('actuals', args)
        return AST("actuals", args)

    def constant(self, args):
        # print('constant', args)
        return AST("constant", [args[0]])

    # def IDENT(self, args):
    #     return AST("ident", [str(args[0])])

    def null(self, args):
        ast = AST("null", [])
        ast.type = "null"
        return ast

    def int_cons(self, args):
        ast = AST("int_const", [args[0]])
        ast.type = "int"
        return ast

    def double_cons(self, args):
        ast = AST("double_const", [args[0]])
        ast.type = "double"
        return ast

    def bool_cons(self, args):
        ast = AST("bool_const", [args[0]])
        ast.type = "bool"
        return ast

    def str_cons(self, args):
        ast = AST("str_const", [args[0]])
        ast.type = "string"
        return ast
