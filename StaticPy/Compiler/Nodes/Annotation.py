class Annotation:
    def __init__(self, struct: dict) -> None:
        '''
        struct - структура этой аннотации в виде словоря
        '''
        self.struct = struct


    def run(self, AST):
        pass
