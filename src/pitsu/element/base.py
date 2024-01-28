from ..class_list import *
from ..attributes import *

class Element:
    def __init__(self, __name: str, *children, **attributes):
        self.__children = list(children)
        self.__attributes = Attributes(**attributes)
        self.__name = __name
        self.__class_list = Class_List()
    
    @property
    def children(self):
        return self.__children

    @property
    def attributes(self):
        return self.__attributes
    
    @property
    def name(self):
        return self.__name
    
    @property
    def class_list(self):
        return self.__class_list
    
    def pack(self) -> str:
        raise NotImplemented