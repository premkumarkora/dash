# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 08:11:12 2022

@author: KORA
"""
import plotly.io as io
io.renderers.default='browser'


import plotly.express as px
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()