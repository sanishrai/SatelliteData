These are the pickled neral networks I have done so far. 

You directly load my specific networks into your code. This way you don't even have to trian the network yourselfYou can just use these pickles to predict datasets you've found.

To load the pickle into your program use the following code:
with open('pickle_name.pkl', 'rb') as f:
    variable_name = pickle.load(f)
    
If you do use pickles, make sure you use 'pip install pickles' in the command line and in your python program use import pickle
