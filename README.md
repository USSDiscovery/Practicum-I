### Analyzing Information Technology Sentiment Through Twitter Data

#### Project Description
This project was completed for my Data Science Practicum I course. In this project I have attempted to combine my fascination with Twitter Data, my interest in Information Technology, and my interest in Data Engineering and Data Science. I have purposely put Data Engineering before Data Science as I first built an IT platform for me to work on and then used that platform to conduct aspects of Data Science to explore Information Technology through Twitter data.

#### Project Outcome
The intended outcome of this project is twofold:
1. Explore topics centered around Information Technology
2. Visualize Sentiment around Information Technology

#### IT Platform
My intent for this project was to run PySpark on Hadoop. For a previous project I ran a cluster of 3 virtual linux machines using my Windows laptop as the host machine. I found that this setup barely got me through the class. This time I decided to purchase, at auction, a dual core, 1TB hard drive, 16GB machine. On this machine I setup the following:

1. Ubuntu Host OS
2. Four Ubuntu Virtual Machines
3. Virtual machine 1 was used to collect tweets
4. Virtual machines 2 through 4 were setup as a hadoop cluster
5. VirtualBox, Ambari-Vagrant, Anaconda were used to setup the environment
6. The environment consists of PySpark running on a 3 node cluster, using Jupiter Notebooks

#### The Dataset
My dataset consists of tweets containing the following terms:
1. data
2. java
3. machine learning
4. iot
5. computer
6. computer programmer
7. database administrator
8. network engineer
9. network administrator
10. data scientist
11. systems
12. systems engineer
13. data analyst
14. technology
15. data architect
16. etl
17. etl architect
18. web programmer
19. automation engineer
20. data processing
21. devops
22. cloud
23. application engineer
24. software engineer
25. software developer
26. developer
27. information architect
28. programmer
29. security analyst
30. business intelligence
31. enterprise architect
32. solution architect
33. data warehouse
34. ai
35. robotics
36. information technology

My Tweets consisted of the following fields:

1. timetext
2. tweet_id
3. tweet_source
4. tweet_truncated
5. tweet_text
6. tweet_user_screen_name
7. tweet_user_id
8. tweet_user_location
9. tweet_user_description
10. tweet_user_followers_count
11. tweet_user_statuses_count
12. tweet_user_time_zone
13. tweet_user_geo_enabled
14. tweet_user_lang
15. tweet_coordinates_coordinates
16. tweet_place_country
17. tweet_place_country_code
18. tweet_place_full_name
19. tweet_place_name
20. tweet_place_type

For this project I really only needed the tweet_text but I wanted to bring back as much information that I could should I want to do time based analysis or utilize the geo fields to perhaps break down sentiment by location.

#### Data Cleaning
Initially the only data cleaning I did was to within each field remove commas and newlines. I did this thinking that with free form fields users could add commas and newlines. Little did I know that this was just the beginning. Thinking back, I really should have known that more data cleaning up front would have been needed.

*tweet_text = tweet_text.replace(',',' ').replace('\n', ' ')*

In addition, I only pulled back english tweets or so I thought.

*isnull(tweet["user"]["lang"]) == "en"*

After pulling back approximately 13 million tweets I realized further cleaning would be needed. The first thing I did was update my original Python script with addition cleaning and then I created another script to clean the data I had already retrieved. I adjusted the original script to only include letters, numbers, and spaces. In addition, I am expecting 20 fields. I also added a line of code to only include records that had 20 fields:

*tweet_text = re.sub('[^ a-zA-Z0-9]', '', tweet_text)*

*if tweet_line_len == 20:
     twitter_jobs_raw_data_file.write(tweet_line + '\n')*

The second script simply read the previously accumulated files, applied the above cleaning, and wrote the cleaned files back out to a different directory.

The last bit of data cleaning needed was discovered further into the project. The topic modeler used, LDA, would only model single word topics. I had both single and multiple word search terms. I wanted to make sure that my multiple word search terms would be candidates for topics. In order to accomplish this I wrote a third script that read all previously cleaned data and added an underscore to all of my multiple word search terms:

*machine learning became machine_learning*

#### Import Needed Libraries
The following libraries were used to build a Spark Context on my Hadoop Cluster, import the tweet data, topic model the tweet data, conduct sentiment analysis on the tweet data, and visualize that sentiment analysis:


#### Exploratory Data analysis
While I only pulled back tweets with the above search terms, I still wanted to pick out topics from those tweets. I used MLIB's LDA to achieve this.
