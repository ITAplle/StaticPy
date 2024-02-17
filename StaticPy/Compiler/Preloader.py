from os import path
from json import loads


class Preloader:
    def __init__(self, pathProject: str, ) -> None:
        self.pathProject = pathProject


    def run(self):
        if not \
            path.exists('build') \
            and path.exists('src') \
            and path.exists('conf.json') \
            and path.exists('conf.json') \
            and path.exists('src/main.spy'):
            raise BaseException()

        with open( path.join(self.pathProject, 'conf.json'), 'r', encoding='utf-8') as file:
            conf: dict = loads( file.read() )

        with open( path.join(self.pathProject, 'src/main.spy'), 'r', encoding='utf-8') as file:
            code: str = file.read()

        return code