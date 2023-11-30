# pitsu
a python module to create html pages with python code

# how to use
```the register process it's blocked in pypi so i only can upload in test pypi and may be some uninstable```

instal pitsu:

```
pip3 install -i https://test.pypi.org/simple/ --upgrade pitsu
```

or 

```
pip install -i https://test.pypi.org/simple/ --upgrade pitsu
```

simple example:

```
from pitsu import *

<span style="color: rgb(255, 255, 60);">html</span>(
    <span>head</span>(
        <span style="color: rgb(255, 255, 60);">meta</span>(charset='UTF-8'),
        <span style="color: rgb(255, 255, 60);">title</span>('Example Login')
    ),
    <span style="color: rgb(255, 255, 60);">body</span>(
        <span style="color: rgb(255, 255, 60);">form</span>(
            <span style="color: rgb(255, 255, 60);">inp</span>( # inp = input element
                type='text',
                name='user',
                id='user',
                required=True
            ),
            <span style="color: rgb(255, 255, 60);">br</span>(),
            <span style="color: rgb(255, 255, 60);">inp</span>(
                type='password',
                name='pass',
                id='pass',
                required=True
            ),
            <span style="color: rgb(255, 255, 60);">br</span>(),
            <span style="color: rgb(255, 255, 60);">inp</span>(
                type='submit',
                value='Submit'
            ),
            action='/',
            method='get'
        )
    ),
    lang='en'
).<span style="color: rgb(255, 255, 60);">pack</span>()
```

output:
```
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
