"""
Stock Analysis
"""
__version__ = "0.1.1"
__author__ = 'Ted Hong'
__credits__ = 'Beyondbond Risk Lab'
__name__ = 'stockan'
from .stockan_wrap import *
__all__=[x for x in globals() if '__' not in x]
