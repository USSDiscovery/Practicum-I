#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-stream-format:
#  - ultra-real-time stream of twitter's public timeline.
#    does some fancy output formatting.
#  - Taken from github python-twitter-examples/twitter-stream-search.py
#-----------------------------------------------------------------------

from twitter import *
import re
import sys
import os.path

reload(sys)
sys.setdefaultencoding('utf8')

na = ''
delimiter = ','
tweet_line = ''

header = 'timetext' + delimiter +\
         'tweet_id' + delimiter +\
         'tweet_source' + delimiter +\
         'tweet_truncated' + delimiter +\
         'tweet_text' + delimiter +\
         'tweet_user_screen_name' + delimiter +\
         'tweet_user_id' + delimiter +\
         'tweet_user_location' + delimiter +\
         'tweet_user_description' + delimiter +\
         'tweet_user_followers_count' + delimiter +\
         'tweet_user_statuses_count' + delimiter +\
         'tweet_user_time_zone' + delimiter +\
         'tweet_user_gio_enabled' + delimiter +\
         'tweet_user_lang' + delimiter +\
         'tweet_coordinates_coordinates' + delimiter +\
         'tweet_place_country' + delimiter +\
         'tweet_place_country_code' + delimiter +\
         'tweet_place_full_name' + delimiter +\
         'tweet_place_name' + delimiter +\
         'tweet_place_type'

# output_file_dir = argv[1]
output_file_dir = '/home/richard/TwitterJobsRaw'

def isnull(check_tweet):
    if check_tweet is None:
        check_tweet = na
    return check_tweet

# Job Terms
# machine learning engineer
# iot architect
# quantum programmer
# computer support specialist
# database administrator
# network administrator
# data scientist
# data engineer
# java programmer
# computer systems analyst

# Initialize file parameter
rawdatatimestamp = '2000010101'

search_term = "data,\
               java,\
               machine learning,\
               iot,\
               computer,\
               computer programmer,\
               database administrator,\
               network engineer,\
               network administrator,\
               data scientist,\
               systems,\
               systems engineer,\
               data analyst,\
               technology,\
               data architect,\
               etl,\
               etl architect,\
               web programmer,\
               automation engineer,\
               data processing,\
               devops,\
               cloud,\
               application engineer,\
               software engineer,\
               software developer,\
               developer,\
               information architect,\
               programmer,\
               security analyst,\
               business intelligence,\
               enterprise architect,\
               solution architect,\
               data warehouse,\
               ai,\
               robotics,\
               information technology"

#-----------------------------------------------------------------------
# import a load of external features, for text display and date handling
# you will need the termcolor module:
#
# pip install termcolor
#-----------------------------------------------------------------------
from time import strftime
from textwrap import fill
from termcolor import colored
from email.utils import parsedate

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"])
stream = TwitterStream(auth = auth, secure = True)

#-----------------------------------------------------------------------
# iterate over tweets matching this filter text
#-----------------------------------------------------------------------
tweet_iter = stream.statuses.filter(track = search_term)

pattern = re.compile("%s" % search_term, re.IGNORECASE)

