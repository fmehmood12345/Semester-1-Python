from banking_application import *
from clients import client_class
import testing_payloads
import unittest
class test_client_class(unittest.TestCase):

    def test_adding_in_account_balance(self):
        client_obj = client_class(**testing_payloads.client_details)
        client_obj.adding_in_account_balance(100)
        client_dict = client_obj.return_client_dict()
        self.assertEqual(200, client_dict['Account Balance'][0])

#removing 150 to show what happens when the overdraft limit is exceeded.
    def test_removing_in_account_balance(self):
        client_obj = client_class(**testing_payloads.client_details)
        client_obj.removing_in_account_balance(150)
        client_dict = client_obj.return_client_dict()
        self.assertEqual(-45, client_dict['Account Balance'][0])

    def test_changing_title(self):
        client_obj = client_class(**testing_payloads.client_details)
        client_obj.changing_title("Mrs")
        client_dict = client_obj.return_client_dict()
        self.assertEqual("Mrs", client_dict['Title'][0])


    def test_changing_first_name(self):
        client_obj = client_class(**testing_payloads.client_details)
        client_obj.changing_first_name("Harry")
        client_dict = client_obj.return_client_dict()
        self.assertEqual("Harry", client_dict['Firstname'][0])

    def test_changing_last_name(self):
        client_obj = client_class(**testing_payloads.client_details)
        client_obj.changing_last_name("Lowe")
        client_dict = client_obj.return_client_dict()
        self.assertEqual("Lowe", client_dict['Lastname'][0])

    def test_changing_preferred_pronoun(self):
        client_obj = client_class(**testing_payloads.client_details)
        client_obj.changing_preferred_pronoun("she/her")
        client_dict = client_obj.return_client_dict()
        self.assertEqual("she/her", client_dict['Pronouns'][0])

    def test_changing_occupation(self):
        client_obj = client_class(**testing_payloads.client_details)
        client_obj.changing_occupation("Singer")
        client_dict = client_obj.return_client_dict()
        self.assertEqual("Singer", client_dict['Occupation'][0])

class test_banking_app(unittest.TestCase):
    def test_accounts_with_negative_balance(self):
        banking_app_obj = Banking_Application()
        actual_client_details = banking_app_obj.searching_for_accounts_with_negative_balance()
        expected = testing_payloads.acc_neg_bal_exp
        self.assertEqual(expected,actual_client_details)

    def test_searching_by_firstname(self):
        banking_app_obj = Banking_Application()
        expected= testing_payloads.acc_searching_by_firstname
        actual_client= banking_app_obj.searching_by_firstname("Wilma")
        self.assertEqual(expected,actual_client)

    def test_searching_by_lastname(self):
        banking_app_obj = Banking_Application()
        expected = testing_payloads.acc_searching_by_lastname
        actual_client = banking_app_obj.searching_by_lastname("Huniwall")
        self.assertEqual(expected, actual_client)

    def test_searching_by_date_of_birth(self):
        banking_app_obj = Banking_Application()
        expected = testing_payloads.acc_searching_by_date_of_birth
        actual_client = banking_app_obj.searching_by_date_of_birth("10/04/1979")
        self.assertEqual(expected, actual_client)

    def test_retrieving_a_client(self):
        banking_app_obj = Banking_Application()
        expected_client_object = client_class(**testing_payloads.client_details)
        actual_response = banking_app_obj.retrieving_a_client("Gerald", "Smith", "15/12/1990")
        self.assertIsInstance(expected_client_object, type(actual_response))


