from lark import Lark, exceptions, Transformer
import logging

# logging.basicConfig(level=logging.DEBUG)

grammar = r"""
start : program

program : decl+

decl : variable_decl | function_decl | class_decl | interface_decl

variable_decl : variable ";"

variable : type IDENT

type : "int" | "double" | "bool" | "string" | IDENT | type "[]"

function_decl : type IDENT "(" formals ")" stmt_block
              | "void" IDENT "(" formals ")" stmt_block

formals : variable ("," variable)*
        |

class_decl : "class" IDENT ["extends" IDENT] ["implements" IDENT ("," IDENT)*] "{" field* "}"

field : variable_decl | function_decl

interface_decl : "interface" IDENT "{" prototype* "}"

prototype : type IDENT "(" formals ")" ";" 
          | "void" IDENT "(" formals ")" ";"
          
stmt_block : "{" variable_decl* stmt* "}"

stmt : [expr] ";" | if_stmt | while_stmt | for_stmt 
     | break_stmt | return_stmt | print_stmt | stmt_block
    
if_stmt : "if" "(" expr ")" stmt ["else" stmt]

while_stmt : "while" "(" expr ")" stmt

for_stmt : "for" "(" [expr] ";" expr ";" [expr] ")" stmt

return_stmt : "return" [expr] ";"

break_stmt : "break" ";"

print_stmt : "Print" "(" expr ("," expr)* ")" ";"

expr : lvalue "=" expr | constant | lvalue | "this" | call | "(" expr ")"
     | add_expr | sub_expr | mult_expr | div_expr 
     | mod_expr | "-" expr | lt_expr | le_expr | gt_expr
     | ge_expr | ne_expr | eq_expr | and_expr
     | or_expr | "!" expr | "ReadInteger" "(" ")" | "ReadLine" "(" ")"
     | "new" IDENT | "NewArray" "(" expr "," type ")"

add_expr : expr "+" expr

sub_expr : expr "-" expr

mult_expr : expr "*" expr

div_expr : expr "/" expr

mod_expr : expr "%" expr

lt_expr : expr "<" expr

le_expr : expr "<=" expr

gt_expr : expr ">" expr

ge_expr : expr ">=" expr

ne_expr : expr "!=" expr

eq_expr : expr "==" expr

and_expr : expr "&&" expr

or_expr : expr "||" expr

lvalue : IDENT | expr "." IDENT | expr "[" expr "]"

call : IDENT "(" actuals ")" | expr "." IDENT "(" actuals ")"

actuals : expr ("," expr)*
        |

constant : INT_CONST | DOUBLE_CONST | BOOL_CONST | STR_CONST | "null"

IDENT : /([a-z]|[A-Z])([a-z]|[A-Z]|[0-9]|_){0,30}/

INT_CONST : /(((0[xX])([0-9]|[a-f]|[A-F])+)|[0-9]+)/

DOUBLE_CONST : /(([0-9]+\.([0-9]*)[eE][-+]?([0-9]+))|([0-9]+\.([0-9]*)))/

BOOL_CONST : /true|false/

STR_CONST : /"[^\n"]*"/

// ignore white-spaces
%import common.WS
%ignore WS

// comments are ignored :)
%ignore /(\/\/[^\n]*)/
%ignore /(\/\*([^\*]|[\r\n]|(\*([^\/]|[\r\n])))*\*\/)/
"""

