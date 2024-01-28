from .element.base import Element
from typing import *
from typing import __all__ as typing_all
from abc import abstractmethod
from .attributes import Attributes as _attrs

_T = TypeVar("_T")

class _alias:
    def __new__(self, type_: type[_T], name: str) -> type[_T]:
        return type(name, (type_,), {})

__all__ = [
    "Child",
    "Children",
    "Value",
    "Unused",
    "Constant",
    "SupportsPack",
    "Attributes"
]

__all__.extend(typing_all)

del typing_all

Child = Union[str, Element]
Children = Sequence[Child]
Unused = object
Constant = type("Constant", (int,), {})
Value = Union[str, Constant]
Attributes = _alias(_attrs, "Attributes")

class SupportsPack(Protocol):
    """An ABC with one abstract method __pack__."""
    __slots__ = ()
    @abstractmethod
    def __pack__(self) -> str:
        pass