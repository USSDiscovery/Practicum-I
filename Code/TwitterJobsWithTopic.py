#!/usr/bin/python

from twitter import *
import re
import sys
import os
import os.path

reload(sys)
sys.setdefaultencoding('utf8')

def replace_all(text, topics):
    for i, j in topics.iteritems():
        text = text.replace(i, j)
    return text

topics = {'machine learning':'machine_learning',\
          'computer programmer':'computer_programmer',\
          'database administrator':'database_engineer',\
          'network engineer':'network_engineer',\
          'network administrator':'network_administrator',\
          'data scientist':'data_scientist',\
          'systems engineer':'systems_engineer',\
          'data analyst':'data_analyst',\
          'data architect': 'data_architect',\
          'etl architect':'etl_architect',\
          'web programmer':'web_programmer',\
          'automation engineer':'automation_engineer',\
          'data processing':'data_processing',\
          'application engineer':'application_engineer',\
          'software engineer':'software_engineer',\
          'software developer':'software_developer',\
          'information architect':'information_architect',\
          'security analyst':'security_analyst',\
          'business intelligence':'business_intelligence',\
          'enterprise architect':'enterprise_architect',\
          'solution architect':'solution_architect',\
          'data warehouse':'data_warehouse',\
          'information technology':'information_technology', \
          'machinelearning':'machine_learning',\
          'computerprogrammer':'computer_programmer',\
          'databaseadministrator':'database_engineer',\
          'networkengineer':'network_engineer',\
          'networkadministrator':'network_administrator',\
          'datascientist':'data_scientist',\
          'systemsengineer':'systems_engineer',\
          'dataanalyst':'data_analyst',\
          'dataarchitect': 'data_architect',\
          'etlarchitect':'etl_architect',\
          'webprogrammer':'web_programmer',\
          'automationengineer':'automation_engineer',\
          'dataprocessing':'data_processing',\
          'applicationengineer':'application_engineer',\
          'softwareengineer':'software_engineer',\
          'softwaredeveloper':'software_developer',\
          'informationarchitect':'information_architect',\
          'securityanalyst':'security_analyst',\
          'businessintelligence':'business_intelligence',\
          'enterprisearchitect':'enterprise_architect',\
          'solutionarchitect':'solution_architect',\
          'datawarehouse':'data_warehouse',\
          'informationtechnology':'information_technology'}

for file in os.listdir('/home/richard/TwitterDataPostClean'):

    print file

    fpostclean = open('/home/richard/TwitterDataPostClean/' + file, "r")

    fwithtopic = open('/home/richard/TwitterDataWithTopic/' + file, "w")

    line = fpostclean.readline()

    while line:

        line = replace_all(line, topics)

        #print(line)

        fwithtopic.write(line)

        line = fpostclean.readline()

    fwithtopic.close()

    fpostclean.close()
