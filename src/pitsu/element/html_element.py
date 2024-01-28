from ..typing import Child, Value
from .element import Element

class HtmlElement(Element):
    def __init__(self, *children: Child, **attributes: Value):
        super().__init__("html", *children, **attributes)

    def pack(self):
        return "<!DOCTYPE html>\n" + super().pack()