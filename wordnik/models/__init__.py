#!/usr/bin/env python
"""Add all of the modules in the current directory to __all__"""

import os

__all__ = [
    module[:-3]
    for module in os.listdir(os.path.dirname(__file__))
    if module != '__init__.py' and module[-3:] == '.py'
]

