# Exceptions

ElementError

ClassError

# Class

* Element(__name: name of the element, *child: the children of the element, **attributes: the attributes of the element): Base Element Class

method: editAttribute(a: the attribute that you want tho change, b: the value of the attribute)

method: editAttributes(**a: the attributes and the values that you want to edit)

method: pack(): render the element and return it as string

property: element_name: return the name of the element

property: class_list: return the class list of the element

property: attributes: return the attributes of the element

property: children: return the children of the element

* HtmlElement(*child: the children of the element, **attributes: the attributes of the element): Class for the html Element

* Class_List: Class to manager the class list of the elements

method: append or add: add a item to the class list

method: remove: remove a item to the class list

method: replace: replace the value of a item to the given value