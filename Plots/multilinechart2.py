import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

#Sort data
df = df.groupby(['month']).agg({'actual_max_temp' : 'max', 'actual_min_temp' : 'max', 'actual_mean_temp' : 'max'}).reset_index()

# Preparing data
trace1 = go.Scatter(x=df['month'], y=df['actual_max_temp'], mode='lines', name='Actual Max Temp')
trace2 = go.Scatter(x=df['month'], y=df['actual_min_temp'], mode='lines', name='Actual Min Temp')
trace3 = go.Scatter(x=df['month'], y=df['actual_mean_temp'], mode='lines', name='Actual Mean Temp')
data = [trace1,trace2,trace3]


# Preparing layout
layout = go.Layout(title='Temperatures 2014-2015', xaxis_title="Month",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart2.html')
