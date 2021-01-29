# Twitter Analyzer


# First Switch MySQL Server and redirect to panel.

Install tweepy, mysql.connector, pandas.

Used XamppServer panel and redirect to   http://127.0.0.1/phpmyadmin/


# Before running the script please check the following data inside Stream.py:


 In StreamListener() have imported StreamListener and status for actual streaming data.


# Script will fetch following details:


1) Name of the user

2) Tweet created date and time

3) Location of user

4) Coordinates of user

5) Followers count 

6) Description of user profile

7) Text tweeted




# Connected to MySQL and have created DB as twitter and table name as twitterdata.


# Mysql server details (host = 'localhost', database='twitter', user='root', password = '')

# Column names : 

1) name 

2) created

3) loc 

4) coords 

5) followers 

6) description

7) text_



# If you run the script inside your MySql account please create DB named as twitter and table name as twitter data and column names are as follow:

1)name (varchar)

2)created (varchar)

3)loc  (varchar)

4)coords (int)

5)followers (int)

6)description (varchar)

7)text_ (varchar)


# Also for count of words in each second irrespective of users are fetched inside table named as twitter_count and column names as timesec and counts.

