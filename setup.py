try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pitsu',
    version='1.0',
    packages=['pitsu', 'pitsu/element'],
    data_files=[
        ('pitsu', ['pitsu/element/_base.pyi'])
    ],
    author='Filipi565',
    description='a python module to create html pages with python code',
)