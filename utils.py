# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:07:43 2022

@author: Batman
"""

import settings


def height_prct(percentage):
    return settings.HEIGHT * percentage / 100


def width_prct(percentage):
    return settings.WIDTH * percentage / 100
