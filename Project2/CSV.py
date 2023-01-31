import csv
import datetime
import pandas
import pandas as pd
from constants import *


class csv:
    def dataframe_of_csv_file(self):
        try:
            dataframe = pd.read_csv(CSV_FILE_PATH, index_col=None)
            return dataframe
        except BaseException as err:
            print(f"ERROR: There was an error while retrieving the dataframe of the csv file : {err}.")
    '''The method takes the client details and turns it into a dataframe.'''
    def refresh_csv_file(self, new_df):
        try:
            new_df.to_csv(CSV_FILE_PATH, index=False)
        except BaseException as err:
            print(f"ERROR: Could not refresh CSV file: {err}.")
    '''This method takes in the updated dataframe once the changes have been made and refreshes the CSV file. '''
