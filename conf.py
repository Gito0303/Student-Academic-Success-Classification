import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Student Academic Success Classification'
author = 'Gito0303'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

html_theme = 'alabaster'
