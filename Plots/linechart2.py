import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

#Sort data
df = df.groupby(['month']).agg({'actual_max_temp' : 'max'}).reset_index()

# Preparing data
data = [go.Scatter(x=df['month'], y=df['actual_max_temp'], mode='lines', name='Actual Max Temp')]

# Preparing layout
layout = go.Layout(title='Actual Max Temperature of Each Month', xaxis_title="Month",
                   yaxis_title="Actual Max Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart2.html')
