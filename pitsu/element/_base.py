from .classes import Class_List as _class
from .. import ElementError

def _base1(name, attrs, *Any):
    content = list()
    for nome in attrs:
        if attrs[nome] and isinstance(attrs[nome], bool):
            content.append(nome)
        elif attrs[nome] and isinstance(attrs[nome], str):
            content.append(f'{nome}="{attrs[nome]}"')
        else:
            pass
    return f"""<{name} {' '.join(content)}>"""

def _base2(name, attrs, children):
    content = list()
    for nome in attrs:
        if attrs[nome] and isinstance(attrs[nome], bool):
            content.append(nome)
        elif attrs[nome] and isinstance(attrs[nome], str):
            content.append(f'{nome}="{attrs[nome]}"')
        else:
            pass
    sep = '\n'
    return f"""<{name} {' '.join(content)}>\n{sep.join([child.pack() if isinstance(child, Element) else child for child in children])}\n</{name}>"""

class Element:
    def __init__(self, __name, *args, **kw):
        self._name = __name
        self._attributes = kw
        double = kw.get('double')
        self._double = double if isinstance(double, bool) else True
        if self._double:
            self._attributes['double'] = None
        self._class_list = _class()
        self._children = list(args)
    
    def editAttribute(self, a, b):
        self._attributes[a] = b

    def editAttributes(self, **a):
        for b in a:
            self._attributes[b] = a[b]
    
    def __repr__(self):
        return f"Element({self._name})"

    def pack(self):
        if self._double:
            base = _base2
        else:
            base = _base1
        classes = ' '.join(self._class_list.list)
        if classes:
            self._attributes['class'] = classes
        return base(self._name, self._attributes, self._children)
    
    @property
    def element_name(self):
        return self._name
    
    @property
    def class_list(self):
        return self._class_list
    
    @property
    def attributes(self):
        return self._attributes
    
    @property
    def children(self):
        return self._children
    
    @children.setter
    def children(self, value):
        for nome in value:
            if isinstance(nome, Element):
                pass
            elif isinstance(nome, str):
                pass
            else:
                raise ElementError(f'value: {value} is not a list with only Elements or Strings')
        self._children = value
