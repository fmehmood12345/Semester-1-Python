from clients import *
from CSV import *
import pandas as pd
from constants import *


class Banking_Application:

    def __init__(self):
        try:
            self.csv_class_obj = csv()
        except BaseException as err:
            print(f"ERROR: Could not initialise csv class object:{type(err)}.")

    '''Made a constructor which is an object of the CSV class so that I can assess the functions in that class. '''

    def __fetch_csv_dataframe(self):
        try:
            dataframe = self.csv_class_obj.dataframe_of_csv_file()
            return dataframe
        except BaseException as err:
            print(f"ERROR: Could not fetch csv dataframe:{type(err)}.")

    '''Private method which uses an object of the CSV class to call the function "dataframe_of_csv_file()" to get the 
    CSV file as dataframe.'''

    def print_current_CSV_file(self):
        try:
            print(self.__fetch_csv_dataframe().to_string())
        except BaseException as err:
            print(f"ERROR: Could not print CSV dataframe:{type(err)}.")

    '''Method to print out the dataframe by running the private method.'''

    def __return_client_df_as_dict(self, **dataframe_input):
        try:
            all_clients = []
            client_dict = {}
            for each_row in range(0, list(dataframe_input["Title"].values()).__len__()):
                client_dict = {}
                for key in dataframe_input:
                    client_dict[key] = list(dataframe_input[key].values())[each_row]
                all_clients.append(client_dict)
            return all_clients
        except BaseException as err:
            print(f"ERROR: Could not return client dataframe as a dictionary:{type(err)}.")

    '''Private method to return a client which is a dataframe as a dictionary. This is so that clients are presented 
    in a cleaner way as opposed to a dictionary. In this method, the dataframe of the client is inputted as an 
    attribute and returns the client in a cleaner form. '''

    def retrieving_a_client(self, first_name, last_name, date_of_birth):
        try:
            assert isinstance(first_name, str)
            assert isinstance(last_name, str)
            assert isinstance(date_of_birth, str)
            dataframe = self.__fetch_csv_dataframe()
            df = dataframe[
                (dataframe.Firstname == first_name) &
                (dataframe.Lastname == last_name) &
                (dataframe["Date_of_Birth"] == date_of_birth)
                ]
            client_obj = client_class(**self.__return_client_df_as_dict(**(df.to_dict()))[0])
            return client_obj
        except BaseException as err:
            print(f"ERROR: Could not retrieve a client:{type(err)}.")

    '''This method retrieves a client from the CSV dataframe by calling the private function. Then the firstname, 
    lastname and date of birth called into the function is compared with the firstname, lastname and date of birth in 
    the CSV dataframe to find the respective client. Once they have been found, they are put in a dataframe. Then this
    client dataframe is called into a function which returns a client as a dictionary. Finally this dictionary is 
    returned.Assert makes new_first_name, last_name and date_of_birth a string and an error message is printed if this 
    requirement is not met.'''

    def searching_for_accounts_with_negative_balance(self):
        try:
            dataframe = self.__fetch_csv_dataframe()
            df = dataframe[dataframe["Account_Balance"] < 0]
            if df.shape[0] == 0:
                return None
            else:
                return self.__return_client_df_as_dict(**(df.to_dict()))
        except BaseException as err:
            print(f"ERROR: Could not search for clients with negative balance:{type(err)}.")

    '''This method get returns all clients with negative balance as a dataframe as there are multiple clients 
    that could be returned. It fetches the CSV dataframe and gets all clients with negative account balance. '''

    def searching_by_firstname(self, first_name):
        try:
            assert isinstance(first_name, str)
            dataframe = self.__fetch_csv_dataframe()
            df = dataframe[(dataframe["Firstname"] == first_name)]
            if df.shape[0] == 0:
                return None
            else:
                return self.__return_client_df_as_dict(**(df.to_dict()))
        except BaseException as err:
            print(f"ERROR: Could not search for clients with firstname", first_name, ":", {type(err)})

    ''' This method compares the firstname passed in the parameter with all the available first names and returns all
    details of the clients as a dataframe.'''

    def searching_by_lastname(self, last_name):
        try:
            assert isinstance(last_name, str)
            dataframe = self.__fetch_csv_dataframe()
            df = dataframe[(dataframe["Lastname"] == last_name)]
            if df.shape[0] == 0:
                return None
            else:
                return self.__return_client_df_as_dict(**(df.to_dict()))
        except BaseException as err:
            print(f"ERROR: Could not search for clients with lastname", last_name, ":", {type(err)})

    '''This method takes the CSV file as a dataframe by calling the fetch_csv_dataframe method from the CSV.py file. 
     Then the last name passed into the parameter is compared with all the lastnames in the lastname column in the 
     dataframe and the respective client is returned as a dataframe.'''

    def searching_by_date_of_birth(self, date_of_birth):
        try:
            assert isinstance(date_of_birth, str)
            dataframe = self.__fetch_csv_dataframe()
            df = dataframe[(dataframe["Date_of_Birth"] == date_of_birth)]
            if df.shape[0] == 0:
                return None
            else:
                return self.__return_client_df_as_dict(**(df.to_dict()))
        except BaseException as err:
            print(f"ERROR: Could not search for clients with date of birth", date_of_birth, ":", {type(err)})

    ''' This method searched for all clients with the same date of birth and prints at out as a dataframe.'''

    def deleting_a_client(self, first_name, last_name, date_of_birth):
        try:
            assert isinstance(first_name, str)
            assert isinstance(last_name, str)
            assert isinstance(date_of_birth, str)
            dataframe = self.__fetch_csv_dataframe()
            dataframe.drop(dataframe[(dataframe["Firstname"] == first_name) & (dataframe["Lastname"] == last_name) & (
                        dataframe["Date_of_Birth"] == date_of_birth)].index, inplace=True)
            self.csv_class_obj.refresh_csv_file(dataframe)
        except BaseException as err:
            print(f"ERROR: Could not delete client:", {type(err)})

    '''This method deletes a client by comparing first names, last names and date of birth with clients and removes the 
     a client who's details match with the passed parameters.'''

    def adding_a_client(self, client_dict):
        try:
            dataframe = self.__fetch_csv_dataframe()
            client_dataframe = pd.DataFrame(client_dict)
            new_dataframe = pd.concat([dataframe, client_dataframe], ignore_index=True)
            self.csv_class_obj.refresh_csv_file(new_dataframe)
        except BaseException as err:
            print(f"ERROR: Failed to add a new client: {type(err)}")

    ''' This method adds a client dataframe into the CSV file.'''

    def changing_overdraft_limits(self, first_name, last_name, date_of_birth, new_overdraft_limit):
        try:
            assert isinstance(first_name, str)
            assert isinstance(last_name, str)
            assert isinstance(date_of_birth, str)
            assert isinstance(new_overdraft_limit, int)
            dataframe = self.__fetch_csv_dataframe()
            for index, row in dataframe.iterrows():
                if row['Firstname'] == first_name and row['Lastname'] == last_name and row['Date_of_Birth'] == date_of_birth:
                    dataframe.at[index, 'Overdraft_Limit'] = new_overdraft_limit
                    self.csv_class_obj.refresh_csv_file(dataframe)
        except BaseException as err:
            print(f"ERROR: Failed to change overdraft limits: {type(err)}")

    '''This method changes a specific clients overdraft limits. A specific client is chosen through comparing the given 
     attributes with the existing clients.'''
