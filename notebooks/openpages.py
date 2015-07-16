#!/usr/bin/python3
"""Open demo pages for the notebook talk"""

import subprocess
import time
import webbrowser

subprocess.Popen(['jupyter', 'notebook'])

time.sleep(1)  # Give the notebook server a moment to start & open a page

urls = [
    'http://localhost:8888/notebooks/spectrogram.ipynb',
    'http://localhost:8888/edit/spectrogram.ipynb',
    'http://nbviewer.ipython.org/url/norvig.com/ipython/Gesture%20Typing.ipynb',
    'http://nbconvert.readthedocs.org/en/latest/customizing.html',
]

for u in urls:
    webbrowser.open(u)
