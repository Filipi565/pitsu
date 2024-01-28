import typing as t

_VT = t.TypeVar("_VT")
_KT = t.TypeVar("_KT")

class Attributes(t.MutableMapping[_KT, _VT]):
    def __init__(self, *args: tuple[_KT, _VT], **kwargs: _VT):
        self.__value: dict[_KT, _VT] = dict()
        for item in args:
            self.__value[item[0]] = item[1]
        self.__value.update(kwargs)
    
    def __getitem__(self, value: _KT):
        return self.__value[value]
    
    def __setitem__(self, key: _KT, value: _VT):
        self.__value.__setitem__(key, value)
    
    def __len__(self):
        return len(self.__value)
    
    def __delitem__(self, key: _KT):
        self.__value.__delitem__(key)
    
    def __iter__(self):
        return iter(self.__value)

    def items(self) -> t.Iterator[tuple[_KT, _VT]]:
        for chave in self.__value:
            yield (chave, self[chave])
    
    def copy(self):
        return type(self)(**self.__value)