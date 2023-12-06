from distutils.core import setup
import os

HERE = os.path.dirname(__file__)

with open(os.path.join(HERE, 'README.md')) as f:
    DESCRIPTION = f.read()

with open(os.path.join(HERE, 'LICENSE')) as f:
    LICENSE = f.read()

URLS = {
    "Source": "https://github.com/Filipi565/pitsu"
}

PACKAGES = [
    'pitsu',
    'pitsu/element'
]

REQUIRES = [

]

setup(
    name='pitsu',
    version='1.0.6',
    author='Filipi565',
    description='a python module to create html pages with python code',
    long_description_content_type='text/markdown',
    long_description=DESCRIPTION,
    license=LICENSE,
    packages=PACKAGES,
    requires=REQUIRES,
    project_urls=URLS
)
