from ast_transform import AST


class SymTable:
    def __init__(self, ast):
        self.ast = ast
        self.scope_stack = [Scope(0)]
        self.var_type = dict()
        self.last_num = 0
        self.data_code = ".data # Data section\n"

    def symbolize(self):
        self.__symbolize(self.ast)

    def __symbolize(self, ast):

        if ast.name == "program":
            for child in ast.children:
                # handle global vars
                if isinstance(child, AST) and child.name == "variable_decl":
                    self.last_num += 1
                    scope = Scope(self.last_num)
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
                elif isinstance(child, AST):
                    self.__symbolize(child)

            self.scope_stack.pop()

        elif ast.name == "lvalue":
            real_name = self.__search_var(ast.children[0])
            assert real_name is not None
            ast.children[0] = real_name

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
        self.var_type[var_name] = var_type
        scope.add_var(var_name, var_type)
        code = var_name + ": "

        # TODO handle all types
        if var_type == "int":
            code += ".word 0\n"
        self.data_code += code

    def fetch(self, var_name):
        # returns address, type (int, double, string, ...)
        return var_name, self.var_type[var_name]

    def get_label(self, command):
        # command \in {"while", "if", "for", ...}
        # returns labels like "WHILE00", ...
        pass


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
