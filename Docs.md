# Element class

create a element for your element page

Exaple:

```python
from pitsu import *

document = html(
    Element("div"), #creates a div element
    lang="en",
).pack()
```

How to edit the class of the element?

There is 2 ways:

```python
from pitsu import *

method1 = div(
    id="method1"
)

method1.class_list.add("Class1")
method1.class_list.append("Class2") # append = add

method2 = div(
    id="method2",
    **{"class": "Class1 Class2"}
)

document = html(
    method1,
    method2,
    lang="en",
).pack()
```

warning: do not use both methods or your code will not work

# Class_List class

the manager of the class list for the element

you can get the class list of your element using:

```python
myElement = div()
myElement.class_list
```