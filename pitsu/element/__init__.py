from . import _base

Child = _base.Element | str
Children = list[Child]

Element = _base.Element

def _double_base(name):
    def a(*children:Child, **attributes:str):
        return _base.Element(name, *children, **{'double': True, **attributes})
    return a

def _not_double_base(name):
    def a(**attributes:str):
        return _base.Element(name, **{'double': False, **attributes})
    return a

html = _double_base('html')
head = _double_base('head')
body = _double_base('body')
anchor = _double_base('a')
audio = _double_base('audio')
video = _double_base('video')
image = img = _not_double_base('img')
button = btn = _double_base('button')
div = _double_base('div')
form = _double_base('form')
def text(name:str, *children:Child, **attributes:str):
    return _base.Element(name, *children, **{'double': True, **attributes})
iframe = _double_base('iframe')
inp = _not_double_base('input')
label = _not_double_base('label')
link = _not_double_base('link')
meta = _not_double_base('meta')
script = _double_base('script')
source = _not_double_base('source')
textarea = _double_base('textarea')
title = _double_base('title')
br = lambda: '<br>'
