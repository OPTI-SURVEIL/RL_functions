import numpy as np
import pandas as pd

FClib2 = pd.read_csv('FClib2.csv')
FC_dict = {}
for i in np.arange(FClib2.shape[0]):
    FC_dict[FClib2['ind'][i]] = FClib2['values'][i]

def str_to_FC(input):
    a = list(input)
    result_list = [FC_dict[i] if i in FC_dict else i for i in a]
    return ''.join(result_list)

def list_to_FC(input):
    return [str_to_FC(i) for i in input]
