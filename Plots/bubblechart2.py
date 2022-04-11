import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')
# Removing empty spaces from column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by Country Column
new_df = df.groupby(['month']).agg(
    {'average_min_temp': 'sum', 'average_max_temp': 'sum'}).reset_index()

# Preparing data
data = [
    go.Scatter(x=new_df['average_min_temp'],
               y=new_df['average_max_temp'],
               text=new_df['month'],
               mode='markers',
               marker=dict(size=new_df['average_max_temp'] / 30, color=new_df['average_max_temp'] / 30, showscale=True))
]

# Preparing layout
layout = go.Layout(title='Weather 2014-2015', xaxis_title="Average Min Temp",
                   yaxis_title="Average Max temp", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart2.html')
