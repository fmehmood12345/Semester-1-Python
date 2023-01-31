import pandas as pd
from banking_application import Banking_Application
from clients import client_class
from testing_payloads import *

client_object = client_class(**client)
client1_object = client_class(**client1)
client2_object = client_class(**client2)
client3_object = client_class(**client3)
client4_object = client_class(**client4)
BA_Obj = Banking_Application()


# client_object.changing_title("Mrs")
# client_object.changing_first_name("Susan")
# client_object.changing_last_name("Blunt")
# client_object.changing_preferred_pronoun("she/her")
# client_object.changing_occupation("Designer")
# client_object.removing_in_account_balance(100)
# client_object.adding_in_account_balance(200)
# print(client_object.return_client_dict())

'''The methods called below have not had unit testing done, remove the "#" and run to see it work:'''
# BA_Obj.deleting_a_client("Alice","Liddyard","8/09/1978")
'''Method to delete a client'''
# BA_Obj.changing_overdraft_limits("Skyler","Harrinson","2/07/1960",1544)
'''Method to change overdraft limits.'''
# BA_Obj.adding_a_client(client1_object.return_client_dict())
# BA_Obj.adding_a_client(client2_object.return_client_dict())
# BA_Obj.adding_a_client(client3_object.return_client_dict())
# BA_Obj.adding_a_client(client4_object.return_client_dict())
'''Methods to add a client. I have given 4 different clients with different information so you can either test it one 
by one or completely remove the comments and run all 4.'''



# print(BA_Obj.print_current_CSV_file())
# print(BA_Obj.retrieving_a_client("Gerald", "Smith", "15/12/1990"))
# print(BA_Obj.searching_by_firstname("Wilma"))
# print(BA_Obj.searching_by_lastname("Wilshin"))
# print(BA_Obj.searching_by_date_of_birth("10/04/1979"))
# print(BA_Obj.searching_for_accounts_with_negative_balance())
'''The print statements above have had unit testing done on them.'''
