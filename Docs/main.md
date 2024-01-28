# Instalation

to install pitsu use:

```bash
pip install pitsu
```

# Creating as html page

```python
#import the module
from pitsu import *

#create a Hello World page
html(
    head(
        meta(charset="UTF-8"),
        title("My Html Page")
    ),
    body(
        h1("Hello World")
    ),
    lang="en"
)
```

<a href="/Docs/Functions.md">Functions</a>

<a href="/Docs/Element.md">Element</a>