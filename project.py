"""
This script is for image analysis
"""
from readlif.reader import LifFile
import numpy as np
new = LifFile('/Users/iisturizpetitj/Desktop/20211223_P1_MCF7 #1.lif')
new.get_image(0)
