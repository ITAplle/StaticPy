from rply import LexerGenerator
from re import DOTALL


class Lexer:
    def __init__(self) -> None:
        self.lex = LexerGenerator()

        self.lex.add('->', r'\-\>')

        self.lex.add('=//', r'\=//')
        self.lex.add('=/', r'\=\/')
        self.lex.add('=**', r'\=\*\*')
        self.lex.add('=+', r'\=\+')
        self.lex.add('=-', r'\=\-')
        self.lex.add('=*', r'\=\*')
        self.lex.add('=%', r'\=\%')
        self.lex.add('=&', r'\=\&')
        self.lex.add('=|', r'\=\|')
        self.lex.add('=^', r'\=\^')
        self.lex.add('=>>', r'\=\>\>')
        self.lex.add('=<<', r'\=\<\<')

        self.lex.add('=', r'\=')

        self.lex.add(':', r'\:')
        self.lex.add('.', r'\.')
        self.lex.add(',', r'\,')
        self.lex.add(';', r'\;')
        
        self.lex.add('FLOAT', r'\d*\.\d+')
        self.lex.add('INT-0x', r'0x[A-Fa-f0-9]+')
        self.lex.add('INT-0o', r'0x[0-7]+')
        self.lex.add('INT-0b', r'0b[01]+')
        self.lex.add('INT', r'\d+')
        self.lex.add('BOOL', r'\bTrue\b|\bFalse\b')
        
        self.lex.add('STR', r'\".*?\"|\'.*?\'')
        self.lex.add('BIG-STR', r'\".*?\"|\'.*?\'', DOTALL)
        self.lex.add('fSTR', r'f\".*?\"|f\'.*?\'')
        self.lex.add('bSTR', r'b\".*?\"|b\'.*?\'')
        self.lex.add('rSTR', r'r\".*?\"|r\'.*?\'')

        self.lex.add('@', r'\@')
        
        self.lex.add('//', r'//')
        self.lex.add('**', r'\*\*')
        self.lex.add('+', r'\+')
        self.lex.add('-', r'\-')
        self.lex.add('*', r'\*')
        self.lex.add('/', r'\/')
        self.lex.add('%', r'\%')
        
        self.lex.add('&', r'\&')
        self.lex.add('|', r'\|')
        self.lex.add('^', r'\^')
        self.lex.add('>>', r'\>\>')
        self.lex.add('<<', r'\<\<')

        self.lex.add('COMMENT', r'\#\.*')

        self.lex.add('(', r'\(')
        self.lex.add(')', r'\)')
        self.lex.add('{', r'\{')
        self.lex.add('}', r'\}')
        self.lex.add('[', r'\[')
        self.lex.add(']', r'\]')

        ####################
        ## НОВЫЙ СТАНДАРТ ##
        ####################
        self.lex.add('STRUCT', r'\bstruct\b')
        self.lex.add('TYPE', r'\btype\b')
        self.lex.add('FLEX', r'\bflex\b')
        self.lex.add('ABSTRACT', r'\babstract\b')
        self.lex.add('STATIC', r'\bstatic\b')
        self.lex.add('META', r'\bmeta\b')
        self.lex.add('DATA', r'\bdata\b')
        self.lex.add('AUTO', r'\bauto\b')
        self.lex.add('CONST', r'\bconst\b')
        self.lex.add('ENUM', r'\benum\b')
        # self.lex.add('', r'\b\b')

        #############################
        ## УНАСЛЕДОВАННЫЙ СТАНДАРТ ##
        #############################
        self.lex.add('CLASS', r'\bclass\b')
        self.lex.add('DEF', r'\bdef\b')
        self.lex.add('LAMBDA', r'\blambda\b')
        self.lex.add('RETURN', r'\breturn\b')
        self.lex.add('PASS', r'\bpass\b')
        self.lex.add('WHILE', r'\bwhile\b')
        self.lex.add('FOR', r'\bfor\b')
        self.lex.add('IN', r'\bin\b')
        self.lex.add('AS', r'\bas\b')
        self.lex.add('IF', r'\bif\b')
        self.lex.add('ELIF', r'\belif\b')
        self.lex.add('ELSE', r'\belse\b')
        self.lex.add('CONTINUE', r'\bcontinue\b')
        self.lex.add('BREAK', r'\bbreak\b')
        self.lex.add('ASSERT', r'\bassert\b')
        self.lex.add('MATCH', r'\bmatch\b')
        self.lex.add('CASE', r'\bcase\b') 
        self.lex.add('ASYNC', r'\basync\b')
        self.lex.add('AWAIT', r'\bawait\b')
        self.lex.add('DEL', r'\bdel\b')
        self.lex.add('EXCEPT', r'\bexcept\b')
        self.lex.add('FINALLY', r'\bfinally\b')
        self.lex.add('FROM', r'\bfrom\b')
        self.lex.add('IMPORT', r'\bimport\b')
        self.lex.add('IS', r'\bis\b')
        self.lex.add('RAISE', r'\braise\b')
        self.lex.add('YIELD', r'\byield\b')
        self.lex.add('WITH', r'\bwith\b')
        self.lex.add('TRY', r'\btry\b')
        # self.lex.add('', r'\b\b')
        
        self.lex.add('AND', r'\band\b')
        self.lex.add('OR', r'\bor\b')
        self.lex.add('NOT', r'\bnot\b')

        self.lex.add('NAME', r'\b\w+\b')
        
        self.lex.add('NEW_LINE', r'\n+')

        self.lex.ignore(r'[ \t\r]+')


    def run(self, code: str):
        return self.lex.build().lex(code)
    
    
    def show(self, code: str, spaces: int = 25):
        for i in self.lex.build().lex(code):
            print(' ' * spaces + 'VALUE: ' + i.value.replace('\n', '\\n') + '\rNAME: ' + i.name)