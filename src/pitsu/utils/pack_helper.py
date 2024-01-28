from ..element.base import Element
from ..constants import *
from ..class_list import Class_List
from ..typing import Value, Child, Unused

NEW_LINE = "\n"
SPACE = " "

def _attributes(**attributes: Value):
    for atributo, valor in attributes.items():
        if valor == NO_VALUE:
            yield atributo
            continue

        if atributo.startswith("_"):
            continue

        if atributo.endswith("_"):
            atributo = atributo[0:-1]

        if not valor:
            continue
        
        yield f"{atributo}=\"{valor}\""
    
class Pack_Helper:
    @classmethod
    def pack_with_double(cls, element_name: str, class_list: Class_List, *children: Child, **attributes: Value):
        atributos: list[str] = list()
        attributes["class"] = SPACE.join(class_list)

        atributos.extend(_attributes(**attributes))

        children = [child.pack() if isinstance(child, Element) else child for child in children]
        
        start = element_name if not atributos else f"{element_name} "
        middle = "" if not children else "\n"
        end = f"</{element_name}>"
        
        return f"<{start}{SPACE.join(atributos)}>{middle}{NEW_LINE.join(children)}{middle}{end}\n"

def pack_with_double(element_name: str, class_list: Class_List, *children: Child, **attributes: Value):
    value = Pack_Helper.pack_with_double(element_name, class_list, *children, **attributes)
    lista: list[str] = list()
    for linha in value.splitlines():
        if linha:
            lista.append(linha)
        else:
            pass
    
    return "\n".join(lista)

def pack_no_double(element_name: str, class_list: Class_List, *children: Unused, **attributes: Value):
    atributos: list[str] = list()
    attributes["class"] = SPACE.join(class_list)

    atributos.extend(_attributes(**attributes))

    start = element_name if not atributos else f"{element_name} "
    end = " />"

    return f"<{start}{SPACE.join(atributos)}{end}\n"