# 1034 Project 2 - Farheen Mehmood

### <u>Overview of the project</u>
I have 3 different python files in this project clients, banking_application and CSV.

The clients class only has methods which will edit attribute that the client will have control over in a real life scenario. For example, the client should only be able to deposit and withdraw money, change title, first name, last name, date of birth, preferred pronouns and occupation. The client cannot have control over how much their overdraft limit is therefore the method to change overdraft limit is in the banking application class.

In my banking application class, I have 8 methods:
1. `__fetch_csv_dataframe()` : This is to fetch and return the dataframe which contains all the clients from the CSV file so that we can manipulate it in the banking application class. Within this method another method is called which exists in CSV file that put the clients in the CSV file into a dataframe. I have kept it private because this is the method I call in other methods so that I can manipulate the clients details.
2. `print_current_CSV_file()`: This is a method to print out the dataframe of clients once it has been fetched using the *__fetch_csv_dataframe()* method from the CSV file.
3. `__return_client_df_as_dict()`: This method will change a dataframe into a dictionary. This method is private as well because I only want to call within other methods within the class.
4. `retrieving_a_client()`: In this method, I retrieve a client by comparing the firstname, lastname and date of birth with other clients in the CSV dataframe.
5. `accounts_with_negative_balance()`: This method retrieves all clients which have a negative account balance from the csv dataframe. The method does not pass anything in the parameters.
6. `deleting_a_client()` : The methods compares the first_name, last_name and date_of_birth which is passed into the method with the clients in the CSV file and deletes that client. It then calls the refresh_csv_file method in the CSV class which will update the csv file.
7. `changing_overdraft_limits()`: Just like *deleting_a_client()*, first_name last_name and date_of_birth is passed into the method, however in this method, a new overdraft limit is also passed in. The firstname,lastname and date of birth is compared with the dataframe to find which client the user wants to edit. Then the overdraft limit is changed to the new overdraft limit which is passed into the method.
8. `adding_a_client()`: This will take a client dictionary as an argument and turn it into a dataframe. Then a concat method is used to join the csv dataframe and the dataframe of the new client together. Then the method *refresh_csv_file* is called to write the updated dataframe to the CSV file. 
9. `searching_by_firstname()`: This is a method which first check if the firstname passed in is equal to any of the firstnames in the CSV file. If there is a client with the matching firstname then all details for that specific client is returned. Otherwise, a print statement is run which states that a client with the passed firstname does not exist in the CSV file.
10. `searching_by_lastname()`: This method searches the dataframe of the CSV file for clients with the same lastname as the one passed into the method, if they match then all details of that client is returned. Otherwise, an else statement is run which will print an error saying that the client with the lastname inputted into the method doesn't exist.
11. `searching_by_date_of_birth()`: This method searches the dataframe of the CSV file for clients with the date of birth equal to the date of birth passed in the method. If there is no date of birth equal to the date of birth passed into the method, then a print statement is run which will state that a client with the date of birth passed into the method doesn't exist. Otherwise, details of all the clients with that date of birth are returned. 

Finally, I have a CSV class which has 2 methods. The first method creates a dataframe of the entire CSV file. This is so that I can manipulate the data in the file without directly interfering with the CSV file. Then to update the CSV file after changes have been made, I have another method which will replace the data in my CSV file with the data in my dataframe. I have called this method everytime a client has to be edited so that it will update in the CSV file as well.

I have a file called constants which I have made to store the file path of my CSV file so that if it happened to change, it can easily be changed throughout the code. This will prevent unnecessary errors.

For my unit testing, I have another file which tests the methods in my banking_application class however, I have also included methods of my client_class to test in this file. This is because a clients details should be altered when retrieved from the CSV file using the methods in the clients class.

I have also done error handling in all my classes to make sure that if incorrect information is passed into the parameters, then an error message prints out. I decided to use the *BaseException* error throughout my methods because it allows a wider scope of errors to be handled and outputted in the print statement as opposed to just one type of error.

<u>Testing Instructions</u>

For testing do not make any changes in the clients CSV file as my tests are based of the current content of the clients CSV file. The methods *changing_overdraft_limits*, *adding_a_client* and *deleting_a_client* do not have unit tests done for them as they directly make changes in the CSV file. So in order to see if those methods work, run the method from the main.py file.

### <u>Assumptions made when building the application</u>
I wanted to make this application as realistic as possible therefore I decided to have 3 separate classes which have different functionalities. Ideally, a client would not be able to change their overdraft limit or their date of birth, and they can only deposit or withdraw money from their account. A client class is responsible for editing only certain attributes e.g. clients only have control over editing title, firstname, lastname, pronouns and occupation. The bank will have control over the clients overdraft limits but the bank will not be able to change any of the clients personal details like firstname, lastname, occupation, preferred pronouns and title. The bank can add clients, delete clients, retrieve clients, change overdraft limits, search by firstname and lastname, search by date of birth, search by negative account balance and print out all clients. CSV class is responsible for just retrieving the csv file as a dataframe and then update the csv file once the data has been manipulated.
### <u>How to run the application</u>
1. python version 3.11
2. pandas
3. pip
### <u>Specific use case examples of how to run this application</u> 
<u> How to run methods in the banking application class</u>

