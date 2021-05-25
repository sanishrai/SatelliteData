# K-means clustering

import pandas as pd
import plotly.express as px
from sklearn.neural_network import MLPClassifier
pulsars = pd.read_csv('HTRU_2.csv')

# give columns a name
pulsars.columns =["mean of ip", "standard deviation of ip","excess kurtosis of ip","skewness of ip","mean of curve","standard deviation of curve","excess kurtosis of curve","skewness of curve","class"]

# need to separate results from data points
pulsars_class = pulsars.copy()
pulsars_class.drop(["mean of ip", "standard deviation of ip","excess kurtosis of ip","skewness of ip","mean of curve","standard deviation of curve","excess kurtosis of curve","skewness of curve"], axis = 1, inplace=True)
pulsars.drop("class", axis = 1, inplace=True)
# there are 17,897 rows in this dataframe.
# going to use 15,000 to train, 1,449 to test and 1,448 to validate
training_set = pulsars[:15_000].copy() # remember noninclusive last element
training_set_ans = pulsars_class[:15_000].copy()
testing_set = pulsars[15_000:16_449].copy()
testing_set_ans = pulsars_class[15_000:16_449].copy()
validation_set = pulsars[16_449:17_898].copy()
validation_set_ans = pulsars_class[16_449:17_898].copy()

# creating neural network
mlp = MLPClassifier(hidden_layer_sizes = (10,10,10), max_iter=1000)
mlp.fit(training_set, training_set_ans.values.ravel())

testing_set_predict = mlp.predict(testing_set)
testing_set["predict"] = testing_set_predict
testing_set["class"] = testing_set_ans

validation_set_predict = mlp.predict(validation_set)
validation_set['predict'] = validation_set_predict
validation_set["class"] = validation_set_ans


overlap = testing_set[testing_set["class"] == testing_set["predict"]]
print("Testing overlap (out of 1449): " + str(overlap.shape))
validation_overlap = validation_set[validation_set['predict'] == validation_set['class']]
print("Validation overlap (out of 1448):  " + str(validation_overlap.shape))