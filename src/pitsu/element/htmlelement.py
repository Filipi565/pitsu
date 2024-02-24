from ..typing import Child
from .element import Element

class HtmlElement(Element):
    def __init__(self, *children: Child, **attributes: str):
        super().__init__("html", *children, **attributes)
    
    def pack(self) -> str:
        return "<!DOCTYPE html>\n" + super().pack()