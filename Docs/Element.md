# Element Class

The Element Class has 3 parameters: element_name, children and attributes

example:

```python
element = Element("div", h1("Element Class"), class_="Element Class")
```

# HtmlElement Class
only use as html

HtmlElement has only 2 parameters: children and attributes

example:
```python
# the HtmlElement is not on default init file
from pitsu.element.html_element import HtmlElement

page = HtmlElement(body(...))
```
