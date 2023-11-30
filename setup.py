from setuptools import setup

DESCRIPTION = '''# how to use
```the register process it's blocked in pypi so i only can upload in test pypi and may be some uninstable```

instal pitsu:

```bash
pip3 install -i https://test.pypi.org/simple/ --upgrade pitsu
```

or 

```bash
pip install -i https://test.pypi.org/simple/ --upgrade pitsu
```

simple example:

```python
from pitsu import *

html(
    head(
        meta(charset='UTF-8'),
        title('Example Login')
    ),
    body(
        form(
            inp( # inp = input element
                type='text',
                name='user',
                id='user',
                required=True
            ),
            br(),
            inp(
                type='password',
                name='pass',
                id='pass',
                required=True
            ),
            br(),
            inp(
                type='submit',
                value='Submit'
            ),
            action='/',
            method='get'
        )
    ),
    lang='en'
).pack()
```

output:
```html
<html lang="en">
<head>
<meta charset="UTF-8">
<title>
Example Login
</title>
</head>
<body>
<form action="/" method="get">
<input type="text" name="user" id="user" required>
<br>
<input type="password" name="pass" id="pass" required>
<br>
<input type="submit" value="Submit">
</form>
</body>
</html>
```
'''

LICENSE = '''MIT License

Copyright (c) 2023 Filipi565

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

setup(
    name='pitsu',
    version='1.0.6',
    packages=['pitsu', 'pitsu/element'],
    author='Filipi565',
    description='a python module to create html pages with python code',
    long_description_content_type='text/markdown',
    long_description=DESCRIPTION,
    url='https://github.com/Filipi565/pitsu',
    license=LICENSE
)
