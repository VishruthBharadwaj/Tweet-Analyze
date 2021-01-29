
import tweepy
import dataset
import csv

import mysql.connector

import json

import pandas as pd

'''
consumer_key = "sAcCBILBdhdfNuRmFuzZFZLCK"
consumer_secret = "crrWltPZt3cCv1G8RzCRDlRYPemWYWQgIReGJAAniOU4pOL4fn"
access_key = "1353293981384232965-QKR7IaxJoUfOkAwmQkCQC9PuSsihYj"
access_secret = "TJny0NFXeUH31mmthW55j5J3EjBZvzaeMbloo2xYKRTG4"'''



consumer_key = "GukVEQqENGxOzKItNQH8WzLnV"
consumer_secret = "y8fnCnbAvVpenm6tG7vDc6EFYnuE6fI6gS2ag0qhAWvqhLMyGj"
access_key = "76901740-uobZSTxtFQd8mVtNgwWcLHw4IrW8UoEI9xInsKfoQ"
access_secret = "jYC0L0fZVU4lHhc2TOWt35dFHyRy83bbPDAm8hZVi9Tw5"




class StreamListener(tweepy.StreamListener):

    def on_status(self, status):

        print(status.id_str)
        if status.retweeted:
            return
        name = status.user.screen_name
        created = status.created_at
        
        loc = status.user.location
        coords = status.coordinates
        followers = status.user.followers_count
        description = status.user.description
        text_ = status.text

        con = mysql.connector.connect(host = 'localhost', database='twitter', user='root', password = '')

        cursor = con.cursor(buffered=True)
        query = """INSERT INTO twitterdata (name, created, loc, coords, followers, description, text_) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        

        cursor.execute(query, (name, created, loc, coords, followers, description, text_))


        tablesearch_query =f"INSERT INTO trend_data (timesec, counts) SELECT created , count('{data}') from twitterdata group by created"
       
        cursor.execute(tablesearch_query)
        try:
            con.commit()

                
        except:
   # Rolling back in case of error
            con.rollback()
        
        con.close()

    def on_error(self, status_code):
        if status_code == 420:
          
            return False


        




if __name__ == "__main__":

    # complete authorization and initialize API endpoint
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)


    # initialize stream
    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended')
   
       
    tagb=input('Enter the word you want search in twitter: ')


    tags = tagb.split(sep=",")
    
    data=input('What u want to search inside database table: ')
    
   
    
    
    stream.filter(track=tags)

