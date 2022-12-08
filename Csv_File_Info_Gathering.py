import pandas as pd



class CSV_READER:


###SIMPLE DATA GATHERING####

    def __init__(self, dataframe ):

        self.dataframe = dataframe


    def give_dtypes(self):

        return self.dataframe.dtypes

    def give_dfinfo(self):

        return self.dataframe.info()

    def give_shape(self):

        return self.dataframe.shape

    def give_describe(self):

        return self.dataframe.describe()

    def give_in_null(self):

        return self.dataframe.isnull().sum()
        
        
###SIMPLE DATA GATHERING####
