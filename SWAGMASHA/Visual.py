import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd

x = np.arange(0, 5, 0.1) #создание массива
def f(x): #функция
    return x**2 #возвести в квадрат

# fig = px.scatter(x=x, y=f(x)) #создание графика
# fig.show() #показать график

fig = go.Figure() # создание пустого графика
fig.add_trace(go.Scatter(x=x, y=f(x),  name='f(x)=x<sup>2</sup>')) #добавление графика (имя через тег <sup></sup>)
fig.add_trace(go.Scatter(x=x, y=x, name='$$g(x)=x$$')) #добавление графика (имя $$ ... $$)
fig.update_layout(legend_orientation="h", #перенести легенду вниз (h - горизонтальная, v - вертикальная)
                  legend=dict(x=.5, xanchor="center"), #выравнять легенду по центру
                  title='Графики функций', #заголовок
                  xaxis_title='x', #название оси абсцисс
                  yaxis_title='y', #название оси ординат
                  margin=dict(l=0, r=0, t=0, b=0)) #отступы вокруг графика
fig.show() #показать график