class SemanticActions(Transformer):
    def start(self, args):
        # print('start', args)
        return args[0]

    def program(self, args):
        # print('program', args)
        return "\n".join(args)

    def decl(self, args):
        # print('decl', args)
        return args[0]

    def variable_decl(self, args):
        # print('variable_decl', args)
        return args[0]

    def variable(self, args):
        # print('variable', args)
        return args[0] + '_' + args[1] + ':'

    def type(self, args):
        # print('type', args)
        try:
            if len(args) == 1:
                return args[0]
            
            return args[0] + '[]'
        except:
            return ';;;;;;;;;;;;;;;' # TODO

    def function_decl(self, args):
        # print('function_decl', args)
        retVal = ';;;;; Begin Function \n'
        retVal += args[0] + '_' + args[1] + ':\n'
        retVal += args[2] + '\n'
        retVal += args[3] # TODO

        return retVal

    def formals(self, args):
        # print('formals', args)
        return '\n'.join([arg for arg in args if arg != ','])

    def class_decl(self, args):
        # print('class_decl', args)
        # "class" IDENT ["extends" IDENT] ["implements" IDENT ("," IDENT)*] "{" field* "}"
        return ';;;;;;; WE ARE FUCKED BROs'

    def field(self, args):
        # print('field', args)
        return args[0]

    def interface_decl(self, args):
        # print('interface_decl', args)
        #"interface" IDENT "{" prototype* "}"
        return ';;;;;;; WE ARE FUCKED BROs'

    def prototype(self, args):
        # print('prototype', args)
        # type IDENT "(" formals ")" ";" 
        #     | "void" IDENT "(" formals ")" ";"
        return ';;;;;;; WE ARE FUCKED BROs'
            
    def stmt_block(self, args):
        # print('stmt_block', args)
        return '\n'.join(args)

    def stmt(self, args):
        # print('stmt', args)
        return args[0]
        
    def if_stmt(self, args):
        # print('if_stmt', args)
        retVal = 'mov tmp_0001,' + args[0] + '\n'
        retVal += 'bz tmp_0001, else_0001' + '\n'
        retVal += args[1] + '\n'
        retVal += 'else_0001:\n'
        if len(args) >= 7:
            retVal += args[2] + '\n'
        
        return retVal

    def while_stmt(self, args):
        # print('while_stmt', args)
        retVal = 'loop_start_0001:\n'
        retVal += 'mov tmp_0001,' + args[0] + '\n'
        retVal += 'bz tmp_0001, endwhile_0001' + '\n'
        retVal += args[1] + '\n'
        retVal += 'jump loop_start_0001\n'
        retVal += 'endwhile_0001: nop\n'

        return retVal

    def for_stmt(self, args):
        # print('for_stmt', args)
        # Assume the existence of all optional parts
        retVal = args[0] + '\n'
        retVal += 'loop_start_0001:\n'
        retVal += 'mov tmp_0001,' + args[1] + '\n'
        retVal += 'bz tmp_0001, endfor_0001' + '\n'
        retVal += args[2] + '\n'
        retVal += args[3] + '\n'
        retVal += 'jump loop_start_0001\n'
        retVal += 'endfor_0001: nop\n'

        return retVal

    def return_stmt(self, args):
        # print('return_stmt', args)
        # "return" [expr] ";"
        return ';;;;;;; WE ARE FUCKED BROs'

    def break_stmt(self, args):
        # print('break_stmt', args)
        return 'jump endfor_0001' # maybe while

    def print_stmt(self, args):
        # print('print_stmt', args)
        # "Print" "(" expr ("," expr)* ")" ";"
        return ';;;;;;; WE ARE FUCKED BROs'

    def expr(self, args):
        # print('expr', args)
        if len(args) != 2:
            # | constant | lvalue | "this" | call | "(" expr ")"
            # | "!" expr | "ReadInteger" "(" ")" | "ReadLine" "(" ")"
            # | "new" IDENT | "NewArray" "(" expr "," type ")"
            return args[0]

        if args[1] == '=':
            return 'mov ' + args[0] + ', ' + args[1]
        
        return args[0]
    
    def add_expr(self, args):
        # print('add_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'add ax, ' + args[1] + '\n'
        
        return retVal
    
    def sub_expr(self, args):
        # print('sub_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'sub ax, ' + args[1] + '\n'
        
        return retVal

    def mult_expr(self, args):
        # print('mult_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'mult ax, ' + args[1] + '\n'
        
        return retVal

    def div_expr(self, args):
        # print('div_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'div ax, ' + args[1] + '\n'
        
        return retVal
    
    def mod_expr(self, args):
        # print('mod_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'mod ax, ' + args[1] + '\n'
        
        return retVal

    def lt_expr(self, args):
        # print('lt_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'lt ax, ' + args[1] + '\n'
        
        return retVal

    def le_expr(self, args):
        # print('le_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'le ax, ' + args[1] + '\n'
        
        return retVal
    
    def gt_expr(self, args):
        # print('gt_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'gt ax, ' + args[1] + '\n'
        
        return retVal

    def ge_expr(self, args):
        # print('ge_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'ge ax, ' + args[1] + '\n'
        
        return retVal
    
    def ne_expr(self, args):
        # print('ne_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'ne ax, ' + args[1] + '\n'
        
        return retVal

    def eq_expr(self, args):
        # print('eq_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'eq ax, ' + args[1] + '\n'
        
        return retVal
    
    def and_expr(self, args):
        # print('and_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'and ax, ' + args[1] + '\n'
        
        return retVal

    def ge_expr(self, args):
        # print('ge_expr', args)
        retVal = 'mov ax, ' + args[0] + '\n'
        retVal += 'ge ax, ' + args[1] + '\n'
        
        return retVal

    def lvalue(self, args):
        # print('lvalue', args)
        return 'mov ax, ' + '___'.join(args)

    def call(self, args):
        # print('call', args)
        retVal = '\n'.join(list(map(lambda x: 'mov ax,+x', args[1:]))) + '\n'
        retVal += 'jump ' + args[0]

        return retVal;

    def actuals(self, args):
        # print('actuals', args)
        return args[0]

    def constant(self, args):
        # print('constant', args)
        return str(args[0])
    
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


parser = Lark(grammar, parser='lalr', transformer=SemanticActions())

code = """
int someFunction(int a)
{
    int i;
    for(i = 0; i < 100; i = i+1)
    {
        a = a + i;
    }

    return a;
}

int main()
{
    return someFunction(10);
}
"""

# code = """
# int getSomeValue() {
#     return something;
# }

# int main() {
#     int a;
#     int b;
#     bool c;
#     double d;
#     d = 1.2E5 * 5. + 1.;
#     c = (a / b < 100) || (!(((a * b) / (a + b)) <= 20) && (a < -10 && b < a || b > 5))
#      || getSomething() % 2 == 42;
#     c = true || false;
# }
# """

print(parser.parse(code))

