from .typing import SupportsPack

def pack(Element: SupportsPack) -> str:
    element_type = type(Element)
    value = element_type.__pack__(Element)
    if not isinstance(value, str):
        raise TypeError(f"expected to {element_type.__name__}.__pack__() to return str "
                        f"object, not {type(value).__name__}")
    
    return value