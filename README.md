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
the database consists of 5 tables:
1: activity
2: heartrate
3: sleep
4: sleep_score
5: user

user_id, user_name e user age are common in all tables

![image](https://user-images.githubusercontent.com/70893659/169274077-604593aa-2a72-4ad5-8501-cef3966f9100.png)
calories - The top level time series for calories burned inclusive of BMR, tracked activity, and manually logged activities.
caloriesBMR - Value includes only BMR calories.
activityCalories - The number of calories burned during the day for periods of time when the user was active above sedentary level. This value is calculated minute by minute for minutes that fall within this criteria. This includes activity burned calories and BMR.


![image](https://user-images.githubusercontent.com/70893659/169274985-0b3d3158-7156-4e7b-b363-3846c2fa0b71.png)
activities-heart : datetime	Date of the heart rate log.
activities-heart : value : customHeartRateZone : caloriesOut	Number calories burned with the custom heart rate zone.
activities-heart : value : customHeartRateZone : max	Maximum range for the custom heart rate zone.
activities-heart : value : customHeartRateZone : min	Minimum range for the custom heart rate zone.
activities-heart : value : customHeartRateZone : minutes	Number minutes withing the custom heart rate zone.
activities-heart : value : customHeartRateZone : name	Name of the custom heart rate zone.
activities-heart : value : restingHeartRate	Resting heart rate value for the day. A sleep stage log is required to generate this value. When a classic sleep log is recorded, this value will be missing.

![image](https://user-images.githubusercontent.com/70893659/169275468-991347d9-9c0e-4bdb-bac0-596d3ea62c1d.png)
sleep : dateOfSleep	The date the sleep log ended.
sleep : duration	Length of the sleep in milliseconds.
sleep : efficiency	Calculated sleep efficiency score. This is not the sleep score available in the mobile application.
sleep : minutesAfterWakeup	The total number of minutes after the user woke up.
sleep : minutesAsleep	The total number of minutes the user was asleep.
sleep : minutesAwake	The total number of minutes the user was awake.
sleep : minutesToFallAsleep	The total number of minutes before the user falls asleep. This value is generally 0 for autosleep created sleep logs.


![image](https://user-images.githubusercontent.com/70893659/169276527-360d7d1e-be80-47fa-87a1-a06d5d25b72a.png)

unfortunately the sleep score is not obtainable through the fitbit API and therefore it is loaded into the database through a csv.

to get the csv you need to log in to the official fitbit website, and access your personal data. At this point it is necessary to download all the user's history and under the sleep folder there is the csv containing the sleep score.

![image](https://user-images.githubusercontent.com/70893659/169277107-45bd2563-f485-4fbf-8758-dc0d17d11387.png)