1. *`print(BA_Obj.retrieving_a_client("Wilma","Huniwall","4/04/2000"))`*  this is an example of how retrieve a client. You have to use the object of the banking application class and call the *retrieving_a_client* method. When calling the method, pass through the firstname, lastname and date of birth. This is because the firstname, lastname and date of birth are compared with all clients in the CSV dataframe so that the correct client is retrieved. Finally, use the print statement to print out the client.
2. *`print(BA_Obj.searching_for_accounts_with_negative_balance())`* this is an example of how to retrieve negative balance. An object of the banking application is used to call this method as well however, for this method, nothing is required to pass through into the parameters. The print statement is used to print out the return of this method.
3. *`BA_Obj.deleting_a_client("Alice","Liddyard","8/09/1978")`* this is an example of how to delete a client from the CSV file. Call the method using the banking application object and pass through the firstname, lastname and date of birth of the client that is required to be deleted. Then to check if the client is deleted, you can use the *BA_Obj.print_current_CSV_file()* method to print out the CSV file in the form of a dataframe.
4. *`BA_Obj.changing_overdraft_limits("Skyler","Harrinson","2/07/1960","1560")`* this is an example of how to change the overdraft limits. First, call the method using the banking application object and pass in the firstname, lastname, date of birth and the amount you want the new overdraft limit to be. You can check if the overdraft limit has changed running the code *BA_Obj.print_current_CSV_file()*.
5. *`BA_Obj.adding_a_client(client_object.return_client_dict())`* First, a client object is made and all required data is filled out. This is called into the *return_client_dict()*. The return of this method is called into the *adding_a_client()* method. However, to be able to call this method, an object of the banking application class has to be made first.
6. *`print(BA_Obj.searching_by_firstname("Wilma"))`* To search by firstname, first make an object of the banking application class and use that to call the *searching_by_firstname()* method. Then pass the firstname of the client or clients that are required to be called in the parameter. Then use the print statement to print out all details of that specific client.
7. *`print(BA_Obj.searching_by_lastname("Huniwall"))`* To search by lastname, use an object of the banking application class to be able to call the method *searching_by_lastname()* and pass in the lastname of the client or clients that are needed to be called. Use the print statement to display all the details of the client.
8. *`print(BA_Obj.searching_by_date_of_birth("10/04/1979"))`* Search the date of birth through passing in the date of birth of the clients or client you want details on. Use the banking application object to call this method. The print statement will output all the details

<u> How to run the methods in the client class </u>

First have a dictionary of all the details of the client you want to add. Then make an object for the client class so that you can call the methods in that class. I used this dictionary to test the client class methods I have made. However, when *BA_Obj.retrieving_a_client("Wilma","Huniwall","4/04/2000")* is run for example, you can use a client from the CSV file and edit their details. The only way methods in the client class will be called is making an object of that class. Therefore, to edit details of "Wilma Huniwall" for example, a client class object should be made and the retrieved client should be passed as a parameter into the client class. Only then can the methods of the client class be used to alter details of the clients recieved from the CSV file.  

`client = {
        "title": 'Mr',
        "first_name": 'Gerald',
        "last_name": 'Smith',
        "preferred_pronouns": 'he/him',
        "date_of_birth": '15/12/1990',
        "occupation": 'Software Engineer',
        "account_balance": 100,
        "overdraft_limit": 10
    }`

`client_object = client_class(**client)`

1. `client_object.changing_title("Mrs")`  : This method is to change the title of the client. Simple call the method using the client class object and then pass in the new title in the parameter
2. `client_object.changing_first_name("Susan")` : This method is the change the first name of the client. Call the method using an object and pass in the new first name of the client.
3. `client_object.changing_last_name("Blunt")`: This method is the change the last name of the client. Call the method using an object and pass in the new last name of the client.
4. `client_object.changing_preferred_pronoun("she/her")`: This method is the change the preferred pronouns of the client. Call the method using an object and pass in the new preferred pronouns of the client.
5. `client_object.changing_occupation("Designer")`:This method is the change the occupation of the client. Call the method using an object and pass in the new occupation of the client.
6. `client_object.removing_in_account_balance(100)`: This method withdraws money from the account balance. If the amount removed is more than the account balance plus the overdraft limit then the account balance will go into negatives and an extra £5 is charged. The class object is used to call the method and the amount withdrawed is passed as a parameter.
7. `client_object.adding_in_account_balance(200)`: The class object will call the method and the deposit amount is passed into the parameter. Then the account balance and incremented by the deposit amount.

These methods are demonstrated in the main.py file. Simply remove the comment to see the method run.
