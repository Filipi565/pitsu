class ElementError(Exception):
    """Error by Element class"""
class ClassError(Exception):
    """Error by Class_List class"""

from .element import *

version = '1.1.2'
__version__ = version
