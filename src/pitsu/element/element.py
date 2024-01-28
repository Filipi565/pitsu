from . import base
from .. import typing as t
from ..errors import ElementError
from ..utils import pack_helper as ph

class Element(base.Element):
    def __init__(
        self,
        __name: str,
        *children: t.Child,
        **attributes: t.Value
    ):
        self.__double = attributes.pop("__double", True)
        if not isinstance(self.__double, bool):
            raise ElementError("expect bool object, not " + type(self.__double).__name__)

        super().__init__(__name, *children, **attributes)
    
    def __getitem__(self, value: str):
        return self.attributes[value]
    
    def __repr__(self):
        return f"Element(\'{self.name}\')"
    
    def __pack__(self):
        return self.pack()

    def editattribute(self, key: str, value: t.Value):
        self.attributes[key] = value
    
    def pack(self):
        if self.__double:
            pack_func = ph.pack_with_double
        else:
            pack_func = ph.pack_no_double
        
        return pack_func(self.name, self.class_list, *self.children, **self.attributes)

    @property
    def attributes(self) -> t.Attributes[str, t.Value]:
        return super().attributes
    
    @property
    def children(self) -> t.Children:
        return super().children