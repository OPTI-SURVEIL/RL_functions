pylib2 = pd.read_csv('pylib2.csv')
pylib_dict = {}
for i in np.arange(pylib2.shape[0]):
    if ',' in pylib2['values'][i]:
        pylib_dict[pylib2['ind'][i]] = '[' + pylib2['values'][i] + ']'
    else:
        pylib_dict[pylib2['ind'][i]] = pylib2['values'][i]

def str_to_py(input):
    a = list(input)
    result_list = [pylib_dict[i] if i in pylib_dict else i for i in a]
    return ''.join(result_list)

def list_to_py(input):
    return [str_to_py(i) for i in input]
