from Compiler.Generator import Generator
from Compiler.Lexer import Lexer
from Compiler.Preloader import Preloader
from Compiler.Parser import Parser

from warnings import filterwarnings
filterwarnings('ignore')


class StaticPy:
    '''
    Добро пожаловать в статически-типизированный Python!
    '''
    def __init__(self, path) -> None:
        preloder = Preloader(path)
        lex = Lexer()
        parse = Parser()
        gen = Generator(path)

        # lex.show( preloder.run() )

        gen.run(
            parse.run(
                lex.run(
                    preloder.run()
                )
            )
        )


StaticPy('C:/Users/1/Desktop/Мир/StaticPy/src/TestProject')
