# Plotly works like matplotlib, but it is more interactive

import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.offline as pyo
import plotly.graph_objs as go
pyo.init_notebook_mode()


#define the function to make the figure
def figure():
    fig = go.Figure()
    return fig 

#define the function to plot the figure
#you can select input name, color, mode, type, showlegend or not

def plot(fig, x, y, name = None, color = None, mode = 'lines'):
    fig.add_trace(go.Scatter(x=x, y=y, name=name, line_color=color, mode=mode))
 

#define the function to dot plot the figure
def dot_plot(fig, x, y, name = None, color = None, mode = 'markers', size = 10):
    fig.add_trace(go.Scatter(x=x, y=y, name=name, line_color=color, mode=mode , marker=dict(size=size)))
 
    
# define the function to show the figure
def show(fig):
    fig.show()

# define the function to save the figure
def save(fig, name):
    fig.write_html(name)

# define the function to make the figure with subplots
def subplots(row, col):
    fig = make_subplots(rows=row, cols=col)
    return fig

# define the function to plot the figure with subplots
def plot_subplots(fig, x, y, row, col, name = None, color = None, mode = 'lines'):
    fig.add_trace(go.Scatter(x=x, y=y, name=name, line_color=color, mode=mode), row=row, col=col)

#define the funtion to dot plot the figure with subplots
def dot_plot_subplots(fig, x, y, row, col, name = None, color = None, mode = 'markers', size = 10):
    fig.add_trace(go.Scatter(x=x, y=y, name=name, line_color=color, mode=mode, marker=dict(size=size)), row=row, col=col)


"""plot example:
import AI_plot as plt
 
x = [1,2,3,4,5]
y = [1,2,3,4,5]

fig = plt.figure()
plt.plot(fig, x, y, name = 'line')
plt.dot_plot(fig, x, y, name = 'dot', color = 'red')

plt.show(fig)
"""

"""subplot example:
fig2 = plt.subplots(2,1)
plt.plot_subplots(fig2, x, y, 1, 1, name = 'line')
plt.plot_subplots(fig2, x, y, 2, 1, name = 'dot', color = 'red')

plt.show(fig2)

"""   