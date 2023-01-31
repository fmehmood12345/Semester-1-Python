import pandas as pd


class client_class:
    # constructor
    def __init__(self, Title, Firstname, Lastname, Pronouns,Date_of_Birth, Occupation, Account_Balance,
                 Overdraft_Limit):
        # instance variables
        try:
            assert isinstance(Firstname, str)
            self.first_name = Firstname

            assert isinstance(Lastname, str)
            self.last_name = Lastname

            assert isinstance(Title, str)
            self.title = Title

            assert isinstance(Pronouns, str)
            self.preferred_pronouns = Pronouns

            assert isinstance(Date_of_Birth, str)
            self.date_of_birth = Date_of_Birth

            assert isinstance(Occupation, str)
            self.occupation = Occupation

            assert isinstance(Account_Balance, int)
            self.account_balance = Account_Balance

            assert isinstance(Overdraft_Limit, int)
            self.overdraft_limit = Overdraft_Limit
        except BaseException as err:
            print(f"ERROR: There was an error while initiating client_class object {type(err)}.")

    '''Client class constructor with all the class attributes needed for each client. Assert has been used to make sure 
    each class attribut has a specific type and if that requirement isn't met, then an error message is outputted.'''

    def __str__(self):
        try:
            return (
                f'Title: {self.title}\n'
                f'Firstname: {self.first_name}\n'
                f'Lastname: {self.last_name}\n'
                f'Preferred Pronoun: {self.preferred_pronouns}\n'
                f'Date of Birth: {self.date_of_birth}\n'
                f'Occupation: {self.occupation}\n'
                f'Account Balance: {self.account_balance}\n'
                f'Overdraft Limit: {self.overdraft_limit}')
        except BaseException as err:
            print(f"ERROR: There was an error while turning the client_class object into a string {type(err)}.")

    '''An str method which presents the client data as a string. '''

    def adding_in_account_balance(self, add_balance):
        try:
            assert isinstance(add_balance, int)
            new_balance = int(add_balance) + int(self.account_balance)
            self.account_balance = new_balance
        except BaseException as err:
            print(f"ERROR: Could not deposit money into account balance: {type(err)}.")

    '''This method deposits money into the clients account balance. Assert allows me to make add_balance an integer value.
    If this requirement isn't met, then an error message is printed.'''

    def removing_in_account_balance(self, removing_balance):
        try:
            assert isinstance(removing_balance, int)
            if removing_balance > (self.account_balance + self.overdraft_limit):
                self.account_balance = (self.account_balance + self.overdraft_limit) - (removing_balance + 5)
            else:
                self.account_balance = (self.account_balance - removing_balance)
        except BaseException as err:
            print(f"ERROR: Could not withdraw from account balance: {type(err)}.")

    '''This method withdraws money from the account balance and if the overdraft limit is surpassed, then an additional 
    £5 is charged as well as the amount the client went over the overdraft limit. Assert is used here to make 
    removing_balance an integer and if this requirement isn't met then an error message is printed.'''

    def changing_title(self, new_title):
        try:
            assert isinstance(new_title, str)
            self.title = new_title
        except BaseException as err:
            print(f"ERROR: Could not change title: {type(err)}.")

    '''Method changes client title. Assert makes new_title a string and an error message is printed if this 
    requirement is not met.'''

    def changing_first_name(self, new_first_name):
        try:
            assert isinstance(new_first_name, str)
            self.first_name = new_first_name
        except BaseException as err:
            print(f"ERROR: Could not change firstname: {type(err)}.")

    '''Method changes the first name.Assert makes new_first_name a string and an error message is printed if this 
    requirement is not met.'''

    def changing_last_name(self, new_last_name):
        try:
            assert isinstance(new_last_name, str)
            self.last_name = new_last_name
        except BaseException as err:
            print(f"ERROR: Could not change lastname: {type(err)}.")

    '''Method changes the last name.Assert makes new_last_name a string and an error message is printed if this 
    requirement is not met.'''

    def changing_preferred_pronoun(self, new_preferred_pronoun):
        try:
            assert isinstance(new_preferred_pronoun, str)
            self.preferred_pronouns = new_preferred_pronoun
        except BaseException as err:
            print(f"ERROR: Could not change preferred pronoun: {type(err)}.")

    '''Method changes the pronouns.Assert makes new_preferred_pronoun a string and an error message is printed if this 
    requirement is not met.'''

    def changing_occupation(self, new_occupation):
        try:
            assert isinstance(new_occupation, str)
            self.occupation = new_occupation
        except BaseException as err:
            print(f"ERROR: Could not change occupation: {type(err)}.")

    '''Method changes the occupation.Assert makes new_occupation a string and an error message is printed if this 
    requirement is not met.'''

    def return_client_dict(self):
        try:
            return {
                "Title": [f"{self.title}"],
                "Firstname": [f"{self.first_name}"],
                "Lastname": [f"{self.last_name}"],
                "Pronouns": [f"{self.preferred_pronouns}"],
                "Date of Birth": [f"{self.date_of_birth}"],
                "Occupation": [f"{self.occupation}"],
                "Account Balance": [self.account_balance],
                "Overdraft Limit": [self.overdraft_limit]
            }
        except BaseException as err:
            print(f"ERROR: Could not return client as a dictionary:{type(err)}.")

    '''This method returns a client as a dictionary. So if a client was inputted as a dataframe into the class, it will
    be returned as a dictionary when this function is called using the client class object.'''