for tweet in tweet_iter:

    tweet_line = ''

    if 'user' in tweet:

        if isnull(tweet["user"]["lang"]) == "en":

            tweet_created_at = isnull(tweet["created_at"])
            tweet_id = isnull(tweet["id"])
            tweet_source = isnull(tweet["source"])
            tweet_truncated = isnull(tweet["truncated"])

            if tweet_truncated:
                tweet_truncated = 'True'
                if isnull(tweet["extended_tweet"]) <> na:
                    tweet_text = isnull(tweet["extended_tweet"]["full_text"])
                else:
                    tweet_text = na
            else:
                tweet_truncated = 'False'
                tweet_text = isnull(tweet["text"])

            if isnull(tweet["user"]) <> na:
                tweet_user_screen_name = isnull(tweet["user"]["screen_name"])
                tweet_user_id = isnull(tweet["user"]["id"])
                tweet_user_location = isnull(tweet["user"]["location"])
                tweet_user_description = isnull(tweet["user"]["description"])
                tweet_user_followers_count = isnull(tweet["user"]["followers_count"])
                tweet_user_friends_count = isnull(tweet["user"]["friends_count"])
                tweet_user_statuses_count = isnull(tweet["user"]["statuses_count"])
                tweet_user_time_zone = isnull(tweet["user"]["time_zone"])
                tweet_user_geo_enabled = isnull(tweet["user"]["geo_enabled"])
                if tweet_user_geo_enabled:
                    tweet_user_geo_enabled = 'True'
                else:
                    tweet_user_geo_enabled = 'False'
                tweet_user_lang = isnull(tweet["user"]["lang"])
            else:
                tweet_user_screen_name = na
                tweet_user_id = na
                tweet_user_location = na
                tweet_user_description = na
                tweet_user_followers_count = na
                tweet_user_friends_count = na
                tweet_user_statuses_count = na
                tweet_user_time_zone = na
                tweet_user_geo_enabled = na
                tweet_user_lang = na

            if isnull(tweet["coordinates"]) <> na:
                tweet_coordinates_coordinates = isnull(tweet["coordinates"]["coordinates"])
            else:
                tweet_coordinates_coordinates = na

            if isnull(tweet["place"]) <> na:
                tweet_place_country = tweet.get('place', na).get('country', na)
                tweet_place_country_code = tweet.get('place', na).get('country_code', na)
                tweet_place_full_name = tweet.get('place', na).get('full_name', na)
                tweet_place_name = tweet.get('place', na).get('name', na)
                tweet_place_type = tweet.get('place', na).get('place_type', na)
            else:
                tweet_place_country = na
                tweet_place_country_code = na
                tweet_place_full_name = na
                tweet_place_name = na
                tweet_place_type = na

            # turn the date string into a date object that python can handle
            timestamp = parsedate(tweet_created_at)

            # now format this nicely into HH:MM:SS format
            timetext = strftime("%Y:%m:%d:%H:%M:%S", timestamp)
            rawdatatimestampcurrent = strftime("%Y%m%d%H", timestamp)

            # create new file if it does not already exist
            if rawdatatimestamp <> rawdatatimestampcurrent:

                if rawdatatimestamp <> '2000010101':
                    twitter_jobs_raw_data_file.close()

                rawdatatimestamp = rawdatatimestampcurrent
                twitter_jobs_filename = output_file_dir + '/' + rawdatatimestamp + '_TwitterJobsRawData.txt'

                if os.path.isfile(twitter_jobs_filename):
                    twitter_jobs_raw_data_file = open(twitter_jobs_filename, "a")
                    print "%s exists" % twitter_jobs_raw_data_file
                else:
                    twitter_jobs_raw_data_file = open(twitter_jobs_filename, "w")
                    twitter_jobs_raw_data_file.write(header + '\n')
                    print "%s file created" % twitter_jobs_filename

            # colour our tweet's time, user and text
            time_colored = colored(timetext, color = "white", attrs = [ "bold" ])
            user_colored = colored(tweet_user_screen_name, "green")
            text_colored = tweet_text

            # replace each instance of our search terms with a highlighted version
            search_term_list = search_term.split(",")
            for term in search_term_list:
                #text_colored = pattern.sub(colored(search_term.upper(), "yellow"), text_colored)
                text_colored = pattern.sub(colored(term.upper(), "yellow"), text_colored)

            # add some indenting to each line and wrap the text nicely
            indent = " " * 11
            text_colored = fill(text_colored, 80, initial_indent = indent, subsequent_indent = indent)

            # build output line
            #timetext = timetext.replace(',',' ').replace('\n', ' ')
            #tweet_id = str(tweet_id).replace(',', '').replace('\n', ' ')
            #tweet_source = tweet_source.replace(',',' ').replace('\n', ' ')
            #tweet_truncated = tweet_truncated.replace(',',' ').replace('\n', ' ')
            #tweet_text = tweet_text.replace(',',' ').replace('\n', ' ')
            #tweet_user_screen_name = tweet_user_screen_name.replace(',',' ').replace('\n', ' ')
            #tweet_user_id = str(tweet_user_id).replace(',', '').replace('\n', ' ')
            #tweet_user_location = tweet_user_location.replace(',',' ').replace('\n', ' ')
            #tweet_user_description = tweet_user_description.replace(',',' ').replace('\n', ' ')
            #tweet_user_followers_count = str(tweet_user_followers_count).replace(',','').replace('\n', ' ')
            #tweet_user_statuses_count = str(tweet_user_statuses_count).replace(',','').replace('\n', ' ')
            #tweet_user_time_zone = tweet_user_time_zone.replace(',',' ').replace('\n', ' ')
            #tweet_user_geo_enabled = tweet_user_geo_enabled.replace(',',' ').replace('\n', ' ')
            #tweet_user_lang = tweet_user_lang.replace(',',' ').replace('\n', ' ')
            #tweet_coordinates_coordinates = str(tweet_coordinates_coordinates).replace(',','').replace('\n', ' ')
            #tweet_place_country = tweet_place_country.replace(',',' ').replace('\n', ' ')
            #tweet_place_country_code = tweet_place_country_code.replace(',',' ').replace('\n', ' ')
            #tweet_place_full_name = tweet_place_full_name.replace(',',' ').replace('\n', ' ')
            #tweet_place_name = tweet_place_name.replace(',',' ').replace('\n', ' ')
            #tweet_place_type = tweet_place_type.replace(',',' ').replace('\n', ' ')

            timetext = re.sub('[^ a-zA-Z0-9]', '', timetext)
            tweet_id = re.sub('[^ a-zA-Z0-9]', '', str(tweet_id))
            tweet_source = re.sub('[^ a-zA-Z0-9]', '', tweet_source)
            tweet_truncated = re.sub('[^ a-zA-Z0-9]', '', tweet_truncated)
            tweet_text = re.sub('[^ a-zA-Z0-9]', '', tweet_text)
            tweet_user_screen_name = re.sub('[^ a-zA-Z0-9]', '', tweet_user_screen_name)
            tweet_user_id = re.sub('[^ a-zA-Z0-9]', '', str(tweet_user_id))
            tweet_user_location = re.sub('[^ a-zA-Z0-9]', '', tweet_user_location)
            tweet_user_description = re.sub('[^ a-zA-Z0-9]', '', tweet_user_description)
            tweet_user_followers_count = re.sub('[^ a-zA-Z0-9]', '', str(tweet_user_followers_count))
            tweet_user_statuses_count = re.sub('[^ a-zA-Z0-9]', '', str(tweet_user_statuses_count))
            tweet_user_time_zone = re.sub('[^ a-zA-Z0-9]', '', tweet_user_time_zone)
            tweet_user_geo_enabled = re.sub('[^ a-zA-Z0-9]', '', tweet_user_geo_enabled)
            tweet_user_lang = re.sub('[^ a-zA-Z0-9]', '', tweet_user_lang)
            tweet_coordinates_coordinates = re.sub('[^ a-zA-Z0-9]', '', str(tweet_coordinates_coordinates))
            tweet_place_country = re.sub('[^ a-zA-Z0-9]', '', tweet_place_country)
            tweet_place_country_code = re.sub('[^ a-zA-Z0-9]', '', tweet_place_country_code)
            tweet_place_full_name = re.sub('[^ a-zA-Z0-9]', '', tweet_place_full_name)
            tweet_place_name = re.sub('[^ a-zA-Z0-9]', '', tweet_place_name)
            tweet_place_type = re.sub('[^ a-zA-Z0-9]', '', tweet_place_type)

            tweet_line = tweet_line + timetext
            tweet_line = tweet_line + delimiter + tweet_id
            tweet_line = tweet_line + delimiter + tweet_source
            tweet_line = tweet_line + delimiter + tweet_truncated
            tweet_line = tweet_line + delimiter + tweet_text
            tweet_line = tweet_line + delimiter + tweet_user_screen_name
            tweet_line = tweet_line + delimiter + tweet_user_id
            tweet_line = tweet_line + delimiter + tweet_user_location
            tweet_line = tweet_line + delimiter + tweet_user_description
            tweet_line = tweet_line + delimiter + tweet_user_followers_count
            tweet_line = tweet_line + delimiter + tweet_user_statuses_count
            tweet_line = tweet_line + delimiter + tweet_user_time_zone
            tweet_line = tweet_line + delimiter + tweet_user_geo_enabled
            tweet_line = tweet_line + delimiter + tweet_user_lang
            tweet_line = tweet_line + delimiter + tweet_coordinates_coordinates
            tweet_line = tweet_line + delimiter + tweet_place_country
            tweet_line = tweet_line + delimiter + tweet_place_country_code
            tweet_line = tweet_line + delimiter + tweet_place_full_name
            tweet_line = tweet_line + delimiter + tweet_place_name
            tweet_line = tweet_line + delimiter + tweet_place_type

            # now output our tweet
            print "(%s) @%s %s" % (time_colored, user_colored, tweet_user_lang)
            print "%s" % (tweet_truncated)
            print "%s" % (text_colored)
            tweet_line_len = tweet_line.count(",") + 1
            print "%d" % (tweet_line_len)

            if tweet_line_len == 20:
                twitter_jobs_raw_data_file.write(tweet_line + '\n')