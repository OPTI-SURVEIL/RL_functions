def missing_value_indices(df): #df is a pandas dataframe with columns such as first name, last name, DOB, sex, etc.
    index_dict = {}
    columns = df.columns #names of each of the columns in the dataframe i.e. 'sex'
    for i in columns:
        index_dict[i] = list(df[i][df[i].isna()].index)
    return index_dict
