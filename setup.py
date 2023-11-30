from distutils.core import setup
import os

HERE = os.path.dirname(__file__)

with open(os.path.join(HERE, 'README.md')) as f:
    DESCRIPTION = f.read()

with open(os.path.join(HERE, 'LICENSE')) as f:
    LICENSE = f.read()

setup(
    name='pitsu',
    version='1.0.6',
    packages=['pitsu', 'pitsu/element'],
    author='Filipi565',
    description='a python module to create html pages with python code',
    long_description_content_type='text/markdown',
    long_description=DESCRIPTION,
    url='https://github.com/Filipi565/pitsu',
    license=LICENSE,
    requires=[
        
    ]
)
