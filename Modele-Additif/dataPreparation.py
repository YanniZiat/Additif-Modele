import pandas
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

class DataPreparation:
	def __init__(self, dataset_df):
        
		self.dataset_df = pandas.read_csv('vente_maillots_de_bain.csv')
		self.prepare_data()



	def prepare_data(self):

		number_of_rows = len(self.dataset_df)
		self.dataset_df["time"] = numpy.arange(1, number_of_rows+1, 1)
		self.dataset_df["Years"] = pandas.to_datetime(self.dataset_df["Years"])
		self.dataset_df["month_name"] = self.dataset_df["Years"].dt.strftime('%B')
		month_name_column = self.dataset_df['month_name']
		self.dataset_df = pandas.get_dummies(self.dataset_df, columns=["month_name"],prefix = '')
		self.dataset_df.insert(loc = 2, column =  'month_name', value = month_name_column)

		dataset_train_df = self.dataset_df.iloc[ : int(number_of_rows*0.75)]
		dataset_test_df = self.dataset_df.iloc[int(number_of_rows*0.75): ]

		self.x_train = dataset_train_df.iloc[:, 3:].values
		self.y_train = dataset_train_df[['Sales']].values

		self.x_test = dataset_test_df.iloc[:, 3:].values
		self.y_test = dataset_test_df[['Sales']].values
        
		self.years_train = self.dataset_df["Years"].iloc[: int(number_of_rows*0.75)]
		self.years_test = self.dataset_df["Years"].iloc[int(number_of_rows*0.75): ]