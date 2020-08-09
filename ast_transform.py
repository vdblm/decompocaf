from lark import Transformer


class AST:
    def __init__(self, name, children):
        self.name = name

        # list of AST nodes
        self.children = children

    def __str__(self):
        return self.__print()

    def __print(self, indent=0):
        ret = "*" * indent + "name: " + self.name + "\n"
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
            return str(args[0])
        else:
            # todo arrays
            raise Exception("No array type")

    def function_decl(self, args):
        # print("function_decl", args)
        return AST("function_decl", [str(args[0]), args[1], args[3], args[5]])

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
        return AST('stmt', args)

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
            # | constant | lvalue | "this" | call | "(" expr ")"
            # | "!" expr | "ReadInteger" "(" ")" | "ReadLine" "(" ")"
            # | "new" IDENT | "NewArray" "(" expr "," type ")"
            return args[0]

        if args[1] == '=':
            return AST("assign_exp", [args[0], args[2]])
            # return 'mov ' + args[0] + ', ' + args[1]
        if len(args == 3):
            if args[1] == '+':
                return AST("add_expr", [args[0], args[2]])
            if args[1] == '-':
                return AST("sub_expr", [args[0], args[2]])
            if args[1] == '*':
                return AST("mult_expr", [args[0], args[2]])
            if args[1] == '/':
                return AST("div_expr", [args[0], args[2]])
            if args[1] == '%':
                return AST("mod_expr", [args[0], args[2]])
            if args[1] == '<':
                return AST("lt_expr", [args[0], args[2]])
            if args[1] == '>':
                return AST("gt_expr", [args[0], args[2]])
            if args[1] == '<=':
                return AST("le_expr", [args[0], args[2]])
            if args[1] == '>=':
                return AST("ge_expr", [args[0], args[2]])
            if args[1] == '==':
                return AST("eq_expr", [args[0], args[2]])
            if args[1] == '!=':
                return AST("ne_expr", [args[0], args[2]])
            if args[1] == '&&':
                return AST("and_expr", [args[0], args[2]])
            if args[1] == '||':
                return AST("or_expr", [args[0], args[2]])

        return args[0]

    # def add_expr(self, args):
    #     # print('add_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'add ax, ' + args[1] + '\n'
    #
    #     return retVal
    #
    # def sub_expr(self, args):
    #     # print('sub_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'sub ax, ' + args[1] + '\n'
    #
    #     return retVal
    #
    # def mult_expr(self, args):
    #     # print('mult_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'mult ax, ' + args[1] + '\n'
    #
    #     return retVal
    #
    # def div_expr(self, args):
    #     # print('div_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'div ax, ' + args[1] + '\n'
    #
    #     return retVal
    #
    # def mod_expr(self, args):
    #     # print('mod_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'mod ax, ' + args[1] + '\n'
    #
    #     return retVal
    #
    # def lt_expr(self, args):
    #     # print('lt_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'lt ax, ' + args[1] + '\n'
    #
    #     return retVal
    #
    # def le_expr(self, args):
    #     # print('le_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'le ax, ' + args[1] + '\n'
    #
    #     return retVal
    #
    # def gt_expr(self, args):
    #     # print('gt_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'gt ax, ' + args[1] + '\n'
    #
    #     return retVal
    #
    # def ge_expr(self, args):
    #     # print('ge_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'ge ax, ' + args[1] + '\n'
    #
    #     return retVal
    #
    # def ne_expr(self, args):
    #     # print('ne_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'ne ax, ' + args[1] + '\n'
    #
    #     return retVal
    #
    # def eq_expr(self, args):
    #     # print('eq_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'eq ax, ' + args[1] + '\n'
    #
    #     return retVal
    #
    # def and_expr(self, args):
    #     # print('and_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'and ax, ' + args[1] + '\n'
    #
    #     return retVal
    #
    # def ge_expr(self, args):
    #     # print('ge_expr', args)
    #     retVal = 'mov ax, ' + args[0] + '\n'
    #     retVal += 'ge ax, ' + args[1] + '\n'
    #
    #     return retVal

    def lvalue(self, args):
        # print('lvalue', args)
        # return 'mov ax, ' + '___'.join(args)
        if len(args) == 1:
            return AST("lvalue", [args[0]])

        else:
            # TODO fix this
            raise Exception

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
    #     return str(args[0])

    # def INT_CONST(self, args):
    #     return str(args[0])

    # def DOUBLE_CONST(self, args):
    #     return str(args[0])

    # def BOOL_CONST(self, args):
    #     return str(args[0])

    # def STR_CONST(self, args):
    #     return str(args[0])
