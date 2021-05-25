import pandas as pd

# visualization imports
import plotly
import plotly.express as px


pulsars = pd.read_csv('HTRU_2.csv')
print(pulsars.dtypes) # so these are already processed into floats and ints

# give columns a name
pulsars.columns =["mean of ip", "standard deviation of ip","excess kurtosis of ip","skewness of ip","mean of curve","standard deviation of curve","excess kurtosis of curve","skewness of curve","class"]
print(pulsars.head())

print(pulsars.shape)
pulsars.drop_duplicates()
print(pulsars.shape) # no duplicates data set already kinda clean ngl

# see if any of the tples has missing data
print(pulsars.isnull().sum()) # literally has no missing data


# making a pie chart for the number of tuples that are a pulsar
fig = pie_chart = px.pie(
    data_frame=pulsars,
    names="class",
    title='percentage of data that are pulsars'
)
fig.show()

# want to separate into two different dataframes one with pulsar one no pulsar then graph some stuffs
pulsar = pulsars[pulsars["class"] == 1]
not_pulsar=pulsars[pulsars["class"]==0]



fig = px.scatter(pulsar, x="standard deviation of ip", y="standard deviation of curve", title="standard deviation chart pulsars")
# fig.show()

fig = px.scatter(pulsars, x="standard deviation of ip", y="standard deviation of curve", color="class", title="standard deviation chart")
fig.show()

fig = px.scatter(pulsars, x="mean of ip", y="mean of curve", color="class", title="mean chart")
fig.show()

fig = px.scatter(not_pulsar, x="standard deviation of ip", y="standard deviation of curve", title="standard deviation chart not_pulsars")
# fig.show()

fig = px.scatter(pulsars, x="excess kurtosis of ip", y="excess kurtosis of curve", color="class", title="kurtosis chart")
fig.show()

fig = px.scatter(pulsars, x="skewness of ip", y="skewness of curve", color="class", title="skewness")
fig.show()

fig = px.scatter_matrix(pulsars, dimensions=['mean of ip', 'standard deviation of ip', 'excess kurtosis of ip', 'skewness of ip'], color='class', title='matrix scatter plot')
fig.show()