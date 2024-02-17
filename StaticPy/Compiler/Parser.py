from rply import ParserGenerator
from rply import Token

from Compiler.Nodes.Annotation import *
from Compiler.Nodes.InitVariable import *


class Parser:
    def __init__(self) -> None:
        self.parse = ParserGenerator(
            [
                'FLOAT', 'INT', 'BOOL', 'STR', 'INT-0x', 'INT-0o', 'INT-0b',
                'COMMENT', 'NAME', 'NEW_LINE', 'CONST',
                '=', ':', '[', ']', ',', '.', '(' ,')',
            ]
        )

        ###################################
        # Создание переменных
        ###################################

        @self.parse.production('$command : NAME : $annotation = $expression')
        def index(prod):
            return NewVariable( prod[0].value, prod[2].value, prod[4].value )
        
        @self.parse.production('$command : CONST NAME : $annotation = $expression')
        def index(prod):
            return NewConst( name=prod[1].value, annot=prod[3], value=int(prod[5]) )
        

        ###################################
        # Создание переменных
        ###################################

        @self.parse.production('$expression : ( $expression )')
        def index(prod):
            return prod[1]
        
        @self.parse.production('$expression : NAME | INT | BOOL | STR | FLOAT')
        def index(prod) -> Token:
            return prod[0]
        

        ###################################
        # Аннотации
        ###################################

        @self.parse.production('$annotation : NAME | INT | BOOL | FLOAT | STR')
        def index(prod) -> Token:
            return prod[0]

        @self.parse.production('$annotation : NAME [ $annotation-params ]')
        def index(prod):
            return [prod[0], prod[2]]
        
        @self.parse.production('$annotation-params : $annotation-params , $annotation')
        def index(prod):
            return [*prod[0], prod[2]]
        
        @self.parse.production('$annotation-params : $annotation')
        def index(prod):
            return [ prod[0] ]


    def run(self, tokens):
        return self.parse.build().parse(tokens)