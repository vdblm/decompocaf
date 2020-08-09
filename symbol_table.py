from ast_transform import AST


class SymTable:
    def __init__(self, ast):
        self.ast = ast
        self.scope_stack = [Scope(0)]
        self.var_types = dict()
        self.last_num = 0
        self.data_code = ".data # Data section\n"
        self.while_num = 0
        self.for_num = 0
        self.if_num = 0

    def symbolize(self):
        self.__symbolize(self.ast)

    def __symbolize(self, ast):

        if ast.name == "program":
            for child in ast.children:
                # handle global vars
                if isinstance(child, AST) and child.name == "variable_decl":
                    self.last_num += 1
                    scope = Scope(self.last_num)
                    self.__symbolize(child)
                    self.__handle_var_dec(child.children[0], scope)
                    self.scope_stack.append(scope)
                elif isinstance(child, AST):
                    self.__symbolize(child)

        elif ast.name == "function_decl":
            # todo handle formals and function scope
            # stmt_block
            self.__symbolize(ast.children[3])

        elif ast.name == "stmt_block":
            self.last_num += 1
            scope = Scope(self.last_num)
            self.scope_stack.append(scope)
            for child in ast.children:
                if isinstance(child, AST) and child.name == "variable_decl":
                    self.__handle_var_dec(child.children[0], scope)
                    self.__symbolize(child)
                elif isinstance(child, AST):
                    self.__symbolize(child)

            self.scope_stack.pop()

        elif ast.name == "lvalue":
            real_name = self.__search_var(ast.children[0])
            assert real_name is not None
            ast.children[0] = real_name
            var_type = self.var_types[real_name]
            ast.type = var_type

        elif "expr" in ast.name:
            if ast.name == "minus_expr" or ast.name == "not_expr" or ast.name == "par_expr":
                self.__symbolize(ast.children[0])
                ast.type = ast.children[0].type

            elif ast.name in ["add_expr", "sub_expr", "mult_expr", "div_expr", "mod_expr"]:
                self.__symbolize(ast.children[0])
                self.__symbolize(ast.children[1])
                typ1 = ast.children[0].type
                typ2 = ast.children[1].type
                assert typ1 == typ2
                ast.type = typ1
            else:
                self.__symbolize(ast.children[0])
                self.__symbolize(ast.children[1])
                ast.type = "bool"
        elif ast.name == "constant":
            ast.type = ast.children[0].type
        elif ast.name == "variable":
            ast.type = ast.children[0].children[0]
        else:
            for child in ast.children:
                if isinstance(child, AST):
                    self.__symbolize(child)

    def __search_var(self, var_name):
        for scope in reversed(self.scope_stack):
            var, typ = scope.get_var(var_name)
            if typ is not None:
                return var
        return None

    def __handle_var_dec(self, var_dec_ast, scope):
        # TODO bad bad bad kheili bad fixit
        var_type = var_dec_ast.children[0].children[0]
        var_name = var_dec_ast.children[1] + "_" + str(scope.num)
        var_dec_ast.children[1] = var_name
        self.var_types[var_name] = var_type
        scope.add_var(var_name, var_type)
        code = var_name + ": "

        # TODO handle all types
        if var_type == "int":
            code += ".word 0\n"
        elif var_type == "double":
            code += ".float 0\n"
        elif var_type == "bool":
            code += ".byte 0\n"
        elif var_type == "string":
            code += ".asciiz \"\""
        else:
            raise Exception("Not defined type")
        self.data_code += code

    def get_label(self, command):
        if command == "while":
            label1 = "WHILLE_START_" + str(self.while_num)
            label2 = "WHILLE_END_" + str(self.while_num)
            self.while_num += 1
            assert self.var_types.get(label1) is None
            assert self.var_types.get(label2) is None
            return label1, label2

        if command == "for":
            label1 = "FOOR_START_" + str(self.for_num)
            label2 = "FOOR_END_" + str(self.for_num)
            self.for_num += 1
            assert self.var_types.get(label1) is None
            assert self.var_types.get(label2) is None
            return label1, label2
        if command == "if":
            label = "IIF_" + str(self.if_num)
            self.if_num += 1
            assert self.var_types.get(label) is None
            return label


class Scope:
    def __init__(self, scope_num):
        self.num = scope_num

        # map of var and type
        self.vars = dict()

    def add_var(self, var_name, var_type):
        self.vars[var_name] = var_type

    def get_var(self, var_name):
        var = var_name + "_" + str(self.num)
        return var, self.vars.get(var)
