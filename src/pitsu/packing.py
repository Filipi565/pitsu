from . import typing as t

def pack(Element: t.SupportsPack):
    element_type = type(Element)
    value = element_type.__pack__(Element)
    if isinstance(value, str):
        return value
    
    raise TypeError(f"expected {element_type.__name__}.__pack__() to return str, not {type(value).__name__}")