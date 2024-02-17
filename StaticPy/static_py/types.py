'''
Все представленные типы StaticPy в реализации
'''

from typing import Any
from typing import Self

from enum import Enum


class Null:
    def __init__(self) -> None:
        pass

    def __eq__(self, __value: Self) -> bool:
        return isinstance(__value, Null)


class struct:
    def __init__(self, nameStruct: str, items: dict[str, Any]):
        self.nameStruct = nameStruct
        self.items = items

    def __getitem__ (self, index: str):
        return self.items[index]
    
    def __eq__(self, __value: Self) -> bool:
        return __value.nameStruct == self.nameStruct and __value.items == self.items
    
    def __call__(self) -> tuple:
        return tuple([self.items[key] for key in self.items])


class typedef:
    def __init__(self, *args: list[type, str]) -> None:
        self.annotations = dict([(args[index], args[index+1]) for index in range(0, len(args), 2)])


class CTypes(Enum):
    I8 = I16 = I32 = I64 = DOUBLE = BYTES = ARRAY = None
