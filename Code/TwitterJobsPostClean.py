#!/usr/bin/python

from twitter import *
import re
import sys
import os
import os.path

reload(sys)
sys.setdefaultencoding('utf8')

for file in os.listdir('/home/richard/TwitterDataPreClean'):
    print file

    fpreclean = open('/home/richard/TwitterDataPreClean/' + file, "r")

    fpostclean = open('/home/richard/TwitterDataPostClean/' + file, "w")

    line = fpreclean.readline()

    while line:

        valid = 1

        numfields = len(line.split(','))

        line = re.sub('[^ ,a-zA-Z0-9]', '', line)

        if numfields == 20:

            #print "%d - %s" % (numfields, line)

            fpostclean.write(line + '\n')

        line = fpreclean.readline()

    fpreclean.close()

    fpostclean.close()
