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

# Mengatur folder sumber
source_suffix = '.rst'

# Menentukan path untuk file statis seperti CSS
html_static_path = ['_static']

# Menentukan folder dokumentasi
master_doc = 'index'

html_theme = 'sphinx_rtd_theme'

html_context = {
    'next_prev_buttons': False,  # Menonaktifkan tombol next/prev
}

# Mengatur kedalaman navigasi agar dapat menavigasi dengan daftar isi
html_theme_options = {
    'navigation_depth': 4,  # Menambah kedalaman navigasi di TOC
    'collapse_navigation': False,  # Menonaktifkan tombol collapse
    'sticky_navigation': False,  # Menonaktifkan sticky navigation
}

