# fitbit_api_database
this application automates the insertion of data obtained through the fitbit API and inserts them into a mysql database

# befor start
To use the Fitbit APIs, you need to have a Fitbit developer account. To create a developer account :

1 : Go to https://accounts.fitbit.com/signup to register for a fitbit.com account. The email address must be valid to complete the verification process. An existing fitbit.com account can be used.
A verification email will be sent to the user requesting a response.
2 : Once the email address is verified, the user will be able to access https://dev.fitbit.com/apps to register new applications used to query the Web APIs.

after logging in, click on register a new app and fill in the fields : 

![Cattura2](https://user-images.githubusercontent.com/70893659/169269490-7872c5e7-53ab-4ac9-8c5f-a9e5b0152f61.PNG)

the important fields are the application name and Redirect URL (which must be http://127.0.0.1:8080/)

Once the application is created, OAuth 2.0 Client ID and Client Secret will be provided, which are required for communication with the API.

![auth](https://user-images.githubusercontent.com/70893659/169270963-3146ed59-5c5a-481e-af7f-120eb464e953.png)

# how programs work 
Atart the main.py program and enter the client id and the client secret, then you will be asked to enter the start date and the end date of the period for which you want to save the data (maximum recommended interval one year).
After starting, the program will download all available data and insert them into the database

# Database
